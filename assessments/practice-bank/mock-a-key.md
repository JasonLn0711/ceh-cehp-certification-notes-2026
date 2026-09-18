# MOCK-A — instructor key v1.0.0

[Question form](mock-a.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-MOCK-A-Q001

**Answer: C — Privileged-account protection**

Protect high-impact administrative identities with strong authentication, controlled use and recovery procedures.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Least-privilege IAM:** Grant only the cloud actions and resources required for a role, with conditions where appropriate.
- **B — Short-lived workload credentials:** Use temporary workload identity or credentials rather than distributing long-lived static secrets when supported.
- **D — Explicit resource policy review:** Review resource-level access together with identity policy because both can affect who can use an object or service.

Coverage: M19; CEH v5 domain 8; Cloud identity.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-MOCK-A-Q002

**Answer: C — CNAME record**

A CNAME record makes one name an alias of another canonical name.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — A record:** An A record maps a name to an IPv4 address.
- **B — AAAA record:** An AAAA record maps a name to an IPv6 address.
- **D — MX record:** An MX record identifies mail exchangers for a domain and includes preference values.

Coverage: M02; CEH v5 domain 2; DNS records.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-MOCK-A-Q003

**Answer: B — Encrypted payload limitation**

Encryption can conceal application content from a passive observer even when addresses, timing or other metadata remain visible.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Network TAP:** A network TAP provides a dedicated observation point on a link; visibility depends on its placement and capabilities.
- **C — Switch port mirroring:** Port mirroring copies selected switch traffic to an authorized monitoring port, subject to configuration and capacity limits.
- **D — Promiscuous mode:** Promiscuous mode allows an interface to pass more received frames to capture software; it does not force a switch to send all traffic to that port.

Coverage: M08; CEH v5 domain 4; Packet visibility.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-MOCK-A-Q004

**Answer: C — Smishing**

Smishing delivers deceptive requests through SMS or similar text-message channels.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Spear phishing:** Spear phishing tailors deception to a particular person or group using relevant context.
- **B — Vishing:** Vishing uses voice communication to deceive a person into disclosure or action.
- **D — Phishing:** Phishing uses deceptive messages to induce harmful actions or disclosure, commonly through email or other electronic messaging.

Coverage: M09; CEH v5 domain 4; Social-engineering channels.
Technical references: [CISA phishing guidance](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing) · [MITRE phishing](https://attack.mitre.org/techniques/T1566/) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-A-Q005

**Answer: A — Ransomware**

Ransomware denies access to data or systems, commonly through encryption, and demands payment; some campaigns also steal data.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Worm:** A worm can propagate between systems without needing to attach itself to an ordinary host file.
- **C — Trojan:** A Trojan presents an apparently useful or legitimate function while carrying hidden malicious behavior.
- **D — Virus:** A virus replicates by attaching to a host file or similar carrier and depends on that host's execution or activation.

Coverage: M07; CEH v5 domain 3; Malware classes.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-MOCK-A-Q006

**Answer: B — Constructive debrief**

A useful debrief explains cues and reporting actions without humiliating individuals.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Outcome-based measurement:** Measure the behavior relevant to the learning goal instead of treating one click count as complete competence evidence.
- **C — Explicit campaign approval:** A social-engineering exercise needs authorized scope, targets, methods and escalation before delivery.
- **D — Participant protection:** Protect people from unnecessary harm and avoid collecting real passwords or unrelated sensitive information.

Coverage: M09; CEH v5 domain 4; Exercise governance.
Technical references: [CISA phishing guidance](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing) · [MITRE phishing](https://attack.mitre.org/techniques/T1566/) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-A-Q007

**Answer: A — Regression coverage**

Retain tests for the repaired weakness and valid behavior so later changes can reveal a recurrence or broken function.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Safe proof of impact:** Demonstrate the minimum authorized effect needed to establish a finding without unnecessary data exposure or damage.
- **C — State-change verification:** Verify the actual backend effect rather than assuming a response code proves the intended action occurred.
- **D — Positive and negative authorization tests:** Check both permitted and forbidden operations with appropriate test identities so success is not judged from one allowed case.

Coverage: M14; CEH v5 domain 5; Testing interpretation.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-A-Q008

**Answer: A — DHCP spoofing**

A rogue DHCP server supplies unauthorized network configuration, such as a malicious gateway or DNS server.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — MAC-table flooding:** MAC-table flooding attempts to overwhelm switch forwarding entries; the resulting behavior depends on the device and controls.
- **C — DNS poisoning:** DNS poisoning causes a resolver or client to use an incorrect name-to-address answer.
- **D — ARP spoofing:** ARP spoofing sends misleading local IPv4-to-link-layer address information and can redirect traffic on a local segment.

Coverage: M08; CEH v5 domain 4; Local-network attacks.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-MOCK-A-Q009

**Answer: D — Host validation**

Validate host information before using it for routing, links or security-sensitive decisions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Origin access restriction:** Restrict direct access to an origin when security controls are intended to be enforced by its reverse proxy.
- **B — Trusted proxy configuration:** Accept forwarding metadata only from defined trusted proxies, not arbitrary clients that can forge headers.
- **C — Consistent HTTP parsing:** Frontends and backends must agree on request framing and interpretation to avoid boundary confusion.

Coverage: M13; CEH v5 domain 5; Proxy trust boundaries.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-A-Q010

**Answer: D — Document metadata**

Document metadata can reveal properties such as authoring software or author fields, which may be stale or user-controlled.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Search-engine indexing:** A search engine exposes its indexed view of content; cached results can lag behind current deployment.
- **B — Certificate transparency logs:** Certificate transparency records publicly logged certificates and can reveal names, but not whether a service is currently live.
- **C — RDAP registration data:** RDAP provides structured registration information; privacy redaction and registry differences limit what it reveals.

Coverage: M02; CEH v5 domain 2; Reconnaissance sources.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-MOCK-A-Q011

**Answer: D — Attack corroboration**

Use multiple indicators such as traffic patterns, request semantics and resource effects to support an attack conclusion.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Legitimate demand surge:** A large increase in genuine user demand can resemble an attack in volume while requiring different decisions.
- **B — Dependency failure:** An upstream or shared dependency can cause outage symptoms even when the application is not being attacked.
- **C — Baseline comparison:** Compare current traffic and resource behavior with a relevant normal baseline before classifying an anomaly.

Coverage: M10; CEH v5 domain 4; Interpreting outages.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-MOCK-A-Q012

**Answer: C — Apply supported updates**

Use maintained software and verified relevant fixes; deployment and restart state must make the fix effective.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Separate writable and executable content:** Prevent user-controlled uploads or writable directories from being interpreted as server-side executable code.
- **B — Run with limited privileges:** Give the web process only the operating-system and filesystem access its function needs.
- **D — Remove unused features:** Disable or remove unneeded handlers, modules and sample applications to reduce attack surface.

Coverage: M13; CEH v5 domain 5; Server hardening.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-A-Q013

**Answer: D — Channel**

The channel identifies the radio-frequency portion used by the network; interference and observation depend on channel conditions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — BSSID:** A BSSID identifies a basic service set, commonly using the access point radio's MAC address.
- **B — Signal strength:** Signal strength measures received power at the observer and does not reliably establish trust or exact physical distance.
- **C — SSID:** An SSID names a wireless network and is not a secret or proof that an access point is legitimate.

Coverage: M16; CEH v5 domain 6; Wireless identity.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-MOCK-A-Q014

**Answer: C — Encoding normalization**

Security checks need a consistent decoded representation so alternate encodings do not bypass matching while reaching the same application meaning.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Encryption visibility gap:** An observer without decryption access may see metadata but cannot inspect protected application payloads directly.
- **B — Fragmentation and reassembly difference:** Different interpretations of fragments or streams can create disagreement between an inspection device and the endpoint.
- **D — Protocol ambiguity:** Parser differences or unexpected protocol use can make different components interpret the same traffic differently.

Coverage: M12; CEH v5 domain 4; Inspection challenges.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-MOCK-A-Q015

**Answer: A — Authorization check**

Every protected operation still needs a server-side decision that the current subject may perform that specific action.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Anti-CSRF token:** An unpredictable request token tied to the expected context helps distinguish legitimate submissions from cross-site forgeries.
- **C — Origin validation:** Checking the request's origin information can support CSRF defenses when implemented with appropriate trust and fallback rules.
- **D — Cross-site request forgery:** CSRF induces a victim's browser to send an unwanted authenticated request using ambient credentials.

Coverage: M11; CEH v5 domain 4; CSRF and session scope.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-A-Q016

**Answer: B — Authenticated inventory**

Authenticated inventory uses trusted management information to complement what unauthenticated network probes can see.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Network segmentation:** Segmentation constrains which network zones can reach services and limits exposure across trust boundaries.
- **C — Detection and logging:** Network or host telemetry can identify probing patterns and preserve context for investigation.
- **D — Service hardening:** Service hardening removes unnecessary listeners and secures the configuration of services that remain.

Coverage: M03; CEH v5 domain 2; Discovery defenses.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-MOCK-A-Q017

**Answer: D — Residual risk**

Residual risk is the risk that remains after controls or remediation have been applied.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Exposure and exploitability:** Reachability, required conditions and credible exploitation evidence affect practical urgency.
- **B — Business impact:** The affected asset's function and the potential harm determine organizational consequences.
- **C — Compensating control:** An alternate control can reduce exposure or impact while the underlying weakness is being repaired.

Coverage: M05; CEH v5 domain 3; Remediation priority.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-MOCK-A-Q018

**Answer: C — Test literal handling**

Confirm that SQL-looking input is processed as ordinary data or rejected by the intended contract, not executed as syntax.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Review every query path:** Apply safe construction to all relevant paths, including alternate endpoints and background jobs using the same data.
- **B — Check database permissions:** Review the account's actual database privileges to limit damage if another application flaw appears.
- **D — Retest valid inputs:** Verify normal application behavior so an injection fix does not merely disable the feature.

Coverage: M15; CEH v5 domain 5; Fix verification.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-A-Q019

**Answer: A — TCP ACK scan**

An ACK scan primarily maps filtering behavior; it does not determine which ports have listening services.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — TCP SYN scan:** A SYN scan sends connection-opening probes and interprets responses without completing the normal handshake for open ports.
- **C — TCP connect scan:** A connect scan uses the operating system connection API and completes successful TCP handshakes.
- **D — UDP scan:** A UDP scan sends UDP probes and interprets replies and ICMP errors; silence can be ambiguous.

Coverage: M03; CEH v5 domain 2; Scan methods.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-MOCK-A-Q020

**Answer: B — Monitor query patterns**

Log and review unusual enumeration volume or sensitive-object queries within appropriate operational limits.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Apply least-privilege access:** Grant directory, share and management access only to the identities and data needed for each role.
- **C — Disable unnecessary anonymous queries:** Reduce unauthenticated information disclosure while preserving required service behavior.
- **D — Remove unnecessary legacy services:** Retire unused legacy discovery or sharing services to reduce avoidable exposure.

Coverage: M04; CEH v5 domain 2; Enumeration countermeasures.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-A-Q021

**Answer: C — Shared responsibility**

Security duties depend on the service and contract; using a provider does not eliminate the customer's responsibilities.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Software as a Service:** SaaS delivers an application operated by the provider, while customer identities, use and configuration still carry responsibilities.
- **B — Platform as a Service:** PaaS manages more of the application platform, while customers still manage their application logic, data and relevant configuration.
- **D — Infrastructure as a Service:** IaaS exposes infrastructure resources while customers typically manage guest operating systems and their workloads.

Coverage: M19; CEH v5 domain 8; Service models.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-MOCK-A-Q022

**Answer: D — Unique salt**

A unique salt makes equal passwords produce different stored verifiers and reduces reuse of precomputed tables.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Multifactor authentication:** MFA requires additional authentication factors, reducing reliance on a password alone; it does not repair weak password storage.
- **B — Password key-derivation function:** A purpose-built password KDF makes each guess expensive through configurable computational or memory cost.
- **C — Pepper held separately:** A pepper is an additional secret kept apart from the password database; losing only the database need not expose it.

Coverage: M06; CEH v5 domain 3; Password storage.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-MOCK-A-Q023

**Answer: A — Source and destination address**

Addresses identify the apparent network endpoints in the observed packet; NAT or spoofing can complicate attribution.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — TCP flags:** TCP flags such as SYN, ACK, FIN and RST describe connection-control information in the segment.
- **C — Payload:** The payload carries higher-layer data, which may be application content or encrypted bytes.
- **D — Transport port:** A transport port identifies a protocol endpoint within a transport, but convention alone does not prove the application.

Coverage: M08; CEH v5 domain 4; Packet fields.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-MOCK-A-Q024

**Answer: B — Volumetric exhaustion**

Volumetric attacks attempt to saturate bandwidth or packet-processing capacity with excessive traffic.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Distributed denial of service:** A DDoS uses many sources to disrupt availability; distribution describes sources rather than a single exhaustion mechanism.
- **C — Protocol-state exhaustion:** State-exhaustion attacks consume connection or protocol tracking resources, even without maximal bandwidth.
- **D — Application resource exhaustion:** Application-layer exhaustion makes the service spend disproportionate resources on requests or sessions.

Coverage: M10; CEH v5 domain 4; Availability mechanisms.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-MOCK-A-Q025

**Answer: A — Reduce published metadata**

Remove unnecessary author, path and software details from public documents and pages.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Inventory public dependencies:** Track public names, certificates and vendor links so abandoned or unexpected dependencies can be investigated.
- **C — Restrict zone transfers:** Allow DNS zone transfers only to the intended authorized secondary servers.
- **D — Use approved public contact roles:** Publish necessary role-based contacts while avoiding unnecessary personal staff details.

Coverage: M02; CEH v5 domain 2; Exposure reduction.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-MOCK-A-Q026

**Answer: D — Operating-system fingerprinting**

OS fingerprinting infers an operating system from characteristics such as network-stack responses and remains an inference.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Service version detection:** Version detection interrogates a service to infer its protocol or implementation; banners and fingerprints require interpretation.
- **B — Vulnerability validation:** Validation checks whether a suspected weakness actually applies under the target's configuration and authorized test conditions.
- **C — Host discovery:** Host discovery tests whether a host is responsive using approved discovery probes; a negative result may reflect filtering.

Coverage: M03; CEH v5 domain 2; Discovery and identification.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-MOCK-A-Q027

**Answer: D — Private service connectivity**

Use supported private access paths where appropriate to reduce unnecessary public routing, while retaining authentication and authorization.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Public exposure inventory:** Track public addresses, listeners and service endpoints rather than assuming a resource is private by name.
- **B — Metadata-service protection:** Protect access to workload metadata and credentials, especially against server-side request paths that can reach it.
- **C — Security-group policy:** A workload-level network policy constrains permitted traffic according to the cloud service's supported semantics.

Coverage: M19; CEH v5 domain 8; Cloud network paths.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-MOCK-A-Q028

**Answer: B — Recovery verification**

Check legitimate user success and resource stability after mitigation rather than relying only on reduced attack traffic.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Bounded load testing:** Use an approved environment, rate, duration and stop condition to test capacity without uncontrolled disruption.
- **C — Rollback plan:** A rollback plan restores the prior configuration if a mitigation damages legitimate service.
- **D — Incident coordination:** Coordinate service owners, network operators and responders because availability incidents can span multiple control points.

Coverage: M10; CEH v5 domain 4; Safe testing and recovery.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-MOCK-A-Q029

**Answer: C — Capacity monitoring**

Monitoring tracks resource use and failure symptoms so the bottleneck and mitigation effects can be identified.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Upstream filtering:** Upstream filtering removes unwanted traffic before it consumes a constrained downstream link or service path.
- **B — SYN cookies:** SYN cookies encode enough handshake state in a response so selected state need not be allocated until a valid acknowledgement arrives.
- **D — Connection-rate controls:** Rate controls constrain new connection creation according to an operational policy.

Coverage: M10; CEH v5 domain 4; SYN-flood defenses.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-MOCK-A-Q030

**Answer: B — Tenant isolation**

Enforce tenant boundaries in data queries and operations so one tenant cannot reach another's resources.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Function-level authorization:** Check whether the subject may invoke a privileged operation, not just whether the route is visible in the UI.
- **C — Object-level authorization:** Check whether the subject may access the specific referenced object on every relevant request.
- **D — Deny-by-default access policy:** Reject access unless the applicable policy explicitly grants it, including newly added routes.

Coverage: M14; CEH v5 domain 5; Server-side authorization.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-A-Q031

**Answer: D — Synthetic-media impersonation**

Generated voice or video can imitate a trusted person, so apparent likeness alone is insufficient verification.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — QR-code phishing:** A QR code can conceal a destination until scanned; the encoded link still needs independent trust checks.
- **B — MFA fatigue:** Repeated authentication prompts can pressure a person into approving an attacker-initiated login.
- **C — Business email compromise:** BEC manipulates business communication to induce actions such as fraudulent payments; malware is not required.

Coverage: M09; CEH v5 domain 4; Modern deception distinctions.
Technical references: [CISA phishing guidance](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing) · [MITRE phishing](https://attack.mitre.org/techniques/T1566/) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-A-Q032

**Answer: A — Asset inventory**

Maintain known devices, firmware, function and ownership so exposure and change decisions have an operational basis.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Controlled jump host:** A managed intermediary can constrain and log approved administrative access instead of exposing controllers directly.
- **C — Industrial zones and conduits:** Separate assets by trust and function, and restrict the communication paths that cross those boundaries.
- **D — Time-bounded vendor access:** Limit vendor remote access to authorized identities, purpose and windows, with reviewable revocation.

Coverage: M18; CEH v5 domain 7; Segmentation and remote access.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-MOCK-A-Q033

**Answer: B — Rotate after privilege change**

Issue a fresh session identifier after authentication or privilege elevation and invalidate the previous relevant state.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Invalidate on logout:** Logout should revoke server-side session usability, not merely remove a page or local UI state.
- **C — Idle and absolute timeout:** Idle timeout limits inactivity while absolute timeout bounds total session lifetime regardless of activity.
- **D — Reauthenticate sensitive actions:** Require fresh verification for sensitive operations when session possession alone is insufficient assurance.

Coverage: M11; CEH v5 domain 4; Session lifecycle defenses.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-A-Q034

**Answer: A — Malicious profile or management enrollment**

An untrusted configuration profile or management relationship can change device settings and trust boundaries.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Lost-device exposure:** A lost device creates risks depending on its lock state, stored data, keys and remote management controls.
- **C — Sideloaded malicious app:** An application obtained outside the intended trusted distribution path may carry unreviewed harmful behavior; provenance still needs assessment.
- **D — SIM-swap risk:** Transfer of a phone number can expose workflows relying on that number for recovery or authentication.

Coverage: M17; CEH v5 domain 7; Mobile threat scenarios.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-MOCK-A-Q035

**Answer: D — Password spraying**

Password spraying tries a small number of likely passwords across many accounts, often to avoid per-account lockout.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Brute-force login guessing:** Online brute-force guessing tries many password candidates through a live authentication interface.
- **B — Credential stuffing:** Credential stuffing reuses previously obtained username/password pairs against other services.
- **C — Offline password guessing:** Offline guessing tests candidate passwords against acquired verifiers without sending each attempt to the login service.

Coverage: M06; CEH v5 domain 3; Credential attacks.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-MOCK-A-Q036

**Answer: A — Decoy interaction evidence**

Interaction with a decoy is an observation that needs context; it is not automatic proof of a particular actor or full compromise.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Realism tradeoff:** A more realistic decoy may collect richer behavior but can require more containment and maintenance.
- **C — Isolation of the decoy:** Constrain a decoy so it cannot become an uncontrolled path into production or harm other systems.
- **D — Detection of deception:** Unrealistic banners, inconsistent behavior or known artifacts can reveal that a resource is a decoy.

Coverage: M12; CEH v5 domain 4; Decoy limitations.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-MOCK-A-Q037

**Answer: B — CISA KEV**

The Known Exploited Vulnerabilities catalog identifies listed vulnerabilities with evidence of exploitation in the wild.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — CVE:** A CVE identifier names a publicly disclosed vulnerability record; the identifier itself is not a severity score.
- **C — CVSS:** CVSS expresses technical vulnerability severity using metrics and a versioned scoring method.
- **D — CWE:** CWE classifies weakness types, such as improper input handling or missing authorization.

Coverage: M05; CEH v5 domain 3; Classification systems.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-MOCK-A-Q038

**Answer: C — Session prediction**

Prediction exploits insufficient randomness or structure that makes valid session identifiers guessable.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Session replay:** Replay presents previously obtained valid session material again; freshness and invalidation controls affect whether it succeeds.
- **B — Session-token theft:** Token theft obtains an existing valid session credential and may allow impersonation without knowing the password.
- **D — Session fixation:** Session fixation reuses an identifier known before login when the application fails to rotate it after authentication.

Coverage: M11; CEH v5 domain 4; Session weaknesses.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-A-Q039

**Answer: C — Capture scope restriction**

Capture only the approved interfaces, hosts and period; shared-network visibility is not permission to collect everything.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Independent corroboration:** Compare packet evidence with appropriate endpoint or application records before making a stronger causal claim.
- **B — Content minimization:** Reduce or redact unnecessary personal or secret payload content when preserving evidence for a limited purpose.
- **D — Time and vantage recording:** Record capture time, clock assumptions and observation location so packets can be interpreted in context.

Coverage: M08; CEH v5 domain 4; Evidence and privacy.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-MOCK-A-Q040

**Answer: B — High-entropy identifier**

A session identifier should be generated with enough unpredictable randomness to resist guessing.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Claim validation:** Validate context such as issuer, audience and expiry; a valid signature alone does not make every token suitable for every service.
- **C — Token signature verification:** Verify a token's signature and intended algorithm with trusted keys before accepting its claims.
- **D — Revocation strategy:** Plan how compromised or logged-out credentials stop working, including the constraints of self-contained tokens.

Coverage: M11; CEH v5 domain 4; Token design.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-A-Q041

**Answer: D — Canonical path containment**

Resolve paths consistently and verify that the final target remains within the authorized base location.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Parameterized interpreter use:** Use APIs that keep data separate from executable command or query structure rather than concatenating syntax.
- **B — Safe file storage:** Store uploads with controlled names and permissions outside executable paths, and serve them through an appropriate access policy.
- **C — Allowlisted input validation:** Validate expected type, format, bounds and permitted values where the application has a well-defined input contract.

Coverage: M14; CEH v5 domain 5; Input and upload controls.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-A-Q042

**Answer: B — Check for regression**

Verify that the change preserves required behavior and has not introduced a new failure.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Apply and verify the fix:** Confirm that the intended change removes the relevant vulnerable condition, rather than only recording that a patch command ran.
- **C — Retest the original finding:** Repeat the permitted check that originally demonstrated the problem and compare the result.
- **D — Document accepted risk:** When an authorized owner accepts remaining risk, record the scope, reason, owner and review conditions.

Coverage: M05; CEH v5 domain 3; Remediation lifecycle.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-MOCK-A-Q043

**Answer: C — Modbus**

Modbus supports industrial register-oriented communication; security depends on variant and deployment controls rather than assuming every installation authenticates commands.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Zigbee:** Zigbee supports low-power wireless networking for constrained devices; joining, keys and implementation security still matter.
- **B — MQTT:** MQTT uses a publish/subscribe model through a broker; authentication, topic authorization and transport protection require configuration.
- **D — CoAP:** CoAP is designed for constrained environments and uses a resource-oriented request/response model, commonly over UDP.

Coverage: M18; CEH v5 domain 7; IoT protocol roles.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-MOCK-A-Q044

**Answer: A — Reverse proxy or CDN**

A reverse proxy or CDN can terminate public requests while hiding or separating the origin server.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Traceroute:** Traceroute infers path hops from probe responses, often using time-to-live or hop-limit expiry; missing replies do not prove a broken path.
- **C — Autonomous-system data:** AS and routing data identify network routing relationships or announced prefixes, not automatic testing permission.
- **D — Geolocation estimate:** IP geolocation estimates an address's location; VPNs, shared infrastructure and stale databases limit precision.

Coverage: M02; CEH v5 domain 2; Network footprint interpretation.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-MOCK-A-Q045

**Answer: A — Secure**

The Secure attribute restricts cookie transmission to secure transport contexts; it does not prevent script access by itself.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — SameSite:** SameSite restricts cookie inclusion in specified cross-site request contexts, depending on its configured value and browser behavior.
- **C — HttpOnly:** HttpOnly prevents ordinary client-side script access to the cookie, but does not stop all actions performed by injected script.
- **D — Path and Domain scope:** Path and Domain influence where a cookie is sent; they should not be treated as a complete authorization boundary.

Coverage: M11; CEH v5 domain 4; Cookie attributes.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-A-Q046

**Answer: D — HMAC**

HMAC uses a shared secret key and a hash-based construction to authenticate messages; any party holding the key can generate a valid tag.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Symmetric encryption:** Symmetric encryption uses shared secret key material to protect confidentiality, with suitable modes and key handling.
- **B — Digital signature:** A digital signature uses a private signing key and public verification key to authenticate signed content under a trust model.
- **C — Cryptographic hash:** A cryptographic hash produces a fixed-size digest without a secret key; an untrusted digest alone does not prove origin.

Coverage: M20; CEH v5 domain 9; Cryptographic primitives.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-MOCK-A-Q047

**Answer: A — Region and service coverage**

Logging and controls must cover the actual regions and services in use rather than assuming one configured location covers everything.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Cloud audit trail:** Audit records capture supported management or data events; configuration, retention and protection determine their investigative usefulness.
- **C — Function event validation:** Validate untrusted event data and authorization even when a managed platform invokes the function.
- **D — Execution and concurrency limits:** Bound function work and concurrency to control availability and cost exposure within platform capabilities.

Coverage: M19; CEH v5 domain 8; Serverless and audit.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-MOCK-A-Q048

**Answer: C — Centralized audit collection**

Forwarding logs to a protected separate system reduces dependence on a potentially altered endpoint's local records.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Application control:** Application control restricts execution according to an approved policy rather than trusting any executable a user can write.
- **B — Patch the vulnerable component:** Patching removes a known software weakness when the relevant fix is installed and effective.
- **D — Restrict credential exposure:** Protect credential stores, reduce unnecessary privileged logons and limit reusable credential material.

Coverage: M06; CEH v5 domain 3; Host defense.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-MOCK-A-Q049

**Answer: C — Context-appropriate output encoding**

Encoding must match the output context so untrusted data remains data rather than executable syntax.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Stored XSS:** Stored XSS persists malicious input in data later rendered to other users in an unsafe execution context.
- **B — Reflected XSS:** Reflected XSS returns request-supplied input in a response where the browser executes it.
- **D — DOM-based XSS:** DOM-based XSS arises when client-side code moves untrusted data into an unsafe browser sink.

Coverage: M14; CEH v5 domain 5; XSS contexts.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-A-Q050

**Answer: B — False negative**

A false negative fails to report a problem that actually exists.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — True negative:** A true negative correctly leaves an absent condition unreported.
- **C — True positive:** A true positive correctly identifies a condition that is actually present.
- **D — False positive:** A false positive reports a problem that is not actually present under the assessed conditions.

Coverage: M05; CEH v5 domain 3; Finding accuracy.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-MOCK-A-Q051

**Answer: A — Trusted update chain**

A trusted update chain authenticates software updates and relies on supported, correctly deployed versions.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Permission model:** Permissions control access to protected capabilities or data; an app should request only what its function needs.
- **C — Rooting or jailbreaking:** Rooting or jailbreaking changes platform restrictions and can weaken assumptions made by applications and management controls.
- **D — Application sandbox:** A sandbox separates application resources and constrains access, though flaws or granted interfaces can cross that boundary.

Coverage: M17; CEH v5 domain 7; Mobile platform boundaries.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-MOCK-A-Q052

**Answer: C — Memory analysis**

Memory analysis inspects volatile state such as loaded modules, processes and in-memory content.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Dynamic analysis:** Dynamic analysis observes behavior while a sample runs in an appropriately controlled environment.
- **B — Static analysis:** Static analysis inspects a sample's code or structure without intentionally executing its behavior.
- **D — Network analysis:** Network analysis studies communications, destinations, protocols and timing rather than relying only on file contents.

Coverage: M07; CEH v5 domain 3; Analysis methods.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-MOCK-A-Q053

**Answer: D — Command and control**

Command-and-control communication lets an external controller coordinate or task an implanted component.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Fileless execution:** Fileless techniques emphasize memory or existing interpreters and system facilities; they can still leave observable artifacts.
- **B — Keylogging:** Keylogging captures keystrokes and can expose entered secrets or sensitive content.
- **C — Botnet participation:** A bot joins a group of compromised devices controlled to perform coordinated activity.

Coverage: M07; CEH v5 domain 3; Malware behavior.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-MOCK-A-Q054

**Answer: A — Device patching**

Firmware and software updates address applicable implementation flaws; supported versions and deployment state need verification.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Discoverability:** Discoverability affects whether a Bluetooth device announces itself for discovery; it is not a substitute for authentication or updates.
- **C — Unnecessary service exposure:** Unused Bluetooth services or permissions create avoidable opportunities for interaction.
- **D — Pairing and association:** Pairing establishes security relationships using a selected method whose resistance to interception or impersonation varies.

Coverage: M16; CEH v5 domain 6; Bluetooth concepts.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-MOCK-A-Q055

**Answer: D — Rate and reliability tradeoff**

Aggressive probing can increase loss, load or false negatives; reliable testing uses suitable rates and conditions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Transport distinction:** TCP and UDP maintain separate port spaces; a result for one does not establish the other.
- **B — Scan-vantage dependence:** Results describe the path, source location and time of observation; another network path may expose different behavior.
- **C — Banner uncertainty:** A banner or fingerprint may be customized, hidden or affected by a proxy, so product claims need corroboration.

Coverage: M03; CEH v5 domain 2; Interpreting scan limits.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-MOCK-A-Q056

**Answer: B — Persistence**

Persistence provides a way to retain or regain access after interruptions such as restart or session loss.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Horizontal access violation:** Horizontal access violates boundaries between subjects at a similar privilege level, such as two customer accounts.
- **C — Lateral movement:** Lateral movement extends access to other systems or resources within an environment.
- **D — Vertical privilege escalation:** Vertical escalation gains permissions above the current privilege level on a system or application.

Coverage: M06; CEH v5 domain 3; Privilege and movement.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-MOCK-A-Q057

**Answer: D — Forward secrecy**

Forward secrecy protects past session keys against later compromise of a long-term key when the protocol and key exchange provide it.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Preimage resistance:** Preimage resistance makes finding an input for a specified hash output computationally impractical under the intended security level.
- **B — Second-preimage resistance:** Second-preimage resistance makes finding a different input with the same digest as a given input impractical.
- **C — Collision resistance:** Collision resistance makes finding any two distinct inputs with the same digest impractical under the intended security level.

Coverage: M20; CEH v5 domain 9; Security properties.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-MOCK-A-Q058

**Answer: C — Reciprocity**

Reciprocity exploits a person's perceived obligation to return a favor or benefit.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Scarcity:** Scarcity suggests that an opportunity or resource is limited and may soon disappear.
- **B — Urgency:** Urgency pressures a person to act quickly before examining the request.
- **D — Authority:** Authority cues exploit apparent rank or trusted institutional status to discourage verification.

Coverage: M09; CEH v5 domain 4; Influence mechanisms.
Technical references: [CISA phishing guidance](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing) · [MITRE phishing](https://attack.mitre.org/techniques/T1566/) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-A-Q059

**Answer: B — Layered detection**

Combine complementary signals so one visibility limitation does not determine the whole conclusion.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — False-negative reduction:** Improve coverage for real events that current detections miss, using appropriate telemetry and validation.
- **C — False-positive reduction:** Reduce incorrect alerts using validated context and careful rule tuning rather than suppressing all visibility.
- **D — Baseline-aware detection:** Interpret anomalies relative to relevant normal behavior while recognizing that a baseline can itself include unwanted activity.

Coverage: M12; CEH v5 domain 4; Detection tuning.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-MOCK-A-Q060

**Answer: C — Phishing-resistant authentication**

Origin-bound cryptographic authentication resists many credential-phishing flows, while broader social engineering still needs controls.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Reporting channel:** A simple trusted reporting path lets recipients raise suspicious requests without continuing the interaction.
- **B — Dual approval:** Require a second authorized reviewer for sensitive changes or transfers so one deceived person is insufficient.
- **D — Independent callback:** Verify a sensitive request through a known trusted contact path, not a number or link supplied by the requester.

Coverage: M09; CEH v5 domain 4; Verification controls.
Technical references: [CISA phishing guidance](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing) · [MITRE phishing](https://attack.mitre.org/techniques/T1566/) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-A-Q061

**Answer: D — Behavior-based detection**

Behavior-based detection looks for suspicious actions or sequences rather than only exact file patterns.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Reputation checking:** Reputation uses previously collected trust or threat information about an indicator; an unknown reputation is not proof of safety.
- **B — Allowlisting:** Allowlisting permits only approved software or behavior under a defined policy, reducing the execution set.
- **C — Signature detection:** Signature detection matches known patterns; unseen or changed implementations may evade a particular signature.

Coverage: M07; CEH v5 domain 3; Detection approaches.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-MOCK-A-Q062

**Answer: D — Detective control**

A detective control identifies activity or conditions that may already have occurred.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Corrective control:** A corrective control repairs a harmful state or restores service after a problem.
- **B — Preventive control:** A preventive control attempts to stop an unwanted action before it succeeds.
- **C — Deterrent control:** A deterrent control discourages an action by communicating consequences or increasing perceived risk.

Coverage: M01; CEH v5 domain 1; Control function.
Technical references: [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST CSF 2.0](https://www.nist.gov/cyberframework)

### CEH26-MOCK-A-Q063

**Answer: B — Service identity corroboration**

Confirm service identity with protocol behavior or trusted host information instead of relying only on a conventional port number.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Effective permission testing:** Check the actual allowed operation under the specific identity; listed configuration alone may not show the effective result.
- **C — Scope-preserving continuation:** Continue only within authorized targets and methods; newly discovered endpoints do not automatically expand scope.
- **D — Sensitive-output protection:** Protect enumeration output because account names, paths and configuration details may aid later misuse.

Coverage: M04; CEH v5 domain 2; Enumeration result quality.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-A-Q064

**Answer: B — Unsafe WebView boundary**

A WebView that exposes privileged bridges or loads untrusted content can cross from web input into app capabilities.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Exposed interprocess component:** An exported component can receive calls from other applications; intended caller permissions and input handling matter.
- **C — Clipboard exposure:** Sensitive content placed on a clipboard may be available beyond the intended app, depending on platform behavior and context.
- **D — Unsafe deep-link handling:** Deep links can deliver untrusted parameters or navigation requests and must not bypass authentication or validation.

Coverage: M17; CEH v5 domain 7; Application interaction.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-MOCK-A-Q065

**Answer: C — TLS handshake metadata**

Handshake metadata can reveal protocol negotiation or certificates where visible, without necessarily exposing application content.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — TCP reset:** A reset abruptly rejects or terminates a TCP connection; its cause needs surrounding context.
- **B — TCP retransmission:** A retransmission repeats data thought to be unacknowledged; loss, delay or capture artifacts require investigation.
- **D — DNS query and response:** DNS messages connect a question with an answer, but a captured answer still requires trust and freshness checks.

Coverage: M08; CEH v5 domain 4; Capture interpretation.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-MOCK-A-Q066

**Answer: C — Remote response actions**

Remote lock, wipe or session revocation can reduce incident exposure, but depend on reachability, scope and platform behavior.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Conditional access:** Access decisions can consider managed-device posture and other signals, while accounting for signal reliability.
- **B — Work-profile separation:** Separate managed work data and applications from personal contexts where the platform supports that boundary.
- **D — MDM policy:** Mobile device management enforces supported device policies and configuration, subject to enrollment and platform capabilities.

Coverage: M17; CEH v5 domain 7; Enterprise mobile controls.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-MOCK-A-Q067

**Answer: A — Rootkit behavior**

A rootkit hides or manipulates system views to conceal activity, often requiring privileged access.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Log tampering:** Log tampering alters or removes audit records and can damage the ability to reconstruct activity.
- **C — Alternate data stream:** On a supporting filesystem, an alternate data stream associates additional data with a file beyond its primary unnamed stream.
- **D — Process injection:** Process injection runs code within another process, potentially changing the apparent execution context.

Coverage: M06; CEH v5 domain 3; Execution and hiding.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-MOCK-A-Q068

**Answer: D — Source corroboration**

Corroboration compares independent evidence because a single public record may be incomplete, stale or misleading.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Passive-source research:** Passive-source research uses already available third-party information without probing the target service directly.
- **B — Data minimization:** Data minimization limits collection to information actually needed for the authorized purpose.
- **C — Active reconnaissance:** Active reconnaissance sends requests or probes to the target or its infrastructure and requires appropriate scope.

Coverage: M02; CEH v5 domain 2; Passive and active reconnaissance.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-MOCK-A-Q069

**Answer: B — RPC service discovery**

RPC service discovery reveals registered remote procedure services or their mapped endpoints.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — NetBIOS name information:** NetBIOS name data can expose host or service naming information but does not prove the underlying system is compromised.
- **C — NFS export enumeration:** NFS export information identifies shared filesystem paths and allowed clients; advertised access still needs scoped verification.
- **D — DNS zone transfer:** A zone transfer can disclose an entire zone when the server permits the requesting client to obtain it.

Coverage: M04; CEH v5 domain 2; Service-specific enumeration.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-A-Q070

**Answer: A — Passive-first observation**

Where active tests could affect fragile systems, approved passive evidence may be the appropriate initial assessment method.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Safety impact:** OT security decisions must consider possible harm to people, equipment and the physical process, not only data loss.
- **C — Process availability:** Industrial operations may require continuity and predictable control behavior; unplanned disruption can have physical consequences.
- **D — Change coordination:** Changes to operational systems require the process owner's approved timing, validation and recovery procedures.

Coverage: M18; CEH v5 domain 7; OT priorities.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-MOCK-A-Q071

**Answer: D — Confidentiality**

Confidentiality prevents information from being disclosed to unauthorized readers.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Integrity:** Integrity protects information against unauthorized alteration or destruction.
- **B — Accountability:** Accountability links actions to identifiable actors so activity can be reviewed.
- **C — Availability:** Availability keeps a service or information accessible when authorized users need it.

Coverage: M01; CEH v5 domain 1; Security objectives.
Technical references: [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST CSF 2.0](https://www.nist.gov/cyberframework)

### CEH26-MOCK-A-Q072

**Answer: B — Certificate pinning tradeoff**

Pinning constrains acceptable credentials but needs a careful rotation and recovery design; it is not a replacement for sound TLS handling.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Cleartext transport exposure:** Unprotected transport can expose application data to observers or modification on the path.
- **C — Backend authorization:** The server must validate subject and object permissions regardless of checks performed by the mobile client.
- **D — TLS trust validation:** Validate peer identity and trust for protected connections instead of accepting any certificate.

Coverage: M17; CEH v5 domain 7; Mobile network security.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-MOCK-A-Q073

**Answer: B — Fail-safe behavior**

On failure or uncertainty, a device should move to the defined safe operational condition rather than an arbitrary convenient state.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Replay protection:** Use appropriate freshness, sequence or challenge mechanisms so an old valid message cannot be reused as a new command.
- **C — Topic or resource authorization:** Authenticate a client and separately check which topics or resources it may read or modify.
- **D — Message authenticity:** Verify that commands or measurements come from an authorized sender and have not been altered under the chosen trust model.

Coverage: M18; CEH v5 domain 7; IoT data and trust.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-MOCK-A-Q074

**Answer: A — WAF defense-in-depth limitation**

A WAF may block some patterns but does not remove unsafe query construction in the application.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Stored procedure review:** A stored procedure can still be injectable if it constructs unsafe dynamic SQL internally.
- **C — Input escaping limitation:** Escaping depends on context, encoding and database rules and is more error-prone than separating query structure from values.
- **D — Client-side check limitation:** Browser validation can be bypassed; the server and database interaction must enforce the security boundary.

Coverage: M15; CEH v5 domain 5; Misleading defenses.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-A-Q075

**Answer: C — Authenticated encryption**

Authenticated encryption, such as correctly used GCM, protects confidentiality and detects tampering while still requiring proper nonce and key handling.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — ECB pattern leakage:** ECB independently encrypts equal plaintext blocks under the same key into equal ciphertext blocks, exposing repeated structure.
- **B — CBC IV requirement:** CBC encryption needs a suitable unpredictable initialization vector and separate integrity protection when used without an authenticated construction.
- **D — CTR nonce uniqueness:** CTR-style encryption requires avoiding reuse of the relevant nonce/counter stream under the same key, or plaintext relationships can leak.

Coverage: M20; CEH v5 domain 9; Encryption modes.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-MOCK-A-Q076

**Answer: D — Name-only evidence**

A discovered name is a lead; it does not establish that the account is active, accessible or authorized for testing.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Excessive write permission:** Excessive write access lets an account alter resources outside its legitimate responsibilities.
- **B — Excessive read permission:** Excessive read access grants an authenticated account more information than its role requires.
- **C — Anonymous information exposure:** Anonymous exposure occurs when useful information can be read without supplying an authenticated identity.

Coverage: M04; CEH v5 domain 2; Identity and access findings.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-A-Q077

**Answer: B — Wireless intrusion monitoring**

Monitoring identifies unexpected APs, identities and radio behavior for investigation, subject to placement and coverage limits.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Wireless segmentation:** Separate guest, managed and sensitive traffic with enforced network policy rather than trusting association alone.
- **C — Protected management frames:** PMF protects selected management frames against certain forgery and replay attacks; it does not prevent radio jamming.
- **D — Server certificate validation:** Validating the expected authentication server certificate helps prevent clients from trusting an impostor enterprise authentication endpoint.

Coverage: M16; CEH v5 domain 6; Wireless controls.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-MOCK-A-Q078

**Answer: A — SMB**

SMB provides file-sharing and related services, with access governed by authentication, share and file permissions.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — LDAP:** LDAP queries directory objects and attributes, with access constrained by authentication and directory permissions.
- **C — SNMP:** SNMP exposes management data through defined objects; security depends on version and access configuration.
- **D — SMTP:** SMTP transfers email; some server commands or responses can reveal recipient information when enabled.

Coverage: M04; CEH v5 domain 2; Enumeration protocols.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-A-Q079

**Answer: A — WPA2-Personal PSK**

WPA2-Personal commonly uses a shared passphrase-derived key; weak passphrases can be exposed to offline guessing from suitable captured authentication material.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Enterprise 802.1X/EAP:** Enterprise authentication uses an EAP method and authentication infrastructure, with method selection and certificate validation affecting security.
- **C — Open network:** An ordinary open network does not provide password-based link authentication or conventional WPA protection; higher-layer protections remain important.
- **D — WPA3-Personal SAE:** SAE is a password-authenticated key exchange used by WPA3-Personal and improves resistance to passive offline password guessing when correctly deployed.

Coverage: M16; CEH v5 domain 6; Wireless authentication.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-MOCK-A-Q080

**Answer: C — Verbose error disclosure**

Detailed error responses can expose internal paths, versions or implementation information useful to an attacker.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Directory listing:** Directory listing reveals files when a server generates an index for a directory without a suitable default document or restriction.
- **B — Default content exposure:** Default pages, sample applications or unused administrative components can reveal information or add unnecessary attack surface.
- **D — Path traversal:** Path traversal uses input to access paths outside the intended directory boundary when path handling is unsafe.

Coverage: M13; CEH v5 domain 5; Web-server exposure.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-A-Q081

**Answer: D — CVSS**

CVSS describes technical vulnerability severity using a defined scoring method; business priority needs additional context.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — NIST Cybersecurity Framework:** The CSF organizes cybersecurity risk management outcomes across functions including Govern, Identify, Protect, Detect, Respond and Recover.
- **B — Cyber Kill Chain:** The Cyber Kill Chain describes a staged intrusion lifecycle from preparation to actions on objectives.
- **C — MITRE ATT&CK:** ATT&CK organizes observed adversary tactics and techniques; it is not a vulnerability severity score.

Coverage: M01; CEH v5 domain 1; Framework purpose.
Technical references: [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST CSF 2.0](https://www.nist.gov/cyberframework)

### CEH26-MOCK-A-Q082

**Answer: A — Radio-frequency jamming**

Jamming interferes with the radio medium and can disrupt availability regardless of application-layer security.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Evil twin:** An evil twin impersonates a trusted wireless network to attract clients, often using a familiar network name.
- **C — Rogue access point:** A rogue access point is an unauthorized AP connected to or operating within an organization's environment.
- **D — Deauthentication abuse:** Forged or abusive management messages can disrupt associations where applicable protections are absent or insufficient.

Coverage: M16; CEH v5 domain 6; Wireless threats.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-MOCK-A-Q083

**Answer: D — Sandbox awareness**

A sample may detect analysis conditions and suppress behavior, so a quiet run does not prove safety.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Living off the land:** An attacker can misuse legitimate installed tools, so a trusted tool name alone does not establish benign intent.
- **B — Packing or obfuscation:** Packing and obfuscation alter representation to hinder inspection; their presence alone does not prove malicious intent.
- **C — False positive investigation:** An alert must be assessed against context and corroborating evidence before being treated as confirmed malicious behavior.

Coverage: M07; CEH v5 domain 3; Evasion and uncertainty.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-MOCK-A-Q084

**Answer: B — Private-key protection**

Protect the private key from disclosure or misuse; a public certificate does not need to be kept secret.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Certificate-chain validation:** Validate a certificate through an accepted trust chain under the verifier's policy.
- **C — Hostname validation:** Check that the certificate identity matches the intended service name rather than merely trusting its issuer.
- **D — Validity and revocation handling:** Consider validity periods and applicable revocation mechanisms according to the client and deployment policy.

Coverage: M20; CEH v5 domain 9; PKI and certificates.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-MOCK-A-Q085

**Answer: A — Server-side request forgery**

SSRF causes a server to make unintended requests influenced by untrusted input, potentially crossing network trust boundaries.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — OS command injection:** Command injection lets untrusted input alter the intended operating-system command or its execution structure.
- **C — Broken object authorization:** Broken object authorization lets a subject access or change an object without the required object-level permission.
- **D — Cross-site scripting:** XSS occurs when untrusted content is interpreted as executable script in a browser context.

Coverage: M14; CEH v5 domain 5; Application weakness classes.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-A-Q086

**Answer: C — Trojan**

A Trojan presents an apparently useful or legitimate function while carrying hidden malicious behavior.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Virus:** A virus replicates by attaching to a host file or similar carrier and depends on that host's execution or activation.
- **B — Ransomware:** Ransomware denies access to data or systems, commonly through encryption, and demands payment; some campaigns also steal data.
- **D — Worm:** A worm can propagate between systems without needing to attach itself to an ordinary host file.

Coverage: M07; CEH v5 domain 3; Malware classes.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-MOCK-A-Q087

**Answer: C — Layered protection**

Link security, endpoint configuration and application encryption address different risks and should not be treated as interchangeable.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Association is not identity proof:** A matching network name or successful association does not establish that the network operator is the intended trusted party.
- **B — Offline artifact analysis:** A supplied sanitized capture can support protocol reasoning without transmitting or interfering with a live wireless network.
- **D — Authorized capture only:** Capture and testing must stay within approved networks, devices and methods, even when neighboring radio traffic is visible.

Coverage: M16; CEH v5 domain 6; Wireless evidence boundaries.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-MOCK-A-Q088

**Answer: B — Open or filtered**

The probe outcome cannot distinguish an open port from one whose traffic is silently filtered.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Open:** An open port has a service accepting the relevant transport connections or datagrams from the scanner's perspective.
- **C — Closed:** A closed port is reachable but has no service listening for the tested transport at that time.
- **D — Filtered:** Filtering prevents the scanner from determining whether a port is open or closed.

Coverage: M03; CEH v5 domain 2; Port states.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-MOCK-A-Q089

**Answer: C — Dynamic ARP inspection**

DAI validates ARP messages against trusted bindings or policy to reduce spoofed address mappings.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — DHCP snooping:** DHCP snooping distinguishes trusted DHCP paths and can build bindings used by other protections.
- **B — Authenticated encryption:** Correctly authenticated encryption protects traffic content and peer identity even when the local path is observable.
- **D — Port security:** Port security restricts learned or permitted source MAC addresses on a switch port according to policy.

Coverage: M08; CEH v5 domain 4; Layer-two defenses.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-MOCK-A-Q090

**Answer: A — Backpressure**

Backpressure limits accepted work or signals overload so downstream queues do not grow without bound.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Request cost limits:** Bound request complexity, body size or execution time so one request cannot consume unbounded work.
- **C — Per-identity quotas:** Quotas allocate a bounded share of resources to a user or tenant; identity design affects how easily limits can be bypassed.
- **D — Caching:** Caching reuses suitable prior results to reduce repeated computation, while correctness and invalidation remain important.

Coverage: M10; CEH v5 domain 4; Application resilience.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-MOCK-A-Q091

**Answer: C — Least-privilege database identity**

The application's database account should have only the operations and objects required for its function.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Bound parameters:** Bound parameters keep supplied values separate from SQL syntax when used correctly by the database API.
- **B — Allowlisted structural choices:** Identifiers or sort directions that cannot be bound as values should be selected from explicit approved structural choices.
- **D — Data interpreted as query syntax:** Injection arises when untrusted data can alter the intended SQL structure rather than remaining a bound value.

Coverage: M15; CEH v5 domain 5; Injection root cause.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-A-Q092

**Answer: C — Rollback protection**

Rollback protection prevents installation of disallowed older versions even if those versions were once correctly signed.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Unique device credentials:** Use distinct credentials per device rather than a shared default secret across a fleet.
- **B — Secure boot:** Secure boot verifies the authorized boot chain and helps prevent execution of untrusted boot components.
- **D — Authenticated firmware update:** Verify update authenticity and integrity before accepting firmware; signature checks need a trusted key and correct implementation.

Coverage: M18; CEH v5 domain 7; Device lifecycle security.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-MOCK-A-Q093

**Answer: D — Written authorization and scope**

Permission must identify who may test which assets, by which methods, and under what limits.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Evidence handling:** Evidence handling records origin and preserves artifacts so later conclusions remain supportable.
- **B — Responsible disclosure:** A disclosure process routes a finding to the appropriate owner while limiting unnecessary exposure.
- **C — Rules of engagement:** Rules of engagement define operational conditions such as timing, contacts, escalation and stopping criteria.

Coverage: M01; CEH v5 domain 1; Assessment authority.
Technical references: [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST CSF 2.0](https://www.nist.gov/cyberframework)

### CEH26-MOCK-A-Q094

**Answer: C — Baiting**

Baiting offers an appealing object or benefit to induce an unsafe action, such as opening untrusted media.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Dumpster diving:** Dumpster diving seeks useful information from discarded materials.
- **B — Tailgating:** Tailgating gains entry by following an authorized person through an access-controlled boundary without proper authorization.
- **D — Shoulder surfing:** Shoulder surfing observes a person's screen, keyboard or similar visible activity to learn sensitive information.

Coverage: M09; CEH v5 domain 4; Physical deception.
Technical references: [CISA phishing guidance](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing) · [MITRE phishing](https://attack.mitre.org/techniques/T1566/) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-A-Q095

**Answer: B — Replay sanitized fixtures**

Use approved recorded or synthetic data to check a detection without creating harmful live traffic.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Compare expected and observed alerts:** A detection test needs a declared expected outcome and an actual observation to establish coverage.
- **C — Preserve rollback and ownership:** A control change needs an accountable owner and a practical reversal path when its effects are unacceptable.
- **D — Measure legitimate impact:** Check latency, errors and valid-user success so a blocking rule does not silently damage normal operation.

Coverage: M12; CEH v5 domain 4; Safe validation.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-MOCK-A-Q096

**Answer: A — -sV**

The -sV option requests service/version detection for discovered ports.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — -O:** The -O option requests operating-system detection, subject to privileges and useful probe conditions.
- **C — -sn:** The -sn option performs host discovery without the normal port scan.
- **D — -Pn:** The -Pn option skips host discovery and treats specified targets as up for subsequent scanning; it does not make traffic invisible.

Coverage: M03; CEH v5 domain 2; Nmap option meaning.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-MOCK-A-Q097

**Answer: D — Accountability**

Accountability links actions to identifiable actors so activity can be reviewed.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Confidentiality:** Confidentiality prevents information from being disclosed to unauthorized readers.
- **B — Availability:** Availability keeps a service or information accessible when authorized users need it.
- **C — Integrity:** Integrity protects information against unauthorized alteration or destruction.

Coverage: M01; CEH v5 domain 1; Security objectives.
Technical references: [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST CSF 2.0](https://www.nist.gov/cyberframework)

### CEH26-MOCK-A-Q098

**Answer: D — Management-plane restriction**

Restricting management traffic to approved sources reduces who can reach the service.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — SNMPv1/v2c community model:** SNMPv1 and v2c use community strings and do not provide the cryptographic protections offered by SNMPv3 USM.
- **B — Read-only management access:** Read-only permissions limit queries to reading permitted management objects rather than modifying them.
- **C — SNMPv3 authPriv:** The authPriv security level adds message authentication and privacy when correctly configured.

Coverage: M04; CEH v5 domain 2; SNMP security.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-A-Q099

**Answer: A — SMTP**

SMTP transfers email; some server commands or responses can reveal recipient information when enabled.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — SMB:** SMB provides file-sharing and related services, with access governed by authentication, share and file permissions.
- **C — SNMP:** SNMP exposes management data through defined objects; security depends on version and access configuration.
- **D — LDAP:** LDAP queries directory objects and attributes, with access constrained by authentication and directory permissions.

Coverage: M04; CEH v5 domain 2; Enumeration protocols.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-A-Q100

**Answer: B — Process and endpoint evidence**

Host-level process, execution and connection information can corroborate what a web request actually caused.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Error log:** An error log records server or application failures and can provide context absent from the client response.
- **C — Access log:** An access log records request activity as configured, such as path, status, client information and timing.
- **D — File integrity evidence:** Trusted file comparisons help detect unexpected changes to deployed content, subject to a trustworthy baseline.

Coverage: M13; CEH v5 domain 5; Web incident evidence.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-A-Q101

**Answer: B — Rule review and expiry**

Review ownership and continued need, and expire temporary exceptions to prevent stale access paths.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Default deny:** Default deny rejects traffic unless an explicit policy permits it.
- **C — Egress filtering:** Egress filtering controls outbound connections and can reduce unnecessary external communication paths.
- **D — Least-necessary rules:** Rules should permit only the source, destination, service and conditions required for the business purpose.

Coverage: M12; CEH v5 domain 4; Firewall policy.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-MOCK-A-Q102

**Answer: D — Time-based blind SQL injection**

Time-based blind injection infers execution from controlled timing differences, which require repeated context-aware validation.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Boolean-based blind SQL injection:** Boolean-based blind injection infers a condition from consistent differences between true and false responses.
- **B — Union-based SQL injection:** Union-based injection combines compatible query results so additional data may appear in the application's response.
- **C — Error-based SQL injection:** Error-based injection uses database error behavior or disclosed error details to learn about query execution or data.

Coverage: M15; CEH v5 domain 5; SQL injection types.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-A-Q103

**Answer: A — 500 Internal Server Error**

HTTP 500 indicates an unexpected server-side condition; the response alone does not prove a particular exploit succeeded.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — 401 Unauthorized:** HTTP 401 indicates that valid authentication credentials are required for the target resource; protocol details include the applicable challenge.
- **C — 403 Forbidden:** HTTP 403 indicates that the server understood the request but refuses it; the reason is not necessarily missing authentication.
- **D — 404 Not Found:** HTTP 404 reports that the target resource is not found or is not being disclosed; it does not prove a file never existed.

Coverage: M13; CEH v5 domain 5; Server response evidence.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-A-Q104

**Answer: D — Error disclosure**

Detailed database errors reveal internal information, but hiding them does not repair unsafe query construction.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Database-specific behavior:** SQL syntax, functions and error messages vary by database; a response must be interpreted in the correct implementation context.
- **B — Query execution evidence:** A finding needs evidence that input changed database execution, not merely that the application displayed an unusual response.
- **C — Timing uncertainty:** Network jitter, caching and ordinary load can change response time, so one delay is not conclusive injection evidence.

Coverage: M15; CEH v5 domain 5; Database evidence.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-A-Q105

**Answer: B — Black-box assessment**

A black-box assessment begins with little or no internal knowledge of the target.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Gray-box assessment:** A gray-box assessment provides limited internal knowledge or a representative user account.
- **C — Vulnerability assessment:** A vulnerability assessment identifies and prioritizes weaknesses; it does not necessarily demonstrate exploitation.
- **D — White-box assessment:** A white-box assessment gives testers substantial internal information such as code and architecture.

Coverage: M01; CEH v5 domain 1; Assessment visibility.
Technical references: [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST CSF 2.0](https://www.nist.gov/cyberframework)

### CEH26-MOCK-A-Q106

**Answer: D — Open**

An open port has a service accepting the relevant transport connections or datagrams from the scanner's perspective.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Open or filtered:** The probe outcome cannot distinguish an open port from one whose traffic is silently filtered.
- **B — Closed:** A closed port is reachable but has no service listening for the tested transport at that time.
- **C — Filtered:** Filtering prevents the scanner from determining whether a port is open or closed.

Coverage: M03; CEH v5 domain 2; Port states.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-MOCK-A-Q107

**Answer: A — Historian**

A historian stores time-series process data for analysis and operational records.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — HMI:** A human-machine interface presents process information and controls to an operator.
- **C — SCADA:** SCADA supervises and gathers data across industrial operations, often involving distributed control assets.
- **D — PLC:** A programmable logic controller executes control logic and interfaces with process inputs and outputs.

Coverage: M18; CEH v5 domain 7; Industrial roles.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-MOCK-A-Q108

**Answer: C — Availability impact**

A database operation can degrade or stop service through excessive work, locks or destructive changes.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Authentication bypass:** A manipulated query can incorrectly satisfy an authentication decision when that decision relies on unsafe SQL construction.
- **B — Unauthorized read:** A flaw can expose records that the current subject is not allowed to retrieve.
- **D — Unauthorized modification:** A flaw can change or delete data beyond the application's intended permitted operation.

Coverage: M15; CEH v5 domain 5; Impact boundaries.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-A-Q109

**Answer: C — Data classification and placement**

Classify information and choose approved storage locations, retention and handling requirements for that class.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Versioning and recovery:** Retained versions or backups can support recovery, subject to retention, deletion privileges and restore testing.
- **B — Public access control:** Review whether storage resources permit anonymous or unintended principals, including effective policy combinations.
- **D — Encryption and key control:** Storage encryption protects data under a key-management model; it does not replace authorization to read decrypted objects.

Coverage: M19; CEH v5 domain 8; Storage and data.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-MOCK-A-Q110

**Answer: B — OPTIONS**

OPTIONS describes communication options for a target or server, but advertised methods do not prove they are usable by every identity.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — PUT:** PUT requests creation or replacement of the target resource's state; enabling it does not by itself prove unauthorized write access.
- **C — POST:** POST submits data for resource-specific processing and may change state; authorization and CSRF controls still matter.
- **D — GET:** GET requests a representation and is defined with safe semantics; applications should not use it for unintended state-changing operations.

Coverage: M13; CEH v5 domain 5; HTTP method interpretation.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-A-Q111

**Answer: A — Secret delivery**

Deliver secrets through appropriate restricted mechanisms rather than embedding them in images, code or broadly visible configuration.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Orchestrator RBAC:** Restrict which identities can perform operations on cluster resources, including sensitive administrative actions.
- **C — Container isolation boundary:** Containers usually share a host kernel; isolation is not equivalent to a completely independent hardware machine.
- **D — Image provenance and maintenance:** Use trustworthy images and maintain their dependencies; a signed origin alone does not mean the contents are vulnerability-free.

Coverage: M19; CEH v5 domain 8; Containers and orchestration.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-MOCK-A-Q112

**Answer: D — Business-logic validation**

Validate workflow-specific rules, sequence and state transitions rather than only input syntax.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — CORS policy:** CORS controls whether browser scripts may read certain cross-origin responses; it is not a substitute for server authorization.
- **B — Server-side validation:** The server must enforce important constraints because clients can modify or bypass browser-side checks.
- **C — Content Security Policy:** CSP can constrain browser resource and script execution as defense in depth, but does not replace fixing injection paths.

Coverage: M14; CEH v5 domain 5; Browser and API trust.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-A-Q113

**Answer: D — Data minimization**

Data minimization limits collection to information actually needed for the authorized purpose.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Passive-source research:** Passive-source research uses already available third-party information without probing the target service directly.
- **B — Active reconnaissance:** Active reconnaissance sends requests or probes to the target or its infrastructure and requires appropriate scope.
- **C — Source corroboration:** Corroboration compares independent evidence because a single public record may be incomplete, stale or misleading.

Coverage: M02; CEH v5 domain 2; Passive and active reconnaissance.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-MOCK-A-Q114

**Answer: B — Sensitive-data minimization**

Avoid storing secrets or personal data that the mobile workflow does not actually need.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Local encryption boundary:** Encryption protects stored data only within its key and threat model; an unlocked compromised runtime may still access plaintext.
- **C — Platform-protected key storage:** Use appropriate platform-backed key facilities rather than hardcoding private keys or keeping them as ordinary files.
- **D — Backup and log review:** Backups and diagnostic logs can expose data even when the main app screen hides it.

Coverage: M17; CEH v5 domain 7; Mobile data storage.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-MOCK-A-Q115

**Answer: C — Honeypot**

A honeypot is a deliberately observed decoy resource used to learn about or detect interactions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — IPS:** An intrusion prevention system can inspect and block traffic in its enforcement path.
- **B — IDS:** An intrusion detection system observes activity and generates detections; a passive deployment does not directly block traffic.
- **D — Firewall:** A firewall enforces traffic policy at its supported layers; permitted traffic is not automatically safe application behavior.

Coverage: M12; CEH v5 domain 4; Security device roles.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-MOCK-A-Q116

**Answer: B — Signing is not confidentiality**

A signature can authenticate content while leaving that content readable to anyone who receives it.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Encoding is not encryption:** Encoding changes representation for interoperability and generally provides no secret-based confidentiality.
- **C — Steganography hides presence:** Steganography hides information within another carrier; secrecy of content may still require encryption.
- **D — Hashing is not password encryption:** Password verification normally uses a suitable one-way password KDF and salt rather than reversible encryption or a fast unsalted hash.

Coverage: M20; CEH v5 domain 9; Common confusions.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-MOCK-A-Q117

**Answer: A — Reflection**

Reflection sends replies from third-party services toward a victim, often by using a spoofed source address in requests.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Amplification:** Amplification produces responses substantially larger than the triggering requests.
- **C — Source-address validation:** Ingress or egress validation reduces spoofed source traffic when applied appropriately in the network.
- **D — Response rate limiting:** Response rate limiting constrains repeated or excessive replies, reducing some abusive response patterns.

Coverage: M10; CEH v5 domain 4; Reflection and amplification.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-MOCK-A-Q118

**Answer: A — Risk**

Risk concerns the likelihood and consequences of an adverse event in a particular context.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Exploit:** An exploit is a method or mechanism that takes advantage of a vulnerability.
- **C — Threat:** A threat is a potential cause of an adverse event, such as an actor or harmful circumstance.
- **D — Vulnerability:** A vulnerability is a weakness that could be exploited under relevant conditions.

Coverage: M05; CEH v5 domain 3; Weakness and risk.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-MOCK-A-Q119

**Answer: C — Contain the affected system**

Containment limits further harm or spread while preserving the ability to investigate.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Eradicate the cause:** Eradication removes malicious components and the access or weakness that enabled the incident.
- **B — Recover and verify:** Recovery restores trusted service and checks that business function and security controls operate as expected.
- **D — Preserve relevant evidence:** Preservation retains necessary logs, volatile data or artifacts before actions that could destroy them, where operational safety permits.

Coverage: M07; CEH v5 domain 3; Response priorities.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-MOCK-A-Q120

**Answer: B — Least privilege**

Least privilege grants only the permissions needed for the assigned task and duration.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Authentication:** Authentication verifies a claimed identity using an accepted credential or mechanism.
- **C — Authorization:** Authorization decides which actions an authenticated or otherwise identified subject may perform.
- **D — Separation of duties:** Separation of duties divides sensitive responsibilities so one actor cannot complete the whole risky process alone.

Coverage: M01; CEH v5 domain 1; Identity and assurance.
Technical references: [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST CSF 2.0](https://www.nist.gov/cyberframework)

### CEH26-MOCK-A-Q121

**Answer: A — Configuration review**

A configuration review compares settings and effective controls with defined requirements.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Credentialed assessment:** A credentialed assessment uses authorized access to inspect information unavailable to an unauthenticated probe.
- **C — Unauthenticated assessment:** An unauthenticated assessment observes exposure without logging in; its visibility is limited to that perspective.
- **D — Manual validation:** Manual validation investigates a finding's applicability or behavior beyond an automated label.

Coverage: M05; CEH v5 domain 3; Assessment access.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-MOCK-A-Q122

**Answer: C — Secure destruction and retention**

Retain keys only as needed and destroy them appropriately when their authorized lifetime ends, considering recovery obligations.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Key separation:** Use keys for their intended purpose and trust boundary rather than reusing one key across unrelated functions.
- **B — Rotation and revocation:** Replace or invalidate keys when required while managing dependent systems and retained data.
- **D — Cryptographically secure randomness:** Security-sensitive keys and nonces need an appropriate unpredictable generator and correct construction-specific handling.

Coverage: M20; CEH v5 domain 9; Key lifecycle.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-MOCK-A-Q123

**Answer: B — Application session boundary**

An application session has its own credentials and lifecycle, distinct from the lifetime of a single transport connection.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — On-path interception:** An on-path position can observe or influence traffic between peers; encryption and authentication constrain useful tampering.
- **C — TCP sequence validation:** TCP sequence numbers help a receiver place data within an expected stream; acceptable sequence state matters to forged segments.
- **D — TLS peer authentication:** Correct peer authentication helps prevent an intermediary from impersonating the intended TLS endpoint.

Coverage: M11; CEH v5 domain 4; Transport-session concepts.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-A-Q124

**Answer: D — Pass-the-hash**

Pass-the-hash uses an appropriate password hash as authentication material where the protocol and conditions permit it.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Kerberoasting:** Kerberoasting obtains suitable service-ticket material for offline guessing of a service account password.
- **B — Credential dumping:** Credential dumping extracts credential material from memory or stored system data; the material may take several forms.
- **C — Pass-the-ticket:** Pass-the-ticket reuses Kerberos ticket material rather than recovering the user's plaintext password.

Coverage: M06; CEH v5 domain 3; Windows credential concepts.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-MOCK-A-Q125

**Answer: A — SOA record**

An SOA record carries zone authority metadata including a serial number and timing values.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — PTR record:** A PTR record maps a reverse-DNS name toward a host name; it does not prove service ownership.
- **C — TXT record:** A TXT record carries text, including formats used by some email policies and ownership checks.
- **D — NS record:** An NS record identifies an authoritative name server for a DNS zone.

Coverage: M02; CEH v5 domain 2; Additional DNS data.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)
