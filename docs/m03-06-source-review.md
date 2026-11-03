# M03-06 source and factual review

Checked 2026-11-03 (Asia/Taipei). Public lesson v1.0.0. This review covers technical claims and bilingual meaning, not independent human accessibility certification or learner understanding.

## Route and scope

The current `study-plan/core-route-2026-10-27.json` row is CEH26-M03-C06, M03-06, reading order 27, source section 三/M03 row 6, title OS Fingerprinting, importance 4/difficulty 3. Its original reason is「理解作業系統辨識的原理、指紋特徵與不確定性。」Mode new_teaching/new_scope, no legacy IDs. The original planned slot 2026-11-04 19:00 Asia/Taipei is planning metadata, not delivery evidence. M03-07 remains the next pending unit; no lesson is skipped by calendar date.

Complete paired teaching and reference answers are retained under `notes/m03/`. The single question is how packet observations support a limited operating-system inference, and what evidence verifies it. Shop-response analogy, active/passive collection, TTL, TCP fields/options, matching uncertainty, middleboxes and management evidence remain one composite unit. Examples are synthetic, no third-party probes were performed. Personal conversation identifiers, submissions and understanding stay outside this public repository.

## Primary sources

All living Nmap pages below were actually read on 2026-11-03. No installed Nmap version or database revision is asserted.

- https://nmap.org/book/man-os-detection.html — `-O` means active OS detection; at least one open and one closed TCP port improves results. This is not a guaranteed identity test.
- https://nmap.org/book/osdetect-methods.html — IPv4 fingerprint probes compare multiple response details, including TCP options, windows, sequence/timestamp behavior and ICMP response features.
- https://nmap.org/book/osdetect-usage.html — OS detection and service-response OS information are distinct evidence and can describe different network layers.
- https://nmap.org/book/osdetect-unidentified.html — NAT, forwarding and other middleboxes can complicate fingerprint interpretation; network position must be recorded.
- https://nmap.org/book/osdetect-other-methods.html — passive observation is distinct from sending identification probes. p0f is introduced only as an example of passive fingerprinting, not a recommendation to install a current version.
- https://nmap.org/book/osdetect-guess.html — matching/confidence behavior differs between IPv4 weighted matching and IPv6 classification; reported similarity is not a guaranteed real-world probability.
- https://www.rfc-editor.org/rfc/rfc791.html — RFC 791, September 1981: IPv4 TTL is an eight-bit lifetime field reduced during processing. The lesson's 64−3=61 is explicitly conditional, not a device identity rule.
- https://www.rfc-editor.org/rfc/rfc9293.html — RFC 9293, August 2022: TCP receive-window and option semantics, including MSS. Receive window is not network speed or whole-machine RAM.

The external p0f README could not be read because robots access was denied. It was not retried or used as evidence; the Nmap primary documentation supports the limited passive-method example.

## Review outcomes

- Observation, tool inference and independently checked asset evidence are labeled separately.
- `filtered` is not substituted for `closed`; scan states alone do not prove intrusion.
- TTL 61 does not identify Linux. Initial TTL and path assumptions remain explicit.
- A match percentage is not stated to be an independently calibrated probability.
- TCP-terminating front end A and application back end B can expose different identity clues. Mere NAT is not assumed to terminate TCP.
- `-O`, `-sV` and broader `-A` are distinguished; this lesson provides no external target scan instructions.
- Existing M03-05 service-version lesson is only bridged briefly, not replayed.
- Paired manuscripts preserve all example values (61/64/3, 443/65000), four questions, conditions and conclusions.
- Two diagrams are generated from the reviewed semantic model: evidence-check order and TCP endpoint relationship. Arrows describe the stated relation, not access or proven vulnerabilities. The same node text supports the searchable HTML alternative.

## Standards responsibility

Latest remote website AGENTS.md, docs/article-standards.md, docs/content-authoring.md, article-writing-template, diagram-design-system, publishing-security and perspectives/authoring were read before authoring. The website owns canonical rule IDs, full authoring worksheet, static checks and per-page release acceptance. WRITE-01–07 cover a single beginner question, terminology, evidence, bilingual agreement and source preservation; HTML-01–04 cover semantic direct body, answer-only collapse and local code scrolling; FIG-01–05 cover model/source/assets/description/readability; A11Y-01–03 require responsive, text scaling, focus and keyboard evidence. Actual executed results, pending checks and deployment provenance belong in the publication receipt, not inferred from this technical review.
