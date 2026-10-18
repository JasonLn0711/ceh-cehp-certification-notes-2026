# M07 source validation receipt

Recorded 2026-10-18. Copies match the actual local package/release reports. Status: **source_ready**.

| Evidence | Result | Claim boundary |
| --- | --- | --- |
| [Source QA](source_qa.json) | 808 passed, 0 failed; 11 chapters, 58 scenes, 9,174 spoken words, 8 questions | Complete source mappings, editable media, fixture, assets, reference silence and links |
| [Browser QA](browser_qa.json) | 94 passed, 0 failed | 58 SVG boards and four actual motion examples; all 12 repeated seek pairs have identical final-run pixel hashes |
| [Static evidence](hyperframes-static-evidence.json), [process tree](hyperframes-process-tree.json), [detection](hyperframes-detection-comparison.json), [quiz](hyperframes-quiz-one-second.json) | All four HyperFrames checks pass | Each retains one nonblocking nested-structure Studio warning for its single-clip example |
| [Visual review](visual-review.md) | All 58 board and 18 actual deck-export previews inspected | Native SVG/PPTX structures and source design, not full-film encoded frames |
| [Release receipt](release_receipt.json) | 296 archive files; 294 payload hashes; 0 CRC/extraction-hash failures | Closed source archive, not final MP4 |
| [Package manifest](PACK_MANIFEST.json) | Payload SHA-256 map; excludes its own digest and FILES_SHA256.txt | Reproducible archive content identity |

The reference silence is exactly 48,000 stereo frames of zero PCM at 48 kHz. This is distinct from future AAC decoded behavior. The editable deck has 18 slides, 222 native shapes/text boxes and 158 text runs. No M07 speech synthesis, aligned subtitles, full 58-scene animation or MP4 was performed.

Full source/assets/ZIP stay under `~/Videos/CEH_M07_v1_0/`. These compact copies support the [production record](../../../notes/m07-malware-threats/video-production-2026-10-18.md).
