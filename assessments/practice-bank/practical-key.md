# CEHP — instructor acceptance key

[Tasks](practical.md) · [Current readiness boundaries](../../study-plan/uuu-aligned-ceh-cehp-2026-09-18.md)

Review actual learner evidence. Prepared instructions, an instructor run or a written proposal are not learner-executed acceptance. The criteria below establish only the named local skill. A task with unmet prerequisites remains blocked; formal exam readiness is separate.

## P1 — Network and vulnerability scanning

### CEHP26-P1-T01 — Loopback port evidence

Both addresses are 127.0.0.1; ports are runtime-assigned; first connect code is zero and second is nonzero. Explain reachable listener versus the local closed control. Do not substitute a supplied sample for your run.

### CEHP26-P1-T02 — Finding triage

F1 has exposure and exploitation evidence; F3 has confidential public access needing prompt action; F2 needs its verified backport recorded rather than automatically called vulnerable. A justified F1/F3 order is accepted; no invented numeric business loss.

### CEHP26-P1-T03 — Scope membership

127.0.0.1 is inside 127.0.0.0/8 and 192.0.2.10 is outside. Permission remains limited to the script-created service; do not send probes to the documentation address.

### CEHP26-P1-T04 — Transport and vantage record

Two actual TCP rows, with UDP and software version unknown. A successful TCP connection does not establish authenticated service identity, vulnerability or another vantage.

### CEHP26-P1-T05 — Cloud finding repair proposal

Replace the wildcard with an explicit illustrative reporting role and retain only the needed read action/resource. The learner's executed predicate must allow that role and deny anonymous reads. This proves the declared local policy checks, not cloud deployment or provider enforcement.

## P2 — Service identification and enumeration

### CEHP26-P2-T01 — Local service enumeration

Actual /status is 200 and /admin is 403, with TrainingGateway in the banner. HTTP is directly exercised; a claimed OS/version exploit is unsupported. The script closes its own server.

### CEHP26-P2-T02 — Permission matrix

alice can read alice-report and cannot write either listed object; payroll read is denied. Preserve computation and a negative case; the fixture is not an enterprise directory.

### CEHP26-P2-T03 — DNS dependency review

A points to 192.0.2.10; MX points to mail.example.test; legacy CNAME references retired.vendor.example.test. Check vendor resource state and ownership before claiming takeover; perform no external request.

### CEHP26-P2-T04 — Mobile least privilege

contacts and location are excess for the stated model-only inventory task. Proposed set is device-model. This validates a synthetic permission comparison, not an installed phone app.

### CEHP26-P2-T05 — Enumeration custody

Report includes direct observations, private/sensitive-output handling, scope and unknown operating-system identity. Do not treat 403 as proof of every underlying policy or permission state.

## P3 — Network traffic analysis

### CEHP26-P3-T01 — Flow reconstruction

Total is 2620 bytes. Events 1–2 DNS, 3–5 handshake, 6–7 encrypted exchange, 8 FIN ACK. The fixture omits a complete close exchange; no application transaction success is proved.

### CEHP26-P3-T02 — Encrypted visibility

Client-to-server TLS is 900 bytes and server-to-client TLS is 1300. Plaintext, credential theft and specific application commands remain unknown; metadata is not content.

### CEHP26-P3-T03 — Wireless identity comparison

Same SSID, different BSSIDs and channels; 02:00:00:00:00:02 is unapproved in the fixture. This is an inventory anomaly, not proof of a malicious operator. Do not transmit wireless traffic.

### CEHP26-P3-T04 — IoT replay filter

Accept indices 0 and 1 (sequences 10 and 11); reject index 2 (sequence 10). Signature validity alone does not establish freshness. Initial sequence/state policy is declared for this synthetic case.

### CEHP26-P3-T05 — Detection sanity check

The supplied 10,11,10 sequence flags the third event; 10,11,12 does not. Explain legitimate retransmission/context and why this toy rule is not a production attack verdict.

## P4 — System attack analysis

### CEHP26-P4-T01 — Benign artifact comparison

Hashes differ; time 2 adds unapproved startup behavior and time 3 contacts an unapproved endpoint. Hash mismatch proves different content, not intent. Save your actual run and interpretation.

### CEHP26-P4-T02 — Host least privilege

modify-system-config is excess; retain read-static and write-upload. A negative test should deny system-configuration modification while preserving required operations.

### CEHP26-P4-T03 — Response ordering

The implemented ordering check accepts the evidence-before-rebuild and verify-before-recovery sequence, and rejects the early-rebuild case. Explain that immediate physical/operational safety can require a different containment decision. This is a synthetic procedure check, not actual incident-response completion.

### CEHP26-P4-T04 — Integrity versus authenticity

Different content produces different observed digests in this exercise. An attacker-controlled expected digest cannot authenticate origin; a trusted manifest/signature or MAC with protected key provides a separate trust route.

### CEHP26-P4-T05 — Detection with a benign control

Flag only time 2 for the stated predicate; time 3 may be separately suspicious but is not a startup event. The approved backup remains unflagged. Save code/output; do not claim complete malware detection.

## P5 — Website attack analysis

### CEHP26-P5-T01 — SQL data/syntax boundary

Unsafe returns IDs 1 and 2; bound malicious-looking literal returns none; normal alice returns 1. Parameter binding preserves the syntax/data boundary. The database is synthetic and in memory.

### CEHP26-P5-T02 — Object authorization predicate

First and third cases should allow; second should deny despite observed 200. Authentication alone does not enforce object ownership. Keep both allowed cases in the regression.

### CEHP26-P5-T03 — Session lifecycle review

Identify the unchanged login ID and the usable logged-out session. The learner's local model must reject the old ID after rotation, accept the fresh ID before logout, then reject it after logout. Preserve code and all three results; the model does not establish a deployed web service's security.

### CEHP26-P5-T04 — Safe upload design

The toy function accepts the authorized small UTF-8 .txt note and rejects the traversal name, oversized content and wrong owner. Save the implemented checks and executed cases. Extension alone is insufficient, and the toy contract does not address every production upload risk such as active-content handling, races or malware inspection.

### CEHP26-P5-T05 — Combined regression

Require parameterized_ids empty, normal_alice_ids [1], and computed cross-owner deny. The original unsafe path intentionally remains demonstrable; do not claim this teaching fixture is production-hardened.
