"""Preserve exact M10 production implementation separately from media acceptance receipts."""
from pathlib import Path
import json,hashlib,shutil
V=Path(__file__).resolve().parent;P=V/'project';Q=V/'qa';R=Path('/home/jnlngx10/phd-research/repos/ceh-cehp-certification-notes-2026');T=R/'source/2026-10-19-ceh-m10-video-production/rebuild-inputs/full-production'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def main():
 root=json.load(open(Q/'master-project-check.json'));seek=json.load(open(Q/'scene-seek-audit.json'));quiz=json.load(open(Q/'quiz-runtime/checks.json'));assert root['ok'] and not root['browserSkipped'] and seek['comparisons']==174 and quiz['checks']==64
 rows=[]
 def cp(f,t):
  t.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,t);assert sha(f)==sha(t);rows.append({'origin':str(f.relative_to(V)),'copy':str(t.relative_to(R)),'sha256':sha(f)})
 for f in sorted((P/'scripts').iterdir()):
  if f.suffix in {'.py','.mjs','.json'}:cp(f,T/'scripts'/f.name)
 for rel in ['package.json','package-lock.json','requirements-lock.txt','hyperframes.json','data/production-overrides.json','data/voice-calibration.json','data/synthesis-policy.json','licenses/M10-media-ledger.json']:cp(P/rel,T/rel)
 for name in ['BRIEF.md','DESIGN.md','EDITING.md','STORYBOARD.md']:cp(P/name,T/(Path(name).stem+'.local.md.txt'))
 for name in ['author_motion_plan.py','archive_source.py','archive_code.py','archive_render_evidence.py','write_final_records.py','qa_progress.py']:cp(V/name,T/'orchestration'/name)
 (T/'README.md').write_text('''# M10 production recovery inputs

Exact native-animation, narration, alignment, caption, chapter-render, master-assembly, validation and packaging scripts, together with pinned configuration and media provenance. Use them in the complete local project under ~/Videos/CEH_M10_v1_0/project/. This compact Git subset keeps large models, source assets, WAVs and videos in their owning Videos workspace.

The [source interfaces](../../content/AGENT_PROMPT.md.txt) and [canonical production record](../../../../notes/m10-denial-of-service/video-production-2026-10-19.md) explain the approved scope. Local-reference Markdown is preserved verbatim as .local.md.txt; its paths resolve in the complete project. The source ZIP and extracted inputs remain immutable. Checked implementation, actual rendered media and full human acceptance have separate evidence.
''')
 (T/'recovery-copy-integrity.json').write_text(json.dumps({'scope':'Exact implementation/configuration copies; runtime checks exist locally and media acceptance is separately recorded.','files':rows},indent=2)+'\n')
 print(json.dumps({'recovery_files':len(rows),'all_hashes_match':True}))
if __name__=='__main__':main()
