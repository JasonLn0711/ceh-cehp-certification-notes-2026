from ceh_video.common import project_root, Project
#!/usr/bin/env python3
"""Validate the delivered master and sample actual encoded frames across every scene."""
from pathlib import Path
import json,subprocess,concurrent.futures,time,math
import numpy as np
from PIL import Image,ImageDraw,ImageFont
MASTER_FILENAME=Project(project_root()).profile['master_filename']
ROOT=project_root();OUT=ROOT.parent/'output';QA=ROOT.parent/'qa';MOVIE=OUT/MASTER_FILENAME
def main():
 started=time.monotonic();meta=json.load(open(ROOT/'data/master-timing.json'));assert MOVIE.exists();samples=OUT/'inspection_frames';samples.mkdir(exist_ok=True)
 from ceh_video.media_scan import require_scan
 scan=require_scan(MOVIE,meta['frames'],QA)
 print(json.dumps({'phase':'full_decode_verified_reuse','decoded_frames':scan['decoded_frames'],'master_sha256':scan['master_sha256']}),flush=True)
 rows=[]
 for s in meta['scenes']:rows.append({'label':s['scene']+' midpoint','time':s['start']+s['duration']/2,'file':s['scene']+'-midpoint.png'})
 for c in meta['chapters']:
  for label,t in [('first',c['start']+.1),('middle',c['start']+c['duration']/2),('last',c['start']+c['duration']-.1)]:rows.append({'label':c['id']+' '+label,'time':t,'file':c['id']+'-'+label+'.png'})
 for i,p in enumerate(meta['silences'],1):rows.append({'label':f'Q{i} silent pause','time':(p['start']+p['end'])/2,'file':f'quiz-{i:02}-pause.png'})
 for i,p in enumerate(meta['silences'],1):
  for label,at in [('before',p['start']-.05),('answer',p['end']+.45)]:rows.append({'label':f'Q{i} {label}','time':at,'file':f'quiz-{i:02}-{label}.png'})
 def grab(row):
  subprocess.run(['ffmpeg','-v','error','-ss',str(row['time']),'-i',str(MOVIE),'-frames:v','1','-y',str(samples/row['file'])],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE);return row
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  for i,row in enumerate(pool.map(grab,rows),1):
   if i%10==0 or i==len(rows):print(json.dumps({'phase':'encoded_frames_sampled','completed':i,'total':len(rows)}),flush=True)
 font=ImageFont.truetype(str(ROOT/'assets/fonts/LiberationSans-Regular.ttf'),25)
 scene_end=len(meta['scenes']);chapter_end=scene_end+3*len(meta['chapters']);quiz_end=chapter_end+len(meta['silences'])
 for group,items in [('scenes',rows[:scene_end]),('chapters',rows[scene_end:chapter_end]),('quiz',rows[chapter_end:quiz_end]),('quiz-boundaries',rows[quiz_end:])]:
  for page in range(math.ceil(len(items)/9)):
   subset=items[page*9:(page+1)*9];sheet=Image.new('RGB',(1920,400*math.ceil(len(subset)/3)),(240,235,228));draw=ImageDraw.Draw(sheet)
   for j,row in enumerate(subset):
    x=(j%3)*640;y=(j//3)*400;draw.text((x+12,y+5),row['label']+' · '+f'{row["time"]:.3f}s',font=font,fill=(41,36,33));img=Image.open(samples/row['file']).convert('RGB');img.thumbnail((640,360));sheet.paste(img,(x,y+36))
   sheet.save(samples/f'{group}-contact-{page+1:02}.jpg',quality=93)
 pauses=[]
 for p in meta['silences']:
  # AAC may smear a few boundary samples; assess the full pause and an interior window separately.
  raw=subprocess.check_output(['ffmpeg','-v','error','-ss',str(p['start']),'-i',str(MOVIE),'-t',str(p['end']-p['start']),'-map','0:a:0','-f','f32le','-ac','2','-ar','48000','pipe:1']);pcm=np.frombuffer(raw,dtype=np.float32).reshape(-1,2);assert len(pcm)==48000
  inner=pcm[2400:-2400];peak=float(np.max(np.abs(inner)));rms=float(np.sqrt(np.mean(inner**2)));full_peak=float(np.max(np.abs(pcm)));full_rms=float(np.sqrt(np.mean(pcm**2)));assert full_peak<.001 and peak<.001,(p['scene'],peak)
  pauses.append({**p,'decoded_samples':len(pcm),'channels':2,'full_window_peak':full_peak,'full_window_rms':full_rms,'nonzero_channel_samples':int(np.count_nonzero(pcm)),'interior_peak':peak,'interior_rms':rms,'acceptance':'digital-zero PCM; decoded AAC boundary residue disclosed'})
 result={'status':'automated_encoded_artifact_checks_passed','duration':meta['duration'],'frames':scan['decoded_frames'],'master_sha256':scan['master_sha256'],'full_decode_receipt':'master-full-decode.json','decoded_entire_master':True,'black_intervals':scan['black_intervals'],'sampled_frames':rows,'quiz_silence':pauses,'elapsed_seconds':time.monotonic()-started,'scope':'Encoded samples require visual inspection; waveform/ASR checks do not constitute human end-to-end listening.'};(QA/'rendered-artifact-audit.json').write_text(json.dumps(result,indent=2))
 chapter_pauses=[]
 for p in meta['silences']:
  chapter_id=next(s['chapter'] for s in meta['scenes'] if s['scene']==p['scene']);chapter_start=next(c['start'] for c in meta['chapters'] if c['id']==chapter_id)
  raw=subprocess.check_output(['ffmpeg','-v','error','-ss',str(p['start']-chapter_start),'-i',str(OUT/'chapters'/f'{chapter_id}.mp4'),'-t','1','-map','0:a:0','-f','f32le','-ac','2','-ar','48000','pipe:1']);pcm=np.frombuffer(raw,dtype=np.float32).reshape(-1,2);assert len(pcm)==48000
  peak=float(np.max(np.abs(pcm)));assert peak<.001
  chapter_pauses.append({'scene':p['scene'],'chapter_local_start':p['start']-chapter_start,'decoded_frames':len(pcm),'full_peak':peak,'nonzero_channel_samples':int(np.count_nonzero(pcm))})
 (QA/'encoded-quiz-silence.json').write_text(json.dumps({'status':'passed_with_disclosed_AAC_boundary_residue','holds':chapter_pauses},indent=2));print(json.dumps({'phase':'encoded_artifact_audit_complete','samples':len(rows),'quiz_pauses':len(meta['silences'])}),flush=True)
if __name__=='__main__':main()
