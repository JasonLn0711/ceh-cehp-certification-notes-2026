# M10 reference rollout: production priorities 1–4

Jason authorized implementation of the first four optimization priorities with M10 as the reference project. The rollout preserves the released M04–M10 workspaces and the [initial design standard](PRODUCTION_STANDARD_v1.0.md). Engine versioning is independent of the editorial standard. The [maintained engine](../../tools/ceh_video/README.md) owns reusable execution; this record owns the reference rollout and its evidence.

## Source and adopted scope

Exact available user requests:

> From M04 to M10, what you would recommend based on the process and all the tasks we do for optimization?

> Please plan detailedly to complete the priorities 1-4, and take full action on them, then using M10 as ther reference project.

> Implement the plan.

Adopted implementation scope: audio triage and targeted pronunciation repairs; a shared production engine; declared-input caching and resumable execution; early preflight and artifact-bound visual review. Autonomous rollout covers engineering and evidence-supported technical repairs. Human listening acceptance remains pending. Existing releases and their source packages stay immutable; future module migrations require their own validation.

FIRST PRINCIPLE routing: the scarce resources are operator attention, rendering capacity and trustworthy evidence. This CEH repository owns implementation, source provenance, detailed execution and validation. `planning-everything-track` holds a thin day/project locator, status, capacity impact and next action. Production does not add learner progress, study minutes, quiz scores, practical acceptance or public media publication. The active [UUU route](../../study-plan/uuu-aligned-ceh-cehp-2026-09-18.md) continues to govern study capacity.

## Execution plan and completion checks

| Priority | Work and dependency | Completion evidence |
| --- | --- | --- |
| 1. Audio integrity and review | Freeze approved canonical/spoken text and pronunciation policy. Inspect all 781 actual clips; prioritize alignment leads, units, technical terms, claim boundaries and quizzes. Persist human dispositions by audio identity. Repair only confirmed defects. | Technical queue covers all clips; canonical copy and one narration-only tempo transformation remain intact. A controlled live fixture proves targeted regeneration. Human listening is explicitly pending. |
| 2. Shared engine | Extract generic compilation, chapter preparation/render, alignment, assembly and QA from M10. Keep module art/cues as adapters. Declare content counts, quiz mappings, runtime, assets and model identities in a production profile. Bundle maintained engine with the new editable project. | M10 executes through the shared CLI and thin adapters; original extraction provenance is retained. Non-M10 scene/chapter mapping receives regression coverage. A fresh C11 rendering environment exercises the portable path. |
| 3. Verified reuse and recovery | Hash resolved speech recipes and declared render inputs. Bind stage implementation and dependency outputs. Use atomic receipts, locks, measured events, child logs and process-group cleanup. Preserve partial failures. | Unchanged build executes no stages; a one-sentence expansion regenerates only its clip; a corrupt clip cache recovers; sentence reordering reuses clip bytes; art-only compilation preserves speech. Controlled failure and interruption preserve exit codes and cleanup evidence. |
| 4. Early gates and current review | Construct real native art and quiz layouts before expensive work. Check source coverage, asset/model identity, imports and narration anchors. Capture semantic states. Require current structured review for each chapter and the actual encoded master. | Real palette/anchor/oversize-quiz failures occur before model/render work. Current native captures and review receipts bind source/image hashes. Full browser, seek, quiz, decode, continuity and archive checks establish their respective layers. |

Execution order: freeze/import the baseline → preflight and cache fixtures → native chapter review → actual chapter renders → continuous-PCM master assembly → encoded checks and sampled visual review → delivery verification → extracted/hash-checked ZIP → unchanged-build verification → repository publication. Two concurrent chapter renders with four workers each bound resource use. A failed stage keeps logs and cannot create a verified receipt.

## Reference and artifact custody

The approved reference is `~/Videos/CEH_M10_v1_0/`. Its source ZIP SHA-256 is `5541e68e98096ea998201b445e8ad565b31ce22e809b638e717510854a16cdf0`; its original master SHA-256 is `5fc53be79a9774ae4a3e297b323f79e582e59bdd144c95f040bdf701e9f101c8`. The initializer rehashed all 6,091 baseline delivery payloads before importing verified audio and alignment. The original [M10 delivery record](../../notes/m10-denial-of-service/video-production-2026-10-19.md) remains historical evidence for that release.

The new workspace is `~/Videos/CEH_M10_optimization_v1/`. `project/production.json` declares the actual runtime; `pronunciation.json` preserves the approved expansions. The migration found scripts naming HyperFrames 0.8.174 while the installed lock still resolved 0.8.173. The isolated project reconciles the actual dependency, lock and profile to 0.8.174 and repeats its browser/render validation. The original project remains on its released runtime. No visual, voice, canonical-content or timing policy change is authorized by this dependency correction.

Engine extraction source hashes are recorded in `tools/ceh_video/extraction-provenance.json`. Actual runtime receipts live under the new workspace's `qa/`; compact publication evidence is linked from the rollout closeout below. Models, large media and full frame captures remain local, outside Git.

## Acceptance boundaries and deferred work

The engineering tests and automated audio checks do not clear pronunciation, naturalness or full-film watching/listening acceptance. The 157 alignment flags (119 low-probability and 38 zero-duration word leads in the reference diagnostics) locate uncertainty; they are not confirmed speech defects. Existing fixed-runtime recognition receipts establish availability, with accuracy and latency `not_evaluated`.

M04–M09 remain on their released workflows until explicitly migrated. Bulk rerenders, a different voice, new speech calibration, global visual redesign, ASR benchmarking, public media upload and learner-study activation stay deferred. A confirmed listening defect can activate a narrowly scoped pronunciation revision and downstream rebuild in a new release workspace.

## Rollout evidence

Implemented checks pass: 35 regression tests; six live cache/art scenarios with two real fixture TTS inferences; five actual preflight scenarios covering three early failures; relocated baseline import with 27 reusable clip entries; and a fresh-environment C11 render. The art fixture originally ran on HyperFrames 0.8.173 and passes a separate actual 0.8.174 browser recheck. All 839 production WAV files remain byte-identical to the reference, with zero new production TTS inferences. The technical review queue contains 479 pending listening items and no confirmed technical defects across 781 clips. The actual original-release rehash passes all 6,091 payloads. The completed reference result and artifact identities follow below. The [engine operator guide](../../tools/ceh_video/README.md) describes the executable interface and troubleshooting.


## Validated reference result — October 19

Priorities 1–4 are implemented and validated on M10. All 11 chapters were actually rendered on HyperFrames 0.8.174, including the fresh-environment C11 encode. The final film remains **71:23.733**, **128,512 frames**, **58 scenes**, **10,241 canonical words** and **1,371 subtitle cues**. All 44 inherited locks and 330 source payload hashes pass. Each of eight quiz holds contains exactly 48,000 stereo zero PCM frames; decoded AAC boundary residue is reported separately.

The full browser/quiz/repeated-seek checks, complete decode, audio continuity and sampled picture review passed. The engine captured 328 unique native states and checked their text geometry. Scoped agent chapter findings name the inspected pages. Agent encoded review covers 165 mandatory samples through 20 contact pages, plus two full-resolution opening frames. Final metadata comes from the module profile and preserves M10's existing exported title. The final master and all 165 sampled picture hashes match the inspected candidate.

A real stale C07 capture receipt stopped the render path. The refreshed frame and all current C07 contact pages were inspected; resume preserved nine verified chapter output/receipt pairs and rendered only C07/C09. A batch review gate now checks existing reviews before costly dispatch, and cancellation blocks new child starts. The final unchanged build reused **all 202 nodes and executed zero**. These are exercised engineering results, with no claimed end-to-end speedup or ASR quality ranking.

The editable ZIP contains **5,706 entries**, **3,329,559,090 bytes** and **5,705 extracted payload hashes**, all verified with ZIP CRC and actual extraction. It includes the bundled engine, profile, pronunciation policy, approved audio, models, alignment, module adapters, original source, 58 transcript receipts and production review evidence. Runtime environments/caches and unrelated Planning/coursework custody notes are excluded.

Local outputs:

- Film: `~/Videos/CEH_M10_optimization_v1/output/CEH_M10_Denial_of_Service_en-US_1_5x_1s_master.mp4`.
- Editable archive: `~/Videos/CEH_M10_optimization_v1/output/CEH_M10_optimization_v1_EDITABLE.zip`.
- Subtitle files, 11 chapter MP4s, continuous PCM and `engine-render-report.md` are adjacent.
- Listening queue: `~/Videos/CEH_M10_optimization_v1/qa/audio-audition/index.html`.

Master SHA-256: `64d31b284dd80fe4d099d7394bb140f845473eee2bb974a4bdf1c8cc2677a46a`. ZIP SHA-256: `5f552a5b14b9fa0728fbcd9ae2f90a3269fbe565e2410215594d848ee54975f2`.

[Compact runtime and archive evidence](../../source/2026-10-19-ceh-video-engine-optimization/validation/README.md) separates 35 regression tests, live fixtures, actual media, cache reuse and archive verification. Human pronunciation/naturalness and full-film listening remain pending for 479 prioritized items; public media release remains unactivated. Git publication concerns implementation/docs/compact evidence only. Existing M04–M10 releases remain preserved.

Planning keeps thin mirrors in the [October 19 day note](../../../planning-everything-track/weeks/2026-W43/days/2026-10-19.md#ceh-video-engine-optimization), [W43 plan](../../../planning-everything-track/weeks/2026-W43/weekly-plan.md#ceh-video-engine-optimization) and [CEH project locator](../../../planning-everything-track/data/projects/2026-07-ceh-cehp-certification-training.md#ceh-video-engine-optimization). The original learning route and independent human listening gate remain in force.
