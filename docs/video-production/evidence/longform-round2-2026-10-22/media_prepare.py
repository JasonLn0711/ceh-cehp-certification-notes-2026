from pathlib import Path
import shutil,json
from ceh_video.common import Project,write
from ceh_video.mandarin import action
from ceh_video.progress import Progress
from types import SimpleNamespace
src=Path('/home/jnlngx10/Videos/Island_Workshop_MATLAB_Concepts_v3_images_gpu/project')
dest=Path('/home/jnlngx10/Videos/longform-round2-2026-10-22/media-optimized/project')
dest.mkdir(parents=True)
for folder in ['assets/fonts','assets/vendor','assets/teaching']:
 if (src/folder).exists():shutil.copytree(src/folder,dest/folder)
for name in ['production.json','hyperframes.json','package.json','package-lock.json','pronunciation.json']:
 shutil.copy2(src/name,dest/name)
for name in ['node_modules','.venv']:(dest/name).symlink_to((src/name).resolve())
(dest/'scripts').mkdir()
for cue in (src/'scripts').glob('cues_*.json'):shutil.copy2(cue,dest/'scripts'/cue.name)
(dest/'data').mkdir();(dest/'compositions').mkdir();(dest/'assets/voice').mkdir()
scenes=[s for s in json.loads((src/'data/scenes.json').read_text())['scenes'] if s['id'] in ['S01','S05']]
write(dest/'data/scenes.json',{'scenes':scenes})
qs=json.loads((src/'data/questions.json').read_text());qs['questions']=[q for q in qs['questions'] if q['scene_id']=='S05'];write(dest/'data/questions.json',qs)
for name in ['chapters.json','teaching-panels.json','teaching-assets.json','coverage.json']:
 shutil.copy2(src/'data'/name,dest/'data'/name)
for s in scenes:
 sid=s['id']
 for suffix in ['audio.json','captions.json','geometry.json','panels.json']:
  p=src/'data'/f'{sid}.{suffix}'
  if p.exists():shutil.copy2(p,dest/'data'/p.name)
 for suffix in ['html','motion.json']:shutil.copy2(src/'compositions'/f'{sid}.{suffix}',dest/'compositions'/f'{sid}.{suffix}')
 shutil.copy2(src/'assets/voice'/f'{sid}.wav',dest/'assets/voice'/f'{sid}.wav')
(dest.parent/'qa').mkdir();(dest.parent/'output').mkdir()
p=Project(dest)
action(p,SimpleNamespace(name='prepare:C01'),Progress(plain=True))
print(json.dumps({'project':str(dest),'duration':sum(p.audio(s['id'])['duration'] for s in scenes)}))
