#!/usr/bin/env python3
"""Join frame-exact video chapters with one continuously encoded narration track."""
from pathlib import Path
import json,subprocess
import soundfile as sf
from production_settings import MASTER_FILENAME
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT.parent/'output';QA=ROOT.parent/'qa'
def main():
 m=json.load(open(ROOT/'data/master-timing.json'));audio=ROOT/'assets/audio/master.wav';total=0
 with sf.SoundFile(audio,'w',samplerate=48000,channels=2,subtype='PCM_16') as dest:
  for row in m['scenes']:
   data,sr=sf.read(ROOT/'assets/voice'/f'{row["scene"]}.wav',dtype='int16');assert sr==48000;dest.write(data);total+=len(data)
 assert total==round(m['duration']*48000)
 concat=QA/'chapter-concat.txt';lines=[]
 for c in m['chapters']:
  f=OUT/'chapters'/f'{c["id"]}.mp4';assert f.exists();lines.extend(["file '"+str(f)+"'",f'duration {c["duration"]:.9f}'])
 concat.write_text('\n'.join(lines)+'\n');target=OUT/MASTER_FILENAME
 metadata=QA/'chapter-metadata.ffmeta';marks=[';FFMETADATA1','title=CEH M10 Denial of Service English Masterclass']
 for c in m['chapters']:
  title=(c['id']+' '+c['title']).replace('\\','\\\\').replace('=','\\=').replace(';','\\;').replace('#','\\#')
  marks.extend(['[CHAPTER]','TIMEBASE=1/48000','START='+str(round(c['start']*48000)),'END='+str(round((c['start']+c['duration'])*48000)),'title='+title])
 metadata.write_text('\n'.join(marks)+'\n')
 print(json.dumps({'phase':'assembling_continuous_master','chapters':len(m['chapters']),'duration':m['duration'],'embedded_chapter_marks':11}),flush=True)
 with (QA/'master-assembly.log').open('w') as log:
  subprocess.run(['ffmpeg','-y','-v','warning','-f','concat','-safe','0','-i',str(concat),'-i',str(audio),'-f','ffmetadata','-i',str(metadata),'-map_metadata','2','-map_chapters','2','-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart','-t',str(m['duration']),str(target)],check=True,stdout=log,stderr=log)
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-show_chapters','-of','json',str(target)]));v=next(s for s in probe['streams'] if s['codec_type']=='video');assert int(v['nb_read_frames'])==m['frames'];assert abs(float(v['duration'])-m['duration'])<.001
 assert len(probe['chapters'])==11
 for actual,expected in zip(probe['chapters'],m['chapters']):
  assert abs(float(actual['start_time'])-expected['start'])<.002 and abs(float(actual['end_time'])-expected['start']-expected['duration'])<.002
 reference=OUT/'master.reference.pcm.wav'
 if not reference.exists():
  import shutil;shutil.copyfile(audio,reference)
 (QA/'master-ffprobe.json').write_text(json.dumps(probe,indent=2));print(json.dumps({'master':str(target),'frames':m['frames'],'duration':m['duration']}))
if __name__=='__main__':main()
