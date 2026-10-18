#!/usr/bin/env python3
"""Package verified editable sources and prove ZIP extraction against all payload hashes."""
from pathlib import Path
import shutil,json,hashlib,zipfile,tempfile,sys
R=Path(__file__).resolve().parents[1];O=R.parent/'output';Q=R.parent/'qa';B=O/'project_source'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def ignore(folder,names):return [n for n in names if n in {'.venv','node_modules','.hyperframes','.waveform-cache','__pycache__','review','.git'} or n.endswith('.tmp')]
def main():
 d=json.load(open(Q/'delivery-validation.json'));assert d['status']=='automated_delivery_checks_passed'
 print(json.dumps({'phase':'copying_verified_editable_project_and_evidence'}),flush=True)
 assert not B.exists(),'Existing delivery bundle must be reconciled before replacement'
 B.mkdir();shutil.copytree(R,B/'project',ignore=ignore);shutil.copytree(R.parent/'inputs',B/'inputs')
 evidence=O/'qa_evidence';evidence.mkdir(exist_ok=True)
 for f in Q.iterdir():
  if f.is_file() and (f.suffix in {'.json','.md'} or f.name in {'master-full-decode.log','master-assembly.log'}) and not f.name.endswith('-process.json'):shutil.copy2(f,evidence/f.name)
 for folder in [Q/'recognition',Q/'quiz-runtime',Q/'audio-audition',Q/'direct-inspection',*Q.glob('C[0-9][0-9]-snapshots'),*Q.glob('C[0-9][0-9]-direct')]:
  if folder.is_dir():shutil.copytree(folder,evidence/folder.name,ignore=lambda folder,names:[n for n in names if n.endswith('.html') and Path(folder).name!='audio-audition'])
 shutil.copytree(evidence,B/'qa');(B/'output').mkdir()
 (B/'README.md').write_text('''# CEH M08 Sniffing v1.0 editable production workspace

The complete film has 11 chapters, 58 animated scenes and all 9,097 canonical spoken words. Eight quiz holds each contain exactly 1.000 second of true zero PCM. Approved M04 v3 Tally/Northstar design and one narration-only 1.5× pass are preserved.

Open `project/` in Codex or HyperFrames, beginning with `project/EDITING.md`. The immutable original 308-file source ZIP and extracted package remain under `inputs/`. Final runtime evidence is under `qa/`, including the flagged audio audition queue. Rebuilt media belongs under `output/`.

The delivered master, 11 chapter MP4s, SRT/VTT, reference PCM, report and encoded samples are in the delivery directory above this workspace. They are not duplicated inside the editable ZIP. Models, fonts, licensed assets, clip baselines, processed speech, alignment and rebuild scripts are included. Python/Node environments, caches and credentials are excluded.

`EDITABLE_FILES_SHA256.txt` covers every payload except itself. The closed ZIP was extracted and every listed payload hash was checked. Full human viewing/listening and public media release remain separate acceptance layers.
''')
 payload=[f for f in sorted(B.rglob('*')) if f.is_file()];manifest={str(f.relative_to(B)):sha(f) for f in payload}
 (B/'EDITABLE_FILES_SHA256.txt').write_text(''.join(h+'  '+n+'\n' for n,h in manifest.items()))
 archive=O/'CEH_M08_Sniffing_v1_0_EDITABLE.zip';files=[f for f in sorted(B.rglob('*')) if f.is_file()]
 print(json.dumps({'phase':'creating_editable_zip','files':len(files)}),flush=True)
 with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=1,allowZip64=True) as z:
  for i,f in enumerate(files,1):
   z.write(f,'project_source/'+str(f.relative_to(B)))
   if i%250==0 or i==len(files):print(json.dumps({'phase':'editable_zip_entries','completed':i,'total':len(files)}),flush=True)
 with zipfile.ZipFile(archive) as z:
  assert len(z.infolist())==len(files) and z.testzip() is None
  with tempfile.TemporaryDirectory(prefix='editable-extraction-',dir=Q) as tmp:
   z.extractall(tmp);base=Path(tmp)/'project_source'
   for i,(name,h) in enumerate(manifest.items(),1):
    assert sha(base/name)==h,name
    if i%500==0 or i==len(manifest):print(json.dumps({'phase':'extracted_payload_hashes','completed':i,'total':len(manifest)}),flush=True)
   assert (base/'EDITABLE_FILES_SHA256.txt').read_bytes()==(B/'EDITABLE_FILES_SHA256.txt').read_bytes()
 receipt={'status':'editable_zip_crc_extraction_hashes_verified','zip':archive.name,'bytes':archive.stat().st_size,'entries':len(files),'payload_hashes':len(manifest),'sha256':sha(archive),'scope':'All editable payloads were extracted and hash checked; environments/caches excluded. Final media remain outside the archive.'}
 (Q/'packaging-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');shutil.copy2(Q/'packaging-receipt.json',evidence/'packaging-receipt.json')
 files=[f for f in sorted(O.rglob('*')) if f.is_file() and f.name!='DELIVERY_SHA256.txt'];rows=[]
 for i,f in enumerate(files,1):
  rows.append(sha(f)+'  '+str(f.relative_to(O)))
  if i%500==0 or i==len(files):print(json.dumps({'phase':'hashing_delivery','completed':i,'total':len(files)}),flush=True)
 (O/'DELIVERY_SHA256.txt').write_text('\n'.join(rows)+'\n');print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
