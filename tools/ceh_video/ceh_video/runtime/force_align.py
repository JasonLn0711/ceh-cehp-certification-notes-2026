from ceh_video.common import project_root, Project
#!/usr/bin/env python3
"""Align known spoken text to real audio using Whisper attention/DTW, not duration division."""
from pathlib import Path
import json,re,hashlib,subprocess,os,time,argparse
from ceh_video.speech import spoken as expand
def spoken(text):return expand(text,__import__('json').load(open(project_root()/'pronunciation.json')))
ROOT=project_root()
RECIPE='base.en-int8-forced-dtw-v1'
def norm(s):return re.sub(r'[^a-z0-9]','',s.lower())
def main():
 p=argparse.ArgumentParser();p.add_argument('--scene');p.add_argument('--start',type=int);p.add_argument('--end',type=int);args=p.parse_args()
 model=None;tok=None
 dest=ROOT/'data/forced-alignment';dest.mkdir(exist_ok=True)
 for scene in json.load(open(ROOT/'data/scenes.json'))['scenes']:
  if args.start is not None and int(scene['id'][1:])<args.start:continue
  if args.end is not None and int(scene['id'][1:])>args.end:continue
  if args.scene and scene['id']!=args.scene:continue
  tf=ROOT/f'data/{scene["id"]}.audio.json'
  while not tf.exists():
   try:os.kill(json.load(open(ROOT.parent/'qa/narration-process.json'))['pid'],0)
   except ProcessLookupError:raise RuntimeError('Narration stopped before '+scene['id'])
   time.sleep(3)
  for r in json.load(open(tf))['segments']:
   if r['kind']!='spoken':continue
   r['text']=r['canonical']
   wav=ROOT/r['path'];key=hashlib.sha256(wav.read_bytes()).hexdigest();out=dest/f'{scene["id"]}-{r["sentence"]:03}.json'
   if out.exists():
    old=json.load(open(out))
    if old.get('audio_sha256')==key and old.get('recipe')==RECIPE and old.get('canonical')==r['canonical'] and old.get('spoken',r['spoken'])==r['spoken']:continue
   if model is None:
    import numpy as np
    from faster_whisper import WhisperModel
    from faster_whisper.tokenizer import Tokenizer
    from faster_whisper.audio import pad_or_trim
    model=WhisperModel(str(ROOT/'models/faster-whisper-base.en'),device='cpu',compute_type='int8',cpu_threads=2)
    tok=Tokenizer(model.hf_tokenizer,model.model.is_multilingual,task='transcribe',language='en')
   pcm=subprocess.check_output(['ffmpeg','-v','error','-i',str(wav),'-ar','16000','-ac','1','-f','f32le','pipe:1'])
   a=np.frombuffer(pcm,dtype=np.float32);duration=len(a)/16000
   assert duration<30,(scene['id'],r['sentence'],duration)
   features=model.feature_extractor(a);enc=model.encode(pad_or_trim(features))
   aligned=model.find_alignment(tok,[tok.encode(r['spoken'])],enc,features.shape[-1])[0]
   # Character spans preserve original spelling while grouping spelled acronyms/host names.
   spans=[];stream=''
   for w in aligned:
    text=norm(w['word'])
    if text:
     start=len(stream);stream+=text;spans.append((start,len(stream),w))
   words=[];cursor=0;flags=[]
   for i,word in enumerate(r['text'].split()):
    text=norm(spoken(word));end=cursor+len(text)
    assert stream[cursor:end]==text,(scene['id'],r['sentence'],word,stream[cursor:end],text)
    parts=[w for lo,hi,w in spans if lo<end and hi>cursor]
    assert parts,(word,r['text'])
    start=max(0,float(parts[0]['start']));stop=min(duration,float(parts[-1]['end']))
    probability=min(float(w['probability']) for w in parts)
    if stop<=start:flags.append({'word':i,'reason':'zero_duration'})
    if probability<.05 and i>0:flags.append({'word':i,'reason':'low_alignment_probability','probability':probability})
    words.append({'text':word,'start':start,'end':stop,'probability':probability});cursor=end
   assert cursor==len(stream)
   data={'scene':scene['id'],'sentence':r['sentence'],'canonical':r['text'],'spoken':r['spoken'],'audio_sha256':key,'recipe':RECIPE,'duration':duration,'words':words,'review_flags':flags,'status':'forced_alignment_not_listen_reviewed'}
   temp=out.with_suffix('.tmp');temp.write_text(json.dumps(data,indent=2));os.replace(temp,out)
   print(json.dumps({'scene':scene['id'],'sentence':r['sentence'],'words':len(words),'flags':len(flags)}),flush=True)
if __name__=='__main__':main()
