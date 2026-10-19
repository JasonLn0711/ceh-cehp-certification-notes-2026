from ceh_video.common import project_root, Project
#!/usr/bin/env python3
"""Independent local speech recognition for omission/pronunciation review; never edits captions."""
from pathlib import Path
import json,hashlib,subprocess,re,difflib,os,time,argparse
import numpy as np
from faster_whisper import WhisperModel
ROOT=project_root();DEST=ROOT.parent/'qa/recognition';DEST.mkdir(exist_ok=True)
parser=argparse.ArgumentParser();parser.add_argument('--scene');parser.add_argument('--start',type=int);parser.add_argument('--end',type=int);args=parser.parse_args()
model=None;generated=[];reused=[]
for scene in json.load(open(ROOT/'data/scenes.json'))['scenes']:
 sid=scene['id']
 if args.start is not None and int(sid[1:])<args.start:continue
 if args.end is not None and int(sid[1:])>args.end:continue
 if args.scene and sid!=args.scene:continue
 wave=ROOT/f'assets/voice/{sid}.wav'
 def ready():
  af=ROOT/'data'/f'{sid}.audio.json'
  return wave.exists() and af.exists() and json.load(open(af))['baseline_speed']==json.load(open(ROOT/'data/voice-calibration.json'))['baseline_speed']
 while not ready():
  try:os.kill(json.load(open(ROOT.parent/'qa/narration-process.json'))['pid'],0)
  except ProcessLookupError:raise RuntimeError('Missing narration '+sid)
  time.sleep(3)
 key=hashlib.sha256(wave.read_bytes()).hexdigest();out=DEST/f'{sid}.json'
 if out.exists() and json.load(open(out)).get('audio_sha256')==key and json.load(open(out)).get('canonical')==scene['narration_en_US']:
  reused.append(sid);continue
 if model is None:model=WhisperModel(str(ROOT/'models/faster-whisper-base.en'),device='cpu',compute_type='int8',cpu_threads=1)
 pcm=subprocess.check_output(['ffmpeg','-v','error','-i',str(wave),'-f','f32le','-ar','16000','-ac','1','pipe:1']);audio=np.frombuffer(pcm,dtype=np.float32)
 segments,info=model.transcribe(audio,language='en',beam_size=1,best_of=1,temperature=0,condition_on_previous_text=False,word_timestamps=False,vad_filter=False)
 transcript=[];rows=[]
 for segment in segments:
  transcript.append(segment.text.strip());rows.append({'start':segment.start,'end':segment.end,'text':segment.text.strip(),'avg_logprob':segment.avg_logprob,'no_speech_probability':segment.no_speech_prob})
 text=' '.join(transcript);normalize=lambda x:re.sub(r'[^a-z0-9]','',x.lower())
 ratio=None # Functional transcript receipt only; no ASR accuracy/performance metric.
 record={'scene':sid,'audio_sha256':key,'method':'independent base.en ASR; no canonical prompt; temperature0','recognized':text,'canonical':scene['narration_en_US'],'accuracy':'not_evaluated','latency':'not_evaluated','segments':rows,'status':'recognition_evidence_not_listening_acceptance'}
 tmp=out.with_suffix('.tmp');tmp.write_text(json.dumps(record,indent=2));os.replace(tmp,out);print(json.dumps({'scene':sid,'functional_transcript':bool(text),'segments':len(rows)}),flush=True)
 generated.append(sid)
from ceh_video.common import write
write(ROOT.parent/'qa/recognition-refresh.json',{'status':'completed','exit_code':0,'new_inferences':len(generated),'generated':generated,'reused':reused,'accuracy':'not_evaluated','latency':'not_evaluated'})
