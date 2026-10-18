# M08 actual full-film validation

The [explicit full-production activation](../execution-activation.md) produced the complete **65:57.933** English film: 11 chapters, 58 native animated scenes, 9,097 canonical spoken words, 118,738 frames at 1920×1080/30 fps, 1,213 caption cues and 11 embedded chapter marks. [Canonical delivery and learning record](../../../notes/m08-sniffing/video-production-2026-10-18.md).

These are actual local production receipts, separate from the earlier source-only 811 / browser 94 checks. [Delivery validation](delivery-validation.json), [full-project browser check](master-project-check.json), [full decode/115 primary encoded samples](rendered-artifact-audit.json) and [17 targeted late samples](late-diagram-samples.json), [concrete final visual review](master-visual-review.md), [64 quiz assertions](quiz-runtime-checks.json), [174 native seek comparisons](scene-seek-audit.json) and [complete audio continuity](audio-continuity-audit.json) establish their named layers. The [source/packet revalidation](production-source-revalidation.json) rechecks 306 source payload hashes, 44 inherited locks, 43 actual offline packet assertions and all six verbose packet decodes.

Every quiz hold contains exactly 48,000 stereo zero PCM frames at 48 kHz. Decoded AAC maximum full-window peak is 2.659495294e-05; [measured windows](C11-encoded-quiz-silence.json) and the master audit disclose compression residue separately. [Audio review](audio-review.md) retains 172 timing flags across 143 clips and the unperformed human full-listening gate. Fixed-runtime ASR availability is verified; accuracy and latency are not_evaluated. The [auxiliary animation-map review](animation-map-review.md) preserves its separate helper version and heuristic flags.

The editable archive has **5,233 files**, **3,095,839,321 bytes** and **5,232 extracted payload hashes verified**. [Packaging receipt](packaging-receipt.json), [production implementation hashes](production-provenance.json) and [recovery tooling](../rebuild-inputs/full-production/README.md). Master SHA-256: 54e5a107cf94d7320eb91169f6a3267b81da408ef7bfacf3e745ef1f2df2faf3. Editable ZIP SHA-256: 0a6520b5c48ee712787db294563545fd6aa263d39ba6b66733e5863f33791bfc.

Full media, encoded/native samples, reference PCM, audition queue, models and editable assets remain in ~/Videos/CEH_M08_v1_0/. Media-dependent Markdown is preserved exactly as .local.md.txt; its links resolve in the local qa/output directory, not as GitHub downloads. [Exact render report](render_report.local.md.txt). Source-ready input receipts retain their historical scope. Human viewing/listening, learner practice and public media release keep separate acceptance.

## Actual chapter receipts

| Chapter | Browser | Render fingerprint | Native review |
| --- | --- | --- | --- |
| C01 | [check](C01-check.json) | [render](C01-render.json) | [review](C01-visual-review.md) |
| C02 | [check](C02-check.json) | [render](C02-render.json) | [review](C02-visual-review.local.md.txt) |
| C03 | [check](C03-check.json) | [render](C03-render.json) | [review](C03-visual-review.md) |
| C04 | [check](C04-check.json) | [render](C04-render.json) | [review](C04-visual-review.md) |
| C05 | [check](C05-check.json) | [render](C05-render.json) | [review](C05-visual-review.md) |
| C06 | [check](C06-check.json) | [render](C06-render.json) | [review](C06-visual-review.md) |
| C07 | [check](C07-check.json) | [render](C07-render.json) | [review](C07-visual-review.md) |
| C08 | [check](C08-check.json) | [render](C08-render.json) | [review](C08-visual-review.local.md.txt) |
| C09 | [check](C09-check.json) | [render](C09-render.json) | [review](C09-visual-review.md) |
| C10 | [check](C10-check.json) | [render](C10-render.json) | [review](C10-visual-review.md) |
| C11 | [check](C11-check.json) | [render](C11-render.json) | [review](C11-visual-review.md) |

## Documentation and delivery closeout

[Actual final hash recheck](delivery-integrity-recheck.json) verified all 5,775 delivery files and 120 exact source/archive copies. [Closeout validation](closeout-validation.json) records 40 Markdown files / 674 relative links with zero new failures, 19 inherited unavailable sibling/private links, clean diff checks and passing Planning validators (44 grandfathered policy warnings, zero new; 181 metadata/catalog entries). Publication receipts are recorded separately from these local checks.

The exact scene QA CSV retains its original CRLF line endings. Its local .gitattributes entry preserves those bytes and recognizes CR-at-EOL; trailing spaces remain checked.
