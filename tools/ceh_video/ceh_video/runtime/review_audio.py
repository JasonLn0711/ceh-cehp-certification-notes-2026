from ceh_video.common import project_root, Project
#!/usr/bin/env python3
"""Preserve functional transcript receipts and forced-alignment uncertainty."""
from pathlib import Path
import json,hashlib
R=project_root();Q=R.parent/'qa'
rows=[];flags=[]
for scene in json.load(open(R/'data/scenes.json'))['scenes']:
 sid=scene['id'];r=json.load(open(Q/'recognition'/f'{sid}.json'));assert r['audio_sha256']==hashlib.sha256((R/'assets/voice'/f'{sid}.wav').read_bytes()).hexdigest();assert r['recognized'].strip() and r['accuracy']=='not_evaluated' and r['latency']=='not_evaluated'
 rows.append({'scene':sid,'audio_sha256':r['audio_sha256'],'functional_transcript':True,'canonical':r['canonical'],'recognized':r['recognized']})
 for f in sorted((R/'data/forced-alignment').glob(sid+'-*.json')):
  d=json.load(open(f))
  for flag in d['review_flags']:flags.append({'file':f.name,'canonical':d['canonical'],'word_text':d['words'][flag['word']]['text'],**flag})
(Q/'audio-review-diagnostics.json').write_text(json.dumps({'mode':'availability_validation','status':'LIVE_FULL_COMPLETED','runtime':'valid_target_runtime','functional_result':'available_and_working','accuracy':'not_evaluated','latency':'not_evaluated','scope':'Actual fixed-runtime unprompted transcript receipts. Known-text forced alignment drives canonical captions; its flags locate timing uncertainty. Human listening acceptance is separate.','scenes':rows,'alignment_flags':flags},indent=2))
print(json.dumps({'functional_scenes':len(rows),'alignment_flags':len(flags),'accuracy':'not_evaluated','latency':'not_evaluated'}))
