from ceh_video.common import project_root, Project
"""Replace only production storyboard estimates/status with checked measured scene timing."""
from pathlib import Path
import json,re
R=project_root();Q=R.parent/'qa'
check=json.load(open(Q/'master-project-check.json'));assert check['ok'] and not check['browserSkipped']
seek=json.load(open(Q/'scene-seek-audit.json'));assert seek['status']=='passed' and seek['scenes']==len(Project(R).scenes)
m=json.load(open(R/'data/master-timing.json'));byid={x['scene']:x for x in m['scenes']}
p=R/'STORYBOARD.md';s=p.read_text();chunks=re.split(r'(?=^## Frame \d+)',s,flags=re.M);changed=0
for i,chunk in enumerate(chunks):
 match=re.search(r'^- src: compositions/(S\d+)\.html$',chunk,re.M)
 if not match:continue
 sid=match.group(1);row=byid[sid];chunk=re.sub(r'^- status: .*$', '- status: animated',chunk,flags=re.M)
 chunk=re.sub(r'^- duration: .*$',f'- duration: {row["duration"]:.9f}s',chunk,flags=re.M);chunks[i]=chunk;changed+=1
assert changed==len(Project(R).scenes)
s=''.join(chunks).replace('Durations below are estimates until replaced by actual measured speech.','Durations below are measured from the final 48kHz sample ledgers. Animated status records checked native motion; actual chapter/master render acceptance is held by the separate QA receipts.')
p.write_text(s.rstrip()+'\n');print(json.dumps({'phase':'storyboard_measured_timing_synchronized','scenes':changed,'duration':m['duration'],'authoring_status':'animated','render_acceptance':'separate chapter/master receipts'}))
