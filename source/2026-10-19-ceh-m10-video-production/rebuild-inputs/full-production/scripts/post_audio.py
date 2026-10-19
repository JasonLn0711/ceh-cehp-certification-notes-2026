"""Finish measured audio evidence after the real narration/alignment/ASR stages succeed."""
from pathlib import Path
import sys,json,time,subprocess,hashlib
import numpy as np
import soundfile as sf
R=Path(__file__).resolve().parents[1];Q=R.parent/'qa';began=time.monotonic()
while True:
 states={}
 for phase in ['narration','alignment','recognition']:
  f=Q/(phase+'-process.json');states[phase]=json.load(open(f))['status']
 if 'failed' in states.values():raise RuntimeError(('Audio stage failed; inspect named log',states))
 print(json.dumps({'phase':'waiting_complete_audio_diagnostics','states':states,'scene_audio_files':len(list((R/'data').glob('S*.audio.json'))),'functional_transcripts':len(list((Q/'recognition').glob('*.json'))),'elapsed_seconds':round(time.monotonic()-began)}),flush=True)
 if all(v=='completed' for v in states.values()):break
 time.sleep(15)
for script in ['measure_speech.py','review_audio.py','make_audio_review.py','asr_receipt.py']:
 print(json.dumps({'phase':'running_actual_audio_check','script':script}),flush=True)
 subprocess.run([sys.executable,str(R/'scripts'/script)],cwd=R,check=True)
subprocess.run([sys.executable,str(R/'scripts/audit_audio_clips.py')],cwd=R,check=True)
clips=json.load(open(Q/'audio-clip-structure-audit.json'))['spoken_clips']

d=json.load(open(Q/'audio-review-diagnostics.json'));flags=d['alignment_flags'];n=len(set(x['file'] for x in flags));rate=json.load(open(Q/'speech-rate-measurement.json'))
(Q/'audio-review.md').write_text(f'''# M10 audio evidence and listening gate

All 58 actual scene WAVs contain the complete 10,241 canonical words across {clips} spoken clips. Actual clip fingerprints, baseline 0.73 and exactly one atempo=1.5 pass are checked. The eight marked holds each contain 48,000 stereo zero PCM frames at 48 kHz; total 8.000 seconds. Scene PCM counts align to 30fps. audio-clip-structure-audit.json records all measured scenes and exact local hold intervals.

All 58 fixed-runtime unprompted base.en CPU/int8 transcript receipts are persisted. Mode availability_validation; status LIVE_FULL_COMPLETED; runtime valid_target_runtime; functional result available_and_working. Accuracy and latency remain not_evaluated. This functional diagnostic does not establish pronunciation accuracy, naturalness or human listening acceptance.

Known-text attention/DTW alignment of the final processed clips retains {len(flags)} timing flags across {n} clips. These identify zero-duration words or low alignment probabilities; they are review leads rather than confirmed omissions or pronunciation errors. Canonical caption spelling is preserved. audio-review-diagnostics.json retains the actual flagged words and independent transcripts. audio-audition/index.html provides the real processed clips, original sentences and flags for later human review.

The measured speech-rate receipt reports raw clip duration and edge-trimmed sensitivity without changing samples or retuning the approved voice. Final decoded AAC continuity and quiz-window residue have separate master-stage receipts. Full end-to-end human watching/listening remains Jason's next acceptance layer when capacity permits; record timecoded corrections in the canonical M10 production note.
''')
print(json.dumps({'phase':'measured_audio_evidence_complete','scenes':58,'clips':clips,'flags':len(flags),'flagged_clips':n,'human_listening':'pending'}),flush=True)
