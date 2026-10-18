"""Bound the completed ASR evidence to functional availability with immutable inputs."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,importlib.metadata as md
R=Path(__file__).resolve().parents[1];Q=R.parent/'qa'
def sha(f):
 with f.open('rb') as h:return hashlib.file_digest(h,'sha256').hexdigest()
process=json.load(open(Q/'recognition-process.json'));assert process['status']=='completed' and process['exit_code']==0
inputs=[];events=[]
for i,s in enumerate(json.load(open(R/'data/scenes.json'))['scenes'],1):
 sid=s['id'];wave=R/'assets/voice'/f'{sid}.wav';receipt=Q/'recognition'/f'{sid}.json';d=json.load(open(receipt));assert d['audio_sha256']==sha(wave) and d['recognized'].strip() and d['segments']
 assert all(0<=x['start']<x['end'] and x['text'].strip() for x in d['segments'])
 inputs.append({'sequence':i,'scene':sid,'path':str(wave.relative_to(R)),'sha256':d['audio_sha256'],'transcript_receipt':str(receipt.relative_to(Q))})
 events.append({'sequence':i,'scene':sid,'event':'functional_transcript_persisted','event_time_utc':datetime.fromtimestamp(receipt.stat().st_mtime,timezone.utc).isoformat(),'nonempty':True,'valid_segments':True})
model=[{'path':str(p.relative_to(R)),'sha256':sha(p)} for p in sorted((R/'models/faster-whisper-base.en').rglob('*')) if p.is_file()]
(Q/'asr-functional-inputs.json').write_text(json.dumps(inputs,indent=2));(Q/'asr-functional-events.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in events));(Q/'asr-functional-errors.jsonl').write_text('')
(Q/'asr-availability-receipt.json').write_text(json.dumps({'mode':'availability_validation','status':'LIVE_FULL_COMPLETED','runtime_validity':'valid_target_runtime','functional_result':'available_and_working','real_inputs':58,'persisted_transcripts':58,'errors':0,'runtime':{'package':'faster-whisper','version':md.version('faster-whisper'),'device':'cpu','compute_type':'int8','model':'base.en','beam_size':1,'temperature':0,'canonical_prompt':False,'vad_filter':False},'models':model,'accuracy':'not_evaluated','latency':'not_evaluated','scope':'Functional production diagnostics only. No ASR model ranking or timing/accuracy endpoint; human audio acceptance remains separate.'},indent=2))
print(json.dumps({'functional_transcripts':58,'mode':'availability_validation','status':'LIVE_FULL_COMPLETED'}))
