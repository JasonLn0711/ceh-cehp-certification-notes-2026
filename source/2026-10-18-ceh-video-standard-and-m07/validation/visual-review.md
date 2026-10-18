# Source visual and runtime review — 2026-10-18

Scope: all 58 static SVG source boards, 18 actual native-deck export pages, and four implemented 12-second motion examples. Complete film animation, narration, aligned captions and MP4 are the next layer.

## Inspected artifacts

All board and slide contact sheets were inspected. Dense quiz S54 and the actual exported slide 17 were also viewed at native size. Process-tree S34/S45 and their deck representation received a final layout check after separating process relationships from contextual evidence. The original Tally, inherited palette, safe caption area, board order and reading hierarchy remain visible. Tally is a preserved artwork object; the deck's instructional text, diagram boxes and connectors remain native editable objects.

The deck has 18 slides, 222 native shapes/text boxes and 158 text runs. These are measured XML object counts, not an arbitrary editability quota. LibreOffice exported the actual deck to PDF and pdftoppm rasterized all 18 pages. This establishes a real export preview and structural editability; no Microsoft PowerPoint application interaction or full-film viewing is claimed.

Export commands, from the package root:

```bash
libreoffice --headless --convert-to pdf --outdir slides slides/CEH_M07_Editable_Visual_Lookbook_18slides.pptx
pdftoppm -scale-to 1920 -png -r 96 slides/CEH_M07_Editable_Visual_Lookbook_18slides.pdf previews/slides/slide
```

## Applied refinements

- Kept the original palette while using existing ink for small metadata/footer text that failed the accent color's contrast check.
- Moved contextual user/time/unknown-script cards outside the parent-child relationship and cleared Tally from their outlines.
- Made all four example asset trees self-contained, so HyperFrames does not traverse above an example project root.
- Made the quiz's initial answer/hold state explicit; the answer is hidden before 7.000 in the illustrative [6.000,7.000) hold.
- Retained a finite paused timeline and measured SVG path length for the process relationship.

## Runtime evidence and limits

Browser QA contains 94 passing assertions and zero failures: 58 SVG safe-region checks plus 36 example contract/motion/seek/resource/boundary checks. All 12 repeated direct/reverse-seek screenshot pairs in the final run have identical hashes and identical computed states. The harness also declares a maximum two-pixel / channel-delta-32 tolerance for isolated Chromium edge rasterization; it was not needed by the final run. Earlier findings are retained as historical, resolved diagnostics in initial-runtime-findings.json.

All four actual HyperFrames checks pass runtime, layout, motion and contrast at 0, 3, 6.5, 7 and 10 seconds. Each retains one nonblocking `nested_structure_needs_subcomposition` Studio warning because the example intentionally has one clip with nested instructional objects. This does not claim a full 58-scene Studio project. A future full-film project should expose scene sub-compositions for editing.

The source WAV contains exactly 48,000 stereo frames of zero PCM at 48 kHz. No generated speech or final AAC exists here. No encoded-film, synchronized-subtitle or human listening acceptance is claimed.
