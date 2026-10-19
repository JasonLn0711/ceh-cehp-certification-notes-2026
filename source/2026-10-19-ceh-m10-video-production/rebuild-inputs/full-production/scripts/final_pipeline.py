"""Wait for verified chapters, then run actual full-master checks."""
from pathlib import Path
import json,time,subprocess,sys,hashlib
from chapter import fingerprint
R=Path(__file__).resolve().parents[1];Q=R.parent/'qa';O=R.parent/'output';began=time.monotonic()
while True:
 ready=[]
 for i in range(1,12):
  ch=f'C{i:02}';p=Q/f'{ch}-render.json';video=O/'chapters'/f'{ch}.mp4'
  if not p.exists() or not video.exists():continue
  d=json.load(open(p))
  if d.get('status')=='rendered_codec_verified' and fingerprint(R/'chapters'/ch)==d['source_sha256'] and hashlib.sha256(video.read_bytes()).hexdigest()==d['output_sha256']:ready.append(ch)
 print(json.dumps({'phase':'waiting_verified_chapters','completed':len(ready),'total':11,'chapters':ready,'elapsed':round(time.monotonic()-began)}),flush=True)
 if len(ready)==11:break
 time.sleep(10)
for script in ['assemble_master.py','audit_rendered.py']:
 print(json.dumps({'phase':'starting','script':script}),flush=True);subprocess.run([sys.executable,str(R/'scripts'/script)],cwd=R,check=True)
