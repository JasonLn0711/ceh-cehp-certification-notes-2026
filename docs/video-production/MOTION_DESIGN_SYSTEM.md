# v1.2 implementation addendum

v1.2 adds independently rendered original SVG figures and resource/sequence/topology forms. Semantic component bounds and ports remain verifiable without a card background. Named semanticFigure sizing and the original student extraction have provenance and measured QA gates.

Status: implemented changes under validation; see [v1.2 standard](PRODUCTION_STANDARD_v1.2.md) and [execution evidence](M10_EFFICIENCY_IMPLEMENTATION.md). Historical evidence below applies only to its named release.

# Motion design system v1.1

## Production remaster tokens 1.2.0

Status: full-scene specifications and the shared production compiler are **implemented and browser-tested** across all 58 scenes, including 558 golden comparisons. The complete encoded master passes full decode and technical checks; all 165 sampled encoded pictures pass artifact-bound agent review, and human acceptance remains separate. The active English profile selects project `design/tokens.json` with `token_manifest`. This version preserves original palette/font hashes and adds explicit production layout variants. The historical `visual/tokens.v1.1.json` remains the earlier prototype source.

The compiler consumes the token body region, 40 px grid gap, 16 px object padding, card-height limit, note region, and right-side character rail. It measures approved font binaries before emitting SVG text; browser QA checks actual rendered font loading, bounds and overflow. Text, connector geometry, and immutable artwork remain independently inspectable. Per-scene absolute coordinates are excluded from the authored specifications.

All 58 scenes are affected. S01–S49 and S58 use source-bound flow, comparison, resource, timeline, evidence or scope specifications; S50–S57 use measured quiz components with unchanged hold/reveal timing. Canonical copy and quantities stay unchanged. Scene labels retain source provenance, including explicit units for bars and illustrative queue counts.

### Figma exchange contract

Figma remains an optional design/specification source. Export named component variants, token references, SVG viewBox, stable object IDs, named ports in component-local coordinates, font family/license identity, source-file/version identity, and SHA-256. Store exports locally and validate them before importing. A changed Tally export requires identity/provenance review; an export cannot silently replace locked artwork. Auto Layout constraints inform supported production variants; unsupported effects remain a documented manual specification. No live Figma file or round-trip test has been supplied, so that integration remains **proposed**.


Actual master checkpoint: `CEH_M10_Denial_of_Service_en-US_Editorial_Remaster_v1_1_1_4x_1s_master.mp4` is 1920×1080 at 30 FPS, 132,727 frames / 73:44.233. SHA-256: `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`. `qa/run-checks.json` is verified; full decoding found zero black intervals, and all 212,363,200 reference audio frames passed continuity comparison. All 165 encoded sample pictures passed artifact-bound agent review: `qa/encoded-review-coverage.json` binds the three inspection receipts and `qa/encoded-review.json` records the actual CLI review against the current master and all 165 hashes. ZIP extraction verification passed. Human viewing/listening remains pending.

### Historical bounded design-system implementation

The prototype status and fixture evidence below describe the earlier engineering workspace. Its scope statement does not limit the now-authorized full remaster.

Status: **implemented** shared tokens, geometry and component specifications; **tested** bounded SVG/Pixi fixtures. Applying every primitive to every historical scene is **proposed**, outside the strict migration scope.

`tools/ceh_video/ceh_video/visual/tokens.v1.1.json` derives the approved palette and safe-area fractions from the immutable `STYLE_TOKENS.json`, records its SHA-256 and records the approved font hashes. The source token file is preserved. The executable compiler still owns existing scene artwork; this version does not replace Tally, Northstar, paper texture or the art direction.

| Category | Contract / source |
|---|---|
| Canvas | 1920×1080, 30 FPS; uniform viewport scaling |
| Color | paper #F0EBE4, ink #292421, terracotta #C8755D; all original palette entries retained |
| Typography | actual Liberation Sans regular/bold and DejaVu Sans Mono files; 54 heading, 34 caption, 36 label, 27 metadata |
| Font metrics | browser `document.fonts.load/ready`; intrinsic canvas measurement; DOM boxes checked after seek |
| Spacing | 8/16/32 component variants; these are prototype variants, not an overwrite of existing scenes |
| Radius | card 8, legacy panel 4; explicit variant required |
| Stroke | prop 4, focus 5, fine 2; round caps/joins |
| Texture/shadow | existing locked assets only; no new filters or procedural warp |
| Subtitle | x230/y940/w1460/h53.6, bottom 993.6; text overflow fails |
| Title/diagram/teaching | explicit zones in tokens; heading y125, diagram y272–822, teaching y850–936 |
| Motion | entrance .8, draw 1.3, packet 2.4, Tally arm .45/.5 seconds; inherited power2.out |
| Stagger | 0 until a component-specific value has evidence |
| Layer order | paper, diagram, character, teaching, subtitle |

`components.mjs` provides typed-by-shape specifications for RoundedCard, RoundedPanel, BrowserWindow, DiagramNode, Connector, CurvedArrow, Callout, Label, Packet, FlowPath, DeviceIcon, CharacterRig and SubtitlePanel. Shared bounds, ports, parent, layer, zone, spacing and overflow policy are implemented. The representative renderer exercises cards, labels, packet, connector and mask. The remaining names are reusable specifications, **not claims that all corresponding production renderers were migrated**.

Grid computes cells from region/columns/gap; CSS Flexbox aligns card contents; SVG viewBox retains composition coordinates. `measureText()` wraps by actual font metrics and rejects unbreakable overflow. Asset-bearing components require original viewBox and asset hash, preserve aspect ratio and allow zero geometric warp. Original rig poses and movement remain in the existing Python/SVG engine.

## Design exchange

Figma is an optional offline design/specification source. Export reviewed component variants, local SVGs, token JSON and anchor sidecars containing stable object IDs, ports and original viewBox. Preserve export version, original asset SHA-256, font license/source and reviewed token differences. Do not automatically re-export Tally or convert every Figma node into code. CI consumes checked-in/local assets without a live Figma service.

The [Figma file API](https://developers.figma.com/docs/rest-api/file-node-types/) exposes layout/constraint information and the [variables API](https://developers.figma.com/docs/rest-api/variables/) supports structured variable exchange. A live Figma export/import round trip is **proposed**: no design file was supplied for this iteration. Token additions require a named variant and review record; they do not silently replace the canonical palette or fonts.

## Measured production component variants

Device icons use the approved SVG viewBox with uniform 72 px inline or 40 px
compact stacked variants. Resource bars reserve a 32 px track. Typography
retains 30 px body text and 28 px notes. The tokenized 8 px width guard covers
observed PIL/Chromium glyph-metric differences (one tested line measured
583.6875 px in PIL, 588 px advance and 589 px ink bounds in Chromium). Actual
rendered text still must fit its inner box within 0.25 px; this is measurement
headroom, not an overflow exception or a reduced font size.

`remaster-assets.mjs` checks original SVG hashes, uniform transforms, absence of
skew, safe-area bounds and the actual Tally/campus rail bounds at component
entrance and gesture times. Its report is a required full-release gate.

Final local delivery: the master is 207,412,180 bytes, SHA-256 `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`; `CEH_M10_editorial_remaster_v1_1_EDITABLE.zip` is 3,707,042,054 bytes, SHA-256 `4f5d3e5a2a82672466cd0830fc02a16a39a14d571810aef13f1bca9976b7264e`. `qa/engine-packaging.json` verifies ZIP CRC, extraction, 8,369 files and 8,368 payload hashes, including 165 encoded pictures and the cited golden-review receipts. `qa/engine-extracted-reconstruction.json` confirms 781 restored clips with zero inference and zero tempo passes. `qa/encoded-review-revalidation.json` confirms the same master and all 165 reviewed picture hashes after the conservative check rerun.

Project documents inside the ZIP retain their honest packaging-time checkpoint. These final repository records and the external receipts establish completed archive acceptance; the frozen project, staging tree and ZIP were not rewritten. Human listening remains pending for 478 items; the one-clip ASR run establishes minimum availability only, with full-film accuracy/timing `not_evaluated`.
