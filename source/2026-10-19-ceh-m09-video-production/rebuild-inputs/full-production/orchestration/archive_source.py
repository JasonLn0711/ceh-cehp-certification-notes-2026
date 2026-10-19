"""Preserve exact M09 authored sources and compact source-stage receipts in the owning repo."""
from pathlib import Path
import json,shutil,hashlib
V=Path(__file__).resolve().parent;S=V/'inputs/package/CEH_M09_English_Editorial_Masterclass';Q=V/'qa';O=V/'output'
R=Path('/home/jnlngx10/phd-research/repos/ceh-cehp-certification-notes-2026');D=R/'source/2026-10-19-ceh-m09-video-production';copies=[]
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def cp(f,target):
 target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,target);assert sha(f)==sha(target)
 copies.append({'origin':str(f.relative_to(V)),'copy':str(target.relative_to(R)),'sha256':sha(f)})
for name in ['AGENT_PROMPT.md','CONCEPT_CONNECTIONS.md','COVERAGE_MATRIX.md','SCRIPT_en-US.md','SOURCES.md','ASSESSMENT_INSTRUCTOR.md','ASSESSMENT_STUDENT.md','VOICE_AND_AUDIO.md','chapters.json','coverage.json','m09_workflow_extensions.json','questions.json','scenes.json','visual_scenes.json','LOCKED_SOURCE_SHA256.json']:
 cp(S/name,D/'content'/name)
for f in sorted((S/'tooling').iterdir()):
 if f.is_file():cp(f,D/'rebuild-inputs'/('README.package.md.txt' if f.name=='README.md' else f.name))
for f in sorted((S/'case').iterdir()):
 if f.is_file():cp(f,D/'case'/f.name)
for f in sorted((S/'lab_mock').iterdir()):
 if f.is_file():cp(f,D/'lab_mock'/f.name)
for f in sorted((S/'validation').iterdir()):
 if f.is_file():cp(f,D/'validation'/f.name)
cp(O/'release_receipt.json',D/'validation/release_receipt.json')
for name in ['source-qa-initial.json','skills-refresh-receipt.json']:
 if (Q/name).is_file():cp(Q/name,D/'validation'/name)
(D/'.gitattributes').write_text('lab_mock/*.csv -text whitespace=cr-at-eol\nlab_mock/*.eml -text whitespace=cr-at-eol\n')
(D/'validation/copy-integrity.json').write_text(json.dumps({'scope':'Exact source-stage and authored recovery copies; source release remains immutable under local Videos inputs.','files':copies},indent=2)+'\n')
(D/'validation/README.md').write_text('''# M09 source-stage validation

Exact copies of actual source/package QA and the closed-ZIP receipt. [Copy integrity](copy-integrity.json) binds each preserved file to its local origin. These receipts establish source readiness separately from actual film execution.

- [Source checks](source_qa.json): 565 passed / 0 failed. The preserved initial receipt records the earlier repaired validator assumptions.
- [Browser checks](browser_qa.json): 94 passed / 0 failed, including 58 source boards, four executable examples and 12 deterministic direct/reverse comparisons.
- [Inert evidence parser](evidence_qa.json): 36 passed / 0 failed. Actual email/JSON/CSV parsing and constructed arithmetic; no delivery, authentication, calls, QR decoding or live interaction.
- [Release receipt](release_receipt.json): 305 ZIP entries / 303 extracted payload hashes, CRC and extraction checks pass.
- [Visual review](visual-review.md): all 58 source captures, 18 actual exported pages, dense quiz and four final example states inspected.
- Four hyperframes-*.json receipts pass actual runtime/layout/contrast. Each standalone example retains one nonblocking nested_structure_needs_subcomposition advisory.
- [Live primary reference retrieval](reference_retrieval.json) preserves 13 HTTP/body-hash receipts. Claim-specific sources are in [SOURCES.md](../content/SOURCES.md).

All 44 inherited asset locks match. The editable presentation contains 223 native shapes and 159 text runs across 18 pages; its PDF was actually exported. Source checks do not establish complete speech, final captions, all native motion, an encoded film or human acceptance. The [canonical M09 record](../../../notes/m09-social-engineering/video-production-2026-10-19.md) owns the current production layer.
''')
(D/'rebuild-inputs/README.md').write_text('''# M09 source-package recovery tooling

These exact authored generators, content seeds and validators produced the [source interfaces](../content/AGENT_PROMPT.md), [inert evidence](../lab_mock/README.md) and [actual source receipts](../validation/README.md). Run them in the complete local source folder; the Git recovery subset does not duplicate shared Tally, fonts, all SVG/PPTX/PDF assets or model weights. Complete assets remain in the source ZIP under ~/Videos/CEH_M09_v1_0/output/.

Preserve the source ZIP and extracted inputs. Subsequent motion, narration and rendered-media changes belong in the separate production project and its full-production recovery record. Source readiness, render acceptance and learner/human acceptance retain distinct evidence.
''')
print(json.dumps({'copied_source_files':len(copies),'source_bytes_preserved':sum((R/x['copy']).stat().st_size for x in copies)}))
