"""Launch a durable, locally authorized production stage with a separate process group."""
from pathlib import Path
import subprocess,sys,os,json,time
R=Path(__file__).resolve().parents[1];Q=R.parent/'qa';name,target=sys.argv[1:3]
record=Q/f'{name}-process.json'
if record.exists():
 old=json.loads(record.read_text())
 if old.get('status')=='running':
  try:os.kill(old['pid'],0);raise SystemExit('Stage already running: '+name)
  except ProcessLookupError:pass
log=(Q/f'{name}-supervisor.log').open('a');env=os.environ.copy();env['OMP_NUM_THREADS']='4';env['OMP_WAIT_POLICY']='PASSIVE';env['PYTHONUNBUFFERED']='1'
p=subprocess.Popen([sys.executable,str(R/'scripts/run_stage.py'),name,sys.executable,str(R/'scripts'/target),*sys.argv[3:]],cwd=R,stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True,env=env)
print(json.dumps({'stage':name,'supervisor_pid':p.pid,'log':str(Q/f'{name}.log'),'status':'launched_not_completed'}))
