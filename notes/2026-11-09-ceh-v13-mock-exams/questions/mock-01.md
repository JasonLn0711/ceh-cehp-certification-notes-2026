# Mock 01

[Collection index](../README.md) · [Key audit](../quality-audit.md) · [All-item register](../items.csv)

Printed keys retain the supplied source markings. Study notes explain the intended mechanism; `qualified` identifies a material condition or ambiguous option and `hold` identifies a key/content problem. All editorial module mappings and scenario interpretations are working assumptions unless the linked primary check explicitly confirms a specific fact. These entries are prepared reference material; no learner answers or scores are recorded.

<a id="ceh13-mock01-q001"></a>

## CEH13-MOCK01-Q001 — Caller-ID spoofing

[Question 1](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-1) · Source PDF reference: p. 1 · [M09](../modules/m09.md)

Printed key: **Call Spoofing** · Review: `study-note`.

The displayed number imitates a trusted institution; vishing describes the voice-based deception and caller-ID spoofing describes the identity cue.

Related source entries: [CEH13-BANK-Q113](bank-101-200.md#ceh13-bank-q113).

<a id="ceh13-mock01-q002"></a>

## CEH13-MOCK01-Q002 — Hash extraction versus cracking

[Question 2](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-2) · Source PDF reference: p. 1 · [M06](../modules/m06.md)

Printed key: **hashdump** · Review: `study-note`.

Meterpreter hashdump retrieves local password-verifier material when privileges permit; offline recovery is a later action.

Related source entries: [CEH13-BANK-Q445](bank-401-500.md#ceh13-bank-q445).

<a id="ceh13-mock01-q003"></a>

## CEH13-MOCK01-Q003 — Confidentiality

[Question 3](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-3) · Source PDF reference: pp. 1–2 · [M01](../modules/m01.md)

Printed key: **Confidentiality** · Review: `study-note`.

Readable sensitive content in transit violates confidentiality; integrity concerns modification and availability concerns access continuity.

Related source entries: [CEH13-BANK-Q442](bank-401-500.md#ceh13-bank-q442).

<a id="ceh13-mock01-q004"></a>

## CEH13-MOCK01-Q004 — Sequence-field ambiguity

[Question 4](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-4) · Source PDF reference: p. 2 · [M03](../modules/m03.md)

Printed key: **IP Identification Number (IPID) Monitoring** · Review: `hold`.

IPID sequences and TCP sequence/flow behavior are different observations; identify which field is actually monitored.

Review detail: the same stem has a conflicting malformed bank key/explanation; the generic word sequence does not uniquely establish IPID.

Related source entries: [CEH13-BANK-Q335](bank-301-400.md#ceh13-bank-q335).

<a id="ceh13-mock01-q005"></a>

## CEH13-MOCK01-Q005 — Active session takeover

[Question 5](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-5) · Source PDF reference: pp. 2–3 · [M11](../modules/m11.md)

Printed key: **Active Session Hijacking** · Review: `qualified`.

Packet injection disrupting the legitimate client while the attacker continues the flow is active hijacking; blind additionally means no flow visibility.

Review detail: this form's active key is better supported than BANK-Q509's blind key for the same stem.

Related source entries: [CEH13-BANK-Q509](bank-501-542.md#ceh13-bank-q509).

<a id="ceh13-mock01-q006"></a>

## CEH13-MOCK01-Q006 — DLL search-order hijacking

[Question 6](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-6) · Source PDF reference: p. 3 · [M06](../modules/m06.md)

Printed key: **Privilege Escalation Using DLL Hijacking** · Review: `qualified`.

A writable search location lets a process load an unintended library; privilege gain requires the victim process to have greater privileges.

Review detail: a nonprivileged victim process does not by itself establish escalation.

Related source entries: [CEH13-BANK-Q057](bank-001-100.md#ceh13-bank-q057).

<a id="ceh13-mock01-q007"></a>

## CEH13-MOCK01-Q007 — Semi-untethered jailbreak

[Question 7](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-7) · Source PDF reference: p. 3 · [M17](../modules/m17.md)

Printed key: **Semi-untethered Jailbreaking** · Review: `study-note`.

Normal boot followed by on-device reapplication of elevated state describes semi-untethered behavior.

Related source entries: [CEH13-BANK-Q498](bank-401-500.md#ceh13-bank-q498).

<a id="ceh13-mock01-q008"></a>

## CEH13-MOCK01-Q008 — IDS

[Question 8](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-8) · Source PDF reference: pp. 3–4 · [M12](../modules/m12.md)

Printed key: **Use an Intrusion Detection System (IDS)** · Review: `study-note`.

Automated signature/rule monitoring fits an IDS; detection is distinct from inline prevention or proof that every hijack is visible.

Related source entries: [CEH13-BANK-Q022](bank-001-100.md#ceh13-bank-q022).

<a id="ceh13-mock01-q009"></a>

## CEH13-MOCK01-Q009 — Passive interception

[Question 9](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-9) · Source PDF reference: p. 4 · [M08](../modules/m08.md)

Printed key: **Passive attack** · Review: `study-note`.

Reading traffic without modifying it is passive observation; location and insider status are separate classifications.

Related source entries: [CEH13-BANK-Q368](bank-301-400.md#ceh13-bank-q368).

<a id="ceh13-mock01-q010"></a>

## CEH13-MOCK01-Q010 — MX records

[Question 10](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-10) · Source PDF reference: pp. 4–5 · [M04](../modules/m04.md)

Printed key: **MX** · Review: `study-note`.

MX records name mail exchangers and priorities; resolve the exchanger hostname separately for IP addresses.

<a id="ceh13-mock01-q011"></a>

## CEH13-MOCK01-Q011 — Unverified firmware

[Question 11](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-11) · Source PDF reference: p. 5 · [M18](../modules/m18.md)

Printed key: **Firmware update attack** · Review: `study-note`.

A controller accepting altered unsigned/unverified code demonstrates an insecure firmware update path.

<a id="ceh13-mock01-q012"></a>

## CEH13-MOCK01-Q012 — Botnet agents

[Question 12](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-12) · Source PDF reference: p. 5 · [M07](../modules/m07.md)

Printed key: **Botnet Agents** · Review: `study-note`.

Multiple compromised endpoints receiving synchronized remote commands are bot agents; propagation method is a separate property.

Related source entries: [CEH13-BANK-Q363](bank-301-400.md#ceh13-bank-q363).

<a id="ceh13-mock01-q013"></a>

## CEH13-MOCK01-Q013 — Anomaly detection

[Question 13](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-13) · Source PDF reference: p. 6 · [M12](../modules/m12.md)

Printed key: **Anomaly-Based Detection** · Review: `study-note`.

Deviation from a learned baseline identifies anomaly detection; fragment normalization remains a separate prerequisite for accurate traffic reconstruction.

Related source entries: [CEH13-BANK-Q072](bank-001-100.md#ceh13-bank-q072).

<a id="ceh13-mock01-q014"></a>

## CEH13-MOCK01-Q014 — Traffic replay testing

[Question 14](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-14) · Source PDF reference: p. 6 · [M12](../modules/m12.md)

Printed key: **Traffic IQ Professional** · Review: `study-note`.

The source associates generated/replayed firewall test traffic with Traffic IQ Professional; product availability and exact features remain source claims.

Related source entries: [CEH13-BANK-Q320](bank-301-400.md#ceh13-bank-q320).

<a id="ceh13-mock01-q015"></a>

## CEH13-MOCK01-Q015 — Forwarding-table overflow

[Question 15](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-15) · Source PDF reference: pp. 6–7 · [M08](../modules/m08.md)

Printed key: **MAC Flooding** · Review: `qualified`.

CAM pressure can cause unknown-unicast flooding within a VLAN; cross-VLAN leakage requires another configuration or defect.

Review detail: MAC flooding alone does not defeat VLAN separation.

Related source entries: [CEH13-BANK-Q490](bank-401-500.md#ceh13-bank-q490).

<a id="ceh13-mock01-q016"></a>

## CEH13-MOCK01-Q016 — Password spraying

[Question 16](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-16) · Source PDF reference: p. 7 · [M06](../modules/m06.md)

Printed key: **Password Spraying** · Review: `study-note`.

A few shared guesses across many accounts and time intervals distinguish spraying from account-focused brute force.

<a id="ceh13-mock01-q017"></a>

## CEH13-MOCK01-Q017 — Startup mechanism evidence

[Question 17](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-17) · Source PDF reference: pp. 7–8 · [M06](../modules/m06.md)

Printed key: **Registry run keys** · Review: `hold`.

Registry Run keys, services, scheduled tasks and startup folders can all cause repeated execution.

Review detail: reboot persistence alone does not uniquely select registry Run keys, which normally act at user logon.

Related source entries: [CEH13-BANK-Q454](bank-401-500.md#ceh13-bank-q454).

<a id="ceh13-mock01-q018"></a>

## CEH13-MOCK01-Q018 — Lateral expansion

[Question 18](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-18) · Source PDF reference: p. 8 · [M07](../modules/m07.md)

Printed key: **Expansion** · Review: `study-note`.

Credential reuse and movement from the first host to other assets describe expansion; collection/exfiltration has separate evidence.

Related source entries: [CEH13-BANK-Q203](bank-201-300.md#ceh13-bank-q203).

<a id="ceh13-mock01-q019"></a>

## CEH13-MOCK01-Q019 — IoT assessment

[Question 19](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-19) · Source PDF reference: pp. 8–9 · [M18](../modules/m18.md)

Printed key: **Vulnerability scanning** · Review: `study-note`.

Checking firmware, credentials and services for weaknesses is vulnerability scanning rather than inventory alone.

<a id="ceh13-mock01-q020"></a>

## CEH13-MOCK01-Q020 — SNMP packet inspection

[Question 20](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-20) · Source PDF reference: p. 9 · [M08](../modules/m08.md)

Printed key: **Wireshark** · Review: `study-note`.

Wireshark passively decodes captured SNMP fields; snmpwalk actively queries a MIB and is a different collection method.

Related source entries: [CEH13-BANK-Q460](bank-401-500.md#ceh13-bank-q460).

<a id="ceh13-mock01-q021"></a>

## CEH13-MOCK01-Q021 — OT vulnerability assessment

[Question 21](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-21) · Source PDF reference: p. 9 · [M18](../modules/m18.md)

Printed key: **Vulnerability Scanning** · Review: `study-note`.

Probing identified services for weaknesses belongs to vulnerability assessment before exploitation; controller tolerance constrains active probes.

Related source entries: [CEH13-BANK-Q106](bank-101-200.md#ceh13-bank-q106).

<a id="ceh13-mock01-q022"></a>

## CEH13-MOCK01-Q022 — Verification

[Question 22](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-22) · Source PDF reference: pp. 9–10 · [M05](../modules/m05.md)

Printed key: **Verification** · Review: `study-note`.

Rescanning after repairs checks whether the reported exposure is resolved; this distinguishes verification from remediation.

Related source entries: [CEH13-BANK-Q296](bank-201-300.md#ceh13-bank-q296).

<a id="ceh13-mock01-q023"></a>

## CEH13-MOCK01-Q023 — Whaling

[Question 23](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-23) · Source PDF reference: p. 10 · [M09](../modules/m09.md)

Printed key: **Whaling** · Review: `study-note`.

A CEO-targeted legal pretext is executive spear phishing; whaling is the more specific subtype.

<a id="ceh13-mock01-q024"></a>

## CEH13-MOCK01-Q024 — Measured service

[Question 24](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-24) · Source PDF reference: pp. 10–11 · [M19](../modules/m19.md)

Printed key: **Measured service** · Review: `study-note`.

Metering compute, storage and bandwidth supports usage accounting; distinguish it from automated provisioning and resource sharing.

Related source entries: [CEH13-BANK-Q071](bank-001-100.md#ceh13-bank-q071).

<a id="ceh13-mock01-q025"></a>

## CEH13-MOCK01-Q025 — DCS

[Question 25](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-25) · Source PDF reference: p. 11 · [M18](../modules/m18.md)

Printed key: **Distributed Control System (DCS)** · Review: `study-note`.

Coordinated distributed controllers across a plant fit a DCS; individual open/closed feedback loops describe another abstraction.

Related source entries: [CEH13-BANK-Q146](bank-101-200.md#ceh13-bank-q146).

<a id="ceh13-mock01-q026"></a>

## CEH13-MOCK01-Q026 — BitLocker boundary

[Question 26](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-26) · Source PDF reference: pp. 11–12 · [M20](../modules/m20.md)

Printed key: **BitLocker Drive Encryption** · Review: `qualified`.

Windows-integrated volume protection and managed recovery-key escrow fit BitLocker; an unlocked compromised system still exposes plaintext.

Review detail: deployment and evidence preservation may require planning; full-volume encryption is not live-compromise containment.

Related source entries: [CEH13-BANK-Q262](bank-201-300.md#ceh13-bank-q262).

<a id="ceh13-mock01-q027"></a>

## CEH13-MOCK01-Q027 — Fileless behavior

[Question 27](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-27) · Source PDF reference: p. 12 · [M07](../modules/m07.md)

Printed key: **Fileless Malware** · Review: `study-note`.

Memory-resident PowerShell without a dropped executable illustrates fileless execution; telemetry may survive reboot.

<a id="ceh13-mock01-q028"></a>

## CEH13-MOCK01-Q028 — Cryptographic failures

[Question 28](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-28) · Source PDF reference: p. 12 · [M20](../modules/m20.md)

Printed key: **Cryptographic Failures** · Review: `study-note`.

Weak protection of sensitive traffic creates confidentiality/integrity exposure; identify the actual negotiated transport and trust checks.

<a id="ceh13-mock01-q029"></a>

## CEH13-MOCK01-Q029 — Credentialed assessment

[Question 29](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-29) · Source PDF reference: p. 13 · [M05](../modules/m05.md)

Printed key: **Credentialed Scanning** · Review: `study-note`.

Successful scanner logins enable local patch/configuration checks; internal location does not imply credentialed access.

Related source entries: [CEH13-BANK-Q246](bank-201-300.md#ceh13-bank-q246).

<a id="ceh13-mock01-q030"></a>

## CEH13-MOCK01-Q030 — Response header injection

[Question 30](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-30) · Source PDF reference: p. 13 · [M13](../modules/m13.md)

Printed key: **HTTP Response Splitting** · Review: `study-note`.

Injected response headers or content boundaries suggest CRLF/response-splitting weaknesses; enforce header-value validation.

Related source entries: [CEH13-BANK-Q397](bank-301-400.md#ceh13-bank-q397).

<a id="ceh13-mock01-q031"></a>

## CEH13-MOCK01-Q031 — UNION results

[Question 31](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-31) · Source PDF reference: pp. 13–14 · [M15](../modules/m15.md)

Printed key: **UNION SQL Injection** · Review: `study-note`.

Combining attacker-selected rows into the ordinary result set indicates UNION injection; column count and compatible types are preconditions.

Related source entries: [CEH13-BANK-Q396](bank-301-400.md#ceh13-bank-q396).

<a id="ceh13-mock01-q032"></a>

## CEH13-MOCK01-Q032 — HTTP work exhaustion

[Question 32](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-32) · Source PDF reference: p. 14 · [M10](../modules/m10.md)

Printed key: **HTTP GET/POST Attack** · Review: `study-note`.

Repeated search/form requests consume application work, unlike a slow incomplete-request attack.

<a id="ceh13-mock01-q033"></a>

## CEH13-MOCK01-Q033 — Predictive analysis

[Question 33](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-33) · Source PDF reference: pp. 14–15 · [M01](../modules/m01.md)

Printed key: **Predictive analysis** · Review: `study-note`.

The scenario's forecasting objective describes predictive analysis; model outputs need empirical evaluation before operational trust.

<a id="ceh13-mock01-q034"></a>

## CEH13-MOCK01-Q034 — Secure boot

[Question 34](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-34) · Source PDF reference: p. 15 · [M18](../modules/m18.md)

Printed key: **Ensure secure boot** · Review: `study-note`.

Verify the boot chain against trusted signatures before execution; signed update delivery and runtime integrity cover other stages.

Related source entries: [CEH13-BANK-Q402](bank-401-500.md#ceh13-bank-q402).

<a id="ceh13-mock01-q035"></a>

## CEH13-MOCK01-Q035 — Crypto agility

[Question 35](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-35) · Source PDF reference: p. 15 · [M20](../modules/m20.md)

Printed key: **Include quantum-resistance checks in SDLC and code review processes** · Review: `study-note`.

Inventory cryptographic dependencies and include migration criteria in design/review; assess data lifetime and interoperable supported algorithms.

Related source entries: [CEH13-BANK-Q329](bank-301-400.md#ceh13-bank-q329).

<a id="ceh13-mock01-q036"></a>

## CEH13-MOCK01-Q036 — ARP spoofing

[Question 36](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-36) · Source PDF reference: p. 16 · [M08](../modules/m08.md)

Printed key: **ARP Spoofing** · Review: `study-note`.

Forged local IP-to-MAC mappings can redirect traffic; encrypted application protocols may still protect intercepted content.

Related source entries: [CEH13-BANK-Q151](bank-101-200.md#ceh13-bank-q151).

<a id="ceh13-mock01-q037"></a>

## CEH13-MOCK01-Q037 — Firmware persistence

[Question 37](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-37) · Source PDF reference: p. 16 · [M07](../modules/m07.md)

Printed key: **Hardware/Firmware Rootkit** · Review: `study-note`.

Survival across OS reinstall plus hardware-resident code points to firmware persistence; OS-only cleanup leaves that layer unverified.

Related source entries: [CEH13-BANK-Q033](bank-001-100.md#ceh13-bank-q033).

<a id="ceh13-mock01-q038"></a>

## CEH13-MOCK01-Q038 — WAF and HTTP floods

[Question 38](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-38) · Source PDF reference: pp. 16–17 · [M10](../modules/m10.md)

Printed key: **Web Application Firewall** · Review: `study-note`.

A WAF can filter application requests and apply request controls; upstream saturation and backend capacity require additional layers.

Related source entries: [CEH13-BANK-Q205](bank-201-300.md#ceh13-bank-q205).

<a id="ceh13-mock01-q039"></a>

## CEH13-MOCK01-Q039 — Network vulnerability scanning

[Question 39](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-39) · Source PDF reference: p. 17 · [M05](../modules/m05.md)

Printed key: **Network-based Scanning** · Review: `study-note`.

Network-based assessment checks remotely exposed services across hosts; internal/external describes vantage rather than an exclusive scanner type.

Related source entries: [CEH13-BANK-Q044](bank-001-100.md#ceh13-bank-q044).

<a id="ceh13-mock01-q040"></a>

## CEH13-MOCK01-Q040 — SYN backlog exhaustion

[Question 40](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-40) · Source PDF reference: pp. 17–18 · [M10](../modules/m10.md)

Printed key: **SYN Flood Attack** · Review: `study-note`.

A missing final ACK leaves half-open connections; correlate backlog/resource pressure with incomplete handshake counts.

Related source entries: [CEH13-BANK-Q110](bank-101-200.md#ceh13-bank-q110).

<a id="ceh13-mock01-q041"></a>

## CEH13-MOCK01-Q041 — Fragmentation evasion

[Question 41](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-41) · Source PDF reference: p. 18 · [M12](../modules/m12.md)

Printed key: **Packet Fragmentation** · Review: `study-note`.

The distinguishing condition is disagreement between sensor and endpoint reassembly; normalization and consistent reassembly address it.

Related source entries: [CEH13-BANK-Q007](bank-001-100.md#ceh13-bank-q007).

<a id="ceh13-mock01-q042"></a>

## CEH13-MOCK01-Q042 — Teardrop

[Question 42](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-42) · Source PDF reference: pp. 18–19 · [M10](../modules/m10.md)

Printed key: **Teardrop Attack** · Review: `study-note`.

Malformed overlapping fragment offsets target vulnerable reassembly logic; modern patched stacks may reject them without crashing.

Related source entries: [CEH13-BANK-Q433](bank-401-500.md#ceh13-bank-q433).

<a id="ceh13-mock01-q043"></a>

## CEH13-MOCK01-Q043 — Permission minimization

[Question 43](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-43) · Source PDF reference: p. 19 · [M17](../modules/m17.md)

Printed key: **Review permissions requested by apps before installing them** · Review: `study-note`.

Reject unnecessary app privileges and use managed policy where appropriate; unrelated contacts/camera/SMS access creates exposure.

Related source entries: [CEH13-BANK-Q281](bank-201-300.md#ceh13-bank-q281).

<a id="ceh13-mock01-q044"></a>

## CEH13-MOCK01-Q044 — Boolean blind SQLi

[Question 44](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-44) · Source PDF reference: p. 19 · [M15](../modules/m15.md)

Printed key: **Boolean Exploitation** · Review: `study-note`.

Stable differences between AND 1=1 and AND 1=2 support a Boolean inference channel; this version supplies both complete predicates.

<a id="ceh13-mock01-q045"></a>

## CEH13-MOCK01-Q045 — Tailgating terminology

[Question 45](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-45) · Source PDF reference: p. 20 · [M09](../modules/m09.md)

Printed key: **Tailgating** · Review: `qualified`.

Following entrants without presenting a badge fits tailgating; some sources reserve piggybacking for knowingly assisted entry.

Review detail: terminology varies; the behavioral description is the reliable distinction.

Related source entries: [CEH13-BANK-Q508](bank-501-542.md#ceh13-bank-q508).

<a id="ceh13-mock01-q046"></a>

## CEH13-MOCK01-Q046 — Parameterized queries

[Question 46](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-46) · Source PDF reference: p. 20 · [M15](../modules/m15.md)

Printed key: **Use parameterized queries or prepared statements** · Review: `study-note`.

Bound parameters preserve the query/data boundary; dynamic identifiers and concatenated fragments still require safe design.

Related source entries: [CEH13-BANK-Q380](bank-301-400.md#ceh13-bank-q380).

<a id="ceh13-mock01-q047"></a>

## CEH13-MOCK01-Q047 — Active wireless discovery

[Question 47](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-47) · Source PDF reference: pp. 20–21 · [M16](../modules/m16.md)

Printed key: **Active Footprinting** · Review: `study-note`.

Transmitting management probes makes discovery active; listening only for beacons is passive.

Related source entries: [CEH13-BANK-Q328](bank-301-400.md#ceh13-bank-q328).

<a id="ceh13-mock01-q048"></a>

## CEH13-MOCK01-Q048 — On-device rooting

[Question 48](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-48) · Source PDF reference: p. 21 · [M17](../modules/m17.md)

Printed key: **It is an APK that can run directly on the device without a PC** · Review: `qualified`.

An APK can run locally without a PC, but actual elevation requires a compatible vulnerability.

Review detail: this does not establish support for the named Android version/device or restrictions.

Related source entries: [CEH13-BANK-Q424](bank-401-500.md#ceh13-bank-q424).

<a id="ceh13-mock01-q049"></a>

## CEH13-MOCK01-Q049 — Stream reconstruction

[Question 49](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-49) · Source PDF reference: pp. 21–22 · [M08](../modules/m08.md)

Printed key: **Follow TCP Stream** · Review: `study-note`.

Follow TCP Stream reconstructs captured application bytes; it cannot reveal encrypted payloads without appropriate decryption material.

Related source entries: [CEH13-BANK-Q448](bank-401-500.md#ceh13-bank-q448).

<a id="ceh13-mock01-q050"></a>

## CEH13-MOCK01-Q050 — Registration records

[Question 50](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-50) · Source PDF reference: p. 22 · [M02](../modules/m02.md)

Printed key: **Whois lookup** · Review: `study-note`.

WHOIS/RDAP may expose registrar and registration data; privacy redaction and intermediary ownership limit attribution.

Related source entries: [CEH13-BANK-Q215](bank-201-300.md#ceh13-bank-q215).

<a id="ceh13-mock01-q051"></a>

## CEH13-MOCK01-Q051 — On-demand self-service

[Question 51](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-51) · Source PDF reference: p. 22 · [M19](../modules/m19.md)

Printed key: **On-demand self-service** · Review: `study-note`.

Provisioning resources without provider staff interaction is on-demand self-service; metering and pooling describe other cloud characteristics.

Related source entries: [CEH13-BANK-Q095](bank-001-100.md#ceh13-bank-q095).

<a id="ceh13-mock01-q052"></a>

## CEH13-MOCK01-Q052 — Kill-chain delivery

[Question 52](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-52) · Source PDF reference: pp. 22–23 · [M01](../modules/m01.md)

Printed key: **Delivery** · Review: `study-note`.

Sending the prepared attachment into the environment is delivery; executing its exploit is a later phase.

Related source entries: [CEH13-BANK-Q312](bank-301-400.md#ceh13-bank-q312).

<a id="ceh13-mock01-q053"></a>

## CEH13-MOCK01-Q053 — Shell-command sink

[Question 53](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-53) · Source PDF reference: p. 23 · [M14](../modules/m14.md)

Printed key: **Shell Injection** · Review: `study-note`.

Untrusted input reaching a shell/system-function boundary can alter OS commands; use safe APIs and constrained arguments.

<a id="ceh13-mock01-q054"></a>

## CEH13-MOCK01-Q054 — Orchestration

[Question 54](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-54) · Source PDF reference: pp. 23–24 · [M19](../modules/m19.md)

Printed key: **Container orchestration** · Review: `study-note`.

Coordinated deployment, scaling and discovery across nodes describe orchestration; self-healing is one included capability.

Related source entries: [CEH13-BANK-Q240](bank-201-300.md#ceh13-bank-q240).

<a id="ceh13-mock01-q055"></a>

## CEH13-MOCK01-Q055 — Passive wireless capture

[Question 55](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-55) · Source PDF reference: p. 24 · [M16](../modules/m16.md)

Printed key: **Airodump-ng** · Review: `study-note`.

Monitor-mode beacon and authentication capture fits airodump-ng; packet injection and password analysis are separate roles.

Related source entries: [CEH13-BANK-Q092](bank-001-100.md#ceh13-bank-q092).

<a id="ceh13-mock01-q056"></a>

## CEH13-MOCK01-Q056 — HTTP tunneling

[Question 56](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-56) · Source PDF reference: p. 24 · [M12](../modules/m12.md)

Printed key: **HTTP Tunneling** · Review: `study-note`.

Encapsulating another channel inside permitted HTTP can exploit shallow filtering; protocol-aware controls and endpoint monitoring add visibility.

Related source entries: [CEH13-BANK-Q449](bank-401-500.md#ceh13-bank-q449).

<a id="ceh13-mock01-q057"></a>

## CEH13-MOCK01-Q057 — Hidden-service search limits

[Question 57](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-57) · Source PDF reference: p. 25 · [M02](../modules/m02.md)

Printed key: **filetype:pdf intitle:"admin access" site:onion** · Review: `hold`.

Advanced filters only query a search provider's corpus; site:onion does not supply general Tor indexing or access.

Review detail: repeated unsupported dark-web search assumption.

Related source entries: [CEH13-BANK-Q365](bank-301-400.md#ceh13-bank-q365).

<a id="ceh13-mock01-q058"></a>

## CEH13-MOCK01-Q058 — Financially motivated abuse

[Question 58](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-58) · Source PDF reference: p. 25 · [M01](../modules/m01.md)

Printed key: **Black Hat hackers** · Review: `study-note`.

Unauthorized credential theft and sale support a malicious financially motivated classification; technical skill and sponsorship remain separate.

Related source entries: [CEH13-BANK-Q518](bank-501-542.md#ceh13-bank-q518).

<a id="ceh13-mock01-q059"></a>

## CEH13-MOCK01-Q059 — WPA2 CCMP

[Question 59](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-59) · Source PDF reference: pp. 25–26 · [M16](../modules/m16.md)

Printed key: **WPA2** · Review: `qualified`.

AES-CCMP is characteristic of WPA2-era protection; WPA3 can also use CCMP, so inspect advertised AKM/security parameters.

Review detail: AES and a four-way handshake alone do not uniquely exclude WPA3.

Related source entries: [CEH13-BANK-Q155](bank-101-200.md#ceh13-bank-q155).

<a id="ceh13-mock01-q060"></a>

## CEH13-MOCK01-Q060 — Bulk phishing

[Question 60](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-60) · Source PDF reference: p. 26 · [M09](../modules/m09.md)

Printed key: **Spam and Phishing** · Review: `study-note`.

Deceptive bulk invitations leading to a credential collection page combine spam delivery with phishing.

Related source entries: [CEH13-BANK-Q104](bank-101-200.md#ceh13-bank-q104).

<a id="ceh13-mock01-q061"></a>

## CEH13-MOCK01-Q061 — Rogue DHCP redirection

[Question 61](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-61) · Source PDF reference: pp. 26–27 · [M08](../modules/m08.md)

Printed key: **Rogue DHCP Server Attack** · Review: `study-note`.

Unauthorized lease options change gateway/DNS settings; distinguish forged configuration from exhausting the lease pool.

Related source entries: [CEH13-BANK-Q484](bank-401-500.md#ceh13-bank-q484).

<a id="ceh13-mock01-q062"></a>

## CEH13-MOCK01-Q062 — Geotag reconnaissance

[Question 62](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-62) · Source PDF reference: p. 27 · [M02](../modules/m02.md)

Printed key: **Creepy** · Review: `study-note`.

The source associates Creepy with mapping public geotagged material; availability and supported platforms require current verification.

Related source entries: [CEH13-BANK-Q177](bank-101-200.md#ceh13-bank-q177).

<a id="ceh13-mock01-q063"></a>

## CEH13-MOCK01-Q063 — Security risk guidance

[Question 63](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-63) · Source PDF reference: p. 27 · [M01](../modules/m01.md)

Printed key: **ISO/IEC 27005:2022** · Review: `study-note`.

ISO/IEC 27005 provides guidance for information-security risk management; distinguish ISMS requirements and control guidance.

Related source entries: [CEH13-BANK-Q426](bank-401-500.md#ceh13-bank-q426).

<a id="ceh13-mock01-q064"></a>

## CEH13-MOCK01-Q064 — Assessment method section

[Question 64](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-64) · Source PDF reference: pp. 27–28 · [M05](../modules/m05.md)

Printed key: **Assessment Overview** · Review: `study-note`.

Scope, targets, tools and scan methodology provide the assessment overview; evidence for specific weaknesses belongs in findings.

Related source entries: [CEH13-BANK-Q431](bank-401-500.md#ceh13-bank-q431).

<a id="ceh13-mock01-q065"></a>

## CEH13-MOCK01-Q065 — Error-based reconnaissance

[Question 65](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-65) · Source PDF reference: p. 28 · [M15](../modules/m15.md)

Printed key: **Testing String** · Review: `study-note`.

Malformed strings revealing SQL internals support an injection hypothesis; errors alone do not prove controllable query execution.

Related source entries: [CEH13-BANK-Q264](bank-201-300.md#ceh13-bank-q264).

<a id="ceh13-mock01-q066"></a>

## CEH13-MOCK01-Q066 — Locate and wipe

[Question 66](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-66) · Source PDF reference: pp. 28–29 · [M17](../modules/m17.md)

Printed key: **Register devices with a remote locate and wipe facility** · Review: `study-note`.

Managed locate/wipe addresses lost-device response where enrolled and connected; revoke the lost device's active sessions too.

<a id="ceh13-mock01-q067"></a>

## CEH13-MOCK01-Q067 — Reflection and amplification

[Question 67](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-67) · Source PDF reference: p. 29 · [M10](../modules/m10.md)

Printed key: **Distributed Reflection Denial-of-Service (DRDOS)** · Review: `study-note`.

Spoofed requests causing third parties to send larger replies describe reflected amplification; NTP and DNS are protocol-specific examples.

Related source entries: [CEH13-BANK-Q083](bank-001-100.md#ceh13-bank-q083).

<a id="ceh13-mock01-q068"></a>

## CEH13-MOCK01-Q068 — Pass-the-ticket

[Question 68](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-68) · Source PDF reference: pp. 29–30 · [M06](../modules/m06.md)

Printed key: **Pass-the-Ticket Attack** · Review: `study-note`.

Reusing stolen Kerberos tickets authenticates without cracking the password; distinguish tickets from NTLM hashes and service-ticket roasting.

Related source entries: [CEH13-BANK-Q457](bank-401-500.md#ceh13-bank-q457).

<a id="ceh13-mock01-q069"></a>

## CEH13-MOCK01-Q069 — Design flaws

[Question 69](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-69) · Source PDF reference: p. 30 · [M05](../modules/m05.md)

Printed key: **Design Flaws** · Review: `study-note`.

Weak custom crypto and intentionally inadequate session controls point to design decisions; distinguish a missing design control from a coding error.

Related source entries: [CEH13-BANK-Q118](bank-101-200.md#ceh13-bank-q118).

<a id="ceh13-mock01-q070"></a>

## CEH13-MOCK01-Q070 — Independent identity verification

[Question 70](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-70) · Source PDF reference: p. 30 · [M09](../modules/m09.md)

Printed key: **Employees must verify the identity of individuals requesting information** · Review: `study-note`.

Call back or check a work order through a known trusted channel before sharing payment details.

Related source entries: [CEH13-BANK-Q401](bank-401-500.md#ceh13-bank-q401).

<a id="ceh13-mock01-q071"></a>

## CEH13-MOCK01-Q071 — Email infrastructure evidence

[Question 71](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-71) · Source PDF reference: p. 31 · [M02](../modules/m02.md)

Printed key: **Sender's IP address** · Review: `hold`.

A trusted Received header can contain a mail-server hostname and IP; correlate both rather than treat one claimed field as definitive.

Review detail: identical stem is keyed to sender IP here and sender mail server in BANK-Q405; the question does not resolve the granularity.

Related source entries: [CEH13-BANK-Q405](bank-401-500.md#ceh13-bank-q405).

<a id="ceh13-mock01-q072"></a>

## CEH13-MOCK01-Q072 — Methodology-stage ambiguity

[Question 72](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-72) · Source PDF reference: p. 31 · [M15](../modules/m15.md)

Printed key: **Information Gathering and Vulnerability Detection** · Review: `hold`.

Submitting a query-altering payload is an active SQL-injection test and can also be the point where the vulnerability is confirmed.

Review detail: identical stem is keyed to information gathering/detection here and launching injection in BANK-Q398; no stage definition resolves the overlap.

Related source entries: [CEH13-BANK-Q398](bank-301-400.md#ceh13-bank-q398).

<a id="ceh13-mock01-q073"></a>

## CEH13-MOCK01-Q073 — Exposed secrets

[Question 73](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-73) · Source PDF reference: pp. 31–32 · [M19](../modules/m19.md)

Printed key: **Compromising secrets** · Review: `study-note`.

Stolen API keys authorize actions according to their permissions; revoke/rotate them and investigate logged use and downstream persistence.

Related source entries: [CEH13-BANK-Q531](bank-501-542.md#ceh13-bank-q531).

<a id="ceh13-mock01-q074"></a>

## CEH13-MOCK01-Q074 — Worm propagation

[Question 74](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-74) · Source PDF reference: p. 32 · [M07](../modules/m07.md)

Printed key: **Worm** · Review: `study-note`.

Autonomous copying and spreading across hosts is worm behavior; contrast a host-dependent virus and a nonreplicating backdoor.

Related source entries: [CEH13-BANK-Q065](bank-001-100.md#ceh13-bank-q065).

<a id="ceh13-mock01-q075"></a>

## CEH13-MOCK01-Q075 — User-space keylogging

[Question 75](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-75) · Source PDF reference: p. 32 · [M07](../modules/m07.md)

Printed key: **Application Keylogger** · Review: `study-note`.

Desktop application input captured without drivers or hardware fits a user-space application keylogger.

Related source entries: [CEH13-BANK-Q429](bank-401-500.md#ceh13-bank-q429).

<a id="ceh13-mock01-q076"></a>

## CEH13-MOCK01-Q076 — Hoax

[Question 76](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-76) · Source PDF reference: p. 33 · [M09](../modules/m09.md)

Printed key: **Hoax** · Review: `qualified`.

A fabricated urgent outage warning is a hoax even without malware; this form has an ordinary four-option key.

Review detail: the bank counterpart has a corrupted all-letter key, while this form directly names Hoax.

Related source entries: [CEH13-BANK-Q372](bank-301-400.md#ceh13-bank-q372).

<a id="ceh13-mock01-q077"></a>

## CEH13-MOCK01-Q077 — Document root

[Question 77](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-77) · Source PDF reference: p. 33 · [M13](../modules/m13.md)

Printed key: **Document Root** · Review: `study-note`.

Document root maps published resources to filesystem content; protect permissions and keep secrets outside served directories.

Related source entries: [CEH13-BANK-Q019](bank-001-100.md#ceh13-bank-q019).

<a id="ceh13-mock01-q078"></a>

## CEH13-MOCK01-Q078 — Minimize exposed services

[Question 78](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-78) · Source PDF reference: pp. 33–34 · [M13](../modules/m13.md)

Printed key: **Block all unnecessary ports, ICMP traffic, and protocols** · Review: `study-note`.

Disable or filter services the web-server role does not require; preserve necessary network control traffic and retest dependencies.

Related source entries: [CEH13-BANK-Q298](bank-201-300.md#ceh13-bank-q298).

<a id="ceh13-mock01-q079"></a>

## CEH13-MOCK01-Q079 — SQL service ports

[Question 79](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-79) · Source PDF reference: p. 34 · [M04](../modules/m04.md)

Printed key: **ms-sql-m** · Review: `study-note`.

1434 is registered for Microsoft SQL Monitor; protocol and an observed service response matter more than a port label.

Related source entries: [CEH13-BANK-Q038](bank-001-100.md#ceh13-bank-q038).

Selected primary check: [R26](../references.md#r26).

<a id="ceh13-mock01-q080"></a>

## CEH13-MOCK01-Q080 — Honeypot fingerprinting

[Question 80](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-80) · Source PDF reference: pp. 34–35 · [M12](../modules/m12.md)

Printed key: **Analyzing Response Time** · Review: `study-note`.

Unusually uniform response timing is a clue, not proof of a honeypot; corroborate with service behavior and environment context.

Related source entries: [CEH13-BANK-Q324](bank-301-400.md#ceh13-bank-q324).

<a id="ceh13-mock01-q081"></a>

## CEH13-MOCK01-Q081 — Incomplete AXFR command

[Question 81](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-81) · Source PDF reference: p. 35 · [M04](../modules/m04.md)

Printed key: **dig @ axfr** · Review: `hold`.

The intended method is a DNS zone transfer with dig; specify both the server and zone for a usable request.

Review detail: the printed dig @ axfr lacks a server token and zone name.

Related source entries: [CEH13-BANK-Q527](bank-501-542.md#ceh13-bank-q527).

<a id="ceh13-mock01-q082"></a>

## CEH13-MOCK01-Q082 — NTP diagnostics

[Question 82](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-82) · Source PDF reference: p. 35 · [M04](../modules/m04.md)

Printed key: **ntpdc [-ilnps] [-c command] [host] [...]** · Review: `study-note`.

The source distinguishes legacy ntpdc daemon control from ntpq peer display; service version and query restrictions govern availability.

Related source entries: [CEH13-BANK-Q236](bank-201-300.md#ceh13-bank-q236).

<a id="ceh13-mock01-q083"></a>

## CEH13-MOCK01-Q083 — Preassigned session

[Question 83](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-83) · Source PDF reference: p. 36 · [M11](../modules/m11.md)

Printed key: **Session Fixation Attack** · Review: `study-note`.

A victim authenticating into an attacker-known identifier is fixation; rotate and invalidate the prelogin session.

Related source entries: [CEH13-BANK-Q243](bank-201-300.md#ceh13-bank-q243).

<a id="ceh13-mock01-q084"></a>

## CEH13-MOCK01-Q084 — SQL comment parsing

[Question 84](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-84) · Source PDF reference: p. 36 · [M15](../modules/m15.md)

Printed key: **In-line Comment** · Review: `study-note`.

Comments may alter a filter's view while the DBMS still parses SQL; use parameterized queries rather than keyword blocklists.

Related source entries: [CEH13-BANK-Q100](bank-001-100.md#ceh13-bank-q100).

<a id="ceh13-mock01-q085"></a>

## CEH13-MOCK01-Q085 — DSA nonce discipline

[Question 85](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-85) · Source PDF reference: pp. 36–37 · [M20](../modules/m20.md)

Printed key: **DSA** · Review: `qualified`.

Subgroup arithmetic and per-signature randomness fit DSA; nonce reuse can expose the signing key.

Review detail: ElGamal-family signatures share some listed properties; algorithm identification needs the precise construction.

Related source entries: [CEH13-BANK-Q222](bank-201-300.md#ceh13-bank-q222).

<a id="ceh13-mock01-q086"></a>

## CEH13-MOCK01-Q086 — Recruiter impersonation

[Question 86](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-86) · Source PDF reference: p. 37 · [M09](../modules/m09.md)

Printed key: **Social Engineering** · Review: `study-note`.

A false professional role used to elicit VPN/stack details is social engineering; leaked information is the outcome.

Related source entries: [CEH13-BANK-Q311](bank-301-400.md#ceh13-bank-q311).

<a id="ceh13-mock01-q087"></a>

## CEH13-MOCK01-Q087 — FTP and NetBIOS

[Question 87](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-87) · Source PDF reference: pp. 37–38 · [M04](../modules/m04.md)

Printed key: **TCP 21 and UDP 137** · Review: `study-note`.

TCP 21 is FTP control; UDP 137 is NetBIOS name service. Anonymous access and exposed files need their own permission checks.

Related source entries: [CEH13-BANK-Q081](bank-001-100.md#ceh13-bank-q081).

<a id="ceh13-mock01-q088"></a>

## CEH13-MOCK01-Q088 — LDAP enumeration

[Question 88](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-88) · Source PDF reference: p. 38 · [M04](../modules/m04.md)

Printed key: **LDAP Enumeration** · Review: `study-note`.

Anonymous directory searches returning users and organizational units are LDAP enumeration; exposure depends on bind policy and ACLs.

Related source entries: [CEH13-BANK-Q161](bank-101-200.md#ceh13-bank-q161).

<a id="ceh13-mock01-q089"></a>

## CEH13-MOCK01-Q089 — Voice impersonation

[Question 89](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-89) · Source PDF reference: pp. 38–39 · [M09](../modules/m09.md)

Printed key: **Impersonation** · Review: `qualified`.

The false manager identity is impersonation and its phone delivery is vishing; both descriptions can apply.

Review detail: overlapping options require the question to specify the classification level.

Related source entries: [CEH13-BANK-Q382](bank-301-400.md#ceh13-bank-q382).

<a id="ceh13-mock01-q090"></a>

## CEH13-MOCK01-Q090 — WPA3 and SAE

[Question 90](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-90) · Source PDF reference: p. 39 · [M16](../modules/m16.md)

Printed key: **Upgrade to WPA3** · Review: `qualified`.

SAE resists passive offline password guessing under its intended protocol assumptions; enterprise identity and shared-password elimination require the chosen deployment mode.

Review detail: WPA3 alone does not guarantee all listed IoT, per-user and weak-passphrase goals.

Related source entries: [CEH13-BANK-Q407](bank-401-500.md#ceh13-bank-q407).

<a id="ceh13-mock01-q091"></a>

## CEH13-MOCK01-Q091 — Routing trust

[Question 91](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-91) · Source PDF reference: p. 39 · [M04](../modules/m04.md)

Printed key: **Insecure routing protocols** · Review: `study-note`.

Unauthenticated or unprotected route exchanges can enable false routing information; inspect the actual protocol and supported authentication.

Related source entries: [CEH13-BANK-Q528](bank-501-542.md#ceh13-bank-q528).

<a id="ceh13-mock01-q092"></a>

## CEH13-MOCK01-Q092 — Rate limiting

[Question 92](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-92) · Source PDF reference: pp. 39–40 · [M10](../modules/m10.md)

Printed key: **Rate Limiting** · Review: `study-note`.

Capping requests per identity or interval is rate limiting; distributed clients and shared-NAT users complicate policy tuning.

Related source entries: [CEH13-BANK-Q238](bank-201-300.md#ceh13-bank-q238).

<a id="ceh13-mock01-q093"></a>

## CEH13-MOCK01-Q093 — OS versus service discovery

[Question 93](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-93) · Source PDF reference: p. 40 · [M03](../modules/m03.md)

Printed key: **OS Discovery** · Review: `hold`.

Network fingerprints suggest an OS; application output suggests service versions. The stem mixes both evidence types.

Review detail: identical stem is keyed to OS discovery here and service version discovery in BANK-Q232.

Related source entries: [CEH13-BANK-Q232](bank-201-300.md#ceh13-bank-q232).

<a id="ceh13-mock01-q094"></a>

## CEH13-MOCK01-Q094 — HTTP message boundaries

[Question 94](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-94) · Source PDF reference: pp. 40–41 · [M13](../modules/m13.md)

Printed key: **HTTP Response Splitting Attack** · Review: `hold`.

Response splitting injects response delimiters/headers; a request interpreted as two requests suggests request splitting or smuggling.

Review detail: the stem describes request boundaries but the printed key names response splitting.

Related source entries: [CEH13-BANK-Q175](bank-101-200.md#ceh13-bank-q175).

<a id="ceh13-mock01-q095"></a>

## CEH13-MOCK01-Q095 — Wrapper and dropper roles

[Question 95](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-95) · Source PDF reference: p. 41 · [M07](../modules/m07.md)

Printed key: **Wrapper** · Review: `qualified`.

Bundling with a functioning installer is wrapping; writing additional payload components is dropping. Both can occur together.

Review detail: this form selects Wrapper while BANK-Q488 selects Dropper for the same behavior.

Related source entries: [CEH13-BANK-Q488](bank-401-500.md#ceh13-bank-q488).

<a id="ceh13-mock01-q096"></a>

## CEH13-MOCK01-Q096 — Promiscuous-mode probes

[Question 96](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-96) · Source PDF reference: pp. 41–42 · [M08](../modules/m08.md)

Printed key: **Ping Method** · Review: `qualified`.

An unusual link-layer-destination probe may test host filtering behavior; positive or negative results are implementation-dependent.

Review detail: this is a heuristic and cannot universally confirm a sniffer.

Related source entries: [CEH13-BANK-Q241](bank-201-300.md#ceh13-bank-q241).

<a id="ceh13-mock01-q097"></a>

## CEH13-MOCK01-Q097 — Host IDS

[Question 97](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-97) · Source PDF reference: p. 42 · [M12](../modules/m12.md)

Printed key: **Host-Based Intrusion Detection System** · Review: `study-note`.

Local file, process and configuration events identify a host-based sensor; a network sensor has a different vantage.

Related source entries: [CEH13-BANK-Q041](bank-001-100.md#ceh13-bank-q041).

<a id="ceh13-mock01-q098"></a>

## CEH13-MOCK01-Q098 — Multilayer firewall

[Question 98](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-98) · Source PDF reference: p. 42 · [M12](../modules/m12.md)

Printed key: **Stateful Multilayer Inspection Firewall** · Review: `study-note`.

Connection-state validation plus application inspection explains the multilayer label; actual product functions matter more than a marketing category.

Related source entries: [CEH13-BANK-Q159](bank-101-200.md#ceh13-bank-q159).

<a id="ceh13-mock01-q099"></a>

## CEH13-MOCK01-Q099 — Required ICMP errors

[Question 99](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-99) · Source PDF reference: pp. 42–43 · [M03](../modules/m03.md)

Printed key: **Block inbound ICMP message types and all outbound ICMP type-3** · Review: `hold`.

Selective filtering can reduce discovery while preserving IPv4 path-MTU errors and other necessary control messages.

Review detail: blanket type-3 blocking includes fragmentation-needed errors and can break connectivity.

Related source entries: [CEH13-BANK-Q091](bank-001-100.md#ceh13-bank-q091).

Selected primary check: [R03](../references.md#r03).

<a id="ceh13-mock01-q100"></a>

## CEH13-MOCK01-Q100 — NetBIOS versus SMB data

[Question 100](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-100) · Source PDF reference: p. 43 · [M04](../modules/m04.md)

Printed key: **NetBIOS Enumeration** · Review: `qualified`.

Name-table queries expose names/roles; shares and many user details are retrieved through SMB/RPC rather than nbtstat alone.

Review detail: the scenario merges protocol layers and authentication conditions.

Related source entries: [CEH13-BANK-Q413](bank-401-500.md#ceh13-bank-q413).

<a id="ceh13-mock01-q101"></a>

## CEH13-MOCK01-Q101 — Wireless IPS

[Question 101](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-101) · Source PDF reference: pp. 43–44 · [M16](../modules/m16.md)

Printed key: **Cisco Adaptive Wireless IPS** · Review: `qualified`.

Controller-integrated wireless monitoring and response explain the named product choice; confirm capabilities against its actual version and deployment.

Review detail: product-name recall is source-level information pending vendor comparison.

Related source entries: [CEH13-BANK-Q089](bank-001-100.md#ceh13-bank-q089).

<a id="ceh13-mock01-q102"></a>

## CEH13-MOCK01-Q102 — Mobile storage

[Question 102](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-102) · Source PDF reference: p. 44 · [M17](../modules/m17.md)

Printed key: **Insecure Data Storage** · Review: `study-note`.

Sensitive local plaintext readable without suitable access controls indicates insecure data storage; classify against the named OWASP edition.

Related source entries: [CEH13-BANK-Q197](bank-101-200.md#ceh13-bank-q197).

<a id="ceh13-mock01-q103"></a>

## CEH13-MOCK01-Q103 — Scanner capability confusion

[Question 103](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-103) · Source PDF reference: pp. 44–45 · [M05](../modules/m05.md)

Printed key: **High-speed asset discovery** · Review: `hold`.

Nessus is a vulnerability scanner with discovery capabilities; its core assessment purpose includes applicable software/configuration checks.

Review detail: high-speed discovery is not uniquely supported and differs from the bank's near-identical capability key.

<a id="ceh13-mock01-q104"></a>

## CEH13-MOCK01-Q104 — Remote-access Trojan

[Question 104](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-104) · Source PDF reference: p. 45 · [M07](../modules/m07.md)

Printed key: **Remote Access Trojan (RAT)** · Review: `study-note`.

A disguised file followed by remote workstation control fits a RAT; surveillance alone could also be spyware.

Related source entries: [CEH13-BANK-Q271](bank-201-300.md#ceh13-bank-q271).

<a id="ceh13-mock01-q105"></a>

## CEH13-MOCK01-Q105 — Local inclusion

[Question 105](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-105) · Source PDF reference: pp. 45–46 · [M13](../modules/m13.md)

Printed key: **Local File Inclusion** · Review: `study-note`.

User-controlled parameters reaching local file resolution can disclose configurations; confirm whether the application includes or merely reads the file.

<a id="ceh13-mock01-q106"></a>

## CEH13-MOCK01-Q106 — PaaS responsibilities

[Question 106](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-106) · Source PDF reference: p. 46 · [M19](../modules/m19.md)

Printed key: **Platform as a Service (PaaS)** · Review: `study-note`.

The customer deploys application logic while the provider manages the platform; applications, data and permitted configuration remain customer responsibilities.

Related source entries: [CEH13-BANK-Q099](bank-001-100.md#ceh13-bank-q099).

<a id="ceh13-mock01-q107"></a>

## CEH13-MOCK01-Q107 — Stealth virus

[Question 107](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-107) · Source PDF reference: p. 46 · [M07](../modules/m07.md)

Printed key: **Stealth Virus** · Review: `study-note`.

Intercepting system calls to hide modifications is stealth behavior; polymorphism instead changes a sample's appearance.

Related source entries: [CEH13-BANK-Q168](bank-101-200.md#ceh13-bank-q168).

<a id="ceh13-mock01-q108"></a>

## CEH13-MOCK01-Q108 — Error disclosure

[Question 108](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-108) · Source PDF reference: pp. 46–47 · [M14](../modules/m14.md)

Printed key: **Verbose Error Messages** · Review: `study-note`.

Returning query strings and directory paths is verbose error disclosure; protect server-side diagnostics.

<a id="ceh13-mock01-q109"></a>

## CEH13-MOCK01-Q109 — robots.txt limits

[Question 109](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-109) · Source PDF reference: p. 47 · [M13](../modules/m13.md)

Printed key: **Information Gathering from Robots.txt File** · Review: `study-note`.

Crawler directives can reveal interesting paths, but they are public instructions rather than authorization or access enforcement.

Related source entries: [CEH13-BANK-Q514](bank-501-542.md#ceh13-bank-q514).

<a id="ceh13-mock01-q110"></a>

## CEH13-MOCK01-Q110 — Shoulder surfing

[Question 110](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-110) · Source PDF reference: pp. 47–48 · [M09](../modules/m09.md)

Printed key: **Shoulder Surfing** · Review: `study-note`.

Observing screens and typing is shoulder surfing; prevent exposure with workspace layout, privacy screens and secure authentication practices.

Related source entries: [CEH13-BANK-Q496](bank-401-500.md#ceh13-bank-q496).

<a id="ceh13-mock01-q111"></a>

## CEH13-MOCK01-Q111 — Automation friction

[Question 111](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-111) · Source PDF reference: p. 48 · [M06](../modules/m06.md)

Printed key: **Use CAPTCHA challenges on login and registration pages** · Review: `study-note`.

CAPTCHA adds an interaction challenge against automation; combine it with rate controls, credential hygiene and MFA.

Related source entries: [CEH13-BANK-Q387](bank-301-400.md#ceh13-bank-q387).

<a id="ceh13-mock01-q112"></a>

## CEH13-MOCK01-Q112 — Bettercap role

[Question 112](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-112) · Source PDF reference: pp. 48–49 · [M08](../modules/m08.md)

Printed key: **Bettercap** · Review: `study-note`.

The described ARP/DNS manipulation and interactive network testing match Bettercap's role; TLS and trust validation constrain token interception.

Related source entries: [CEH13-BANK-Q339](bank-301-400.md#ceh13-bank-q339).

<a id="ceh13-mock01-q113"></a>

## CEH13-MOCK01-Q113 — Session fixation defense

[Question 113](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-113) · Source PDF reference: p. 49 · [M11](../modules/m11.md)

Printed key: **Regenerate the session ID after a successful login to prevent session fixation attacks** · Review: `study-note`.

Issue a fresh session identifier after authentication and privilege changes, and invalidate the old identifier.

Related source entries: [CEH13-BANK-Q085](bank-001-100.md#ceh13-bank-q085).

<a id="ceh13-mock01-q114"></a>

## CEH13-MOCK01-Q114 — Twofish identifiers

[Question 114](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-114) · Source PDF reference: p. 49 · [M20](../modules/m20.md)

Printed key: **Twofish** · Review: `study-note`.

The AES-finalist history plus 128-bit block and up-to-256-bit key identifies Twofish.

<a id="ceh13-mock01-q115"></a>

## CEH13-MOCK01-Q115 — Global DHCP snooping

[Question 115](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-115) · Source PDF reference: p. 50 · [M08](../modules/m08.md)

Printed key: **Switch(config)# ip dhcp snooping** · Review: `study-note`.

The shown command globally enables the feature; VLAN selection, trusted uplinks and client-port policy complete deployment.

Related source entries: [CEH13-BANK-Q422](bank-401-500.md#ceh13-bank-q422).

<a id="ceh13-mock01-q116"></a>

## CEH13-MOCK01-Q116 — Known-plaintext model

[Question 116](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-116) · Source PDF reference: p. 50 · [M20](../modules/m20.md)

Printed key: **Known-plaintext attack** · Review: `study-note`.

Already available matching plaintext/ciphertext pairs define known-plaintext analysis; choosing new inputs would change the attack model.

Related source entries: [CEH13-BANK-Q196](bank-101-200.md#ceh13-bank-q196).

<a id="ceh13-mock01-q117"></a>

## CEH13-MOCK01-Q117 — IoT data protection

[Question 117](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-117) · Source PDF reference: pp. 50–51 · [M18](../modules/m18.md)

Printed key: **Insecure data transfer and storage** · Review: `study-note`.

Cleartext transport and retrievable unprotected storage expose data at two different layers; secure both transport and storage/key access.

Related source entries: [CEH13-BANK-Q077](bank-001-100.md#ceh13-bank-q077).

<a id="ceh13-mock01-q118"></a>

## CEH13-MOCK01-Q118 — Forged TCP reset

[Question 118](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-118) · Source PDF reference: p. 51 · [M11](../modules/m11.md)

Printed key: **RST Hijacking** · Review: `study-note`.

A correctly sequenced reset terminates a connection; this source explicitly distinguishes teardown from complete session takeover.

Related source entries: [CEH13-BANK-Q209](bank-201-300.md#ceh13-bank-q209).

<a id="ceh13-mock01-q119"></a>

## CEH13-MOCK01-Q119 — Defacement

[Question 119](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-119) · Source PDF reference: pp. 51–52 · [M13](../modules/m13.md)

Printed key: **Website Defacement** · Review: `study-note`.

Unauthorized modification of visible site content is defacement and primarily affects integrity and trust.

Related source entries: [CEH13-BANK-Q417](bank-401-500.md#ceh13-bank-q417).

<a id="ceh13-mock01-q120"></a>

## CEH13-MOCK01-Q120 — Root cause versus symptom

[Question 120](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-120) · Source PDF reference: p. 52 · [M19](../modules/m19.md)

Printed key: **Insufficient logging and monitoring** · Review: `hold`.

Undefined security responsibilities describe a governance gap; insufficient logs are a possible consequence.

Review detail: this form omits loss of governance from its options and keys the symptom; BANK-Q130 keys the root cause.

Related source entries: [CEH13-BANK-Q130](bank-101-200.md#ceh13-bank-q130).

<a id="ceh13-mock01-q121"></a>

## CEH13-MOCK01-Q121 — NTP enumeration

[Question 121](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-121) · Source PDF reference: p. 52 · [M04](../modules/m04.md)

Printed key: **NTP Enumeration** · Review: `study-note`.

Exposed time-service diagnostic data can reveal peer/internal-system information; exact commands depend on daemon configuration.

Related source entries: [CEH13-BANK-Q507](bank-501-542.md#ceh13-bank-q507).

<a id="ceh13-mock01-q122"></a>

## CEH13-MOCK01-Q122 — Rogue AP

[Question 122](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-122) · Source PDF reference: p. 53 · [M16](../modules/m16.md)

Printed key: **Rogue AP** · Review: `study-note`.

An unapproved AP attached to the internal switch is rogue; impersonating an existing SSID would additionally make it an evil twin.

Related source entries: [CEH13-BANK-Q152](bank-101-200.md#ceh13-bank-q152).

<a id="ceh13-mock01-q123"></a>

## CEH13-MOCK01-Q123 — NULL scan

[Question 123](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-123) · Source PDF reference: p. 53 · [M03](../modules/m03.md)

Printed key: **NULL Scan** · Review: `study-note`.

No TCP flags identifies NULL probing; an absent reply can mean open or filtered and depends on target-stack behavior.

Related source entries: [CEH13-BANK-Q080](bank-001-100.md#ceh13-bank-q080).

<a id="ceh13-mock01-q124"></a>

## CEH13-MOCK01-Q124 — Blockchain eclipse

[Question 124](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-124) · Source PDF reference: pp. 53–54 · [M20](../modules/m20.md)

Printed key: **Eclipse Attack** · Review: `study-note`.

Attacker-controlled peers isolate a victim's network view; this differs from controlling majority consensus power.

Related source entries: [CEH13-BANK-Q063](bank-001-100.md#ceh13-bank-q063).

<a id="ceh13-mock01-q125"></a>

## CEH13-MOCK01-Q125 — Nmap MAC spoofing

[Question 125](../../../source/2026-11-09-ceh-v13-mock-exams/mock-01-125.source.md#question-125) · Source PDF reference: p. 54 · [M03](../modules/m03.md)

Printed key: **nmap -sT -Pn --spoof-mac Dell 10.10.1.11** · Review: `hold`.

The vendor-name argument expresses the requested OUI, but MAC spoofing affects suitable raw local-link probes.

Review detail: -sT uses OS connect sockets; the printed command does not establish spoofing of connect traffic.

Related source entries: [CEH13-BANK-Q023](bank-001-100.md#ceh13-bank-q023).

Selected primary check: [R01](../references.md#r01).
