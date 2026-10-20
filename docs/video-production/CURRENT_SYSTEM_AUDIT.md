# CEH motion engineering audit — 2026-10-20

## Active full editorial remaster — engine 0.4.0

The user expanded production to all 58 scenes and the complete eleven-chapter film. The active workspace is `/home/jnlngx10/Videos/CEH_M10_editorial_remaster_v1_1/project`, with design profile `m10-editorial-remaster-v1.1` and project `design/tokens.json` version 1.2.0. Production standard and English audio policy remain v1.1. The reference engineering workspace `CEH_M10_motion_v1_1` remains preserved.

| Deliverable | Current state | Next evidence |
|---|---|---|
| Source-bound specifications and compiler for S01–S58 | implemented, tested | 2,143 text boxes and 558 golden states pass; full encoded decode passes |
| Dynamic ports, obstacle routing, absolute-time packet motion | implemented, tested | 110,721 diagram frames and golden regression pass; fixed independent ports in 11 scenes; full encoded decode passes |
| Full capture inventory and strict render gate | implemented, tested | 558/558 golden states, 171 boundaries, 905 asset states; all 58 current-source scenes pass |
| Copied 1.4× caches and source package | implemented; audio and source tested | Actual 117-node audio run reused every clip; `qa/remaster-delivery-readiness.json` verifies 330 source hashes and exact canonical payload; final package hash verification remains |
| Active voice-calibration metadata and configured worker count | implemented; metadata tested | Readiness receipt verifies af_heart / 0.73 / once-1.4×; all eleven chapter codec/frame/GPU receipts pass |
| Eleven chapters and complete master | implemented, tested | 132,727 frames; full decode, zero black intervals and continuous-audio comparison pass |
| Editable ZIP | implemented, tested | CRC, 8,368 extracted payload hashes, 165 pictures and 781 restored cache entries verified |
| Human listening and full-film acceptance | blocked on actual human review | Concrete listening/viewing findings |

The completed, decoded full master contains 132,727 video frames and 212,363,200 stereo audio frames: 73:44.233 at 30 FPS and 48 kHz. Actual evidence is recorded in `qa/master-ffprobe.json`, `qa/rendered-artifact-audit.json` and `qa/audio-continuity-audit.json`.

Current implementation locations: `tools/ceh_video/ceh_video/remaster.py:57` compiles components, `:86` builds scenes; `visual/remaster-geometry.mjs:105` routes ports; `visual_gate.py:41` independently derives required captures and `:81` checks the complete report; `graph.py:16` owns visual-only dependency identities; `runtime/chapter.py:8` validates configured workers. Source-bound scene rationale lives in `remaster_early.py` and `remaster_late.py`.

The active calibration record previously carried 1.5× metadata copied from the source. It now identifies the selected 1.4× policy, verified by `qa/remaster-delivery-readiness.json`, while the source-package copy remains historical. The earlier gate accepted one passing screenshot per scene; the new profile requires the complete independently calculated set. The chapter renderer now consumes the configured worker count instead of a fixed four.

Affected scenes: S01–S05 framing; S06–S10 resource mechanisms; S11–S16 constrained links; S17–S22 TCP/state; S23–S28 reflection; S29–S33 application work; S34–S38 evidence; S39–S42 controls; S43–S46 Northstar cases; S47–S49 response/AI boundaries; S50–S57 quizzes; S58 synthesis. Every range is included in the remaster. New-scene exceptions: **zero**. The lock inventory now includes 73 approved original files; 29 existing props were added with source-package hash verification, without changing their bytes.

Current audio review: the one-clip ASR availability check is `LIVE_MINIMUM_COMPLETED`, with accuracy/timing `not_evaluated` and no full-film transcription. Technical triage reports zero defects across 781 clips; 161 alignment flags across 142 clips feed a queue of 478 pending listening items. See [the audio evidence scopes](AUDIO_TIMING_POLICY.md#current-technical-review-and-listening-boundary).


Actual master checkpoint: `CEH_M10_Denial_of_Service_en-US_Editorial_Remaster_v1_1_1_4x_1s_master.mp4` is 1920×1080 at 30 FPS, 132,727 frames / 73:44.233. SHA-256: `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`. `qa/run-checks.json` is verified; full decoding found zero black intervals, and all 212,363,200 reference audio frames passed continuity comparison. All 165 encoded sample pictures passed artifact-bound agent review: `qa/encoded-review-coverage.json` binds the three inspection receipts and `qa/encoded-review.json` records the actual CLI review against the current master and all 165 hashes. ZIP extraction verification passed. Human viewing/listening remains pending.

### Historical bounded-run audit follows

The following audit and numerical test results describe engine 0.3.0 in `CEH_M10_motion_v1_1`. Its 56 Python tests, five geometry tests, 86 snapshots, representative encodes, and PCM checks do not certify the new remaster. Historical scope exclusions below apply to that completed slice only.

Canonical owner: `ceh-cehp-certification-notes-2026`, baseline Git revision `03becdf`. Maintained engine was 0.2.0; this work increments it independently to 0.3.0. Frozen M10 optimization-v1 identifies engine 0.1.0. A reference-document snapshot is not the executable project.

Execution workspace: `/home/jnlngx10/Videos/CEH_M10_motion_v1_1/project`. Reference: `/home/jnlngx10/Videos/CEH_M10_optimization_v1/project`. Scarce resources are verified source custody and local rendering/model time. The repository owns code, contracts and compact evidence; Videos owns media/runtime/raw QA. Planning has no new execution-detail copy.

## Existing capabilities and concrete gaps

Historical line references below refer to revision `03becdf`; current added modules use working-tree lines. This distinction keeps the audit reproducible after code moves.

| Finding | Existing capability / evidence | Change or remaining gap |
|---|---|---|
| Speech cache | `speech.py:26–61` already hashes canonical/resolved pronunciation, voice/models and files | Old `:43, :73–78, :95–100` fixed atempo1.5 and buffers; new `audio_policy.py:4–19`, baseline cache and integer ledger replace active hardcodes |
| Timing/alignment | `runtime/force_align.py:16–67` already uses local Whisper attention/DTW and new audio hashes | Preserve method; regenerate after processing; flags remain review items |
| Receipt graph | `graph.py:15–52, :88–125` already fingerprints stages/dependencies and verified outputs | Include audio policy and new gate; prevent historical seed receipts being relabeled v1.1 |
| Asset custody | `preflight.py:42–55` already checks locked files, models and local fonts | Retain all 44 locked asset hashes and original Tally rig; no re-export |
| GSAP seek | `runtime/build_film.py:11–32` already creates finite paused timelines keyed by scene | Real HyperFrames seek tests add completion barriers and pixel comparisons |
| Scene toolkit | `runtime/editorial.py` and `art_common.py` already provide cards, routes, labels, props and rig poses | New pure port/grid/component specs complement them; historical hand-authored geometry is not all migrated |
| Captures | `capture.mjs:12–46` already captures narration-linked native DOM states | Its direct GSAP seek is not proof of HyperFrames adapter readiness; new harness uses actual runtime |
| Seek/quiz QA | `runtime/audit_scene_seek.mjs`, `audit_quiz.mjs:24–43` already check reverse state / eight quiz boundaries | Add integer PCM ledger, exact boundary frame samples, geometry and read-only goldens |
| Output | `runtime/assemble_master.py` already preserves PCM and encodes AAC once for the full master | New audio-only path preserves continuous PCM without requiring a full-film render |
| Subtitle zone | Frozen DESIGN declares y945–1028; measured 1,371 boxes max bottom992.09375 | Document legacy reservation; enforce <=993.6 for new output, no silent extension |
| Top margin | Actual chapter label y85, top safe86.4 | New compiler y87; no exception |
| Typography | STYLE_TOKENS describes Inter/Arial; actual CSS embeds Liberation Sans and DejaVu Sans Mono | Preserve actual approved binaries and hashes; record mismatch explicitly |
| Initializer | `initialize.py` imports original source synthesis script and copied legacy receipts | New `engineering.migrate` supports verified optimized reference and rejects existing destinations |
| Governance | Old full-film review and package guards already exist | Add source-bound new-scene visual gate and narrow exception register |

Paths in the table are relative to `tools/ceh_video/ceh_video/`. Existing functions are retained as existing capabilities, not advertised as new features.

## Environment and reusable inputs

Linux aarch64, Ubuntu24.04, Node24.22.0, FFmpeg6.1.1, local Python scientific/Whisper/Kokoro runtime. Installed HyperFrames0.8.174 and Chromium151.0.7922.34 revision1234. WebGL2 uses ANGLE/SwiftShader software rendering. The approved local GSAP asset is3.14.2. Docker daemon access is unavailable; native execution works. Hardware GPU performance is not established.

All 781 spoken baseline references matched their historical raw hashes and recipe metadata before migration: 24 kHz mono PCM16. Old processed clips are 1.5× and are never accepted as 1.4×. The migrated run processed baseline PCM exactly once at1.4 with zero new Kokoro inference. Canonical word count remains10,241; scenes58, chapters11, questions8.

## Selection and scope

Option A remains the production choice: HTML/CSS/SVG + GSAP with computable geometry and strict QA. Option B adds Pixi only in a bounded six-second S23 engineering comparison; no general performance advantage is claimed. Full discussion and pinned licenses are in [RENDERING_ARCHITECTURE.md](RENDERING_ARCHITECTURE.md).

The original narrated S17/S23 and all eight quiz boundary states are the representative production acceptance set. Every scene receives new audio/alignment/timing, but no full 11-chapter/master MP4 or editable delivery ZIP is authorized by this strict slice. Figma exchange, broad component migration, remote CI and hardware-GPU comparison remain separate activation gates.

## Exceptions and affected scenes

Exactly one registered exception: `LEGACY-M10-SUBTITLE-001`, frozen optimization-v1 `.caption` reservation only, explicit S01–S58 membership and source-profile and all 58 frozen composition hashes in `visual/exceptions.v1.1.json`. It applies to zero scenes in the new workspace. No exceptions to fonts, narration, clipping, overlap, assets, audio or source custody were added. New generated S01–S58 receive chapter y87 and caption y940; their timing is regenerated.

## Implementation and evidence status

| Deliverable | Status | Evidence / limit |
|---|---|---|
| v1.1 standard and audio contract | implemented, tested | `audio_policy.py`, `qa/audio-policy-v1.1.json` |
| Raw/processed cache separation | implemented, tested | 781 verified baseline imports; no inference; old cache isolation test |
| 58 scene PCM / continuous reference | implemented, tested | 212,363,200 stereo frames; eight exact holds totaling384,000 |
| Alignment/captions/anchors/chapter timing | implemented, tested | 781 new hash-bound alignments; 1,371 captions; 58 compositions; 11 chapter marks; 161 review flags in 142 clips remain for listening |
| Tokens, pure geometry and component specifications | implemented, tested | Node tests and actual fixture geometry; not all production components converted |
| SVG/Pixi runtime comparison | implemented, tested | Actual HyperFrames seek, read-only screenshot runner; native software WebGL |
| Screenshot/geometry/seek gate | implemented | New production scenes fail closed without matching passing evidence |
| Representative encoded video | implemented, tested for two six-second fixtures; narrated S17/S23 closeout recorded in evidence | H.264 1920×1080 / 30 FPS, exact frame counts verified |
| Eight AAC boundary measurements | implemented, tested | Nonzero AAC residuals in every hold, peak 1 PCM16 unit; PCM holds remain exactly zero |
| Figma round trip / no-WebGL Pixi fallback / GPU performance | proposed | No supplied Figma file or demonstrated production need |
| Remote CI and branch protection | workflow implemented; activation blocked | Self-hosted ARM64 runner / publication not configured or authorized here |
| Human listening/full-film approval | not performed | Automated tests and agent image inspection do not substitute |

## Observed failures and fixes

The first Python run exposed a changed exception type in legacy profile validation; compatibility was restored. Migration initially omitted a locked reference-board file and dereferenced node executable symlinks; the copy contract now includes all protected paths and preserves node-package symlinks. HyperFrames initially rejected paths above the fixture project root; self-contained fixture bundles fix that. It also identified the Pixi canvas above text; explicit layer ordering puts text above the packet canvas. Failure evidence is retained locally, not converted into a success claim.

Run records, image manifests, test logs and remaining gates are summarized in `evidence/motion-v1.1/`. See [migration](MIGRATION_AND_ROLLBACK.md) for commands and rollback. No commit or publication is implied.

## Final bounded findings

All 2,200 measured caption, heading, teaching, quiz and SVG-label boxes pass across 58 newly generated scenes. Maximum measured text bottom is987.09375 against993.6. The representative regression set contains78 narrated-scene states and8 fixture states. New-workspace exception count is0. The registered historical exception binds58 individual frozen composition hashes as well as the source profile.

Remaining engineering limits: full primitive/connector conversion beyond the bounded fixture, Figma round trip, no-WebGL Pixi fallback, hardware performance and remote CI activation. Listening review must inspect161 forced-alignment flags across142 clips; no pronunciation or human-acceptance score is inferred. Existing test-process ResourceWarnings remain a separate legacy cleanup item.

Final local delivery: the master is 207,412,180 bytes, SHA-256 `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`; `CEH_M10_editorial_remaster_v1_1_EDITABLE.zip` is 3,707,042,054 bytes, SHA-256 `4f5d3e5a2a82672466cd0830fc02a16a39a14d571810aef13f1bca9976b7264e`. `qa/engine-packaging.json` verifies ZIP CRC, extraction, 8,369 files and 8,368 payload hashes, including 165 encoded pictures and the cited golden-review receipts. `qa/engine-extracted-reconstruction.json` confirms 781 restored clips with zero inference and zero tempo passes. `qa/encoded-review-revalidation.json` confirms the same master and all 165 reviewed picture hashes after the conservative check rerun.

Project documents inside the ZIP retain their honest packaging-time checkpoint. These final repository records and the external receipts establish completed archive acceptance; the frozen project, staging tree and ZIP were not rewritten. Human listening remains pending for 478 items; the one-clip ASR run establishes minimum availability only, with full-film accuracy/timing `not_evaluated`.
