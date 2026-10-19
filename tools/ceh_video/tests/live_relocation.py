"""Exercise first-run verified audio import with the original locator unavailable."""
from pathlib import Path
import argparse,shutil,json
from ceh_video.common import Project,read,write,sha
from ceh_video.runner import seed_audio

parser=argparse.ArgumentParser();parser.add_argument('--project',required=True);args=parser.parse_args()
source=Project(args.project);base=source.root.parent/'relocation-fixture';root=base/'project'
assert not base.exists(),'Preserve previous relocation evidence'
shutil.copytree(source.root.parent/'integration-fixture/project',root,
                ignore=shutil.ignore_patterns('.production','review','__pycache__'))
(base/'qa').mkdir();(base/'output').mkdir()
p=Project(root)
write(p.qa/'reference-import.json',{'reference':'/unavailable/original-workspace',
      'reference_manifest_sha256':read(source.qa/'reference-import.json')['reference_manifest_sha256']})
write(p.qa/'reference-audio-identities.json',{'scenes':{s['id']:sha(source.root/'assets/voice'/f'{s["id"]}.wav') for s in p.scenes},'voice':p.profile['voice'],'models':p.profile['models']})
seed_audio(p)
assert read(p.state/'audio-import.json')['status']=='verified_reference_audio_and_alignment_imported'
result={'status':'passed','scenes':len(p.scenes),'original_workspace':'unavailable',
        'speech_cache_entries':len(list((p.state/'speech-cache').glob('*/receipt.json'))),
        'actual_original_locator_reads_required':False,'new_model_inferences':0,
        'scope':'Actual first-run import of shipped PCM, clip recipes and alignment. Model regeneration and rendering have their own evidence.'}
write(source.qa/'live-relocation.json',result);print(json.dumps(result))
