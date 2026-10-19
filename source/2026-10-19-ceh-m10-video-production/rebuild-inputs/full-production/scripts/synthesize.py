#!/usr/bin/env python3
"""Local M10 narration: calibrated baseline, exactly one spoken-only atempo step."""
from pathlib import Path
import json,re,hashlib,os,time,argparse,subprocess
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro
from production_settings import quiz_seconds
ROOT=Path(__file__).resolve().parents[1];SR=48000
MODEL_SHA={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'models/kokoro-v1.0.onnx',ROOT/'models/voices-v1.0.bin']}
SPELL=set('CEH AI URL HTTP HTTPS IT ID CSV JSON PDF CPU TCP UDP DNS RFC IP PCAP RPS API WAF CDN SYNACK UTF'.split())
PRON={'DoS':'denial of service','DDoS':'distributed denial of service','SYN':'sin','SYN-ACK':'sin ack','ACK':'ack','Mbps':'megabits per second','Gbps':'gigabits per second','pps':'packets per second','bps':'bits per second','TShark':'T shark','IPv4':'I P version four','IPv6':'I P version six','A':'A,','DMARC':'dee mark','DKIM':'dee kim','WebAuthn':'Web Authentication','WebAuthn-based':'Web Authentication based','GoPhish':'Go Fish','AI-sounding':'A I sounding','NIST':'nist','CISA':'see suh','Tally':'Tally'}

def spoken(text):
 def token(m):
  w=m.group(0)
  return ' '.join('A,' if c=='A' else c for c in w) if w in SPELL else PRON.get(w,w)
 return re.sub(r'\b[A-Za-z][A-Za-z0-9-]*\b',token,text)
def sentences(text):
 parts=re.split(r'(?<=[.!?])\s+(?=[A-Z“\"])',text);out=[];prefix=''
 for p in parts:
  if re.fullmatch('[A-D][.]',p):prefix=p+' ';continue
  out.append(prefix+p);prefix=''
 if prefix:out.append(prefix.strip())
 assert ' '.join(out)==' '.join(text.split())
 return out
def words(text):return len(re.findall(r"\b[\w'-]+\b",text))
def make(model,text,speed,path):
 samples,rate=model.create(spoken(text),voice='af_heart',speed=speed,lang='en-us');assert rate==24000 and len(samples)
 gain=min(1.,.94/max(float(np.max(np.abs(samples))),1e-9));sf.write(path,samples*gain,rate,subtype='PCM_16')
 return len(samples)/rate

def main():
 p=argparse.ArgumentParser();p.add_argument('--calibrate',action='store_true');p.add_argument('--scene');p.add_argument('--start',type=int,default=1);p.add_argument('--end',type=int,default=58);args=p.parse_args()
 os.environ.setdefault('OMP_NUM_THREADS','4')
 model=Kokoro(str(ROOT/'models/kokoro-v1.0.onnx'),str(ROOT/'models/voices-v1.0.bin'))
 quiet,quiet_sr=sf.read(ROOT/'production/silence_1s_48k_stereo.wav',dtype='float32');assert quiet_sr==SR and quiet.shape==(SR,2) and not np.any(quiet)
 scenes=json.loads((ROOT/'data/scenes.json').read_text())['scenes'];qa=ROOT.parent/'qa';config=ROOT/'data/voice-calibration.json'
 if args.calibrate:raise RuntimeError('M10 baseline is approved at0.73; create a separately approved voice version before recalibration')
 cfg=json.loads(config.read_text());speed=cfg['baseline_speed'];started=time.monotonic()
 scenes=[s for s in scenes if args.start<=int(s['id'][1:])<=args.end]
 if args.scene:scenes=[s for s in scenes if s['id']==args.scene]
 for ordinal,scene in enumerate(scenes,1):
  sid=scene['id'];folder=ROOT/'assets/voice'/sid;folder.mkdir(parents=True,exist_ok=True);rawfolder=ROOT/'assets/voice-baseline'/sid;rawfolder.mkdir(parents=True,exist_ok=True)
  clips=[np.zeros((SR//2,2),dtype=np.float32)];cursor=len(clips[0]);timeline=[];sentence_id=0
  for seg_i,segment in enumerate(scene['audio_segments']):
   if segment['kind']=='silence':
    seconds=quiz_seconds();count=SR*seconds;timeline.append({'kind':'silence','source_segment':seg_i,'start_sample':cursor,'end_sample':cursor+count,'seconds':seconds});clips.append(quiet.copy());cursor+=count;continue
   parts=sentences(segment['text'])
   for j,canonical in enumerate(parts):
    recipe={'text':canonical,'spoken':spoken(canonical),'voice':'af_heart','baseline_speed':speed,'atempo':1.5,'version':'m10-1','models_sha256':MODEL_SHA};key=hashlib.sha256(json.dumps(recipe,sort_keys=True).encode()).hexdigest()
    wav=folder/f'{sentence_id:03d}.wav';raw=rawfolder/wav.name;meta=wav.with_suffix('.json')
    if not(wav.exists() and meta.exists() and json.loads(meta.read_text()).get('recipe_sha256')==key):
     baseline_duration=make(model,canonical,speed,raw)
     subprocess.run(['ffmpeg','-v','error','-nostdin','-y','-i',str(raw),'-af','atempo=1.5','-ar','48000','-ac','2','-c:a','pcm_s16le',str(wav)],check=True)
     meta.write_text(json.dumps({**recipe,'recipe_sha256':key,'baseline_seconds':baseline_duration,'speed_applications':1},indent=2))
    samples,rate=sf.read(wav,dtype='float32');assert rate==SR and len(samples)>0 and np.isfinite(samples).all() and np.max(np.abs(samples))<1
    detail=json.loads(meta.read_text());timeline.append({'kind':'spoken','source_segment':seg_i,'sentence':sentence_id,'canonical':canonical,'spoken':spoken(canonical),'path':str(wav.relative_to(ROOT)),'baseline_path':str(raw.relative_to(ROOT)),'baseline_seconds':detail['baseline_seconds'],'speed_applications':1,'start_sample':cursor,'end_sample':cursor+len(samples),'sha256':hashlib.sha256(wav.read_bytes()).hexdigest()})
    clips.append(samples);cursor+=len(samples);sentence_id+=1
    if j<len(parts)-1:gap=np.zeros((round(.18*SR),2),dtype=np.float32);clips.append(gap);cursor+=len(gap)
   print(json.dumps({'phase':'speech_segment_ready','scene':sid,'segment':seg_i,'sentences':sentence_id}),flush=True)
  clips.append(np.zeros((SR*3,2),dtype=np.float32));cursor+=SR*3;pad=(-cursor)%(SR//30)
  if pad:clips.append(np.zeros((pad,2),dtype=np.float32));cursor+=pad
  full=np.concatenate(clips);assert len(full)==cursor
  target=ROOT/f'assets/voice/{sid}.wav';sf.write(str(target)+'.tmp.wav',full,SR,subtype='PCM_16');os.replace(str(target)+'.tmp.wav',target)
  result={'scene':sid,'chapter':scene['chapter_id'],'voice':'af_heart','language':'en-us','baseline_speed':speed,'atempo':1.5,'sample_rate':SR,'channels':2,'samples':cursor,'duration':cursor/SR,'sentence_count':sentence_id,'segments':timeline,'scope':'Generated post-speed audio; review pending'}
  out=ROOT/f'data/{sid}.audio.json';tmp=out.with_suffix('.tmp');tmp.write_text(json.dumps(result,indent=2));os.replace(tmp,out)
  print(json.dumps({'phase':'scene_audio_generated','scene':sid,'completed':ordinal,'total':len(scenes),'duration':cursor/SR,'elapsed_seconds':round(time.monotonic()-started,1)}),flush=True)
if __name__=='__main__':main()
