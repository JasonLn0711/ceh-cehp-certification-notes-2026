# Mock 03

[Collection index](../README.md) · [Key audit](../quality-audit.md) · [All-item register](../items.csv)

Printed keys retain the supplied source markings. Study notes explain the intended mechanism; `qualified` identifies a material condition or ambiguous option and `hold` identifies a key/content problem. All editorial module mappings and scenario interpretations are working assumptions unless the linked primary check explicitly confirms a specific fact. These entries are prepared reference material; no learner answers or scores are recorded.

<a id="ceh13-mock03-q001"></a>

## CEH13-MOCK03-Q001 — Indexed S3 references

[Question 1](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-1) · Source PDF reference: p. 1 · [M02](../modules/m02.md)

Printed key: **B** — Use Google advanced search operators to enumerate S3 bucket URLs. · Review: `study-note`.

Search operators can surface additional indexed URLs; confirm owner and public permissions separately from bucket-name discovery.

<a id="ceh13-mock03-q002"></a>

## CEH13-MOCK03-Q002 — Legacy TLS

[Question 2](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-2) · Source PDF reference: p. 1 · [M20](../modules/m20.md)

Printed key: **D** — Use a man-in-the-middle (MitM) attack to intercept and decrypt traffic. · Review: `hold`.

TLS 1.0 is obsolete; exploitation still requires a concrete cipher/protocol weakness and attacker position.

Review detail: old TLS does not by itself let a MitM decrypt an arbitrary session.

Related source entries: [CEH13-BANK-Q088](bank-001-100.md#ceh13-bank-q088).

<a id="ceh13-mock03-q003"></a>

## CEH13-MOCK03-Q003 — Poisoned name resolution

[Question 3](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-3) · Source PDF reference: pp. 1–2 · [M06](../modules/m06.md)

Printed key: **D** — Exploit name resolution to capture password hashes. · Review: `study-note`.

Forged LLMNR/NBT-NS replies can induce NTLM challenge-response authentication; this is not direct recovery of the underlying password hash.

<a id="ceh13-mock03-q004"></a>

## CEH13-MOCK03-Q004 — IDS insertion

[Question 4](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-4) · Source PDF reference: p. 2 · [M12](../modules/m12.md)

Printed key: **B** — Insertion attack · Review: `study-note`.

A sensor accepting packets discarded by the endpoint reconstructs a different stream; align checksum validation and normalization.

<a id="ceh13-mock03-q005"></a>

## CEH13-MOCK03-Q005 — robots.txt and authorization

[Question 5](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-5) · Source PDF reference: p. 2 · [M13](../modules/m13.md)

Printed key: **B** — Gathering information through exposed indexing instructions. · Review: `study-note`.

Public crawler paths supply leads; lack of authentication, rather than Disallow itself, permits sensitive-file access.

<a id="ceh13-mock03-q006"></a>

## CEH13-MOCK03-Q006 — Unencrypted local data

[Question 6](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-6) · Source PDF reference: p. 2 · [M17](../modules/m17.md)

Printed key: **A** — Access the local storage to retrieve data directly from the device. · Review: `study-note`.

Readable storage exposes data after suitable device access; application sandbox and key/access controls remain relevant.

<a id="ceh13-mock03-q007"></a>

## CEH13-MOCK03-Q007 — Session attack prerequisites

[Question 7](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-7) · Source PDF reference: pp. 2–3 · [M11](../modules/m11.md)

Printed key: **C** — Exploit a browser zero-day vulnerability to inject scripts. · Review: `hold`.

HTTPS and MFA leave endpoint/session threats possible but do not establish a browser zero-day.

Review detail: no evidenced browser flaw or guarantee of undetected takeover supports the marked option.

<a id="ceh13-mock03-q008"></a>

## CEH13-MOCK03-Q008 — Shared-hardware leakage

[Question 8](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-8) · Source PDF reference: p. 3 · [M19](../modules/m19.md)

Printed key: **A** — Side-channel attack · Review: `study-note`.

CPU timing leakage across colocated VMs is a side channel under specific sharing and measurement conditions.

<a id="ceh13-mock03-q009"></a>

## CEH13-MOCK03-Q009 — SNMP process MIB

[Question 9](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-9) · Source PDF reference: p. 3 · [M04](../modules/m04.md)

Printed key: **D** — nmap -sU -p 161 --script snmp-processes · Review: `study-note`.

snmp-processes queries process information exposed by the agent; the community and supported MIB determine results.

<a id="ceh13-mock03-q010"></a>

## CEH13-MOCK03-Q010 — Logout replay

[Question 10](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-10) · Source PDF reference: p. 3 · [M11](../modules/m11.md)

Printed key: **A** — Perform a replay attack by using the same token after logout. · Review: `study-note`.

A still-accepted token after logout proves missing invalidation for that session; record server behavior and token expiry.

<a id="ceh13-mock03-q011"></a>

## CEH13-MOCK03-Q011 — Timing versus policy

[Question 11](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-11) · Source PDF reference: pp. 3–4 · [M03](../modules/m03.md)

Printed key: **A** — Use a low-and-slow scan. · Review: `hold`.

Slow probes can avoid a rate threshold; they do not open a firewall-blocked port.

Review detail: the marked timing choice does not itself evade an explicit nonstandard-port block.

<a id="ceh13-mock03-q012"></a>

## CEH13-MOCK03-Q012 — Default credential exposure

[Question 12](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-12) · Source PDF reference: p. 4 · [M18](../modules/m18.md)

Printed key: **A** — Gain unauthorized access to the ICS and control operations. · Review: `study-note`.

Validate weak/default credentials only under the agreed ICS scope; process-safety constraints govern permitted operations.

<a id="ceh13-mock03-q013"></a>

## CEH13-MOCK03-Q013 — Login query boundary

[Question 13](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-13) · Source PDF reference: p. 4 · [M15](../modules/m15.md)

Printed key: **A** — Enter ' OR '1'='1 in the username/password fields. · Review: `study-note`.

A Boolean input may reveal unsafe concatenation; use non-destructive controls and parameterized queries as the repair.

<a id="ceh13-mock03-q014"></a>

## CEH13-MOCK03-Q014 — Fake onboarding portal

[Question 14](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-14) · Source PDF reference: p. 4 · [M09](../modules/m09.md)

Printed key: **B** — Create a convincing fake onboarding portal. · Review: `study-note`.

A role-relevant portal pretext can elicit credentials; identity verification and phishing-resistant authentication reduce exposure.

<a id="ceh13-mock03-q015"></a>

## CEH13-MOCK03-Q015 — TCP handshake

[Question 15](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-15) · Source PDF reference: p. 4 · [M03](../modules/m03.md)

Printed key: **B** — TCP · Review: `study-note`.

TCP establishes connection state with SYN, SYN/ACK and ACK; SYN probing infers listeners without completing the normal exchange.

<a id="ceh13-mock03-q016"></a>

## CEH13-MOCK03-Q016 — Search operators

[Question 16](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-16) · Source PDF reference: p. 5 · [M02](../modules/m02.md)

Printed key: **B** — Google Hacking (Dorking) · Review: `study-note`.

An intitle/index query locates indexed pages matching a pattern; findings require ownership and current-access confirmation.

<a id="ceh13-mock03-q017"></a>

## CEH13-MOCK03-Q017 — OS detection flag

[Question 17](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-17) · Source PDF reference: p. 5 · [M03](../modules/m03.md)

Printed key: **C** — -O · Review: `study-note`.

-O requests active OS detection; -sV instead probes service versions and -sS selects a TCP scan technique.

<a id="ceh13-mock03-q018"></a>

## CEH13-MOCK03-Q018 — Knowledge-based test models

[Question 18](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-18) · Source PDF reference: p. 5 · [M01](../modules/m01.md)

Printed key: **B** — White Box has full knowledge; Black Box has none. · Review: `study-note`.

White-box supplies extensive internal knowledge; black-box begins with little supplied knowledge and acquires information through testing.

<a id="ceh13-mock03-q019"></a>

## CEH13-MOCK03-Q019 — Web interception proxy

[Question 19](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-19) · Source PDF reference: p. 5 · [M14](../modules/m14.md)

Printed key: **B** — Burp Suite · Review: `study-note`.

Burp Suite intercepts controlled HTTP(S) requests; TLS interception requires an authorized trust setup.

<a id="ceh13-mock03-q020"></a>

## CEH13-MOCK03-Q020 — Shodan observations

[Question 20](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-20) · Source PDF reference: pp. 5–6 · [M02](../modules/m02.md)

Printed key: **B** — Publicly accessible internet-connected devices · Review: `study-note`.

An internet-service search engine indexes observations of reachable systems; stale banners do not prove present exploitability.

<a id="ceh13-mock03-q021"></a>

## CEH13-MOCK03-Q021 — Web transports

[Question 21](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-21) · Source PDF reference: p. 6 · [M13](../modules/m13.md)

Printed key: **C** — 80 and 443 · Review: `study-note`.

TCP 80/443 are conventional HTTP/HTTPS ports; modern HTTP/3 may also use UDP 443 and custom deployments may differ.

<a id="ceh13-mock03-q022"></a>

## CEH13-MOCK03-Q022 — Active fingerprints

[Question 22](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-22) · Source PDF reference: p. 6 · [M03](../modules/m03.md)

Printed key: **B** — Active OS Fingerprinting · Review: `study-note`.

Sending probes to observe stack behavior is active OS fingerprinting; a passive method observes traffic already present.

<a id="ceh13-mock03-q023"></a>

## CEH13-MOCK03-Q023 — SYN stealth terminology

[Question 23](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-23) · Source PDF reference: p. 6 · [M03](../modules/m03.md)

Printed key: **B** — Stealth SYN Scan (-sS) · Review: `qualified`.

A SYN scan avoids a full application connection but remains visible to network sensors.

Review detail: most-stealthy is not universal and the available idle-scan option makes the ranking ambiguous.

<a id="ceh13-mock03-q024"></a>

## CEH13-MOCK03-Q024 — Redirection evidence

[Question 24](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-24) · Source PDF reference: pp. 6–7 · [M14](../modules/m14.md)

Printed key: **C** — Cross-Site Scripting (XSS) · Review: `hold`.

A trusted site redirecting to another destination may be an open redirect; XSS additionally requires script execution.

Review detail: the stem provides no executable browser-context evidence for the marked XSS choice.

<a id="ceh13-mock03-q025"></a>

## CEH13-MOCK03-Q025 — Continuous vulnerability management

[Question 25](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-25) · Source PDF reference: p. 7 · [M05](../modules/m05.md)

Printed key: **B** — To continuously identify, prioritize, and remediate security weaknesses. · Review: `study-note`.

Inventory, validate, prioritize, remediate and verify repeatedly; a scanner run is one input to the lifecycle.

<a id="ceh13-mock03-q026"></a>

## CEH13-MOCK03-Q026 — tcpdump role

[Question 26](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-26) · Source PDF reference: p. 7 · [M08](../modules/m08.md)

Printed key: **C** — Tcpdump · Review: `study-note`.

A command-line packet capture/analyzer observes traffic at the selected interface; visibility depends on capture position and encryption.

<a id="ceh13-mock03-q027"></a>

## CEH13-MOCK03-Q027 — HTTP banner

[Question 27](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-27) · Source PDF reference: p. 7 · [M13](../modules/m13.md)

Printed key: **B** — Banner Grabbing · Review: `study-note`.

Response headers can suggest server/version identity; a banner is a claim, not a confirmed vulnerable build.

<a id="ceh13-mock03-q028"></a>

## CEH13-MOCK03-Q028 — Ping sweep

[Question 28](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-28) · Source PDF reference: p. 8 · [M03](../modules/m03.md)

Printed key: **C** — ICMP · Review: `study-note`.

Conventional ping sweeps use ICMP Echo to identify responsive hosts; silence does not establish absence.

<a id="ceh13-mock03-q029"></a>

## CEH13-MOCK03-Q029 — CVSS scale

[Question 29](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-29) · Source PDF reference: p. 8 · [M05](../modules/m05.md)

Printed key: **C** — CVSS (Common Vulnerability Scoring System) · Review: `study-note`.

CVSS expresses standardized vulnerability severity from 0 to 10; it does not replace local business-risk assessment.

Selected primary check: [R09](../references.md#r09).

<a id="ceh13-mock03-q030"></a>

## CEH13-MOCK03-Q030 — Inverse-mapping uncertainty

[Question 30](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-30) · Source PDF reference: p. 8 · [M03](../modules/m03.md)

Printed key: **B** — There is likely a firewall or packet filter that identifies which ports are open/closed. · Review: `hold`.

Inverse probing depends on negative/error responses and filtering behavior; interpret the exact probe and returned ICMP/TCP fields.

Review detail: responds to inverse mapping is too vague to justify the marked firewall conclusion.

<a id="ceh13-mock03-q031"></a>

## CEH13-MOCK03-Q031 — Half-open flag

[Question 31](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-31) · Source PDF reference: pp. 8–9 · [M03](../modules/m03.md)

Printed key: **B** — nmap -sS · Review: `study-note`.

-sS selects SYN scanning; -sT uses the operating system's connect interface.

<a id="ceh13-mock03-q032"></a>

## CEH13-MOCK03-Q032 — Xmas probe

[Question 32](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-32) · Source PDF reference: p. 9 · [M03](../modules/m03.md)

Printed key: **B** — Xmas Scan · Review: `study-note`.

FIN, PSH and URG together identify Xmas; supporting stacks usually reset closed ports and leave open-or-filtered silent.

<a id="ceh13-mock03-q033"></a>

## CEH13-MOCK03-Q033 — SMB transport

[Question 33](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-33) · Source PDF reference: p. 9 · [M04](../modules/m04.md)

Printed key: **C** — SMB · Review: `study-note`.

TCP 445 commonly carries direct SMB; user/share enumeration depends on protocol permissions and authentication.

<a id="ceh13-mock03-q034"></a>

## CEH13-MOCK03-Q034 — SNMP community defaults

[Question 34](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-34) · Source PDF reference: p. 9 · [M04](../modules/m04.md)

Printed key: **A** — public · Review: `study-note`.

public is a historically common read community, not a mandatory protocol default; replace defaults or deploy authenticated SNMPv3.

<a id="ceh13-mock03-q035"></a>

## CEH13-MOCK03-Q035 — fping discovery

[Question 35](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-35) · Source PDF reference: pp. 9–10 · [M03](../modules/m03.md)

Printed key: **B** — To identify active (alive) hosts within a subnet. · Review: `study-note`.

-g expands a subnet/range and -a reports responsive targets; this discovers reachability rather than service ports.

<a id="ceh13-mock03-q036"></a>

## CEH13-MOCK03-Q036 — Document metadata

[Question 36](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-36) · Source PDF reference: p. 10 · [M02](../modules/m02.md)

Printed key: **C** — FOCA · Review: `study-note`.

FOCA is associated with extracting public-document metadata; software/user strings remain potentially stale clues.

<a id="ceh13-mock03-q037"></a>

## CEH13-MOCK03-Q037 — Implementation leakage

[Question 37](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-37) · Source PDF reference: p. 10 · [M20](../modules/m20.md)

Printed key: **B** — Physical information leaked by the hardware (e.g., power consumption, timing). · Review: `study-note`.

Timing, power and other implementation signals can leak secrets independently of the cipher's abstract security.

<a id="ceh13-mock03-q038"></a>

## CEH13-MOCK03-Q038 — Exhaustive guessing

[Question 38](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-38) · Source PDF reference: p. 10 · [M06](../modules/m06.md)

Printed key: **B** — Brute-Force Attack · Review: `study-note`.

Brute force enumerates the defined candidate space; feasibility depends on entropy and verification cost.

<a id="ceh13-mock03-q039"></a>

## CEH13-MOCK03-Q039 — Pass-the-hash

[Question 39](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-39) · Source PDF reference: pp. 10–11 · [M06](../modules/m06.md)

Printed key: **B** — Pass-the-Hash (PtH) · Review: `study-note`.

Supported authentication protocols can accept a stolen hash-derived credential without plaintext recovery; arbitrary hashes are not universally reusable.

<a id="ceh13-mock03-q040"></a>

## CEH13-MOCK03-Q040 — Honeypot purpose

[Question 40](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-40) · Source PDF reference: p. 11 · [M12](../modules/m12.md)

Printed key: **B** — To distract and monitor attackers by providing a decoy system. · Review: `study-note`.

A monitored decoy attracts and records interactions; isolate it so observation does not create a production foothold.

<a id="ceh13-mock03-q041"></a>

## CEH13-MOCK03-Q041 — Vulnerability scanner

[Question 41](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-41) · Source PDF reference: p. 11 · [M05](../modules/m05.md)

Printed key: **C** — Nessus · Review: `study-note`.

Nessus reports candidate patch/configuration weaknesses; verify applicability and do not equate scanner output with successful exploitation.

<a id="ceh13-mock03-q042"></a>

## CEH13-MOCK03-Q042 — MX lookup

[Question 42](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-42) · Source PDF reference: p. 11 · [M04](../modules/m04.md)

Printed key: **C** — MX record · Review: `study-note`.

MX names the zone's mail exchangers; priorities rank delivery preference.

<a id="ceh13-mock03-q043"></a>

## CEH13-MOCK03-Q043 — Evil-twin impersonation

[Question 43](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-43) · Source PDF reference: p. 11 · [M16](../modules/m16.md)

Printed key: **B** — Evil Twin · Review: `study-note`.

A fake AP imitating a legitimate network is an evil twin; a rogue AP need not impersonate another.

<a id="ceh13-mock03-q044"></a>

## CEH13-MOCK03-Q044 — Ettercap role

[Question 44](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-44) · Source PDF reference: p. 12 · [M08](../modules/m08.md)

Printed key: **B** — Ettercap · Review: `study-note`.

The source associates local MitM/DNS manipulation with Ettercap; authenticated encryption and local-link conditions constrain outcomes.

<a id="ceh13-mock03-q045"></a>

## CEH13-MOCK03-Q045 — DoS meaning

[Question 45](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-45) · Source PDF reference: p. 12 · [M10](../modules/m10.md)

Printed key: **C** — Denial · Review: `study-note`.

DoS means denial of service; distributed refers to multiple participating sources in DDoS.

<a id="ceh13-mock03-q046"></a>

## CEH13-MOCK03-Q046 — Human manipulation

[Question 46](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-46) · Source PDF reference: p. 12 · [M09](../modules/m09.md)

Printed key: **C** — Social Engineering · Review: `study-note`.

Social engineering exploits trust and decision processes; channel and pretext give more specific classifications.

<a id="ceh13-mock03-q047"></a>

## CEH13-MOCK03-Q047 — Token exposure in URLs

[Question 47](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-47) · Source PDF reference: p. 12 · [M11](../modules/m11.md)

Printed key: **B** — Sensitive Data Exposure · Review: `study-note`.

URL tokens can leak through browser history, logs and referrers; use secure session handling and remove secrets from URLs.

<a id="ceh13-mock03-q048"></a>

## CEH13-MOCK03-Q048 — NSE vulnerability category

[Question 48](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-48) · Source PDF reference: pp. 12–13 · [M05](../modules/m05.md)

Printed key: **C** — vuln · Review: `study-note`.

vuln groups vulnerability-related scripts; category labels do not guarantee safe or non-intrusive behavior.

<a id="ceh13-mock03-q049"></a>

## CEH13-MOCK03-Q049 — Password salts

[Question 49](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-49) · Source PDF reference: p. 13 · [M06](../modules/m06.md)

Printed key: **B** — To prevent the use of precomputed Rainbow Tables. · Review: `study-note`.

A unique salt prevents reuse of one precomputed table across users; use a slow password KDF to add per-guess cost.

<a id="ceh13-mock03-q050"></a>

## CEH13-MOCK03-Q050 — Keylogging

[Question 50](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-50) · Source PDF reference: p. 13 · [M07](../modules/m07.md)

Printed key: **B** — Keylogger · Review: `study-note`.

Capturing keyboard input is keylogging; scope varies from a web form to a user session or physical device.

<a id="ceh13-mock03-q051"></a>

## CEH13-MOCK03-Q051 — Kill-chain order

[Question 51](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-51) · Source PDF reference: p. 13 · [M01](../modules/m01.md)

Printed key: **B** — Weaponization · Review: `study-note`.

Weaponization follows reconnaissance in the traditional kill chain; delivery transmits the prepared artifact.

<a id="ceh13-mock03-q052"></a>

## CEH13-MOCK03-Q052 — Windows route table

[Question 52](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-52) · Source PDF reference: pp. 13–14 · [M03](../modules/m03.md)

Printed key: **C** — route print · Review: `study-note`.

route print displays local routes; traceroute observes a path and ipconfig shows interface configuration.

<a id="ceh13-mock03-q053"></a>

## CEH13-MOCK03-Q053 — Targeted phishing

[Question 53](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-53) · Source PDF reference: p. 14 · [M09](../modules/m09.md)

Printed key: **B** — Spear Phishing · Review: `study-note`.

A specific employee receiving a crafted executive impersonation is spear phishing; executive impersonation alone does not make the victim a whaling target.

<a id="ceh13-mock03-q054"></a>

## CEH13-MOCK03-Q054 — SSH port

[Question 54](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-54) · Source PDF reference: p. 14 · [M04](../modules/m04.md)

Printed key: **B** — SSH · Review: `study-note`.

TCP 22 is the conventional SSH service port; an observed port number is only an identification lead.

<a id="ceh13-mock03-q055"></a>

## CEH13-MOCK03-Q055 — Footprinting objective

[Question 55](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-55) · Source PDF reference: p. 14 · [M02](../modules/m02.md)

Printed key: **C** — To collect as much information as possible about a target network. · Review: `study-note`.

Gather relevant target information within scope to build hypotheses; more data is useful only when reliable and actionable.

<a id="ceh13-mock03-q056"></a>

## CEH13-MOCK03-Q056 — RSA family

[Question 56](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-56) · Source PDF reference: p. 14 · [M20](../modules/m20.md)

Printed key: **C** — RSA · Review: `study-note`.

RSA is asymmetric; AES, DES and Blowfish are symmetric block ciphers.

<a id="ceh13-mock03-q057"></a>

## CEH13-MOCK03-Q057 — Rootkit purpose

[Question 57](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-57) · Source PDF reference: pp. 14–15 · [M07](../modules/m07.md)

Printed key: **C** — To maintain hidden access to a system at the OS level. · Review: `study-note`.

A rootkit conceals privileged presence/access by subverting trusted system views; persistence layer varies.

<a id="ceh13-mock03-q058"></a>

## CEH13-MOCK03-Q058 — HTTP upload methods

[Question 58](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-58) · Source PDF reference: p. 15 · [M13](../modules/m13.md)

Printed key: **C** — PUT · Review: `qualified`.

PUT creates/replaces a resource at the target URI; many browser uploads use POST multipart forms.

Review detail: typically used to upload is underspecified; both PUT and POST support upload workflows.

<a id="ceh13-mock03-q059"></a>

## CEH13-MOCK03-Q059 — XSS impact

[Question 59](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-59) · Source PDF reference: p. 15 · [M14](../modules/m14.md)

Printed key: **B** — Executing malicious scripts in the victim's browser. · Review: `study-note`.

Injected script executes in a victim's browser origin context; server-side command execution is a different vulnerability.

<a id="ceh13-mock03-q060"></a>

## CEH13-MOCK03-Q060 — Wardriving tool history

[Question 60](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-60) · Source PDF reference: p. 15 · [M16](../modules/m16.md)

Printed key: **B** — NetStumbler · Review: `study-note`.

NetStumbler is a historical wireless discovery example; present platform/adapter compatibility requires verification.

<a id="ceh13-mock03-q061"></a>

## CEH13-MOCK03-Q061 — KRACK conditions

[Question 61](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-61) · Source PDF reference: pp. 15–16 · [M16](../modules/m16.md)

Printed key: **B** — KRACK (Key Reinstallation Attack) · Review: `study-note`.

A vulnerable key reinstall can reuse nonce/replay state; it does not reveal a WPA2 password or affect all patched clients equally.

Selected primary check: [R20](../references.md#r20).

<a id="ceh13-mock03-q062"></a>

## CEH13-MOCK03-Q062 — Burp scanning roles

[Question 62](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-62) · Source PDF reference: p. 16 · [M14](../modules/m14.md)

Printed key: **C** — Dashboard / Scanner · Review: `study-note`.

Automated Scanner/Dashboard functionality is separate from Repeater, Intruder and Sequencer; edition/version affects availability.

<a id="ceh13-mock03-q063"></a>

## CEH13-MOCK03-Q063 — Boolean blind channel

[Question 63](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-63) · Source PDF reference: p. 16 · [M15](../modules/m15.md)

Printed key: **B** — Blind SQLi · Review: `study-note`.

True/false behavior reveals a predicate outcome without directly returning database rows.

<a id="ceh13-mock03-q064"></a>

## CEH13-MOCK03-Q064 — Buffer overflow

[Question 64](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-64) · Source PDF reference: p. 16 · [M06](../modules/m06.md)

Printed key: **B** — Buffer Overflow · Review: `study-note`.

A write beyond a buffer boundary is memory corruption; code execution depends on control of memory and mitigations.

<a id="ceh13-mock03-q065"></a>

## CEH13-MOCK03-Q065 — Steganography

[Question 65](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-65) · Source PDF reference: pp. 16–17 · [M20](../modules/m20.md)

Printed key: **B** — Steganography · Review: `study-note`.

Hide a message within a carrier; encryption instead protects message content and the two can be combined.

<a id="ceh13-mock03-q066"></a>

## CEH13-MOCK03-Q066 — Physical responsibility

[Question 66](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-66) · Source PDF reference: p. 17 · [M19](../modules/m19.md)

Printed key: **A** — The Cloud Service Provider (CSP) · Review: `study-note`.

The cloud provider operates physical datacenter security in SaaS; customer identities, data use and configuration retain their own responsibilities.

<a id="ceh13-mock03-q067"></a>

## CEH13-MOCK03-Q067 — MQTT

[Question 67](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-67) · Source PDF reference: p. 17 · [M18](../modules/m18.md)

Printed key: **B** — MQTT · Review: `study-note`.

MQTT is a lightweight publish/subscribe messaging protocol; authentication, authorization and TLS need deliberate configuration.

<a id="ceh13-mock03-q068"></a>

## CEH13-MOCK03-Q068 — Adversarial ML input

[Question 68](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-68) · Source PDF reference: p. 17 · [M07](../modules/m07.md)

Printed key: **C** — Adversarial Attack · Review: `study-note`.

An inference-time crafted input causing misclassification is adversarial evasion; modifying training data is poisoning.

<a id="ceh13-mock03-q069"></a>

## CEH13-MOCK03-Q069 — Containers

[Question 69](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-69) · Source PDF reference: pp. 17–18 · [M19](../modules/m19.md)

Printed key: **B** — Containers · Review: `study-note`.

Containers isolate processes/user space while commonly sharing the host kernel; they are distinct from separate guest-kernel VMs.

<a id="ceh13-mock03-q070"></a>

## CEH13-MOCK03-Q070 — Ransomware

[Question 70](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-70) · Source PDF reference: p. 18 · [M07](../modules/m07.md)

Printed key: **C** — Ransomware · Review: `study-note`.

Encrypting files with an extortion demand is ransomware; payment method is incidental to the malware classification.

<a id="ceh13-mock03-q071"></a>

## CEH13-MOCK03-Q071 — Signature properties

[Question 71](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-71) · Source PDF reference: p. 18 · [M20](../modules/m20.md)

Printed key: **B** — Integrity, Non-repudiation, and Authentication · Review: `study-note`.

A verified signature supports integrity and signer-key authentication; nonrepudiation depends on identity binding and key custody.

<a id="ceh13-mock03-q072"></a>

## CEH13-MOCK03-Q072 — IDS versus IPS

[Question 72](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-72) · Source PDF reference: p. 18 · [M12](../modules/m12.md)

Printed key: **C** — IDS alerts on threats; IPS actively blocks threats. · Review: `study-note`.

IDS primarily detects/alerts while an inline IPS can enforce blocking; deployment configuration determines actual behavior.

<a id="ceh13-mock03-q073"></a>

## CEH13-MOCK03-Q073 — State tracking

[Question 73](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-73) · Source PDF reference: p. 18 · [M12](../modules/m12.md)

Printed key: **B** — Stateful Inspection Firewall · Review: `study-note`.

A stateful firewall checks traffic against connection context rather than independent packet headers alone.

<a id="ceh13-mock03-q074"></a>

## CEH13-MOCK03-Q074 — Hash limitation

[Question 74](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-74) · Source PDF reference: pp. 18–19 · [M20](../modules/m20.md)

Printed key: **C** — Hashing · Review: `study-note`.

A cryptographic digest detects changes only when compared with a trusted expected digest; it does not by itself authenticate the sender.

<a id="ceh13-mock03-q075"></a>

## CEH13-MOCK03-Q075 — OWASP lists

[Question 75](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-75) · Source PDF reference: p. 19 · [M14](../modules/m14.md)

Printed key: **B** — OWASP · Review: `study-note`.

OWASP publishes versioned risk lists; web, API, mobile and IoT editions use distinct categories.

<a id="ceh13-mock03-q076"></a>

## CEH13-MOCK03-Q076 — Exploit and payload

[Question 76](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-76) · Source PDF reference: p. 19 · [M06](../modules/m06.md)

Printed key: **B** — Exploit · Review: `qualified`.

An exploit triggers a vulnerability and a payload performs selected post-trigger behavior; the two roles should be distinguished.

Review detail: delivering code is imprecise wording when payload is omitted from the options.

<a id="ceh13-mock03-q077"></a>

## CEH13-MOCK03-Q077 — Wireshark display filter

[Question 77](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-77) · Source PDF reference: p. 19 · [M08](../modules/m08.md)

Printed key: **B** — ip.addr == 10.0.0.5 · Review: `study-note`.

ip.addr == 10.0.0.5 matches IPv4 source or destination in displayed captured packets; capture-filter syntax is different.

<a id="ceh13-mock03-q078"></a>

## CEH13-MOCK03-Q078 — ARP poisoning

[Question 78](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-78) · Source PDF reference: pp. 19–20 · [M08](../modules/m08.md)

Printed key: **B** — ARP Poisoning (Spoofing) · Review: `study-note`.

A forged IP-to-MAC association redirects local-link delivery; inspect trusted gateway bindings and switch evidence.

<a id="ceh13-mock03-q079"></a>

## CEH13-MOCK03-Q079 — DNSSEC properties

[Question 79](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-79) · Source PDF reference: p. 20 · [M04](../modules/m04.md)

Printed key: **C** — To provide authentication and integrity to DNS data. · Review: `study-note`.

DNSSEC provides origin authentication and integrity for signed DNS data; it does not encrypt DNS queries or classify malicious sites.

Selected primary check: [R25](../references.md#r25).

<a id="ceh13-mock03-q080"></a>

## CEH13-MOCK03-Q080 — Authentication factors

[Question 80](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-80) · Source PDF reference: p. 20 · [M06](../modules/m06.md)

Printed key: **C** — Fingerprint · Review: `study-note`.

A fingerprint is an inherence factor; passwords are knowledge and hardware tokens are possession.

<a id="ceh13-mock03-q081"></a>

## CEH13-MOCK03-Q081 — Bluesnarfing

[Question 81](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-81) · Source PDF reference: p. 20 · [M16](../modules/m16.md)

Printed key: **B** — Bluesnarfing · Review: `study-note`.

Unauthorized Bluetooth data retrieval is bluesnarfing; unsolicited message delivery is bluejacking.

<a id="ceh13-mock03-q082"></a>

## CEH13-MOCK03-Q082 — MDM

[Question 82](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-82) · Source PDF reference: pp. 20–21 · [M17](../modules/m17.md)

Printed key: **B** — To enforce security policies and remotely wipe corporate mobile devices. · Review: `study-note`.

Managed device policy and remote response are core MDM roles; enrollment, platform permissions and connectivity constrain actions.

<a id="ceh13-mock03-q083"></a>

## CEH13-MOCK03-Q083 — REST authorization

[Question 83](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-83) · Source PDF reference: p. 21 · [M14](../modules/m14.md)

Printed key: **B** — REST · Review: `study-note`.

REST commonly uses HTTP resource operations; object/function authorization must be enforced regardless of architecture style.

<a id="ceh13-mock03-q084"></a>

## CEH13-MOCK03-Q084 — CSRF

[Question 84](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-84) · Source PDF reference: p. 21 · [M14](../modules/m14.md)

Printed key: **B** — CSRF (Cross-Site Request Forgery) · Review: `study-note`.

A victim browser making an unwanted authenticated cross-site action is CSRF; token theft is not required.

<a id="ceh13-mock03-q085"></a>

## CEH13-MOCK03-Q085 — IDOR/BOLA

[Question 85](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-85) · Source PDF reference: p. 21 · [M14](../modules/m14.md)

Printed key: **B** — IDOR (Insecure Direct Object Reference) · Review: `study-note`.

Changing an object ID and receiving unauthorized private data demonstrates missing object authorization.

<a id="ceh13-mock03-q086"></a>

## CEH13-MOCK03-Q086 — SOC triage

[Question 86](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-86) · Source PDF reference: pp. 21–22 · [M01](../modules/m01.md)

Printed key: **A** — Tier 1 Analyst · Review: `study-note`.

Tier-1 analysts commonly monitor and triage alerts; actual team responsibilities depend on the organization's operating model.

<a id="ceh13-mock03-q087"></a>

## CEH13-MOCK03-Q087 — Incident-response model

[Question 87](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-87) · Source PDF reference: p. 22 · [M01](../modules/m01.md)

Printed key: **C** — Preparation · Review: `qualified`.

Preparation is first in the traditional four-phase model; distinguish this mnemonic from current NIST CSF-aligned incident-response guidance.

Review detail: the question must name the framework/version before claiming one universal first phase.

Selected primary check: [R10](../references.md#r10).

<a id="ceh13-mock03-q088"></a>

## CEH13-MOCK03-Q088 — Business continuity

[Question 88](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-88) · Source PDF reference: p. 22 · [M01](../modules/m01.md)

Printed key: **C** — BCP (Business Continuity Plan) · Review: `study-note`.

A BCP defines how critical business functions continue during disruption; disaster recovery focuses on restoring systems/services.

<a id="ceh13-mock03-q089"></a>

## CEH13-MOCK03-Q089 — Unix mode bits

[Question 89](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-89) · Source PDF reference: p. 22 · [M06](../modules/m06.md)

Printed key: **C** — Grants full read, write, and execute permissions to everyone. · Review: `study-note`.

Mode 777 grants owner/group/other read, write and execute bits; ACLs, mount options and other policies may still constrain access.

<a id="ceh13-mock03-q090"></a>

## CEH13-MOCK03-Q090 — Current-user registry

[Question 90](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-90) · Source PDF reference: p. 22 · [M06](../modules/m06.md)

Printed key: **B** — HKEY_CURRENT_USER (HKCU) · Review: `study-note`.

HKCU presents configuration for the current user; HKLM holds machine-wide configuration.

<a id="ceh13-mock03-q091"></a>

## CEH13-MOCK03-Q091 — Vertical escalation

[Question 91](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-91) · Source PDF reference: p. 23 · [M06](../modules/m06.md)

Printed key: **B** — Vertical Privilege Escalation · Review: `study-note`.

Low-privilege to administrative rights crosses an authority tier; lateral movement crosses systems and is a different dimension.

<a id="ceh13-mock03-q092"></a>

## CEH13-MOCK03-Q092 — Log tampering

[Question 92](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-92) · Source PDF reference: p. 23 · [M06](../modules/m06.md)

Printed key: **C** — wevtutil or Event Viewer · Review: `study-note`.

wevtutil/Event Viewer can clear permitted Windows event logs; centralized copies and tampering alerts can preserve evidence.

<a id="ceh13-mock03-q093"></a>

## CEH13-MOCK03-Q093 — Dynamic malware analysis

[Question 93](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-93) · Source PDF reference: p. 23 · [M07](../modules/m07.md)

Printed key: **B** — Dynamic Analysis (Sandboxing) · Review: `study-note`.

Observe execution in an isolated controlled environment; static analysis examines artifacts without running the payload.

<a id="ceh13-mock03-q094"></a>

## CEH13-MOCK03-Q094 — RAT scope

[Question 94](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-94) · Source PDF reference: pp. 23–24 · [M07](../modules/m07.md)

Printed key: **B** — RAT (Remote Access Trojan) · Review: `study-note`.

A remote-access Trojan supplies remote control subject to obtained privileges; complete control is not guaranteed on every host.

<a id="ceh13-mock03-q095"></a>

## CEH13-MOCK03-Q095 — Session splicing

[Question 95](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-95) · Source PDF reference: p. 24 · [M12](../modules/m12.md)

Printed key: **B** — It splits the attack payload into multiple small packets to avoid signature matching. · Review: `study-note`.

Splitting application bytes across small TCP segments exploits weak stream reconstruction; distinguish it from IP fragmentation.

<a id="ceh13-mock03-q096"></a>

## CEH13-MOCK03-Q096 — Encapsulation tunnel

[Question 96](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-96) · Source PDF reference: p. 24 · [M12](../modules/m12.md)

Printed key: **B** — Tunneling · Review: `study-note`.

Carrying a prohibited protocol inside an allowed one is tunneling; protocol-aware inspection may still identify it.

<a id="ceh13-mock03-q097"></a>

## CEH13-MOCK03-Q097 — SQL query/data separation

[Question 97](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-97) · Source PDF reference: p. 24 · [M15](../modules/m15.md)

Printed key: **C** — Using Prepared Statements (Parameterized Queries). · Review: `study-note`.

Prepared statements bind values as data; dynamic table/column names still require safe allowlisting/design.

<a id="ceh13-mock03-q098"></a>

## CEH13-MOCK03-Q098 — IaaS responsibilities

[Question 98](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-98) · Source PDF reference: pp. 24–25 · [M19](../modules/m19.md)

Printed key: **A** — IaaS (Infrastructure as a Service) · Review: `study-note`.

IaaS gives the customer OS/middleware control while the provider operates underlying infrastructure; compare exact service contracts.

<a id="ceh13-mock03-q099"></a>

## CEH13-MOCK03-Q099 — OT and ICS

[Question 99](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-99) · Source PDF reference: p. 25 · [M18](../modules/m18.md)

Printed key: **C** — OT / ICS (Operational Technology / Industrial Control Systems) · Review: `study-note`.

A PLC controlling a water-treatment process is OT/ICS; physical safety and availability shape assessment acceptance.

<a id="ceh13-mock03-q100"></a>

## CEH13-MOCK03-Q100 — Zero-day terminology

[Question 100](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-100) · Source PDF reference: p. 25 · [M05](../modules/m05.md)

Printed key: **C** — A vulnerability that is unknown to the vendor and has no available patch. · Review: `qualified`.

Zero-day commonly describes a newly unknown/unpatched vulnerability; disclosure, vendor awareness and patch status should be recorded separately.

Review detail: vendor-known but still unpatched flaws may also be described as zero-day in incident reporting.

<a id="ceh13-mock03-q101"></a>

## CEH13-MOCK03-Q101 — Zero-trust decisions

[Question 101](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-101) · Source PDF reference: pp. 25–26 · [M01](../modules/m01.md)

Printed key: **C** — To never trust, always verify, regardless of where the request originates. · Review: `study-note`.

Grant access based on explicit identity, device, resource and context policy rather than network location alone; the source slogan is a shorthand.

Selected primary check: [R17](../references.md#r17).

<a id="ceh13-mock03-q102"></a>

## CEH13-MOCK03-Q102 — Training-data poisoning

[Question 102](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-102) · Source PDF reference: p. 26 · [M07](../modules/m07.md)

Printed key: **B** — Data Poisoning · Review: `study-note`.

Changing training examples to embed triggered behavior is poisoning/backdooring; inference-time input attacks are evasion.

<a id="ceh13-mock03-q103"></a>

## CEH13-MOCK03-Q103 — Bluejacking

[Question 103](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-103) · Source PDF reference: p. 26 · [M16](../modules/m16.md)

Printed key: **A** — Bluejacking · Review: `study-note`.

Unsolicited Bluetooth messaging is bluejacking; unauthorized data extraction is bluesnarfing.

<a id="ceh13-mock03-q104"></a>

## CEH13-MOCK03-Q104 — SAE name

[Question 104](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-104) · Source PDF reference: pp. 26–27 · [M16](../modules/m16.md)

Printed key: **B** — Simultaneous (Simultaneous Authentication of Equals) · Review: `study-note`.

SAE expands to Simultaneous Authentication of Equals; its password-authenticated exchange differs from WPA2-PSK offline verification.

<a id="ceh13-mock03-q105"></a>

## CEH13-MOCK03-Q105 — SLE arithmetic

[Question 105](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-105) · Source PDF reference: p. 27 · [M01](../modules/m01.md)

Printed key: **B** — $50,000 · Review: `study-note`.

SLE equals asset value times exposure factor: $100,000 × 0.5 = $50,000; ALE also needs annualized occurrence frequency.

<a id="ceh13-mock03-q106"></a>

## CEH13-MOCK03-Q106 — Enterprise policy

[Question 106](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-106) · Source PDF reference: p. 27 · [M01](../modules/m01.md)

Printed key: **A** — Enterprise Information Security Policy (EISP) · Review: `study-note`.

An organization-wide policy sets security purpose and principles; issue-specific and system-specific policies provide narrower rules.

<a id="ceh13-mock03-q107"></a>

## CEH13-MOCK03-Q107 — HIPAA scope

[Question 107](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-107) · Source PDF reference: p. 27 · [M01](../modules/m01.md)

Printed key: **C** — HIPAA · Review: `qualified`.

The intended U.S. law is HIPAA; applicability depends on covered-entity/business-associate status and the data involved.

Review detail: this study identification is not an organization-specific compliance determination.

Selected primary check: [R18](../references.md#r18).

<a id="ceh13-mock03-q108"></a>

## CEH13-MOCK03-Q108 — Telnet banner

[Question 108](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-108) · Source PDF reference: pp. 27–28 · [M03](../modules/m03.md)

Printed key: **B** — Banner Grabbing · Review: `study-note`.

The displayed OS string is a service-provided banner; corroborate version/OS identity before assessing applicability.

<a id="ceh13-mock03-q109"></a>

## CEH13-MOCK03-Q109 — Aggressive timing

[Question 109](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-109) · Source PDF reference: p. 28 · [M03](../modules/m03.md)

Printed key: **D** — T5 (Insane) · Review: `study-note`.

-T5 is Nmap's most aggressive preset; faster settings can lose results or disrupt fragile services and are readily detectable.

<a id="ceh13-mock03-q110"></a>

## CEH13-MOCK03-Q110 — Purge terminology

[Question 110](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-110) · Source PDF reference: p. 28 · [M06](../modules/m06.md)

Printed key: **B** — To make data recovery impossible even with laboratory-grade tools. · Review: `qualified`.

Purge aims to make recovery infeasible using state-of-the-art laboratory techniques while potentially preserving media reuse.

Review detail: the printed impossible guarantee is stronger than an evidence-based sanitization claim; method/media validation matters.

Selected primary check: [R16](../references.md#r16).

<a id="ceh13-mock03-q111"></a>

## CEH13-MOCK03-Q111 — Search-engine findings

[Question 111](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-111) · Source PDF reference: p. 28 · [M02](../modules/m02.md)

Printed key: **C** — Google Search Engine · Review: `study-note`.

Google operators find indexed candidate exposures; search results alone do not prove a vulnerable web-server version.

<a id="ceh13-mock03-q112"></a>

## CEH13-MOCK03-Q112 — Hacktivist objective

[Question 112](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-112) · Source PDF reference: pp. 28–29 · [M01](../modules/m01.md)

Printed key: **B** — Hacktivist · Review: `study-note`.

A political/social motive fits hacktivism; authorization and actual actor attribution remain independent.

<a id="ceh13-mock03-q113"></a>

## CEH13-MOCK03-Q113 — Physical control

[Question 113](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-113) · Source PDF reference: p. 29 · [M01](../modules/m01.md)

Printed key: **C** — Security Guard · Review: `study-note`.

A security guard implements physical access/response controls; technical controls protect other layers.

<a id="ceh13-mock03-q114"></a>

## CEH13-MOCK03-Q114 — Containment purpose

[Question 114](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-114) · Source PDF reference: p. 29 · [M01](../modules/m01.md)

Printed key: **B** — The affected systems are isolated to prevent the threat from spreading. · Review: `study-note`.

Limit spread and ongoing harm using safe isolation or other restrictions; eradication removes cause and recovery restores service.

<a id="ceh13-mock03-q115"></a>

## CEH13-MOCK03-Q115 — Power side channel

[Question 115](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-115) · Source PDF reference: p. 29 · [M20](../modules/m20.md)

Printed key: **B** — Power Analysis Attack · Review: `study-note`.

Power-consumption correlations are power analysis; distinguish timing and fault-injection mechanisms.

<a id="ceh13-mock03-q116"></a>

## CEH13-MOCK03-Q116 — Container hardening

[Question 116](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-116) · Source PDF reference: pp. 29–30 · [M19](../modules/m19.md)

Printed key: **B** — Using minimal base images and scanning for vulnerabilities. · Review: `study-note`.

Minimal trusted images and vulnerability checks reduce unnecessary components; also restrict privileges, secrets and runtime access.

<a id="ceh13-mock03-q117"></a>

## CEH13-MOCK03-Q117 — Netcat listener syntax

[Question 117](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-117) · Source PDF reference: p. 30 · [M04](../modules/m04.md)

Printed key: **B** — To listen for an incoming connection on port 4444. · Review: `qualified`.

The intended traditional netcat command listens on port 4444; option syntax differs across implementations.

Review detail: preserve the source syntax and inspect the installed variant before any separately authorized use.

<a id="ceh13-mock03-q118"></a>

## CEH13-MOCK03-Q118 — Traceroute probes and replies

[Question 118](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-118) · Source PDF reference: p. 30 · [M03](../modules/m03.md)

Printed key: **C** — ICMP · Review: `hold`.

Traceroute commonly uses UDP, ICMP or TCP probes and learns hops from ICMP Time Exceeded responses.

Review detail: the question conflates probe transport with returned ICMP errors; ICMP is not the only traceroute probe protocol.

<a id="ceh13-mock03-q119"></a>

## CEH13-MOCK03-Q119 — Stack corruption

[Question 119](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-119) · Source PDF reference: p. 30 · [M06](../modules/m06.md)

Printed key: **A** — Stack-based Buffer Overflow · Review: `study-note`.

Overwriting a stack return address is stack-based buffer overflow; ASLR, NX and canaries affect exploitability.

<a id="ceh13-mock03-q120"></a>

## CEH13-MOCK03-Q120 — Slowloris symptom

[Question 120](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-120) · Source PDF reference: p. 30 · [M10](../modules/m10.md)

Printed key: **B** — The web server runs out of available connections because many remain partially open. · Review: `study-note`.

Many incompletely sent HTTP requests can exhaust concurrent connection capacity without link saturation.

<a id="ceh13-mock03-q121"></a>

## CEH13-MOCK03-Q121 — CA trust

[Question 121](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-121) · Source PDF reference: pp. 30–31 · [M20](../modules/m20.md)

Printed key: **C** — The Certificate Authority (CA) · Review: `study-note`.

A CA signs certificates binding a key to validated identity attributes; relying parties still verify chains, names, validity and relevant revocation.

<a id="ceh13-mock03-q122"></a>

## CEH13-MOCK03-Q122 — Fuzzing scope

[Question 122](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-122) · Source PDF reference: p. 31 · [M05](../modules/m05.md)

Printed key: **B** — Sending massive amounts of random data to a program to find crashes and vulnerabilities. · Review: `qualified`.

Fuzzing exercises input handling with generated or mutated cases; structured, coverage-guided and deterministic approaches also exist.

Review detail: massive random input is an incomplete definition and does not guarantee vulnerability discovery.

<a id="ceh13-mock03-q123"></a>

## CEH13-MOCK03-Q123 — Passive discovery

[Question 123](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-123) · Source PDF reference: p. 31 · [M03](../modules/m03.md)

Printed key: **C** — Passive Discovery · Review: `study-note`.

Observing existing traffic emits no target probes from the discovery activity; capture permissions and vantage still matter.

<a id="ceh13-mock03-q124"></a>

## CEH13-MOCK03-Q124 — Written authorization

[Question 124](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-124) · Source PDF reference: p. 31 · [M01](../modules/m01.md)

Printed key: **C** — Always obtain written permission before testing. · Review: `study-note`.

Obtain explicit written permission, scope and stop conditions from the appropriate owner before testing.

<a id="ceh13-mock03-q125"></a>

## CEH13-MOCK03-Q125 — Reporting

[Question 125](../../../source/2026-11-09-ceh-v13-mock-exams/mock-03-125.source.md#question-125) · Source PDF reference: pp. 31–32 · [M01](../modules/m01.md)

Printed key: **D** — Reporting · Review: `study-note`.

Deliver evidence, impact, limitations and actionable recommendations to the agreed audience; testing and report acceptance are separate gates.
