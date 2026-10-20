from ceh_video.common import project_root, Project, sha
"""Compare the decoded continuous AAC track with the exact reference PCM, block by block."""
from pathlib import Path
import json,subprocess,tempfile,os,math
import numpy as np
import soundfile as sf
def hold_residue(decoded, start, end):
 assert type(start) is int and type(end) is int and 0<=start<end<=len(decoded)
 x=np.asarray(decoded[start:end],dtype=np.float64)
 return {'start_sample':start,'end_sample':end,'frames':end-start,
         'nonzero_channel_samples':int(np.count_nonzero(x)),
         'peak_normalized':float(np.max(np.abs(x))),
         'peak_pcm16_units':float(np.max(np.abs(x))*32768),
         'rms_normalized':float(np.sqrt(np.mean(x*x))),
         'claim':'Measured decoded lossy AAC residue; zero-valued PCM is validated separately.'}

MASTER_FILENAME=Project(project_root()).profile['master_filename']
R=project_root();Q=R.parent/'qa';O=R.parent/'output';m=json.load(open(R/'data/master-timing.json'));n=m['frames']*1600
print(json.dumps({'phase':'decoding_final_AAC_for_reference_continuity','reference_frames':n}),flush=True)
with tempfile.TemporaryDirectory(prefix='aac-continuity-',dir=Q) as tmp:
 f=Path(tmp)/'decoded.f32'
 subprocess.run(['ffmpeg','-v','error','-i',str(O/MASTER_FILENAME),'-map','0:a:0','-ac','2','-ar','48000','-f','f32le',str(f)],check=True)
 count=f.stat().st_size//8;assert n<=count<=n+2048,(n,count)
 decoded=np.memmap(f,dtype='<f4',mode='r',shape=(count,2));rows=[];cursor=0
 with sf.SoundFile(O/'master.reference.pcm.wav') as ref:
  assert len(ref)==n and ref.samplerate==48000 and ref.channels==2
  for ch in m['chapters']:
   frames=ch.get('duration_samples',round(ch['duration']*48000));left=frames;signal=noise=dot=dec_energy=0.;blocks=quiet_replacements=0
   while left:
    size=min(48000*5,left);x=ref.read(size,dtype='float32',always_2d=True);y=np.asarray(decoded[cursor:cursor+size]);assert x.shape==y.shape
    diff=x-y;signal+=float(np.sum(x*x,dtype=np.float64));noise+=float(np.sum(diff*diff,dtype=np.float64));dot+=float(np.sum(x*y,dtype=np.float64));dec_energy+=float(np.sum(y*y,dtype=np.float64));blocks+=1
    if np.max(np.abs(x))>.01 and not np.any(y):quiet_replacements+=1
    cursor+=size;left-=size
   snr=10*math.log10(signal/max(noise,1e-20));correlation=dot/math.sqrt(signal*dec_energy);assert snr>12 and correlation>.97 and quiet_replacements==0,(ch['id'],snr,correlation)
   rows.append({'chapter':ch['id'],'reference_frames':frames,'blocks_checked':blocks,'signal_to_codec_error_db':snr,'correlation':correlation,'all_zero_replacements':quiet_replacements})
   print(json.dumps({'phase':'AAC_reference_chapter_checked','chapter':ch['id'],'completed':len(rows),'total':len(m['chapters'])}),flush=True)
 assert cursor==n
 holds=[];global_sample=0
 for scene in m['scenes']:
  a=json.load(open(R/'data'/f"{scene['scene']}.audio.json"))
  for seg in a['segments']:
   if seg['kind']!='silence':continue
   start=global_sample+seg['start_sample'];end=global_sample+seg['end_sample']
   assert end-start==48000
   holds.append({'scene':scene['scene'],**hold_residue(decoded,start,end),
     'opening_boundary':hold_residue(decoded,start,min(start+1024,end)),
     'closing_boundary':hold_residue(decoded,max(start,end-1024),end)})
  global_sample+=a['samples']
 assert global_sample==n and len(holds)==len(Project(R).questions)
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams','a:0','-show_streams','-of','json',str(O/MASTER_FILENAME)]))
 stream=probe['streams'][0]
 boundary={'status':'measured','master_sha256':sha(O/MASTER_FILENAME),
  'reference_frames':n,'decoded_frames':count,'codec_tail_padding_frames':count-n,
  'audio_timestamps':{key:stream.get(key) for key in ['time_base','start_pts','start_time','duration_ts','duration','codec_name']},
  'sample_rate':48000,'channels':2,'holds':holds,
  'scope':'Final master AAC decoded with FFmpeg; sample alignment follows decoded stream presentation timestamps. Lossy intervals need not be zero.'}
 if count>n:boundary['decoded_tail']=hold_residue(decoded,n,count)
 (Q/'master-aac-boundaries.json').write_text(json.dumps(boundary,indent=2))
 (Q/'audio-continuity-audit.json').write_text(json.dumps({'status':'passed','master_sha256':boundary['master_sha256'],'reference_sha256':sha(O/'master.reference.pcm.wav'),'reference_frames':n,'decoded_frames':count,'codec_tail_padding_frames':count-n,'channels':2,'sample_rate':48000,'all_reference_frames_compared':True,'chapters':rows,'aac_boundary_report':'master-aac-boundaries.json','scope':'Sample-aligned codec/reference signal integrity and full-track continuity. Not ASR accuracy, pronunciation, naturalness or human listening acceptance.'},indent=2))
 del decoded
print(json.dumps({'phase':'audio_continuity_complete','reference_frames_compared':n}),flush=True)
