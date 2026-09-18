# M08 — Sniffing — instructor key v1.0.0

[Question form](m08.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M08-Q001

**Answer: A — Promiscuous mode**

Promiscuous mode allows an interface to pass more received frames to capture software; it does not force a switch to send all traffic to that port.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Network TAP:** A network TAP provides a dedicated observation point on a link; visibility depends on its placement and capabilities.
- **C — Switch port mirroring:** Port mirroring copies selected switch traffic to an authorized monitoring port, subject to configuration and capacity limits.
- **D — Encrypted payload limitation:** Encryption can conceal application content from a passive observer even when addresses, timing or other metadata remain visible.

Coverage: M08; CEH v5 domain 4; Packet visibility.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q002

**Answer: D — ARP spoofing**

ARP spoofing sends misleading local IPv4-to-link-layer address information and can redirect traffic on a local segment.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — DNS poisoning:** DNS poisoning causes a resolver or client to use an incorrect name-to-address answer.
- **B — MAC-table flooding:** MAC-table flooding attempts to overwhelm switch forwarding entries; the resulting behavior depends on the device and controls.
- **C — DHCP spoofing:** A rogue DHCP server supplies unauthorized network configuration, such as a malicious gateway or DNS server.

Coverage: M08; CEH v5 domain 4; Local-network attacks.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q003

**Answer: C — Dynamic ARP inspection**

DAI validates ARP messages against trusted bindings or policy to reduce spoofed address mappings.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Authenticated encryption:** Correctly authenticated encryption protects traffic content and peer identity even when the local path is observable.
- **B — Port security:** Port security restricts learned or permitted source MAC addresses on a switch port according to policy.
- **D — DHCP snooping:** DHCP snooping distinguishes trusted DHCP paths and can build bindings used by other protections.

Coverage: M08; CEH v5 domain 4; Layer-two defenses.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q004

**Answer: D — Source and destination address**

Addresses identify the apparent network endpoints in the observed packet; NAT or spoofing can complicate attribution.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — TCP flags:** TCP flags such as SYN, ACK, FIN and RST describe connection-control information in the segment.
- **B — Payload:** The payload carries higher-layer data, which may be application content or encrypted bytes.
- **C — Transport port:** A transport port identifies a protocol endpoint within a transport, but convention alone does not prove the application.

Coverage: M08; CEH v5 domain 4; Packet fields.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q005

**Answer: A — TCP retransmission**

A retransmission repeats data thought to be unacknowledged; loss, delay or capture artifacts require investigation.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — TCP reset:** A reset abruptly rejects or terminates a TCP connection; its cause needs surrounding context.
- **C — DNS query and response:** DNS messages connect a question with an answer, but a captured answer still requires trust and freshness checks.
- **D — TLS handshake metadata:** Handshake metadata can reveal protocol negotiation or certificates where visible, without necessarily exposing application content.

Coverage: M08; CEH v5 domain 4; Capture interpretation.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q006

**Answer: B — Capture scope restriction**

Capture only the approved interfaces, hosts and period; shared-network visibility is not permission to collect everything.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Content minimization:** Reduce or redact unnecessary personal or secret payload content when preserving evidence for a limited purpose.
- **C — Independent corroboration:** Compare packet evidence with appropriate endpoint or application records before making a stronger causal claim.
- **D — Time and vantage recording:** Record capture time, clock assumptions and observation location so packets can be interpreted in context.

Coverage: M08; CEH v5 domain 4; Evidence and privacy.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q007

**Answer: B — Switch port mirroring**

Port mirroring copies selected switch traffic to an authorized monitoring port, subject to configuration and capacity limits.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Encrypted payload limitation:** Encryption can conceal application content from a passive observer even when addresses, timing or other metadata remain visible.
- **C — Network TAP:** A network TAP provides a dedicated observation point on a link; visibility depends on its placement and capabilities.
- **D — Promiscuous mode:** Promiscuous mode allows an interface to pass more received frames to capture software; it does not force a switch to send all traffic to that port.

Coverage: M08; CEH v5 domain 4; Packet visibility.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q008

**Answer: C — MAC-table flooding**

MAC-table flooding attempts to overwhelm switch forwarding entries; the resulting behavior depends on the device and controls.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — DNS poisoning:** DNS poisoning causes a resolver or client to use an incorrect name-to-address answer.
- **B — DHCP spoofing:** A rogue DHCP server supplies unauthorized network configuration, such as a malicious gateway or DNS server.
- **D — ARP spoofing:** ARP spoofing sends misleading local IPv4-to-link-layer address information and can redirect traffic on a local segment.

Coverage: M08; CEH v5 domain 4; Local-network attacks.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q009

**Answer: C — DHCP snooping**

DHCP snooping distinguishes trusted DHCP paths and can build bindings used by other protections.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Authenticated encryption:** Correctly authenticated encryption protects traffic content and peer identity even when the local path is observable.
- **B — Dynamic ARP inspection:** DAI validates ARP messages against trusted bindings or policy to reduce spoofed address mappings.
- **D — Port security:** Port security restricts learned or permitted source MAC addresses on a switch port according to policy.

Coverage: M08; CEH v5 domain 4; Layer-two defenses.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q010

**Answer: D — Transport port**

A transport port identifies a protocol endpoint within a transport, but convention alone does not prove the application.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Source and destination address:** Addresses identify the apparent network endpoints in the observed packet; NAT or spoofing can complicate attribution.
- **B — Payload:** The payload carries higher-layer data, which may be application content or encrypted bytes.
- **C — TCP flags:** TCP flags such as SYN, ACK, FIN and RST describe connection-control information in the segment.

Coverage: M08; CEH v5 domain 4; Packet fields.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q011

**Answer: C — TCP reset**

A reset abruptly rejects or terminates a TCP connection; its cause needs surrounding context.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — DNS query and response:** DNS messages connect a question with an answer, but a captured answer still requires trust and freshness checks.
- **B — TLS handshake metadata:** Handshake metadata can reveal protocol negotiation or certificates where visible, without necessarily exposing application content.
- **D — TCP retransmission:** A retransmission repeats data thought to be unacknowledged; loss, delay or capture artifacts require investigation.

Coverage: M08; CEH v5 domain 4; Capture interpretation.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q012

**Answer: B — Time and vantage recording**

Record capture time, clock assumptions and observation location so packets can be interpreted in context.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Independent corroboration:** Compare packet evidence with appropriate endpoint or application records before making a stronger causal claim.
- **C — Capture scope restriction:** Capture only the approved interfaces, hosts and period; shared-network visibility is not permission to collect everything.
- **D — Content minimization:** Reduce or redact unnecessary personal or secret payload content when preserving evidence for a limited purpose.

Coverage: M08; CEH v5 domain 4; Evidence and privacy.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q013

**Answer: D — Network TAP**

A network TAP provides a dedicated observation point on a link; visibility depends on its placement and capabilities.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Promiscuous mode:** Promiscuous mode allows an interface to pass more received frames to capture software; it does not force a switch to send all traffic to that port.
- **B — Encrypted payload limitation:** Encryption can conceal application content from a passive observer even when addresses, timing or other metadata remain visible.
- **C — Switch port mirroring:** Port mirroring copies selected switch traffic to an authorized monitoring port, subject to configuration and capacity limits.

Coverage: M08; CEH v5 domain 4; Packet visibility.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q014

**Answer: D — DHCP spoofing**

A rogue DHCP server supplies unauthorized network configuration, such as a malicious gateway or DNS server.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — ARP spoofing:** ARP spoofing sends misleading local IPv4-to-link-layer address information and can redirect traffic on a local segment.
- **B — MAC-table flooding:** MAC-table flooding attempts to overwhelm switch forwarding entries; the resulting behavior depends on the device and controls.
- **C — DNS poisoning:** DNS poisoning causes a resolver or client to use an incorrect name-to-address answer.

Coverage: M08; CEH v5 domain 4; Local-network attacks.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q015

**Answer: B — Port security**

Port security restricts learned or permitted source MAC addresses on a switch port according to policy.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Dynamic ARP inspection:** DAI validates ARP messages against trusted bindings or policy to reduce spoofed address mappings.
- **C — Authenticated encryption:** Correctly authenticated encryption protects traffic content and peer identity even when the local path is observable.
- **D — DHCP snooping:** DHCP snooping distinguishes trusted DHCP paths and can build bindings used by other protections.

Coverage: M08; CEH v5 domain 4; Layer-two defenses.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q016

**Answer: B — TCP flags**

TCP flags such as SYN, ACK, FIN and RST describe connection-control information in the segment.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Payload:** The payload carries higher-layer data, which may be application content or encrypted bytes.
- **C — Transport port:** A transport port identifies a protocol endpoint within a transport, but convention alone does not prove the application.
- **D — Source and destination address:** Addresses identify the apparent network endpoints in the observed packet; NAT or spoofing can complicate attribution.

Coverage: M08; CEH v5 domain 4; Packet fields.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q017

**Answer: A — DNS query and response**

DNS messages connect a question with an answer, but a captured answer still requires trust and freshness checks.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — TCP reset:** A reset abruptly rejects or terminates a TCP connection; its cause needs surrounding context.
- **C — TLS handshake metadata:** Handshake metadata can reveal protocol negotiation or certificates where visible, without necessarily exposing application content.
- **D — TCP retransmission:** A retransmission repeats data thought to be unacknowledged; loss, delay or capture artifacts require investigation.

Coverage: M08; CEH v5 domain 4; Capture interpretation.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q018

**Answer: A — Content minimization**

Reduce or redact unnecessary personal or secret payload content when preserving evidence for a limited purpose.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Capture scope restriction:** Capture only the approved interfaces, hosts and period; shared-network visibility is not permission to collect everything.
- **C — Independent corroboration:** Compare packet evidence with appropriate endpoint or application records before making a stronger causal claim.
- **D — Time and vantage recording:** Record capture time, clock assumptions and observation location so packets can be interpreted in context.

Coverage: M08; CEH v5 domain 4; Evidence and privacy.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q019

**Answer: C — Encrypted payload limitation**

Encryption can conceal application content from a passive observer even when addresses, timing or other metadata remain visible.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Promiscuous mode:** Promiscuous mode allows an interface to pass more received frames to capture software; it does not force a switch to send all traffic to that port.
- **B — Switch port mirroring:** Port mirroring copies selected switch traffic to an authorized monitoring port, subject to configuration and capacity limits.
- **D — Network TAP:** A network TAP provides a dedicated observation point on a link; visibility depends on its placement and capabilities.

Coverage: M08; CEH v5 domain 4; Packet visibility.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q020

**Answer: D — DNS poisoning**

DNS poisoning causes a resolver or client to use an incorrect name-to-address answer.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — DHCP spoofing:** A rogue DHCP server supplies unauthorized network configuration, such as a malicious gateway or DNS server.
- **B — ARP spoofing:** ARP spoofing sends misleading local IPv4-to-link-layer address information and can redirect traffic on a local segment.
- **C — MAC-table flooding:** MAC-table flooding attempts to overwhelm switch forwarding entries; the resulting behavior depends on the device and controls.

Coverage: M08; CEH v5 domain 4; Local-network attacks.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q021

**Answer: B — Authenticated encryption**

Correctly authenticated encryption protects traffic content and peer identity even when the local path is observable.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Port security:** Port security restricts learned or permitted source MAC addresses on a switch port according to policy.
- **C — DHCP snooping:** DHCP snooping distinguishes trusted DHCP paths and can build bindings used by other protections.
- **D — Dynamic ARP inspection:** DAI validates ARP messages against trusted bindings or policy to reduce spoofed address mappings.

Coverage: M08; CEH v5 domain 4; Layer-two defenses.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q022

**Answer: A — Payload**

The payload carries higher-layer data, which may be application content or encrypted bytes.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — TCP flags:** TCP flags such as SYN, ACK, FIN and RST describe connection-control information in the segment.
- **C — Source and destination address:** Addresses identify the apparent network endpoints in the observed packet; NAT or spoofing can complicate attribution.
- **D — Transport port:** A transport port identifies a protocol endpoint within a transport, but convention alone does not prove the application.

Coverage: M08; CEH v5 domain 4; Packet fields.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q023

**Answer: A — TLS handshake metadata**

Handshake metadata can reveal protocol negotiation or certificates where visible, without necessarily exposing application content.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — DNS query and response:** DNS messages connect a question with an answer, but a captured answer still requires trust and freshness checks.
- **C — TCP reset:** A reset abruptly rejects or terminates a TCP connection; its cause needs surrounding context.
- **D — TCP retransmission:** A retransmission repeats data thought to be unacknowledged; loss, delay or capture artifacts require investigation.

Coverage: M08; CEH v5 domain 4; Capture interpretation.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q024

**Answer: D — Independent corroboration**

Compare packet evidence with appropriate endpoint or application records before making a stronger causal claim.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Content minimization:** Reduce or redact unnecessary personal or secret payload content when preserving evidence for a limited purpose.
- **B — Capture scope restriction:** Capture only the approved interfaces, hosts and period; shared-network visibility is not permission to collect everything.
- **C — Time and vantage recording:** Record capture time, clock assumptions and observation location so packets can be interpreted in context.

Coverage: M08; CEH v5 domain 4; Evidence and privacy.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q025

**Answer: A — Promiscuous mode**

Promiscuous mode allows an interface to pass more received frames to capture software; it does not force a switch to send all traffic to that port.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Encrypted payload limitation:** Encryption can conceal application content from a passive observer even when addresses, timing or other metadata remain visible.
- **C — Switch port mirroring:** Port mirroring copies selected switch traffic to an authorized monitoring port, subject to configuration and capacity limits.
- **D — Network TAP:** A network TAP provides a dedicated observation point on a link; visibility depends on its placement and capabilities.

Coverage: M08; CEH v5 domain 4; Packet visibility.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q026

**Answer: C — ARP spoofing**

ARP spoofing sends misleading local IPv4-to-link-layer address information and can redirect traffic on a local segment.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — DNS poisoning:** DNS poisoning causes a resolver or client to use an incorrect name-to-address answer.
- **B — DHCP spoofing:** A rogue DHCP server supplies unauthorized network configuration, such as a malicious gateway or DNS server.
- **D — MAC-table flooding:** MAC-table flooding attempts to overwhelm switch forwarding entries; the resulting behavior depends on the device and controls.

Coverage: M08; CEH v5 domain 4; Local-network attacks.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q027

**Answer: B — DHCP snooping**

DHCP snooping distinguishes trusted DHCP paths and can build bindings used by other protections.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Dynamic ARP inspection:** DAI validates ARP messages against trusted bindings or policy to reduce spoofed address mappings.
- **C — Port security:** Port security restricts learned or permitted source MAC addresses on a switch port according to policy.
- **D — Authenticated encryption:** Correctly authenticated encryption protects traffic content and peer identity even when the local path is observable.

Coverage: M08; CEH v5 domain 4; Layer-two defenses.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q028

**Answer: D — Transport port**

A transport port identifies a protocol endpoint within a transport, but convention alone does not prove the application.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — TCP flags:** TCP flags such as SYN, ACK, FIN and RST describe connection-control information in the segment.
- **B — Source and destination address:** Addresses identify the apparent network endpoints in the observed packet; NAT or spoofing can complicate attribution.
- **C — Payload:** The payload carries higher-layer data, which may be application content or encrypted bytes.

Coverage: M08; CEH v5 domain 4; Packet fields.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q029

**Answer: C — TCP retransmission**

A retransmission repeats data thought to be unacknowledged; loss, delay or capture artifacts require investigation.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — TLS handshake metadata:** Handshake metadata can reveal protocol negotiation or certificates where visible, without necessarily exposing application content.
- **B — DNS query and response:** DNS messages connect a question with an answer, but a captured answer still requires trust and freshness checks.
- **D — TCP reset:** A reset abruptly rejects or terminates a TCP connection; its cause needs surrounding context.

Coverage: M08; CEH v5 domain 4; Capture interpretation.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-M08-Q030

**Answer: B — Content minimization**

Reduce or redact unnecessary personal or secret payload content when preserving evidence for a limited purpose.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Independent corroboration:** Compare packet evidence with appropriate endpoint or application records before making a stronger causal claim.
- **C — Time and vantage recording:** Record capture time, clock assumptions and observation location so packets can be interpreted in context.
- **D — Capture scope restriction:** Capture only the approved interfaces, hosts and period; shared-network visibility is not permission to collect everything.

Coverage: M08; CEH v5 domain 4; Evidence and privacy.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)
