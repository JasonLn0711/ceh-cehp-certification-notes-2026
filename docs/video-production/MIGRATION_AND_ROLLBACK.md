# Engine 0.5.2 scoped-retry maintenance

[Second-round evidence and rollback](M10_HIGH_IMPACT_FIXES.md) covers `.production/encoded-chapters` and independent `checks:frames`, `checks:audio`, `checks:late` nodes. Apply in a new workspace. Existing archives retain their own engines; old generic render receipts do not seed the new cache. Current QA/review gates and exact source/runtime/output hashes govern reuse. Revert graph and runner routing together to restore sequential checks; keep all validation gates. Full native cold/warm retry timing remains pending.

# Engine 0.5.1 maintenance

See [the two targeted fixes and evidence](M10_HIGH_IMPACT_FIXES.md). Apply maintenance in a new owned workspace; preserve the completed v1.2 MP4, ZIP and receipts. Existing `.production/master-audio` cache is optional and local; a miss uses original continuous AAC encoding. Packaging does not require this derived cache. Reuse depends on exact PCM and encoder identity, not a release filename.

Rollback assembly, checks, delivery and graph together to the preserved 0.5.0 implementation; restore the original two-pass decode contract. Do not disable validation in isolation. Historical archives retain their bundled engine. The performance validation workspace is intentionally a partial remux harness, not a complete media/model/runtime project for subsequent production.

# v1.2 implementation addendum

v1.2 operates only in the new efficiency workspace. Existing runtime is reused; media/source copies are independently owned. Manifest-first ZIP omits reproducible hosts and combined host PCM; restore rebuilds them without inference. Previous workspaces, codecs, fonts and release hashes remain immutable.

Status: complete local v1.2 delivery verified; see [v1.2 standard](PRODUCTION_STANDARD_v1.2.md) and [execution evidence](M10_EFFICIENCY_IMPLEMENTATION.md). Historical evidence below applies only to its named release.

# Migration and rollback

## Full-remaster workspace and execution

The active workspace is `/home/jnlngx10/Videos/CEH_M10_editorial_remaster_v1_1`; engine 0.4.0 selects `m10-editorial-remaster-v1.1` and project tokens 1.2.0. The original source-package inputs are copied and verified: `qa/remaster-delivery-readiness.json` records 330 matching file hashes, exact canonical payload equality and the active af_heart / 0.73 / once-1.4× calibration. Final packaged payload verification passed. The earlier engineering workspace and both archived releases remain unchanged. The pre-remaster engine snapshot is retained at the new workspace's `qa/pre-remaster-engine.tar.gz`.

Status: workspace preparation and full-scene implementation are **implemented and tested**. The 558-state golden regression, 171 boundary states, 905 asset states and all-58-scene strict visual gate pass. Actual full-production checks completed with exit 0 (`qa/run-checks.json`, `qa/full-production-run.log`): all eleven chapters and the master pass codec/frame/GPU, full decode and audio continuity. Editable ZIP verification has **passed**. Measured full duration is 132,727 video frames / 212,363,200 stereo audio frames / 73:44.233. Publication remains outside the local-production request.

Run from the repository with the prepared project and its installed runtime:

```bash
export CEH_PROJECT=/home/jnlngx10/Videos/CEH_M10_editorial_remaster_v1_1/project
export CEH_PY="$CEH_PROJECT/.venv/bin/python"
export PYTHONPATH=tools/ceh_video
"$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain preflight
"$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain engineering --stage verify-audio
"$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain plan --target package --explain
"$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain engineering --stage build
node tools/ceh_video/ceh_video/visual/remaster-qa.mjs "$CEH_PROJECT" --precheck
node tools/ceh_video/ceh_video/visual/remaster-qa.mjs "$CEH_PROJECT"
```

The first QA run can produce `candidate_baseline_review_required`. Inspect the complete candidate inventory and differences, record source/environment/image-bound review, and install the approved baseline separately. QA commands never promote candidates automatically. Preserve failed reports and diffs. Then run regression against the reviewed read-only baseline, nested boundary and asset checks before the root target, which requires all three passing reports:

```bash
node tools/ceh_video/ceh_video/visual/remaster-qa.mjs "$CEH_PROJECT"
node tools/ceh_video/ceh_video/visual/remaster-boundaries.mjs "$CEH_PROJECT"
node tools/ceh_video/ceh_video/visual/remaster-assets.mjs "$CEH_PROJECT"
node tools/ceh_video/ceh_video/visual/quiz-divider-negative.mjs "$CEH_PROJECT"
"$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain run --target root --resume
```

Inspect each chapter's prepared states before issuing its review command; repeat for C01 through C11 with actual chapter-specific findings:

```bash
"$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain review --chapter C01 --findings 'Actual inspected-frame findings'
"$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain run --target render:C01 --resume
"$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain run --target checks --resume
```

The `checks` target renders remaining chapters only after their reviews and the complete visual gate pass, then assembles and checks the master. Inspect actual encoded samples and preserve any listening limitations before final packaging:

```bash
"$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain review --encoded --findings 'Actual inspected encoded-frame findings'
"$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain run --target package --resume
```

Packaging excludes the reproducible `qa/remaster-boundaries/hosts/` directory: its temporary host projects link to the project media and would duplicate those assets when dereferenced. The archive retains the boundary report and all 171 captured PNGs; `project/vendor/ceh_video/visual/remaster-boundaries.mjs` regenerates hosts from the included project. `qa/archive-exclusions.json` records this narrow exclusion. A tested copy preserves all screenshot/report hashes in 10,614,019 bytes. The first expanded-host attempt and inventory remain in `qa/package-attempt-001-expanded-hosts.*`; no rendering source or validation requirement changed.

Archive acceptance is recorded in the adjacent `qa/engine-packaging.json` only after CRC, extraction, payload-hash verification and cache restoration complete. It has passed in the final external receipt. Project documents freeze when packaging starts; the external final receipt is authoritative for archive completion and ZIP SHA-256, avoiding a circular repack to embed the archive’s own hash.

Expected artifacts are the profile-named master MP4, eleven `output/chapters/Cxx.mp4` files, lossless PCM, SRT/VTT, chapter metadata, editable ZIP and QA manifests. A started command or prepared scaffold is not completion evidence. Require decode/frame checks, final-master AAC boundary measurement, protected/source hashes, archive CRC, extracted payload hashes and packaged reconstruction before technical closeout. Human listening findings must be recorded as actual human evidence.

Rollback selects the prior workspace and its matching engine/runtime. Restore reviewed source changes from `qa/pre-remaster-engine.tar.gz` only after checking the archive and preserving unrelated changes; do not extract it over a live workspace blindly. Retain current media, failed attempts and logs. Recheck historical master/ZIP and locked-asset hashes. Never overwrite frozen releases or relabel their 1.5× media.


Actual master checkpoint: `CEH_M10_Denial_of_Service_en-US_Editorial_Remaster_v1_1_1_4x_1s_master.mp4` is 1920×1080 at 30 FPS, 132,727 frames / 73:44.233. SHA-256: `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`. `qa/run-checks.json` is verified; full decoding found zero black intervals, and all 212,363,200 reference audio frames passed continuity comparison. All 165 encoded sample pictures passed artifact-bound agent review: `qa/encoded-review-coverage.json` binds the three inspection receipts and `qa/encoded-review.json` records the actual CLI review against the current master and all 165 hashes. ZIP extraction verification passed. Human viewing/listening remains pending.

### Historical bounded migration procedure

The commands and scope exclusions below describe the earlier engine 0.3.0 engineering slice. The active full-remaster procedure above supersedes its delivery scope; it does not alter historical evidence.

Status: **implemented** isolated migration and scoped engineering commands; **tested** with the maintained M10 reference. Full-film publication is outside this run.

Canonical implementation: this repository, `tools/ceh_video`. Historical evidence remains in `docs/video-production/M10_ENGINE_OPTIMIZATION.md` and immutable local M10 releases. New media and raw QA live at `/home/jnlngx10/Videos/CEH_M10_motion_v1_1`; compact evidence is under `docs/video-production/evidence/motion-v1.1`. The supplied technical-document snapshot is a reference, not a complete runtime. Planning needs only a locator/status mirror if separately requested; raw rendering and model evidence belong here.

## Reproduce the scoped migration

```bash
export CEH_PROJECT=/home/jnlngx10/Videos/CEH_M10_motion_v1_1/project
export CEH_PY="$CEH_PROJECT/.venv/bin/python"
# Run once, with a destination that does not exist:
PYTHONPATH=tools/ceh_video /home/jnlngx10/Videos/CEH_M10_optimization_v1/project/.venv/bin/python -m ceh_video --plain migrate \
  --reference /home/jnlngx10/Videos/CEH_M10_optimization_v1 \
  --workspace /home/jnlngx10/Videos/CEH_M10_motion_v1_1
PYTHONPATH=tools/ceh_video "$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain engineering --stage audio
PYTHONPATH=tools/ceh_video "$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain engineering --stage align
PYTHONPATH=tools/ceh_video "$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain engineering --stage build
PYTHONPATH=tools/ceh_video "$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain engineering --stage aac-audit
# After reviewed screenshot regressions and HyperFrames scene checks pass:
PYTHONPATH=tools/ceh_video "$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain engineering --stage render-representatives
```

Migration copies owned assets/runtime files, preserves relative node-package executable symlinks, imports verified raw PCM, removes stale alignment and timing metadata, assigns new filenames and writes a provenance report. Copies are not writable hardlinks into the old release. Source teaching content and its original metadata remain historical source evidence; the active policy addendum and production profile select v1.1.

The migration is deliberately an engineering workspace, not a delivery archive reconstruction: source-package input ZIP custody and old chapter MP4s are not copied. Full delivery needs its own source-package import and review gates. No old speech/align/render receipt is silently recertified. If a new destination is partially created, inspect `qa/migration.json` and its stage outputs before choosing a fresh destination; migration never merges over an existing directory.

Audio reruns reuse validated 1.4× processed cache entries. Alignment reruns reuse only matching new audio hashes/canonical text/recipe. The active main alignment pass can coexist with bounded later-scene passes only when their file ranges do not overlap in flight; all later cache reuse is hash checked. Keep process logs and do not count started work as completed.

## Rollback

1. Stop only processes owned by the new workspace and retain failure logs.
2. Point production back to the frozen `CEH_M10_optimization_v1` workspace and its original pinned engine/runtime. Do not relabel v1.1 PCM as v1.0.
3. Retain the new workspace and evidence for diagnosis; delete it only through a separate explicit cleanup decision.
4. Restore code changes by their reviewed diff/version, preserving unrelated work. No commit, push, old-delivery overwrite or automatic deletion is part of this task.
5. Compare protected asset hashes and historical delivery hashes with their recorded values. A hash mismatch blocks release.

The original v1.0 standard, archived tests and master/ZIP records remain unchanged. Engine 0.3.0 supports explicit legacy profiles for reproducibility; the new English profile uses v1.1. Mandarin schema 2 remains independent. New dependencies are pinned in the engineering lockfile with their license files in installed packages. Native Linux aarch64 execution is supported by observed results; Docker daemon access, remote CI and hardware-GPU rendering are separate environment gates.

Final local delivery: the master is 207,412,180 bytes, SHA-256 `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`; `CEH_M10_editorial_remaster_v1_1_EDITABLE.zip` is 3,707,042,054 bytes, SHA-256 `4f5d3e5a2a82672466cd0830fc02a16a39a14d571810aef13f1bca9976b7264e`. `qa/engine-packaging.json` verifies ZIP CRC, extraction, 8,369 files and 8,368 payload hashes, including 165 encoded pictures and the cited golden-review receipts. `qa/engine-extracted-reconstruction.json` confirms 781 restored clips with zero inference and zero tempo passes. `qa/encoded-review-revalidation.json` confirms the same master and all 165 reviewed picture hashes after the conservative check rerun.

Project documents inside the ZIP retain their honest packaging-time checkpoint. These final repository records and the external receipts establish completed archive acceptance; the frozen project, staging tree and ZIP were not rewritten. Human listening remains pending for 478 items; the one-clip ASR run establishes minimum availability only, with full-film accuracy/timing `not_evaluated`.
