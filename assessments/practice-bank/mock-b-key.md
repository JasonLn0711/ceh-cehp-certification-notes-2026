# MOCK-B — instructor key v1.0.0

[Question form](mock-b.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-MOCK-B-Q001

**Answer: B — LDAP**

LDAP queries directory objects and attributes, with access constrained by authentication and directory permissions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — SMB:** SMB provides file-sharing and related services, with access governed by authentication, share and file permissions.
- **C — SMTP:** SMTP transfers email; some server commands or responses can reveal recipient information when enabled.
- **D — SNMP:** SNMP exposes management data through defined objects; security depends on version and access configuration.

Coverage: M04; CEH v5 domain 2; Enumeration protocols.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-B-Q002

**Answer: C — Realism tradeoff**

A more realistic decoy may collect richer behavior but can require more containment and maintenance.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Isolation of the decoy:** Constrain a decoy so it cannot become an uncontrolled path into production or harm other systems.
- **B — Detection of deception:** Unrealistic banners, inconsistent behavior or known artifacts can reveal that a resource is a decoy.
- **D — Decoy interaction evidence:** Interaction with a decoy is an observation that needs context; it is not automatic proof of a particular actor or full compromise.

Coverage: M12; CEH v5 domain 4; Decoy limitations.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-MOCK-B-Q003

**Answer: D — Platform as a Service**

PaaS manages more of the application platform, while customers still manage their application logic, data and relevant configuration.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Software as a Service:** SaaS delivers an application operated by the provider, while customer identities, use and configuration still carry responsibilities.
- **B — Shared responsibility:** Security duties depend on the service and contract; using a provider does not eliminate the customer's responsibilities.
- **C — Infrastructure as a Service:** IaaS exposes infrastructure resources while customers typically manage guest operating systems and their workloads.

Coverage: M19; CEH v5 domain 8; Service models.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-MOCK-B-Q004

**Answer: D — Scarcity**

Scarcity suggests that an opportunity or resource is limited and may soon disappear.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Urgency:** Urgency pressures a person to act quickly before examining the request.
- **B — Authority:** Authority cues exploit apparent rank or trusted institutional status to discourage verification.
- **C — Reciprocity:** Reciprocity exploits a person's perceived obligation to return a favor or benefit.

Coverage: M09; CEH v5 domain 4; Influence mechanisms.
Technical references: [CISA phishing guidance](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing) · [MITRE phishing](https://attack.mitre.org/techniques/T1566/) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-B-Q005

**Answer: A — Unnecessary service exposure**

Unused Bluetooth services or permissions create avoidable opportunities for interaction.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Pairing and association:** Pairing establishes security relationships using a selected method whose resistance to interception or impersonation varies.
- **C — Discoverability:** Discoverability affects whether a Bluetooth device announces itself for discovery; it is not a substitute for authentication or updates.
- **D — Device patching:** Firmware and software updates address applicable implementation flaws; supported versions and deployment state need verification.

Coverage: M16; CEH v5 domain 6; Bluetooth concepts.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-MOCK-B-Q006

**Answer: A — Disable unnecessary anonymous queries**

Reduce unauthenticated information disclosure while preserving required service behavior.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Remove unnecessary legacy services:** Retire unused legacy discovery or sharing services to reduce avoidable exposure.
- **C — Monitor query patterns:** Log and review unusual enumeration volume or sensitive-object queries within appropriate operational limits.
- **D — Apply least-privilege access:** Grant directory, share and management access only to the identities and data needed for each role.

Coverage: M04; CEH v5 domain 2; Enumeration countermeasures.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-B-Q007

**Answer: B — Application control**

Application control restricts execution according to an approved policy rather than trusting any executable a user can write.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Restrict credential exposure:** Protect credential stores, reduce unnecessary privileged logons and limit reusable credential material.
- **C — Patch the vulnerable component:** Patching removes a known software weakness when the relevant fix is installed and effective.
- **D — Centralized audit collection:** Forwarding logs to a protected separate system reduces dependence on a potentially altered endpoint's local records.

Coverage: M06; CEH v5 domain 3; Host defense.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-MOCK-B-Q008

**Answer: B — White-box assessment**

A white-box assessment gives testers substantial internal information such as code and architecture.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Black-box assessment:** A black-box assessment begins with little or no internal knowledge of the target.
- **C — Vulnerability assessment:** A vulnerability assessment identifies and prioritizes weaknesses; it does not necessarily demonstrate exploitation.
- **D — Gray-box assessment:** A gray-box assessment provides limited internal knowledge or a representative user account.

Coverage: M01; CEH v5 domain 1; Assessment visibility.
Technical references: [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST CSF 2.0](https://www.nist.gov/cyberframework)

### CEH26-MOCK-B-Q009

**Answer: D — Signature detection**

Signature detection matches known patterns; unseen or changed implementations may evade a particular signature.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Behavior-based detection:** Behavior-based detection looks for suspicious actions or sequences rather than only exact file patterns.
- **B — Allowlisting:** Allowlisting permits only approved software or behavior under a defined policy, reducing the execution set.
- **C — Reputation checking:** Reputation uses previously collected trust or threat information about an indicator; an unknown reputation is not proof of safety.

Coverage: M07; CEH v5 domain 3; Detection approaches.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-MOCK-B-Q010

**Answer: C — Replay protection**

Use appropriate freshness, sequence or challenge mechanisms so an old valid message cannot be reused as a new command.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Fail-safe behavior:** On failure or uncertainty, a device should move to the defined safe operational condition rather than an arbitrary convenient state.
- **B — Message authenticity:** Verify that commands or measurements come from an authorized sender and have not been altered under the chosen trust model.
- **D — Topic or resource authorization:** Authenticate a client and separately check which topics or resources it may read or modify.

Coverage: M18; CEH v5 domain 7; IoT data and trust.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-MOCK-B-Q011

**Answer: D — Integrity**

Integrity protects information against unauthorized alteration or destruction.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Accountability:** Accountability links actions to identifiable actors so activity can be reviewed.
- **B — Availability:** Availability keeps a service or information accessible when authorized users need it.
- **C — Confidentiality:** Confidentiality prevents information from being disclosed to unauthorized readers.

Coverage: M01; CEH v5 domain 1; Security objectives.
Technical references: [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST CSF 2.0](https://www.nist.gov/cyberframework)

### CEH26-MOCK-B-Q012

**Answer: D — Allowlisted structural choices**

Identifiers or sort directions that cannot be bound as values should be selected from explicit approved structural choices.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Bound parameters:** Bound parameters keep supplied values separate from SQL syntax when used correctly by the database API.
- **B — Least-privilege database identity:** The application's database account should have only the operations and objects required for its function.
- **C — Data interpreted as query syntax:** Injection arises when untrusted data can alter the intended SQL structure rather than remaining a bound value.

Coverage: M15; CEH v5 domain 5; Injection root cause.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-B-Q013

**Answer: C — Authentication**

Authentication verifies a claimed identity using an accepted credential or mechanism.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Least privilege:** Least privilege grants only the permissions needed for the assigned task and duration.
- **B — Authorization:** Authorization decides which actions an authenticated or otherwise identified subject may perform.
- **D — Separation of duties:** Separation of duties divides sensitive responsibilities so one actor cannot complete the whole risky process alone.

Coverage: M01; CEH v5 domain 1; Identity and assurance.
Technical references: [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST CSF 2.0](https://www.nist.gov/cyberframework)

### CEH26-MOCK-B-Q014

**Answer: C — Living off the land**

An attacker can misuse legitimate installed tools, so a trusted tool name alone does not establish benign intent.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — False positive investigation:** An alert must be assessed against context and corroborating evidence before being treated as confirmed malicious behavior.
- **B — Packing or obfuscation:** Packing and obfuscation alter representation to hinder inspection; their presence alone does not prove malicious intent.
- **D — Sandbox awareness:** A sample may detect analysis conditions and suppress behavior, so a quiet run does not prove safety.

Coverage: M07; CEH v5 domain 3; Evasion and uncertainty.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-MOCK-B-Q015

**Answer: B — DNS zone transfer**

A zone transfer can disclose an entire zone when the server permits the requesting client to obtain it.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — NFS export enumeration:** NFS export information identifies shared filesystem paths and allowed clients; advertised access still needs scoped verification.
- **C — RPC service discovery:** RPC service discovery reveals registered remote procedure services or their mapped endpoints.
- **D — NetBIOS name information:** NetBIOS name data can expose host or service naming information but does not prove the underlying system is compromised.

Coverage: M04; CEH v5 domain 2; Service-specific enumeration.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-B-Q016

**Answer: A — Corrective control**

A corrective control repairs a harmful state or restores service after a problem.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Detective control:** A detective control identifies activity or conditions that may already have occurred.
- **C — Deterrent control:** A deterrent control discourages an action by communicating consequences or increasing perceived risk.
- **D — Preventive control:** A preventive control attempts to stop an unwanted action before it succeeds.

Coverage: M01; CEH v5 domain 1; Control function.
Technical references: [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST CSF 2.0](https://www.nist.gov/cyberframework)

### CEH26-MOCK-B-Q017

**Answer: A — Application sandbox**

A sandbox separates application resources and constrains access, though flaws or granted interfaces can cross that boundary.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Trusted update chain:** A trusted update chain authenticates software updates and relies on supported, correctly deployed versions.
- **C — Permission model:** Permissions control access to protected capabilities or data; an app should request only what its function needs.
- **D — Rooting or jailbreaking:** Rooting or jailbreaking changes platform restrictions and can weaken assumptions made by applications and management controls.

Coverage: M17; CEH v5 domain 7; Mobile platform boundaries.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-MOCK-B-Q018

**Answer: C — CoAP**

CoAP is designed for constrained environments and uses a resource-oriented request/response model, commonly over UDP.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Zigbee:** Zigbee supports low-power wireless networking for constrained devices; joining, keys and implementation security still matter.
- **B — Modbus:** Modbus supports industrial register-oriented communication; security depends on variant and deployment controls rather than assuming every installation authenticates commands.
- **D — MQTT:** MQTT uses a publish/subscribe model through a broker; authentication, topic authorization and transport protection require configuration.

Coverage: M18; CEH v5 domain 7; IoT protocol roles.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-MOCK-B-Q019

**Answer: D — Outcome-based measurement**

Measure the behavior relevant to the learning goal instead of treating one click count as complete competence evidence.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Participant protection:** Protect people from unnecessary harm and avoid collecting real passwords or unrelated sensitive information.
- **B — Constructive debrief:** A useful debrief explains cues and reporting actions without humiliating individuals.
- **C — Explicit campaign approval:** A social-engineering exercise needs authorized scope, targets, methods and escalation before delivery.

Coverage: M09; CEH v5 domain 4; Exercise governance.
Technical references: [CISA phishing guidance](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing) · [MITRE phishing](https://attack.mitre.org/techniques/T1566/) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-B-Q020

**Answer: B — Inventory public dependencies**

Track public names, certificates and vendor links so abandoned or unexpected dependencies can be investigated.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Restrict zone transfers:** Allow DNS zone transfers only to the intended authorized secondary servers.
- **C — Reduce published metadata:** Remove unnecessary author, path and software details from public documents and pages.
- **D — Use approved public contact roles:** Publish necessary role-based contacts while avoiding unnecessary personal staff details.

Coverage: M02; CEH v5 domain 2; Exposure reduction.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-MOCK-B-Q021

**Answer: A — Unique device credentials**

Use distinct credentials per device rather than a shared default secret across a fleet.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Rollback protection:** Rollback protection prevents installation of disallowed older versions even if those versions were once correctly signed.
- **C — Authenticated firmware update:** Verify update authenticity and integrity before accepting firmware; signature checks need a trusted key and correct implementation.
- **D — Secure boot:** Secure boot verifies the authorized boot chain and helps prevent execution of untrusted boot components.

Coverage: M18; CEH v5 domain 7; Device lifecycle security.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-MOCK-B-Q022

**Answer: A — Time and vantage recording**

Record capture time, clock assumptions and observation location so packets can be interpreted in context.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Content minimization:** Reduce or redact unnecessary personal or secret payload content when preserving evidence for a limited purpose.
- **C — Independent corroboration:** Compare packet evidence with appropriate endpoint or application records before making a stronger causal claim.
- **D — Capture scope restriction:** Capture only the approved interfaces, hosts and period; shared-network visibility is not permission to collect everything.

Coverage: M08; CEH v5 domain 4; Evidence and privacy.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-MOCK-B-Q023

**Answer: A — Retest the original finding**

Repeat the permitted check that originally demonstrated the problem and compare the result.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Apply and verify the fix:** Confirm that the intended change removes the relevant vulnerable condition, rather than only recording that a patch command ran.
- **C — Document accepted risk:** When an authorized owner accepts remaining risk, record the scope, reason, owner and review conditions.
- **D — Check for regression:** Verify that the change preserves required behavior and has not introduced a new failure.

Coverage: M05; CEH v5 domain 3; Remediation lifecycle.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-MOCK-B-Q024

**Answer: B — Execution and concurrency limits**

Bound function work and concurrency to control availability and cost exposure within platform capabilities.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Cloud audit trail:** Audit records capture supported management or data events; configuration, retention and protection determine their investigative usefulness.
- **C — Function event validation:** Validate untrusted event data and authorization even when a managed platform invokes the function.
- **D — Region and service coverage:** Logging and controls must cover the actual regions and services in use rather than assuming one configured location covers everything.

Coverage: M19; CEH v5 domain 8; Serverless and audit.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-MOCK-B-Q025

**Answer: C — Server certificate validation**

Validating the expected authentication server certificate helps prevent clients from trusting an impostor enterprise authentication endpoint.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Protected management frames:** PMF protects selected management frames against certain forgery and replay attacks; it does not prevent radio jamming.
- **B — Wireless segmentation:** Separate guest, managed and sensitive traffic with enforced network policy rather than trusting association alone.
- **D — Wireless intrusion monitoring:** Monitoring identifies unexpected APs, identities and radio behavior for investigation, subject to placement and coverage limits.

Coverage: M16; CEH v5 domain 6; Wireless controls.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-MOCK-B-Q026

**Answer: D — Object-level authorization**

Check whether the subject may access the specific referenced object on every relevant request.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Tenant isolation:** Enforce tenant boundaries in data queries and operations so one tenant cannot reach another's resources.
- **B — Function-level authorization:** Check whether the subject may invoke a privileged operation, not just whether the route is visible in the UI.
- **C — Deny-by-default access policy:** Reject access unless the applicable policy explicitly grants it, including newly added routes.

Coverage: M14; CEH v5 domain 5; Server-side authorization.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-B-Q027

**Answer: D — True positive**

A true positive correctly identifies a condition that is actually present.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — True negative:** A true negative correctly leaves an absent condition unreported.
- **B — False negative:** A false negative fails to report a problem that actually exists.
- **C — False positive:** A false positive reports a problem that is not actually present under the assessed conditions.

Coverage: M05; CEH v5 domain 3; Finding accuracy.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-MOCK-B-Q028

**Answer: C — Rotation and revocation**

Replace or invalidate keys when required while managing dependent systems and retained data.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Key separation:** Use keys for their intended purpose and trust boundary rather than reusing one key across unrelated functions.
- **B — Secure destruction and retention:** Retain keys only as needed and destroy them appropriately when their authorized lifetime ends, considering recovery obligations.
- **D — Cryptographically secure randomness:** Security-sensitive keys and nonces need an appropriate unpredictable generator and correct construction-specific handling.

Coverage: M20; CEH v5 domain 9; Key lifecycle.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-MOCK-B-Q029

**Answer: B — Rollback plan**

A rollback plan restores the prior configuration if a mitigation damages legitimate service.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Bounded load testing:** Use an approved environment, rate, duration and stop condition to test capacity without uncontrolled disruption.
- **C — Incident coordination:** Coordinate service owners, network operators and responders because availability incidents can span multiple control points.
- **D — Recovery verification:** Check legitimate user success and resource stability after mitigation rather than relying only on reduced attack traffic.

Coverage: M10; CEH v5 domain 4; Safe testing and recovery.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-MOCK-B-Q030

**Answer: C — NS record**

An NS record identifies an authoritative name server for a DNS zone.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — PTR record:** A PTR record maps a reverse-DNS name toward a host name; it does not prove service ownership.
- **B — TXT record:** A TXT record carries text, including formats used by some email policies and ownership checks.
- **D — SOA record:** An SOA record carries zone authority metadata including a serial number and timing values.

Coverage: M02; CEH v5 domain 2; Additional DNS data.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-MOCK-B-Q031

**Answer: A — Switch port mirroring**

Port mirroring copies selected switch traffic to an authorized monitoring port, subject to configuration and capacity limits.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Network TAP:** A network TAP provides a dedicated observation point on a link; visibility depends on its placement and capabilities.
- **C — Encrypted payload limitation:** Encryption can conceal application content from a passive observer even when addresses, timing or other metadata remain visible.
- **D — Promiscuous mode:** Promiscuous mode allows an interface to pass more received frames to capture software; it does not force a switch to send all traffic to that port.

Coverage: M08; CEH v5 domain 4; Packet visibility.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-MOCK-B-Q032

**Answer: D — Dual approval**

Require a second authorized reviewer for sensitive changes or transfers so one deceived person is insufficient.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Reporting channel:** A simple trusted reporting path lets recipients raise suspicious requests without continuing the interaction.
- **B — Phishing-resistant authentication:** Origin-bound cryptographic authentication resists many credential-phishing flows, while broader social engineering still needs controls.
- **C — Independent callback:** Verify a sensitive request through a known trusted contact path, not a number or link supplied by the requester.

Coverage: M09; CEH v5 domain 4; Verification controls.
Technical references: [CISA phishing guidance](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing) · [MITRE phishing](https://attack.mitre.org/techniques/T1566/) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-B-Q033

**Answer: D — Steganography hides presence**

Steganography hides information within another carrier; secrecy of content may still require encryption.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Hashing is not password encryption:** Password verification normally uses a suitable one-way password KDF and salt rather than reversible encryption or a fast unsalted hash.
- **B — Encoding is not encryption:** Encoding changes representation for interoperability and generally provides no secret-based confidentiality.
- **C — Signing is not confidentiality:** A signature can authenticate content while leaving that content readable to anyone who receives it.

Coverage: M20; CEH v5 domain 9; Common confusions.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-MOCK-B-Q034

**Answer: B — Separate writable and executable content**

Prevent user-controlled uploads or writable directories from being interpreted as server-side executable code.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Apply supported updates:** Use maintained software and verified relevant fixes; deployment and restart state must make the fix effective.
- **C — Run with limited privileges:** Give the web process only the operating-system and filesystem access its function needs.
- **D — Remove unused features:** Disable or remove unneeded handlers, modules and sample applications to reduce attack surface.

Coverage: M13; CEH v5 domain 5; Server hardening.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-B-Q035

**Answer: B — Content Security Policy**

CSP can constrain browser resource and script execution as defense in depth, but does not replace fixing injection paths.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — CORS policy:** CORS controls whether browser scripts may read certain cross-origin responses; it is not a substitute for server authorization.
- **C — Business-logic validation:** Validate workflow-specific rules, sequence and state transitions rather than only input syntax.
- **D — Server-side validation:** The server must enforce important constraints because clients can modify or bypass browser-side checks.

Coverage: M14; CEH v5 domain 5; Browser and API trust.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-B-Q036

**Answer: B — BSSID**

A BSSID identifies a basic service set, commonly using the access point radio's MAC address.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Signal strength:** Signal strength measures received power at the observer and does not reliably establish trust or exact physical distance.
- **C — Channel:** The channel identifies the radio-frequency portion used by the network; interference and observation depend on channel conditions.
- **D — SSID:** An SSID names a wireless network and is not a secret or proof that an access point is legitimate.

Coverage: M16; CEH v5 domain 6; Wireless identity.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-MOCK-B-Q037

**Answer: C — Exposed interprocess component**

An exported component can receive calls from other applications; intended caller permissions and input handling matter.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Clipboard exposure:** Sensitive content placed on a clipboard may be available beyond the intended app, depending on platform behavior and context.
- **B — Unsafe deep-link handling:** Deep links can deliver untrusted parameters or navigation requests and must not bypass authentication or validation.
- **D — Unsafe WebView boundary:** A WebView that exposes privileged bridges or loads untrusted content can cross from web input into app capabilities.

Coverage: M17; CEH v5 domain 7; Application interaction.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-MOCK-B-Q038

**Answer: C — Backend authorization**

The server must validate subject and object permissions regardless of checks performed by the mobile client.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — TLS trust validation:** Validate peer identity and trust for protected connections instead of accepting any certificate.
- **B — Cleartext transport exposure:** Unprotected transport can expose application data to observers or modification on the path.
- **D — Certificate pinning tradeoff:** Pinning constrains acceptable credentials but needs a careful rotation and recovery design; it is not a replacement for sound TLS handling.

Coverage: M17; CEH v5 domain 7; Mobile network security.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-MOCK-B-Q039

**Answer: A — Scan-vantage dependence**

Results describe the path, source location and time of observation; another network path may expose different behavior.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Banner uncertainty:** A banner or fingerprint may be customized, hidden or affected by a proxy, so product claims need corroboration.
- **C — Transport distinction:** TCP and UDP maintain separate port spaces; a result for one does not establish the other.
- **D — Rate and reliability tradeoff:** Aggressive probing can increase loss, load or false negatives; reliable testing uses suitable rates and conditions.

Coverage: M03; CEH v5 domain 2; Interpreting scan limits.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-MOCK-B-Q040

**Answer: A — Detection and logging**

Network or host telemetry can identify probing patterns and preserve context for investigation.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Authenticated inventory:** Authenticated inventory uses trusted management information to complement what unauthenticated network probes can see.
- **C — Service hardening:** Service hardening removes unnecessary listeners and secures the configuration of services that remain.
- **D — Network segmentation:** Segmentation constrains which network zones can reach services and limits exposure across trust boundaries.

Coverage: M03; CEH v5 domain 2; Discovery defenses.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-MOCK-B-Q041

**Answer: C — Active reconnaissance**

Active reconnaissance sends requests or probes to the target or its infrastructure and requires appropriate scope.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Passive-source research:** Passive-source research uses already available third-party information without probing the target service directly.
- **B — Data minimization:** Data minimization limits collection to information actually needed for the authorized purpose.
- **D — Source corroboration:** Corroboration compares independent evidence because a single public record may be incomplete, stale or misleading.

Coverage: M02; CEH v5 domain 2; Passive and active reconnaissance.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-MOCK-B-Q042

**Answer: D — Pass-the-ticket**

Pass-the-ticket reuses Kerberos ticket material rather than recovering the user's plaintext password.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Kerberoasting:** Kerberoasting obtains suitable service-ticket material for offline guessing of a service account password.
- **B — Pass-the-hash:** Pass-the-hash uses an appropriate password hash as authentication material where the protocol and conditions permit it.
- **C — Credential dumping:** Credential dumping extracts credential material from memory or stored system data; the material may take several forms.

Coverage: M06; CEH v5 domain 3; Windows credential concepts.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-MOCK-B-Q043

**Answer: B — False-negative reduction**

Improve coverage for real events that current detections miss, using appropriate telemetry and validation.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — False-positive reduction:** Reduce incorrect alerts using validated context and careful rule tuning rather than suppressing all visibility.
- **C — Layered detection:** Combine complementary signals so one visibility limitation does not determine the whole conclusion.
- **D — Baseline-aware detection:** Interpret anomalies relative to relevant normal behavior while recognizing that a baseline can itself include unwanted activity.

Coverage: M12; CEH v5 domain 4; Detection tuning.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-MOCK-B-Q044

**Answer: A — Conditional access**

Access decisions can consider managed-device posture and other signals, while accounting for signal reliability.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Work-profile separation:** Separate managed work data and applications from personal contexts where the platform supports that boundary.
- **C — Remote response actions:** Remote lock, wipe or session revocation can reduce incident exposure, but depend on reachability, scope and platform behavior.
- **D — MDM policy:** Mobile device management enforces supported device policies and configuration, subject to enrollment and platform capabilities.

Coverage: M17; CEH v5 domain 7; Enterprise mobile controls.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-MOCK-B-Q045

**Answer: A — SameSite**

SameSite restricts cookie inclusion in specified cross-site request contexts, depending on its configured value and browser behavior.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Path and Domain scope:** Path and Domain influence where a cookie is sent; they should not be treated as a complete authorization boundary.
- **C — HttpOnly:** HttpOnly prevents ordinary client-side script access to the cookie, but does not stop all actions performed by injected script.
- **D — Secure:** The Secure attribute restricts cookie transmission to secure transport contexts; it does not prevent script access by itself.

Coverage: M11; CEH v5 domain 4; Cookie attributes.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-B-Q046

**Answer: B — Measure legitimate impact**

Check latency, errors and valid-user success so a blocking rule does not silently damage normal operation.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Replay sanitized fixtures:** Use approved recorded or synthetic data to check a detection without creating harmful live traffic.
- **C — Preserve rollback and ownership:** A control change needs an accountable owner and a practical reversal path when its effects are unacceptable.
- **D — Compare expected and observed alerts:** A detection test needs a declared expected outcome and an actual observation to establish coverage.

Coverage: M12; CEH v5 domain 4; Safe validation.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-MOCK-B-Q047

**Answer: B — Versioning and recovery**

Retained versions or backups can support recovery, subject to retention, deletion privileges and restore testing.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Public access control:** Review whether storage resources permit anonymous or unintended principals, including effective policy combinations.
- **C — Encryption and key control:** Storage encryption protects data under a key-management model; it does not replace authorization to read decrypted objects.
- **D — Data classification and placement:** Classify information and choose approved storage locations, retention and handling requirements for that class.

Coverage: M19; CEH v5 domain 8; Storage and data.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-MOCK-B-Q048

**Answer: D — Autonomous-system data**

AS and routing data identify network routing relationships or announced prefixes, not automatic testing permission.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Geolocation estimate:** IP geolocation estimates an address's location; VPNs, shared infrastructure and stale databases limit precision.
- **B — Reverse proxy or CDN:** A reverse proxy or CDN can terminate public requests while hiding or separating the origin server.
- **C — Traceroute:** Traceroute infers path hops from probe responses, often using time-to-live or hop-limit expiry; missing replies do not prove a broken path.

Coverage: M02; CEH v5 domain 2; Network footprint interpretation.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-MOCK-B-Q049

**Answer: C — Firewall**

A firewall enforces traffic policy at its supported layers; permitted traffic is not automatically safe application behavior.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Honeypot:** A honeypot is a deliberately observed decoy resource used to learn about or detect interactions.
- **B — IPS:** An intrusion prevention system can inspect and block traffic in its enforcement path.
- **D — IDS:** An intrusion detection system observes activity and generates detections; a passive deployment does not directly block traffic.

Coverage: M12; CEH v5 domain 4; Security device roles.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-MOCK-B-Q050

**Answer: D — SNMP**

SNMP exposes management data through defined objects; security depends on version and access configuration.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — LDAP:** LDAP queries directory objects and attributes, with access constrained by authentication and directory permissions.
- **B — SMTP:** SMTP transfers email; some server commands or responses can reveal recipient information when enabled.
- **C — SMB:** SMB provides file-sharing and related services, with access governed by authentication, share and file permissions.

Coverage: M04; CEH v5 domain 2; Enumeration protocols.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-B-Q051

**Answer: D — Unauthenticated assessment**

An unauthenticated assessment observes exposure without logging in; its visibility is limited to that perspective.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Configuration review:** A configuration review compares settings and effective controls with defined requirements.
- **B — Manual validation:** Manual validation investigates a finding's applicability or behavior beyond an automated label.
- **C — Credentialed assessment:** A credentialed assessment uses authorized access to inspect information unavailable to an unauthenticated probe.

Coverage: M05; CEH v5 domain 3; Assessment access.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-MOCK-B-Q052

**Answer: B — Hostname validation**

Check that the certificate identity matches the intended service name rather than merely trusting its issuer.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Validity and revocation handling:** Consider validity periods and applicable revocation mechanisms according to the client and deployment policy.
- **C — Private-key protection:** Protect the private key from disclosure or misuse; a public certificate does not need to be kept secret.
- **D — Certificate-chain validation:** Validate a certificate through an accepted trust chain under the verifier's policy.

Coverage: M20; CEH v5 domain 9; PKI and certificates.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-MOCK-B-Q053

**Answer: A — Orchestrator RBAC**

Restrict which identities can perform operations on cluster resources, including sensitive administrative actions.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Secret delivery:** Deliver secrets through appropriate restricted mechanisms rather than embedding them in images, code or broadly visible configuration.
- **C — Image provenance and maintenance:** Use trustworthy images and maintain their dependencies; a signed origin alone does not mean the contents are vulnerability-free.
- **D — Container isolation boundary:** Containers usually share a host kernel; isolation is not equivalent to a completely independent hardware machine.

Coverage: M19; CEH v5 domain 8; Containers and orchestration.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-MOCK-B-Q054

**Answer: D — Compensating control**

An alternate control can reduce exposure or impact while the underlying weakness is being repaired.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Business impact:** The affected asset's function and the potential harm determine organizational consequences.
- **B — Residual risk:** Residual risk is the risk that remains after controls or remediation have been applied.
- **C — Exposure and exploitability:** Reachability, required conditions and credible exploitation evidence affect practical urgency.

Coverage: M05; CEH v5 domain 3; Remediation priority.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-MOCK-B-Q055

**Answer: A — 401 Unauthorized**

HTTP 401 indicates that valid authentication credentials are required for the target resource; protocol details include the applicable challenge.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — 500 Internal Server Error:** HTTP 500 indicates an unexpected server-side condition; the response alone does not prove a particular exploit succeeded.
- **C — 403 Forbidden:** HTTP 403 indicates that the server understood the request but refuses it; the reason is not necessarily missing authentication.
- **D — 404 Not Found:** HTTP 404 reports that the target resource is not found or is not being disclosed; it does not prove a file never existed.

Coverage: M13; CEH v5 domain 5; Server response evidence.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-B-Q056

**Answer: B — TLS peer authentication**

Correct peer authentication helps prevent an intermediary from impersonating the intended TLS endpoint.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Application session boundary:** An application session has its own credentials and lifecycle, distinct from the lifetime of a single transport connection.
- **C — On-path interception:** An on-path position can observe or influence traffic between peers; encryption and authentication constrain useful tampering.
- **D — TCP sequence validation:** TCP sequence numbers help a receiver place data within an expected stream; acceptable sequence state matters to forged segments.

Coverage: M11; CEH v5 domain 4; Transport-session concepts.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-B-Q057

**Answer: C — MAC-table flooding**

MAC-table flooding attempts to overwhelm switch forwarding entries; the resulting behavior depends on the device and controls.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — ARP spoofing:** ARP spoofing sends misleading local IPv4-to-link-layer address information and can redirect traffic on a local segment.
- **B — DHCP spoofing:** A rogue DHCP server supplies unauthorized network configuration, such as a malicious gateway or DNS server.
- **D — DNS poisoning:** DNS poisoning causes a resolver or client to use an incorrect name-to-address answer.

Coverage: M08; CEH v5 domain 4; Local-network attacks.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-MOCK-B-Q058

**Answer: D — Input escaping limitation**

Escaping depends on context, encoding and database rules and is more error-prone than separating query structure from values.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Stored procedure review:** A stored procedure can still be injectable if it constructs unsafe dynamic SQL internally.
- **B — Client-side check limitation:** Browser validation can be bypassed; the server and database interaction must enforce the security boundary.
- **C — WAF defense-in-depth limitation:** A WAF may block some patterns but does not remove unsafe query construction in the application.

Coverage: M15; CEH v5 domain 5; Misleading defenses.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-B-Q059

**Answer: C — TCP flags**

TCP flags such as SYN, ACK, FIN and RST describe connection-control information in the segment.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Payload:** The payload carries higher-layer data, which may be application content or encrypted bytes.
- **B — Transport port:** A transport port identifies a protocol endpoint within a transport, but convention alone does not prove the application.
- **D — Source and destination address:** Addresses identify the apparent network endpoints in the observed packet; NAT or spoofing can complicate attribution.

Coverage: M08; CEH v5 domain 4; Packet fields.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-MOCK-B-Q060

**Answer: C — Source-address validation**

Ingress or egress validation reduces spoofed source traffic when applied appropriately in the network.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Response rate limiting:** Response rate limiting constrains repeated or excessive replies, reducing some abusive response patterns.
- **B — Reflection:** Reflection sends replies from third-party services toward a victim, often by using a spoofed source address in requests.
- **D — Amplification:** Amplification produces responses substantially larger than the triggering requests.

Coverage: M10; CEH v5 domain 4; Reflection and amplification.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-MOCK-B-Q061

**Answer: B — Platform-protected key storage**

Use appropriate platform-backed key facilities rather than hardcoding private keys or keeping them as ordinary files.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Sensitive-data minimization:** Avoid storing secrets or personal data that the mobile workflow does not actually need.
- **C — Local encryption boundary:** Encryption protects stored data only within its key and threat model; an unlocked compromised runtime may still access plaintext.
- **D — Backup and log review:** Backups and diagnostic logs can expose data even when the main app screen hides it.

Coverage: M17; CEH v5 domain 7; Mobile data storage.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-MOCK-B-Q062

**Answer: C — Authorized capture only**

Capture and testing must stay within approved networks, devices and methods, even when neighboring radio traffic is visible.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Layered protection:** Link security, endpoint configuration and application encryption address different risks and should not be treated as interchangeable.
- **B — Offline artifact analysis:** A supplied sanitized capture can support protocol reasoning without transmitting or interfering with a live wireless network.
- **D — Association is not identity proof:** A matching network name or successful association does not establish that the network operator is the intended trusted party.

Coverage: M16; CEH v5 domain 6; Wireless evidence boundaries.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-MOCK-B-Q063

**Answer: A — Host discovery**

Host discovery tests whether a host is responsive using approved discovery probes; a negative result may reflect filtering.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Vulnerability validation:** Validation checks whether a suspected weakness actually applies under the target's configuration and authorized test conditions.
- **C — Service version detection:** Version detection interrogates a service to infer its protocol or implementation; banners and fingerprints require interpretation.
- **D — Operating-system fingerprinting:** OS fingerprinting infers an operating system from characteristics such as network-stack responses and remains an inference.

Coverage: M03; CEH v5 domain 2; Discovery and identification.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-MOCK-B-Q064

**Answer: B — AAAA record**

An AAAA record maps a name to an IPv6 address.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — MX record:** An MX record identifies mail exchangers for a domain and includes preference values.
- **C — A record:** An A record maps a name to an IPv4 address.
- **D — CNAME record:** A CNAME record makes one name an alias of another canonical name.

Coverage: M02; CEH v5 domain 2; DNS records.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-MOCK-B-Q065

**Answer: C — Cross-site request forgery**

CSRF induces a victim's browser to send an unwanted authenticated request using ambient credentials.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Origin validation:** Checking the request's origin information can support CSRF defenses when implemented with appropriate trust and fallback rules.
- **B — Authorization check:** Every protected operation still needs a server-side decision that the current subject may perform that specific action.
- **D — Anti-CSRF token:** An unpredictable request token tied to the expected context helps distinguish legitimate submissions from cross-site forgeries.

Coverage: M11; CEH v5 domain 4; CSRF and session scope.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-B-Q066

**Answer: D — Passive-source research**

Passive-source research uses already available third-party information without probing the target service directly.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Active reconnaissance:** Active reconnaissance sends requests or probes to the target or its infrastructure and requires appropriate scope.
- **B — Source corroboration:** Corroboration compares independent evidence because a single public record may be incomplete, stale or misleading.
- **C — Data minimization:** Data minimization limits collection to information actually needed for the authorized purpose.

Coverage: M02; CEH v5 domain 2; Passive and active reconnaissance.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-MOCK-B-Q067

**Answer: A — Digital signature**

A digital signature uses a private signing key and public verification key to authenticate signed content under a trust model.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — HMAC:** HMAC uses a shared secret key and a hash-based construction to authenticate messages; any party holding the key can generate a valid tag.
- **C — Symmetric encryption:** Symmetric encryption uses shared secret key material to protect confidentiality, with suitable modes and key handling.
- **D — Cryptographic hash:** A cryptographic hash produces a fixed-size digest without a secret key; an untrusted digest alone does not prove origin.

Coverage: M20; CEH v5 domain 9; Cryptographic primitives.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-MOCK-B-Q068

**Answer: C — Vishing**

Vishing uses voice communication to deceive a person into disclosure or action.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Phishing:** Phishing uses deceptive messages to induce harmful actions or disclosure, commonly through email or other electronic messaging.
- **B — Spear phishing:** Spear phishing tailors deception to a particular person or group using relevant context.
- **D — Smishing:** Smishing delivers deceptive requests through SMS or similar text-message channels.

Coverage: M09; CEH v5 domain 4; Social-engineering channels.
Technical references: [CISA phishing guidance](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing) · [MITRE phishing](https://attack.mitre.org/techniques/T1566/) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-B-Q069

**Answer: A — Connection-rate controls**

Rate controls constrain new connection creation according to an operational policy.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — SYN cookies:** SYN cookies encode enough handshake state in a response so selected state need not be allocated until a valid acknowledgement arrives.
- **C — Capacity monitoring:** Monitoring tracks resource use and failure symptoms so the bottleneck and mitigation effects can be identified.
- **D — Upstream filtering:** Upstream filtering removes unwanted traffic before it consumes a constrained downstream link or service path.

Coverage: M10; CEH v5 domain 4; SYN-flood defenses.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-MOCK-B-Q070

**Answer: D — NIST Cybersecurity Framework**

The CSF organizes cybersecurity risk management outcomes across functions including Govern, Identify, Protect, Detect, Respond and Recover.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — CVSS:** CVSS describes technical vulnerability severity using a defined scoring method; business priority needs additional context.
- **B — Cyber Kill Chain:** The Cyber Kill Chain describes a staged intrusion lifecycle from preparation to actions on objectives.
- **C — MITRE ATT&CK:** ATT&CK organizes observed adversary tactics and techniques; it is not a vulnerability severity score.

Coverage: M01; CEH v5 domain 1; Framework purpose.
Technical references: [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST CSF 2.0](https://www.nist.gov/cyberframework)

### CEH26-MOCK-B-Q071

**Answer: C — Read-only management access**

Read-only permissions limit queries to reading permitted management objects rather than modifying them.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — SNMPv3 authPriv:** The authPriv security level adds message authentication and privacy when correctly configured.
- **B — SNMPv1/v2c community model:** SNMPv1 and v2c use community strings and do not provide the cryptographic protections offered by SNMPv3 USM.
- **D — Management-plane restriction:** Restricting management traffic to approved sources reduces who can reach the service.

Coverage: M04; CEH v5 domain 2; SNMP security.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-B-Q072

**Answer: B — Rogue access point**

A rogue access point is an unauthorized AP connected to or operating within an organization's environment.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Deauthentication abuse:** Forged or abusive management messages can disrupt associations where applicable protections are absent or insufficient.
- **C — Radio-frequency jamming:** Jamming interferes with the radio medium and can disrupt availability regardless of application-layer security.
- **D — Evil twin:** An evil twin impersonates a trusted wireless network to attract clients, often using a familiar network name.

Coverage: M16; CEH v5 domain 6; Wireless threats.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-MOCK-B-Q073

**Answer: D — GET**

GET requests a representation and is defined with safe semantics; applications should not use it for unintended state-changing operations.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — OPTIONS:** OPTIONS describes communication options for a target or server, but advertised methods do not prove they are usable by every identity.
- **B — PUT:** PUT requests creation or replacement of the target resource's state; enabling it does not by itself prove unauthorized write access.
- **C — POST:** POST submits data for resource-specific processing and may change state; authorization and CSRF controls still matter.

Coverage: M13; CEH v5 domain 5; HTTP method interpretation.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-B-Q074

**Answer: C — Change coordination**

Changes to operational systems require the process owner's approved timing, validation and recovery procedures.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Process availability:** Industrial operations may require continuity and predictable control behavior; unplanned disruption can have physical consequences.
- **B — Passive-first observation:** Where active tests could affect fragile systems, approved passive evidence may be the appropriate initial assessment method.
- **D — Safety impact:** OT security decisions must consider possible harm to people, equipment and the physical process, not only data loss.

Coverage: M18; CEH v5 domain 7; OT priorities.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-MOCK-B-Q075

**Answer: A — Broken object authorization**

Broken object authorization lets a subject access or change an object without the required object-level permission.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Server-side request forgery:** SSRF causes a server to make unintended requests influenced by untrusted input, potentially crossing network trust boundaries.
- **C — Cross-site scripting:** XSS occurs when untrusted content is interpreted as executable script in a browser context.
- **D — OS command injection:** Command injection lets untrusted input alter the intended operating-system command or its execution structure.

Coverage: M14; CEH v5 domain 5; Application weakness classes.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-B-Q076

**Answer: A — Unauthorized modification**

A flaw can change or delete data beyond the application's intended permitted operation.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Authentication bypass:** A manipulated query can incorrectly satisfy an authentication decision when that decision relies on unsafe SQL construction.
- **C — Availability impact:** A database operation can degrade or stop service through excessive work, locks or destructive changes.
- **D — Unauthorized read:** A flaw can expose records that the current subject is not allowed to retrieve.

Coverage: M15; CEH v5 domain 5; Impact boundaries.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-B-Q077

**Answer: D — Token signature verification**

Verify a token's signature and intended algorithm with trusted keys before accepting its claims.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Claim validation:** Validate context such as issuer, audience and expiry; a valid signature alone does not make every token suitable for every service.
- **B — High-entropy identifier:** A session identifier should be generated with enough unpredictable randomness to resist guessing.
- **C — Revocation strategy:** Plan how compromised or logged-out credentials stop working, including the constraints of self-contained tokens.

Coverage: M11; CEH v5 domain 4; Token design.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-B-Q078

**Answer: B — State-change verification**

Verify the actual backend effect rather than assuming a response code proves the intended action occurred.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Safe proof of impact:** Demonstrate the minimum authorized effect needed to establish a finding without unnecessary data exposure or damage.
- **C — Regression coverage:** Retain tests for the repaired weakness and valid behavior so later changes can reveal a recurrence or broken function.
- **D — Positive and negative authorization tests:** Check both permitted and forbidden operations with appropriate test identities so success is not judged from one allowed case.

Coverage: M14; CEH v5 domain 5; Testing interpretation.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-B-Q079

**Answer: B — Availability**

Availability keeps a service or information accessible when authorized users need it.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Integrity:** Integrity protects information against unauthorized alteration or destruction.
- **C — Confidentiality:** Confidentiality prevents information from being disclosed to unauthorized readers.
- **D — Accountability:** Accountability links actions to identifiable actors so activity can be reviewed.

Coverage: M01; CEH v5 domain 1; Security objectives.
Technical references: [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST CSF 2.0](https://www.nist.gov/cyberframework)

### CEH26-MOCK-B-Q080

**Answer: A — Collision resistance**

Collision resistance makes finding any two distinct inputs with the same digest impractical under the intended security level.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Second-preimage resistance:** Second-preimage resistance makes finding a different input with the same digest as a given input impractical.
- **C — Forward secrecy:** Forward secrecy protects past session keys against later compromise of a long-term key when the protocol and key exchange provide it.
- **D — Preimage resistance:** Preimage resistance makes finding an input for a specified hash output computationally impractical under the intended security level.

Coverage: M20; CEH v5 domain 9; Security properties.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-MOCK-B-Q081

**Answer: B — Evidence handling**

Evidence handling records origin and preserves artifacts so later conclusions remain supportable.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Written authorization and scope:** Permission must identify who may test which assets, by which methods, and under what limits.
- **C — Responsible disclosure:** A disclosure process routes a finding to the appropriate owner while limiting unnecessary exposure.
- **D — Rules of engagement:** Rules of engagement define operational conditions such as timing, contacts, escalation and stopping criteria.

Coverage: M01; CEH v5 domain 1; Assessment authority.
Technical references: [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST CSF 2.0](https://www.nist.gov/cyberframework)

### CEH26-MOCK-B-Q082

**Answer: D — Baseline comparison**

Compare current traffic and resource behavior with a relevant normal baseline before classifying an anomaly.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Legitimate demand surge:** A large increase in genuine user demand can resemble an attack in volume while requiring different decisions.
- **B — Attack corroboration:** Use multiple indicators such as traffic patterns, request semantics and resource effects to support an attack conclusion.
- **C — Dependency failure:** An upstream or shared dependency can cause outage symptoms even when the application is not being attacked.

Coverage: M10; CEH v5 domain 4; Interpreting outages.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-MOCK-B-Q083

**Answer: C — HMI**

A human-machine interface presents process information and controls to an operator.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — SCADA:** SCADA supervises and gathers data across industrial operations, often involving distributed control assets.
- **B — Historian:** A historian stores time-series process data for analysis and operational records.
- **D — PLC:** A programmable logic controller executes control logic and interfaces with process inputs and outputs.

Coverage: M18; CEH v5 domain 7; Industrial roles.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-MOCK-B-Q084

**Answer: B — RDAP registration data**

RDAP provides structured registration information; privacy redaction and registry differences limit what it reveals.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Certificate transparency logs:** Certificate transparency records publicly logged certificates and can reveal names, but not whether a service is currently live.
- **C — Document metadata:** Document metadata can reveal properties such as authoring software or author fields, which may be stale or user-controlled.
- **D — Search-engine indexing:** A search engine exposes its indexed view of content; cached results can lag behind current deployment.

Coverage: M02; CEH v5 domain 2; Reconnaissance sources.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-MOCK-B-Q085

**Answer: D — Alternate data stream**

On a supporting filesystem, an alternate data stream associates additional data with a file beyond its primary unnamed stream.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Process injection:** Process injection runs code within another process, potentially changing the apparent execution context.
- **B — Log tampering:** Log tampering alters or removes audit records and can damage the ability to reconstruct activity.
- **C — Rootkit behavior:** A rootkit hides or manipulates system views to conceal activity, often requiring privileged access.

Coverage: M06; CEH v5 domain 3; Execution and hiding.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-MOCK-B-Q086

**Answer: A — Union-based SQL injection**

Union-based injection combines compatible query results so additional data may appear in the application's response.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Error-based SQL injection:** Error-based injection uses database error behavior or disclosed error details to learn about query execution or data.
- **C — Boolean-based blind SQL injection:** Boolean-based blind injection infers a condition from consistent differences between true and false responses.
- **D — Time-based blind SQL injection:** Time-based blind injection infers execution from controlled timing differences, which require repeated context-aware validation.

Coverage: M15; CEH v5 domain 5; SQL injection types.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-B-Q087

**Answer: D — WPA3-Personal SAE**

SAE is a password-authenticated key exchange used by WPA3-Personal and improves resistance to passive offline password guessing when correctly deployed.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — WPA2-Personal PSK:** WPA2-Personal commonly uses a shared passphrase-derived key; weak passphrases can be exposed to offline guessing from suitable captured authentication material.
- **B — Open network:** An ordinary open network does not provide password-based link authentication or conventional WPA protection; higher-layer protections remain important.
- **C — Enterprise 802.1X/EAP:** Enterprise authentication uses an EAP method and authentication infrastructure, with method selection and certificate validation affecting security.

Coverage: M16; CEH v5 domain 6; Wireless authentication.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-MOCK-B-Q088

**Answer: A — Credential stuffing**

Credential stuffing reuses previously obtained username/password pairs against other services.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Brute-force login guessing:** Online brute-force guessing tries many password candidates through a live authentication interface.
- **C — Password spraying:** Password spraying tries a small number of likely passwords across many accounts, often to avoid per-account lockout.
- **D — Offline password guessing:** Offline guessing tests candidate passwords against acquired verifiers without sending each attempt to the login service.

Coverage: M06; CEH v5 domain 3; Credential attacks.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-MOCK-B-Q089

**Answer: C — Per-identity quotas**

Quotas allocate a bounded share of resources to a user or tenant; identity design affects how easily limits can be bypassed.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Request cost limits:** Bound request complexity, body size or execution time so one request cannot consume unbounded work.
- **B — Caching:** Caching reuses suitable prior results to reduce repeated computation, while correctness and invalidation remain important.
- **D — Backpressure:** Backpressure limits accepted work or signals overload so downstream queues do not grow without bound.

Coverage: M10; CEH v5 domain 4; Application resilience.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

### CEH26-MOCK-B-Q090

**Answer: B — Check database permissions**

Review the account's actual database privileges to limit damage if another application flaw appears.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Review every query path:** Apply safe construction to all relevant paths, including alternate endpoints and background jobs using the same data.
- **C — Retest valid inputs:** Verify normal application behavior so an injection fix does not merely disable the feature.
- **D — Test literal handling:** Confirm that SQL-looking input is processed as ordinary data or rejected by the intended contract, not executed as syntax.

Coverage: M15; CEH v5 domain 5; Fix verification.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-B-Q091

**Answer: A — Port security**

Port security restricts learned or permitted source MAC addresses on a switch port according to policy.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Authenticated encryption:** Correctly authenticated encryption protects traffic content and peer identity even when the local path is observable.
- **C — Dynamic ARP inspection:** DAI validates ARP messages against trusted bindings or policy to reduce spoofed address mappings.
- **D — DHCP snooping:** DHCP snooping distinguishes trusted DHCP paths and can build bindings used by other protections.

Coverage: M08; CEH v5 domain 4; Layer-two defenses.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-MOCK-B-Q092

**Answer: A — Worm**

A worm can propagate between systems without needing to attach itself to an ordinary host file.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Trojan:** A Trojan presents an apparently useful or legitimate function while carrying hidden malicious behavior.
- **C — Ransomware:** Ransomware denies access to data or systems, commonly through encryption, and demands payment; some campaigns also steal data.
- **D — Virus:** A virus replicates by attaching to a host file or similar carrier and depends on that host's execution or activation.

Coverage: M07; CEH v5 domain 3; Malware classes.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-MOCK-B-Q093

**Answer: C — Stored XSS**

Stored XSS persists malicious input in data later rendered to other users in an unsafe execution context.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — DOM-based XSS:** DOM-based XSS arises when client-side code moves untrusted data into an unsafe browser sink.
- **B — Reflected XSS:** Reflected XSS returns request-supplied input in a response where the browser executes it.
- **D — Context-appropriate output encoding:** Encoding must match the output context so untrusted data remains data rather than executable syntax.

Coverage: M14; CEH v5 domain 5; XSS contexts.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-B-Q094

**Answer: B — Excessive write permission**

Excessive write access lets an account alter resources outside its legitimate responsibilities.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Anonymous information exposure:** Anonymous exposure occurs when useful information can be read without supplying an authenticated identity.
- **C — Excessive read permission:** Excessive read access grants an authenticated account more information than its role requires.
- **D — Name-only evidence:** A discovered name is a lead; it does not establish that the account is active, accessible or authorized for testing.

Coverage: M04; CEH v5 domain 2; Identity and access findings.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-B-Q095

**Answer: D — Dumpster diving**

Dumpster diving seeks useful information from discarded materials.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Shoulder surfing:** Shoulder surfing observes a person's screen, keyboard or similar visible activity to learn sensitive information.
- **B — Baiting:** Baiting offers an appealing object or benefit to induce an unsafe action, such as opening untrusted media.
- **C — Tailgating:** Tailgating gains entry by following an authorized person through an access-controlled boundary without proper authorization.

Coverage: M09; CEH v5 domain 4; Physical deception.
Technical references: [CISA phishing guidance](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing) · [MITRE phishing](https://attack.mitre.org/techniques/T1566/) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-B-Q096

**Answer: D — Filtered**

Filtering prevents the scanner from determining whether a port is open or closed.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Closed:** A closed port is reachable but has no service listening for the tested transport at that time.
- **B — Open:** An open port has a service accepting the relevant transport connections or datagrams from the scanner's perspective.
- **C — Open or filtered:** The probe outcome cannot distinguish an open port from one whose traffic is silently filtered.

Coverage: M03; CEH v5 domain 2; Port states.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-MOCK-B-Q097

**Answer: B — CTR nonce uniqueness**

CTR-style encryption requires avoiding reuse of the relevant nonce/counter stream under the same key, or plaintext relationships can leak.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — CBC IV requirement:** CBC encryption needs a suitable unpredictable initialization vector and separate integrity protection when used without an authenticated construction.
- **C — Authenticated encryption:** Authenticated encryption, such as correctly used GCM, protects confidentiality and detects tampering while still requiring proper nonce and key handling.
- **D — ECB pattern leakage:** ECB independently encrypts equal plaintext blocks under the same key into equal ciphertext blocks, exposing repeated structure.

Coverage: M20; CEH v5 domain 9; Encryption modes.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-MOCK-B-Q098

**Answer: D — Consistent HTTP parsing**

Frontends and backends must agree on request framing and interpretation to avoid boundary confusion.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Trusted proxy configuration:** Accept forwarding metadata only from defined trusted proxies, not arbitrary clients that can forge headers.
- **B — Origin access restriction:** Restrict direct access to an origin when security controls are intended to be enforced by its reverse proxy.
- **C — Host validation:** Validate host information before using it for routing, links or security-sensitive decisions.

Coverage: M13; CEH v5 domain 5; Proxy trust boundaries.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-B-Q099

**Answer: C — Access log**

An access log records request activity as configured, such as path, status, client information and timing.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Process and endpoint evidence:** Host-level process, execution and connection information can corroborate what a web request actually caused.
- **B — File integrity evidence:** Trusted file comparisons help detect unexpected changes to deployed content, subject to a trustworthy baseline.
- **D — Error log:** An error log records server or application failures and can provide context absent from the client response.

Coverage: M13; CEH v5 domain 5; Web incident evidence.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-B-Q100

**Answer: C — Query execution evidence**

A finding needs evidence that input changed database execution, not merely that the application displayed an unusual response.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Error disclosure:** Detailed database errors reveal internal information, but hiding them does not repair unsafe query construction.
- **B — Database-specific behavior:** SQL syntax, functions and error messages vary by database; a response must be interpreted in the correct implementation context.
- **D — Timing uncertainty:** Network jitter, caching and ordinary load can change response time, so one delay is not conclusive injection evidence.

Coverage: M15; CEH v5 domain 5; Database evidence.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-B-Q101

**Answer: D — CWE**

CWE classifies weakness types, such as improper input handling or missing authorization.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — CISA KEV:** The Known Exploited Vulnerabilities catalog identifies listed vulnerabilities with evidence of exploitation in the wild.
- **B — CVE:** A CVE identifier names a publicly disclosed vulnerability record; the identifier itself is not a severity score.
- **C — CVSS:** CVSS expresses technical vulnerability severity using metrics and a versioned scoring method.

Coverage: M05; CEH v5 domain 3; Classification systems.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-MOCK-B-Q102

**Answer: C — Pepper held separately**

A pepper is an additional secret kept apart from the password database; losing only the database need not expose it.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Multifactor authentication:** MFA requires additional authentication factors, reducing reliance on a password alone; it does not repair weak password storage.
- **B — Unique salt:** A unique salt makes equal passwords produce different stored verifiers and reduces reuse of precomputed tables.
- **D — Password key-derivation function:** A purpose-built password KDF makes each guess expensive through configurable computational or memory cost.

Coverage: M06; CEH v5 domain 3; Password storage.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-MOCK-B-Q103

**Answer: C — Scope-preserving continuation**

Continue only within authorized targets and methods; newly discovered endpoints do not automatically expand scope.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Effective permission testing:** Check the actual allowed operation under the specific identity; listed configuration alone may not show the effective result.
- **B — Sensitive-output protection:** Protect enumeration output because account names, paths and configuration details may aid later misuse.
- **D — Service identity corroboration:** Confirm service identity with protocol behavior or trusted host information instead of relying only on a conventional port number.

Coverage: M04; CEH v5 domain 2; Enumeration result quality.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-B-Q104

**Answer: A — Session replay**

Replay presents previously obtained valid session material again; freshness and invalidation controls affect whether it succeeds.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Session fixation:** Session fixation reuses an identifier known before login when the application fails to rotate it after authentication.
- **C — Session prediction:** Prediction exploits insufficient randomness or structure that makes valid session identifiers guessable.
- **D — Session-token theft:** Token theft obtains an existing valid session credential and may allow impersonation without knowing the password.

Coverage: M11; CEH v5 domain 4; Session weaknesses.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-B-Q105

**Answer: D — Fragmentation and reassembly difference**

Different interpretations of fragments or streams can create disagreement between an inspection device and the endpoint.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Encryption visibility gap:** An observer without decryption access may see metadata but cannot inspect protected application payloads directly.
- **B — Encoding normalization:** Security checks need a consistent decoded representation so alternate encodings do not bypass matching while reaching the same application meaning.
- **C — Protocol ambiguity:** Parser differences or unexpected protocol use can make different components interpret the same traffic differently.

Coverage: M12; CEH v5 domain 4; Inspection challenges.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-MOCK-B-Q106

**Answer: B — Dynamic analysis**

Dynamic analysis observes behavior while a sample runs in an appropriately controlled environment.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Static analysis:** Static analysis inspects a sample's code or structure without intentionally executing its behavior.
- **C — Memory analysis:** Memory analysis inspects volatile state such as loaded modules, processes and in-memory content.
- **D — Network analysis:** Network analysis studies communications, destinations, protocols and timing rather than relying only on file contents.

Coverage: M07; CEH v5 domain 3; Analysis methods.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-MOCK-B-Q107

**Answer: C — Lost-device exposure**

A lost device creates risks depending on its lock state, stored data, keys and remote management controls.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Sideloaded malicious app:** An application obtained outside the intended trusted distribution path may carry unreviewed harmful behavior; provenance still needs assessment.
- **B — Malicious profile or management enrollment:** An untrusted configuration profile or management relationship can change device settings and trust boundaries.
- **D — SIM-swap risk:** Transfer of a phone number can expose workflows relying on that number for recovery or authentication.

Coverage: M17; CEH v5 domain 7; Mobile threat scenarios.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-MOCK-B-Q108

**Answer: A — Invalidate on logout**

Logout should revoke server-side session usability, not merely remove a page or local UI state.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Idle and absolute timeout:** Idle timeout limits inactivity while absolute timeout bounds total session lifetime regardless of activity.
- **C — Rotate after privilege change:** Issue a fresh session identifier after authentication or privilege elevation and invalidate the previous relevant state.
- **D — Reauthenticate sensitive actions:** Require fresh verification for sensitive operations when session possession alone is insufficient assurance.

Coverage: M11; CEH v5 domain 4; Session lifecycle defenses.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-B-Q109

**Answer: A — Path traversal**

Path traversal uses input to access paths outside the intended directory boundary when path handling is unsafe.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Verbose error disclosure:** Detailed error responses can expose internal paths, versions or implementation information useful to an attacker.
- **C — Directory listing:** Directory listing reveals files when a server generates an index for a directory without a suitable default document or restriction.
- **D — Default content exposure:** Default pages, sample applications or unused administrative components can reveal information or add unnecessary attack surface.

Coverage: M13; CEH v5 domain 5; Web-server exposure.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-MOCK-B-Q110

**Answer: B — UDP scan**

A UDP scan sends UDP probes and interprets replies and ICMP errors; silence can be ambiguous.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — TCP connect scan:** A connect scan uses the operating system connection API and completes successful TCP handshakes.
- **C — TCP ACK scan:** An ACK scan primarily maps filtering behavior; it does not determine which ports have listening services.
- **D — TCP SYN scan:** A SYN scan sends connection-opening probes and interprets responses without completing the normal handshake for open ports.

Coverage: M03; CEH v5 domain 2; Scan methods.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-MOCK-B-Q111

**Answer: A — Allowlisted input validation**

Validate expected type, format, bounds and permitted values where the application has a well-defined input contract.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Parameterized interpreter use:** Use APIs that keep data separate from executable command or query structure rather than concatenating syntax.
- **C — Canonical path containment:** Resolve paths consistently and verify that the final target remains within the authorized base location.
- **D — Safe file storage:** Store uploads with controlled names and permissions outside executable paths, and serve them through an appropriate access policy.

Coverage: M14; CEH v5 domain 5; Input and upload controls.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-MOCK-B-Q112

**Answer: B — Time-bounded vendor access**

Limit vendor remote access to authorized identities, purpose and windows, with reviewable revocation.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Controlled jump host:** A managed intermediary can constrain and log approved administrative access instead of exposing controllers directly.
- **C — Industrial zones and conduits:** Separate assets by trust and function, and restrict the communication paths that cross those boundaries.
- **D — Asset inventory:** Maintain known devices, firmware, function and ownership so exposure and change decisions have an operational basis.

Coverage: M18; CEH v5 domain 7; Segmentation and remote access.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-MOCK-B-Q113

**Answer: D — TCP reset**

A reset abruptly rejects or terminates a TCP connection; its cause needs surrounding context.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — TLS handshake metadata:** Handshake metadata can reveal protocol negotiation or certificates where visible, without necessarily exposing application content.
- **B — TCP retransmission:** A retransmission repeats data thought to be unacknowledged; loss, delay or capture artifacts require investigation.
- **C — DNS query and response:** DNS messages connect a question with an answer, but a captured answer still requires trust and freshness checks.

Coverage: M08; CEH v5 domain 4; Capture interpretation.
Technical references: [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) · [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

### CEH26-MOCK-B-Q114

**Answer: A — -sn**

The -sn option performs host discovery without the normal port scan.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — -sV:** The -sV option requests service/version detection for discovered ports.
- **C — -Pn:** The -Pn option skips host discovery and treats specified targets as up for subsequent scanning; it does not make traffic invisible.
- **D — -O:** The -O option requests operating-system detection, subject to privileges and useful probe conditions.

Coverage: M03; CEH v5 domain 2; Nmap option meaning.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-MOCK-B-Q115

**Answer: C — Threat**

A threat is a potential cause of an adverse event, such as an actor or harmful circumstance.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Vulnerability:** A vulnerability is a weakness that could be exploited under relevant conditions.
- **B — Exploit:** An exploit is a method or mechanism that takes advantage of a vulnerability.
- **D — Risk:** Risk concerns the likelihood and consequences of an adverse event in a particular context.

Coverage: M05; CEH v5 domain 3; Weakness and risk.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-MOCK-B-Q116

**Answer: C — MFA fatigue**

Repeated authentication prompts can pressure a person into approving an attacker-initiated login.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — QR-code phishing:** A QR code can conceal a destination until scanned; the encoded link still needs independent trust checks.
- **B — Business email compromise:** BEC manipulates business communication to induce actions such as fraudulent payments; malware is not required.
- **D — Synthetic-media impersonation:** Generated voice or video can imitate a trusted person, so apparent likeness alone is insufficient verification.

Coverage: M09; CEH v5 domain 4; Modern deception distinctions.
Technical references: [CISA phishing guidance](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing) · [MITRE phishing](https://attack.mitre.org/techniques/T1566/) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-MOCK-B-Q117

**Answer: B — Recover and verify**

Recovery restores trusted service and checks that business function and security controls operate as expected.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Eradicate the cause:** Eradication removes malicious components and the access or weakness that enabled the incident.
- **C — Contain the affected system:** Containment limits further harm or spread while preserving the ability to investigate.
- **D — Preserve relevant evidence:** Preservation retains necessary logs, volatile data or artifacts before actions that could destroy them, where operational safety permits.

Coverage: M07; CEH v5 domain 3; Response priorities.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-MOCK-B-Q118

**Answer: B — Lateral movement**

Lateral movement extends access to other systems or resources within an environment.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Persistence:** Persistence provides a way to retain or regain access after interruptions such as restart or session loss.
- **C — Vertical privilege escalation:** Vertical escalation gains permissions above the current privilege level on a system or application.
- **D — Horizontal access violation:** Horizontal access violates boundaries between subjects at a similar privilege level, such as two customer accounts.

Coverage: M06; CEH v5 domain 3; Privilege and movement.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-MOCK-B-Q119

**Answer: D — Least-privilege IAM**

Grant only the cloud actions and resources required for a role, with conditions where appropriate.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Short-lived workload credentials:** Use temporary workload identity or credentials rather than distributing long-lived static secrets when supported.
- **B — Privileged-account protection:** Protect high-impact administrative identities with strong authentication, controlled use and recovery procedures.
- **C — Explicit resource policy review:** Review resource-level access together with identity policy because both can affect who can use an object or service.

Coverage: M19; CEH v5 domain 8; Cloud identity.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-MOCK-B-Q120

**Answer: A — Worm**

A worm can propagate between systems without needing to attach itself to an ordinary host file.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Trojan:** A Trojan presents an apparently useful or legitimate function while carrying hidden malicious behavior.
- **C — Ransomware:** Ransomware denies access to data or systems, commonly through encryption, and demands payment; some campaigns also steal data.
- **D — Virus:** A virus replicates by attaching to a host file or similar carrier and depends on that host's execution or activation.

Coverage: M07; CEH v5 domain 3; Malware classes.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-MOCK-B-Q121

**Answer: D — Open**

An open port has a service accepting the relevant transport connections or datagrams from the scanner's perspective.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Filtered:** Filtering prevents the scanner from determining whether a port is open or closed.
- **B — Open or filtered:** The probe outcome cannot distinguish an open port from one whose traffic is silently filtered.
- **C — Closed:** A closed port is reachable but has no service listening for the tested transport at that time.

Coverage: M03; CEH v5 domain 2; Port states.
Technical references: [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) · [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html) · [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

### CEH26-MOCK-B-Q122

**Answer: C — Egress filtering**

Egress filtering controls outbound connections and can reduce unnecessary external communication paths.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Rule review and expiry:** Review ownership and continued need, and expire temporary exceptions to prevent stale access paths.
- **B — Default deny:** Default deny rejects traffic unless an explicit policy permits it.
- **D — Least-necessary rules:** Rules should permit only the source, destination, service and conditions required for the business purpose.

Coverage: M12; CEH v5 domain 4; Firewall policy.
Technical references: [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

### CEH26-MOCK-B-Q123

**Answer: A — Public exposure inventory**

Track public addresses, listeners and service endpoints rather than assuming a resource is private by name.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Private service connectivity:** Use supported private access paths where appropriate to reduce unnecessary public routing, while retaining authentication and authorization.
- **C — Metadata-service protection:** Protect access to workload metadata and credentials, especially against server-side request paths that can reach it.
- **D — Security-group policy:** A workload-level network policy constrains permitted traffic according to the cloud service's supported semantics.

Coverage: M19; CEH v5 domain 8; Cloud network paths.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-MOCK-B-Q124

**Answer: B — Keylogging**

Keylogging captures keystrokes and can expose entered secrets or sensitive content.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Botnet participation:** A bot joins a group of compromised devices controlled to perform coordinated activity.
- **C — Command and control:** Command-and-control communication lets an external controller coordinate or task an implanted component.
- **D — Fileless execution:** Fileless techniques emphasize memory or existing interpreters and system facilities; they can still leave observable artifacts.

Coverage: M07; CEH v5 domain 3; Malware behavior.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-MOCK-B-Q125

**Answer: B — Protocol-state exhaustion**

State-exhaustion attacks consume connection or protocol tracking resources, even without maximal bandwidth.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Volumetric exhaustion:** Volumetric attacks attempt to saturate bandwidth or packet-processing capacity with excessive traffic.
- **C — Application resource exhaustion:** Application-layer exhaustion makes the service spend disproportionate resources on requests or sessions.
- **D — Distributed denial of service:** A DDoS uses many sources to disrupt availability; distribution describes sources rather than a single exhaustion mechanism.

Coverage: M10; CEH v5 domain 4; Availability mechanisms.
Technical references: [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf) · [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827) · [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)
