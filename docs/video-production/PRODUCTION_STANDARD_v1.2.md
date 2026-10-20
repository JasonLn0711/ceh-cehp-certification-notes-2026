# CEH English production standard v1.2

Adopted 2026-10-20. Engine 0.5.0 selects `ceh-en-v1.2`; design profile remains the compatible M10 editorial renderer with `visual_variant: semantic-v1.2` and tokens 1.3.0. Historical v1.0/v1.1 releases retain their original contracts. This standard is implemented and the complete new movie has passed rendering and encoded/audio checks. Actual editable-archive extraction and reconstruction also passed; full human listening remains separate.

## Timing and protected identity

Preserve af_heart/en-US, synthesis baseline 0.73, exactly one atempo=1.4 on baseline spoken PCM, approved fonts, Tally, Northstar, canonical copy, 58 scenes, 11 chapters and eight quizzes. Video/animation remain 1x; music off; 1920×1080 at30fps; stereo48kHz PCM reference retained.

| Named interval | Audio frames | Meaning |
|---|---:|---|
| Scene opening | 14400 |0.300s|
| In-scene sentence gap |14400|0.300s; replaces v1.1's9600|
| Scene ending |24000|0.500s|
| Chapter boundary |38400|existing ending+next opening, never another inserted pause|
| Quiz hold |48000|exactly1.000s, eight holds total384000|

Pause precedence: quiz, scene/chapter boundary, ordinary sentence gap. Frame alignment is independently recorded, never hidden in a named interval. Ten chapter-boundary records disclose named and actual intervals including padding. AAC boundary residue is measured separately from zero PCM. Captions and answers remain absent throughout each quiz hold.

Clip synthesis, clip processing and scene assembly have separate identities. Timing changes rebuild assembly and absolute cues while preserving verified spoken PCM and clip-relative alignment. All captions, motion anchors, chapter markers and answer reveals are recalculated and checked.

## Efficient production contract

Iteration performs affected compilation and checks without automatically packing a release. Release requires the complete current-source QA inventory, native chapter checks/reviews, actual encoded-artifact checks and verified extraction. A smoke fixture never clears a full-film gate. Golden changes require preserved differences and explicit artifact-bound review.

Ready chapters execute longest estimated duration first; encoded presentation stays C01..C11. A failed review prevents render dispatch. Worker settings come from paired same-input, same-quality native measurements; no framework or GPU speed claim follows from its name. The default is changed only after successful correctness and performance evidence.

Packaging changes invalidate packaging evidence only. Audio diagnostics, render, decode and review identities are independent of archive implementation. A changed actual artifact still invalidates its own downstream checks. Every attempt has a unique run ID, append-only events and independent summary; retries never overwrite prior evidence. Wall time, overlapping task time, queue time and idle tail are reported separately.

### Engine 0.5.1 maintenance contract

The completed release above used engine 0.5.0. Maintenance 0.5.1 retains this timing/design standard and adds the [targeted assembly fixes](M10_HIGH_IMPACT_FIXES.md). Cache continuous AAC only against exact PCM, sample count, approved voice/model/policy and encoder identities; never reuse concatenated chapter AAC or bypass full audio QA. Cache extraction must exclude inherited chapter metadata. Final chapter marks come from the timing ledger.

One complete decoder pass may jointly prove actual frame count, absence of black intervals and decoder integrity. Later QA must verify the movie/code/runtime/log/progress hashes of that receipt. Metadata-only frame counts are insufficient. Record cache hit/miss and assembly substages explicitly. Chapter capture defaults remain unchanged after failed performance candidates. Maintenance verification does not retroactively change the closed release or establish a new full-production timing result.

## Visual vocabulary and constraints

Text cards remain available alongside standalone original SVG icons, actor figures, service nodes, topology, sequences, packets, resource bars/queues, comparisons, timelines and callouts. Semantic meaning and presentation are separate. Each component declares bounds, ports, parent, layer and measured labels; validation does not depend on a visible card rectangle.

Named `semanticFigure` variant uses maximum height300px and16px label gap, inherited font sizes and uniform source viewBox scaling. Actual geometry and readability must pass before release. The first authored scenes are S01,S07,S17,S23,S27,S33,S40,S44,S47,S48,S49. Other scene layouts remain approved; all scenes adopt new timing. The authorized student figure is extracted from the original S01 person geometry with source-function provenance, not a new Tally identity.

New/redesigned bounds remain x134.4..1785.6,y86.4..993.6. New exceptions: zero. LEGACY-M10-SUBTITLE-001 remains confined to frozen optimization-v1 S01..S58. No exception can waive audio, assets, clipping, provenance or safety.

## Packaging and acceptance

Build an explicit source manifest before writing an archive. Include canonical source, assets, fonts, models, baseline/processed clips, scene PCM, engine and necessary reviews. Omit reproducible chapter/review/boundary hosts and combined host audio; regenerate them locally from included scene PCM. Unknown/circular/outside symlinks fail before copy. Runtime environments remain separately installed pinned dependencies, as in previous editable deliveries.

Stream canonical files directly to a temporary ZIP; verify CRC, extracted hashes, picture reviews and zero-inference cache/host reconstruction before promoting it. Unchanged manifests reuse the verified archive. A changed closed release requires a new workspace. Final ZIP hash/acceptance receipt remains external to avoid circular repacking.

Paired workloads target at least50% reduction; one-hour routine production is a stretch goal. One full new release is authorized, without an additional full-film baseline. Report the exact scope of every improvement; historical whole-film timings are not a controlled A/B. Human end-to-end watching/listening remains separate. No public upload or Git publication is included.

[Full audit](M10_PRODUCTION_PERFORMANCE_AUDIT.md) · [Implementation plan](M10_EFFICIENCY_IMPLEMENTATION.md) · [Source and decisions](../../source/2026-10-20-ceh-m10-performance-optimization/source.md)
