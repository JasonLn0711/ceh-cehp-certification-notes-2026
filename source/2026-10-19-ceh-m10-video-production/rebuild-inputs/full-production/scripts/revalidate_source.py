"""Revalidate immutable M10 source bytes and actually parse the inert case artifacts."""
from pathlib import Path
import json, subprocess, hashlib, zipfile, sys, os
R=Path(__file__).resolve().parents[1];Q=R.parent/'qa';S=R.parent/'inputs/package/CEH_M10_English_Editorial_Masterclass'
IDENTITY=json.loads((R.parent/'inputs/source-identity.json').read_text())
EXPECTED=IDENTITY['archive_sha256']
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def main():
 archive=R.parent/'inputs/CEH_M10_English_Masterclass_HandDrawn_Editorial_v1_FULL.zip'
 assert sha(archive)==EXPECTED
 with zipfile.ZipFile(archive) as z:
  entries=len(z.infolist());assert entries==IDENTITY['archive_file_count'] and z.testzip() is None
 rows=[]
 for line in (S/'FILES_SHA256.txt').read_text().splitlines():
  if not line.strip() or line.startswith('#'):continue
  h,n=line.split(None,1);n=n.lstrip('* ');assert sha(S/n)==h,n;rows.append(n)
 locks=json.load(open(S/'LOCKED_SOURCE_SHA256.json'))['sha256']
 for rel,h in locks.items():
  f=R/rel
  if not f.exists():f=R/'data'/rel
  assert sha(f)==h,rel
 print(json.dumps({'phase':'immutable_source_verified','payload_hashes':len(rows),'locked_assets':len(locks)}),flush=True)
 p=subprocess.run([sys.executable,str(S/'tooling/verify_evidence.py')],capture_output=True,text=True,check=True,env={**os.environ,'CEH_EVIDENCE_READONLY':'1'})
 result=json.loads(p.stdout);assert result['failed']==0
 (Q/'production-evidence-recheck.json').write_text(json.dumps(result,indent=2)+'\n')
 receipt={'status':'passed','source_zip_sha256':sha(archive),'source_entries':entries,'payload_hashes':len(rows),'locked_assets':len(locks),'offline_evidence_assertions':result['passed'],'scope':result['inference_boundary']}
 (Q/'production-source-revalidation.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
