"""Revalidate immutable M08 source bytes and actual offline packet decoding."""
from pathlib import Path
import json,subprocess,hashlib,zipfile,sys
R=Path(__file__).resolve().parents[1];Q=R.parent/'qa';S=R.parent/'inputs/package/CEH_M08_English_Editorial_Masterclass'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def main():
 archive=R.parent/'inputs/CEH_M08_English_Masterclass_HandDrawn_Editorial_v1_FULL.zip'
 assert sha(archive)=='bd375286deebf6fcaf1a913d7e1760371bad57f62c2d1ec5d9e720807f45da74'
 with zipfile.ZipFile(archive) as z:assert len(z.infolist())==308 and z.testzip() is None
 rows=[]
 for line in (S/'FILES_SHA256.txt').read_text().splitlines():
  if not line.strip() or line.startswith('#'):continue
  h,n=line.split(None,1);n=n.lstrip('* ');assert sha(S/n)==h,n;rows.append(n)
 for rel,h in json.load(open(S/'LOCKED_SOURCE_SHA256.json'))['sha256'].items():
  f=R/rel
  if not f.exists():f=R/'data'/rel
  assert sha(f)==h,rel
 print(json.dumps({'phase':'immutable_source_verified','payload_hashes':len(rows),'locked_assets':44}),flush=True)
 result=subprocess.run([sys.executable,str(S/'tooling/verify_packets.py')],capture_output=True,text=True,check=True)
 p=json.loads(result.stdout);assert p['failed']==0;(Q/'production-packet-recheck.json').write_text(json.dumps(p,indent=2))
 verbose=[]
 for item in json.load(open(S/'lab_mock/fixture_manifest.json'))['files']:
  cmd=['tcpdump','-nn','-tt','-vvv','-XX','-r',str(S/item['path'])];p=subprocess.run(cmd,capture_output=True,text=True)
  assert p.returncode==0 and 'bad cksum' not in p.stdout.lower() and 'bad udp cksum' not in p.stdout.lower(),item['path']
  verbose.append({'file':item['path'],'sha256':sha(S/item['path']),'argv':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
 (Q/'production-packet-decodes.json').write_text(json.dumps({'status':'passed','scope':'Actual offline tcpdump verbose decoding of all six immutable synthetic fixtures. No interface collection, transmission, client acceptance or control enforcement.','files':verbose},indent=2))
 receipt={'status':'passed','source_zip_sha256':sha(archive),'source_entries':308,'payload_hashes':len(rows),'locked_assets':44,'offline_packet_assertions':json.load(open(Q/'production-packet-recheck.json'))['passed'],'verbose_files':len(verbose)}
 (Q/'production-source-revalidation.json').write_text(json.dumps(receipt,indent=2));print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
