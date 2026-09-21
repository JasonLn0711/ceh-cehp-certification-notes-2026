# M02 — Footprinting and reconnaissance

Reconnaissance turns observations into a bounded account of an environment. Each useful note records where information came from, when it was observed, what it supports, and what remains an inference.

[Week 1 index](README.md) · [Connections](connections.md) · [Complete coverage](coverage.md) · [Source receipt and live checks](../../source/2026-09-20-ceh-week-01/README.md)

Captured 2026-09-20, Asia/Taipei. Detailed sections below reorganize the user-supplied audited study references and retain their wording where precision matters. Linked claim records own status, original line ranges and evidence limits. Newly written synthesis is labeled editorial. These are study notes, not evidence of attendance, personal study completion or executed labs.

## Contents

[Complete plain-English M02 reading](plain-english/m02-reconnaissance.md) connects collection boundaries, tools, DNS, paths, email and lab interfaces to these audited details.

[中文講義二 §11–19](handouts-zh/part-02.md#h2-11) provides the complete teaching sequence for collection, search, OSINT, Tor, DNS, paths, email, human factors and lab interfaces, with explicit links back to this audit layer.

- [Reconnaissance and evidence quality](#collection-boundary)
- [Search operators, GHDB and Shodan](#search-tools)
- [DNS, archives, registration and historical clues](#dns-and-history)
- [Tor, dark-web assertions and Bitcoin](#tor-and-bitcoin)
- [Competitive intelligence and research tools](#competitive-intelligence)
- [Traceroute, CDN and TTL](#paths-and-ttl)
- [Email headers, human factors and countermeasures](#email-and-human-factors)
- [From a collected clue to a defensible statement](#observation-matrix)

<a id="collection-boundary"></a>
## Reconnaissance and evidence quality

*Source-derived: part 02, M02.1; qualifications retained.*

**Transcript coverage:** T002:L744–L865 (01:34:09–01:46:26). **Audit records:** [P2-C061](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C061) [P2-C062](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C062) [P2-C063](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C063) [P2-C064](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C064) [P2-C065](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C065) [P2-C066](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C066) [P2-C067](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C067) [P2-C068](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C068) [P2-C069](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C069) [P2-C070](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C070).

The course uses **footprinting and reconnaissance** for collecting information about an organization and its environment. They overlap in this context without becoming universally identical terms. Its information categories include organization, employees, locations, domains, IP ranges, hosting and system clues.

**Editorial workflow:** define scope → collect permitted information → record its source and observation time → distinguish observed facts from hypotheses → identify what evidence would test each hypothesis. A company name in a job advertisement or an email local part does not prove a deployed product, an AD account or a measured probability.

**Passive/active distinction:** viewing an existing third-party record may avoid new probing. A request that causes a tool, service or proxy to interact with a target remains target interaction; outsourcing the request does not make it unobservable or automatically passive. The active-scanning concept does not require a completed TCP session. [P2-S001](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S001)

The authority-pressure phone call is a classroom social-engineering illustration, not a permitted exercise on real coworkers. Its success rate and occupational stereotypes are unsupported. No credential-harvesting script is reproduced.

<a id="search-tools"></a>
## Search operators, GHDB and Shodan

*Source-derived: part 02, M02.2; qualifications retained.*

**Transcript coverage:** T002:L866–L995 (01:46:37–02:01:26). **Audit records:** [P2-C071](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C071) [P2-C072](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C072) [P2-C073](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C073) [P2-C074](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C074) [P2-C075](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C075) [P2-C076](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C076) [P2-C077](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C077) [P2-C078](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C078) [P2-C079](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C079) [P2-C080](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C080) [P2-C081](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C081).

Google search operators such as **site:** and **filetype:** can narrow a query. Results are an index view, not a complete current inventory. The harmless expression `site:example.org filetype:pdf` illustrates syntax; it does not represent a performed search of the learner’s systems. [P2-S026](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S026) [P2-S027](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S027)

**Google Hacking Database (GHDB)** is a third-party collection of search examples, not Google’s own product. **Shodan** indexes information about Internet-connected services/devices. A returned record is not proof of current vulnerability or permission to access the endpoint. [P2-S028](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S028) [P2-S029](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S029)

The lecture’s alleged backup downloads and camera views are not independently replayed. No backups, private feeds or intimate images were accessed. An exposed URL or absent password does not establish that material was intentionally published for unrestricted use. These cases are retained as data-exposure risks, not actionable directions to collect or exploit private material.

Search-engine superiority, the 40% submarine-cable statistic and capacity rankings lack the required data and definitions. They do not become verified merely because the vendor operates a large network.

<a id="dns-and-history"></a>
## DNS, archives, registration and historical clues

*Source-derived: part 02, M02.3; qualifications retained.*

**Transcript coverage:** T002:L996–L1059 (02:01:28–02:07:47). **Audit records:** [P2-C082](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C082) [P2-C083](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C083) [P2-C084](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C084) [P2-C085](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C085) [P2-C086](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C086) [P2-C087](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C087).

**DNSDumpster** assembles domain-related observations and relationships. Such data does not reveal every DNS record or establish the actual packet path through an organization. Provider labels are evidence of a relationship, not a complete enterprise network diagram. [P2-S030](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S030)

**Wayback Machine** supplies archived captures. Its calendar timestamps refer to captures, not necessarily the instant a website changed. Missing captures do not prove no site existed; a capture is not a complete immutable history of every page. A changed footer is insufficient to prove a corporate acquisition or its motive. [P2-S031](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S031)

The lecture’s UUU/SYSTEX/Taiwan Mobile ownership narrative remains unverified. Job advertisements can suggest skills sought, including customer-project requirements, but do not establish an exhaustive inventory of internal equipment.

**Related later DNS material:** forward lookup can return address records; reverse DNS uses separately managed PTR information and need not be an exact inverse. A record is not a certificate of machine ownership or physical location. **WHOIS** and **RDAP** concern registration data, not an unrestricted list of personal contacts. ICANN’s January 2025 gTLD changes do not mean every WHOIS service worldwide ceased, especially across ccTLD arrangements. [P2-S038](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S038) [P2-S037](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S037)

<a id="tor-and-bitcoin"></a>
## Tor, dark-web assertions and Bitcoin

*Source-derived: part 02, M02.4; qualifications retained.*

**Transcript coverage:** T002:L1060–L1126 (02:07:50–02:14:05). **Audit records:** [P2-C088](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C088) [P2-C089](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C089) [P2-C090](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C090) [P2-C091](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C091) [P2-C092](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C092).

**Tor Browser** uses the Tor network; describing its relays as a collection of ordinary VPN servers is inaccurate. For ordinary websites, a visible source address can be an exit relay’s address. Onion services use a different connection arrangement and are not ordinary sites reached through an exit. A Tor start page or a default search engine is not a comprehensive dark-web database. [P2-S032](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S032) [P2-S034](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S034)

**Bitcoin privacy:** its public transaction history prevents equating decentralization with guaranteed anonymity or untraceability. That does not establish the identity behind every address, the proportion of criminal transactions, or the lecturer’s value judgment about the technology. [P2-S035](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S035)

The alleged sale of a Taiwanese population dataset is not verified: the recording gives no reliable named listing, date or authenticated dataset. No market was accessed and no personal-data collection was performed. The garbled IP-check result cannot establish the actual classroom address.

<a id="competitive-intelligence"></a>
## Competitive intelligence and research tools

*Source-derived: part 02, M02.5; qualifications retained.*

**Transcript coverage:** T002:L1127–L1228 (02:14:09–02:23:41). **Audit records:** [P2-C093](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C093) [P2-C094](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C094) [P2-C095](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C095) [P2-C096](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C096) [P2-C097](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C097) [P2-C098](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C098) [P2-C099](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C099) [P2-C100](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C100) [P2-C101](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C101) [P2-C102](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C102) [P2-C103](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C103).

**Competitive intelligence** can use legitimate public information about competitors. It is not equivalent to industrial espionage. A patent grants defined exclusionary rights; a filing or publication is not proof that a corresponding product is about to launch. Photographic lighting does not prove that an interview was purchased or determine its price. [P2-S075](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S075)

**theHarvester** is an information-collection tool. The lecture’s domain/search, source and result-limit options must be checked against the installed version. Provider availability changes; the specific historical LinkedIn/Baidu workflow is not demonstrated by the current README alone. Do not reconstruct the incomplete classroom command as known-good current syntax. [P2-S036](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S036)

Other briefly named tools and an unclear service remain qualified ASR readings. **OSINT Framework**, discussed later, is a directory of resources, not a promise that every linked tool is free or open-source software. “Open source” in OSINT refers to information sources and is not a universal software license claim. [P2-S044](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S044)

<a id="paths-and-ttl"></a>
## Traceroute, CDN and TTL

*Source-derived: part 02, M02.6; qualifications retained.*

**Transcript coverage:** T002:L1229–L1313 (02:23:48–02:32:42). **Audit records:** [P2-C104](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C104) [P2-C105](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C105) [P2-C106](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C106) [P2-C107](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C107) [P2-C108](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C108) [P2-C109](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C109) [P2-C110](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C110).

**Traceroute/tracert** uses network responses to expose aspects of a route. Missing replies, changing paths and intermediary behavior limit what a trace proves. The Windows name is `tracert`; platform behavior is not identical just because the broad goal is similar. [P2-S039](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S039)

A **content delivery network (CDN)** is a distributed delivery architecture, not just a private high-speed cable replacing the Internet. An edge response or provider hostname need not identify the origin application’s OS or ownership. The reviewed Azure Front Door documentation describes Microsoft’s own CDN/edge capability; it does not rank cloud bandwidth. [P2-S041](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S041)

**TTL** is a packet lifetime/hop-limiting field. Linux documents a configurable default of 64; Windows also exposes configurable TTL behavior. Treat the course’s 64/128 pairing as a common heuristic, not a unique signature. Adding a forward traceroute’s hop count to an echo reply’s remaining TTL does not recover an initial value reliably when the reply path can differ. [P2-S053](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S053) [P2-S070](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S070) [P2-S071](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S071)

The arithmetic 58 + 6 = 64 is correct; the inference “therefore Microsoft’s web server runs Linux” is not established. A dated Meta outage source from October 2021 is not evidence that it is the incident meant by “last October.”

<a id="email-and-human-factors"></a>
## Email headers, human factors and countermeasures

*Source-derived: part 02, M02.7; qualifications retained.*

**Transcript coverage:** T002:L1314–L1529 (02:32:51–02:55:38). **Audit records:** [P2-C111](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C111) [P2-C112](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C112) [P2-C113](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C113) [P2-C114](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C114) [P2-C115](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C115) [P2-C116](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C116) [P2-C117](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C117) [P2-C118](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C118) [P2-C119](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C119) [P2-C120](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C120) [P2-C121](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C121) [P2-C122](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C122) [P2-C123](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C123) [P2-C124](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C124) [P2-C125](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C125) [P2-C126](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C126) [P2-C127](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C127) [P2-C128](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C128).

**Email trace information** can provide evidence about relays. SMTP servers add Received fields, but not every supplied field is trustworthy and not every internal service is exposed. Hidden journaling, internal routing or fabricated earlier headers prevent a claim that any message reveals the sender’s entire enterprise topology. Preserve the original message and evaluate each trust boundary. [P2-S043](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S043)

The lecture’s social-engineering vocabulary includes **eavesdropping** (overhearing), **shoulder surfing** (observing input/screens), **dumpster diving** (examining discarded material), and **impersonation** (claiming another identity). The taxonomy mixes methods of information access and deception. Respectful incident reporting is professional guidance; appearance, geography mistakes and a conversation’s emotional effect are not reliable standalone tests of whether someone is a bot or a criminal.

**Countermeasure scope:** publish usable policies, maintain awareness and reduce unnecessary exposure. Blanket social-network bans do not remove already-public information. A first-party account of partner-shared off-platform activity supports that mechanism, not a claim that every in-app session steals all credentials or that 99% of advertisements are fraudulent. [P2-S045](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S045)

**Directory listing** can reveal files unintentionally, but deliberately public indexes also exist. Restrict sensitive content itself; disabling an index does not prevent access to a known URL. Defaults depend on the server and configuration. [P2-S047](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S047) [P2-S048](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S048)

<a id="observation-matrix"></a>
## From a collected clue to a defensible statement

*Editorial synthesis of the audited reconnaissance claims above.* Record a clue with its source, collection time and actual subject. Then separate the observation from its interpretation. The distinction matters because an archive, DNS answer, service index and job advertisement describe different things.

| Clue | Supported starting statement | Additional claim requiring evidence |
| --- | --- | --- |
| An archived page at a capture timestamp | The archive presents a captured representation | The organization's founding date, exact original publication date or present deployment |
| An A or AAAA record | DNS supplied an address for the queried name under the observed conditions | That address is the private origin, physical office or sole owned host |
| An MX record | DNS identifies mail-exchange information | The complete internal email topology |
| An RDAP result | A registry/registrar supplies scoped registration data | Every real operator's identity or permission to test the resource |
| A Shodan or DNSDumpster record | A third-party source associates information with infrastructure | A complete current inventory or authenticated live output |
| A job advertisement naming a technology | The advertisement asks for that skill | The employer necessarily deploys it internally today |
| A TTL or trace response | A responder/path produced those observed values | A definitive operating system, return path or physical location |
| A social-media profile or username | A source presents that identifier or claim | An authenticated person, AD account or authorized recipient |

The [coursework DNS lab](../../../nycu_114-2_network_security_practices/labs/dns-reconnaissance/README.md) already uses the useful pattern: record each answer, explain its narrow implication, and identify its limits. Existing M02 questions and the CEHP DNS-dependency task can reuse that reasoning within their own permitted scope.

## Distinguish passive attacks from passive-source research

Part 01 discusses passive and active **attacks**; Part 02 discusses **collection activity**. Keep the context explicit. Observing existing third-party data is different from initiating target contact, including contact initiated through a service or proxy. Conversely, an ordinary authorized connection is not automatically a malicious attack. These distinctions reconcile the apparent shorthand across the recordings. See [part 01 attack categories](m01-foundations.md#attack-categories) and [collection boundary](#collection-boundary).

## Useful countermeasure questions

The defender's questions are which information is intentionally public, which record is stale, which service or document is exposed unintentionally, and who owns correction. Removing a directory index addresses listing behavior; the file itself still needs appropriate access control. Staff need understandable disclosure and escalation procedures. No searches for exposed private material, account enumeration, impersonation or target requests were performed in this capture.
