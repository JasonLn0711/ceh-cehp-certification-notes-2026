#!/usr/bin/env python3
"""Seal and independently extract/check the source ZIP; no circular archive hash."""
from pathlib import Path
import json,hashlib,zipfile,tempfile,sys,time
R=Path(__file__).resolve().parents[1];start=time.monotonic();OUT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else R.parent.parent/'output';OUT.mkdir(parents=True,exist_ok=True)
qa=json.loads((R/'validation/source_qa.json').read_text());assert qa['failed']==0,'Source validation must pass first'
def included(p):return p.is_file() and not any(x in p.relative_to(R).parts for x in ['.hyperframes','__pycache__','node_modules','.git']) and p.name not in ['FILES_SHA256.txt','PACK_MANIFEST.json']
files=sorted(p for p in R.rglob('*') if included(p));manifest={p.relative_to(R).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(R/'FILES_SHA256.txt').write_text(''.join(f'{sha}  {name}\n' for name,sha in manifest.items()))
meta=dict(package='CEH M09 English Editorial Masterclass',version='1.0',status='source_ready',actual_final_mp4_rendered=False,chapters=11,scenes=58,questions=8,spoken_words=qa['spoken_words'],payload_hashes=len(manifest),archive_file_count=len(manifest)+2,manifest_exclusions=['FILES_SHA256.txt','PACK_MANIFEST.json'],excluded_directories=['.hyperframes','__pycache__','node_modules','.git'],sha256=manifest)
(R/'PACK_MANIFEST.json').write_text(json.dumps(meta,indent=2)+'\n');archive=OUT/'CEH_M09_English_Masterclass_HandDrawn_Editorial_v1_FULL.zip'
print(f'Packaging {len(manifest)+2} files; then CRC, extraction and SHA-256 checks...',file=sys.stderr)
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in files+[R/'FILES_SHA256.txt',R/'PACK_MANIFEST.json']:z.write(p,R.name+'/'+p.relative_to(R).as_posix())
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None;assert len(z.namelist())==meta['archive_file_count']
 with tempfile.TemporaryDirectory(prefix='m09-extract-',dir=OUT) as d:
  z.extractall(d);extracted=Path(d)/R.name
  for name,sha in manifest.items():assert hashlib.sha256((extracted/name).read_bytes()).hexdigest()==sha,name
  assert (extracted/'FILES_SHA256.txt').read_bytes()==(R/'FILES_SHA256.txt').read_bytes();assert (extracted/'PACK_MANIFEST.json').read_bytes()==(R/'PACK_MANIFEST.json').read_bytes()
receipt=dict(status='source_ready',archive=str(archive),archive_bytes=archive.stat().st_size,archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),archive_file_count=meta['archive_file_count'],payload_hashes_verified=len(manifest),crc_failures=0,extraction_hash_failures=0,source_qa_passed=qa['passed'],source_qa_failed=qa['failed'],actual_final_mp4_rendered=False,elapsed_seconds=round(time.monotonic()-start,3))
(OUT/'release_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
