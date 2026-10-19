"""Resume verified chapter renders with at most two active render processes."""
from pathlib import Path
import json,os,time,subprocess,sys,hashlib
from chapter import fingerprint
R=Path(__file__).resolve().parents[1];Q=R.parent/'qa';O=R.parent/'output';began=time.monotonic();chapters=[f'C{i:02}' for i in range(1,12)]
while True:
 done=[];active=[];eligible=[];waiting=[]
 for ch in chapters:
  folder=R/'chapters'/ch;receipt=Q/f'{ch}-render.json';video=O/'chapters'/f'{ch}.mp4'
  if receipt.exists() and video.exists():
   d=json.load(open(receipt))
   if fingerprint(folder)==d['source_sha256'] and hashlib.sha256(video.read_bytes()).hexdigest()==d['output_sha256']:done.append(ch);continue
  process=Q/f'{ch}-render-process.json'
  if not process.exists():process=Q/f'render-{ch}-process.json'
  if process.exists():
   d=json.load(open(process))
   if d['status']=='failed':raise RuntimeError(ch+' render failed; inspect '+str(Q/f'{ch}-render.log'))
   if d['status']=='running':
    try:os.kill(d['pid'],0)
    except ProcessLookupError:raise RuntimeError(ch+' process disappeared; reconcile its receipt before retrying')
    active.append(ch);continue
  check=Q/f'{ch}-checked-fingerprint.json';review=Q/f'{ch}-visual-review.md';prep=Q/f'{ch}-prepare-process.json'
  if prep.exists() and json.load(open(prep)).get('status')=='failed':raise RuntimeError(ch+' preparation failed; inspect '+str(Q/f'{ch}-prepare.log'))
  if check.exists() and review.exists() and 'review_status: pass' in review.read_text() and fingerprint(folder)==json.load(open(check))['sha256']:eligible.append(ch)
  else:waiting.append(ch)
 print(json.dumps({'phase':'chapter_render_queue','verified':len(done),'total':11,'completed':done,'active':active,'ready':eligible,'waiting_visual_or_preparation':waiting,'elapsed_seconds':round(time.monotonic()-began)}),flush=True)
 if len(done)==11:break
 for ch in eligible[:max(0,2-len(active))]:subprocess.run([sys.executable,str(R/'scripts/launch_stage.py'),ch+'-render','chapter.py','render',ch],cwd=R,check=True)
 time.sleep(15)
print(json.dumps({'phase':'all_chapter_renders_verified','chapters':11}),flush=True)
