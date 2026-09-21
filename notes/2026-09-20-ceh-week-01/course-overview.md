# Course overview, resources and terminology

Use the lecture overview to locate a topic in the twenty-module course, distinguish official exam information from provider arrangements, and recover technical vocabulary from ASR. Detailed instruction in these files covers M01–M03; previews of the other modules remain previews.

[Week 1 index](README.md) · [Connections](connections.md) · [Complete coverage](coverage.md) · [Source receipt and live checks](../../source/2026-09-20-ceh-week-01/README.md)

Captured 2026-09-20, Asia/Taipei. Detailed sections below reorganize the user-supplied audited study references and retain their wording where precision matters. Linked claim records own status, original line ranges and evidence limits. Newly written synthesis is labeled editorial. These are study notes, not evidence of attendance, personal study completion or executed labs.

## Contents

[中文講義一 §1–3](handouts-zh/part-01.md#h1-01) connects the introductory vocabulary, all twenty module previews, VM roles and exam distinctions. [中文逐節索引](handouts-zh/README.md) preserves the full handout structure.

- [Course purpose, materials and boundaries](#course-purpose)
- [Assessment concepts and the course sequence](#assessment-sequence)
- [Labs and virtualization](#virtualization)
- [Exam facts and preparation advice](#exam-guidance)
- [Compact study workflow — editorial addition](#study-workflow)
- [Separate connection instructions from authority](#classroom-access)
- [Twenty-module overview and depth boundary](#module-map)
- [Contextual terminology — part 01](#glossary-part-01)
- [Contextual terminology — part 02](#glossary-part-02)
- [What part 02 clarifies and what remains open](#cross-recording-resolution)

<a id="course-purpose"></a>
## Course purpose, materials and boundaries

*Source-derived: part 01, 2.1; qualifications retained.*

CEH expands to **Certified Ethical Hacker** and is an EC-Council program. The uploaded lecture identifies its textbook as **v13** and previews twenty modules. Its claims about the particular book’s page count, how much content is intended for classroom explanation, and next-week registration are not independently established by a public syllabus. Accreditation of a certification program must not be expanded into universal recognition by governments or guaranteed credit for mandatory training. [S001](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S001) [S002](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S002) [S003](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S003)

The key technical purpose is to understand and assess weaknesses within authorization. Learning an attacker’s methods is not permission to apply them to arbitrary systems. The instructor’s repeated warning against relying on good intentions is useful, but moral labels such as “all hackers are bad” and legal conclusions such as “every network connection is criminal” are not interchangeable with a precise scope or statutory test. [S002](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S002) [S044](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S044) [S045](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S045)

**Transcript:** T001:L25–L68; L1111–L1127; L1361–L1397. **Audit:** [C003](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C003) [C004](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C004) [C005](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C005) [C006](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C006) [C007](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C007) [C008](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C008) [C009](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C009) [C114](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C114).

<a id="assessment-sequence"></a>
## Assessment concepts and the course sequence

*Source-derived: part 01, 2.2; qualifications retained.*

The lecture’s introductory sequence can be read as **learn about the environment → discover exposed services → enumerate available details → assess candidate weaknesses → validate permitted findings**. This is a useful teaching path, not a law governing every attacker. MITRE ATT&CK explicitly treats its tactical goals as unordered; not every intrusion includes every goal. [S052](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S052)

A host-discovery probe reports whether it received a response through a particular network path. No response is not proof that a host is switched off. An open port concerns a listening service and reachability; a filtered port is a different observation. Similarly, a product-version match is a lead for vulnerability analysis, not conclusive proof that the specific host is exploitable. [S034](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S034) [S035](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S035) [S022](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S022)

A **vulnerability** is a weakness; an **exploit** takes advantage of a weakness; a **compromise** is a loss of security or trust. Compromise does not require an attacker first to turn off antivirus or a firewall. Configuration, design, identity and procedural weaknesses can remain even when all available patches are installed. [S022](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S022) [S023](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S023) [S028](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S028)

**Lecture examples retained:** reconnaissance is compared with examining a property before a burglary; application input is illustrated by an integer-only quantity field receiving `10000.01`; an unrequested update is illustrated by a reboot that interrupts production. These are explanatory scenarios, not documented incidents or universally inevitable outcomes. See [C025](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C025) and [C115](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C115).

<a id="virtualization"></a>
## Labs and virtualization

*Source-derived: part 01, 2.3; qualifications retained.*

The provider’s classroom environment and the learner’s purchased online-lab entitlement are separate matters. The official CEH page advertises six months of lab access in relevant offerings; it does not prove this individual account’s activation or expiry date. Confirm the entitlement in the provider’s own registration details. [S001](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S001)

The November 11, 2024 announcement made VMware Workstation and Fusion free for all stated use categories. This verifies the licensing announcement, **not** the assertion that VMware always has the best speed, stability or memory use. [S006](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S006)

The garbled “para/parent virtual machine” passage most likely means **Parrot OS running inside a VM**. Parrot and Kali are security-oriented Linux distributions; Parrot is not the technical concept of paravirtualization and not merely a fixed one-fifth-size Kali. Edition, image and installed packages matter. A VM is the virtual computer; the distribution is the operating system installed in it. [S007](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S007) [S008](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S008) [S009](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S009)

The lecture’s Windows 11, Windows Server 2019/2022, FTP/web, DNS/domain-controller and possible SMTP roles are only partly recoverable. The whiteboard is missing. Consequently, **no exact topology, IP plan, service-to-machine assignment, nested-VM requirement or production-ready domain design is reconstructed**. Combining server roles to save RAM is preserved as a classroom suggestion, not a universal deployment recommendation. See [C044](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C044) and [C045](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C045).

**Editorial study boundary:** use the actual lab manual to reproduce the class environment; keep exercises within authorized lab systems. This document is not a replacement installation guide.

<a id="exam-guidance"></a>
## Exam facts and preparation advice

*Source-derived: part 01, 2.4; qualifications retained.*

For the CEH knowledge exam, the official certification page lists **312-50**, **125 multiple-choice questions**, and **four hours**. It describes form-dependent cut scores of **60%–85%**, not the lecture’s 65%–75% range or a universal 75% pass threshold. “Multiple choice” should not be embellished into a guarantee about every future item’s single-answer format. [S002](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S002)

The claim that candidates must deliberately remain for over an hour to avoid an audit is not an official rule established by the reviewed exam-security policy. Its documented review mechanisms do not make exam duration a reliable safe-harbor promise. Follow exam instructions and any actual review notice rather than trying to manipulate presumed screening thresholds. [S004](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S004)

The lecture names ExamTopics and Udemy, but the exact course listing and the provenance of individual questions are not established. A high vote count or rating is not proof that an answer is correct. Distinguish legitimate authored practice from confidential exam content; the certification agreement restricts disclosure of exam materials. [S005](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S005)

Udemy’s refund rules are conditional. Completing or substantially consuming a course can affect eligibility, and refunds do not universally become immediate account credits. Do not follow the lecture’s suggestion to finish the material and assume an unconditional refund. [S010](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S010) [S011](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S011)

**Historical cipher example:** the question’s 64-bit blocks and three 56-effective-bit DES keys identify three-key TDEA/Triple DES. That identification is separate from a deployment recommendation: NIST withdrew SP 800-67 Rev.2 effective January 1, 2024; legacy handling should not be confused with approval for new encryption. [S029](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S029) [S030](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S030)

**Transcript:** T001:L430–L519. **Key claims:** [C046](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C046) [C048](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C048) [C050](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C050) [C052](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C052) [C054](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C054) [C055](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C055) [C056](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C056) [C058](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C058) [C059](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C059).

<a id="study-workflow"></a>
## Compact study workflow — editorial addition

*Source-derived: part 01, 2.12; qualifications retained.*

Read the five security properties and test each against the email or firewall example. Then distinguish vulnerability, exploit, compromise, active/passive behavior, and the three TTP levels. Finally, rehearse the consultant scenario: state exactly what permission covers and which changes require approval. A useful finished note explains the concept, gives a bounded example, names a failure mode, and points to an evidence source. This workflow is newly organized from the lesson; it was not a sequence dictated in the transcript.

<a id="classroom-access"></a>
## Separate connection instructions from authority

*Source-derived: part 02, Lab setup; qualifications retained.*

**Transcript coverage:** T002:L1530–L1593 (02:55:42–03:07:03). **Audit records:** [P2-C129](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C129) [P2-C130](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C130) [P2-C131](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C131) [P2-C132](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C132).

The transcript clearly restates four VM roles: **Parrot, Windows Server 2019, Windows Server 2022 and Windows 11**. It directs students to a provider-specific RDP endpoint and a desktop PDF for credentials. These are classroom arrangements, not independently verified access entitlements or instructions for an agent to connect.

Microsoft documents **mstsc** and host/port syntax. The actual endpoint, assigned port, logins and validity window must come from the provider. The referenced credential PDF and whiteboard were not uploaded, so they are not reconstructed. [P2-S049](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S049)

**Privacy boundary:** the Markdown and default ingestion records omit reusable classroom credentials. The optional provenance archive contains the unchanged original transcript in an explicitly sensitive folder; do not publish or automatically index it.

<a id="module-map"></a>
## Twenty-module overview and depth boundary


Canonical titles follow the official outline [S001](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S001). Descriptions are concise, qualified restatements of what this upload previews. **Only Module 1 has a substantial lesson in this file.**

| Module | Canonical title / Chinese label | Transcript overview | What this upload supports |
|---:|---|---|---|
| 01 | **Introduction to Ethical Hacking** / 道德駭客與資安基本概念 | `T001:L69–L70` | Main detailed lesson begins at L535; authorization, properties, threats, actor terminology and AI. |
| 02 | **Footprinting and Reconnaissance** / 足跡蒐集與偵察 | `T001:L71–L92` | Collect information and context about a target. |
| 03 | **Scanning Networks** / 網路掃描 | `T001:L92–L98` | Assess reachable hosts, ports and services; silence is not proof of power-off. |
| 04 | **Enumeration** / 列舉 | `T001:L99–L101` | Obtain available details about services, accounts and resources. |
| 05 | **Vulnerability Analysis** / 弱點分析 | `T001:L101–L105` | Identify candidate weaknesses and assess applicability. |
| 06 | **System Hacking** / 系統入侵測試 | `T001:L106–L107` | Understand exploitation and impact within authorization. |
| 07 | **Malware Threats** / 惡意軟體威脅 | `T001:L108–L116` | Understand malicious software and delivery scenarios. |
| 08 | **Sniffing** / 封包嗅探 | `T001:L117–L119` | Observe network traffic; protected content is not automatically readable. |
| 09 | **Social Engineering** / 社交工程 | `T001:L119–L124` | Understand manipulation of people and processes. |
| 10 | **Denial-of-Service** / 阻斷服務 | `T001:L125–L135` | Understand loss of access, not just machine crashes. |
| 11 | **Session Hijacking** / 工作階段劫持 | `T001:L136–L141` | Distinguish session takeover from other credential attacks. |
| 12 | **Evading IDS, Firewalls, and Honeypots** / 規避入侵偵測、防火牆與誘捕系統 | `T001:L142–L146` | Overview of adversary interaction with defensive controls. |
| 13 | **Hacking Web Servers** / 網頁伺服器安全測試 | `T001:L147–L150` | Server software, deployment and configuration exposure. |
| 14 | **Hacking Web Applications** / 網頁應用程式安全測試 | `T001:L151–L190` | Application logic, validation and authorization weaknesses. |
| 15 | **SQL Injection** / SQL 注入 | `T001:L191–L197` | Untrusted input changes the interpretation of database queries. |
| 16 | **Hacking Wireless Networks** / 無線網路安全測試 | `T001:L198–L222` | Standards, authentication and encryption choices; exact vulnerable schemes are not taught here. |
| 17 | **Hacking Mobile Platforms** / 行動平台安全測試 | `T001:L223–L226` | Android and iOS security topics are previewed. |
| 18 | **IoT and OT Hacking** / 物聯網與營運技術安全測試 | `T001:L227–L232` | IoT, operational technology and industrial control concerns. |
| 19 | **Cloud Computing** / 雲端運算 | `T001:L232–L235` | Cloud concepts and characteristics are previewed, not fully explained. |
| 20 | **Cryptography** / 密碼學 | `T001:L235–L286` | Cryptographic use and trade-offs; the later TDEA example is historical. |

<a id="glossary-part-01"></a>
## Contextual terminology — part 01


These are contextual normalizations, not evidence that the original speaker pronounced an incorrect word. Never run this table as an unconditional global replacement. Low-confidence entries remain unresolved; only audio/slides can close those gaps.

| ID | Observed ASR form | Normalized reading | Original lines | Confidence | Limitation |
|---|---|---|---|---|---|
| G001 | SMB, in the expansion subject matter expert | SME — subject matter expert | `T001:L58–L59` | high | The acronym is normalized; the audio itself was not supplied. |
| G002 | Full printing / full printing | Footprinting | `T001:L71–L92` | high | Course module context. |
| G003 | module eight sleeping | Sniffing — 封包擷取／嗅探 | `T001:L117–L119` | high | The eighth official module and surrounding packet discussion agree. |
| G004 | 風暴 / 風包, when referring to network traffic | 封包 — packet | `T001:L117–L119` | high | Contextual only; never replace these strings everywhere. |
| G005 | ideas, in the module 12 name | IDS — Intrusion Detection System | `T001:L142–L146` | high | Canonical course module title. |
| G006 | iOS, in a list of web-server products | IIS — Internet Information Services | `T001:L147–L150` | medium | A contextual reconstruction, not an audio-confirmed product name. |
| G007 | apachenginx | Apache; nginx | `T001:L147–L150` | high | Separate the recognizable product names. |
| G008 | 自然 / 治安, in information-security explanations | 資安 — information security | `T001:L154–L167` | high | Do not apply outside a clearly technical security context. |
| G009 | OS, paired with Android | iOS | `T001:L223–L226` | high | Mobile-platform context; not the web-server IIS occurrence. |
| G010 | ut, paired with IoT | OT — operational technology | `T001:L227–L231` | high | ICS discussion supports the normalization. |
| G011 | be aware / be aware station | VMware / VMware Workstation | `T001:L353–L376` | high | VMware is also explicitly transcribed at line 363. |
| G012 | para / parent / parameter virtual machine | Parrot OS running as a VM | `T001:L378–L400` | medium | Context and comparison with Kali support this; do not interpret as paravirtualization. |
| G013 | SMTG server | Possibly SMTP server | `T001:L410–L411` | low | Do not assign it to an exact VM or reconstruct installation steps. |
| G014 | DNS 遊戲 / your main controller | Possibly DNS service / domain controller | `T001:L412–L414` | medium | Roles are partly intelligible, but the whiteboard topology is unavailable. |
| G015 | 31250 | 312-50 | `T001:L430–L437` | high | Official CEH knowledge-exam identifier. |
| G016 | gene, in the cipher question | key | `T001:L474–L475` | high | Three 56-bit keys and 64-bit blocks identify the historical TDEA example. |
| G017 | non-recognition | non-repudiation — 不可否認性 | `T001:L606–L610` | high | Canonical property and surrounding discussion. |
| G018 | closing attack / lousy | close-in attack — 近距離／實體接近攻擊 | `T001:L949–L968` | high | Physical-proximity context. |
| G019 | sigmoid injection | SQL injection | `T001:L943–L948` | high | Attack-example context. |
| G020 | inherent translated as 繼承 | inherent — 固有的 | `T001:L886–L891` | high | This is a translation/concept correction, not proof of the original speech. |
| G021 | control bias / comfort, in the security-control passage | compromise — 安全遭破壞／失陷 | `T001:L1058–L1080` | high | Keep the broader security meaning, not ordinary-language 妥協 alone. |
| G022 | script keyning / 腳本小字 | script kiddie — 腳本小子 | `T001:L1128–L1136` | high | Informal actor label; not a diagnosis or legal category. |
| G023 | 白貓 / 黑貓, in actor labels | white hat / black hat — 白帽／黑帽 | `T001:L1140–L1148` | high | Contextual normalization. |
| G024 | greyhead | gray hat / grey hat — 灰帽 | `T001:L1149–L1152` | high | Both English spellings occur in use; not a legal category. |
| G025 | state sponsor hacker | state-sponsored hacker | `T001:L1219–L1224` | high | Standard adjective form; sponsorship of any specific actor still needs evidence. |
| G026 | 零金計劃 / 臨境計劃 | PRISM — 稜鏡計畫 | `T001:L1224–L1267` | medium | Snowden/NSA context supports the identity; the lecture’s description of its scope is corrected separately. |
| G027 | Boris / bias / files, in the firmware-password story | BIOS | `T001:L1249–L1265` | high | Do not retain the alleged universal bypass sequence as valid instructions. |
| G028 | scope and imitation | scope and limitations | `T001:L1398–L1432` | high | The later limitation examples clarify the intended expression. |
| G029 | check the GPT | ChatGPT | `T001:L1522–L1537` | high | Product-name normalization; no claim about a particular model version. |
| G030 | Shell GPT | ShellGPT; project TheR1D/shell_gpt | `T001:L1541–L1544` | high | Separate the third-party project from OpenAI API services. |
| G031 | nvdm driver | Unresolved driver name | `T001:L112–L113` | low | Do not silently assert a vendor or package. |
| G032 | m map followed by garbled flags | Nmap-like reference; exact command unresolved | `T001:L1513–L1514` | low | No executable reconstruction, guessed flags or claimed output. |
| G033 | IHC-like credential acronym | Unresolved credential acronym | `T001:L1439–L1455` | low | Do not silently substitute CEH, CHFI or another credential. |
| G034 | Garbled attack-success equation | Exact slide formula unresolved | `T001:L724–L763` | low | Motive, method and vulnerability are discussed; the equation itself is not recoverable. |

<a id="glossary-part-02"></a>
## Contextual terminology — part 02


Do not apply this table as unconditional global replacement. Confidence reflects a contextual reading; audio, slides or exact tool output are needed to resolve remaining uncertainty. A conceptual correction is labeled as such and is not blamed automatically on the ASR engine.

| ID | Observed form | Normalized interpretation | Original lines | Confidence / limitation |
|---|---|---|---|---|
| P2-G001 | 特洛伊步吧 / 特多移入碼 | Trojan / Trojan horse — 特洛伊木馬 | T002:L18–L28 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G002 | Mitre ATT and CK | MITRE ATT&CK | T002:L37–L51 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G003 | victor / 受害的足跡 | victim — 受害者／受害實體 | T002:L62–L65 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G004 | IAIA | IA — Information Assurance — 資訊保證 | T002:L135–L149 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G005 | continue adaptive security strategy | continuous adaptive security strategy | T002:L150–L161 | medium: The slide’s exact title and provenance are not available. |
| P2-G006 | 眾生法律 / 眾生防禦 | defense in depth — 縱深防禦 | T002:L151–L266 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G007 | instant response | incident response — 事件應變 | T002:L155–L157 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G008 | memory 磁碑 | Storage/disk reference; exact term unresolved | T002:L174–L174 | low: Do not infer an NVMe model or storage technology. |
| P2-G009 | 群件 / 全線管制 | permissions / access controls — 權限／存取控制 | T002:L205–L240 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G010 | main trap / main traffic gate | mantrap / access-control vestibule | T002:L249–L258 | medium: Physical design must also meet applicable life-safety requirements. |
| P2-G011 | 風險就是已知問題不改善 | Risk — 風險; the definition requires correction, not mere transcription repair | T002:L267–L303 | high: Risk is not probability alone or limited to known uncorrected flaws. |
| P2-G012 | soak / SOC ASTEP | SOC / SOC staff | T002:L374–L381 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G013 | cv 編號 | CVE identifier | T002:L379–L381 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G014 | Thread modeling | Threat modeling — 威脅建模 | T002:L390–L428 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G015 | Design the decompose deep application | decompose the application | T002:L397–L425 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G016 | formal ability handling | vulnerability handling | T002:L429–L432 | medium: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G017 | artific handle / RT Sector / 二級匪 | artifact handling / artifacts — 跡證與分析材料 | T002:L433–L450 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G018 | Instagram handle | incident handling | T002:L498–L501 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G019 | PCIe 的程式 | PCI DSS — Payment Card Industry Data Security Standard | T002:L569–L591 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G020 | 主導集合員 | lead auditor — 主導稽核員 | T002:L619–L620 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G021 | miss / list / network 標準 | NIST, in contrast with ISO | T002:L625–L638 | medium: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G022 | socks / soft-as-ox.net / 殺兵法案 | SOX — Sarbanes–Oxley Act | T002:L685–L700 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G023 | 數位遷徙年版權法案 | Digital Millennium Copyright Act — 數位千禧年著作權法 | T002:L701–L708 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G024 | GDP, in the privacy-law section | GDPR — General Data Protection Regulation | T002:L709–L733 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G025 | full printing / food printing | footprinting — 足跡蒐集 | T002:L745–L865 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G026 | D 端 / 定端 | on-premises — 地端 | T002:L834–L841 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G027 | web 是 iOS | IIS, probably, in the web-server context | T002:L770–L770 | medium: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G028 | sight / search algorithm, in filtering context | site: / search operator | T002:L902–L925 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G029 | file type pdf | filetype:pdf | T002:L917–L925 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G030 | google hanging database | Google Hacking Database — GHDB | T002:L927–L957 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G031 | shielded / student / Sheldon | Shodan | T002:L958–L995 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G032 | DNS dumpster | DNSDumpster | T002:L996–L1013 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G033 | 時光回溯機 | Wayback Machine — 網頁歷史存檔服務 | T002:L1014–L1032 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G034 | 很易 / 橫溢 / 恆意 | UUU training provider name; do not normalize each occurrence globally | T002:L999–L1051 | medium: Corporate ownership claims need their own evidence. |
| P2-G035 | Tool / TOL / code / Toast browser | Tor Browser | T002:L1092–L1126 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G036 | VPN server, while describing Tor | Tor relay; an architectural correction rather than an ASR-only repair | T002:L1103–L1124 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G037 | dot dot go | DuckDuckGo | T002:L1108–L1108 | medium: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G038 | Pattern / 傳遞, in patent discussion | patent — 專利 | T002:L1178–L1183 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G039 | parent / paravirtual machine | Parrot OS VM | T002:L1191–L1200 | high: Not the hypervisor concept of paravirtualization. |
| P2-G040 | the harvesterthe harvester | theHarvester | T002:L1194–L1202 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G041 | 巴斯數碼 | Unresolved search-service name | T002:L1203–L1204 | low: Do not guess a provider from the sound. |
| P2-G042 | who is / cold daddy | WHOIS / GoDaddy | T002:L1205–L1214 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G043 | pin 減號 a | Windows ping -a | T002:L1222–L1227 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G044 | trees RT | Windows tracert | T002:L1229–L1237 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G045 | Akman / ArcMod | Akamai | T002:L1254–L1261 | medium: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G046 | AWS class | Possibly Amazon CloudFront | T002:L1257–L1259 | medium: Contextual provider-name reconstruction, not verified classroom network routing. |
| P2-G047 | output, in mail-client discussion | Outlook | T002:L1315–L1317 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G048 | tool / top 圖, in mail-routing discussion | topology / mail-flow diagram | T002:L1338–L1346 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G049 | shooter surfing / sugar surfing | shoulder surfing — 窺視輸入或螢幕 | T002:L1452–L1458 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G050 | multi-go / record ng / Folka | Possibly Maltego / Recon-ng / FOCA | T002:L1459–L1460 | medium: The short list does not establish versions or commands. |
| P2-G051 | osing / housing / async framework | OSINT Framework | T002:L1460–L1469 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G052 | directory / direction listing | directory listing — 目錄索引 | T002:L1525–L1529 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G053 | Windows 7 二零二二 | Windows Server 2022 | T002:L1557–L1577 | high: Resolved by explicit within-file restatement at L1577, not guessed from part 01. |
| P2-G054 | control auto delete | Ctrl+Alt+Delete | T002:L1559–L1561 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G055 | post-poor services | host, port and services | T002:L1596–L1644 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G056 | drivers btc / serious / service 檔案 | drivers/etc/services / /etc/services | T002:L1628–L1642 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G057 | PCPIP / GPI / PCPID | TCP/IP, where networking context is explicit | T002:L1651–L1727 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G058 | UTP, in transport-protocol contrast | UDP — User Datagram Protocol | T002:L1707–L1717 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G059 | 風包 / 紅包 / phone 包 | packet — 封包 | T002:L1686–L1780 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G060 | pay lot | payload — 承載資料 | T002:L1727–L1730 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G061 | TCP Flex | TCP flags — TCP 控制旗標 | T002:L1731–L1748 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G062 | sing / sin / scene / same | SYN, only where TCP synchronization context supports it | T002:L1746–L1772 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G063 | seen egg / scene ache | SYN+ACK | T002:L1868–L1900 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G064 | 3 項交貨 / 3 項交往 | three-way handshake — 三向交握 | T002:L1771–L1789 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G065 | mat-terminal / made terminal | MATE Terminal, likely | T002:L1805–L1807 | medium: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G066 | who am i | whoami | T002:L1810–L1810 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G067 | mmap / m map / end map | Nmap / nmap | T002:L1811–L1994 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G068 | 簡號 sn / 大寫 pr | -sn / -PR | T002:L1812–L1831 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G069 | p1 / p2, in ICMP discovery | Possibly -PE; exact spoken flag unresolved | T002:L1842–L1860 | low: -PE is a documented equivalent, not an unconditional ASR replacement. |
| P2-G070 | 簡號 st / ss | -sT / -sS | T002:L1888–L1917 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G071 | have open / half love scan | half-open SYN scan | T002:L1888–L1917 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G072 | 簡號 sv | -sV | T002:L1920–L1925 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G073 | always discovery / open-source discovery | OS discovery — 作業系統辨識 | T002:L1946–L1971 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G074 | 簡號 o 大寫 | -O | T002:L1967–L1971 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G075 | usr share add map scripts | /usr/share/nmap/scripts, a common package path | T002:L1972–L1981 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G076 | scripts / SMB always discovery | --script / smb-os-discovery | T002:L1982–L1994 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G077 | package recommendation / framework, in fragment discussion | packet fragmentation / fragment | T002:L1995–L2039 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G078 | Satellite source routing | source routing | T002:L2040–L2054 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G079 | source program manipulation | Probably source-port manipulation | T002:L2055–L2075 | medium: The example instead concerns destination port 80; preserve this conceptual mismatch. |
| P2-G080 | hpin3 | hping3 | T002:L2111–L2119 | medium: No executable spoofing or reflection command is reconstructed. |
| P2-G081 | collasoft packet builder | Colasoft Packet Builder | T002:L2121–L2122 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G082 | check sound / check 上 | checksum | T002:L2123–L2142 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G083 | pricey server | proxy server — 代理伺服器 | T002:L2143–L2159 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G084 | no locks | no-logs claim | T002:L2170–L2187 | high: Contextual normalization; not audio-confirmed pronunciation. |
| P2-G085 | serner series / server signature off | ServerSignature Off | T002:L2228–L2234 | high: This directive does not remove the HTTP Server header. |
| P2-G086 | Lab passwords and inconsistent IP strings | Not normalized or reproduced in the knowledge layer | T002:L1530–L1593 | low: Use the provider’s authorized handout; raw text remains only in the sensitive source folder. |

<a id="cross-recording-resolution"></a>
## What part 02 clarifies and what remains open

*Editorial reconciliation of the two references.* Part 01 has an incomplete whiteboard description of the classroom machines. Part 02 explicitly reports Parrot, Windows Server 2019, Windows Server 2022 and Windows 11. That improves the reported role list; it does not establish an IP plan, actual machine state, host compatibility or a learner's access rights. The provider handout remains the owner of actual connection details.

The course sequence previews twenty modules, while the substantive recordings cover M01, M02 and M03. Module 4 enumeration and Module 5 vulnerability analysis are important next conceptual connections, not completed lecture units inferred from the preview. Courseware version v13 is reported in part 01; the exact delivered book was not independently inspected.

Use the [current registration source](../../source/2026-09-18-ucom-class-payment-update/notes.md) for provider-confirmed dates and rights. Do not use a public six-month lab advertisement, a spoken return time or a filename to overwrite individual activation/expiry facts. Package questions, missing handouts and unreadable commands remain named gaps in the [source receipt](../../source/2026-09-20-ceh-week-01/README.md#unresolved-evidence).

The full glossary above preserves source-specific confidence. Similar ASR strings can mean different things: IIS in a web-server passage and iOS in a mobile-platform passage are distinct. Read the source range before applying a normalization; medium- and low-confidence reconstructions remain conditional.
