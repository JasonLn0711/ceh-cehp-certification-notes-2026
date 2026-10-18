initial_review_status: repairs_required

# C05 native visual review

Reviewed on 2026-10-18, Asia/Taipei. This review covers the ten actual 1920×1080 PNGs in `C05-direct`: middle and reason captures for S22–S26. It is pre-render evidence from direct native GSAP scene capture. Encoded output, continuous motion, and delivery readiness remain separate checks.

The updated `C05-check.json` reports HyperFrames 0.8.171, `ok: true`, and zero lint/runtime/layout/contrast findings. Its motion check is disabled; this receipt does not establish continuous playback or encoded quality. The earlier contrast warning is retained below as repair history.

## Repair findings from the first captures

| ID | Capture and local time | First-capture issue, now superseded | Repair and native verification |
| --- | --- | --- | --- |
| C05-L1 | `S22-reason.png`, 57.267 s | “Offline reading • no cache install” at baseline y803 crossed the teaching-mapping paper’s bottom stroke at y785. | Resolved. The complete mapping cluster moved up 20 pixels; the paper now ends at y765. The new reason capture shows a clear gap above the offline limit, with fixture values unchanged. |
| C05-L2 | `S24-reason.png`, 61.733 s | “Next check” at baseline y735 touched the approval-paper bottom at y715. | Resolved. The new reason capture places the label at x1265, baseline325, above the records column. It clears the hypotheses heading, paper, stamp, and evidence strip. |
| C05-C1 | S23 cache question mark | Earlier CLI contrast was 2.06:1 against the required 3:1: gray `?`, selector `div > div:nth-of-type(2) > div > svg > g:nth-of-type(19) > text > tspan`, group `S23-cache-question`. | Resolved. The new middle capture shows an INK question mark. The updated browser check reports zero contrast findings. `UNMEASURED` remains explicit. |
| C05-T1 | `S22-middle.png`, 30.633 s | “Local broadcast” accompanied an off-subnet IP packet inside a gateway-addressed frame, which could blur ARP-request broadcast with subsequent gateway-directed traffic. | Resolved. The new middle capture says “Local broadcast: ARP request only,” preserving the request-only scope while the remote IP remains visible. |

## Protocol, fixture, and evidence checks

- S22 displays STAFF `10.44.10.21`, gateway `10.44.10.1`, and teaching MAC `02:44:10:00:00:01` correctly. The nested Ethernet/IP graphic retains the remote IP destination while using the gateway’s local MAC. The ending states offline reading causes no cache installation.
- S23 displays the same gateway IPv4 address with exact MACs `02:44:10:00:00:01` and `02:44:10:00:00:66`. Cache state remains `UNMEASURED`; dashed paths, “If adopted,” and “Forwarding?” retain the conditional mechanism. No captured packet token presents forwarding as observed.
- S24 keeps failover, maintenance, duplicate address, and spoofing as plausible explanations. `UNCONFIRMED` approval and `Cause: OPEN` preserve the case uncertainty. Blank record checkboxes stay blank.
- S25 presents trusted bindings, inspection, trusted-port configuration, and permitted/rejected tests. Its source and ending caption keep device enforcement dependent on an activated real lab; these captures do not establish DAI enforcement.
- S26 distinguishes stored-field observation from active tools in a separate authorized lab. Its ending explicitly separates tool output from changed cache or measured forwarding.

The exact ARP claims were also read from the local PCAP bytes. All six fixture files match the manifest SHA-256 values and packet counts; this was offline file reading only. No traffic was sent.

No diagram or label overlaps the caption region in the inspected images. At `S26-middle.png` (31.650 s), a blank caption is consistent with the supplied caption gap from 31.481 s to 32.191 s.

## Native raster diagnostic

Initial per-frame viewing showed apparent common-layer omissions in S23-middle, S24-middle, S24-reason, and S26-middle despite receipt opacity `1`. That discrepancy was recorded separately from the authored evidence states.

The refreshed native contact sheet `C05-native-reviewed.png` shows the simulation stamp, campus, and Tally across all ten captures. A direct pixel check of the three common-layer regions is also nonblank in every current PNG, with consistent ink counts across scenes, and the current receipt retains opacity `1`. The initial discrepancy remains a capture/viewing diagnostic; it does not establish an authored hide or an encoded failure.

DOM opacity and native PNGs do not establish encoded visibility. Inspect actual encoded samples for the same intervals later. Simulation provenance must remain visibly established in final output.

## Current gate

All ten refreshed native frames were reviewed in `C05-native-reviewed.png`; repaired S22-middle/reason, S23-middle, and S24-reason were additionally reviewed at full resolution. The updated browser check has zero findings. No remaining authored protocol, fixture, evidence-state, label, or caption-overlap blocker was observed at these sampled times.

This pass clears the native pre-render review. Continuous motion and actual encoded samples remain separate gates.

review_status: pass
