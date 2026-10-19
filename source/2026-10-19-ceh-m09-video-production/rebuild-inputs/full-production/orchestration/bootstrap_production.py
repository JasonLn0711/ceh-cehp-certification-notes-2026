from pathlib import Path
import hashlib,json,shutil,zipfile
W=Path(__file__).parent;R=W/'project';OLD=Path('/home/jnlngx10/Videos/CEH_M08_v1_0/project')
A=W/'output/CEH_M09_English_Masterclass_HandDrawn_Editorial_v1_FULL.zip'
def sha(p):return hashlib.file_digest(p.open('rb'),'sha256').hexdigest()
I=W/'inputs';shutil.copy2(A,I/A.name)
with zipfile.ZipFile(A) as z:
 assert z.testzip() is None
 assert all(not n.startswith('/') and '..' not in Path(n).parts for n in z.namelist())
 z.extractall(I/'package')
S=I/'package/CEH_M09_English_Editorial_Masterclass';manifest=json.loads((S/'PACK_MANIFEST.json').read_text())
for n,h in manifest['sha256'].items():assert sha(S/n)==h,n
for n,h in json.loads((S/'LOCKED_SOURCE_SHA256.json').read_text())['sha256'].items():assert sha(S/n)==h,n
for folder in ['assets','case','lab_mock','reference','slides','boards','examples','production','licenses']:
 shutil.copytree(S/folder,R/folder)
for p in S.glob('*.md'):shutil.copy2(p,R/p.name)
(R/'data').mkdir()
for p in S.glob('*.json'):shutil.copy2(p,R/'data'/p.name)
for name in ['STYLE_TOKENS.json','network_map.json','LOCKED_SOURCE_SHA256.json']:shutil.copy2(S/name,R/name)
(R/'scripts').mkdir()
excluded={'scene_art.py','art_arp.py','art_dhcp.py','art_dns.py','m08_art_common.py'}
for p in (OLD/'scripts').iterdir():
 if p.is_file() and p.suffix in ['.py','.mjs'] and p.name not in excluded:
  s=p.read_text()
  for a,b in [('CEH_M08','CEH_M09'),('ceh-m08','ceh-m09'),('m08-1','m09-1'),('M08','M09'),('9,097','9,814'),('9097','9814'),('Sniffing','Social Engineering')]:s=s.replace(a,b)
  (R/'scripts'/p.name).write_text(s)
shutil.copytree(OLD/'models',R/'models',ignore=shutil.ignore_patterns('.cache','__pycache__'))
for p in (OLD/'licenses').rglob('*'):
 if p.is_file() and not p.name.startswith(('M08','M07','M06')):
  target=R/'licenses'/p.relative_to(OLD/'licenses');target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target)
for folder in ['voice','voice-baseline','audio']:(R/'assets'/folder).mkdir()
shutil.copy2(S/'production/quiz_silence_1s_48k_stereo.wav',R/'production/silence_1s_48k_stereo.wav')
(R/'data/production-overrides.json').write_text(json.dumps(dict(module='M09',quiz_silence_seconds=1,voice='af_heart',baseline_speed=.73,speech_atempo=1.5,video_rate=1.,canonical_words=manifest['spoken_words']),indent=2)+'\n')
(R/'data/voice-calibration.json').write_text(json.dumps(dict(voice='af_heart',lang='en-us',baseline_speed=.73,atempo=1.5,method='Approved M06 baseline reused for M09; no recalibration or WPM forcing.'),indent=2)+'\n')
p=R/'meta.json';d=json.loads(p.read_text());d.update(id='ceh-m09-social-engineering-v1',name='CEH M09 Social Engineering');p.write_text(json.dumps(d,indent=2)+'\n')
# Source extraction must not replace the independently approved production brief/design.
receipt=dict(status='source_verified_production_activated_not_rendered',source_zip_sha256=sha(A),
 source_payloads=len(manifest['sha256']),locked_assets=44,canonical_words=manifest['spoken_words'],scenes=58,chapters=11,
 model_sha256={str(p.relative_to(R)):sha(p) for p in (R/'models').rglob('*') if p.is_file()},
 source_stage_qa=json.loads((S/'validation/source_qa.json').read_text())['passed'],
 actual_master_rendered=False)
(W/'qa/source-activation.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['status','source_payloads','locked_assets','canonical_words']}))
