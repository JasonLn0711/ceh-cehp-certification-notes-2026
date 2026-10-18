# M07 actual full-film validation

The [later full-production activation](../full-production-activation.md) produced the complete **64:39.467** English film: 11 chapters, 58 animated scenes, 9,174 canonical spoken words, 116,384 frames at 1920×1080/30 fps. [Canonical delivery and learning record](../../../notes/m07-malware-threats/video-production-2026-10-18.md).

These are exact copies of the actual local production receipts, separate from the earlier source-only 808 / browser 94 checks. [Delivery validation](delivery-validation.json), [full-project check](master-project-check.json), [full decode/115 encoded samples](rendered-artifact-audit.json), [concrete visual review](master-visual-review.md), [64 quiz assertions](quiz-runtime-checks.json), [174 native seek comparisons](scene-seek-audit.json) and [full audio continuity](audio-continuity-audit.json) establish their named layers. All 294 original source payload hashes and 44 locked inherited assets remain verified.

Every quiz hold contains exactly 48,000 stereo zero PCM frames at 48 kHz. Decoded AAC has a maximum full-window peak of 2.65262788e-05 and 49,152 nonzero channel samples across all eight windows; its measured compression residue is reported separately. [Audio review](audio-review.md) retains 103 timing flags across 93 clips and the human listening gate. Fixed-runtime ASR availability is verified; accuracy and latency are `not_evaluated`.

The editable archive has **5,365 files**, **3,037,443,862 bytes** and **5,364 extracted payload hashes checked**. [Packaging receipt](packaging-receipt.json) and [production implementation hashes](production-provenance.json). Master SHA-256: `fefe704fc2fa33be38242c9d12baa9b3427d8388c64c83582a4492c58ddc3d47`. Editable ZIP SHA-256: `0b6a44c27f86882566274e7ea6dc7dd449361b23e11d9c6443834fb0d1727772`.

Full media, reference WAV, local audition queue, chapter files, source assets, model files and environments remain in `~/Videos/CEH_M07_v1_0/`; environments/caches are excluded from the editable ZIP. The exact [local render report](render_report.local.md.txt) is an evidence copy whose media links resolve from the local output directory. Its relative media links are not GitHub downloads. [Copied-file hashes](COPIED_FILES_SHA256.txt) bind all copied receipts.

Human viewing/listening, learner progress and public video release retain separate evidence. Git publication concerns documentation and compact QA.
