"""Public CLI; structured results on stdout, measured progress on stderr."""
import argparse, json, os, sys
from .common import Project, read, write

def emit(row):
    print(json.dumps(row),file=sys.stderr,flush=True)

def main():
    parser=argparse.ArgumentParser(prog='ceh-video')
    parser.add_argument('--project');parser.add_argument('--json',action='store_true');parser.add_argument('--plain',action='store_true');sub=parser.add_subparsers(dest='command',required=True)
    init=sub.add_parser('init');init.add_argument('--reference',required=True);init.add_argument('--workspace',required=True);init.add_argument('--legacy',action='store_true',help='Explicit historical v1.0 reconstruction only')
    migrate=sub.add_parser('migrate');migrate.add_argument('--reference',required=True);migrate.add_argument('--workspace',required=True)
    for command in (init,migrate):
        command.add_argument('--audio-policy',choices=['ceh-en-v1.1','ceh-en-v1.2'],default='ceh-en-v1.2',help='New work defaults to v1.2; select v1.1 only for historical reproduction')
    engineering=sub.add_parser('engineering');engineering.add_argument('--stage',choices=['audio','verify-audio','align','build','aac-audit','render-representatives'],required=True)
    engineering.add_argument('--run-kind',choices=['migration','routine','retry'],default='migration')
    engineering.add_argument('--parent-run')
    sub.add_parser('preflight');plan=sub.add_parser('plan');plan.add_argument('--target',default='package');plan.add_argument('--explain',action='store_true')
    run=sub.add_parser('run');run.add_argument('--target');run.add_argument('--intent',choices=['iteration','release']);run.add_argument('--run-kind',choices=['migration','routine','retry','delivery','benchmark'],default='routine');run.add_argument('--parent-run');run.add_argument('--resume',action='store_true');run.add_argument('--force',action='append',default=[])
    qa=sub.add_parser('qa');qa.add_argument('--scope',choices=['changed','representative','full'],required=True);qa.add_argument('--precheck',action='store_true')
    qa.add_argument('--run-kind',choices=['migration','routine','retry'],default='routine');qa.add_argument('--parent-run')
    package=sub.add_parser('package');package.add_argument('--plan',action='store_true')
    report=sub.add_parser('report');report.add_argument('--run',required=True)
    sub.add_parser('restore')
    sub.add_parser('status');rev=sub.add_parser('review');rev.add_argument('--chapter');rev.add_argument('--findings');rev.add_argument('--reviewer',default='agent');rev.add_argument('--audio',action='store_true');rev.add_argument('--encoded',action='store_true');rev.add_argument('--item');rev.add_argument('--disposition');rev.add_argument('--evidence')
    args=parser.parse_args()
    if args.command=='run':
        # Route termination through the existing child cleanup and attempt ledger.
        # SIGKILL and host loss still require explicit interrupted-run recovery.
        import signal
        def terminate(signum, frame):
            raise KeyboardInterrupt('Received SIGTERM')
        signal.signal(signal.SIGTERM, terminate)
    from .progress import Progress
    progress=Progress(args.plain)
    try:
        if args.command=='migrate':
            from .engineering import migrate
            result=migrate(args.reference,args.workspace,progress,args.audio_policy)
        elif args.command=='init':
            if args.legacy:
                from .initialize import initialize
                result=initialize(args.reference,args.workspace,progress)
            else:
                from .engineering import migrate
                result=migrate(args.reference,args.workspace,progress,args.audio_policy)
        else:
            if not args.project:parser.error('--project is required')
            p=Project(args.project);os.environ['CEH_VIDEO_PROJECT']=str(p.root)
            if args.command=='engineering':
                from .engineering import run
                from .run_record import RunRecord
                record=RunRecord(p,'engineering:'+args.stage,args.run_kind,args.parent_run);p.run_record=record
                def observed(row):record.event(row);progress(row)
                try:
                    result=run(p,args.stage,observed)
                except BaseException as exc:
                    record.finish('interrupted' if isinstance(exc,KeyboardInterrupt) else 'failed',error=str(exc))
                    raise
                else:result['attempt']=record.finish('completed',stage_result=result.copy())
                finally:del p.run_record
            elif args.command=='preflight':
                from .preflight import preflight
                result=preflight(p)
            elif args.command=='plan':
                from .graph import planning
                rows=planning(p,args.target);result={'target':args.target,'run':sum(r['action']=='run' for r in rows),'reuse':sum(r['action']=='reuse' for r in rows),'nodes':rows}
            elif args.command=='run':
                from .runner import run
                target=args.target or ('package' if (args.intent or p.profile.get('default_intent','release'))=='release' else 'checks')
                if args.intent=='iteration' and target=='package':raise ValueError('Use release intent for a complete archive')
                result=run(p,target,args.force,progress,args.run_kind,args.parent_run)
            elif args.command=='qa':
                from .qa import execute
                result=execute(p,args.scope,args.precheck,progress,args.run_kind,args.parent_run)
            elif args.command=='package':
                from .packaging import inventory
                if not args.plan:raise ValueError('Use run --intent release to create a verified archive')
                result=inventory(p)
            elif args.command=='restore':
                from .packaging import restore_hosts
                from .delivery import restore_packaged_audio_cache
                result=dict(audio=restore_packaged_audio_cache(p),hosts=restore_hosts(p))
            elif args.command=='report':
                if __import__('pathlib').Path(args.run).name!=args.run:raise ValueError('Invalid run ID')
                result=read(p.qa/'runs'/args.run/'summary.json')
            elif args.command=='status':
                result={'nodes':[read(f) for f in sorted((p.state/'processes').glob('*.json'))],'human_acceptance':'pending'}
            else:
                from .review import audio_queue,audio_decision,record,record_encoded
                if args.item:
                    audio_decision(p,args.item,args.disposition,args.reviewer,args.evidence or '');result={'recorded':args.item}
                elif args.audio:result=audio_queue(p)
                elif args.encoded:result=record_encoded(p,args.findings or '')
                elif args.chapter and args.findings:result=record(p,args.chapter,args.findings,args.reviewer)
                else:raise ValueError('Use --audio or --chapter with concrete --findings')
        print(json.dumps(result),flush=True)
    except (Exception,KeyboardInterrupt) as exc:
        print(json.dumps({'status':'interrupted' if isinstance(exc,KeyboardInterrupt) else 'failed','error':str(exc)}),flush=True)
        return 130 if isinstance(exc,KeyboardInterrupt) else getattr(exc,'exit_code',1)
    return 0

if __name__=='__main__':sys.exit(main())
