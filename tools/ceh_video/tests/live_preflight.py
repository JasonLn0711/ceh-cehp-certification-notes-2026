"""Actual source-failure checks in a separate fixture, with no model inference."""
from pathlib import Path
import argparse, json, shutil, subprocess
from ceh_video.common import Project,read,write

parser=argparse.ArgumentParser();parser.add_argument('--project',required=True);args=parser.parse_args()
source=Project(args.project);base=source.root.parent/'preflight-fixture';root=base/'project'
assert not base.exists(),'Preserve earlier evidence; choose a new fixture directory'
shutil.copytree(source.root.parent/'integration-fixture/project',root,
                ignore=shutil.ignore_patterns('.production','review','__pycache__'))
(base/'qa').mkdir();(base/'output').mkdir()
profile=read(root/'production.json');profile['runtime']=source.profile['runtime'];write(root/'production.json',profile)
for rel in profile['locked_assets']:
    target=root/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source.root/rel,target)
results=[]
def attempt(name,expected=None):
    p=Project(root)
    run=subprocess.run([str(source.root/'.venv/bin/python'),'-m','ceh_video','--project',str(root),'preflight'],
                       env=p.environment(),capture_output=True,text=True)
    receipt=read(base/'qa/preflight.json')
    if expected:
        assert run.returncode!=0 and expected in str(receipt['errors']),(name,run.stdout,run.stderr)
    else:assert run.returncode==0,(name,run.stdout,run.stderr)
    results.append({'scenario':name,'status':'passed','actual_exit_code':run.returncode,'errors':receipt['errors']})
attempt('actual_diagram_and_anchor_baseline')
art=root/'scripts/scene_art_mid.py';original=art.read_text()
try:
    art.write_text(original.replace('def render(scene, audio):','def render(scene, audio):\n    return UNDEFINED_PALETTE_TOKEN'))
    attempt('unknown_palette_fails_before_models','UNDEFINED_PALETTE_TOKEN')
finally:art.write_text(original)
cue=next(f for f in (root/'scripts').glob('cues_*.json') if 'S24' in read(f));original=cue.read_text()
try:
    value=read(cue);value['S24'][0]='absent narration anchor fixture';write(cue,value)
    attempt('missing_narration_anchor_fails_before_models','missing spoken anchor')
finally:cue.write_text(original)
# Bring an actual long quiz scene into the small fixture, then exceed its real layout budget.
scene=source.by_id['S55'];data=read(root/'data/scenes.json');data['scenes'].append(scene);write(root/'data/scenes.json',data)
question=next(q for q in source.questions if q['scene_id']=='S55');write(root/'data/questions.json',{'questions':[question]})
shutil.copy2(source.root/'data/S55.audio.json',root/'data/S55.audio.json')
profile['expected'].update(scenes=3,chapters=2,questions=1,canonical_words=sum(len(s['narration_en_US'].split()) for s in data['scenes']))
write(root/'production.json',profile);attempt('actual_long_quiz_baseline')
question['prompt']=' '.join([question['prompt']]*15);write(root/'data/questions.json',{'questions':[question]})
attempt('oversize_quiz_fails_before_render','Quiz requires more room')
write(source.qa/'live-preflight.json',{'status':'passed','real_model_inferences':0,'scenarios':results,'scope':'Actual diagram construction and quiz geometry in an isolated fixture; failures occur before expensive execution.'})
print(json.dumps(results))
