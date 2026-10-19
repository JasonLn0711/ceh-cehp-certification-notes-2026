from ceh_video.common import project_root, Project
"""Measure actual clip recipes, canonical coverage and zero buffers without overwriting caption timing evidence."""
from pathlib import Path
import json,hashlib
import numpy as np
import soundfile as sf
R=project_root();Q=R.parent/'qa'
rows=[];words=clips=0;pauses=[]
for scene in json.load(open(R/'data/scenes.json'))['scenes']:
 sid=scene['id'];a=json.load(open(R/'data'/f'{sid}.audio.json'));pcm,sr=sf.read(R/'assets/voice'/f'{sid}.wav',dtype='int16',always_2d=True)
 assert sr==48000 and pcm.shape==(a['samples'],2) and len(pcm)%1600==0
 spoken=[x for x in a['segments'] if x['kind']=='spoken'];assert ' '.join(x['canonical'] for x in spoken)==' '.join(scene['narration_en_US'].split())
 for x in spoken:
  f=R/x['path'];recipe=json.load(open(f.with_suffix('.json')));assert recipe['baseline_speed']==.73 and recipe['atempo']==1.5 and recipe['speed_applications']==1
  assert hashlib.sha256(f.read_bytes()).hexdigest()==x['sha256']
  words+=len(x['canonical'].split());clips+=1
 for x in a['segments']:
  if x['kind']!='silence':continue
  zero=pcm[x['start_sample']:x['end_sample']];assert zero.shape==(48000,2) and not np.any(zero)
  pauses.append({'scene':sid,'start_sample':x['start_sample'],'end_sample':x['end_sample'],'stereo_frames':len(zero),'nonzero_channel_samples':int(np.count_nonzero(zero))})
 rows.append({'scene':sid,'samples':len(pcm),'frames':len(pcm)//1600,'spoken_clips':len(spoken),'canonical_words':sum(len(x['canonical'].split()) for x in spoken),'peak_pcm':int(np.max(np.abs(pcm.astype(np.int32))))})
assert words==Project(project_root()).profile['expected']['canonical_words'] and len(rows)==len(Project(project_root()).scenes) and len(pauses)==8
(Q/'audio-clip-structure-audit.json').write_text(json.dumps({'status':'passed','scenes':len(Project(project_root()).scenes),'canonical_words':words,'spoken_clips':clips,'quiz_holds':pauses,'total_hold_seconds':8,'sample_rate':48000,'channels':2,'recipe':'af_heart/en-us baseline0.73; one atempo1.5 per speech clip','scope':'Actual PCM, clip recipes, canonical coverage and digital-zero buffers; no full human listening or pronunciation score.','rows':rows},indent=2)+'\n')
print(json.dumps({'phase':'audio_clip_structure_verified','scenes':len(rows),'canonical_words':words,'spoken_clips':clips,'zero_holds':len(pauses)}),flush=True)
