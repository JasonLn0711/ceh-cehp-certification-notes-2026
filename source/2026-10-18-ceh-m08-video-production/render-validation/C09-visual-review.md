initial_review_status: repairs_required

# C09 native visual review

Reviewed on 2026-10-18, Asia/Taipei. This review covers the ten actual 1920×1080 PNGs in `C09-direct`: middle and reason captures for S44–S48. It is pre-render evidence from direct native GSAP scene capture. Encoded output, continuous motion, and delivery readiness remain separate checks.

`C09-check.json` reports HyperFrames 0.8.171, `ok: true`, zero lint/runtime/layout/contrast findings. Its motion check is disabled; this receipt does not establish continuous playback or encoded quality.

## Repair findings from the first captures

| ID | Capture and local time | First-capture issue, now superseded | Repair and native verification |
| --- | --- | --- | --- |
| C09-L1 | `S44-reason.png`, 58.033 s | The coverage note started at y715 while both comparison cards ended near y720; the borders overlapped. | Resolved. The new reason capture shows the note at y740, h82, separated from the comparison cards and teaching cue. |
| C09-L2 | `S46-reason.png`, 63.600 s | The `REQUEST / ACK / installed client state` strip started at y630 while the table extended to y654, covering its lower border. | Resolved. Table row height 90 makes the table end at y600. The new reason capture shows clear separation above the y630 strip and below it. |
| C09-T1 | `S45-middle.png`, 31.783 s | “Two MAC claims” appeared with only packet 1; packet 2 was delayed to 35.124 s despite the opening explanation. | Resolved. The second row now reveals at the actual “Both are visible” sentence. Both exact claims are visible in the new middle capture. |
| C09-E1 | `S45-reason.png`, 59.567 s | The note grouped approval with cache/forwarding under “unmeasured,” conflating their evidence states. | Resolved. The new reason capture reads “Approval unconfirmed; recipient cache and forwarding unmeasured.” It fits in two lines inside the note and clears the teaching cue. |

## Protocol, fixture, and evidence checks

The fixture files were read offline and checked against their manifest hashes and counts. No traffic was sent.

| Scene | Exact fixture comparison | Evidence boundary in the captured teaching content |
| --- | --- | --- |
| S44 | Endpoint fixture: 1 packet; mirror fixture: 4 packets. The manifest declares one shared broadcast plus three additional STAFF DNS records in the stipulated mirror view. | Coverage differences stay distinct from packet loss or a failed real service. “Stipulated mirror view” keeps the configuration assumption visible. |
| S45 | ARP packet 1 claims `10.44.10.1 → 02:44:10:00:00:01`; packet 2 claims `10.44.10.1 → 02:44:10:00:00:66`. Displayed suffixes `...:00:01` and `...:00:66` match. | No recipient cache export or measured forwarding path is supplied; successful interception or theft is not asserted. The repaired note correctly keeps approval unconfirmed. |
| S46 | Discover and both offers share transaction `0x4e530008`. The two router options are `10.44.10.1` and `10.44.10.66`. | The graphic calls the router settings proposed and states REQUEST, ACK, and installed client state are not supplied. It does not claim client acceptance or an exhausted pool. |
| S47 | DNS transaction `0x4808`, type A, question `lesson.northstar.example.test`, responses `203.0.113.80` and `203.0.113.81`. The visible short name `lesson` consistently abbreviates that supplied question. | The diagram states cache adoption, later connection, and compromise are unmeasured. Resolver policy, zone state, and client behavior remain next evidence sources. Matching question/ID is presented as a comparison, not sufficient authentication. |
| S48 | The four mechanisms remain collection coverage, ARP claims, DHCP offers, and DNS answers. | The concluding note explicitly declines to infer one successful interception chain from shared context. |

The inspected diagrams, notes, and teaching cues stay clear of the caption region. The material S44/S46 border collisions in the first captures are resolved in the refreshed captures.

## Native raster diagnostic

Initial per-frame viewing showed apparent common-layer omissions in S44-middle/reason, S45-reason, S46-middle, S47-middle/reason, and S48-reason, while their receipt opacity values were `1`. Those appearances were recorded separately from packet facts and evidence states.

After recapture, a direct pixel check finds nonblank simulation-stamp, campus, and Tally regions in all ten current PNGs, with consistent ink counts for each common region across scenes. The current DOM receipt also records opacity `1`. Any differing tool-display appearance remains a capture/viewing diagnostic; it does not establish an authored hide or an encoded failure.

DOM opacity and native PNGs do not establish encoded visibility. Actual encoded samples must verify final visibility and simulation provenance.

## Current gate

All ten refreshed native frames were reviewed in `C09-native-reviewed.png`; repaired S44-reason, S45-middle/reason, and S46-reason were additionally reviewed at full resolution. The updated 0.8.171 browser check has zero lint/runtime/layout/contrast findings. No remaining authored protocol, fixture, evidence-state, label, or caption-overlap blocker was observed at these sampled times.

This pass clears the native pre-render review. Continuous motion and actual encoded samples remain separate gates.

review_status: pass
