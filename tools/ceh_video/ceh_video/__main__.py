"""Public CLI; structured results on stdout, measured progress on stderr."""
import argparse, json, os, sys
from .common import Project, read, write

def emit(row):
    print(json.dumps(row),file=sys.stderr,flush=True)

def main():
    parser=argparse.ArgumentParser(prog='ceh-video')
    parser.add_argument('--project');parser.add_argument('--json',action='store_true');parser.add_argument('--plain',action='store_true');sub=parser.add_subparsers(dest='command',required=True)
    init=sub.add_parser('init');init.add_argument('--reference',required=True);init.add_argument('--workspace',required=True)
    sub.add_parser('preflight');plan=sub.add_parser('plan');plan.add_argument('--target',default='package');plan.add_argument('--explain',action='store_true')
    run=sub.add_parser('run');run.add_argument('--target',default='package');run.add_argument('--resume',action='store_true');run.add_argument('--force',action='append',default=[])
    sub.add_parser('status');rev=sub.add_parser('review');rev.add_argument('--chapter');rev.add_argument('--findings');rev.add_argument('--reviewer',default='agent');rev.add_argument('--audio',action='store_true');rev.add_argument('--encoded',action='store_true');rev.add_argument('--item');rev.add_argument('--disposition');rev.add_argument('--evidence')
    args=parser.parse_args()
    from .progress import Progress
    progress=Progress(args.plain)
    try:
        if args.command=='init':
            from .initialize import initialize
            result=initialize(args.reference,args.workspace,progress)
        else:
            if not args.project:parser.error('--project is required')
            p=Project(args.project);os.environ['CEH_VIDEO_PROJECT']=str(p.root)
            if args.command=='preflight':
                from .preflight import preflight
                result=preflight(p)
            elif args.command=='plan':
                from .graph import planning
                rows=planning(p,args.target);result={'target':args.target,'run':sum(r['action']=='run' for r in rows),'reuse':sum(r['action']=='reuse' for r in rows),'nodes':rows}
            elif args.command=='run':
                from .runner import run
                result=run(p,args.target,args.force,progress)
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
