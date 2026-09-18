# CEHP — 25 bounded practical tasks

[Bank](README.md) · [Local runner](lab.py) · [Shared synthetic input](fixtures.json)

These are original local exercises, not actual exam tasks. P1–P5 follow the UUU review families and map to the broader Practical blueprint. Complete at least one executed and accepted task in each family for the first-pass goal; T01 in each family is the default starter. A written design alone is supplementary; each accepted task needs its declared local run, calculation or implemented check.

## Setup and evidence

Use Python 3 standard library. The runner creates only its own short-lived loopback services for P1/P2; P3/P4 are offline, and P5 uses an in-memory database. It takes no external target argument and does not install tools, activate codes or modify cloud resources. If loopback sockets are unavailable, record the exact blocker or use an already authorized course lab; supplied output does not establish your execution.

From the CEH repository root run `python3 assessments/practice-bank/lab.py p1` (replace p1 with the required family). Save your own command, output, interpretation, time if known and acceptance check in a dated attempt. Do not reuse the instructor self-test as learner output. Official Nmap/Wireshark or range proficiency remains a separate later check; these fixtures establish only their declared small skills.

## P1 — Network and vulnerability scanning

### CEHP26-P1-T01 — Loopback port evidence

Scope: M03 / Practical D02. Version: 1.0.0. Input: `lab.py p1` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Run p1 and save both probe rows. Interpret the listening and non-listening controls, transport, observation time and scope. Explain why the result says nothing about other hosts.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P1-T02 — Finding triage

Scope: M05 / Practical D03. Version: 1.0.0. Input: `lab.py p1` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Using p1 findings, rank F1, F2 and F3 for investigation. Separate the confirmed backport, public exposure, known exploitation and business data sensitivity. Produce one next verification per finding.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P1-T03 — Scope membership

Scope: M01 M03 / Practical D01 D02. Version: 1.0.0. Input: `lab.py p1` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Use Python ipaddress to evaluate 127.0.0.1 and 192.0.2.10 against the supplied allowed network. Preserve the result and explain why address membership alone does not authorize a method.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P1-T04 — Transport and vantage record

Scope: M03 / Practical D02. Version: 1.0.0. Input: `lab.py p1` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Turn your actual p1 result into two inventory rows containing host, port, transport, local vantage, time and observed state. Add explicit unknown fields for software version and UDP state.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P1-T05 — Cloud finding repair proposal

Scope: M19 / Practical D08. Version: 1.0.0. Input: `lab.py p1` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Read the synthetic cloud_policy in p1. Write a restricted JSON replacement for a named reporting role and a small local Python permission predicate. Run one allowed reporting-role read and one denied anonymous read; save code, policy and output. Do not connect to a cloud account.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

## P2 — Service identification and enumeration

### CEHP26-P2-T01 — Local service enumeration

Scope: M03 M04 M13 / Practical D02. Version: 1.0.0. Input: `lab.py p2` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Run p2. Save the observed Server header and the two route statuses. Distinguish service evidence from a banner-only operating-system or vulnerability claim.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P2-T02 — Permission matrix

Scope: M04 / Practical D02. Version: 1.0.0. Input: `lab.py p2` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Use the permissions fixture to compute the objects alice can read and write. Save your query or script plus output and identify one negative access test.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P2-T03 — DNS dependency review

Scope: M02 M04 / Practical D02. Version: 1.0.0. Input: `lab.py p2` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Parse the DNS fixture by type. Identify the service address, mail destination and retired alias. Write one verification step before calling the alias exploitable.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P2-T04 — Mobile least privilege

Scope: M17 / Practical D07. Version: 1.0.0. Input: `lab.py p2` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Compute granted minus required capabilities in the mobile_profile fixture. Save the calculation and a proposed reduced permission set.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P2-T05 — Enumeration custody

Scope: M01 M04 / Practical D01 D02. Version: 1.0.0. Input: `lab.py p2` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Create a short redacted report from your p2 output containing service, allowed/denied behavior and unknowns. Keep only synthetic data; state source, method and scope.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

## P3 — Network traffic analysis

### CEHP26-P3-T01 — Flow reconstruction

Scope: M08 / Practical D04. Version: 1.0.0. Input: `lab.py p3` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Run p3 and use Python to total the supplied flow bytes and reconstruct DNS lookup, TCP handshake, protected exchange and close. Preserve your computation and result.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P3-T02 — Encrypted visibility

Scope: M08 M11 / Practical D04. Version: 1.0.0. Input: `lab.py p3` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Filter the flows to TLS and compute directional byte totals. State exactly which content claims the fixture cannot support.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P3-T03 — Wireless identity comparison

Scope: M16 / Practical D06. Version: 1.0.0. Input: `lab.py p3` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Compare the wireless fixture by SSID, BSSID, channel and approved flag. Save the unexpected identifier and a bounded investigation question.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P3-T04 — IoT replay filter

Scope: M18 / Practical D07. Version: 1.0.0. Input: `lab.py p3` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Process iot_messages in order, accepting only validly signed messages with a sequence greater than the last accepted sequence. Save accepted and rejected indices.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P3-T05 — Detection sanity check

Scope: M08 M10 / Practical D04. Version: 1.0.0. Input: `lab.py p3` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Write a small detector for a repeated IoT sequence, then test it with the supplied sequence and a fresh monotonic sequence. Preserve both outputs and a false-positive limitation.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

## P4 — System attack analysis

### CEHP26-P4-T01 — Benign artifact comparison

Scope: M06 M07 / Practical D03. Version: 1.0.0. Input: `lab.py p4` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Run p4 and compare the two content hashes. Correlate the synthetic process events and identify the unauthorized startup action without calling the benign fixture live malware.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P4-T02 — Host least privilege

Scope: M06 / Practical D03. Version: 1.0.0. Input: `lab.py p4` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Compute web-worker permissions not present in required. Produce a reduced set and one negative test expectation.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P4-T03 — Response ordering

Scope: M07 / Practical D03. Version: 1.0.0. Input: `lab.py p4` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Using p4 events, write a synthetic response sequence and a small Python ordering check: when immediate physical safety is not at risk, preserve needed volatile evidence before a reboot/rebuild, and verify service before declaring recovery. Run the check on a correctly ordered sequence and on one that rebuilds too early. Save both outputs and state the safety exception.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P4-T04 — Integrity versus authenticity

Scope: M20 / Practical D09. Version: 1.0.0. Input: `lab.py p4` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Use hashlib on two locally constructed benign byte strings and save their digests. Explain what changes if an attacker can also replace the expected digest.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P4-T05 — Detection with a benign control

Scope: M07 M12 / Practical D03 D04. Version: 1.0.0. Input: `lab.py p4` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Write a predicate for unapproved startup events and evaluate all process_events. Keep the approved backup event as a benign control.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

## P5 — Website attack analysis

### CEHP26-P5-T01 — SQL data/syntax boundary

Scope: M15 / Practical D05. Version: 1.0.0. Input: `lab.py p5` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Run p5. Compare unsafe, parameterized and normal-alice results. Explain the root cause and why valid input still needs a regression check.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P5-T02 — Object authorization predicate

Scope: M14 / Practical D05. Version: 1.0.0. Input: `lab.py p5` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Implement an owner-equals-actor decision over web_cases. Save expected allow/deny decisions and compare them with observed_status.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P5-T03 — Session lifecycle review

Scope: M11 / Practical D04. Version: 1.0.0. Input: `lab.py p5` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Read the session fixture. Implement a local Python session-state model that rotates the identifier on login and invalidates it on logout. Run checks for old-ID rejection after rotation, new-ID acceptance before logout and rejection after logout; save code/output and distinguish this model from a deployed service.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P5-T04 — Safe upload design

Scope: M13 M14 / Practical D05. Version: 1.0.0. Input: `lab.py p5` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Implement a local upload-admission function for this toy contract: owner must match, filename must be a plain basename ending in .txt, content must decode as UTF-8 and be at most 1024 bytes. Test a valid note, a traversal filename, an oversized body and a wrong owner. Save code and decisions; if writing a file, use only a temporary directory with no execution handler. Explain why this limited model is not a complete production upload defense.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.

### CEHP26-P5-T05 — Combined regression

Scope: M14 M15 / Practical D05. Version: 1.0.0. Input: `lab.py p5` / `fixtures.json`. First block: at most 25 minutes; continue only after confirming capacity.

Run p5 and your object-authorization predicate again. Save a check that confirms safe SQL literal handling, normal alice access and denial of the cross-owner case.

Save: actual command/code and any supporting design; observed result; explanation; declared check; pending question. State: planned / attempted / blocked / accepted.
