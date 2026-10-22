# M11 Session Hijacking — English Masterclass production

Status: implemented and tested — complete film and editable archive delivered locally; automated and agent visual checks passed. Full human viewing/listening pending. Owner: CEH repository. Workspace: `/home/jnlngx10/Videos/CEH_M11_initial_v1/project`. Large media and raw runtime evidence remain local. Planning holds locator, capacity and next gate only.

[User request](../../source/2026-10-20-ceh-m11-video-production/source.md) · [Initial series baseline](../../docs/video-production/INITIAL_SERIES_STANDARD.md) · [M11 practice scope](../../assessments/practice-bank/m11.md)

FIRST PRINCIPLE: protect learner attention, production/review waiting time, compute/storage and reliable evidence. Use the approved English production identity, adapt only module-owned teaching content and illustrations. New scenes inherit no visual exceptions. Exact final duration follows measured speech; no artificial WPM adjustment. The film uses fictional Northstar examples and offline synthetic evidence. It does not count as learner quiz/practical completion.

## Content and acceptance plan

Eleven chapters: session foundations; lifecycle; takeover mechanisms; browser boundaries; TCP sessions; secure transport; defensive architecture; offline evidence; incident response; eight narrated questions; synthesis. The content distinguishes token theft, fixation, prediction and replay, application and transport sessions, XSS and CSRF, authentication and authorization. Eight quiz holds remain exactly one second of zero PCM each.

Build and inspect representative scenes before full geometry/seek/screenshot QA. Render reviewed chapters longest-first, assemble one master, run complete decode and audio validation, inspect encoded samples, then package once. Preserve all failures and actual stage timing. Human timecoded viewing/listening is a separate next gate.

## Implemented and measured during authoring

- Source: 48 scenes, eleven chapters, eight original film questions, 7,603 canonical spoken words. The module has its own diagram specifications and narration cues.
- Engine 0.5.4: explicit module scene specifications, semantic-scene inventory, representative-scene selection and profile-sized full/boundary QA; historical M10 fallback preserved. The full suite passed 127 tests before the final coverage-count correction; the subsequent six-test module suite verifies both 40- and 50-scene coverage and rejects missing, duplicate, incomplete or faulty geometry evidence. Node geometry tests also passed.
- S01: actual HyperFrames geometry precheck passed; eight candidate snapshots had zero forward/reverse/repeated seek differences. Agent inspected a full-size late state with readable labels, original Tally and subtitle clearance. This is preliminary scene evidence, not full-film acceptance.
- Speech and forced alignment are real local runs with independent receipts. The fixed-runtime ASR availability check initially hit a PyAV 19 / faster-whisper file-adapter incompatibility (`metadata_errors` argument); retained the failure and used pinned FFmpeg to decode one clip to mono 16 kHz float32 for the same base.en/int8 CPU inference. Functional transcript persisted. Accuracy and latency remain not_evaluated; full-film recognition was not run.
- A bounded four-thread CPU synthesis candidate was not adopted: no controlled paired production benefit or full audio review was established. The first comparison selected the wrong baseline clip; the corrected comparison and all three warm trials remain in local QA. The approved synthesis settings and voice remain unchanged.
- C01 native HyperFrames lint, runtime, layout and contrast checks passed with zero errors/warnings. Agent inspected all three contact sheets covering S01–S04 teaching cues, midpoint and completion; the artifact-bound chapter review records readable labels/captions and no observed clipping or overlap. This does not establish full-film encoded acceptance.
- S37 candidate inspection covered all fourteen states, including the question/hold/answer boundaries. All A–D options precede the hold; no caption or answer is visible during it. The candidate had zero geometry and deterministic-seek failures. Final full-module golden approval and regression subsequently passed; the earlier scoped evidence remains preserved.
- Three narration lanes keep shared canonical sentence cache keys in one lane to prevent concurrent writes. The alignment consumer processes whichever scene is ready, removing presentation-order waiting. The initial serial attempt and two superseded alignment attempts remain in the run ledger; their elapsed time belongs to first-production/retry costs.
- The source package separates `authoring-questions.json` from the canonical `questions.json` envelope. Clean-directory compilation reproduced the four canonical scene, quiz, diagram and cue manifests. Ten diagram notes now state concrete distinctions or synthetic fixture results; narration and quiz payloads remained semantically unchanged.
- The initial chapter capture command used the repository as its working directory and could not resolve Puppeteer through the project's runtime. The retry ran from the project directory and succeeded. Both logs remain available; this was a command-context failure, not evidence that a new dependency was required.
- A read-only HyperFrames update check reported 0.8.181 while this production pins 0.8.174. The pinned runtime, Chromium and GSAP versions remain unchanged; upgrading requires a separate compatibility check of the seek/boundary adapter. The check did not establish compatibility with the newer release.

Raw run evidence: `/home/jnlngx10/Videos/CEH_M11_initial_v1/qa/`. First-authoring, routine synthesis/alignment, failed attempts, native render and final delivery must remain distinct in the closeout. Authoring conversation time was not independently instrumented as operator labor. Other research processes were observed on the shared host; no exclusive-host timing claim applies.

- Before full candidate capture, native inspection identified misleading sequence arrows in S04 (failure categories) and S07 (independent timeout limits). Both now use parallel comparisons. Only C01/C02 native checks/captures were rebuilt; narration was unchanged. Fifteen C01 and sixteen C02 images remained byte-identical; all changed states were inspected and new source-bound reviews recorded. The interrupted full precheck remains in its retry ledger; no completed full candidate baseline was discarded.
- The validation coordinator now waits for current native chapter reviews before full QA and writes each attempt's logs under its own run directory. Source-package compilation was rechecked after the comparison correction.

## Measured pre-encoding evidence

- Completed 591 spoken clips across 48 scenes. Measured lossless timeline: 162,472,000 stereo audio frames at 48 kHz, or 101,545 video frames at 30 FPS (56:24.833). Eight quiz holds contain exactly 384,000 zero PCM frames; opening, sentence gaps, ending and frame alignment are separately verified. Final AAC continuity passed; codec residue and tail padding are recorded separately below.
- All eleven native chapter checks and current artifact-bound visual reviews passed. Full precheck passed all 48 scenes. Full candidate capture passed 432 states with zero geometry or deterministic seek failures; 17 contact pages containing 152 selected states were actually inspected (40 teaching states and all 112 quiz states). Initial golden approval is bound to this candidate and review hashes. Independent golden regression subsequently passed all 432 states; encoded QA passed 145 sampled states after actual inspection.
- Integration run `20261020T173612Z-2ad30f59` passed 141 nested boundary states, 600 asset states and eight quiz negative checks. Its measured wall time was 326.53 seconds.
- Three-lane narration coordinator `20261020T160400Z-50e003e9` completed in 4,847.36 seconds; alignment consumer `20261020T160524Z-e314698c` completed in 4,856.72 seconds including readiness waiting; native preparation `20261020T165311Z-b0cc22eb` completed in 2,078.46 seconds including waiting. These overlap and cannot be summed as end-to-end time or personal labor. New M11 synthesis cannot be compared directly with warm-cache M10 reuse.
- Planned native encoding order from measured chapter duration: C10, C02, C07, C04, C05, C09, C01, C03, C06, C08, C11. C10 is longest at 473 seconds; C11 is shortest at 282.37 seconds. Presentation order remains C01–C11. Actual order matched this plan; measured render window was 2,957.51 seconds and the final C11-only tail was 105.95 seconds.

## Rendered-film validation and delivery

`20261020T175442Z-6404978f` completed all 173 production/check nodes in 4,208.61 seconds, including 2,957.51 seconds of overlapping chapter rendering, 901.37 seconds of master assembly/full decode, 42.79 seconds of encoded-frame checks, 99.15 seconds of audio continuity and 16.98 seconds of late-diagram sampling. Node execution includes verified clip/check reuse; all 591 spoken clips were reused without inference at this stage. The summed stage work is not elapsed time. No chapter render failed or required a retry.

- Full decode: 101,545 frames, zero detected black intervals; MP4 SHA-256 `3e47e52251bad57998473807177ebdb86c57d266fe2654553122634e41ca7743`.
- Actual encoded picture review: 18 contact sheets, 145 samples (48 scene midpoints, 33 chapter boundaries/midpoints, 24 quiz states, 40 completed diagrams). All inspected with no observed clipping, unwanted overlap or early answer reveal. Chapter opening/reveal states follow the source-bound timeline.
- Audio continuity: all 162,472,000 reference frames compared; no all-zero replacement blocks. Decoded AAC has 960 tail-padding frames (0.020 seconds), separate from the timeline. The maximum quiz-hold residual is 0.9105926156 PCM16 units, measured in floating-point decode. PCM holds remain exactly zero. AAC container duration is rounded to 3384.833 seconds; the video and lossless reference retain the exact frame timeline.
- Technical audio triage checked 591 clips with zero technical defects. It queued 297 clips for technical terms, quantities, quiz content or other review leads; these are not 297 confirmed defects. Human pronunciation, naturalness and full-film viewing/listening remain pending.
- Initial release attempt `20261020T190514Z-35ba87b4` reused all 173 production/check nodes, then was intentionally interrupted during packaging after 43.27 seconds to correct a generic report locator that named a historical reference-import receipt absent from fresh M11. The partial archive and old report remain under local `qa/authoring-history/report-locator-correction/`. The corrected report identifies actual M11 evidence and distinguishes included verified speech PCM from excluded runtime caches. Thirteen targeted delivery-evidence tests passed. Retry `20261020T190725Z-6797fb91` completed in 202.08 seconds: 18.23 seconds delivery checks and 138.85 seconds packaging/verification, with 173 production/check nodes reused. Media and audiovisual QA were not rerun.

## Local deliverables and remaining acceptance

All files are in `/home/jnlngx10/Videos/CEH_M11_initial_v1/output/`:

| Artifact | Exact bytes | Result |
| --- | ---: | --- |
| `CEH_M11_Session_Hijacking_en-US_Editorial_v1_master.mp4` | 145,516,716 | 1920×1080, 30 FPS, 56:24.833, eleven embedded chapters |
| `CEH_M11_English_Masterclass_v1_EDITABLE.zip` | 1,449,652,005 | CRC extraction and 4,932 payload hashes verified |
| `master.reference.pcm.wav` | 649,888,044 | Lossless 48 kHz stereo reference |
| `captions.en-US.srt` / `captions.en-US.vtt` | 87,379 / 83,389 | 1,021 measured subtitle cues |
| `chapters.txt` | 427 | Eleven chapter positions |
| `engine-render-report.md` / `SHA256SUMS.txt` | See output inventory | Validation boundaries and exact artifact hashes |

[Compact validation evidence](video-evidence/validation-summary.json) and [selected measured stage ledger](video-evidence/stage-timing.json) preserve the owner-repo audit trail. Full raw logs, screenshots, failed attempts and media remain in the local workspace. The verified ZIP restores all 591 spoken clips with zero model inference and zero tempo passes, plus twelve PCM host hashes and twelve normalized HTML host identities (master and eleven chapters). Media staging bytes were zero; verification extraction was separately measured. The final ZIP SHA-256 is `57b208874881f4f09e8d8388ee06a1eb1e951ea622b458a6da2de3d84dad240d`.

M11 has zero visual exceptions. `LEGACY-M10-SUBTITLE-001` remains scoped to the historical M10 release. No older module or approved asset was overwritten. Full human listening/timecoded viewing remains pending; full-film ASR accuracy and latency remain `not_evaluated`. No public media upload, Git commit or push was performed for this task. No learner quiz, practical or Blog completion is inferred.

Next acceptance: review the delivered MP4 and the prioritized audio queue (`qa/audio-audition/index.html`) and record any concrete timecoded defects before a new revision. Runtime upgrades, new rendering frameworks, whole-series rerenders and voice recalibration remain outside this release.

## October 21 continuation (Asia/Taipei)

Production crossed midnight after the October 20 adoption. Run receipts retain actual UTC times; this source record keeps the original start date. [Planning adoption](../../../planning-everything-track/weeks/2026-W43/days/2026-10-20.md#ceh-initial-series-m11) → [October 21 continuation](../../../planning-everything-track/weeks/2026-W43/days/2026-10-21.md#ceh-m11-production) → [project locator](../../../planning-everything-track/data/projects/2026-07-ceh-cehp-certification-training.md#ceh-initial-series-m11). No learner completion or personal labor duration is inferred from unattended media processing.

## Director-led workflow adoption — October 21

The [new authoring workflow](../../docs/video-production/DIRECTOR_LED_WORKFLOW.md) records user-owned content/script and assistant-designed visuals, with whole-film review and scene-level decisions. [Exact choices and documentation evidence](../../docs/video-production/DIRECTOR_LED_ADOPTION.md) distinguish this adoption from production. [S06](../../docs/video-production/templates/director-led/M11_S06.example.md) is a source-bound proposed storyboard example only. No M11 source, engine, media or existing approval receipt was changed; no new camera sequence was rendered. Future creative approval and the existing full human viewing/listening gate remain separate.

Later Git publication and Planning status: [October 22 closeout](../../docs/video-production/PUBLICATION_2026-10-22.md). Earlier publication statements remain historical snapshots.
