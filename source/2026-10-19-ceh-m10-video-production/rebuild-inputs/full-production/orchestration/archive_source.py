from pathlib import Path
import json,shutil,hashlib
V=Path(__file__).resolve().parent;S=V/'inputs/package/CEH_M10_English_Editorial_Masterclass';Q=V/'qa';R=Path('/home/jnlngx10/phd-research/repos/ceh-cehp-certification-notes-2026');D=R/'source/2026-10-19-ceh-m10-video-production';copies=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def cp(p,t):
 t.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,t);assert sha(p)==sha(t);copies.append({'origin':str(p.relative_to(V)),'copy':str(t.relative_to(R)),'sha256':sha(p)})
for p in sorted(S.iterdir()):
 if p.suffix in ['.md','.json'] and p.name not in ['PACK_MANIFEST.json','package.json']:cp(p,D/'content'/(p.name+'.txt' if p.suffix=='.md' else p.name))
for folder in ['tooling','case','lab_mock','validation']:
 for p in sorted((S/folder).iterdir()):
  if p.is_file():cp(p,D/('rebuild-inputs' if folder=='tooling' else folder)/p.name)
cp(V/'output/release_receipt.json',D/'validation/release_receipt.json')
for name in ['skills-refresh-receipt.json','content-review.json']:cp(Q/name,D/'validation'/name)
(D/'.gitattributes').write_text('lab_mock/*.csv -text whitespace=cr-at-eol\nlab_mock/*.pcap binary\n')
(D/'validation/copy-integrity.json').write_text(json.dumps({'scope':'Exact source-stage recovery copies; full assets remain in the immutable local source archive.','files':copies},indent=2)+'\n')
(D/'validation/README.md').write_text('''# M10 source validation

[Source checks](source_qa.json): 627 passed, zero failed. [Browser checks](browser_qa.json): 94 passed, zero failed. [Offline evidence parser](evidence-verification.json): 44 passed, zero failed, including actual PCAP byte parsing and CSV arithmetic. [Release receipt](release_receipt.json): 332 entries and 330 payload hashes verified after extraction; CRC passed. All 44 inherited locks match.

The 18-page editable deck contains 217 native shapes and 151 text runs; its PDF was actually exported. [Visual review](visual-review.md) records inspected source boards, slide pages and four running animation examples. [Twelve primary references](../content/SOURCES.md.txt) have actual retrieval/body-hash receipts. [Copy integrity](copy-integrity.json) binds this recovery subset to immutable local files.

Source readiness establishes this package layer. Full-film runtime, encoded output and human viewing/listening retain separate evidence in the [canonical production record](../../../notes/m10-denial-of-service/video-production-2026-10-19.md).
''')
(D/'rebuild-inputs/README.md').write_text('''# M10 source recovery

Exact generators, content seeds and validators for the [source interfaces](../content/AGENT_PROMPT.md.txt), [offline fixtures](../lab_mock/README.md) and [source QA](../validation/README.md). Execute in the complete source folder under ~/Videos/CEH_M10_v1_0/source/CEH_M10_English_Editorial_Masterclass/. The Git subset preserves authored recovery inputs; the immutable source ZIP owns all shared art, fonts, SVG, PPTX, PDF and examples. Production narration and native motion retain their separate project and runtime receipts.
''')
print(json.dumps({'copied':len(copies),'bytes':sum((R/x['copy']).stat().st_size for x in copies)}))
