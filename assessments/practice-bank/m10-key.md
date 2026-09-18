# M10 — Denial of Service — instructor key v1.0.0

[Question form](m10.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M10-Q001

**Answer: C — Volumetric exhaustion**

Volumetric attacks attempt to saturate bandwidth or packet-processing capacity with excessive traffic.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Distributed denial of service:** A DDoS uses many sources to disrupt availability; distribution describes sources rather than a single exhaustion mechanism.
- **B — Application resource exhaustion:** Application-layer exhaustion makes the service spend disproportionate resources on requests or sessions.
- **D — Protocol-state exhaustion:** State-exhaustion attacks consume connection or protocol tracking resources, even without maximal bandwidth.

Coverage: M10; CEH v5 domain 4; Availability mechanisms.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q002

**Answer: D — Reflection**

Reflection sends replies from third-party services toward a victim, often by using a spoofed source address in requests.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Source-address validation:** Ingress or egress validation reduces spoofed source traffic when applied appropriately in the network.
- **B — Amplification:** Amplification produces responses substantially larger than the triggering requests.
- **C — Response rate limiting:** Response rate limiting constrains repeated or excessive replies, reducing some abusive response patterns.

Coverage: M10; CEH v5 domain 4; Reflection and amplification.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q003

**Answer: B — SYN cookies**

SYN cookies encode enough handshake state in a response so selected state need not be allocated until a valid acknowledgement arrives.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Connection-rate controls:** Rate controls constrain new connection creation according to an operational policy.
- **C — Capacity monitoring:** Monitoring tracks resource use and failure symptoms so the bottleneck and mitigation effects can be identified.
- **D — Upstream filtering:** Upstream filtering removes unwanted traffic before it consumes a constrained downstream link or service path.

Coverage: M10; CEH v5 domain 4; SYN-flood defenses.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q004

**Answer: A — Request cost limits**

Bound request complexity, body size or execution time so one request cannot consume unbounded work.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Caching:** Caching reuses suitable prior results to reduce repeated computation, while correctness and invalidation remain important.
- **C — Backpressure:** Backpressure limits accepted work or signals overload so downstream queues do not grow without bound.
- **D — Per-identity quotas:** Quotas allocate a bounded share of resources to a user or tenant; identity design affects how easily limits can be bypassed.

Coverage: M10; CEH v5 domain 4; Application resilience.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q005

**Answer: B — Baseline comparison**

Compare current traffic and resource behavior with a relevant normal baseline before classifying an anomaly.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Attack corroboration:** Use multiple indicators such as traffic patterns, request semantics and resource effects to support an attack conclusion.
- **C — Legitimate demand surge:** A large increase in genuine user demand can resemble an attack in volume while requiring different decisions.
- **D — Dependency failure:** An upstream or shared dependency can cause outage symptoms even when the application is not being attacked.

Coverage: M10; CEH v5 domain 4; Interpreting outages.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q006

**Answer: D — Bounded load testing**

Use an approved environment, rate, duration and stop condition to test capacity without uncontrolled disruption.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Incident coordination:** Coordinate service owners, network operators and responders because availability incidents can span multiple control points.
- **B — Rollback plan:** A rollback plan restores the prior configuration if a mitigation damages legitimate service.
- **C — Recovery verification:** Check legitimate user success and resource stability after mitigation rather than relying only on reduced attack traffic.

Coverage: M10; CEH v5 domain 4; Safe testing and recovery.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q007

**Answer: D — Protocol-state exhaustion**

State-exhaustion attacks consume connection or protocol tracking resources, even without maximal bandwidth.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Application resource exhaustion:** Application-layer exhaustion makes the service spend disproportionate resources on requests or sessions.
- **B — Distributed denial of service:** A DDoS uses many sources to disrupt availability; distribution describes sources rather than a single exhaustion mechanism.
- **C — Volumetric exhaustion:** Volumetric attacks attempt to saturate bandwidth or packet-processing capacity with excessive traffic.

Coverage: M10; CEH v5 domain 4; Availability mechanisms.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q008

**Answer: A — Amplification**

Amplification produces responses substantially larger than the triggering requests.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Reflection:** Reflection sends replies from third-party services toward a victim, often by using a spoofed source address in requests.
- **C — Source-address validation:** Ingress or egress validation reduces spoofed source traffic when applied appropriately in the network.
- **D — Response rate limiting:** Response rate limiting constrains repeated or excessive replies, reducing some abusive response patterns.

Coverage: M10; CEH v5 domain 4; Reflection and amplification.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q009

**Answer: A — Connection-rate controls**

Rate controls constrain new connection creation according to an operational policy.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — SYN cookies:** SYN cookies encode enough handshake state in a response so selected state need not be allocated until a valid acknowledgement arrives.
- **C — Upstream filtering:** Upstream filtering removes unwanted traffic before it consumes a constrained downstream link or service path.
- **D — Capacity monitoring:** Monitoring tracks resource use and failure symptoms so the bottleneck and mitigation effects can be identified.

Coverage: M10; CEH v5 domain 4; SYN-flood defenses.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q010

**Answer: C — Per-identity quotas**

Quotas allocate a bounded share of resources to a user or tenant; identity design affects how easily limits can be bypassed.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Backpressure:** Backpressure limits accepted work or signals overload so downstream queues do not grow without bound.
- **B — Request cost limits:** Bound request complexity, body size or execution time so one request cannot consume unbounded work.
- **D — Caching:** Caching reuses suitable prior results to reduce repeated computation, while correctness and invalidation remain important.

Coverage: M10; CEH v5 domain 4; Application resilience.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q011

**Answer: D — Dependency failure**

An upstream or shared dependency can cause outage symptoms even when the application is not being attacked.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Baseline comparison:** Compare current traffic and resource behavior with a relevant normal baseline before classifying an anomaly.
- **B — Attack corroboration:** Use multiple indicators such as traffic patterns, request semantics and resource effects to support an attack conclusion.
- **C — Legitimate demand surge:** A large increase in genuine user demand can resemble an attack in volume while requiring different decisions.

Coverage: M10; CEH v5 domain 4; Interpreting outages.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q012

**Answer: B — Rollback plan**

A rollback plan restores the prior configuration if a mitigation damages legitimate service.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Incident coordination:** Coordinate service owners, network operators and responders because availability incidents can span multiple control points.
- **C — Recovery verification:** Check legitimate user success and resource stability after mitigation rather than relying only on reduced attack traffic.
- **D — Bounded load testing:** Use an approved environment, rate, duration and stop condition to test capacity without uncontrolled disruption.

Coverage: M10; CEH v5 domain 4; Safe testing and recovery.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q013

**Answer: A — Application resource exhaustion**

Application-layer exhaustion makes the service spend disproportionate resources on requests or sessions.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Volumetric exhaustion:** Volumetric attacks attempt to saturate bandwidth or packet-processing capacity with excessive traffic.
- **C — Distributed denial of service:** A DDoS uses many sources to disrupt availability; distribution describes sources rather than a single exhaustion mechanism.
- **D — Protocol-state exhaustion:** State-exhaustion attacks consume connection or protocol tracking resources, even without maximal bandwidth.

Coverage: M10; CEH v5 domain 4; Availability mechanisms.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q014

**Answer: A — Source-address validation**

Ingress or egress validation reduces spoofed source traffic when applied appropriately in the network.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Amplification:** Amplification produces responses substantially larger than the triggering requests.
- **C — Reflection:** Reflection sends replies from third-party services toward a victim, often by using a spoofed source address in requests.
- **D — Response rate limiting:** Response rate limiting constrains repeated or excessive replies, reducing some abusive response patterns.

Coverage: M10; CEH v5 domain 4; Reflection and amplification.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q015

**Answer: C — Upstream filtering**

Upstream filtering removes unwanted traffic before it consumes a constrained downstream link or service path.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — SYN cookies:** SYN cookies encode enough handshake state in a response so selected state need not be allocated until a valid acknowledgement arrives.
- **B — Capacity monitoring:** Monitoring tracks resource use and failure symptoms so the bottleneck and mitigation effects can be identified.
- **D — Connection-rate controls:** Rate controls constrain new connection creation according to an operational policy.

Coverage: M10; CEH v5 domain 4; SYN-flood defenses.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q016

**Answer: B — Caching**

Caching reuses suitable prior results to reduce repeated computation, while correctness and invalidation remain important.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Backpressure:** Backpressure limits accepted work or signals overload so downstream queues do not grow without bound.
- **C — Per-identity quotas:** Quotas allocate a bounded share of resources to a user or tenant; identity design affects how easily limits can be bypassed.
- **D — Request cost limits:** Bound request complexity, body size or execution time so one request cannot consume unbounded work.

Coverage: M10; CEH v5 domain 4; Application resilience.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q017

**Answer: C — Legitimate demand surge**

A large increase in genuine user demand can resemble an attack in volume while requiring different decisions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Baseline comparison:** Compare current traffic and resource behavior with a relevant normal baseline before classifying an anomaly.
- **B — Dependency failure:** An upstream or shared dependency can cause outage symptoms even when the application is not being attacked.
- **D — Attack corroboration:** Use multiple indicators such as traffic patterns, request semantics and resource effects to support an attack conclusion.

Coverage: M10; CEH v5 domain 4; Interpreting outages.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q018

**Answer: A — Recovery verification**

Check legitimate user success and resource stability after mitigation rather than relying only on reduced attack traffic.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Rollback plan:** A rollback plan restores the prior configuration if a mitigation damages legitimate service.
- **C — Incident coordination:** Coordinate service owners, network operators and responders because availability incidents can span multiple control points.
- **D — Bounded load testing:** Use an approved environment, rate, duration and stop condition to test capacity without uncontrolled disruption.

Coverage: M10; CEH v5 domain 4; Safe testing and recovery.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q019

**Answer: B — Distributed denial of service**

A DDoS uses many sources to disrupt availability; distribution describes sources rather than a single exhaustion mechanism.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Protocol-state exhaustion:** State-exhaustion attacks consume connection or protocol tracking resources, even without maximal bandwidth.
- **C — Volumetric exhaustion:** Volumetric attacks attempt to saturate bandwidth or packet-processing capacity with excessive traffic.
- **D — Application resource exhaustion:** Application-layer exhaustion makes the service spend disproportionate resources on requests or sessions.

Coverage: M10; CEH v5 domain 4; Availability mechanisms.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q020

**Answer: D — Response rate limiting**

Response rate limiting constrains repeated or excessive replies, reducing some abusive response patterns.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Amplification:** Amplification produces responses substantially larger than the triggering requests.
- **B — Source-address validation:** Ingress or egress validation reduces spoofed source traffic when applied appropriately in the network.
- **C — Reflection:** Reflection sends replies from third-party services toward a victim, often by using a spoofed source address in requests.

Coverage: M10; CEH v5 domain 4; Reflection and amplification.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q021

**Answer: B — Capacity monitoring**

Monitoring tracks resource use and failure symptoms so the bottleneck and mitigation effects can be identified.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — SYN cookies:** SYN cookies encode enough handshake state in a response so selected state need not be allocated until a valid acknowledgement arrives.
- **C — Connection-rate controls:** Rate controls constrain new connection creation according to an operational policy.
- **D — Upstream filtering:** Upstream filtering removes unwanted traffic before it consumes a constrained downstream link or service path.

Coverage: M10; CEH v5 domain 4; SYN-flood defenses.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q022

**Answer: C — Backpressure**

Backpressure limits accepted work or signals overload so downstream queues do not grow without bound.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Caching:** Caching reuses suitable prior results to reduce repeated computation, while correctness and invalidation remain important.
- **B — Request cost limits:** Bound request complexity, body size or execution time so one request cannot consume unbounded work.
- **D — Per-identity quotas:** Quotas allocate a bounded share of resources to a user or tenant; identity design affects how easily limits can be bypassed.

Coverage: M10; CEH v5 domain 4; Application resilience.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q023

**Answer: D — Attack corroboration**

Use multiple indicators such as traffic patterns, request semantics and resource effects to support an attack conclusion.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Baseline comparison:** Compare current traffic and resource behavior with a relevant normal baseline before classifying an anomaly.
- **B — Legitimate demand surge:** A large increase in genuine user demand can resemble an attack in volume while requiring different decisions.
- **C — Dependency failure:** An upstream or shared dependency can cause outage symptoms even when the application is not being attacked.

Coverage: M10; CEH v5 domain 4; Interpreting outages.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q024

**Answer: B — Incident coordination**

Coordinate service owners, network operators and responders because availability incidents can span multiple control points.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Rollback plan:** A rollback plan restores the prior configuration if a mitigation damages legitimate service.
- **C — Bounded load testing:** Use an approved environment, rate, duration and stop condition to test capacity without uncontrolled disruption.
- **D — Recovery verification:** Check legitimate user success and resource stability after mitigation rather than relying only on reduced attack traffic.

Coverage: M10; CEH v5 domain 4; Safe testing and recovery.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q025

**Answer: C — Application resource exhaustion**

Application-layer exhaustion makes the service spend disproportionate resources on requests or sessions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Volumetric exhaustion:** Volumetric attacks attempt to saturate bandwidth or packet-processing capacity with excessive traffic.
- **B — Protocol-state exhaustion:** State-exhaustion attacks consume connection or protocol tracking resources, even without maximal bandwidth.
- **D — Distributed denial of service:** A DDoS uses many sources to disrupt availability; distribution describes sources rather than a single exhaustion mechanism.

Coverage: M10; CEH v5 domain 4; Availability mechanisms.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q026

**Answer: B — Amplification**

Amplification produces responses substantially larger than the triggering requests.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Response rate limiting:** Response rate limiting constrains repeated or excessive replies, reducing some abusive response patterns.
- **C — Source-address validation:** Ingress or egress validation reduces spoofed source traffic when applied appropriately in the network.
- **D — Reflection:** Reflection sends replies from third-party services toward a victim, often by using a spoofed source address in requests.

Coverage: M10; CEH v5 domain 4; Reflection and amplification.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q027

**Answer: A — SYN cookies**

SYN cookies encode enough handshake state in a response so selected state need not be allocated until a valid acknowledgement arrives.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Upstream filtering:** Upstream filtering removes unwanted traffic before it consumes a constrained downstream link or service path.
- **C — Capacity monitoring:** Monitoring tracks resource use and failure symptoms so the bottleneck and mitigation effects can be identified.
- **D — Connection-rate controls:** Rate controls constrain new connection creation according to an operational policy.

Coverage: M10; CEH v5 domain 4; SYN-flood defenses.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q028

**Answer: A — Request cost limits**

Bound request complexity, body size or execution time so one request cannot consume unbounded work.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Per-identity quotas:** Quotas allocate a bounded share of resources to a user or tenant; identity design affects how easily limits can be bypassed.
- **C — Caching:** Caching reuses suitable prior results to reduce repeated computation, while correctness and invalidation remain important.
- **D — Backpressure:** Backpressure limits accepted work or signals overload so downstream queues do not grow without bound.

Coverage: M10; CEH v5 domain 4; Application resilience.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q029

**Answer: D — Dependency failure**

An upstream or shared dependency can cause outage symptoms even when the application is not being attacked.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Baseline comparison:** Compare current traffic and resource behavior with a relevant normal baseline before classifying an anomaly.
- **B — Legitimate demand surge:** A large increase in genuine user demand can resemble an attack in volume while requiring different decisions.
- **C — Attack corroboration:** Use multiple indicators such as traffic patterns, request semantics and resource effects to support an attack conclusion.

Coverage: M10; CEH v5 domain 4; Interpreting outages.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-M10-Q030

**Answer: C — Bounded load testing**

Use an approved environment, rate, duration and stop condition to test capacity without uncontrolled disruption.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Incident coordination:** Coordinate service owners, network operators and responders because availability incidents can span multiple control points.
- **B — Recovery verification:** Check legitimate user success and resource stability after mitigation rather than relying only on reduced attack traffic.
- **D — Rollback plan:** A rollback plan restores the prior configuration if a mitigation damages legitimate service.

Coverage: M10; CEH v5 domain 4; Safe testing and recovery.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)
