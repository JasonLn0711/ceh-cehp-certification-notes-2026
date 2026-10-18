# C06 native visual review

Review outcome: corrected native frames approved.

Reviewed all twelve actual native frames in `C06-direct/`: S27–S32 at their measured midpoints and duration minus four seconds. The capture command was `node scripts/inspect_direct.mjs C06`; `C06-direct/receipt.json` records the seek times and common-layer DOM state. Chapter preparation completed with exit code 0 before capture. This review covers native scene appearance, protocol meaning, fixture values, evidence limits, and label/caption clearance. Encoded output remains a separate verification gate.

Resolved findings, verified after integration rebuilt C06 and a second complete native capture finished:

- S32, reasoning frame at 63.900 s: the unwanted-OFFER model now leaves before the planned isolated-lab rows appear. Its former stroke at x1062, y615–620 no longer touches `10.44.10.1`; both the router and DNS values are clear. The trust topology remains. Evidence: `C06-direct/S32-reason.png`.
- S30, reasoning frame at 60.267 s: the teaching cue now reads `ACK: not supplied in E03`, consistent with unmeasured acceptance. The common DORA model has correct message directions. Evidence: `C06-direct/S30-reason.png`.
- S28, midpoint and reasoning frames at 31.817 s and 59.633 s: headers now read `Observation | Dependency / handling`, correctly describing the mechanism-summary cells. Evidence: `C06-direct/S28-middle.png` and `C06-direct/S28-reason.png`.

The inspected S27 and S29 content remains readable. S28 preserves platform-dependent handling and avoids claiming universal hub-like forwarding. S30/S31 retain router values `10.44.10.1` and `10.44.10.66`; the DORA model records DNS `10.44.20.53`. The E03 diagrams retain one Discover, two Offers, and unresolved client acceptance. S31 keeps lease-pool state unmeasured and names the missing capacity/client evidence. S32 distinguishes trusted server paths from untrusted access paths, shows binding support for DAI and IP Source Guard, and keeps live validation pending with empty result markers.

Titles, subtitles, and teaching labels have clear separation in the inspected frames. Northstar, Tally, and the simulation stamp are visible; the receipt reports opacity 1 for these common layers. No blocking overlap, clipping, incorrect fixture value, protocol-direction error, or unsupported acceptance claim remains in the inspected native frames. No production sources were changed by this reviewer. This approval covers the native review scope; encoded-media verification and human full-view acceptance remain separate.

review_status: pass
