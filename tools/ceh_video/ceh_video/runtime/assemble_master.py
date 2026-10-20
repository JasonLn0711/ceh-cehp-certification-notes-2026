from ceh_video.common import project_root, Project
#!/usr/bin/env python3
"""Join frame-exact video chapters with one continuously encoded narration track."""
from pathlib import Path
import json,subprocess,time
from contextlib import contextmanager
from ceh_video.common import sha,write
import soundfile as sf
MASTER_FILENAME=Project(project_root()).profile['master_filename']
ROOT=project_root();OUT=ROOT.parent/'output';QA=ROOT.parent/'qa'
@contextmanager
def stage(name,rows):
 started=time.monotonic()
 print(json.dumps({'phase':name,'state':'start'}),flush=True)
 try:
  yield
 except BaseException:
  rows.append({'phase':name,'status':'failed','elapsed_seconds':time.monotonic()-started})
  write(QA/'master-stage-timing.json',{'stages':rows});raise
 else:
  row={'phase':name,'status':'completed','elapsed_seconds':time.monotonic()-started};rows.append(row)
  write(QA/'master-stage-timing.json',{'stages':rows});print(json.dumps(row),flush=True)
def metadata_lines(profile,chapters):
 def escape(text):return text.replace('\\','\\\\').replace('=','\\=').replace(';','\\;').replace('#','\\#')
 marks=[';FFMETADATA1','title='+escape(profile.get('metadata_title',profile['title']))]
 for c in chapters:
  title=escape(c['id']+' '+c['title'])
  start=c.get('start_sample',round(c['start']*48000));duration=c.get('duration_samples',round(c['duration']*48000))
  marks.extend(['[CHAPTER]','TIMEBASE=1/48000','START='+str(start),'END='+str(start+duration),'title='+title])
 return marks
def main():
 rows=[];started=time.monotonic()
 m=json.load(open(ROOT/'data/master-timing.json'));audio=ROOT/'assets/audio/master.wav';total=0
 with sf.SoundFile(audio,'w',samplerate=48000,channels=2,subtype='PCM_16') as dest:
  for row in m['scenes']:
   data,sr=sf.read(ROOT/'assets/voice'/f'{row["scene"]}.wav',dtype='int16',always_2d=True);assert sr==48000 and data.shape[1]==2 and len(data)%1600==0;dest.write(data);total+=len(data)
 assert total==m.get('samples',m['frames']*1600) and total==m['frames']*1600
 assert sum(c.get('duration_samples',round(c['duration']*48000)) for c in m['chapters'])==total
 rows.append({'phase':'pcm_assembly','status':'completed','elapsed_seconds':time.monotonic()-started})
 concat=QA/'chapter-concat.txt';lines=[]
 for c in m['chapters']:
  f=OUT/'chapters'/f'{c["id"]}.mp4';assert f.exists();lines.extend(["file '"+str(f)+"'",f'duration {c.get("duration_samples",round(c["duration"]*48000))/48000:.9f}'])
 concat.write_text('\n'.join(lines)+'\n');target=OUT/MASTER_FILENAME
 metadata=QA/'chapter-metadata.ffmeta';marks=metadata_lines(Project(ROOT).profile,m['chapters'])
 metadata.write_text('\n'.join(marks)+'\n')
 from ceh_video.master_audio_cache import audio_key,cached_audio,retain_audio
 with stage('continuous_aac_cache_lookup',rows):
  key=audio_key(audio,total,Project(ROOT).profile);cache=ROOT/'.production/master-audio'
  cached=cached_audio(cache,key)
  audio_input=cached or audio
  audio_codec=['-c:a','copy'] if cached else ['-c:a','aac','-b:a','192k','-ar','48000']
 print(json.dumps({'phase':'continuous_aac_cache','reused':bool(cached),'pcm_sha256':key['pcm_sha256']}),flush=True)
 print(json.dumps({'phase':'assembling_continuous_master','chapters':len(m['chapters']),'duration':m['duration'],'embedded_chapter_marks':len(m['chapters'])}),flush=True)
 with stage('aac_copy_and_mux_faststart' if cached else 'aac_encode_and_mux_faststart',rows):
  with (QA/'master-assembly.log').open('w') as log:
   subprocess.run(['ffmpeg','-y','-v','warning','-progress',str(QA/'master-assembly.progress'),'-f','concat','-safe','0','-i',str(concat),'-i',str(audio_input),'-f','ffmetadata','-i',str(metadata),'-map_metadata','2','-map_chapters','2','-map','0:v:0','-map','1:a:0','-c:v','copy',*audio_codec,'-movflags','+faststart','-t',format(total/48000,'.9f'),str(target)],check=True,stdout=log,stderr=log)
 # Count actual decoded frames and inspect black/error intervals in one pass.
 # The metadata probe is cheap; it is explicitly not frame-count evidence.
 from ceh_video.media_scan import scan_master
 with stage('full_decode_count_black_integrity',rows):scan=scan_master(target,m['frames'],QA)
 with stage('retain_continuous_aac',rows):
  if audio_key(audio,total,Project(ROOT).profile)!=key:raise ValueError('PCM or audio recipe changed during assembly')
  retained=retain_audio(target,cache,key)
  write(QA/'master-audio-cache.json',{'reused':bool(cached),'key':key,'audio_sha256':sha(retained),'master_sha256':scan['master_sha256'],'scope':'Encoding reuse only; full audio QA remains mandatory'})
 with stage('metadata_probe',rows):probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-show_chapters','-of','json',str(target)]))
 v=next(s for s in probe['streams'] if s['codec_type']=='video')
 v['nb_read_frames']=str(scan['decoded_frames'])
 probe['ceh_frame_count_evidence']={'method':'ffmpeg_full_decode_progress','receipt':'master-full-decode.json','master_sha256':scan['master_sha256']}
 assert abs(float(v['duration'])-m['duration'])<.001
 assert len(probe['chapters'])==len(m['chapters'])
 for actual,expected in zip(probe['chapters'],m['chapters']):
  assert abs(float(actual['start_time'])-expected['start'])<.002 and abs(float(actual['end_time'])-expected['start']-expected['duration'])<.002
 reference=OUT/'master.reference.pcm.wav'
 with stage('retain_pcm_reference',rows):
  if not reference.exists() or sha(reference)!=sha(audio):
   import shutil;shutil.copyfile(audio,reference)
 write(QA/'master-stage-timing.json',{'stages':rows,'wall_seconds':time.monotonic()-started})
 (QA/'master-ffprobe.json').write_text(json.dumps(probe,indent=2));print(json.dumps({'master':str(target),'frames':m['frames'],'duration':m['duration']}))
if __name__=='__main__':main()
