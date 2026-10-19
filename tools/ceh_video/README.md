# CEH video engine 0.2.0

Local production engine for the [CEH series standard](../../docs/video-production/PRODUCTION_STANDARD_v1.0.md). M10 is the reference migration. The engine owns execution, verified reuse, process receipts and review guards; each module owns its canonical script, native diagrams, quiz, evidence, assets and production profile. Full human listening remains a separate acceptance step.

## Run an existing project

Use the project's declared Python environment, Node lockfile, FFmpeg and Chromium. The editable archive bundles this package under `project/vendor/ceh_video`; the source repository keeps the maintained implementation here.

```bash
# From an extracted project/ directory:
export PYTHONPATH=vendor
.venv/bin/python -m ceh_video --project . preflight
.venv/bin/python -m ceh_video --project . plan --target package --explain
.venv/bin/python -m ceh_video --project . run --target root --resume
# Inspect qa/Cxx-states and record actual findings for each chapter.
.venv/bin/python -m ceh_video --project . review --chapter C01 --findings 'Concrete inspected-frame findings'
.venv/bin/python -m ceh_video --project . run --target checks --resume
# Inspect the new encoded samples before recording their review.
.venv/bin/python -m ceh_video --project . review --encoded --findings 'Concrete inspected encoded-frame findings'
.venv/bin/python -m ceh_video --project . run --target package --resume
```

The examples assume the local dependencies have been installed. Archives exclude `.venv`, `node_modules` and caches. Run `npm ci` and recreate Python using the included environment inventory before rendering; provision the browser path in `production.json`. Model files, local fonts, approved assets, raw and processed speech, alignment, module adapters and pronunciation policy travel with the editable project. Rebuilding one chapter needs the rendering dependencies; generating new speech also needs Kokoro and alignment dependencies.

On the first use of an extracted release, run the baseline `root` target before editing canonical copy or pronunciation. This verifies the shipped identity manifest and imports its approved clips/alignment without needing the original workspace. Subsequent edits follow normal dependency invalidation.

From this repository, use `PYTHONPATH=tools/ceh_video` and an explicit `--project /absolute/project`. `status` reports recorded stage outcomes. Progress goes to stderr; stdout contains final JSON. `--plain` suppresses interactive styling. Failures preserve the actual nonzero child exit code, and interruption terminates the child process group. Quiet-process heartbeats explicitly report unknown progress.

## Production profile and extension points

`production.json` declares the module/release, filenames, expected content counts, voice/output contracts, immutable asset identities, speech and alignment model hashes, renderer identity, browser path, diagram input files and concurrency. `metadata_title` can preserve an established exported title; otherwise the assembler uses the profile title. `data/scenes.json` and `data/questions.json` supply the chapter and quiz mappings. Shared code does not select quiz scenes by a numeric scene range.

The approved defaults remain 1920×1080/30 fps, warm paper editorial design, Tally, Northstar, `af_heart` American English, calibrated baseline speed 0.73 and exactly one `atempo=1.5` narration transformation. Picture runs at 1×. Each quiz hold contains exactly 48,000 stereo zero PCM frames. AAC residue has a separate decoded-audio check.

Module adapters live in `scripts/scene_art*.py` and `scripts/cues_*.json`. They return native editable art and narration-anchored moves. Generic compilation, chapter preparation, checks, rendering and assembly live in `ceh_video/runtime`. Thin script wrappers keep existing project commands usable. `extract_reference.py` documents the initial M10 extraction; rerunning it would replace subsequently maintained runtime code and is a migration operation, not a normal build command.

## Dependency and cache contract

```text
speech:Sxx → align:Sxx → scene:Sxx → prepare:Cxx → render:Cxx
                                  prepare:* → root
render:* + root → master
speech:* + align:* → audio-review
master + audio-review → checks → delivery → package
```

Each receipt binds declared inputs, relevant implementation files, dependency identities and verified output hashes. A changed/missing output schedules work again. Speech recipes use canonical text, resolved spoken text, voice, model and processing settings. A policy edit affects only sentences whose spoken form changes; moving a sentence can reuse the same content-keyed clip. Invalid entries regenerate through the actual model path. Stage receipts use atomic writes and locks. Maximum chapter concurrency is two, with four renderer workers each.

Chapter fingerprints include declared composition HTML/motion, assets, encoding and renderer. Preview caches are excluded; exact editor-added `data-hf-id` attributes are normalized. Changes to actual authored content remain significant. Adapter files and cue files are declared conservatively at file granularity, so changing a shared adapter may recompile several scenes. An art-only change leaves speech recipes unchanged.

`--force NODE` explicitly executes that node and its downstream dependencies. `--resume` uses the same hash verification as ordinary execution; it never treats file existence as proof of completion. A fresh receipt is written only after the stage's required outputs exist. Source-bound native review is required even when a chapter encode can be reused. Final delivery also requires review bound to the actual master and encoded samples.

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
