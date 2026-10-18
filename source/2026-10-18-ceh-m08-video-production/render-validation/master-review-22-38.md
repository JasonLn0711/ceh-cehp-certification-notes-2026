# Encoded master sample review: S22–S38 and C05–C07

Result: **sampled pass**. No blocking protocol, displayed-value, evidence-boundary, common-layer, clipping, or caption/layout issue was found in the **33 inspected encoded frames: 26 primary samples plus seven supplemental late-phase samples**.

Artifact: `output/CEH_M08_Sniffing_en-US_1_5x_1s_master.mp4`.

Master SHA-256, computed with `sha256sum` after the encoded audit passed:

`54e5a107cf94d7320eb91169f6a3267b81da408ef7bfacf3e745ef1f2df2faf3`

The review began after `qa/rendered-artifact-audit.json` reported `automated_encoded_artifact_checks_passed` and `qa/final-pipeline-process.json` reported completion with exit code 0. The automated receipt records a 3,957.933333-second master, 118,738 decoded frames, zero detected black intervals, and 115 extracted inspection samples. The primary review covers exactly **26** of those samples: 17 scene midpoints for S22–S38 and nine first/middle/last samples for C05–C07. Integration subsequently supplied seven additional late-phase frames from the same master; their separate review is appended below. Every reviewed PNG was opened at its original 1920×1080 size; no contact-sheet-only judgment was used.

The following are the audit's seek times in seconds on the master timeline. Images are under `output/inspection_frames/`.

| Encoded sample | Seek time (s) | Concrete observation |
| --- | ---: | --- |
| S22-midpoint.png | 1340.633333 | STAFF `10.44.10.21`, gateway `10.44.10.1`, and mapping `02:44:10:00:00:01` are readable. Ethernet gateway destination stays distinct from the remote-server IP destination. The repaired cue says `Local broadcast: ARP request only`. |
| S23-midpoint.png | 1403.033333 | Claim `02:44:10:00:00:66` is readable; recipient cache is `UNMEASURED`. Path arrows retain `If adopted` and `Forwarding?` conditions. |
| S24-midpoint.png | 1467.666667 | Gateway claims ending `:01` and `:66`, plausible explanations, empty record checkboxes, and `Names ≠ approval` are clear. |
| S25-midpoint.png | 1534.883333 | Trusted bindings and ARP inspection remain distinct diagram stages. No completed-control result is displayed. |
| S26-midpoint.png | 1600.883333 | Observing fields and active functions retain separate roles and the authorized-lab boundary. |
| S27-midpoint.png | 1664.583333 | A new MAC is paired with possible replacement/VM/privacy context, preserving identity uncertainty. |
| S28-midpoint.png | 1728.450000 | Corrected headers `Observation` and `Dependency / handling` match the mechanism-summary cells. |
| S29-midpoint.png | 1791.466667 | Expected devices, learning limit/action, and legitimate classroom flow remain readable and separate. |
| S30-midpoint.png | 1854.800000 | The initial-exchange model has Discover/Request toward the service and Offer/ACK toward the client. Router `10.44.10.1` and DNS `10.44.20.53` are readable. |
| S31-midpoint.png | 1921.466667 | Lease-pool state is unmeasured; client acceptance requires selected-exchange/client-state checks. The caption explicitly leaves offer acceptance unproved. |
| S32-midpoint.png | 1989.950000 | Trusted server replies and untrusted client requests have correct directions. The proposed binding schema supports DAI/IP Source Guard, with platform-specific rate policy. |
| S33-midpoint.png | 2057.450000 | Trunk prerequisites, outer/inner tag roles, and non-universal forwarding conditions remain explicit. |
| S34-midpoint.png | 2123.050000 | Access/trunk roles and allowed/native VLAN policy remain distinct review items. |
| S35-midpoint.png | 2187.666667 | Expected-root-to-neighbor BPDU/election direction is clear and remains conceptual. |
| S36-midpoint.png | 2251.766667 | Ordinary-edge expectation is paired with BPDU Guard; table text and teaching cue are clear. |
| S37-midpoint.png | 2321.133333 | The repaired `query` label clears the question card and query path. The client-to-resolver direction is correct; acceptance and cache adoption remain questions. |
| S38-midpoint.png | 2393.416667 | Signed-data authenticity/validation and encrypted-path confidentiality occupy separate lanes, with no claim that transport encryption validates every answer. |
| C05-first.png | 1310.100000 | The opening ARP title and simulation-stamp entrance are present before staged diagram/common-layer reveals. |
| C05-middle.png | 1471.266667 | The S24 record card is entering `UNCONFIRMED`; claim values and caption preserve an unconfirmed cause/approval boundary. See the crossfade note below. |
| C05-last.png | 1632.433333 | `Tool output ≠ changed cache or measured forwarding` is readable; common layers are present. |
| C06-first.png | 1632.633333 | The opening MAC-spoofing title and simulation-stamp entrance are present before staged diagram/common-layer reveals. |
| C06-middle.png | 1828.216667 | The DORA model's client/service roles and lifelines are present during its early reveal. |
| C06-last.png | 2023.800000 | The repaired S32 planned-check row has clear router `10.44.10.1` and DNS `10.44.20.53`, with no unwanted-OFFER gate overprint. Result markers remain empty and live testing remains pending. |
| C07-first.png | 2024.000000 | The opening VLAN title and simulation-stamp entrance are present before staged diagram/common-layer reveals. |
| C07-middle.png | 2225.883333 | The STP guard-role table is in its header reveal, with clear title, teaching cue, and common layers. |
| C07-last.png | 2427.766667 | DNSSEC and encrypted-DNS lanes remain distinct. The fixture explicitly claims no validation run or encrypted session. |

Northstar, Tally, and `SIMULATED OUTPUT` are visible in all **23 established-content samples**. The three chapter-first samples occur at chapter start plus 0.1 seconds and show the opening title/stamp entrance before the later reveals; those opening frames were not counted as missing common layers. Visible captions and teaching cues have clear separation from the diagrams and frame edges. No persistent label collision or clipped text was observed in these samples.

One nonblocking transition is disclosed: `C05-middle.png` at 1471.266667 seconds catches `Names ≠ approval` fading beneath the entering `UNCONFIRMED` stamp. The label and caption communicate the same unresolved-approval state. Source inspection confirms an explicit fade/reveal handoff; this still-frame review does not measure the transition's entire duration.

The primary midpoint set alone does not show the later E03 fixture phase in S30 or the later E04 fixture phase in S37. The supplemental encoded review below closes those specific coverage gaps. Separate native reviews remain recorded in `qa/C06-visual-review.md` and `qa/C07-visual-review.md`; encoded findings here are based on the actual decoded PNGs.

Supplemental review: **seven late-phase frames**, supplied by integration and listed in `qa/late-diagram-samples.json`, were inspected full-size. That manifest records the same master SHA-256 as this report. Global seek times and scene-local times are retained separately below; these seven are additional to the 26 primary samples, giving **33 inspected frames total**.

| Supplemental encoded sample | Master seek (s) | Scene-local time (s) | Concrete finding |
| --- | ---: | ---: | --- |
| S22-late.png | 1367.266667 | 57.266667 | STAFF `10.44.10.21`, gateway `10.44.10.1`, and MAC `02:44:10:00:00:01` remain clear. Ethernet/local-gateway and remote-IP roles are distinct. `Offline reading • no cache install` preserves the evidence boundary. |
| S23-late.png | 1430.800000 | 59.533333 | Two replies visibly claim gateway `10.44.10.1` with MACs `02:44:10:00:00:01` and `02:44:10:00:00:66`. The cache stays `UNMEASURED`; forwarding/adoption are conditional, with no accepted MITM path claimed. |
| S24-late.png | 1496.533333 | 61.733333 | The stamp is fully readable as `UNCONFIRMED`, with no remaining crossfade overprint. `Cause: OPEN`, empty checkboxes, and the record-evidence strip are clear. |
| S28-late.png | 1756.266667 | 59.633333 | Corrected observation/handling headers and unknown-destination row are clear. Possible handling remains a question; table pressure explicitly does not guarantee hub-like forwarding. |
| S30-late.png | 1882.933333 | 60.266667 | E03 shows Discover plus two incoming Offers with router options `10.44.10.1` and `10.44.10.66`. Client acceptance remains unmeasured and the repaired cue reads `ACK: not supplied in E03`. |
| S32-late.png | 2019.900000 | 63.900000 | The unwanted-OFFER model has cleared the planned-check rows. Router `10.44.10.1` and DNS `10.44.20.53` are unobstructed; result markers remain empty and switch export/live test remain pending. |
| S37-late.png | 2354.966667 | 71.666667 | Full question `lesson.northstar.example.test · A`, transaction `0x4808`, and records `203.0.113.80` / `203.0.113.81` are readable. Query/response directions are correct. Client acceptance and cache adoption remain open; source IP is labelled a packet claim. |

Northstar, Tally, and the simulation stamp are present in all seven supplemental frames. Diagrams, late status labels, teaching cues, and visible captions have clear separation. The seven late-phase samples have **no blocking finding** and verify the targeted repaired claims, status boundaries, and cleared boxes in encoded pixels. Including the primary set, common layers are visible in all 30 established-content samples; the three chapter-first samples retain their opening-entry timing described above.

This is a sampled encoded visual review. It does not establish continuous motion quality between samples, complete subtitle synchronization, human end-to-end listening/watching, or learner/practical acceptance. No production source, render, or Git operation was performed by this reviewer; the only authored file in this assignment is this report.

review_status: sampled_pass
