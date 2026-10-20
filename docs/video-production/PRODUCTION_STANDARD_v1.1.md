# CEH English production standard v1.1

## Active full-remaster application

Engine 0.4.0 applies this standard to all 58 M10 scenes through `design_profile: m10-editorial-remaster-v1.1`. The production token manifest is `design/tokens.json` version 1.2.0. Engine, token, and audio-policy versions are independent. Mandarin schema 2 retains its own approved policy.

Status: the remaster compiler, source-bound scene specifications, and strict QA guards are **implemented and tested**. Full-scene golden, boundary and asset validation have passed. All eleven chapters and the full master are **rendered and technically tested**. Full decode and audio continuity pass; editable archive verification has **passed**. Actual evidence: `qa/visual/scenes/manifest.json` and `qa/remaster-regression.log` record 558/558 passing golden comparisons; `qa/final-visual-gate.json` passes all 58 current-source scenes with zero exceptions. Boundary QA passes 171 states and asset QA passes 905 sampled states. The complete encoded master passes technical checks (`qa/run-checks.json`); ZIP verification passed. Historical engine 0.3.0 evidence remains valid only for its own inputs.

All new and redesigned scenes enforce x134.4–1785.6 and y86.4–993.6. Preserve the approved font binaries, warm paper palette, Tally identity, Northstar case, narration, questions and answers. Changes to layout and motion cannot change the exact PCM timing contract. Full production requires the complete screenshot inventory, all-frame geometry, exact quiz holds, 171 nested boundary states, encoded checks, and source-bound reviews.

Only `LEGACY-M10-SUBTITLE-001` applies to frozen optimization-v1 S01–S58. The new remaster has zero exceptions. No exception can waive PCM precision, asset identity, clipping, or provenance.

Effective 2026-10-20. Engine version is independently managed; the active remaster uses 0.4.0.
Status: **implemented** in the English profile selected by `audio_policy: ceh-en-v1.1`; validation results are recorded in [CURRENT_SYSTEM_AUDIT.md](CURRENT_SYSTEM_AUDIT.md). v1.0 and historical M10 delivery evidence remain unchanged.

## Binding contracts

Preserve M04 Editorial Masterclass v3.0: warm paper, the approved palette, original Tally rig, Northstar Learning Center, American English teaching copy, chapters and eight quizzes. Use the approved Liberation Sans regular/bold and DejaVu Sans Mono binaries, identified by SHA-256. Descriptive Inter/Arial text in the historical token file does not authorize a font substitution.

| Contract | v1.0 historical | v1.1 active English |
|---|---|---|
| Kokoro voice / language / synthesis | af_heart / en-US / 0.73 | unchanged |
| Spoken processing | one atempo=1.5 | exactly one atempo=1.4 from baseline PCM |
| Opening | 24,000 frames | 14,400 frames |
| Sentence gap | 8,640 frames | 9,600 frames |
| Ending | 144,000 frames | 24,000 frames |
| Quiz hold | 48,000 frames | 48,000 frames, eight holds |
| Output | 1920×1080, 30 FPS | unchanged |
| Video / animation rate | 1× | unchanged |
| Music | off | off |
| New scene bottom boundary | historical zone ambiguity | 993.6 px at 1080 height |

Audio frames are stereo frames at 48 kHz. Named silences contain zero-valued PCM. Frame-alignment padding has its own ledger entries and never changes a named duration. See [AUDIO_TIMING_POLICY.md](AUDIO_TIMING_POLICY.md).

All newly generated or redesigned scenes obey 7% horizontal and 8% vertical safe areas. The subtitle panel must fit within the bottom boundary; clipping or hidden overflow is a failure. Frozen `CEH_M10_optimization_v1` S01–S58 alone have `LEGACY-M10-SUBTITLE-001`, restricted to the documented subtitle zone. The new workspace inherits **zero exceptions**. [LAYOUT_AND_GEOMETRY_RULES.md](LAYOUT_AND_GEOMETRY_RULES.md) defines the exact scope.

## Enforcement and scope

Hard constraints: PCM counts, exactly-once processing, canonical coverage, no early quiz answer, loaded approved fonts, intact asset hashes, deterministic seek, safe-area bounds, non-clipped text, connected anchors, valid aspect ratios, dependency identity and reviewed screenshot regressions. `visual_gate.py` blocks new English scene renders and delivery without current passing evidence.

Soft guidelines: composition balance, decorative density and choice among inherited easing/component variants. Changes require a reason and a traceable diff. A documented exception names its ID, scenes, component selectors, original rule, reason, approver/review, tests, version and expiry/scope. Exceptions cannot waive audio, provenance, asset integrity or safety requirements.

The active remaster covers all 58 scenes, eleven chapter encodes, the complete master and a verified local editable archive. The earlier representative-only engineering run remains historical evidence. Full master execution and technical checks are complete; ZIP packaging and extraction checks are complete; publication and human acceptance are separate. Mandarin schema 2 retains its separately approved policy.

The maintained documents are [motion system](MOTION_DESIGN_SYSTEM.md), [rendering architecture](RENDERING_ARCHITECTURE.md), [visual QA](VISUAL_QA_STANDARD.md), and [migration/rollback](MIGRATION_AND_ROLLBACK.md).

Actual master checkpoint: `CEH_M10_Denial_of_Service_en-US_Editorial_Remaster_v1_1_1_4x_1s_master.mp4` is 1920×1080 at 30 FPS, 132,727 frames / 73:44.233. SHA-256: `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`. `qa/run-checks.json` is verified; full decoding found zero black intervals, and all 212,363,200 reference audio frames passed continuity comparison. All 165 encoded sample pictures passed artifact-bound agent review: `qa/encoded-review-coverage.json` binds the three inspection receipts and `qa/encoded-review.json` records the actual CLI review against the current master and all 165 hashes. ZIP extraction verification passed. Human viewing/listening remains pending.

Final local delivery: the master is 207,412,180 bytes, SHA-256 `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`; `CEH_M10_editorial_remaster_v1_1_EDITABLE.zip` is 3,707,042,054 bytes, SHA-256 `4f5d3e5a2a82672466cd0830fc02a16a39a14d571810aef13f1bca9976b7264e`. `qa/engine-packaging.json` verifies ZIP CRC, extraction, 8,369 files and 8,368 payload hashes, including 165 encoded pictures and the cited golden-review receipts. `qa/engine-extracted-reconstruction.json` confirms 781 restored clips with zero inference and zero tempo passes. `qa/encoded-review-revalidation.json` confirms the same master and all 165 reviewed picture hashes after the conservative check rerun.

Project documents inside the ZIP retain their honest packaging-time checkpoint. These final repository records and the external receipts establish completed archive acceptance; the frozen project, staging tree and ZIP were not rewritten. Human listening remains pending for 478 items; the one-clip ASR run establishes minimum availability only, with full-film accuracy/timing `not_evaluated`.
