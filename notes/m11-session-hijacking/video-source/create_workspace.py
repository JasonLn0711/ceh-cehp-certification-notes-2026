"""Create only the new M11 workspace; never copy historical derived media or QA."""
from pathlib import Path
import json,shutil,hashlib,sys,importlib.metadata
SOURCE=Path(__file__).resolve().parent
REPO=SOURCE.parents[2]
reference=Path('/home/jnlngx10/Videos/CEH_M10_efficiency_v1_2/project')
workspace=Path('/home/jnlngx10/Videos/CEH_M11_initial_v1')
assert not workspace.exists(),'Resume existing workspace explicitly'
root=workspace/'project';root.mkdir(parents=True)
for name in ('qa','output','inputs'):(workspace/name).mkdir()
for name in ('data','scripts','compositions','provenance'):(root/name).mkdir()
for name in ('models','design'):
 shutil.copytree(reference/name,root/name)
shutil.copytree(reference/'assets',root/'assets',ignore=lambda folder,names:[n for n in names if Path(folder)==reference/'assets' and n in ('audio','voice','voice-baseline')])
for name in ('.venv','node_modules'):(root/name).symlink_to((reference/name).resolve(),target_is_directory=True)
for name in ('STYLE_TOKENS.json','network_map.json','pronunciation.json','hyperframes.json','package.json','package-lock.json','requirements-lock.txt'):
 if (reference/name).exists():shutil.copy2(reference/name,root/name)
profile=json.loads((reference/'production.json').read_text())
# Immutable files not included by normal source directories retain exact bytes.
for rel,h in profile['locked_assets'].items():
 target=root/rel
 if not target.exists():target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(reference/rel,target)
 assert hashlib.sha256(target.read_bytes()).hexdigest()==h,rel
profile.update(module='M11',engine_version='0.5.4',release='initial-series-v1',title='CEH M11 Session Hijacking English Masterclass',metadata_title='CEH M11 Session Hijacking English Masterclass',master_filename='CEH_M11_Session_Hijacking_en-US_Editorial_v1_master.mp4',editable_filename='CEH_M11_English_Masterclass_v1_EDITABLE.zip',source_package='../inputs/CEH_M11_English_Masterclass',scene_specs='data/scene-specs.json',representative_scenes=['S01','S06','S14','S18','S26','S30','S37','S44','S48'])
for old in ('source_reference','migration','reference_project'):profile.pop(old,None)
scenes=json.loads((SOURCE/'scenes.json').read_text())['scenes'];quiz=json.loads((SOURCE/'quiz.json').read_text())['questions'];qs={q['scene_id'] for q in quiz}
profile['expected']=dict(scenes=len(scenes),chapters=len({s['chapter_id'] for s in scenes}),questions=8,canonical_words=sum(len(s['narration_en_US'].split()) for s in scenes))
profile['semantic_scenes']=[s['id'] for s in scenes if s['id'] not in qs]
profile['diagram_inputs']={s['id']:['data/scene-specs.json'] for s in scenes if s['id'] not in qs}
profile['baseline_runtime']={'python':sys.version.split()[0],**{name:importlib.metadata.version(name) for name in ('kokoro-onnx','onnxruntime','numpy','soundfile')}}
(root/'production.json').write_text(json.dumps(profile,indent=2)+'\n')
for source,dest in [('scenes.json','data/scenes.json'),('quiz.json','data/questions.json'),('scene-specs.json','data/scene-specs.json'),('cues_m11.json','scripts/cues_m11.json')]:shutil.copy2(SOURCE/source,root/dest)
(root/'data/voice-calibration.json').write_text(json.dumps(dict(
 baseline_speed=.73,voice='af_heart',status='inherited_approved_baseline',
 source='CEH English initial series standard; no recalibration'),indent=2)+'\n')
(root/'scripts/scene_art.py').write_text('def build(scene,audio):\n    raise RuntimeError("M11 uses the source-bound remaster compiler")\n')
# Legacy import contract is maintained, but no M10 diagram implementation is invoked.
shutil.copy2(reference/'scripts/art_common.py',root/'scripts/art_common.py')
engine=REPO/'tools/ceh_video/ceh_video'
shutil.copytree(engine,root/'vendor/ceh_video',ignore=shutil.ignore_patterns('__pycache__','node_modules'))
(root/'vendor/ceh_video/visual/node_modules').symlink_to((engine/'visual/node_modules').resolve(),target_is_directory=True)
for script in (engine/'runtime').glob('*.py'):
 (root/'scripts'/script.name).write_text('import os,sys\nfrom pathlib import Path\nr=Path(__file__).resolve().parents[1]\nos.environ["CEH_VIDEO_PROJECT"]=str(r)\nsys.path.insert(0,str(r/"vendor"))\nfrom ceh_video.worker import main\nsys.argv=[sys.argv[0],'+repr(script.stem)+',*sys.argv[1:]]\nmain()\n')
(root/'scripts/production_settings.py').write_text('from ceh_video.common import Project,project_root\nMASTER_FILENAME=Project(project_root()).profile["master_filename"]\ndef quiz_seconds():return 1\ndef quiz_label():return "1 second each"\n')
for name in ('audit_quiz.mjs','audit_scene_seek.mjs'):shutil.copy2(engine/'runtime'/name,root/'scripts'/name)
source_package=workspace/'inputs/CEH_M11_English_Masterclass'
shutil.copytree(SOURCE,source_package,ignore=shutil.ignore_patterns('__pycache__'))
shutil.copy2(SOURCE/'quiz.json',source_package/'questions.json')
(root/'BRIEF.md').write_text('''---
workflow: general-video
flow: automation
storyboard: no
---
# CEH M11 English Masterclass

User-authorized complete M11 Session Hijacking film under the adopted initial series baseline. Retain M04 editorial art, Tally, Northstar, fonts and English voice. Music off. 1920x1080/30. 48 source scenes, eleven chapters, eight questions. Duration follows measured spoken PCM; no target-WPM changes. Fresh workspace; no inherited media/QA acceptance. Runtime pins retained for reproducibility. Full human listening remains separate. No public upload.
''')
print(root)
