# v1.2 implementation addendum

v1.2 uses explicit data-component-bounds for card and standalone components. Invisible logical bounds reserve the whole figure/label group; they do not waive visible icon aspect/identity or text containment tests. All new scenes have zero exceptions.

Status: implemented changes under validation; see [v1.2 standard](PRODUCTION_STANDARD_v1.2.md) and [execution evidence](M10_EFFICIENCY_IMPLEMENTATION.md). Historical evidence below applies only to its named release.

# Layout and geometry rules

## Active production constraints

Status: full-remaster constrained compilation and orthogonal routing are **implemented and tested**: 110,721 diagram frames, 2,143 text boxes and 558 golden states pass. All-scene browser validation is complete; the completed master passes full decode and technical checks, with sampled encoded-picture review being closed. `remaster.py:57` calculates card layouts from tokens; `visual/remaster-geometry.mjs:105` calculates current card-border ports and obstacle-free routes. `pointAt` evaluates packet position directly from progress, and `validateState` checks bounds, overlaps, port alignment, and illegal crossings.

Connector routes use round joins, 4 px strokes, 16 px arrow length and 10 px half-height. Intermediate obstacles receive 12 px clearance. The named diagram-routing variant confines centerlines to x=144.4–1470 and y=304–744, excluding headings, notes, subtitles and the asset rail. Its executable constants and tests live in `visual/remaster-geometry.mjs`. An unroutable connection fails; no fallback may cross a card. Independent-port variants reserve earlier edge corridors regardless of visibility, use fixed side/fraction anchors and reject shared ports, overlapping segments and transverse crossings. Their explicit scene scope is S05, S06, S10, S12, S14, S23, S26, S27, S31, S32 and S36. S27 uses a blocked terminal with an X and no moving packet; S32 places admission control below application work and the waiting queue below its pool. These are component variants, not constraint exceptions. Card motion updates endpoint geometry from absolute time. Browser text measurements and source-bound all-frame geometry complement screenshots.

The body grid, character rail, note region, teaching panel and subtitle region have separate responsibilities. Quiz scenes S50–S57 omit the decorative editorial divider because it crosses the category-label zone; their approved typography and timing remain unchanged. Teaching-panel placement accounts for its measured height and preserves a 16 px gap above the subtitle anchor at y940. Required text that exceeds its allocation fails compilation or QA; font substitution and silent shrinking are not remedies.

| Exception ID | Release / scenes | Remaster applicability |
|---|---|---|
| `LEGACY-M10-SUBTITLE-001` | Frozen `CEH_M10_optimization_v1`, individually enumerated S01–S58 | None; zero exceptions in all 58 new scenes |

HARD CONSTRAINTS block rendering and delivery: safe bounds, text clipping, unauthorized overlap, invalid anchors, altered assets, nondeterminism, mismatched dependencies, and audio precision. SOFT DESIGN GUIDELINES cover composition preference, optional decoration and inherited easing variants. DOCUMENTED EXCEPTIONS require scene/component IDs, rule, reason, reviewer, tests, version and validity scope. Exception records cannot waive audio precision, asset custody or provenance.


Actual master checkpoint: `CEH_M10_Denial_of_Service_en-US_Editorial_Remaster_v1_1_1_4x_1s_master.mp4` is 1920×1080 at 30 FPS, 132,727 frames / 73:44.233. SHA-256: `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`. `qa/run-checks.json` is verified; full decoding found zero black intervals, and all 212,363,200 reference audio frames passed continuity comparison. All 165 encoded sample pictures passed artifact-bound agent review: `qa/encoded-review-coverage.json` binds the three inspection receipts and `qa/encoded-review.json` records the actual CLI review against the current master and all 165 hashes. ZIP extraction verification passed. Human viewing/listening remains pending.

### Historical geometry audit and reusable rules

The earlier measured caption bounds below describe the frozen reference, not proof of new scene placement.

Status: **implemented / tested** pure geometry validator and explicit exception matching. Full conversion of hand-authored diagrams to constraint primitives is **proposed**.

At 1920×1080 the effective safe rectangle is left=134.4, right=1785.6, top=86.4, bottom=993.6. Newly generated and redesigned content must fit. Decorative full-canvas paper is not content; it must have an explicit background role. Layout uses composition coordinates and uniform scaling, never independent x/y stretching of icons.

M10's document declared a subtitle reservation y945–1028, which conflicts with the 8% bottom margin. The audit measured all 1,371 existing caption boxes: maximum bottom 992.09375, no current caption-content breach. These are separate facts: the reservation needs a legacy exception even though present text fits. Existing chapter labels are at y85, 1.4 px above the top safe boundary. New output moves them to y87 and subtitles to y940, preserving font metrics and narration timing.

## Exception register

The machine register is `tools/ceh_video/ceh_video/visual/exceptions.v1.1.json`.

| ID | Release | Explicit affected scenes | Component / rule | New-workspace scope |
|---|---|---|---|---|
| LEGACY-M10-SUBTITLE-001 | frozen CEH_M10_optimization_v1 / optimization-v1 | S01–S58, enumerated individually in JSON | `.caption`, bottom-safe-area reservation only | none |

The exception binds the exact source production-profile hash, all 58 frozen composition hashes, release, frozen-legacy generation state, scene membership, selector and rule. Unknown IDs, changed source identities, new scenes, redesigned scenes and different selectors fail. User authorization is recorded verbatim in the register. No top-margin exception was added. No exception waives overlap, clipping, PCM accuracy, asset identity or provenance.

## Computable rules

Every new component carries bounds, ports, parent, layer, zone, minimum spacing, original aspect ratio where relevant and overflow policy. Card radius and stroke must belong to tokens. `geometry.mjs` calculates connector control points from the actual endpoint boxes. The fixture recalculates these at every absolute seek time, including reverse seeks. DOM-measured card edges and SVG path endpoints must agree within 0.25 px; a one-pixel displacement fails.

Text loads approved fonts before measurement. Measure words and lines, reject unbreakable overflow, and check browser boxes after seek. Clipping text to conceal overflow is forbidden. Parent backgrounds may contain child text; connector/packet overlaps with their own path are intentional component structure. Sibling content overlap requires an explicit relationship, never a general scene-wide exemption.

Geometry assertions are independent of screenshot tolerance. `AssetValidator` responsibilities currently live in the visual harness and preflight: compare all locked asset/font hashes, retain viewBox, and reject nonuniform aspect ratios. `LayoutValidator` and `GeometryValidator` responsibilities live in `geometry.mjs`; component specifications live in `components.mjs`. This avoids adding a TypeScript build solely for validation.

Existing hand-authored scenes remain a migration surface. Representative testing does not certify unmeasured paths in all historical scenes. New production renders are blocked when their scene lacks current visual evidence; this preserves the hard boundary while component adoption proceeds.

Final local delivery: the master is 207,412,180 bytes, SHA-256 `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`; `CEH_M10_editorial_remaster_v1_1_EDITABLE.zip` is 3,707,042,054 bytes, SHA-256 `4f5d3e5a2a82672466cd0830fc02a16a39a14d571810aef13f1bca9976b7264e`. `qa/engine-packaging.json` verifies ZIP CRC, extraction, 8,369 files and 8,368 payload hashes, including 165 encoded pictures and the cited golden-review receipts. `qa/engine-extracted-reconstruction.json` confirms 781 restored clips with zero inference and zero tempo passes. `qa/encoded-review-revalidation.json` confirms the same master and all 165 reviewed picture hashes after the conservative check rerun.

Project documents inside the ZIP retain their honest packaging-time checkpoint. These final repository records and the external receipts establish completed archive acceptance; the frozen project, staging tree and ZIP were not rewritten. Human listening remains pending for 478 items; the one-clip ASR run establishes minimum availability only, with full-film accuracy/timing `not_evaluated`.
