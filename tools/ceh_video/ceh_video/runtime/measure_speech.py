from ceh_video.common import project_root, Project
#!/usr/bin/env python3
"""Measure final speech clips, distinguishing model edge padding from signal duration."""
from pathlib import Path
import hashlib,json
import numpy as np
import soundfile as sf
R=project_root();Q=R.parent/'qa'
def main():
 words=0;raw=0;durations={-60:0.,-50:0.,-40:0.};rows=[]
 for f in sorted((R/'data').glob('S*.audio.json')):
  for s in json.loads(f.read_text())['segments']:
   if s['kind']!='spoken':continue
   wav=R/s['path'];assert hashlib.sha256(wav.read_bytes()).hexdigest()==s['sha256'];a,sr=sf.read(wav);assert sr==48000 and a.shape[1]==2
   mono=np.max(np.abs(a),axis=1);win=480;count=len(mono)//win;energy=np.sqrt(np.mean(mono[:count*win].reshape(-1,win)**2,axis=1));seconds={}
   for db in durations:
    active=np.flatnonzero(energy>=10**(db/20));assert len(active)
    start=max(0,int(active[0])*win-480);end=min(len(a),(int(active[-1])+1)*win+480)
    seconds[str(db)]=(end-start)/sr;durations[db]+=seconds[str(db)]
   raw+=len(a)/sr;words+=len(s['canonical'].split());rows.append({'scene':f.name[:3],'sentence':s['sentence'],'audio_sha256':s['sha256'],'raw_seconds':len(a)/sr,'edge_trimmed_seconds_by_dbfs':seconds})
   if len(rows)%100==0:print(json.dumps({'phase':'measuring_final_speech','clips_measured':len(rows)}),flush=True)
 result={'method':'Canonical words / final processed clip duration. Edge-trimmed estimate uses 10ms RMS windows, first/last window above threshold, with 10ms guard at both edges; internal pauses retained. Measurement only: no audio samples changed.','primary_threshold_dbfs':-50,'canonical_words':words,'clips':len(rows),'raw_clip_seconds':raw,'raw_clip_wpm':words*60/raw,'sensitivity':[{'threshold_dbfs':db,'edge_trimmed_seconds':v,'edge_trimmed_wpm':words*60/v,'removed_edge_seconds':raw-v} for db,v in durations.items()],'clips_measured':rows,'scope':'Signal-threshold estimate, not perceptual intelligibility or pronunciation accuracy.'}
 (Q/'speech-rate-measurement.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='clips_measured'}))
if __name__=='__main__':main()
