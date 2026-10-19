"""Run independent encoded late-frame and full-track audio checks after master closure."""
from pathlib import Path
import concurrent.futures,json,time,subprocess,sys
R=Path(__file__).resolve().parents[1];Q=R.parent/'qa';began=time.monotonic()
while not (Q/'master-ffprobe.json').exists():
 d=json.load(open(Q/'final-pipeline-process.json'))
 if d['status']=='failed':raise RuntimeError('Master assembly/audit failed; inspect final-pipeline.log')
 print(json.dumps({'phase':'waiting_closed_master','assembly_pipeline':d['status'],'elapsed_seconds':round(time.monotonic()-began)}),flush=True);time.sleep(15)
def run(name):
 script=R/'scripts'/name;logpath=Q/(Path(name).stem+'.log')
 with logpath.open('w') as log:
  p=subprocess.Popen([sys.executable,str(script)],cwd=R,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
  for line in p.stdout:
   log.write(line);log.flush()
   if line.strip().startswith('{'):print(line.rstrip(),flush=True)
  code=p.wait()
 if code:raise RuntimeError((name,code,'see '+str(logpath)))
 return name
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 for name in pool.map(run,['audit_audio_continuity.py','capture_late_diagrams.py']):print(json.dumps({'phase':'encoded_postcheck_completed','script':name}),flush=True)
print(json.dumps({'phase':'actual_post_master_checks_complete','elapsed_seconds':round(time.monotonic()-began)}),flush=True)
