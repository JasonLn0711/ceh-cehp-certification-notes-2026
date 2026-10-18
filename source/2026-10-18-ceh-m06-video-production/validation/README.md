# Preserved M06 production evidence

These files are unchanged copies from the final local M06 production QA, captured on 2026-10-18, Asia/Taipei. Copying a report does not rerun its checks. [SHA256SUMS.txt](SHA256SUMS.txt) records copied-file hashes and local-only master/editable-ZIP identities.

| Evidence | Established layer |
| --- | --- |
| [Source integrity](source-integrity.json), [validator](source-validation.txt) | 273-file original ZIP, 271 manifest matches, 44 inherited locked assets and 1,065 source checks |
| [Delivery validation](delivery-validation.json) | Complete rendered film, 58 scenes, 11 chapters, 8,969 words, frames, format and hash-matched audio/caption inputs |
| [Encoded artifact audit](rendered-artifact-audit.json) | Complete decode, zero detected black intervals, 115 extracted samples and full decoded AAC quiz windows |
| [Actual quiz timeline](quiz-runtime-checks.json) | 64 assertions for clock, answer timing, no early highlight and backward seeking |
| [Visual review](master-visual-review.md) | Concrete inspection of all 115 encoded samples, with native dense-frame checks |
| [Audio review](audio-review.md), [rate measurement](speech-rate-measurement.json) | Canonical coverage, independent ASR, retained listening priorities, raw-clip and signal-threshold WPM estimates |
| [Enunciation correction](speech-enunciation-correction.json), [final prompt check](speech-final-prompt-recheck.json) | One regenerated S56 sentence, unchanged canonical words/speed, final correctly recognized question |
| [Chronology corrections](source-corrections.json), [technical review](technical-source-review.md) | Two minimal working-script chronology corrections; original source remains immutable |
| [Full-master PCM check](master-pcm-silence.json), [delivery manifest verification](delivery-manifest-verification.json) | Eight exact zero holds in the delivered reference mix; all 5,769 delivery entries rehashed successfully |
| [Packaging receipt](packaging-receipt.json), [preservation recheck](preservation-recheck.json) | Editable ZIP CRC/hash and unchanged original M06 ZIP / previous M05 master identities |

Full human end-to-end viewing/listening acceptance, learner results and public media release remain separate. Bare filenames in unchanged copied reviews refer to the original local QA directory. The [production record](../../../notes/m06-system-hacking/video-production-2026-10-18.md) holds current locations and next gates.
