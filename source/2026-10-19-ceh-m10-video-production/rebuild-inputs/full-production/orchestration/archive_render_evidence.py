"""Archive compact actual M10 film evidence and exact recovery inputs in the CEH owner repo."""
from pathlib import Path
import json,hashlib,shutil,re
V=Path(__file__).resolve().parent;P=V/'project';Q=V/'qa';O=V/'output'
R=Path('/home/jnlngx10/phd-research/repos/ceh-cehp-certification-notes-2026');S=R/'source/2026-10-19-ceh-m10-video-production';D=S/'render-validation';T=S/'rebuild-inputs/full-production'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def main():
 d=json.load(open(Q/'delivery-validation.json'));z=json.load(open(Q/'packaging-receipt.json'));assert d['status']=='automated_delivery_checks_passed' and z['status']=='editable_zip_crc_extraction_hashes_verified'
 D.mkdir(exist_ok=True);T.mkdir(parents=True,exist_ok=True);copies=[];aliases={}
 def cp(f,target):
  target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,target);assert sha(f)==sha(target);copies.append({'origin':str(f.relative_to(V)),'copy':str(target.relative_to(R)),'sha256':sha(f)})
 names=['source-activation.json','production-source-revalidation.json','production-evidence-recheck.json','audio-structure-audit.json','audio-clip-structure-audit.json','audio-review.md','delivery-validation.json','master-ffprobe.json','master-project-check.json','master-visual-review.md','rendered-artifact-audit.json','late-diagram-samples.json','C11-encoded-quiz-silence.json','packaging-receipt.json','production-provenance.json','scene-seek-audit.json','audio-continuity-audit.json','asr-availability-receipt.json','speech-rate-measurement.json','technical-source-review.md','animation-helper-receipt.json','animation-map-context.json','animation-map-review.md']
 for i in range(1,12):names.extend([f'C{i:02}-check.json',f'C{i:02}-render.json',f'C{i:02}-visual-review.md'])
 for name in names:
  f=Q/name;assert f.is_file(),f;target=name
  if f.suffix=='.md' and any(not re.match(r'(https?://|#)',u) for u in re.findall(r'\]\(([^)]+)\)',f.read_text())):target=f.stem+'.local.md.txt'
  cp(f,D/target);aliases[name]=target
 for f,name in [(Q/'quiz-runtime/checks.json','quiz-runtime-checks.json'),(O/'render_report.md','render_report.local.md.txt'),(O/'scene_qa_ledger.csv','scene_qa_ledger.csv'),(P/'data/master-timing.json','master-timing.json')]:cp(f,D/name)
 for f in sorted((P/'scripts').iterdir()):
  if f.suffix in {'.py','.mjs','.json'}:cp(f,T/'scripts'/f.name)
 for rel in ['package.json','package-lock.json','requirements-lock.txt','hyperframes.json','data/production-overrides.json','data/voice-calibration.json','data/synthesis-policy.json','licenses/M10-media-ledger.json']:cp(P/rel,T/rel)
 for name in ['BRIEF.md','DESIGN.md','EDITING.md','STORYBOARD.md']:cp(P/name,T/(Path(name).stem+'.local.md.txt'))
 for name in ['author_motion_plan.py','archive_source.py','archive_code.py','archive_render_evidence.py','write_final_records.py','qa_progress.py']:cp(V/name,T/'orchestration'/name)
 (T/'README.md').write_text('''# M10 full-production recovery inputs

Exact copies of actual production scripts, package/configuration locks, media provenance and local design/editing records. They supplement the [canonical source interfaces](../../content/AGENT_PROMPT.md.txt) and [actual film evidence](../../render-validation/README.md). The complete asset/model/audio workspace is in the local editable ZIP; this compact Git subset is not a standalone renderable project.

Run chapter/assembly/audit commands from the complete extracted project and follow EDITING.md. Preserve valid clip caches and unchanged chapter fingerprints. Local-reference Markdown is retained verbatim as .local.md.txt because its media links resolve inside that full workspace. Raw source bytes, models, voice WAVs and final videos remain in Videos. Orchestration scripts retain the original GX10 paths as provenance; review paths before recovery on another machine.
''')
 ms=round(d['duration']*1000);mm,rem=divmod(ms,60000);ss,milli=divmod(rem,1000);duration=f'{mm}:{ss:02}.{milli:03}';peak=max(v['full_window_peak'] for v in json.load(open(Q/'rendered-artifact-audit.json'))['quiz_silence'])
 (D/'README.md').write_text(f'''# M10 actual full-film validation

The [approved full-film scope](../source.md) produced the complete **{duration}** film: 11 chapters, 58 native animated scenes, 10,241 canonical spoken words, {d['frames']:,} frames at 1920×1080/30fps and 11 embedded chapter marks. [Canonical delivery and learning record](../../../notes/m10-denial-of-service/video-production-2026-10-19.md).

[Delivery validation](delivery-validation.json), [actual root browser check](master-project-check.json), [full decode and 115 primary encoded samples](rendered-artifact-audit.json), [50 complete late diagrams](late-diagram-samples.json) and [concrete visual review](master-visual-review.md) establish their named layers. [64 quiz assertions](quiz-runtime-checks.json), [174 native seek comparisons](scene-seek-audit.json) and [full PCM/AAC continuity](audio-continuity-audit.json) preserve timing and signal evidence separately. The [source revalidation](production-source-revalidation.json) rechecks 330 payload hashes, 44 inherited locks and 44 actual offline evidence assertions.

Each quiz hold contains 48,000 stereo zero PCM frames at 48 kHz, exactly 1.000 second. The final AAC maximum full-window peak is {peak:.10g}; [decoded chapter windows](C11-encoded-quiz-silence.json) and the master audit disclose lossy residue separately. [Audio review](audio-review.md) retains timing uncertainty and the human listening gate. Fixed-runtime ASR establishes availability; accuracy and latency are not_evaluated. [Animation-map review](animation-map-review.md) records the matching isolated 0.8.173 helper and its contextual heuristic findings.

The editable ZIP has **{z['entries']:,} files / {z['bytes']:,} bytes**, with CRC, extraction and all **{z['payload_hashes']:,} payload hashes** verified. [Packaging receipt](packaging-receipt.json), [actual implementation identity](production-provenance.json), [exact-copy manifest](copy-integrity.json) and [recovery tooling](../rebuild-inputs/full-production/README.md). Master SHA-256: {d['master_sha256']}. Editable ZIP SHA-256: {z['sha256']}.

Large media, native/encoded samples, reference PCM, audition queue and models remain under ~/Videos/CEH_M10_v1_0/. [Exact local report](render_report.local.md.txt) retains media-dependent links for that workspace. Source-ready receipts remain historical source evidence. Full human viewing/listening, learner results and public media release keep separate acceptance.
''')
 (D/'copy-integrity.json').write_text(json.dumps({'scope':'Exact actual execution evidence and recovery copies; large assets/media remain in the local owning workspace.','aliases':aliases,'files':copies},indent=2)+'\n')
 print(json.dumps({'render_evidence_and_recovery_copies':len(copies),'master_sha256':d['master_sha256'],'status':'archived_exactly'}))
if __name__=='__main__':main()
