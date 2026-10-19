from ceh_video.common import project_root, Project
#!/usr/bin/env python3
"""Export measured chapter marks, aligned captions and audio/silence checks."""
from pathlib import Path
import json,hashlib,math,csv
import numpy as np
import soundfile as sf
def quiz_seconds():return Project(project_root()).profile['quiz_silence_seconds']
ROOT=project_root();OUT=ROOT.parent/'output';QA=ROOT.parent/'qa'
def clock(value,sep=','):
 ms=round(value*1000);h,ms=divmod(ms,3600000);m,ms=divmod(ms,60000);s,ms=divmod(ms,1000);return f'{h:02}:{m:02}:{s:02}{sep}{ms:03}'
def main():
 scenes=json.load(open(ROOT/'data/scenes.json'))['scenes'];assert len(scenes)==len(Project(project_root()).scenes)
 OUT.mkdir(exist_ok=True);cursor=0;captions=[];chapters=[];ledger=[];silences=[];flags=[]
 for scene in scenes:
  sid=scene['id'];a=json.load(open(ROOT/'data'/f'{sid}.audio.json'));caps=json.load(open(ROOT/'data'/f'{sid}.captions.json'));assert caps,(sid,'missing aligned captions')
  pcm,sr=sf.read(ROOT/'assets/voice'/f'{sid}.wav');assert sr==48000 and len(pcm)==a['samples'];assert len(pcm)%1600==0
  source=' '.join(s['canonical'] for s in a['segments'] if s['kind']=='spoken');norm=lambda x:' '.join(x.split());assert norm(source)==norm(scene['narration_en_US'])
  assert norm(' '.join(c['text'] for c in caps))==norm(source),(sid,'caption coverage')
  for seg in a['segments']:
   if seg['kind']=='silence':
    zero=pcm[seg['start_sample']:seg['end_sample']];assert len(zero)==quiz_seconds()*sr and np.count_nonzero(zero)==0
    silences.append({'scene':sid,'start':cursor+seg['start_sample']/sr,'end':cursor+seg['end_sample']/sr,'samples':len(zero),'nonzero_samples':0})
  if not chapters or chapters[-1]['id']!=scene['chapter_id']:chapters.append({'id':scene['chapter_id'],'title':scene['chapter_title'],'start':cursor,'duration':0})
  chapters[-1]['duration']+=a['duration']
  for cap in caps:
   assert 0<=cap['start']<cap['end']<=a['duration'],(sid,cap)
   captions.append({**cap,'start':cursor+cap['start'],'end':cursor+cap['end'],'scene':sid})
  rms=float(np.sqrt(np.mean(pcm**2)));peak=float(np.max(np.abs(pcm)))
  ledger.append({'scene':sid,'chapter':scene['chapter_id'],'start':cursor,'duration':a['duration'],'peak':peak,'rms_dbfs':20*math.log10(max(rms,1e-12)),'audio_sha256':hashlib.sha256((ROOT/'assets/voice'/f'{sid}.wav').read_bytes()).hexdigest(),'status':'authored_audio_and_alignment_checked_visual_review_pending'})
  cursor+=a['duration']
 assert len(chapters)==len(Project(ROOT).chapters) and len(silences)==8
 (OUT/'captions.en-US.srt').write_text('\n\n'.join(f'{i}\n{clock(c["start"])} --> {clock(c["end"])}\n{c["text"]}' for i,c in enumerate(captions,1))+'\n')
 (OUT/'captions.en-US.vtt').write_text('WEBVTT\n\n'+'\n\n'.join(f'{clock(c["start"],".")} --> {clock(c["end"],".")}\n{c["text"]}' for c in captions)+'\n')
 (OUT/'chapters.txt').write_text('\n'.join(clock(c['start'],'.')+' '+c['id']+' '+c['title'] for c in chapters)+'\n')
 (ROOT/'data/master-timing.json').write_text(json.dumps({'duration':cursor,'frames':round(cursor*30),'chapters':chapters,'scenes':ledger,'silences':silences},indent=2))
 with (OUT/'scene_qa_ledger.csv').open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(ledger[0]));w.writeheader();w.writerows(ledger)
 (QA/'audio-structure-audit.json').write_text(json.dumps({'scene_count':len(Project(project_root()).scenes),'chapters':len(Project(ROOT).chapters),'duration':cursor,'captions':len(captions),'silent_intervals':silences,'audio':ledger,'scope':'Sample structure and canonical alignment; not listening or full-film acceptance'},indent=2))
 print(json.dumps({'duration':cursor,'captions':len(captions),'silent_intervals':8}))
if __name__=='__main__':main()
