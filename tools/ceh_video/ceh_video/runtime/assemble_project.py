from ceh_video.common import project_root, Project
#!/usr/bin/env python3
"""Assemble full root preview without modifying checked chapter compositions."""
from build_film import ROOT,host
import json,re
scenes=json.load(open(ROOT/'data/scenes.json'))['scenes'];ready=[];ledger=[]
for scene in scenes:
 sid=scene['id'];audio=json.load(open(ROOT/'data'/f'{sid}.audio.json'));ch=scene['chapter_id']
 normalize=lambda b:re.sub(rb' data-hf-id="[^"]*"',b'',b)
 assert normalize((ROOT/'compositions'/f'{sid}.html').read_bytes())==normalize((ROOT/'chapters'/ch/'compositions'/f'{sid}.html').read_bytes())
 motion=json.load(open(ROOT/'compositions'/f'{sid}.motion.json'));caps=json.load(open(ROOT/'data'/f'{sid}.captions.json'))
 ready.append((scene,audio));ledger.append({'scene':sid,'duration':audio['duration'],'movements':len(motion['moves']),'captions':len(caps),'chapter':ch,'status':'see chapter render evidence'})
assert len(ready)==len(Project(project_root()).scenes)
(ROOT/'index.html').write_text(host(ready,'master'))
(ROOT/'data/build-ledger.json').write_text(json.dumps(ledger,indent=2))
print(json.dumps({'assembled_scenes':len(Project(project_root()).scenes),'duration':sum(a['duration'] for s,a in ready)}))
