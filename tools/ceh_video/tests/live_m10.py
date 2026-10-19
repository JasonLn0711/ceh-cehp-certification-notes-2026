"""Explicitly activated real M10 fixture execution; never edits the released project."""
from pathlib import Path
import argparse,collections,hashlib,json,os,shutil,subprocess,sys
from ceh_video.common import Project,read,write,sha
from ceh_video.speech import import_cache,synthesize,recipe,cache_entry
from ceh_video.graph import nodes,planning,commit_receipt,node_key

p=argparse.ArgumentParser();p.add_argument('--project',required=True);args=p.parse_args();source=Project(args.project)
base=source.root.parent/'integration-fixture';root=base/'project';assert not root.exists(),'Preserve earlier fixture evidence; choose a new run'
root.mkdir(parents=True);(base/'qa').mkdir();(base/'output').mkdir();(root/'data').mkdir();(root/'assets/voice').mkdir(parents=True);(root/'assets/voice-baseline').mkdir();(root/'models').symlink_to(source.root/'models',target_is_directory=True)
for folder in ['scripts','vendor']:
 shutil.copytree(source.root/folder,root/folder,ignore=shutil.ignore_patterns('__pycache__'))
for name in ['fonts','props','mascot','vendor']:shutil.copytree(source.root/'assets'/name,root/'assets'/name)
for name in ['hyperframes.json','pronunciation.json']:shutil.copy2(source.root/name,root/name)
profile=read(source.root/'production.json');profile['expected'].update(scenes=2,chapters=1,questions=0)
scenes=[s for s in source.scenes if s['id'] in {'S23','S24'}];profile['expected']['canonical_words']=sum(len(s['narration_en_US'].split()) for s in scenes)
write(root/'production.json',profile);write(root/'data/scenes.json',{'scenes':scenes});write(root/'data/questions.json',{'questions':[]});(root/'data/forced-alignment').mkdir()
for scene in scenes:
 sid=scene['id'];shutil.copy2(source.root/'data'/f'{sid}.audio.json',root/'data'/f'{sid}.audio.json')
 shutil.copy2(source.root/'assets/voice'/f'{sid}.wav',root/'assets/voice'/f'{sid}.wav')
 shutil.copytree(source.root/'assets/voice'/sid,root/'assets/voice'/sid);shutil.copytree(source.root/'assets/voice-baseline'/sid,root/'assets/voice-baseline'/sid)
 for f in (source.root/'data/forced-alignment').glob(sid+'-*.json'):shutil.copy2(f,root/'data/forced-alignment'/f.name)
p=Project(root);imported=import_cache(p);checks=[]
def emit(row):print(json.dumps(row),flush=True)
def proof(name,**fields):checks.append({'scenario':name,'status':'passed',**fields});emit(checks[-1])
before={str(f.relative_to(root)):sha(f) for f in (root/'assets/voice').rglob('*.wav')}
a=synthesize(p,'S24',emit);assert a['generated']==0;assert before['assets/voice/S24.wav']==sha(root/'assets/voice/S24.wav');proof('real_noop_speech_reconstruction',**a,pcm_identical=True)
# Expand one uniquely occurring lexical word using punctuation only; canonical fixture wording remains unchanged.
scene=p.by_id['S24'];counts=collections.Counter(__import__('re').findall(r'\b[A-Za-z]{6,}\b',scene['narration_en_US']));term=next(w for w,n in counts.items() if n==1 and w not in read(root/'pronunciation.json')['pronunciations'])
policy=read(root/'pronunciation.json');policy['pronunciations'][term]=term+',';write(root/'pronunciation.json',policy)
oldclips={f.name:sha(f) for f in (root/'assets/voice/S24').glob('*.wav')};a=synthesize(p,'S24',emit);assert a['generated']==1
changed=[f.name for f in (root/'assets/voice/S24').glob('*.wav') if sha(f)!=oldclips[f.name]]
proof('real_single_expansion_inference',**a,term=term,changed_processed_clips=changed,canonical_unchanged=True)
text=next(r['canonical'] for r in p.audio('S24')['segments'] if r['kind']=='spoken' and term in r['canonical']);entry=cache_entry(p,text);(entry/'processed.wav').write_bytes(b'controlled corrupt cache fixture');a=synthesize(p,'S24',emit);assert a['generated']==1;proof('real_corrupt_cache_recovery',**a)
policy=read(source.root/'pronunciation.json');write(root/'pronunciation.json',policy)
# Moving sentences exercises position-independent reuse of all original clip bytes.
from ceh_video.speech import sentences
parts=sentences(scene['audio_segments'][0]['text']);parts[0],parts[1]=parts[1],parts[0];scene['audio_segments'][0]['text']=' '.join(parts);scene['narration_en_US']=' '.join(s['text'] for s in scene['audio_segments'] if s['kind']=='spoken');a=synthesize(p,'S24',emit);assert a['generated']==0;proof('real_sentence_reordering_reuse',**a)
# Restore the exact source and original ordered reconstruction before exercising visual changes.
p=Project(root);a=synthesize(p,'S24',emit);assert a['generated']==0
voice={str(f.relative_to(root)):sha(f) for f in (root/'assets/voice').rglob('*.wav')}
env=p.environment()
for sid in ['S23','S24']:subprocess.run([str(source.root/'.venv/bin/python'),'-m','ceh_video.worker','build_film','--scene',sid],env=env,cwd=root,check=True)
art_before={sid:sha(root/'compositions'/f'{sid}.html') for sid in ['S23','S24']};speech_inputs=nodes(p)['speech:S24'].inputs
write(root/'data/visual-overrides.json',{'S24':{'offset_x':1}})
subprocess.run([str(source.root/'.venv/bin/python'),'-m','ceh_video.worker','build_film','--scene','S24'],env=env,cwd=root,check=True)
assert sha(root/'compositions/S23.html')==art_before['S23'];assert sha(root/'compositions/S24.html')!=art_before['S24']
assert voice=={str(f.relative_to(root)):sha(f) for f in (root/'assets/voice').rglob('*.wav')};assert nodes(p)['speech:S24'].inputs==speech_inputs
proof('real_art_only_compilation',unchanged_scene='S23',changed_scene='S24',all_speech_hashes_unchanged=True)
# Run the actual supported browser check on the modified standalone scene review project.
with (base/'qa/art-browser-check.json').open('w') as log:
 subprocess.run([str(source.root/'node_modules/.bin/hyperframes'),'check',str(root/'review/S24'),'--at','10,30,60','--json'],env=env,cwd=root,stdout=log,check=True)
r=read(base/'qa/art-browser-check.json');assert r['ok'] and not r['browserSkipped'];proof('real_art_browser_check',browser_executed=True)
result={'status':'live_fixture_scenarios_passed','runtime_validity':'valid_target_runtime','real_tts_inferences':2,'scenarios':checks,'scope':'Controlled fixture uses actual models and browser. Canonical release and production audio unchanged; no human pronunciation acceptance.'};write(source.qa/'live-integration.json',result);emit(result)
