"""Align/compile ready scenes without waiting for presentation-order predecessors."""
import argparse,json,os,subprocess,sys,time
from ceh_video.common import Project,read
from ceh_video.run_record import RunRecord
parser=argparse.ArgumentParser();parser.add_argument('--project',required=True);parser.add_argument('--parent-run',required=True);args=parser.parse_args();p=Project(args.project);record=RunRecord(p,'M11:ready-scene-alignment','retry',args.parent_run);env=p.environment();pending=set(p.by_id)
try:
 while pending:
  ready=[sid for sid in pending if (p.root/'data'/f'{sid}.audio.json').is_file()]
  if not ready:
   state=read(p.qa/'narration-process.json')
   if state['status']!='running':raise RuntimeError('Narration ended with missing scenes: '+','.join(sorted(pending)))
   os.kill(state['pid'],0);time.sleep(3);continue
  for sid in sorted(ready,key=lambda s:-p.audio(s)['samples']):
   for stage in ['force_align','build_film']:
    node=stage+':'+sid;started=time.monotonic();record.event(dict(phase='node_start',node=node))
    with (p.qa/(stage+'-'+sid+'.log')).open('a') as log:
     result=subprocess.run([sys.executable,'-m','ceh_video.worker',stage,'--scene',sid],env=env,stdout=log,stderr=subprocess.STDOUT)
    if result.returncode:raise RuntimeError(node+' failed; inspect log')
    record.event(dict(phase='node_verified',node=node,elapsed_seconds=time.monotonic()-started))
   pending.remove(sid);print(json.dumps(dict(scene=sid,status='aligned_and_compiled',completed=len(p.scenes)-len(pending),total=len(p.scenes))),flush=True)
 record.finish('completed',scenes=len(p.scenes))
except BaseException as e:record.finish('interrupted' if isinstance(e,KeyboardInterrupt) else 'failed',error=str(e));raise
