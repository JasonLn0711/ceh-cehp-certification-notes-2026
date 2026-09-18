# M03 — Scanning Networks — instructor key v1.0.0

[Question form](m03.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M03-Q001

**Answer: B — Open**

An open port has a service accepting the relevant transport connections or datagrams from the scanner's perspective.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Filtered:** Filtering prevents the scanner from determining whether a port is open or closed.
- **C — Open or filtered:** The probe outcome cannot distinguish an open port from one whose traffic is silently filtered.
- **D — Closed:** A closed port is reachable but has no service listening for the tested transport at that time.

Coverage: M03; CEH v5 domain 2; Port states.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q002

**Answer: D — TCP SYN scan**

A SYN scan sends connection-opening probes and interprets responses without completing the normal handshake for open ports.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — UDP scan:** A UDP scan sends UDP probes and interprets replies and ICMP errors; silence can be ambiguous.
- **B — TCP connect scan:** A connect scan uses the operating system connection API and completes successful TCP handshakes.
- **C — TCP ACK scan:** An ACK scan primarily maps filtering behavior; it does not determine which ports have listening services.

Coverage: M03; CEH v5 domain 2; Scan methods.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q003

**Answer: D — Host discovery**

Host discovery tests whether a host is responsive using approved discovery probes; a negative result may reflect filtering.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Operating-system fingerprinting:** OS fingerprinting infers an operating system from characteristics such as network-stack responses and remains an inference.
- **B — Service version detection:** Version detection interrogates a service to infer its protocol or implementation; banners and fingerprints require interpretation.
- **C — Vulnerability validation:** Validation checks whether a suspected weakness actually applies under the target's configuration and authorized test conditions.

Coverage: M03; CEH v5 domain 2; Discovery and identification.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q004

**Answer: A — -sV**

The -sV option requests service/version detection for discovered ports.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — -O:** The -O option requests operating-system detection, subject to privileges and useful probe conditions.
- **C — -sn:** The -sn option performs host discovery without the normal port scan.
- **D — -Pn:** The -Pn option skips host discovery and treats specified targets as up for subsequent scanning; it does not make traffic invisible.

Coverage: M03; CEH v5 domain 2; Nmap option meaning.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q005

**Answer: A — Scan-vantage dependence**

Results describe the path, source location and time of observation; another network path may expose different behavior.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Transport distinction:** TCP and UDP maintain separate port spaces; a result for one does not establish the other.
- **C — Banner uncertainty:** A banner or fingerprint may be customized, hidden or affected by a proxy, so product claims need corroboration.
- **D — Rate and reliability tradeoff:** Aggressive probing can increase loss, load or false negatives; reliable testing uses suitable rates and conditions.

Coverage: M03; CEH v5 domain 2; Interpreting scan limits.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q006

**Answer: C — Network segmentation**

Segmentation constrains which network zones can reach services and limits exposure across trust boundaries.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Service hardening:** Service hardening removes unnecessary listeners and secures the configuration of services that remain.
- **B — Authenticated inventory:** Authenticated inventory uses trusted management information to complement what unauthenticated network probes can see.
- **D — Detection and logging:** Network or host telemetry can identify probing patterns and preserve context for investigation.

Coverage: M03; CEH v5 domain 2; Discovery defenses.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q007

**Answer: D — Closed**

A closed port is reachable but has no service listening for the tested transport at that time.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Open:** An open port has a service accepting the relevant transport connections or datagrams from the scanner's perspective.
- **B — Open or filtered:** The probe outcome cannot distinguish an open port from one whose traffic is silently filtered.
- **C — Filtered:** Filtering prevents the scanner from determining whether a port is open or closed.

Coverage: M03; CEH v5 domain 2; Port states.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q008

**Answer: B — TCP connect scan**

A connect scan uses the operating system connection API and completes successful TCP handshakes.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — TCP ACK scan:** An ACK scan primarily maps filtering behavior; it does not determine which ports have listening services.
- **C — UDP scan:** A UDP scan sends UDP probes and interprets replies and ICMP errors; silence can be ambiguous.
- **D — TCP SYN scan:** A SYN scan sends connection-opening probes and interprets responses without completing the normal handshake for open ports.

Coverage: M03; CEH v5 domain 2; Scan methods.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q009

**Answer: C — Service version detection**

Version detection interrogates a service to infer its protocol or implementation; banners and fingerprints require interpretation.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Operating-system fingerprinting:** OS fingerprinting infers an operating system from characteristics such as network-stack responses and remains an inference.
- **B — Vulnerability validation:** Validation checks whether a suspected weakness actually applies under the target's configuration and authorized test conditions.
- **D — Host discovery:** Host discovery tests whether a host is responsive using approved discovery probes; a negative result may reflect filtering.

Coverage: M03; CEH v5 domain 2; Discovery and identification.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q010

**Answer: C — -O**

The -O option requests operating-system detection, subject to privileges and useful probe conditions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — -Pn:** The -Pn option skips host discovery and treats specified targets as up for subsequent scanning; it does not make traffic invisible.
- **B — -sn:** The -sn option performs host discovery without the normal port scan.
- **D — -sV:** The -sV option requests service/version detection for discovered ports.

Coverage: M03; CEH v5 domain 2; Nmap option meaning.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q011

**Answer: C — Transport distinction**

TCP and UDP maintain separate port spaces; a result for one does not establish the other.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Banner uncertainty:** A banner or fingerprint may be customized, hidden or affected by a proxy, so product claims need corroboration.
- **B — Rate and reliability tradeoff:** Aggressive probing can increase loss, load or false negatives; reliable testing uses suitable rates and conditions.
- **D — Scan-vantage dependence:** Results describe the path, source location and time of observation; another network path may expose different behavior.

Coverage: M03; CEH v5 domain 2; Interpreting scan limits.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q012

**Answer: B — Service hardening**

Service hardening removes unnecessary listeners and secures the configuration of services that remain.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Detection and logging:** Network or host telemetry can identify probing patterns and preserve context for investigation.
- **C — Network segmentation:** Segmentation constrains which network zones can reach services and limits exposure across trust boundaries.
- **D — Authenticated inventory:** Authenticated inventory uses trusted management information to complement what unauthenticated network probes can see.

Coverage: M03; CEH v5 domain 2; Discovery defenses.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q013

**Answer: C — Filtered**

Filtering prevents the scanner from determining whether a port is open or closed.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Open or filtered:** The probe outcome cannot distinguish an open port from one whose traffic is silently filtered.
- **B — Closed:** A closed port is reachable but has no service listening for the tested transport at that time.
- **D — Open:** An open port has a service accepting the relevant transport connections or datagrams from the scanner's perspective.

Coverage: M03; CEH v5 domain 2; Port states.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q014

**Answer: A — UDP scan**

A UDP scan sends UDP probes and interprets replies and ICMP errors; silence can be ambiguous.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — TCP ACK scan:** An ACK scan primarily maps filtering behavior; it does not determine which ports have listening services.
- **C — TCP connect scan:** A connect scan uses the operating system connection API and completes successful TCP handshakes.
- **D — TCP SYN scan:** A SYN scan sends connection-opening probes and interprets responses without completing the normal handshake for open ports.

Coverage: M03; CEH v5 domain 2; Scan methods.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q015

**Answer: A — Operating-system fingerprinting**

OS fingerprinting infers an operating system from characteristics such as network-stack responses and remains an inference.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Host discovery:** Host discovery tests whether a host is responsive using approved discovery probes; a negative result may reflect filtering.
- **C — Service version detection:** Version detection interrogates a service to infer its protocol or implementation; banners and fingerprints require interpretation.
- **D — Vulnerability validation:** Validation checks whether a suspected weakness actually applies under the target's configuration and authorized test conditions.

Coverage: M03; CEH v5 domain 2; Discovery and identification.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q016

**Answer: D — -Pn**

The -Pn option skips host discovery and treats specified targets as up for subsequent scanning; it does not make traffic invisible.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — -sV:** The -sV option requests service/version detection for discovered ports.
- **B — -sn:** The -sn option performs host discovery without the normal port scan.
- **C — -O:** The -O option requests operating-system detection, subject to privileges and useful probe conditions.

Coverage: M03; CEH v5 domain 2; Nmap option meaning.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q017

**Answer: D — Banner uncertainty**

A banner or fingerprint may be customized, hidden or affected by a proxy, so product claims need corroboration.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Rate and reliability tradeoff:** Aggressive probing can increase loss, load or false negatives; reliable testing uses suitable rates and conditions.
- **B — Scan-vantage dependence:** Results describe the path, source location and time of observation; another network path may expose different behavior.
- **C — Transport distinction:** TCP and UDP maintain separate port spaces; a result for one does not establish the other.

Coverage: M03; CEH v5 domain 2; Interpreting scan limits.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q018

**Answer: D — Detection and logging**

Network or host telemetry can identify probing patterns and preserve context for investigation.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Authenticated inventory:** Authenticated inventory uses trusted management information to complement what unauthenticated network probes can see.
- **B — Network segmentation:** Segmentation constrains which network zones can reach services and limits exposure across trust boundaries.
- **C — Service hardening:** Service hardening removes unnecessary listeners and secures the configuration of services that remain.

Coverage: M03; CEH v5 domain 2; Discovery defenses.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q019

**Answer: B — Open or filtered**

The probe outcome cannot distinguish an open port from one whose traffic is silently filtered.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Open:** An open port has a service accepting the relevant transport connections or datagrams from the scanner's perspective.
- **C — Closed:** A closed port is reachable but has no service listening for the tested transport at that time.
- **D — Filtered:** Filtering prevents the scanner from determining whether a port is open or closed.

Coverage: M03; CEH v5 domain 2; Port states.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q020

**Answer: B — TCP ACK scan**

An ACK scan primarily maps filtering behavior; it does not determine which ports have listening services.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — TCP connect scan:** A connect scan uses the operating system connection API and completes successful TCP handshakes.
- **C — TCP SYN scan:** A SYN scan sends connection-opening probes and interprets responses without completing the normal handshake for open ports.
- **D — UDP scan:** A UDP scan sends UDP probes and interprets replies and ICMP errors; silence can be ambiguous.

Coverage: M03; CEH v5 domain 2; Scan methods.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q021

**Answer: C — Vulnerability validation**

Validation checks whether a suspected weakness actually applies under the target's configuration and authorized test conditions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Service version detection:** Version detection interrogates a service to infer its protocol or implementation; banners and fingerprints require interpretation.
- **B — Host discovery:** Host discovery tests whether a host is responsive using approved discovery probes; a negative result may reflect filtering.
- **D — Operating-system fingerprinting:** OS fingerprinting infers an operating system from characteristics such as network-stack responses and remains an inference.

Coverage: M03; CEH v5 domain 2; Discovery and identification.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q022

**Answer: A — -sn**

The -sn option performs host discovery without the normal port scan.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — -Pn:** The -Pn option skips host discovery and treats specified targets as up for subsequent scanning; it does not make traffic invisible.
- **C — -O:** The -O option requests operating-system detection, subject to privileges and useful probe conditions.
- **D — -sV:** The -sV option requests service/version detection for discovered ports.

Coverage: M03; CEH v5 domain 2; Nmap option meaning.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q023

**Answer: B — Rate and reliability tradeoff**

Aggressive probing can increase loss, load or false negatives; reliable testing uses suitable rates and conditions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Banner uncertainty:** A banner or fingerprint may be customized, hidden or affected by a proxy, so product claims need corroboration.
- **C — Scan-vantage dependence:** Results describe the path, source location and time of observation; another network path may expose different behavior.
- **D — Transport distinction:** TCP and UDP maintain separate port spaces; a result for one does not establish the other.

Coverage: M03; CEH v5 domain 2; Interpreting scan limits.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q024

**Answer: A — Authenticated inventory**

Authenticated inventory uses trusted management information to complement what unauthenticated network probes can see.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Service hardening:** Service hardening removes unnecessary listeners and secures the configuration of services that remain.
- **C — Detection and logging:** Network or host telemetry can identify probing patterns and preserve context for investigation.
- **D — Network segmentation:** Segmentation constrains which network zones can reach services and limits exposure across trust boundaries.

Coverage: M03; CEH v5 domain 2; Discovery defenses.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q025

**Answer: B — Closed**

A closed port is reachable but has no service listening for the tested transport at that time.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Filtered:** Filtering prevents the scanner from determining whether a port is open or closed.
- **C — Open or filtered:** The probe outcome cannot distinguish an open port from one whose traffic is silently filtered.
- **D — Open:** An open port has a service accepting the relevant transport connections or datagrams from the scanner's perspective.

Coverage: M03; CEH v5 domain 2; Port states.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q026

**Answer: B — TCP connect scan**

A connect scan uses the operating system connection API and completes successful TCP handshakes.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — UDP scan:** A UDP scan sends UDP probes and interprets replies and ICMP errors; silence can be ambiguous.
- **C — TCP ACK scan:** An ACK scan primarily maps filtering behavior; it does not determine which ports have listening services.
- **D — TCP SYN scan:** A SYN scan sends connection-opening probes and interprets responses without completing the normal handshake for open ports.

Coverage: M03; CEH v5 domain 2; Scan methods.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q027

**Answer: D — Service version detection**

Version detection interrogates a service to infer its protocol or implementation; banners and fingerprints require interpretation.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Host discovery:** Host discovery tests whether a host is responsive using approved discovery probes; a negative result may reflect filtering.
- **B — Operating-system fingerprinting:** OS fingerprinting infers an operating system from characteristics such as network-stack responses and remains an inference.
- **C — Vulnerability validation:** Validation checks whether a suspected weakness actually applies under the target's configuration and authorized test conditions.

Coverage: M03; CEH v5 domain 2; Discovery and identification.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q028

**Answer: D — -Pn**

The -Pn option skips host discovery and treats specified targets as up for subsequent scanning; it does not make traffic invisible.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — -O:** The -O option requests operating-system detection, subject to privileges and useful probe conditions.
- **B — -sV:** The -sV option requests service/version detection for discovered ports.
- **C — -sn:** The -sn option performs host discovery without the normal port scan.

Coverage: M03; CEH v5 domain 2; Nmap option meaning.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q029

**Answer: A — Transport distinction**

TCP and UDP maintain separate port spaces; a result for one does not establish the other.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Rate and reliability tradeoff:** Aggressive probing can increase loss, load or false negatives; reliable testing uses suitable rates and conditions.
- **C — Banner uncertainty:** A banner or fingerprint may be customized, hidden or affected by a proxy, so product claims need corroboration.
- **D — Scan-vantage dependence:** Results describe the path, source location and time of observation; another network path may expose different behavior.

Coverage: M03; CEH v5 domain 2; Interpreting scan limits.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-M03-Q030

**Answer: C — Service hardening**

Service hardening removes unnecessary listeners and secures the configuration of services that remain.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Network segmentation:** Segmentation constrains which network zones can reach services and limits exposure across trust boundaries.
- **B — Detection and logging:** Network or host telemetry can identify probing patterns and preserve context for investigation.
- **D — Authenticated inventory:** Authenticated inventory uses trusted management information to complement what unauthenticated network probes can see.

Coverage: M03; CEH v5 domain 2; Discovery defenses.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)
