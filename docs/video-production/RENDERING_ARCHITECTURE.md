# v1.2 implementation addendum

v1.2 retains HTML/CSS/SVG+GSAP+HyperFrames. Longest-first ready chapter scheduling preserves output order. Runtime and worker optimizations require paired measured comparisons; prior1vs2-worker excerpt results do not prove superiority over4.

Status: implemented changes under validation; see [v1.2 standard](PRODUCTION_STANDARD_v1.2.md) and [execution evidence](M10_EFFICIENCY_IMPLEMENTATION.md). Historical evidence below applies only to its named release.

# Rendering architecture and decision

## Full-film production architecture

The full remaster uses HTML/CSS text, SVG components and connectors, finite paused GSAP timelines, and HyperFrames composition/rendering. PixiJS remains a bounded comparison fixture; it is not added to the production scene dependency path. Three.js has no activated use case.

Status: source-bound scene specifications, token-driven compiler and deterministic runtime are **implemented and tested**. Full-scene regression (558 states), boundary QA (171 states), asset QA (905 states), eleven native chapter reviews and the paired worker benchmark described below have passed. Full-film encoding and technical checks are **complete**. All eleven chapters pass codec/frame/GPU verification; the complete master passes full decode and audio continuity. The worker benchmark remains an excerpt-specific comparison, and all 165 sampled encoded pictures pass artifact-bound agent review. `Frame(t)` derives from the model and absolute time; path movement does not accumulate prior-frame state. Runtime completion must occur before HyperFrames capture.

`graph.py:16` includes compiler, specification, runtime, geometry and selected project-token hashes in visual recipe identities. Derived layout files are outputs, avoiding a self-invalidating recipe cycle. Speech and alignment keys remain independent of visual-only changes. Chapter rendering reads `runtime.render_workers` through `runtime/chapter.py:8`; measured comparisons must select production concurrency rather than a guessed performance claim.

Preserve the tested pins listed below. The Playwright fixture and screenshot environment reports ANGLE/SwiftShader; a separate probe with the exact QA launch flags confirms this. Native HyperFrames reports `ANGLE (NVIDIA Corporation, NVIDIA GB10/PCIe, OpenGL ES 3.2)`. The production profile now pins hardware mode and that exact renderer. Each chapter render must preserve and validate the actual probe output; the mode label alone is insufficient. These environments retain separate evidence, and no SVG/Pixi performance winner is claimed.

Two paired concurrent tests rendered the same ten-second S44 excerpt with two jobs. On the final source, one worker per job took 64.576 and 59.018 seconds; two workers per job took 46.949 and 46.023 seconds. All eight 300-frame outputs were byte-identical and passed full decoding. The selected production configuration is two concurrent chapter jobs with two workers each. This measured 28.24–37.55% throughput improvement applies to that workload under shared QA load; full-chapter scaling remains subject to the actual production run. Evidence: `qa/render-benchmark-concurrent-final/report.json` in the remaster workspace.


Actual master checkpoint: `CEH_M10_Denial_of_Service_en-US_Editorial_Remaster_v1_1_1_4x_1s_master.mp4` is 1920×1080 at 30 FPS, 132,727 frames / 73:44.233. SHA-256: `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`. `qa/run-checks.json` is verified; full decoding found zero black intervals, and all 212,363,200 reference audio frames passed continuity comparison. All 165 encoded sample pictures passed artifact-bound agent review: `qa/encoded-review-coverage.json` binds the three inspection receipts and `qa/encoded-review.json` records the actual CLI review against the current master and all 165 hashes. ZIP extraction verification passed. Human viewing/listening remains pending.

### Historical technical selection and fixture evidence

The bounded comparison below remains the reason for retaining the simpler production stack. It does not certify the new full film.

Decision: **A — strengthen HTML/CSS/SVG + GSAP**. B remains a bounded engineering comparison. Status: A **implemented**, SVG/Pixi compatibility **tested** locally; broader particle stress/performance selection **proposed**.

| Criterion | A: existing stack strengthened | B: selective PixiJS |
|---|---|---|
| Fidelity | Keeps editable vector artwork, paper palette and local fonts | Same DOM/SVG typography; packet layer can match palette |
| Determinism | Existing paused GSAP timelines; explicit seek | Requires stopped tickers, absolute state and completion barrier |
| Cost | Small adapters and geometry checks | Extra GPU lifecycle, adapter and dependency maintenance |
| Performance | No speed claim; sufficient for the bounded scene | Local compatibility established; no general speed claim |
| Maintainability | Existing engine and asset ownership | More renderer-specific failure modes |
| Testability | DOM/SVG boxes plus pixels | Explicit geometry model plus backend-specific pixels |
| Migration risk | Small | WebGL/fallback and renderer differences |
| Reuse | Cards, ports, text metrics, policy shared | Useful only if a real packet/particle workload warrants it |

| Scene responsibility | Selected technology |
|---|---|
| Teaching text, cards, UI | HTML/CSS, Flexbox/Grid |
| Arrows, topology, vector characters | SVG |
| Finite transitions/timelines | GSAP 3.14.2 |
| High-volume packet/particle effects | PixiJS candidate only, not production default |
| Spatial depth | Three.js deferred; no demonstrated need |
| Composition and output | installed HyperFrames 0.8.174 |

The six-second S23 fixture reuses its approved title and labels to isolate card translation, dynamic connections, a masked packet and text. It is explicitly an engineering fixture, not a replacement for the narrated scene. Original S17/S23 and the eight quiz scenes are tested separately after new timing compilation.

## Deterministic contract

`Frame(t) = Render(Scene, Assets, t)`. Finite paused GSAP timelines register under the exact composition ID. Pixi initializes before readiness, stops private/shared/system tickers, calculates state directly from t, renders explicitly, and registers its promise synchronously through `hf-seek.detail.waitUntil`. HyperFrames 0.8.174 exposes `__player.renderSeek(t,{exact:true})` and `__hfWaitForSeekCompletion`; tests await both the real runtime and font readiness. No production state depends on wall clocks, unseeded randomness or accumulated frame deltas.

The ordinary GSAP PixiPlugin API is documented by [GSAP](https://gsap.com/docs/v3/Plugins/PixiPlugin/); Pixi's [ticker documentation](https://pixijs.com/8.x/guides/components/application/ticker-plugin) explains ticker ownership. This integration uses the installed HyperFrames generic seek event; it does not claim an official dedicated Pixi adapter.

## Local compatibility

Pinned test dependencies: PixiJS 8.22.0, GSAP/PixiPlugin 3.14.2, Playwright 1.62.1, Chromium 151.0.7922.34 (revision 1234), HyperFrames 0.8.174. `visual/package-lock.json` pins transitive packages. Playwright 1.62.1 was selected to match the approved installed browser. Runtime: Linux aarch64, Ubuntu 24.04; WebGL2 via ANGLE/SwiftShader software rendering. The HyperFrames render log labels its auto capture mode “hardware gpu”; that label alone does not establish the physical adapter or performance. Hardware-GPU performance and a no-WebGL Pixi fallback remain **not tested**. SVG is the operational fallback; failure does not silently change backend within a golden comparison.

`qa/visual/fixtures/manifest.json` records actual runtime, source/token/dependency identities, pixels and measured seek round trips. Round trips include automation overhead and are not rendering-throughput rankings. PixiPlugin's paused x=100 tween reaches x=50 at t=.5 in the real browser. Backend goldens are separate because rasterization need not be byte-identical across SVG/WebGL.

New dependencies stay in the engineering package. Licenses: HyperFrames/Playwright Apache-2.0; PixiJS/pixelmatch/pngjs MIT; GSAP Standard License as supplied with 3.14.2. Local font and protected asset provenance remain in the source package. Remote CI, Docker and cross-platform results are not inferred from this native run.

Final local delivery: the master is 207,412,180 bytes, SHA-256 `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`; `CEH_M10_editorial_remaster_v1_1_EDITABLE.zip` is 3,707,042,054 bytes, SHA-256 `4f5d3e5a2a82672466cd0830fc02a16a39a14d571810aef13f1bca9976b7264e`. `qa/engine-packaging.json` verifies ZIP CRC, extraction, 8,369 files and 8,368 payload hashes, including 165 encoded pictures and the cited golden-review receipts. `qa/engine-extracted-reconstruction.json` confirms 781 restored clips with zero inference and zero tempo passes. `qa/encoded-review-revalidation.json` confirms the same master and all 165 reviewed picture hashes after the conservative check rerun.

Project documents inside the ZIP retain their honest packaging-time checkpoint. These final repository records and the external receipts establish completed archive acceptance; the frozen project, staging tree and ZIP were not rewritten. Human listening remains pending for 478 items; the one-clip ASR run establishes minimum availability only, with full-film accuracy/timing `not_evaluated`.
