# M12 — IDS Firewalls and Honeypots — instructor key v1.0.0

[Question form](m12.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M12-Q001

**Answer: C — IDS**

An intrusion detection system observes activity and generates detections; a passive deployment does not directly block traffic.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — IPS:** An intrusion prevention system can inspect and block traffic in its enforcement path.
- **B — Honeypot:** A honeypot is a deliberately observed decoy resource used to learn about or detect interactions.
- **D — Firewall:** A firewall enforces traffic policy at its supported layers; permitted traffic is not automatically safe application behavior.

Coverage: M12; CEH v5 domain 4; Security device roles.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q002

**Answer: D — Encryption visibility gap**

An observer without decryption access may see metadata but cannot inspect protected application payloads directly.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Fragmentation and reassembly difference:** Different interpretations of fragments or streams can create disagreement between an inspection device and the endpoint.
- **B — Protocol ambiguity:** Parser differences or unexpected protocol use can make different components interpret the same traffic differently.
- **C — Encoding normalization:** Security checks need a consistent decoded representation so alternate encodings do not bypass matching while reaching the same application meaning.

Coverage: M12; CEH v5 domain 4; Inspection challenges.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q003

**Answer: B — False-positive reduction**

Reduce incorrect alerts using validated context and careful rule tuning rather than suppressing all visibility.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Baseline-aware detection:** Interpret anomalies relative to relevant normal behavior while recognizing that a baseline can itself include unwanted activity.
- **C — False-negative reduction:** Improve coverage for real events that current detections miss, using appropriate telemetry and validation.
- **D — Layered detection:** Combine complementary signals so one visibility limitation does not determine the whole conclusion.

Coverage: M12; CEH v5 domain 4; Detection tuning.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q004

**Answer: A — Default deny**

Default deny rejects traffic unless an explicit policy permits it.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Least-necessary rules:** Rules should permit only the source, destination, service and conditions required for the business purpose.
- **C — Rule review and expiry:** Review ownership and continued need, and expire temporary exceptions to prevent stale access paths.
- **D — Egress filtering:** Egress filtering controls outbound connections and can reduce unnecessary external communication paths.

Coverage: M12; CEH v5 domain 4; Firewall policy.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q005

**Answer: B — Decoy interaction evidence**

Interaction with a decoy is an observation that needs context; it is not automatic proof of a particular actor or full compromise.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Realism tradeoff:** A more realistic decoy may collect richer behavior but can require more containment and maintenance.
- **C — Detection of deception:** Unrealistic banners, inconsistent behavior or known artifacts can reveal that a resource is a decoy.
- **D — Isolation of the decoy:** Constrain a decoy so it cannot become an uncontrolled path into production or harm other systems.

Coverage: M12; CEH v5 domain 4; Decoy limitations.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q006

**Answer: D — Replay sanitized fixtures**

Use approved recorded or synthetic data to check a detection without creating harmful live traffic.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Measure legitimate impact:** Check latency, errors and valid-user success so a blocking rule does not silently damage normal operation.
- **B — Preserve rollback and ownership:** A control change needs an accountable owner and a practical reversal path when its effects are unacceptable.
- **C — Compare expected and observed alerts:** A detection test needs a declared expected outcome and an actual observation to establish coverage.

Coverage: M12; CEH v5 domain 4; Safe validation.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q007

**Answer: C — IPS**

An intrusion prevention system can inspect and block traffic in its enforcement path.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Firewall:** A firewall enforces traffic policy at its supported layers; permitted traffic is not automatically safe application behavior.
- **B — Honeypot:** A honeypot is a deliberately observed decoy resource used to learn about or detect interactions.
- **D — IDS:** An intrusion detection system observes activity and generates detections; a passive deployment does not directly block traffic.

Coverage: M12; CEH v5 domain 4; Security device roles.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q008

**Answer: B — Fragmentation and reassembly difference**

Different interpretations of fragments or streams can create disagreement between an inspection device and the endpoint.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Protocol ambiguity:** Parser differences or unexpected protocol use can make different components interpret the same traffic differently.
- **C — Encryption visibility gap:** An observer without decryption access may see metadata but cannot inspect protected application payloads directly.
- **D — Encoding normalization:** Security checks need a consistent decoded representation so alternate encodings do not bypass matching while reaching the same application meaning.

Coverage: M12; CEH v5 domain 4; Inspection challenges.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q009

**Answer: A — False-negative reduction**

Improve coverage for real events that current detections miss, using appropriate telemetry and validation.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Layered detection:** Combine complementary signals so one visibility limitation does not determine the whole conclusion.
- **C — False-positive reduction:** Reduce incorrect alerts using validated context and careful rule tuning rather than suppressing all visibility.
- **D — Baseline-aware detection:** Interpret anomalies relative to relevant normal behavior while recognizing that a baseline can itself include unwanted activity.

Coverage: M12; CEH v5 domain 4; Detection tuning.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q010

**Answer: C — Least-necessary rules**

Rules should permit only the source, destination, service and conditions required for the business purpose.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Rule review and expiry:** Review ownership and continued need, and expire temporary exceptions to prevent stale access paths.
- **B — Default deny:** Default deny rejects traffic unless an explicit policy permits it.
- **D — Egress filtering:** Egress filtering controls outbound connections and can reduce unnecessary external communication paths.

Coverage: M12; CEH v5 domain 4; Firewall policy.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q011

**Answer: A — Isolation of the decoy**

Constrain a decoy so it cannot become an uncontrolled path into production or harm other systems.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Realism tradeoff:** A more realistic decoy may collect richer behavior but can require more containment and maintenance.
- **C — Decoy interaction evidence:** Interaction with a decoy is an observation that needs context; it is not automatic proof of a particular actor or full compromise.
- **D — Detection of deception:** Unrealistic banners, inconsistent behavior or known artifacts can reveal that a resource is a decoy.

Coverage: M12; CEH v5 domain 4; Decoy limitations.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q012

**Answer: A — Compare expected and observed alerts**

A detection test needs a declared expected outcome and an actual observation to establish coverage.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Preserve rollback and ownership:** A control change needs an accountable owner and a practical reversal path when its effects are unacceptable.
- **C — Replay sanitized fixtures:** Use approved recorded or synthetic data to check a detection without creating harmful live traffic.
- **D — Measure legitimate impact:** Check latency, errors and valid-user success so a blocking rule does not silently damage normal operation.

Coverage: M12; CEH v5 domain 4; Safe validation.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q013

**Answer: C — Firewall**

A firewall enforces traffic policy at its supported layers; permitted traffic is not automatically safe application behavior.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — IDS:** An intrusion detection system observes activity and generates detections; a passive deployment does not directly block traffic.
- **B — Honeypot:** A honeypot is a deliberately observed decoy resource used to learn about or detect interactions.
- **D — IPS:** An intrusion prevention system can inspect and block traffic in its enforcement path.

Coverage: M12; CEH v5 domain 4; Security device roles.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q014

**Answer: B — Encoding normalization**

Security checks need a consistent decoded representation so alternate encodings do not bypass matching while reaching the same application meaning.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Protocol ambiguity:** Parser differences or unexpected protocol use can make different components interpret the same traffic differently.
- **C — Encryption visibility gap:** An observer without decryption access may see metadata but cannot inspect protected application payloads directly.
- **D — Fragmentation and reassembly difference:** Different interpretations of fragments or streams can create disagreement between an inspection device and the endpoint.

Coverage: M12; CEH v5 domain 4; Inspection challenges.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q015

**Answer: C — Baseline-aware detection**

Interpret anomalies relative to relevant normal behavior while recognizing that a baseline can itself include unwanted activity.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — False-negative reduction:** Improve coverage for real events that current detections miss, using appropriate telemetry and validation.
- **B — False-positive reduction:** Reduce incorrect alerts using validated context and careful rule tuning rather than suppressing all visibility.
- **D — Layered detection:** Combine complementary signals so one visibility limitation does not determine the whole conclusion.

Coverage: M12; CEH v5 domain 4; Detection tuning.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q016

**Answer: D — Egress filtering**

Egress filtering controls outbound connections and can reduce unnecessary external communication paths.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Default deny:** Default deny rejects traffic unless an explicit policy permits it.
- **B — Least-necessary rules:** Rules should permit only the source, destination, service and conditions required for the business purpose.
- **C — Rule review and expiry:** Review ownership and continued need, and expire temporary exceptions to prevent stale access paths.

Coverage: M12; CEH v5 domain 4; Firewall policy.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q017

**Answer: B — Realism tradeoff**

A more realistic decoy may collect richer behavior but can require more containment and maintenance.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Decoy interaction evidence:** Interaction with a decoy is an observation that needs context; it is not automatic proof of a particular actor or full compromise.
- **C — Detection of deception:** Unrealistic banners, inconsistent behavior or known artifacts can reveal that a resource is a decoy.
- **D — Isolation of the decoy:** Constrain a decoy so it cannot become an uncontrolled path into production or harm other systems.

Coverage: M12; CEH v5 domain 4; Decoy limitations.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q018

**Answer: C — Measure legitimate impact**

Check latency, errors and valid-user success so a blocking rule does not silently damage normal operation.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Preserve rollback and ownership:** A control change needs an accountable owner and a practical reversal path when its effects are unacceptable.
- **B — Replay sanitized fixtures:** Use approved recorded or synthetic data to check a detection without creating harmful live traffic.
- **D — Compare expected and observed alerts:** A detection test needs a declared expected outcome and an actual observation to establish coverage.

Coverage: M12; CEH v5 domain 4; Safe validation.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q019

**Answer: D — Honeypot**

A honeypot is a deliberately observed decoy resource used to learn about or detect interactions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Firewall:** A firewall enforces traffic policy at its supported layers; permitted traffic is not automatically safe application behavior.
- **B — IDS:** An intrusion detection system observes activity and generates detections; a passive deployment does not directly block traffic.
- **C — IPS:** An intrusion prevention system can inspect and block traffic in its enforcement path.

Coverage: M12; CEH v5 domain 4; Security device roles.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q020

**Answer: D — Protocol ambiguity**

Parser differences or unexpected protocol use can make different components interpret the same traffic differently.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Encryption visibility gap:** An observer without decryption access may see metadata but cannot inspect protected application payloads directly.
- **B — Fragmentation and reassembly difference:** Different interpretations of fragments or streams can create disagreement between an inspection device and the endpoint.
- **C — Encoding normalization:** Security checks need a consistent decoded representation so alternate encodings do not bypass matching while reaching the same application meaning.

Coverage: M12; CEH v5 domain 4; Inspection challenges.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q021

**Answer: A — Layered detection**

Combine complementary signals so one visibility limitation does not determine the whole conclusion.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Baseline-aware detection:** Interpret anomalies relative to relevant normal behavior while recognizing that a baseline can itself include unwanted activity.
- **C — False-positive reduction:** Reduce incorrect alerts using validated context and careful rule tuning rather than suppressing all visibility.
- **D — False-negative reduction:** Improve coverage for real events that current detections miss, using appropriate telemetry and validation.

Coverage: M12; CEH v5 domain 4; Detection tuning.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q022

**Answer: D — Rule review and expiry**

Review ownership and continued need, and expire temporary exceptions to prevent stale access paths.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Least-necessary rules:** Rules should permit only the source, destination, service and conditions required for the business purpose.
- **B — Default deny:** Default deny rejects traffic unless an explicit policy permits it.
- **C — Egress filtering:** Egress filtering controls outbound connections and can reduce unnecessary external communication paths.

Coverage: M12; CEH v5 domain 4; Firewall policy.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q023

**Answer: B — Detection of deception**

Unrealistic banners, inconsistent behavior or known artifacts can reveal that a resource is a decoy.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Isolation of the decoy:** Constrain a decoy so it cannot become an uncontrolled path into production or harm other systems.
- **C — Realism tradeoff:** A more realistic decoy may collect richer behavior but can require more containment and maintenance.
- **D — Decoy interaction evidence:** Interaction with a decoy is an observation that needs context; it is not automatic proof of a particular actor or full compromise.

Coverage: M12; CEH v5 domain 4; Decoy limitations.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q024

**Answer: A — Preserve rollback and ownership**

A control change needs an accountable owner and a practical reversal path when its effects are unacceptable.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Replay sanitized fixtures:** Use approved recorded or synthetic data to check a detection without creating harmful live traffic.
- **C — Compare expected and observed alerts:** A detection test needs a declared expected outcome and an actual observation to establish coverage.
- **D — Measure legitimate impact:** Check latency, errors and valid-user success so a blocking rule does not silently damage normal operation.

Coverage: M12; CEH v5 domain 4; Safe validation.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q025

**Answer: C — IDS**

An intrusion detection system observes activity and generates detections; a passive deployment does not directly block traffic.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Honeypot:** A honeypot is a deliberately observed decoy resource used to learn about or detect interactions.
- **B — IPS:** An intrusion prevention system can inspect and block traffic in its enforcement path.
- **D — Firewall:** A firewall enforces traffic policy at its supported layers; permitted traffic is not automatically safe application behavior.

Coverage: M12; CEH v5 domain 4; Security device roles.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q026

**Answer: D — Encryption visibility gap**

An observer without decryption access may see metadata but cannot inspect protected application payloads directly.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Protocol ambiguity:** Parser differences or unexpected protocol use can make different components interpret the same traffic differently.
- **B — Encoding normalization:** Security checks need a consistent decoded representation so alternate encodings do not bypass matching while reaching the same application meaning.
- **C — Fragmentation and reassembly difference:** Different interpretations of fragments or streams can create disagreement between an inspection device and the endpoint.

Coverage: M12; CEH v5 domain 4; Inspection challenges.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q027

**Answer: A — False-positive reduction**

Reduce incorrect alerts using validated context and careful rule tuning rather than suppressing all visibility.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Layered detection:** Combine complementary signals so one visibility limitation does not determine the whole conclusion.
- **C — Baseline-aware detection:** Interpret anomalies relative to relevant normal behavior while recognizing that a baseline can itself include unwanted activity.
- **D — False-negative reduction:** Improve coverage for real events that current detections miss, using appropriate telemetry and validation.

Coverage: M12; CEH v5 domain 4; Detection tuning.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q028

**Answer: D — Least-necessary rules**

Rules should permit only the source, destination, service and conditions required for the business purpose.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Egress filtering:** Egress filtering controls outbound connections and can reduce unnecessary external communication paths.
- **B — Rule review and expiry:** Review ownership and continued need, and expire temporary exceptions to prevent stale access paths.
- **C — Default deny:** Default deny rejects traffic unless an explicit policy permits it.

Coverage: M12; CEH v5 domain 4; Firewall policy.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q029

**Answer: B — Isolation of the decoy**

Constrain a decoy so it cannot become an uncontrolled path into production or harm other systems.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Decoy interaction evidence:** Interaction with a decoy is an observation that needs context; it is not automatic proof of a particular actor or full compromise.
- **C — Detection of deception:** Unrealistic banners, inconsistent behavior or known artifacts can reveal that a resource is a decoy.
- **D — Realism tradeoff:** A more realistic decoy may collect richer behavior but can require more containment and maintenance.

Coverage: M12; CEH v5 domain 4; Decoy limitations.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-M12-Q030

**Answer: C — Compare expected and observed alerts**

A detection test needs a declared expected outcome and an actual observation to establish coverage.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Measure legitimate impact:** Check latency, errors and valid-user success so a blocking rule does not silently damage normal operation.
- **B — Preserve rollback and ownership:** A control change needs an accountable owner and a practical reversal path when its effects are unacceptable.
- **D — Replay sanitized fixtures:** Use approved recorded or synthetic data to check a detection without creating harmful live traffic.

Coverage: M12; CEH v5 domain 4; Safe validation.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)
