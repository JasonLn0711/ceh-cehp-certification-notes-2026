# Question keys, defects and interpretation audit

[Collection index](README.md) · [All-item register](items.csv) · [Repeated stems](duplicates.csv) · [Primary evidence](references.md)

## Meaning of review labels

`study-note` explains the apparent intended mechanism. `qualified` records a material prerequisite, overlap or limitation. `hold` means the source content/key is unsuitable for scoring until repaired. Counts are 676 / 139 / 102 across 917 note records. These are editorial review outcomes. The remaining keys are not certified by omission from the hold list.

## Confirmed source structure

- Eight bank entries (Q5, Q101, Q181, Q210, Q251, Q335, Q372, Q469) paste explanation text into option E and print `A B C D E` as the answer. The explanation indicates an intended answer, but the original key remains preserved.
- Bank Q183 and Q512 supply three options. Q517 contains a second, malformed-heading BYOD question; it is recorded separately with its original label rather than merged into the honeypot question.
- Bank Q48 has no category in its heading. IoT/loT spellings and category variants remain as supplied; editorial module tags are separate.
- Mock 02 has no numbered Q110 and its table says `(無此題)`. No replacement item or inferred learner answer is created.
- Mock 03 uses bold-marked options and a derived index rather than a separately printed answer key. All 125 markings must agree with that derived index in validation.
- The image attached to Mock 03 illustrates identity verification, device verification and least privilege. Its simplified sequence is interpreted in [M01](modules/m01.md) against [NIST zero trust](references.md#r17).

## Selected primary-checked corrections

| Source entries | Study correction | Evidence |
| --- | --- | --- |
| Bank Q23; Mock 01 Q125; Mock 02 Q42 | MAC spoofing applies to raw Ethernet probes; -sT connect traffic is not established as spoofed by that option. | [R01](references.md#r01) |
| Bank Q91; Mock 01 Q99 | Blanket IPv4 type-3 blocking can suppress fragmentation-needed errors and break path-MTU discovery. | [R03](references.md#r03) |
| Bank Q172 | WAITFOR DELAY is Transact-SQL; the Oracle attribution is incorrect. | [R04](references.md#r04) |
| Mock 02 Q2 | Variable chains from one dictionary fit PRINCE; ordinary combinator mode has different input semantics. | [R05](references.md#r05) |
| Mock 02 Q111 | HTTP response-compression leakage is BREACH-family; CRIME refers to TLS/SPDY compression. | [R06](references.md#r06) |
| Bank Q147 | The 398-million-rps event was HTTP/2 Rapid Reset in 2023; Google says it did not cause outages. | [R07](references.md#r07) |
| Mock 02 Q56 | Global Catalog uses TCP 3268/3269; UDP in the supplied option is erroneous. | [R08](references.md#r08) |
| Bank Q381 | Google cache: is retired; use a currently available dated archive. | [R15](references.md#r15) |
| Bank Q185/Q386 | AES alone does not conceal traffic sizes/timing; encryption and traffic-analysis protection are separate. | [R19](references.md#r19) |
| Mock 03 Q87/Q110 | Name the incident-response framework/version and use sanitization infeasibility language rather than universal impossibility. | [R10](references.md#r10), [R16](references.md#r16) |
| Bank Q61; Mock 03 Q79 | DNSSEC provides authenticated DNS data, with no DNS confidentiality or universal hijack prevention. | [R25](references.md#r25) |
| Mock 02 Q58 | LDAP host/URI, search base and scope are separate arguments; the printed missing-host command is incomplete. | [R27](references.md#r27) |

These checks confirm the specific mechanism/version distinctions shown. Product-edition claims, rooting support, campaign attribution and every other printed answer remain within their stated review labels.

## Same-stem key conflicts

The [duplicate register](duplicates.csv) compares normalized stem strings while retaining different source options/keys. Substantive conflicts include active/blind hijacking (Bank Q509 ↔ Mock 01 Q5), email server/IP (Q405 ↔ Q71), injection methodology stage (Q398 ↔ Q72), OS/service discovery (Q232 ↔ Q93), wrapper/dropper (Q488 ↔ Q95), and governance/logging (Q130 ↔ Q120). Bank Q335 ↔ Mock 01 Q4 also conflicts with a malformed all-letter key and differing sequence-field interpretation. Some raw key differences are formatting/truncation rather than conceptual disagreement. Every pair remains inspectable; no key is selected merely by majority vote.

## Every held entry

| Entry | Concept | Issue |
| --- | --- | --- |
| [CEH13-BANK-Q004](questions/bank-001-100.md#ceh13-bank-q004) | OT covert channels | no universal hardest-to-detect technique follows from these choices; X2S is unexplained. |
| [CEH13-BANK-Q005](questions/bank-001-100.md#ceh13-bank-q005) | Graceful degradation | explanation is fused into option E and printed key is A B C D E; intended A follows the scenario. |
| [CEH13-BANK-Q015](questions/bank-001-100.md#ceh13-bank-q015) | Persistence discovery | an excluded extension cannot ensure a backdoor remains undetected. |
| [CEH13-BANK-Q016](questions/bank-001-100.md#ceh13-bank-q016) | Mobile RAT | hardest-to-detect ranking is unsupported. |
| [CEH13-BANK-Q023](questions/bank-001-100.md#ceh13-bank-q023) | Nmap MAC spoofing | -sT uses OS connect sockets; the printed command does not establish spoofing of connect traffic. |
| [CEH13-BANK-Q029](questions/bank-001-100.md#ceh13-bank-q029) | Search indexing limits | site:onion does not establish dark-web coverage; the proposed title is only a search hypothesis. |
| [CEH13-BANK-Q036](questions/bank-001-100.md#ceh13-bank-q036) | DNS cache snooping | NOERROR with no answer does not prove that no client recently requested the name. |
| [CEH13-BANK-Q042](questions/bank-001-100.md#ceh13-bank-q042) | Cloud exposure | an unspecified unknown vulnerability does not identify misconfigured security groups as the cause. |
| [CEH13-BANK-Q049](questions/bank-001-100.md#ceh13-bank-q049) | Firewall inspection | the wording about content beyond headers fits DPI better than the printed stateful-inspection answer. |
| [CEH13-BANK-Q060](questions/bank-001-100.md#ceh13-bank-q060) | Session replay | most-difficult ranking has no defined threat model. |
| [CEH13-BANK-Q088](questions/bank-001-100.md#ceh13-bank-q088) | Legacy TLS | old TLS does not by itself let a MitM decrypt an arbitrary session. |
| [CEH13-BANK-Q091](questions/bank-001-100.md#ceh13-bank-q091) | ICMP filtering | blocking all outbound IPv4 type 3 also blocks fragmentation-needed messages and can break connectivity. |
| [CEH13-BANK-Q101](questions/bank-101-200.md#ceh13-bank-q101) | Spoofing inference | explanation is fused into option E and key lists A B C D E; intended D is not a dependable anti-spoofing proof. |
| [CEH13-BANK-Q105](questions/bank-101-200.md#ceh13-bank-q105) | Local MitM versus remote hijacking | remote-access wording and hardest-to-detect ranking do not justify the printed local ARP answer. |
| [CEH13-BANK-Q108](questions/bank-101-200.md#ceh13-bank-q108) | Vulnerability lifecycle | the final stated activity is verification, while the key selects remediation; the asked phase is ambiguous. |
| [CEH13-BANK-Q111](questions/bank-101-200.md#ceh13-bank-q111) | Application resource exhaustion | no evidence ranks this above every other attack; distributed SQL injection is not a uniquely defined hardest DoS class. |
| [CEH13-BANK-Q119](questions/bank-101-200.md#ceh13-bank-q119) | ARP poisoning versus port stealing | the described fake ARP replies support ARP poisoning more directly than the printed port-stealing label. |
| [CEH13-BANK-Q144](questions/bank-101-200.md#ceh13-bank-q144) | Attack-path evidence | the SQL-injection key does not follow from the supplied evidence. |
| [CEH13-BANK-Q147](questions/bank-101-200.md#ceh13-bank-q147) | HTTP/2 Rapid Reset | source chronology and service-impact wording need the original Google incident report. |
| [CEH13-BANK-Q172](questions/bank-101-200.md#ceh13-bank-q172) | DBMS-specific time delays | Oracle backend and the printed WAITFOR DELAY answer conflict. |
| [CEH13-BANK-Q174](questions/bank-101-200.md#ceh13-bank-q174) | FIN versus Xmas | unspecified unusual flag combinations do not uniquely identify FIN rather than Xmas. |
| [CEH13-BANK-Q175](questions/bank-101-200.md#ceh13-bank-q175) | HTTP message boundaries | the stem describes request boundaries but the printed key names response splitting. |
| [CEH13-BANK-Q178](questions/bank-101-200.md#ceh13-bank-q178) | Tautology evidence | the stated single-quote input does not establish tautology-based SQL injection. |
| [CEH13-BANK-Q181](questions/bank-101-200.md#ceh13-bank-q181) | Botnet coordination | option E contains the explanation and printed key is A B C D E; intended answer is C. |
| [CEH13-BANK-Q185](questions/bank-101-200.md#ceh13-bank-q185) | Traffic-analysis limits | changing the cipher to AES alone does not conceal encrypted traffic patterns. |
| [CEH13-BANK-Q200](questions/bank-101-200.md#ceh13-bank-q200) | WPA and WEP distinctions | the generic WPA weak-IV answer appears to mix protocol generations. |
| [CEH13-BANK-Q210](questions/bank-201-300.md#ceh13-bank-q210) | ldapsearch | pasted explanation creates option E and an A B C D E key; intended D. |
| [CEH13-BANK-Q219](questions/bank-201-300.md#ceh13-bank-q219) | Authorized next-step selection | a similar earlier item chooses SQL injection; neither stealth nor mirroring establishes a universal next step. |
| [CEH13-BANK-Q230](questions/bank-201-300.md#ceh13-bank-q230) | Token length versus security | unequal ciphertext lengths do not establish inconsistent encryption strength. |
| [CEH13-BANK-Q251](questions/bank-201-300.md#ceh13-bank-q251) | Reconnaissance controls | explanation is fused into option E and key lists all letters; intended C is a bounded control, not universal scan prevention. |
| [CEH13-BANK-Q255](questions/bank-201-300.md#ceh13-bank-q255) | Discovery flags | these flags do not prove stealth or guarantee that only ICMP was transmitted. |
| [CEH13-BANK-Q257](questions/bank-201-300.md#ceh13-bank-q257) | Rooting claims | the tool name does not establish Android 11 Galaxy Tab S6 exploit support under the stated restrictions. |
| [CEH13-BANK-Q266](questions/bank-201-300.md#ceh13-bank-q266) | Cache inference limits | same overclaim as B036; expiry, ACL and resolver behavior are alternatives. |
| [CEH13-BANK-Q276](questions/bank-201-300.md#ceh13-bank-q276) | Token-validation evidence | a race condition needs timing/state evidence; replay of an acquired valid token remains plausible. |
| [CEH13-BANK-Q282](questions/bank-201-300.md#ceh13-bank-q282) | BLE encryption boundary | Btlejacking is not a substitute for missing encryption key material; device/protocol prerequisites are unspecified. |
| [CEH13-BANK-Q290](questions/bank-201-300.md#ceh13-bank-q290) | IoT update security | the options omit the most precise insecure-update/data-transfer categories; insecure network services is incomplete. |
| [CEH13-BANK-Q294](questions/bank-201-300.md#ceh13-bank-q294) | Backup access and recovery | the 3-2-1 model alone does not prevent attackers altering accessible backup copies. |
| [CEH13-BANK-Q295](questions/bank-201-300.md#ceh13-bank-q295) | Medical-image steganography | the ranking and clinical-image-specific superiority are unsupported. |
| [CEH13-BANK-Q305](questions/bank-301-400.md#ceh13-bank-q305) | CSRF versus hijacking | no specified CSRF or token-control flaw supports the printed session-hijacking answer. |
| [CEH13-BANK-Q308](questions/bank-301-400.md#ceh13-bank-q308) | APT entry evidence | an APT label alone does not make a zero-day the most plausible vector. |
| [CEH13-BANK-Q327](questions/bank-301-400.md#ceh13-bank-q327) | TLS trust compromise | no CA compromise is evidenced or authorized, and no-detection is unsupported. |
| [CEH13-BANK-Q335](questions/bank-301-400.md#ceh13-bank-q335) | TCP sequence observations | key lists all letters and explanation is pasted into E; the wording also leaves TCP sequence versus IPID unclear. |
| [CEH13-BANK-Q337](questions/bank-301-400.md#ceh13-bank-q337) | Exploit feasibility | the source recommends a custom exploit without sufficient technical evidence. |
| [CEH13-BANK-Q338](questions/bank-301-400.md#ceh13-bank-q338) | Non-destructive validation | the printed DROP TABLE choice is destructive and does not include the context needed for valid SQL syntax. |
| [CEH13-BANK-Q345](questions/bank-301-400.md#ceh13-bank-q345) | APT attribution limits | repeats the unsupported APT-implies-zero-day ranking. |
| [CEH13-BANK-Q347](questions/bank-301-400.md#ceh13-bank-q347) | Version versus vulnerability | the printed exploit type is unsupported by the scenario. |
| [CEH13-BANK-Q354](questions/bank-301-400.md#ceh13-bank-q354) | OT covert channels | no hardest-to-detect ranking is demonstrated. |
| [CEH13-BANK-Q358](questions/bank-301-400.md#ceh13-bank-q358) | Independent weakness classes | the printed deserialization key has no supporting object-reconstruction evidence. |
| [CEH13-BANK-Q365](questions/bank-301-400.md#ceh13-bank-q365) | Hidden-service search limits | repeated unsupported dark-web search assumption. |
| [CEH13-BANK-Q366](questions/bank-301-400.md#ceh13-bank-q366) | Race-condition evidence | timing/concurrency evidence is missing. |
| [CEH13-BANK-Q370](questions/bank-301-400.md#ceh13-bank-q370) | Corrupted SQL example | preserve malformed payload; do not memorize or execute it as valid syntax. |
| [CEH13-BANK-Q372](questions/bank-301-400.md#ceh13-bank-q372) | Hoax | pasted explanation creates option E and all-letter key; intended A. |
| [CEH13-BANK-Q376](questions/bank-301-400.md#ceh13-bank-q376) | VLAN boundary | strict segmentation plus an unspecified vulnerability cannot justify universal covert capture. |
| [CEH13-BANK-Q381](questions/bank-301-400.md#ceh13-bank-q381) | Historical web archives | Google's retired cache operator is a stale technique and should not be treated as a current working method. |
| [CEH13-BANK-Q386](questions/bank-301-400.md#ceh13-bank-q386) | Cipher versus metadata | a block-cipher choice alone does not protect traffic patterns; PSA is unexplained. |
| [CEH13-BANK-Q391](questions/bank-301-400.md#ceh13-bank-q391) | Unsupported DoS ranking | no threat model or measurement supports the hardest-to-detect selection. |
| [CEH13-BANK-Q394](questions/bank-301-400.md#ceh13-bank-q394) | Unknown mobile flaws | healthcare context does not establish a universal hardest technique. |
| [CEH13-BANK-Q411](questions/bank-401-500.md#ceh13-bank-q411) | SQL parsing inconsistency | the printed SE+LECT query is not generally valid SQL and does not establish a successful bypass. |
| [CEH13-BANK-Q414](questions/bank-401-500.md#ceh13-bank-q414) | Backup tampering defense | 3-2-1 copy distribution alone does not enforce access or prevent modification. |
| [CEH13-BANK-Q423](questions/bank-401-500.md#ceh13-bank-q423) | Browser compromise | no universally hardest-to-detect session technique follows. |
| [CEH13-BANK-Q436](questions/bank-401-500.md#ceh13-bank-q436) | Unspecified cloud cause | an unknown vulnerability does not establish the cause. |
| [CEH13-BANK-Q439](questions/bank-401-500.md#ceh13-bank-q439) | FIN and NULL ambiguity | no flag detail uniquely selects FIN over NULL. |
| [CEH13-BANK-Q454](questions/bank-401-500.md#ceh13-bank-q454) | Startup mechanism evidence | reboot persistence alone does not uniquely select registry Run keys, which normally act at user logon. |
| [CEH13-BANK-Q467](questions/bank-401-500.md#ceh13-bank-q467) | Vehicle RF evidence | RF jamming monitoring alone neither confirms nor prevents replay/relay. |
| [CEH13-BANK-Q469](questions/bank-401-500.md#ceh13-bank-q469) | Keystroke monitoring command | explanation is fused into E and the printed key lists all letters; intended A. |
| [CEH13-BANK-Q471](questions/bank-401-500.md#ceh13-bank-q471) | SMB null sessions | default Windows servers and no-alert guarantees are unsupported generalizations. |
| [CEH13-BANK-Q481](questions/bank-401-500.md#ceh13-bank-q481) | IP-header covert channels | greatest-challenge ranking lacks evidence. |
| [CEH13-BANK-Q483](questions/bank-401-500.md#ceh13-bank-q483) | WPA3 transition conditions | the source assumes downgrade availability without establishing its preconditions. |
| [CEH13-BANK-Q485](questions/bank-401-500.md#ceh13-bank-q485) | Rooted-device boundary | partial root access to an app is imprecise and MAM alone does not restore device trust. |
| [CEH13-BANK-Q503](questions/bank-501-542.md#ceh13-bank-q503) | AI attribution evidence | the observed behaviors do not prove AI-powered malware. |
| [CEH13-BANK-Q509](questions/bank-501-542.md#ceh13-bank-q509) | Active versus blind hijacking | no inability to observe is stated, so the printed blind answer is unsupported; active is better supported. |
| [CEH13-BANK-Q517](questions/bank-501-542.md#ceh13-bank-q517) | Decoy-service fingerprinting | an additional unlabeled mobile/BYOD question and four options are embedded in this entry; preserve all source text. |
| [CEH13-BANK-Q521](questions/bank-501-542.md#ceh13-bank-q521) | Unsupported exploit recipe | device/build and exploit prerequisites are absent. |
| [CEH13-MOCK01-Q004](questions/mock-01.md#ceh13-mock01-q004) | Sequence-field ambiguity | the same stem has a conflicting malformed bank key/explanation; the generic word sequence does not uniquely establish IPID. |
| [CEH13-MOCK01-Q017](questions/mock-01.md#ceh13-mock01-q017) | Startup mechanism evidence | reboot persistence alone does not uniquely select registry Run keys, which normally act at user logon. |
| [CEH13-MOCK01-Q057](questions/mock-01.md#ceh13-mock01-q057) | Hidden-service search limits | repeated unsupported dark-web search assumption. |
| [CEH13-MOCK01-Q071](questions/mock-01.md#ceh13-mock01-q071) | Email infrastructure evidence | identical stem is keyed to sender IP here and sender mail server in BANK-Q405; the question does not resolve the granularity. |
| [CEH13-MOCK01-Q072](questions/mock-01.md#ceh13-mock01-q072) | Methodology-stage ambiguity | identical stem is keyed to information gathering/detection here and launching injection in BANK-Q398; no stage definition resolves the overlap. |
| [CEH13-MOCK01-Q081](questions/mock-01.md#ceh13-mock01-q081) | Incomplete AXFR command | the printed dig @ axfr lacks a server token and zone name. |
| [CEH13-MOCK01-Q093](questions/mock-01.md#ceh13-mock01-q093) | OS versus service discovery | identical stem is keyed to OS discovery here and service version discovery in BANK-Q232. |
| [CEH13-MOCK01-Q094](questions/mock-01.md#ceh13-mock01-q094) | HTTP message boundaries | the stem describes request boundaries but the printed key names response splitting. |
| [CEH13-MOCK01-Q099](questions/mock-01.md#ceh13-mock01-q099) | Required ICMP errors | blanket type-3 blocking includes fragmentation-needed errors and can break connectivity. |
| [CEH13-MOCK01-Q103](questions/mock-01.md#ceh13-mock01-q103) | Scanner capability confusion | high-speed discovery is not uniquely supported and differs from the bank's near-identical capability key. |
| [CEH13-MOCK01-Q120](questions/mock-01.md#ceh13-mock01-q120) | Root cause versus symptom | this form omits loss of governance from its options and keys the symptom; BANK-Q130 keys the root cause. |
| [CEH13-MOCK01-Q125](questions/mock-01.md#ceh13-mock01-q125) | Nmap MAC spoofing | -sT uses OS connect sockets; the printed command does not establish spoofing of connect traffic. |
| [CEH13-MOCK02-Q002](questions/mock-02.md#ceh13-mock02-q002) | PRINCE versus combinator | the single-list variable-combination description favors PRINCE over the printed Combinator key. |
| [CEH13-MOCK02-Q030](questions/mock-02.md#ceh13-mock02-q030) | HTTP/2 memory growth | normal connection closure and memory growth do not uniquely prove the named RST-specific vulnerability. |
| [CEH13-MOCK02-Q040](questions/mock-02.md#ceh13-mock02-q040) | Active collection ambiguity | no probe type is stated to uniquely establish network/port scanning. |
| [CEH13-MOCK02-Q053](questions/mock-02.md#ceh13-mock02-q053) | Covert-channel attribution | no DNS queries, ports or names are supplied to distinguish the printed DNS key. |
| [CEH13-MOCK02-Q056](questions/mock-02.md#ceh13-mock02-q056) | Global Catalog transport | the keyed option incorrectly labels TCP/UDP 3268; treat UDP as a source error. |
| [CEH13-MOCK02-Q058](questions/mock-02.md#ceh13-mock02-q058) | RootDSE query | ldapsearch -h -x omits the required host value and is not a reusable complete command. |
| [CEH13-MOCK02-Q062](questions/mock-02.md#ceh13-mock02-q062) | EAP versus RADIUS replay | a generic wireless capture does not establish capture or successful replay of RADIUS packets. |
| [CEH13-MOCK02-Q083](questions/mock-02.md#ceh13-mock02-q083) | Website mirroring | the specific behavior fits Website Mirroring more directly than the printed broader Footprinting answer. |
| [CEH13-MOCK02-Q094](questions/mock-02.md#ceh13-mock02-q094) | Search-result phishing | the printed Pharming answer and options omit the precise search-engine mechanism; the key itself acknowledges variant terminology. |
| [CEH13-MOCK02-Q098](questions/mock-02.md#ceh13-mock02-q098) | RF-jammer attribution | no primary product specification verifies the keyed model or performance. |
| [CEH13-MOCK02-Q111](questions/mock-02.md#ceh13-mock02-q111) | Compression side channels | the source's response-compression description conflicts with its CRIME key. |
| [CEH13-MOCK03-Q002](questions/mock-03.md#ceh13-mock03-q002) | Legacy TLS | old TLS does not by itself let a MitM decrypt an arbitrary session. |
| [CEH13-MOCK03-Q007](questions/mock-03.md#ceh13-mock03-q007) | Session attack prerequisites | no evidenced browser flaw or guarantee of undetected takeover supports the marked option. |
| [CEH13-MOCK03-Q011](questions/mock-03.md#ceh13-mock03-q011) | Timing versus policy | the marked timing choice does not itself evade an explicit nonstandard-port block. |
| [CEH13-MOCK03-Q024](questions/mock-03.md#ceh13-mock03-q024) | Redirection evidence | the stem provides no executable browser-context evidence for the marked XSS choice. |
| [CEH13-MOCK03-Q030](questions/mock-03.md#ceh13-mock03-q030) | Inverse-mapping uncertainty | responds to inverse mapping is too vague to justify the marked firewall conclusion. |
| [CEH13-MOCK03-Q118](questions/mock-03.md#ceh13-mock03-q118) | Traceroute probes and replies | the question conflates probe transport with returned ICMP errors; ICMP is not the only traceroute probe protocol. |

## Qualifications and future scoring

All 139 qualified entries retain their specific detail in [items.csv](items.csv) and their question notes. Repeated concerns include unsupported hardest/most-effective rankings, missing attacker position, unknown product/build support, incomplete command syntax, and controls that only address one layer of a larger problem. A qualification does not establish that every other aspect of an item is correct.

| Future trigger | Owner | Required evidence | Record |
| --- | --- | --- | --- |
| Jason chooses a held item for formal practice | Learning owner / item reviewer | Corrected stem/options/key with primary mechanism evidence and version; independent review where needed | New versioned review alongside this audit; preserve original source |
| Jason submits an actual answer | Jason; learning owner records it | Exact answer, exposure/assistance, confidence when required, mode/version and actual time if reported | Existing assessment attempt workflow |
| A current product/version claim affects the chosen concept | Learning owner | Current official implementation documentation for that product/build | Update the specific annotation and its checked date |
| Any public redistribution is proposed | Jason / rights holder as applicable | Appropriate distribution authority and selected content scope | Separate publication decision; source custody alone supplies no publication claim |
