from pathlib import Path
import subprocess,sys,concurrent.futures,json,time
R=Path(__file__).resolve().parents[1];Q=R.parent/'qa';start=time.monotonic()
def worker(pair):
 lo,hi=pair
 with (Q/f'alignment-S{lo:02}-S{hi:02}.log').open('a') as log:
  p=subprocess.Popen([sys.executable,str(R/'scripts/force_align.py'),'--start',str(lo),'--end',str(hi)],cwd=R,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
  for line in p.stdout:
   log.write(line);log.flush()
   if '"sentence"' in line:
    d=json.loads(line);d['range']=[lo,hi];print(json.dumps(d),flush=True)
  code=p.wait()
  if code:raise RuntimeError(f'Voice range{lo}-{hi} failed({code}); see {log.name}')
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(worker,[(1,19),(20,38),(39,58)]))
print(json.dumps({'phase':'all_alignment_ready','scenes':58,'elapsed':time.monotonic()-start}),flush=True)
