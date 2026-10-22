# CEH video engine 0.6.0

Local production engine for the [CEH English series standard](../../docs/video-production/PRODUCTION_STANDARD_v1.2.md). M10 is the reference migration. The engine owns execution, verified reuse, process receipts and review guards; each module owns its canonical script, native diagrams, quiz, evidence, assets and production profile. Full human listening remains a separate acceptance step.


## Engine 0.5.1: continuous AAC reuse and one full decode

The [two targeted fixes](../../docs/video-production/M10_HIGH_IMPACT_FIXES.md) preserve the approved video, font, narration and timing policies. Unchanged full PCM can reuse an integrity-bound continuous AAC track; new masters still undergo complete audio QA. One full video decode supplies actual frame count, decoder integrity and black detection, and downstream checks validate its movie-bound receipt. The existing completed v1.2 release remains frozen; this maintenance work uses a separate validation workspace.

`qa/master-stage-timing.json` records the assembly substages. `qa/master-audio-cache.json` reports whether AAC encoding was reused. `qa/master-full-decode.json` binds the actual count and raw progress/log to the movie and FFmpeg. Missing or stale scan evidence blocks checks. `.production/master-audio` is a disposable local cache; removing it causes the next assembly to encode AAC again, without regenerating narration. Cache extraction excludes chapter metadata; final chapter marks still come from the canonical timing ledger.

The new tests run with the approved Python environment:

```bash
PYTHONPATH=tools/ceh_video "$CEH_PY" -m unittest discover -s tools/ceh_video/tests
```

Full-film timing improvements require their own measured run. This patch does not change chapter capture defaults: the tested screenshot/filter-thread candidates were rejected. See the linked report for exact test scope and retained failures.

## M10 v1.2 efficiency upgrade — preserved release record

The paths in this section identify the completed 0.5.0 reference release. Use a new owned workspace for 0.5.3; do not point modifying commands at the frozen release.

The active new-work contract is [production standard v1.2](../../docs/video-production/PRODUCTION_STANDARD_v1.2.md). The prior completed v1.1 release remains unchanged. New workspace: `/home/jnlngx10/Videos/CEH_M10_efficiency_v1_2/project`. New `init`/`migrate` runs default to `ceh-en-v1.2`; `--audio-policy ceh-en-v1.1` explicitly selects historical timing. The v1.2 migration reuses pinned runtime directories through local links, omits regenerated combined audio, and imports validated 1.4× clips and relative alignment when compatible. This migration route still requires its own real-workspace acceptance; fixture tests do not establish a delivered film.

The registered English policy uses a 0.300-second sentence gap and a 0.800-second chapter boundary composed of the existing 0.500-second ending and 0.300-second next opening. Spoken PCM, voice, typography and eight exact one-second quiz holds retain their approved identities. Eleven named scenes use standalone semantic figures; remaining scene layouts are retained.

```bash
python -m ceh_video --project "$CEH_PROJECT" qa --scope representative --precheck
python -m ceh_video --project "$CEH_PROJECT" qa --scope changed
python -m ceh_video --project "$CEH_PROJECT" run --intent iteration --run-kind routine
python -m ceh_video --project "$CEH_PROJECT" package --plan
python -m ceh_video --project "$CEH_PROJECT" run --intent release --run-kind delivery
python -m ceh_video --project "$CEH_PROJECT" report --run RUN_ID
# A retry preserves the failed attempt and links its origin:
python -m ceh_video --project "$CEH_PROJECT" run --intent iteration --run-kind retry --parent-run FAILED_RUN_ID
```

Iteration ends at checks and creates no archive. Scoped QA is feedback, not release acceptance. Reviewed goldens, complete QA and encoded review still gate release. Every attempt preserves events, logs, summed stage work, wall duration, queue waits and final single-job render tail under `qa/runs/RUN_ID/`. Packaging uses a manifest and direct ZIP stream, omits reproducible hosts, and independently checks extraction and zero-inference restoration.

`python -m ceh_video.benchmark PROJECT VARIANT SOURCE_DIRECTORY` runs three interleaved trials of three fixed 30-second visual workloads at 1×4, 2×2 and 2×4. Optional `--jobs N --workers N` pins the paired optimization comparison. Results apply to those excerpts and include validation overhead; they do not establish whole-film speedup. The command records decoded pictures and full-decode checks, and does not modify production configuration.

See [findings](../../docs/video-production/M10_PRODUCTION_PERFORMANCE_AUDIT.md) and [implementation/acceptance](../../docs/video-production/M10_EFFICIENCY_IMPLEMENTATION.md). Full new-film and ZIP validation remain pending; the completed evidence below belongs to v1.1.

## Preserved completed M10 v1.1 editorial remaster

Engine 0.4.0 implements the expanded 58-scene remaster with `design_profile: m10-editorial-remaster-v1.1` and project `design/tokens.json` version 1.2.0. It preserves approved typography, palette, Tally, Northstar, canonical teaching copy and the English v1.1 audio contract. All newly authored scenes enforce the 8% bottom safe area; the only legacy subtitle exception applies exclusively to frozen optimization-v1 S01–S58.

Current implementation includes measured SVG layouts, source-bound scene specifications, dynamic connector ports, absolute-time packet motion, complete capture inventories, and fail-closed visual gates. Full remaster browser acceptance passes: 558 golden states, 171 boundary states and 905 asset states, with a strict passing gate for all 58 scenes. The completed master passes full decode, codec/frame and continuous-audio checks. All 165 sampled encoded pictures pass artifact-bound agent review; packaging/extraction verification passed. The earlier 56 Python tests, five geometry tests and 86 snapshot results belong to the preserved engineering workspace, not this new film.

Active media/runtime: `/home/jnlngx10/Videos/CEH_M10_editorial_remaster_v1_1/project`. Expected complete duration: 132,727 video frames / 73:44.233. Follow [migration and production commands](../../docs/video-production/MIGRATION_AND_ROLLBACK.md) for source verification, root preparation, actual HyperFrames QA, reviewed goldens, chapter reviews, renders, master checks and packaging. The new `visual/remaster-qa.mjs` and `visual/remaster-boundaries.mjs` reports are mandatory for this profile. Golden snapshots are never updated by the test command.

`qa/remaster-delivery-readiness.json` verifies 330 source-file hashes, exact canonical scene/question payloads and the active calibration correction. Final archive verification passed. Full-master AAC measurements and human listening are distinct from earlier PCM and scene-level AAC checks. See the [current audit](../../docs/video-production/CURRENT_SYSTEM_AUDIT.md) for implemented versus pending work and the [exception register](../../docs/video-production/LAYOUT_AND_GEOMETRY_RULES.md) for exact scope.

## Run an existing project

Use the project's declared Python environment, Node lockfile, FFmpeg and Chromium. The editable archive bundles this package under `project/vendor/ceh_video`; the source repository keeps the maintained implementation here.

```bash
# From an extracted engine_project_source/project/ directory on the pinned host:
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
npm ci
npm ci --prefix vendor/ceh_video/visual --ignore-scripts
export PYTHONPATH="$PWD/vendor"
export CEH_VIDEO_PROJECT="$PWD"
# Remaster only: restore verified cache; performs no inference or tempo processing.
.venv/bin/python -c 'from ceh_video.common import Project, project_root; from ceh_video.delivery import restore_packaged_audio_cache; print(restore_packaged_audio_cache(Project(project_root())))'
.venv/bin/python -m ceh_video --project . preflight
.venv/bin/python -m ceh_video --project . plan --target package --explain
# Remaster: replay existing reviewed evidence before root; never auto-update goldens.
node vendor/ceh_video/visual/remaster-qa.mjs "$PWD"
node vendor/ceh_video/visual/remaster-boundaries.mjs "$PWD"
node vendor/ceh_video/visual/remaster-assets.mjs "$PWD"
.venv/bin/python -m ceh_video --project . run --target root --resume
# Inspect qa/Cxx-states and record actual findings for each chapter.
.venv/bin/python -m ceh_video --project . review --chapter C01 --findings 'Concrete inspected-frame findings'
.venv/bin/python -m ceh_video --project . run --target checks --resume
# Inspect the new encoded samples before recording their review.
.venv/bin/python -m ceh_video --project . review --encoded --findings 'Concrete inspected encoded-frame findings'
.venv/bin/python -m ceh_video --project . run --target package --resume
```

The setup block targets the full-remaster archive, Python 3.12 and the pinned Linux aarch64 runtime. `PYTHONPATH` points at `vendor`, whose child `ceh_video` is the import package; pip installs runtime dependencies from `requirements-lock.txt`. Archives exclude `.venv`, `node_modules` and caches. Provision the exact browser/FFmpeg/model paths declared by `production.json`. The hardware renderer is pinned to NVIDIA GB10; a different host needs explicit compatibility validation and new source-bound visual evidence, with no automatic backend fallback. Other profiles retain their own dependency inventory and initialization route. Model files, local fonts, approved assets, raw and processed speech, alignment, module adapters and pronunciation policy travel with the editable project. Rebuilding one chapter needs the rendering dependencies; generating new speech also needs Kokoro and alignment dependencies.

For an extracted remaster, run the explicit restoration command before cache-dependent work and before editing canonical copy or pronunciation. It checks `provenance/audio-restore.json`, all bundled media/metadata hashes and current recipes, then restores the operational cache with zero new inference or tempo passes. The `root` target does not perform this restoration for `ceh-en-v1.1`. Matching alignments remain hash-validated by the normal graph. The packaged reconstruction smoke test uses this same helper; a complete render on a relocated host remains a separate check. Subsequent edits follow normal dependency invalidation. For first authoring without reviewed goldens, use the build → precheck → candidate → review → regression → boundaries/assets → root order in the migration guide.

From this repository, use `PYTHONPATH=tools/ceh_video` and an explicit `--project /absolute/project`. `status` reports recorded stage outcomes. Progress goes to stderr; stdout contains final JSON. `--plain` suppresses interactive styling. Failures preserve the actual nonzero child exit code, and interruption terminates the child process group. Quiet-process heartbeats explicitly report unknown progress.

## Production profile and extension points

`production.json` declares the module/release, filenames, expected content counts, voice/output contracts, immutable asset identities, speech and alignment model hashes, renderer identity, browser path, diagram input files and concurrency. `metadata_title` can preserve an established exported title; otherwise the assembler uses the profile title. `data/scenes.json` and `data/questions.json` supply the chapter and quiz mappings. Shared code does not select quiz scenes by a numeric scene range.

The approved defaults remain 1920×1080/30 fps, warm paper editorial design, Tally, Northstar, `af_heart` American English, calibrated baseline speed 0.73 and exactly one `atempo=1.4` spoken-only narration transformation. Opening, sentence gap and ending are exactly 14,400, 9,600 and 24,000 stereo frames at 48 kHz. Historical v1.0 profiles explicitly retain their original policy for reconstruction. Picture runs at 1×. Each quiz hold contains exactly 48,000 stereo zero PCM frames. AAC residue has a separate decoded-audio check.

Module adapters live in `scripts/scene_art*.py` and `scripts/cues_*.json`. They return native editable art and narration-anchored moves. Generic compilation, chapter preparation, checks, rendering and assembly live in `ceh_video/runtime`. Thin script wrappers keep existing project commands usable. `extract_reference.py` documents the initial M10 extraction; rerunning it would replace subsequently maintained runtime code and is a migration operation, not a normal build command.

## Dependency and cache contract

```text
speech:Sxx → align:Sxx → scene:Sxx → prepare:Cxx → render:Cxx
                                  prepare:* → root
render:* + root → master
speech:* + align:* → audio-review
master + audio-review → checks → delivery → package
```

Each receipt binds declared inputs, relevant implementation files, dependency identities and verified output hashes. A changed/missing output schedules work again. Speech recipes use canonical text, resolved spoken text, voice, model and processing settings. A policy edit affects only sentences whose spoken form changes; moving a sentence can reuse the same content-keyed clip. Invalid entries regenerate through the actual model path. Stage receipts use atomic writes and locks. Maximum chapter concurrency is two. Each renderer consumes the validated `runtime.render_workers` setting (one through four); select the production setting using measured equal-workload checks.

Chapter fingerprints include declared composition HTML/motion, assets, encoding and renderer. Preview caches are excluded; exact editor-added `data-hf-id` attributes are normalized. Changes to actual authored content remain significant. Adapter files and cue files are declared conservatively at file granularity, so changing a shared adapter may recompile several scenes. An art-only change leaves speech recipes unchanged.

`--force NODE` explicitly executes that node and its downstream dependencies. `--resume` uses the same hash verification as ordinary execution; it never treats file existence as proof of completion. A fresh receipt is written only after the stage's required outputs exist. Source-bound native review is required even when a chapter encode can be reused. Final delivery also requires review bound to the actual master and encoded samples.

The current remaster's one-clip ASR availability receipt is `LIVE_MINIMUM_COMPLETED`; full-film transcription is unexecuted, and accuracy/timing are `not_evaluated`. Technical triage checks 781 clips with zero defects; 161 alignment flags across 142 clips and 478 queued listening items remain pending human review. See [audio review scope and receipts](../../docs/video-production/AUDIO_TIMING_POLICY.md#current-technical-review-and-listening-boundary).

## Audio review and repairs

`pronunciation.json` separates canonical copy from the spoken expansions. `review --audio` builds a context-linked local audition queue. Alignment flags, quantities, technical terms, quiz text and claim boundaries are review leads. PCM/hash/recipe checks establish technical integrity; flags alone do not establish pronunciation errors.

Listening dispositions persist by canonical text and audio identity. Use `review --item ID --disposition confirmed_listening_defect --reviewer human --evidence 'Timecode and finding'` only with actual human listening evidence. Automated decisions cannot clear listening acceptance. Edit a confirmed pronunciation expansion, inspect the resulting `plan`, regenerate the affected sentence, then let alignment, captions, diagrams, chapter/master and delivery checks follow the graph. Keep the previous release and diagnosis evidence.

## Validation and troubleshooting

Run `PYTHONPATH=tools/ceh_video python3 -m unittest discover -s tools/ceh_video/tests -v` from the repository. `tests/live_m10.py` explicitly runs real fixture TTS/cache/diagram checks; `tests/live_preflight.py` exercises actual diagram and quiz failures. `tests/live_relocation.py` checks first-run imports with the original workspace unavailable. These scripts use separate fixture directories and preserve earlier attempts. Their evidence establishes the exercised engineering behavior; it does not replace human listening or final encoded review.

Preflight checks canonical coverage, scene/question/hold mappings, AST syntax, approved asset/model identities, real diagram construction, narration anchors, local fonts and quiz geometry before model or encode work. Browser checks, repeated seeks, native semantic captures, full master decode, codec/frame/chapter counts, captions, quiz boundaries and audio continuity run at later stages. Packaging checks ZIP CRC, extracts the archive and verifies every payload hash.

If a review is stale, recapture current states and inspect them before replacing its receipt. If installed HyperFrames differs from the profile, reconcile `package.json`, lockfile, installed package and profile together, then recheck. Inspect the stage log named in the error for child failures; detailed renderer events are in `qa/Cxx-render.log`. Quiet-child heartbeats report liveness, with progress unknown. An existing closed package is preserved: use a new release workspace for changed deliverables. Old Markdown review notes and historical QA remain provenance; the structured current receipts govern this engine.

The [M10 optimization record](../../docs/video-production/M10_ENGINE_OPTIMIZATION.md) owns the exercised rollout, limitations and artifact locators. The engine has been migrated on M10; M04–M09 adoption requires explicit module migration and its own checks. Existing module releases remain preserved.

## Taiwan Mandarin profile (schema 2)

Schema 1 retains the approved CEH English contract. Schema 2 adds an explicit `content.locale=zh-TW`, `narration_key=narration_zh_TW`, a versioned online Taiwan-Mandarin voice, local CJK fonts and provider word-boundary timing. Its first course adapter is *小公司的數位日常*. The course owns its source and curriculum in the sibling coursework workspace; CEH owns the reusable implementation here.

The Mandarin profile uses `edge-tts==7.3.1`, `zh-TW-HsiaoChenNeural`, baseline `+0%` and exactly one `atempo=1.5` transformation. Original provider audio, decoded baseline, processed PCM, canonical/spoken copy, boundary events and hash receipts remain distinct. Unicode normalization retains Han characters; ASCII token edges allow pronunciation expansion next to Chinese text. A provider metadata mismatch stops the stage. Timing metadata establishes alignment coverage, while human pronunciation acceptance remains pending until actual listening.

The v2 graph reuses the common planner, child-process lifecycle, locks, output fingerprints and artifact-bound review guards. Speech and artwork are separate dependencies. New diagrams use editable geometry shared by SVG, HTML animation and native PowerPoint shapes. Captions preserve canonical punctuation and use measured CJK text width. Locale-v2 archives include the verified speech cache for offline reuse; fresh or changed narration requires the declared online provider. English v1 archives keep their original import behavior and package layout.

In an extracted schema-2 project, set `PYTHONPATH="$PWD/vendor/ceh_video"` (the schema-1 example above uses its original vendor layout). Recreate Python from `requirements.lock` and Node from `package-lock.json`, and set the local Chromium path. Run the same CLI against the v2 `production.json`: `preflight`, `run --target root`, native review, `run --target checks`, encoded review and `run --target package`. The first implementation adds fifteen Mandarin regression cases to the existing thirty-five engine cases. Live film evidence and any remaining limitations belong to the course's own validation packet, linked from the [production index](../../docs/video-production/README.md).

## English v1.1 engineering migration (engine 0.3.0)

The historical v1.1 migration contract is [PRODUCTION_STANDARD_v1.1](../../docs/video-production/PRODUCTION_STANDARD_v1.1.md): approved Kokoro 0.73 baseline, one spoken-only atempo=1.4, exact 0.3/0.2/0.5-second buffers and eight one-second quiz holds. `init` and `migrate` default to the current v1.2 verified-baseline migration. Use `--audio-policy ceh-en-v1.1` for the earlier migration contract; `init --legacy` is reserved for v1.0 reconstruction. Mandarin keeps its independent profile.

Use [migration commands](../../docs/video-production/MIGRATION_AND_ROLLBACK.md) for `migrate` and `engineering --stage audio|verify-audio|align|build|aac-audit|render-representatives`. They operate in a new workspace and do not render the full master or package a release. `tools/ceh_video/ci/verify-motion.sh` runs the bounded acceptance suite with `CEH_PROJECT` and `CEH_PY` supplied. Installed media/model/runtime dependencies are required; this repository alone is not a complete render package.

The new layout enforces an 8% bottom margin. `LEGACY-M10-SUBTITLE-001` applies only to frozen M10 optimization-v1 S01–S58. New scenes have no inherited exceptions. See the [audit and actual evidence](../../docs/video-production/CURRENT_SYSTEM_AUDIT.md) before treating any stage as accepted.

Completed M10 delivery: [master MP4](/home/jnlngx10/Videos/CEH_M10_editorial_remaster_v1_1/output/CEH_M10_Denial_of_Service_en-US_Editorial_Remaster_v1_1_1_4x_1s_master.mp4) — 207,412,180 bytes, SHA-256 `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`; [editable ZIP](/home/jnlngx10/Videos/CEH_M10_editorial_remaster_v1_1/output/CEH_M10_editorial_remaster_v1_1_EDITABLE.zip) — 3,707,042,054 bytes, SHA-256 `4f5d3e5a2a82672466cd0830fc02a16a39a14d571810aef13f1bca9976b7264e`. The [final external closeout](/home/jnlngx10/Videos/CEH_M10_editorial_remaster_v1_1/qa/final-delivery-closeout.json) binds verification receipts. All 165 encoded pictures remained unchanged after revalidation; CRC, extracted hashes and 781-clip cache restoration pass. Human viewing/listening remains pending.

### Scoped retries (engine 0.5.2)

For English v1.2, successful new chapter encodes retain hash-bound local receipts
in `.production/encoded-chapters`. Current visual, preparation and review gates
still run before reuse. Runtime/source/output changes and explicit force require
rendering; old releases do not automatically seed this cache. No media is copied.

`checks:frames`, `checks:audio`, and `checks:late` have independent receipts and
stage timings. `checks` remains the delivery gate and includes audio review.
Changing one QA implementation reruns that part; changing the master reruns all.
Inspection PNGs and contact sheets are verified outputs, so missing or modified
images invalidate the owning check. This reduces retry work; full-film first-run
speedup has not been measured. See the second round in
[the performance report](../../docs/video-production/M10_HIGH_IMPACT_FIXES.md).

### Master reuse and material QA inputs (engine 0.5.3)

English v1.2 assembly retains `.production/master-reuse.json` after successful
mux, full decode, metadata verification and PCM retention. The receipt binds
actual chapter MP4s, scene WAVs, timing/profile, FFmpeg and implementation to
all master outputs and scan evidence. A repeat with identical inputs validates
those hashes and the current decode receipt without rewriting the movie or PCM.
Current upstream gates remain required; explicit `--force master` bypasses reuse.
Old releases are not automatically imported into the cache.

Encoded QA keys retain master output identities and declared consumed files,
including the timing ledger, relevant chapter MP4s, font, PCM and scene audio
annotations. An upstream execution-key change alone no longer repeats QA.
Missing/changed inputs or outputs, validator changes and failed upstream receipts
still invalidate reuse. Planning stays conservative until upstream work finishes.
See the third round in [the performance report](../../docs/video-production/M10_HIGH_IMPACT_FIXES.md)
for real excerpt measurements, rejected capture tuning and full-film limits.

## Long-film storage maintenance — 0.5.5, October 22, 2026

[Storage and production standard v1.0.0](../../docs/video-production/LONGFORM_STORAGE_STANDARD_v1.0.0.md) governs new CEH, Mandarin concept and MATLAB practice-film releases. It records dates, ownership, retention, version metadata, failure recovery and unchanged quality gates.

English packaging cleans its own partial ZIP on handled failure. Mandarin packaging references engine sources directly, checks scratch capacity, verifies a temporary extraction and promotes the archive only after all payload hashes pass. Practice-film packaging checks six video hashes and streams CRC/SHA verification without an extracted media tree. Closed releases remain immutable; use a new release workspace. The Mandarin module split conservatively invalidates checks referencing the old shared delivery module once; inspect the plan before migration.

Run the read-only inventory from the repository root:

```bash
PYTHONPATH=tools/ceh_video python3 -m ceh_video.storage --plain "$CEH_WORKSPACE"
```

The argument is the release directory containing `project`, `output` and `qa`. JSON goes to stdout and progress to stderr. Categories identify review candidates, not reclaimable bytes or deletion approval. No historical cleanup command is provided. See the [validation receipt](../../docs/video-production/evidence/longform-storage-validation-2026-10-22.json) for engineering test scope; no existing full film was rendered or repackaged for this maintenance update.

### Compact delivery and Mandarin reuse — 0.6.0, 2026-10-22

New English migrations select `"package_format": "compact-v1"` in `production.json`. Set the same field when creating a new Mandarin or practice release workspace. Profiles without the field keep their legacy package format; use a new workspace for a revised release.

Compact delivery writes a ZIP, its `.sha256` sidecar and `RESTORE.py`. Restore offline using Python's standard library:

```bash
python3 RESTORE.py --archive PACKAGE.zip --destination NEW_DIRECTORY
```

The destination must not exist. Restoration validates every original path, length, CRC and SHA-256 before promotion, preserves regular permissions, and creates independent files. Duplicate payloads share one ZIP object. New English compact packages include chapter hosts and combined PCM for direct restoration; the package gate also runs the existing zero-inference reconstruction checks. Runtime environments remain outside the archive.

Mandarin chapter and master reuse now bind actual sources, runtime, implementation and output hashes. Current visual gates still run. PCM concatenation and identical host assets avoid unnecessary rewrites; valid full-decode receipts avoid a second video decode in Mandarin QA. Actual audio, quiz and frame checks remain required. `--force` bypasses the selected stage's reuse, and failed attempts cannot retain its success receipt.

See the [v2 standard](../../docs/video-production/LONGFORM_STORAGE_STANDARD_v2.0.0.md) and [measured execution record](../../docs/video-production/evidence/longform-round2-2026-10-22/README.md). Historical ZIPs and unique evidence are preserved; cleanup uses a separately audited fixed allowlist.
