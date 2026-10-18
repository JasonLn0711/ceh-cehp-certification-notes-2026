# Preserved production validation

These files are byte-for-byte copies from the local M05 v1.1 workspace's
`qa/` directory, captured on 2026-10-18, Asia/Taipei. The copying step adds no
new runtime result. [SHA256SUMS.txt](SHA256SUMS.txt) records their hashes and
the original ZIP/final master hashes checked during documentation closeout.

| Evidence | What it establishes |
| --- | --- |
| [Source validator](source-validation.txt) | 858 checks, zero failures for the immutable original package |
| [Delivery validation](delivery-validation.json) | 11 chapters, 58 scenes, 8,279 words, measured audio rate, runtime, frame count and caption-alignment review flags |
| [Retiming audit](retiming-audit.json) | Eight holds changed, 88 seconds removed, 721 unchanged spoken clips and identical non-hold PCM |
| [Revision invariants](revision-invariants.json) | 54 unchanged scene WAVs/SVGs, four clock-only SVG changes, unchanged PPTX and S58 metadata |
| [Revision origin](revision-origin.json) | Previous master identity and ten inherited chapter hashes |
| [Encoded artifact audit](rendered-artifact-audit.json) | Full master decode, 115 extracted frames and eight decoded silent holds |
| [Actual-timeline checks](quiz-runtime-checks.json) | 64 browser assertions, including pause boundaries and backward seeking |
| [Visual review](revision-visual-review.md) | Review findings for the 115 encoded samples and native-resolution checks |
| [Audio review](audio-review.md) | Speech/caption checks and retained S19/S40/S47 listening uncertainties |
| [Technical source review](technical-source-review.md) | Teaching-source checks, fictional-case boundaries and content-depth gaps |

The raw machine reports and authored reviews remain separate. Sampled visual
review, independent ASR and waveform checks support their declared layers;
end-to-end human viewing/listening acceptance is pending. Bare evidence
filenames in the unchanged copied reviews refer to the original production
workspace. Use the [production record](../../../notes/m05-vulnerability-analysis/video-production-2026-10-18.md)
for the current delivery locations and next actions.
