"""Three paired native warm comparisons; excerpt only, fixed runtime and voice bytes."""
from pathlib import Path
import json,os,shutil,subprocess,sys,time
from datetime import datetime,timezone
from ceh_video.common import Project,read,sha,write
from ceh_video.review import record
HERE=Path(__file__).resolve().parent
WORK=Path('/home/jnlngx10/Videos/longform-round2-2026-10-22')
ENGINE=Path(__file__).resolve().parents[4]/'tools/ceh_video'
BASELINE=WORK/'baseline/ceh_video'

def main():
    report_path=HERE/'media-results.json'
    if report_path.exists():raise RuntimeError('Run already recorded')
    p=Project(WORK/'media-optimized/project')
    findings='Inspected ten newly captured native states in contact-01/02: S01 Chinese headings, captions and paper-image panel stay separated; S05 hold has four neutral options and timer, with C highlighted only after the hold. Sampled states only; human listening and full-film watching remain pending.'
    record(p,'C01',findings)
    baseline=WORK/'media-baseline'
    shutil.copytree(p.root.parent,baseline,symlinks=True,ignore=shutil.ignore_patterns('.production'))
    report={'study_id':'longform-storage-round2','experiment_id':'mandarin-native-reuse-2026-10-22',
            'created_at':datetime.now(timezone.utc).isoformat(),'timezone':'Asia/Taipei',
            'execution_status':'running','runtime_validity':'pending','gate_outcome':'pending',
            'source_scenes':['S01','S05'],'duration_seconds':sum(p.audio(s['id'])['duration'] for s in p.scenes),
            'runtime':p.profile['runtime'],'output':p.profile['output'],'voice':p.profile['voice'],
            'source_audio_sha256':{s['id']:sha(p.root/'assets/voice'/f'{s["id"]}.wav') for s in p.scenes},
            'baseline_engine':str(BASELINE),'optimized_engine':str(ENGINE),
            'scope':'Native two-scene excerpt; cold means absent encoded-media receipt, not OS cache flush. No full-film speed estimate.',
            'runs':[]}
    write(report_path,report)
    def run(arm,phase,stage):
        root=WORK/('media-'+arm)/'project';engine=BASELINE if arm=='baseline' else ENGINE
        env=os.environ.copy();env['PYTHONPATH']=str(engine)
        log=WORK/f'{arm}-{phase}-{stage.replace(":","-")}.log'
        start=time.monotonic()
        with log.open('w') as out:
            proc=subprocess.run([sys.executable,str(HERE/'media_stage.py'),str(root),stage],env=env,stdout=out,stderr=subprocess.STDOUT)
        result={'arm':arm,'phase':phase,'stage':stage,'wall_seconds':time.monotonic()-start,'log':str(log),'log_sha256':sha(log),'exit_code':proc.returncode}
        report['runs'].append(result);write(report_path,report)
        print(json.dumps(result),flush=True)
        if proc.returncode:raise RuntimeError('Native stage failed: '+str(log))
        return result
    try:
        for arm in ['baseline','optimized']:
            for stage in ['host','render:C01','master','checks']:run(arm,'cold',stage)
        # Independent baseline/optimized outputs prevent a baseline encode from
        # overwriting the optimized artifact whose reuse is being measured.
        for pair in range(1,4):
            for arm in ['baseline','optimized']:
                root=WORK/('media-'+arm);movie=root/'output'/p.profile['master_filename'];chapter=root/'output/chapters/C01.mp4'
                before={str(f):[sha(f),f.stat().st_mtime_ns] for f in [movie,chapter]}
                for stage in ['host','render:C01','master','checks']:run(arm,f'warm-{pair}',stage)
                if arm=='optimized':
                    assert before=={str(f):[sha(f),f.stat().st_mtime_ns] for f in [movie,chapter]},'Warm reuse rewrote encoded media'
        # A local authored change must invalidate chapter reuse and actually encode.
        source=p.root/'compositions/S01.html';source.write_text(source.read_text()+'\n<!-- local revision for reuse invalidation -->\n')
        run('optimized','local-change','host')
        # Native captures are unchanged pixels; bind freshly checked current hosts.
        from ceh_video.mandarin import hf_check
        hf_check(p,p.root/'chapters/C01',[20,64.2,64.9],'local-change-check.json',lambda row:None)
        write(p.qa/'C01-checked-fingerprint.json',{'sha256':p.chapter_inputs('C01'),'status':'checked_visual_review_pending'})
        record(p,'C01',findings+' Local revision is an HTML comment; native check rerun, captured pixel assets unchanged.')
        before=(p.output/'chapters/C01.mp4').stat().st_mtime_ns
        run('optimized','local-change','render:C01')
        assert (p.output/'chapters/C01.mp4').stat().st_mtime_ns!=before
        run('optimized','local-change','master');run('optimized','local-change','checks')
        for sid,h in report['source_audio_sha256'].items():assert sha(p.root/'assets/voice'/f'{sid}.wav')==h
        report.update(execution_status='LIVE_FULL_COMPLETED',runtime_validity='valid',gate_outcome='passed',
                      decision='Native excerpt reuse passed; no full-film speed or human acceptance claim')
    except BaseException as exc:
        report.update(execution_status='failed',gate_outcome='failed',error=repr(exc));raise
    finally:write(report_path,report)
if __name__=='__main__':main()
