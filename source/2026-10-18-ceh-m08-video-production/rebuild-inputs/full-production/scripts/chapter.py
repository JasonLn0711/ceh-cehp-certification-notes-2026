#!/usr/bin/env python3
"""Prepare/check or render one full chapter from final measured assets."""
from pathlib import Path
import sys,json,time,subprocess,os,hashlib,fcntl,re
ROOT=Path(__file__).resolve().parents[1];QA=ROOT.parent/'qa';OUT=ROOT.parent/'output';PY=sys.executable;HF=str(ROOT/'node_modules/.bin/hyperframes')
ENV=os.environ.copy();ENV.setdefault('HYPERFRAMES_BROWSER_PATH','/home/jnlngx10/.cache/ms-playwright/chromium_headless_shell-1234/chrome-linux/headless_shell');ENV['HYPERFRAMES_RUN_ID']='ceh-m08-v1-0'
def fingerprint(folder):
 h=hashlib.sha256()
 for f in sorted(folder.rglob('*')):
  if f.is_file() and '.hyperframes' not in f.parts:
   data=f.read_bytes()
   if f.suffix=='.html':data=re.sub(rb' data-hf-id="[^"]*"',b'',data)
   h.update(str(f.relative_to(folder)).encode());h.update(data)
 return h.hexdigest()
def run(args,log=None):
 if log:
  with log.open('w') as f:r=subprocess.run(args,cwd=ROOT,env=ENV,stdout=f,stderr=subprocess.PIPE,text=True)
 else:r=subprocess.run(args,cwd=ROOT,env=ENV,text=True)
 if r.returncode:
  if log:print(r.stderr,file=sys.stderr)
  raise RuntimeError(('command failed',r.returncode,args,str(log)))
def main():
 mode,ch=sys.argv[1:3];folder=ROOT/'chapters'/ch;scenes=[s for s in json.load(open(ROOT/'data/scenes.json'))['scenes'] if s['chapter_id']==ch];assert scenes
 if mode=='prepare':
  began=time.monotonic()
  while True:
   ready=0
   for s in scenes:
    f=ROOT/'data'/f'{s["id"]}.audio.json'
    if not f.exists():continue
    a=json.load(open(f))
    if a['baseline_speed']!=json.load(open(ROOT/'data/voice-calibration.json'))['baseline_speed']:continue
    ok=True
    for seg in a['segments']:
     if seg['kind']!='spoken':continue
     af=ROOT/'data/forced-alignment'/f'{s["id"]}-{seg["sentence"]:03}.json'
     if not af.exists() or json.load(open(af)).get('audio_sha256')!=seg['sha256']:ok=False;break
    if ok:ready+=1
   if ready==len(scenes):break
   for phase in ['narration','alignment']:
    pf=QA/(phase+'-process.json')
    if pf.exists() and json.load(open(pf)).get('status')=='failed':raise RuntimeError(phase+' failed; inspect '+str(QA/(phase+'.log')))
   print(json.dumps({'chapter':ch,'phase':'waiting_final_audio_alignment','ready':ready,'total':len(scenes),'elapsed':round(time.monotonic()-began)}),flush=True);time.sleep(10)
  with (QA/'build.lock').open('w') as lock:
   fcntl.flock(lock,fcntl.LOCK_EX);run([PY,str(ROOT/'scripts/build_film.py'),'--chapter',ch]);fcntl.flock(lock,fcntl.LOCK_UN)
  ts=[];mids=[];offset=0
  for s in scenes:
   a=json.load(open(ROOT/'data'/f'{s["id"]}.audio.json'));d=a['duration'];ts.extend(offset+d*x for x in [.12,.5,.9]);mids.append(offset+d*.5)
   for seg in a['segments']:
    if seg['kind']=='silence':ts.extend([offset+seg['start_sample']/48000+.1,offset+(seg['start_sample']+seg['end_sample'])/96000,offset+seg['end_sample']/48000+.1]);mids.append(offset+(seg['start_sample']+seg['end_sample'])/96000)
   offset+=d
  (QA/f'{ch}-timing.json').write_text(json.dumps({'duration':offset,'frames':round(offset*30),'scenes':[s['id'] for s in scenes],'midpoints':mids},indent=2))
  run([HF,'check',str(folder),'--at',','.join(f'{v:.6f}' for v in sorted(set(ts))),'--json'],QA/f'{ch}-check.json')
  check=json.load(open(QA/f'{ch}-check.json'));assert check['ok'] and not check['browserSkipped']
  run([HF,'snapshot',str(folder),'--at',','.join(f'{v:.6f}' for v in mids),'--no-end','--describe','false','--output',str(QA/f'{ch}-snapshots')],QA/f'{ch}-snapshots.log')
  (QA/f'{ch}-checked-fingerprint.json').write_text(json.dumps({'sha256':fingerprint(folder),'status':'checked_visual_review_pending'},indent=2))
  print(json.dumps({'chapter':ch,'status':'prepared_for_visual_review','snapshots':str(QA/f'{ch}-snapshots')}))
 elif mode=='render':
  key=fingerprint(folder);check=json.load(open(QA/f'{ch}-check.json'));assert check['ok'] and not check['browserSkipped'];assert key==json.load(open(QA/f'{ch}-checked-fingerprint.json'))['sha256']
  assert (QA/f'{ch}-visual-review.md').exists(),'Write concrete frame-review findings before render'
  assert 'review_status: pass' in (QA/f'{ch}-visual-review.md').read_text(),'Review contains unresolved findings'
  (OUT/'chapters').mkdir(exist_ok=True);target=OUT/'chapters'/f'{ch}.mp4';started=time.monotonic()
  run([HF,'render',str(folder),'--output',str(target),'--fps','30','--quality','delivery','--workers','4','--no-best-effort','--strict'],QA/f'{ch}-render.log')
  probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(target)]));v=next(x for x in probe['streams'] if x['codec_type']=='video');a=next(x for x in probe['streams'] if x['codec_type']=='audio');expected=json.load(open(QA/f'{ch}-timing.json'))
  assert (v['codec_name'],v['width'],v['height'],v['r_frame_rate'],a['codec_name'])==('h264',1920,1080,'30/1','aac');assert abs(float(v['duration'])-expected['duration'])<1/30+.001
  assert key==fingerprint(folder),'source changed during render'
  (QA/f'{ch}-render.json').write_text(json.dumps({'status':'rendered_codec_verified','source_sha256':key,'output_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-started,'probe':probe},indent=2))
  print(json.dumps({'chapter':ch,'rendered':str(target),'duration':v['duration']}))
 else:raise ValueError(mode)
if __name__=='__main__':main()
