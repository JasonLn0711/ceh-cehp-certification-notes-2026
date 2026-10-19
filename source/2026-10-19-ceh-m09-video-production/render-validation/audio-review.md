# M09 audio evidence and listening gate

All 58 actual scene WAVs contain the complete 9,814 canonical words across 708 spoken clips. Actual clip fingerprints, baseline 0.73 and exactly one atempo=1.5 pass are checked. The eight marked holds each contain 48,000 stereo zero PCM frames at 48 kHz; total 8.000 seconds. Scene PCM counts align to 30fps. audio-clip-structure-audit.json records all measured scenes and exact local hold intervals.

All 58 fixed-runtime unprompted base.en CPU/int8 transcript receipts are persisted. Mode availability_validation; status LIVE_FULL_COMPLETED; runtime valid_target_runtime; functional result available_and_working. Accuracy and latency remain not_evaluated. This functional diagnostic does not establish pronunciation accuracy, naturalness or human listening acceptance.

Known-text attention/DTW alignment of the final processed clips retains 109 timing flags across 93 clips. These identify zero-duration words or low alignment probabilities; they are review leads rather than confirmed omissions or pronunciation errors. Canonical caption spelling is preserved. audio-review-diagnostics.json retains the actual flagged words and independent transcripts. audio-audition/index.html provides the real processed clips, original sentences and flags for later human review.

The measured speech-rate receipt reports raw clip duration and edge-trimmed sensitivity without changing samples or retuning the approved voice. Final decoded AAC continuity and quiz-window residue have separate master-stage receipts. Full end-to-end human watching/listening remains Jason's next acceptance layer when capacity permits; record timecoded corrections in the canonical M09 production note.
