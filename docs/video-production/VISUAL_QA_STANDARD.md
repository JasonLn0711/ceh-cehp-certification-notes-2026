# v1.2 implementation addendum

v1.2 exposes changed/representative/full feedback scopes. Only full current-source evidence can clear release. Representative cases precede full candidate capture and artifact-bound golden review. Source changes invalidate actual consumers; no fail-to-pass auto baseline updates.

Status: implemented changes under validation; see [v1.2 standard](PRODUCTION_STANDARD_v1.2.md) and [execution evidence](M10_EFFICIENCY_IMPLEMENTATION.md). Historical evidence below applies only to its named release.

# Visual QA standard v1.1

## Complete-remaster release gate

Status: the full-film harness and strict integration gate are **implemented and tested**. Actual evidence: `qa/visual/scenes/manifest.json` and `qa/remaster-regression.log` record 558/558 passing golden comparisons; `qa/final-visual-gate.json` passes all 58 current-source scenes with zero exceptions. Boundary QA passes 171 states and asset QA passes 905 sampled states. The complete encoded master passes technical checks (`qa/run-checks.json`); ZIP verification passed. Historical 86-state evidence below belongs to the previous engineering release.

`visual/remaster-qa.mjs` uses actual HyperFrames seek/completion barriers and loaded fonts. It derives captures at start, 15%, midpoint, 85%, final frame, every narration-label window midpoint, and nine quiz boundary/hold states. The Python guard independently reproduces this inventory with JavaScript-compatible rounding; one passing sample cannot stand in for a complete scene.

Require all 58 scenes, every non-quiz frame's pure geometry, all 240 quiz-hold frames, every unique text layout, decoration-versus-text overlap checks, zero unexpected exceptions, current source/audio/cue/layout hashes, and pinned runtime/token/font/asset identities. The runtime path also requires a complete 171-state report from `visual/remaster-boundaries.mjs`, covering before/exact/after every one of 57 scene boundaries. Visible canonical headings prevent blank hydration from passing a pixel comparison.

Golden baselines are read-only during tests. Initial candidates require inspection and a recorded review with environment and image hashes before copying approved images into `qa/visual/scenes/golden`. Preserve earlier baselines and rejected diffs. Tests must not automatically update a failed baseline. Existing threshold 0.05 with antialias handling and zero unexplained pixels remains subject to a one-pixel displacement negative control; geometry uses 0.25 px tolerance.

The asset gate additionally requires `qa/remaster-assets/report.json`: current runtime/token/source hashes, original asset hashes and passing geometry for all 50 non-quiz scenes. The eight-scene `quiz-divider-negative.mjs` control injects a divider in disposable browser DOM and must detect its text overlap while leaving production HTML unchanged.

Commands and review order are in [MIGRATION_AND_ROLLBACK.md](MIGRATION_AND_ROLLBACK.md). Pure geometry and negative guard unit tests establish their own layer; production acceptance requires actual browser reports and final encoded-media checks. Remote CI and human full-film acceptance retain separate statuses.


Actual master checkpoint: `CEH_M10_Denial_of_Service_en-US_Editorial_Remaster_v1_1_1_4x_1s_master.mp4` is 1920×1080 at 30 FPS, 132,727 frames / 73:44.233. SHA-256: `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`. `qa/run-checks.json` is verified; full decoding found zero black intervals, and all 212,363,200 reference audio frames passed continuity comparison. All 165 encoded sample pictures passed artifact-bound agent review: `qa/encoded-review-coverage.json` binds the three inspection receipts and `qa/encoded-review.json` records the actual CLI review against the current master and all 165 hashes. ZIP extraction verification passed. Human viewing/listening remains pending.

### Historical bounded QA standard and evidence

Status: **implemented** geometry, screenshot, asset and seek harness; **tested** locally as recorded in the audit. A self-hosted ARM64 GitHub workflow is **implemented** at `.github/workflows/ceh-motion-qa.yml`; remote execution and branch-protection activation remain **blocked** on publication and runner configuration, which were not requested.

## Reproducible environment

Use HyperFrames 0.8.174, GSAP 3.14.2, Playwright 1.62.1, Chromium revision 1234 / 151.0.7922.34, 1920×1080, DPR 1, seed 0 and local font assets. Install engineering dependencies with `npm ci --prefix tools/ceh_video/ceh_video/visual --ignore-scripts`. The lockfile, font hashes, token hash and browser identity enter the evidence manifest. Backend changes require separate baselines. Playwright's [snapshot guidance](https://playwright.dev/docs/test-snapshots) explains why environment identity matters.

The harness loads the installed HyperFrames runtime, waits for `__renderReady`, calls `__player.renderSeek(t,{exact:true})`, then awaits `__hfWaitForSeekCompletion` and fonts. It never uses elapsed playback as a substitute for a seek barrier.

## Assertions

- Geometry: 0.25 px maximum anchor/boundary tolerance; safe areas; token radius/stroke; nonuniform icon distortion; minimum spacing; illegal sibling overlap; text overflow. Parent-child geometry and decorative structure have explicit roles.
- Assets: all locked files and approved font binaries must match hashes.
- Seek: direct t, forward through intermediate time, past t, back to zero, repeated t. Same-time screenshots must have zero changed non-antialiased pixels.
- Quiz boundaries: hold start/end and adjacent 30 FPS frames, midpoint, scene start/mid/end. Caption and answer opacity must be zero throughout the hold; answer timing is derived from integer sample metadata.
- Pixel regression: pixelmatch threshold .05, antialias-only differences excluded, zero other changed pixels. A real one-pixel card displacement is a required negative control. Numeric geometry remains independent of this raster threshold.
- Output: PNGs, pixel diffs, geometry arrays, seek differences, exceptions, source hashes and environment are retained with a machine report. A failed test never overwrites its golden.

## Commands and baseline review

```bash
npm test --prefix tools/ceh_video/ceh_video/visual
node tools/ceh_video/ceh_video/visual/representative.mjs "$CEH_PROJECT"
node tools/ceh_video/ceh_video/visual/qa.mjs "$CEH_PROJECT" fixtures
node tools/ceh_video/ceh_video/visual/qa.mjs "$CEH_PROJECT" scenes
```

Missing goldens yield `candidate_baseline_review_required`, not a regression pass. Review candidate images and geometric failures first; record reviewer, reason, source/environment identity and the exact accepted image hashes in a separate golden directory. A repeat invocation reads these files without modifying them. Golden changes require a new review record and before/after diffs; there is no automatic update-on-failure option.

The exhaustive bounds runner checks all 2,200 generated text boxes, including SVG labels. The nested C04 boundary runner checks S17→S18 at the adjacent frames and exact transition, then seeks past and backwards before repeating. Fixtures cover four times for each backend. Narrated scene coverage is S17, S23, and S50–S57 with all eight quiz boundaries. These bounded checks do not certify every unmeasured diagram primitive in S01–S58. `visual_gate.py` blocks a new scene's chapter render or delivery unless that scene has current source-bound passing geometry, screenshot and seek evidence with no exceptions. Missing coverage therefore remains a visible gate.

The CI entry script runs unit/geometry tests, verifies the pinned local browser and replays the representative golden comparisons. A self-hosted ARM64 runner must provide the approved local project, media and goldens. A public hosted runner cannot reconstruct those protected assets from this repository alone. Human listening and production activation are separate from automated acceptance.

## Full-remaster CI entry point

`tools/ceh_video/ci/verify-remaster.sh` runs both geometry suites, audio sample
verification, the full 58-scene screenshot/seek harness, nested boundary checks
and the fail-closed delivery guard. It requires an explicitly isolated
`CEH_PROJECT` workspace with reviewed goldens; it never updates goldens. The
workflow targets `CEH_M10_editorial_remaster_ci`, separate from the delivery
workspace. Remote runner provisioning and remote CI execution remain `blocked`
until that workspace and runner label exist; local command execution has its own
receipts.

Final local delivery: the master is 207,412,180 bytes, SHA-256 `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`; `CEH_M10_editorial_remaster_v1_1_EDITABLE.zip` is 3,707,042,054 bytes, SHA-256 `4f5d3e5a2a82672466cd0830fc02a16a39a14d571810aef13f1bca9976b7264e`. `qa/engine-packaging.json` verifies ZIP CRC, extraction, 8,369 files and 8,368 payload hashes, including 165 encoded pictures and the cited golden-review receipts. `qa/engine-extracted-reconstruction.json` confirms 781 restored clips with zero inference and zero tempo passes. `qa/encoded-review-revalidation.json` confirms the same master and all 165 reviewed picture hashes after the conservative check rerun.

Project documents inside the ZIP retain their honest packaging-time checkpoint. These final repository records and the external receipts establish completed archive acceptance; the frozen project, staging tree and ZIP were not rewritten. Human listening remains pending for 478 items; the one-clip ASR run establishes minimum availability only, with full-film accuracy/timing `not_evaluated`.


## v1.2 full-composition visual/audio partition

The production index and all 58 compositions remain unchanged. `root_check.py` creates a temporary visual QA host by removing audio elements only, retaining the original head, visual markup, slots, global offsets and GSAP timelines. Native HyperFrames checks every scene midpoint and all eight quiz-hold midpoints (66 times), including contrast, with strict zero warnings. The receipt binds every original/transformed source, runtime, configuration and implementation hash. Delivery rejects changed sources, missing samples, skipped browser checks or disabled contrast. Temporary hosts are excluded from the archive; source-transform and native receipts are included.

This extends the existing visual-only boundary-check approach; it does not claim full-host browser audio playback acceptance. The unchanged production host passed a separate real single-point check in 329.424 seconds. The original all-66-time check hit the native deadline. The visual-only all-66-time diagnostic passed in 98.327 seconds, with 59 contrast objects checked. These are diagnostic observations with different scopes, not a controlled speedup percentage. PCM sample validation, eight exact holds, full encoded-media decode and AAC continuity remain independent mandatory gates. The two earlier SIGTERM origins remain unknown; the traced deadline attempt received no SIGTERM.
