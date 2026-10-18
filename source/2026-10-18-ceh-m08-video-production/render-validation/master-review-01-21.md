review_status: sampled_visual_pass

# Encoded master review: S01–S21 and C01–C04

All 33 primary and 3 supplemental encoded samples received a sampled visual pass: **36 unique encoded frames total**. No blocking visual defect was observed at the selected times.

The reviewed artifact is `output/CEH_M08_Sniffing_en-US_1_5x_1s_master.mp4` in `/home/jnlngx10/Videos/CEH_M08_v1_0`.

- SHA-256: `54e5a107cf94d7320eb91169f6a3267b81da408ef7bfacf3e745ef1f2df2faf3`
- File size: 185,499,119 bytes.
- Duration: 3957.933333333333 seconds; 118,738 frames.
- Audit gate: `qa/rendered-artifact-audit.json`, status `automated_encoded_artifact_checks_passed`, complete master decode, zero detected black intervals.
- Primary sample count: **33 unique encoded frames**: 21 scene midpoints, S01–S21, plus 12 chapter first/middle/last frames, C01–C04.
- Supplemental sample count: **3 additional unique encoded frames** at S06, S08, and S11 duration-minus-4 positions, from `qa/late-diagram-samples.json`. Total inspected: **36**.

## What was inspected

All 33 primary PNGs in `output/inspection_frames` were viewed through these contact sheets:

- `output/inspection_frames/scenes-contact-01.jpg`: S01–S09.
- `output/inspection_frames/scenes-contact-02.jpg`: S10–S18.
- `qa/master-review-19-21-contact.jpg`: S19–S21.
- `qa/master-review-C01-C04-contact.jpg`: all 12 assigned chapter samples.

Fifteen of those same frames also received full-resolution follow-up: S03, S06, S07, S08, S10, S11, S14, S15, S17, S18; C01-middle, C01-last, C02-last, C03-last, and C04-last. These follow-ups do not increase the primary sample count. The three supplemental frames were each viewed at full resolution, making 18 full-resolution inspections among the 36 unique frames. Technical labels were compared with `project/data/scenes.json` and the corresponding native scene definitions.

## Findings

| Check | Observed result |
| --- | --- |
| Legibility and layout | Titles, visible table cells, address labels, mechanism labels, and teaching cues are readable. The dense layer stack, collection plan, four-source evidence grid, and final question grid remain separated. No clipped label or diagram/caption collision was observed. |
| Encoded common layers | `SIMULATED OUTPUT`, campus, and Tally are visible in the active-scene and chapter-ending samples. The encoded frames do not reproduce the apparent common-layer omissions seen during earlier native/tool viewing. |
| Chapter boundaries | The four opening samples are 0.1 seconds after chapter start. They show the correct incoming title and the start of the provenance reveal before diagram bodies and Tally enter. The corresponding middle and last samples contain the expected scene content. No outgoing-scene bleed or unexpected disappearance was observed at these boundary samples. |
| Local delivery and routing | S03 visibly retains STAFF `10.44.10.21`, office SVI `10.44.10.1`, and the local-gateway MAC relationship. S08 distinguishes gateway MAC from DNS server IP. S06 preserves source learning and destination lookup; S07 preserves the local NIC-filter boundary. |
| Observation and collection | Endpoint, mirror, tap, filter, and conversation labels agree with the canonical lesson. C01-middle separates recorded bytes, interpretation, and bounded claim. C01-last retains offline-file scope and stop conditions. C03-last retains the limitation that missing retained data does not establish absence from the network. |
| Application and protection limits | S17 shows `POST /classroom` and the harmless constructed body `lesson=packet-evidence`; the caption explicitly separates request body from authentication. S18 uses a TLS channel diagram rather than packet bytes claimed as a completed handshake. S19/S20 and C04-last preserve tunnel endpoints, configuration context, and independent evidence questions. |
| S10 reveal state | The checksum-offload box is partially transparent at 579.9333333333333 seconds. The encoded sample falls at scene-local 30.566666666666666 seconds, inside its 0.8-second authored entrance beginning at 30.444417 seconds. This sample records a reveal in progress, rather than establishing a persistent low-contrast or missing layer. |

No repair or rerender is requested from this sampled review.

## Exact primary sample times

Times are seconds from master start, copied from the audit’s `sampled_frames` values without rounding. All files below are under `output/inspection_frames`.

| Sample | Master time, seconds | PNG |
| --- | ---: | --- |
| S01 midpoint | 31.7 | `S01-midpoint.png` |
| S02 midpoint | 93.7 | `S02-midpoint.png` |
| S03 midpoint | 154.1 | `S03-midpoint.png` |
| S04 midpoint | 214.79999999999998 | `S04-midpoint.png` |
| S05 midpoint | 277.0333333333333 | `S05-midpoint.png` |
| S06 midpoint | 338.3333333333333 | `S06-midpoint.png` |
| S07 midpoint | 396.8666666666666 | `S07-midpoint.png` |
| S08 midpoint | 457.79999999999995 | `S08-midpoint.png` |
| S09 midpoint | 519.6166666666666 | `S09-midpoint.png` |
| S10 midpoint | 579.9333333333333 | `S10-midpoint.png` |
| S11 midpoint | 642.1833333333332 | `S11-midpoint.png` |
| S12 midpoint | 704.8666666666666 | `S12-midpoint.png` |
| S13 midpoint | 766.8499999999999 | `S13-midpoint.png` |
| S14 midpoint | 830.7166666666666 | `S14-midpoint.png` |
| S15 midpoint | 897.0166666666665 | `S15-midpoint.png` |
| S16 midpoint | 958.7333333333332 | `S16-midpoint.png` |
| S17 midpoint | 1018.4666666666666 | `S17-midpoint.png` |
| S18 midpoint | 1084.1 | `S18-midpoint.png` |
| S19 midpoint | 1150.2 | `S19-midpoint.png` |
| S20 midpoint | 1215.6 | `S20-midpoint.png` |
| S21 midpoint | 1279.55 | `S21-midpoint.png` |
| C01 first | 0.1 | `C01-first.png` |
| C01 middle | 122.69999999999999 | `C01-middle.png` |
| C01 last | 245.29999999999998 | `C01-last.png` |
| C02 first | 245.49999999999997 | `C02-first.png` |
| C02 middle | 397.3833333333333 | `C02-middle.png` |
| C02 last | 549.2666666666665 | `C02-last.png` |
| C03 first | 549.4666666666666 | `C03-first.png` |
| C03 middle | 768.1999999999999 | `C03-middle.png` |
| C03 last | 986.9333333333333 | `C03-last.png` |
| C04 first | 987.1333333333333 | `C04-first.png` |
| C04 middle | 1148.5166666666667 | `C04-middle.png` |
| C04 last | 1309.9 | `C04-last.png` |

## Supplemental late-phase encoded samples

These three additional frames are preserved separately from the 115 primary audit samples in `qa/late-diagram-samples.json`. Its master hash matches the reviewed MP4. Each position is the scene’s duration minus 4 seconds. They increase this review’s inspected count from 33 to 36, without changing the primary table above.

| Supplemental sample | Exact master time, seconds | Exact scene-local time, seconds | PNG | Full-resolution finding |
| --- | ---: | ---: | --- | --- |
| S06 late | 363.99999999999994 | 55.333333333333336 | `S06-late.png` | `ANALYST` and `Audit port` fit cleanly in the final learning-table row. Header padding, forwarding-choice cards, Tally, stamp, and caption spacing are clear. |
| S08 late | 485.8666666666666 | 60.13333333333334 | `S08-late.png` | Both VLANs and routed-hop arrows are visible. The complete table retains gateway MAC versus destination IP, and the ARP/new-frame note has a visible gap below the table. No label or caption overlap. |
| S11 late | 669.8666666666666 | 59.36666666666667 | `S11-late.png` | `Selected directions` is readable below the route and above the cards. Source port, switch mirror, collector, capacity limit, Tally, and stamp remain visible without collision. |

All three supplemental samples pass. No additional repair or rerender is requested.

## Scope and remaining limits

This is visual inspection of actual encoded master samples after the automated encoded-artifact gate passed. It is distinct from the earlier native capture review. It does not constitute uninterrupted human watching or listening, and does not rule out brief defects between the selected times. Audio continuity and quiz holds are outside this assignment.

The primary midpoint set alone did not expose the later S06 `ANALYST` row or S11 `Selected directions` label. Their authored reveals begin after those midpoints. The separately identified late-phase samples now provide direct encoded evidence for those corrected labels and the S08 table/note gap. This targeted coverage does not establish uninterrupted visibility at every intervening frame.

The pass applies to the stated artifact hash and selected frames. Human full-length acceptance remains a separate gate.
