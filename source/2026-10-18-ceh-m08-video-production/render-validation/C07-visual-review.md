# C07 native visual review

Review outcome: corrected native frames approved.

Reviewed all twelve actual native frames in `C07-direct/`: S33–S38 at their measured midpoints and duration minus four seconds. The capture command was `node scripts/inspect_direct.mjs C07`; `C07-direct/receipt.json` records seek times and common-layer DOM state. Chapter preparation completed with exit code 0 before capture. This review covers native scene appearance, protocol meaning, fixture values, evidence limits, and label/caption clearance. Encoded output remains a separate verification gate.

Resolved findings, verified after integration rebuilt C07 and a second complete native capture finished:

- S37, midpoint at 37.833 s and reasoning frame at 71.667 s: the `query` label now has baseline 435 in its own native text group. It has clear separation from the question card's bottom at y400 and the route at y455. Evidence: `C07-direct/S37-middle.png` and `C07-direct/S37-reason.png`.
- S37, reasoning frame: the 600px-wide question card now visibly shows `lesson.northstar.example.test · A` at 30px, matching `data/m08_network_extensions.json` and the scene's fixture metadata. The transaction identifier remains readable below it.

S33/S34 keep VLAN-hopping prerequisites and platform/design conditions explicit and preserve the distinction between a proposed path and observed boundary crossing. S35 remains a conceptual STP diagram, with an expected root and a request to verify selected root and port state. S36 distinguishes BPDU Guard's ordinary-edge expectation from Root Guard's superior-root boundary and preserves platform-specific recovery review.

The S37 answer records show `203.0.113.80` and `203.0.113.81` for transaction `0x4808`. Both response arrows point toward the client-side boundary; client acceptance and cache adoption stay open, and the sender's IP remains a packet claim. S38 distinguishes signed-data authenticity/validation from encrypted-path confidentiality and explicitly states that the fixture establishes no validation run or encrypted session.

Text, teaching cues, and subtitles are readable and separated in the inspected frames. Northstar, Tally, and the simulation stamp are visible in all inspected frames; the receipt reports opacity 1 for those common layers. No blocking overlap, clipping, incorrect fixture value, protocol-direction error, or unsupported acceptance claim remains in the inspected native frames. No production sources were changed by this reviewer. This approval covers the native review scope; encoded-media verification and human full-view acceptance remain separate.

review_status: pass
