# Primary-source checks

[Collection index](README.md) · [Question audit](quality-audit.md)

Accessed 2026-11-09 (Asia/Taipei). These are selected primary checks of mechanisms and disputed claims. They do not authenticate the supplied PDFs, certify the whole answer key or establish an official exam distribution. Standards retain the named version; the NIST OT page also links a later draft, whose existence does not make that draft the final standard used here. No third-party exam site was visited or downloaded.

<a id="r01"></a>

## R01 — Nmap: Firewall/IDS Evasion and Spoofing

[Nmap: Firewall/IDS Evasion and Spoofing](https://nmap.org/book/man-bypass-firewalls-ids.html). MAC spoofing affects raw Ethernet scans, not connection-oriented features; fragment/evasion claims have implementation limits.

<a id="r02"></a>

## R02 — Nmap: Port Scanning Techniques

[Nmap: Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html). Scan type, returned packets and target-stack behavior determine state interpretation; FIN/NULL/Xmas are not universal invisibility techniques.

<a id="r03"></a>

## R03 — RFC 1191: Path MTU Discovery

[RFC 1191: Path MTU Discovery](https://www.rfc-editor.org/rfc/rfc1191). IPv4 fragmentation-needed ICMP errors support classic path-MTU discovery, so blocking every type-3 message can impair connectivity.

<a id="r04"></a>

## R04 — Microsoft: WAITFOR (Transact-SQL)

[Microsoft: WAITFOR (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/waitfor-transact-sql). WAITFOR DELAY is a SQL Server/Transact-SQL construct; the source's Oracle attribution should not be memorized.

<a id="r05"></a>

## R05 — hashcat: princeprocessor

[hashcat: princeprocessor](https://github.com/hashcat/princeprocessor). PRINCE builds chains from one input wordlist, distinguishing the source's described workflow from the ordinary two-input combinator.

<a id="r06"></a>

## R06 — BREACH: original research explanation

[BREACH: original research explanation](https://www.breachattack.com/). BREACH targets HTTP response compression with reflected input and a secret; CRIME's original mitigation concerns TLS/SPDY compression.

<a id="r07"></a>

## R07 — Google: How HTTP/2 Rapid Reset works (2023-10-10)

[Google: How HTTP/2 Rapid Reset works (2023-10-10)](https://cloud.google.com/blog/products/identity-security/how-it-works-the-novel-http2-rapid-reset-ddos-attack). The historical campaign surpassed 398 million requests per second using rapid stream resets; Google states it did not lead to outages.

<a id="r08"></a>

## R08 — Microsoft: Windows service and port requirements

[Microsoft: Windows service and port requirements](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements). Global Catalog is listed on TCP 3268/3269; the mock's UDP label is erroneous.

<a id="r09"></a>

## R09 — FIRST: CVSS v4.0 specification

[FIRST: CVSS v4.0 specification](https://www.first.org/cvss/v4.0/specification-document). CVSS is a standardized severity input; threat/environmental context and other local risk factors affect prioritization.

<a id="r10"></a>

## R10 — NIST SP 800-61r3: Incident Response (April 2025)

[NIST SP 800-61r3: Incident Response (April 2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final). Rev. 3 supersedes Rev. 2 and aligns incident response with CSF 2.0 risk management; label traditional phase questions by framework/version.

<a id="r11"></a>

## R11 — NIST SP 800-145: Definition of Cloud Computing

[NIST SP 800-145: Definition of Cloud Computing](https://csrc.nist.gov/pubs/sp/800/145/final). The definition separates five essential characteristics, three service models and four deployment models.

<a id="r12"></a>

## R12 — OWASP: Session Management Cheat Sheet

[OWASP: Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html). Use unpredictable session identifiers, rotate at authentication/privilege changes and invalidate sessions appropriately; cookie flags cover specific exposure paths.

<a id="r13"></a>

## R13 — OWASP: CSRF Prevention Cheat Sheet

[OWASP: CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html). CSRF induces unwanted authenticated requests; origin/token/SameSite controls address that mechanism separately from stealing a session identifier.

<a id="r14"></a>

## R14 — OWASP: SQL Injection Prevention Cheat Sheet

[OWASP: SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html). Parameterized queries separate values from query structure; dynamic identifiers require suitable safe design and escaping is not the general preferred repair.

<a id="r15"></a>

## R15 — Google Search Central: documentation updates

[Google Search Central: documentation updates](https://developers.google.com/search/updates). The official change log records removal of cache: documentation because the operator no longer works.

<a id="r16"></a>

## R16 — NIST SP 800-88r2: Media Sanitization (September 2025)

[NIST SP 800-88r2: Media Sanitization (September 2025)](https://csrc.nist.gov/pubs/sp/800/88/r2/final). Sanitization seeks infeasibility of access/recovery for a specified level of effort; avoid a universal impossible-recovery guarantee.

<a id="r17"></a>

## R17 — NIST SP 800-207: Zero Trust Architecture

[NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final). Network location and asset ownership alone grant no implicit trust; the supplied identity/device/least-privilege image is a partial teaching aid.

<a id="r18"></a>

## R18 — HHS: Covered Entities and Business Associates

[HHS: Covered Entities and Business Associates](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html). HIPAA applicability depends on covered-entity/business-associate definitions; a healthcare narrative alone is insufficient for a compliance determination.

<a id="r19"></a>

## R19 — RFC 8446: TLS 1.3

[RFC 8446: TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446). Content encryption is distinct from complete length/timing traffic-analysis resistance; a cipher name alone does not hide all metadata.

<a id="r20"></a>

## R20 — KRACK: original key-reinstallation research

[KRACK: original key-reinstallation research](https://www.krackattacks.com/). Vulnerable handshake key reinstallation can force nonce reuse; this is different from learning the Wi-Fi password.

<a id="r21"></a>

## R21 — AWS: Instance Metadata Service

[AWS: Instance Metadata Service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html). IMDSv2 is session-oriented; metadata access/configuration and a workload's attached role permissions define the relevant exposure.

<a id="r22"></a>

## R22 — Kubernetes: Security Checklist

[Kubernetes: Security Checklist](https://kubernetes.io/docs/concepts/security/security-checklist/). Workload privilege, access control, secrets and runtime protections need explicit configuration; image scanning alone does not establish isolation.

<a id="r23"></a>

## R23 — NIST SP 800-82r3: Guide to OT Security

[NIST SP 800-82r3: Guide to OT Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final). OT security must account for performance, reliability and safety requirements; controller isolation/probing decisions need operational coordination.

<a id="r24"></a>

## R24 — NIST: Post-Quantum Cryptography project

[NIST: Post-Quantum Cryptography project](https://csrc.nist.gov/projects/post-quantum-cryptography). Plan migration using supported post-quantum key-establishment/signature mechanisms and distinguish these roles from bulk symmetric encryption.

<a id="r25"></a>

## R25 — RFC 4033: DNS Security Introduction and Requirements

[RFC 4033: DNS Security Introduction and Requirements](https://www.rfc-editor.org/rfc/rfc4033). DNSSEC provides DNS data-origin authentication and integrity, not confidentiality or protection against every authoritative/account compromise.

<a id="r26"></a>

## R26 — IANA: Service Name and Transport Protocol Port Number Registry

[IANA: Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml). Registered service/transport assignments are identification leads; a port number does not prove the actual running application.

<a id="r27"></a>

## R27 — OpenLDAP: ldapsearch manual

[OpenLDAP: ldapsearch manual](https://www.openldap.org/software/man.cgi?query=ldapsearch). Search base, scope, filter and server URI are separate arguments; preserve malformed source commands and use complete client syntax in an authorized environment.
