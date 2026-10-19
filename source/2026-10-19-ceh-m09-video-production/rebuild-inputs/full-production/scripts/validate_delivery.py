#!/usr/bin/env python3
"""M09 evidence gates for complete rendered media, separate from source acceptance."""
from pathlib import Path
import json,re,hashlib,csv
import numpy as np
import soundfile as sf
from chapter import fingerprint
from production_settings import MASTER_FILENAME
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT.parent/'output';QA=ROOT.parent/'qa';SOURCE=ROOT.parent/'inputs/package/CEH_M09_English_Editorial_Masterclass'
def sha(f):
 with f.open('rb') as h:return hashlib.file_digest(h,'sha256').hexdigest()
def main():
 scenes=json.loads((ROOT/'data/scenes.json').read_text())['scenes'];assert len(scenes)==58
 assert json.loads((SOURCE/'scenes.json').read_text())==json.loads((ROOT/'data/scenes.json').read_text()),'canonical M09 content changed'
 for f in SOURCE.glob('*.json'):
  if f.name!='scenes.json':assert sha(f)==sha(ROOT/'data'/f.name),f.name
 manifest=[]
 for line in (SOURCE/'FILES_SHA256.txt').read_text().splitlines():
  if not line.strip() or line.startswith('#'):continue
  h,name=line.split(None,1);name=name.lstrip('* ');assert sha(SOURCE/name)==h,name;manifest.append(name)
 for rel,h in json.loads((SOURCE/'LOCKED_SOURCE_SHA256.json').read_text())['sha256'].items():
  target=ROOT/rel
  if not target.exists():target=ROOT/'data'/rel
  assert sha(target)==h,('locked asset changed',rel)
 normalize=lambda b:re.sub(rb' data-hf-id="[^"]*"',b'',b)
 assert (ROOT/'index.html').read_text().count('data-composition-src=')==58
 check=json.loads((QA/'master-project-check.json').read_text());assert check['ok'] and not check['browserSkipped']
 for layer in ['lint','runtime','layout','contrast']:assert check[layer]['errorCount']==0 and check[layer]['warningCount']==0,layer
 cfg=json.loads((ROOT/'data/voice-calibration.json').read_text());words=0;spoken=baseline=cursor=0;pauses=[];rows=[];caps=[];flags=[]
 for scene in scenes:
  sid=scene['id'];ch=scene['chapter_id'];name=sid+'.html'
  assert normalize((ROOT/'compositions'/name).read_bytes())==normalize((ROOT/'chapters'/ch/'compositions'/name).read_bytes())
  a=json.loads((ROOT/'data'/f'{sid}.audio.json').read_text());assert a['baseline_speed']==cfg['baseline_speed']
  audio=ROOT/'assets/voice'/f'{sid}.wav';pcm,sr=sf.read(audio);assert sr==48000 and pcm.shape==(a['samples'],2) and len(pcm)%1600==0 and np.max(np.abs(pcm))<1
  joined=' '.join(r['canonical'] for r in a['segments'] if r['kind']=='spoken');assert joined==' '.join(scene['narration_en_US'].split())
  for r in a['segments']:
   if r['kind']=='spoken':
    assert r['speed_applications']==1 and sha(ROOT/r['path'])==r['sha256'];recipe=json.loads((ROOT/r['path']).with_suffix('.json').read_text());assert recipe['atempo']==1.5 and recipe['baseline_speed']==.73 and recipe['speed_applications']==1;duration=(r['end_sample']-r['start_sample'])/sr
    assert abs(r['baseline_seconds']/duration-1.5)<.1,(sid,r['sentence'],'speed ratio')
    words+=len(r['canonical'].split());spoken+=duration;baseline+=r['baseline_seconds']
    align=json.loads((ROOT/'data/forced-alignment'/f'{sid}-{r["sentence"]:03}.json').read_text());assert align['audio_sha256']==r['sha256'];flags.extend({'scene':sid,'sentence':r['sentence'],**v} for v in align['review_flags'])
   else:
    zero=pcm[r['start_sample']:r['end_sample']];assert r['seconds']==1 and zero.shape==(48000,2) and not np.any(zero);pauses.append(r)
  c=json.loads((ROOT/'data'/f'{sid}.captions.json').read_text());assert ' '.join(v['text'] for v in c)==joined
  for v in c:
   assert 0<=v['start']<v['end']<=a['duration']
   for hold in [seg for seg in a['segments'] if seg['kind']=='silence']:assert v['end']<=hold['start_sample']/48000+.00001 or v['start']>=hold['end_sample']/48000-.00001,(sid,'caption enters quiz silence',v)
   caps.append({'scene':sid,**v,'start':cursor+v['start'],'end':cursor+v['end']})
  asr=json.loads((QA/'recognition'/f'{sid}.json').read_text());assert asr['audio_sha256']==sha(audio) and asr['canonical']==scene['narration_en_US'] and asr['recognized'].strip() and asr['accuracy']=='not_evaluated' and asr['latency']=='not_evaluated'
  ccheck=json.loads((QA/f'{ch}-check.json').read_text());render=json.loads((QA/f'{ch}-render.json').read_text());assert ccheck['ok'] and not ccheck['browserSkipped'];assert render['status']=='rendered_codec_verified';assert fingerprint(ROOT/'chapters'/ch)==render['source_sha256'];assert sha(OUT/'chapters'/f'{ch}.mp4')==render['output_sha256']
  rows.append({'scene':sid,'chapter':ch,'authored':True,'implemented':True,'timed':True,'rendered':True,'start':cursor,'duration':a['duration'],'audio_sha256':sha(audio),'chapter_evidence':f'qa_evidence/{ch}-render.json','visual_review':f'qa_evidence/{ch}-visual-review.md'});cursor+=a['duration']
 assert words==9814 and len(pauses)==8
 clip_audit=json.load(open(QA/'audio-clip-structure-audit.json'));assert clip_audit['status']=='passed' and clip_audit['scenes']==58 and clip_audit['canonical_words']==words and len(clip_audit['quiz_holds'])==8
 raw_wpm=words*60/spoken
 rate=json.loads((QA/'speech-rate-measurement.json').read_text());assert rate['canonical_words']==words and abs(rate['raw_clip_seconds']-spoken)<.001
 assert {r['audio_sha256'] for r in rate['clips_measured']}=={r['sha256'] for scene in scenes for r in json.loads((ROOT/'data'/f"{scene['id']}.audio.json").read_text())['segments'] if r['kind']=='spoken'}
 wpm=next(x['edge_trimmed_wpm'] for x in rate['sensitivity'] if x['threshold_dbfs']==-50)
 assert all(a['end']<=b['start']+.001 for a,b in zip(caps,caps[1:])),'caption overlap'
 master=OUT/MASTER_FILENAME;probe=json.loads((QA/'master-ffprobe.json').read_text());v=next(s for s in probe['streams'] if s['codec_type']=='video');a=next(s for s in probe['streams'] if s['codec_type']=='audio')
 assert (v['codec_name'],v['width'],v['height'],v['r_frame_rate'],a['codec_name'],a['sample_rate'],a['channels'])==('h264',1920,1080,'30/1','aac','48000',2)
 assert int(v['nb_read_frames'])==round(cursor*30)
 assert len(probe['chapters'])==11,'Embedded chapter markers missing'
 artifact=json.loads((QA/'rendered-artifact-audit.json').read_text());assert artifact['decoded_entire_master'] and len(artifact['quiz_silence'])==8 and len(artifact['sampled_frames'])==115
 late=json.load(open(QA/'late-diagram-samples.json'));assert late['status']=='sampled_visual_checks_passed' and late['count']==54 and late['master_sha256']==sha(master)
 assert all((OUT/'inspection_frames'/r['file']).is_file() for r in late['samples'])
 assert (QA/'master-visual-review.md').is_file() and (QA/'audio-review.md').is_file() and (QA/'technical-source-review.md').is_file(),'Required concrete review records missing'
 assert 'review_status: pass' in (QA/'master-visual-review.md').read_text() and 'review_status: pass' in (QA/'technical-source-review.md').read_text()
 quiz=json.loads((QA/'quiz-runtime/checks.json').read_text());assert quiz['status']=='passed' and quiz['checks']==64
 seek=json.load(open(QA/'scene-seek-audit.json'));assert seek['status']=='passed' and seek['scenes']==58 and seek['comparisons']==174
 continuity=json.load(open(QA/'audio-continuity-audit.json'));assert continuity['status']=='passed' and continuity['all_reference_frames_compared'] and len(continuity['chapters'])==11
 with (OUT/'scene_qa_ledger.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 result={'source_hashes':len(manifest),'scenes':58,'chapters':11,'canonical_spoken_words':words,'baseline_seconds':baseline,'post_speed_spoken_seconds':spoken,'effective_spoken_wpm':wpm,'speech_wpm_method':'Edge-trimmed signal estimate at -50dBFS, 10ms RMS windows/guard; internal pauses retained; audio unchanged','raw_clip_wpm':raw_wpm,'measured_baseline_to_final_duration_ratio':baseline/spoken,'speed_method':'Exactly one atempo=1.5 on each native24k baseline speech clip, resampled to48k stereo','silence_intervals':8,'silent_seconds':8,'pcm_zero_frames_per_hold':48000,'pcm_channels':2,'aac_boundary_residues':'Measured and disclosed separately; not bit-exact zero claim','duration':cursor,'frames':round(cursor*30),'primary_encoded_samples':115,'targeted_late_encoded_samples':late['count'],'embedded_chapter_marks':11,'alignment_review_flags':flags,'source_corrections':'None; complete canonical M09 content preserved','master_sha256':sha(master),'status':'automated_delivery_checks_passed','review_limit':'Sampled visual review and ASR/waveform diagnostics; full human viewing/listening acceptance separate.'}
 (QA/'delivery-validation.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='alignment_review_flags'}))
if __name__=='__main__':main()
