"""Compare the decoded continuous AAC track with the exact reference PCM, block by block."""
from pathlib import Path
import json,subprocess,tempfile,os,math
import numpy as np
import soundfile as sf
from production_settings import MASTER_FILENAME
R=Path(__file__).resolve().parents[1];Q=R.parent/'qa';O=R.parent/'output';m=json.load(open(R/'data/master-timing.json'));n=m['frames']*1600
print(json.dumps({'phase':'decoding_final_AAC_for_reference_continuity','reference_frames':n}),flush=True)
with tempfile.TemporaryDirectory(prefix='aac-continuity-',dir=Q) as tmp:
 f=Path(tmp)/'decoded.f32'
 subprocess.run(['ffmpeg','-v','error','-i',str(O/MASTER_FILENAME),'-map','0:a:0','-ac','2','-ar','48000','-f','f32le',str(f)],check=True)
 count=f.stat().st_size//8;assert n<=count<=n+2048,(n,count)
 decoded=np.memmap(f,dtype='<f4',mode='r',shape=(count,2));rows=[];cursor=0
 with sf.SoundFile(O/'master.reference.pcm.wav') as ref:
  assert len(ref)==n and ref.samplerate==48000 and ref.channels==2
  for ch in m['chapters']:
   frames=round(ch['duration']*48000);left=frames;signal=noise=dot=dec_energy=0.;blocks=quiet_replacements=0
   while left:
    size=min(48000*5,left);x=ref.read(size,dtype='float32',always_2d=True);y=np.asarray(decoded[cursor:cursor+size]);assert x.shape==y.shape
    diff=x-y;signal+=float(np.sum(x*x,dtype=np.float64));noise+=float(np.sum(diff*diff,dtype=np.float64));dot+=float(np.sum(x*y,dtype=np.float64));dec_energy+=float(np.sum(y*y,dtype=np.float64));blocks+=1
    if np.max(np.abs(x))>.01 and not np.any(y):quiet_replacements+=1
    cursor+=size;left-=size
   snr=10*math.log10(signal/max(noise,1e-20));correlation=dot/math.sqrt(signal*dec_energy);assert snr>12 and correlation>.97 and quiet_replacements==0,(ch['id'],snr,correlation)
   rows.append({'chapter':ch['id'],'reference_frames':frames,'blocks_checked':blocks,'signal_to_codec_error_db':snr,'correlation':correlation,'all_zero_replacements':quiet_replacements})
   print(json.dumps({'phase':'AAC_reference_chapter_checked','chapter':ch['id'],'completed':len(rows),'total':11}),flush=True)
 assert cursor==n
 (Q/'audio-continuity-audit.json').write_text(json.dumps({'status':'passed','reference_frames':n,'decoded_frames':count,'codec_tail_padding_frames':count-n,'channels':2,'sample_rate':48000,'all_reference_frames_compared':True,'chapters':rows,'scope':'Sample-aligned codec/reference signal integrity and full-track continuity. Not ASR accuracy, pronunciation, naturalness or human listening acceptance.'},indent=2))
 del decoded
print(json.dumps({'phase':'audio_continuity_complete','reference_frames_compared':n}),flush=True)
