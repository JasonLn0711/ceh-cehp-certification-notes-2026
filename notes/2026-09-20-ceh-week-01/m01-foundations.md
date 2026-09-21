# M01 — Security foundations, authorization and evidence

The central skill is to explain what a security claim means, which boundary or property it concerns, and what evidence would support it. Part 01 establishes the vocabulary; Part 02 extends it into models, controls, risk, intelligence and governance.

[Week 1 index](README.md) · [Connections](connections.md) · [Complete coverage](coverage.md) · [Source receipt and live checks](../../source/2026-09-20-ceh-week-01/README.md)

Captured 2026-09-20, Asia/Taipei. Detailed sections below reorganize the user-supplied audited study references and retain their wording where precision matters. Linked claim records own status, original line ranges and evidence limits. Newly written synthesis is labeled editorial. These are study notes, not evidence of attendance, personal study completion or executed labs.

## Contents

[中文講義一 §4–11](handouts-zh/part-01.md#h1-04) explains properties, authorization and AI boundaries; [中文講義二 §1–10](handouts-zh/part-02.md#h2-01) connects models, controls, risk, intelligence, response and standards. These are the September 21 supplied teaching-handout companion, not new transcript claims.

- [Five information-security properties](#security-properties)
- [The banking-email example: what it proves and what it does not](#email-evidence)
- [Attack categories and TTPs](#attack-categories)
- [Vulnerability causes and the firewall example](#vulnerabilities)
- [Actor labels, history and allegations](#actor-labels)
- [Authorization, scope and the consultant example](#authorization)
- [AI-assisted testing and safe evidence boundaries](#ai-assisted-testing)
- [Intrusion models and the USB scenario](#intrusion-models)
- [Assurance, adaptive security and layered controls](#layered-controls)
- [Windows SID, ACL and offline disk access](#windows-permissions)
- [Risk and risk management](#risk)
- [Threat intelligence, SOC and CVE](#threat-intelligence)
- [Threat modeling and incident management](#incident-response)
- [Machine learning terminology](#machine-learning)
- [Laws, standards and certification](#law-and-standards)
- [Cross-part synthesis: properties, mechanisms and evidence](#cross-part-synthesis)

<a id="security-properties"></a>
## Five information-security properties

*Source-derived: part 01, 2.5; qualifications retained.*

Preserve the lecture’s five-part organization, but do not present it as the only possible security framework. These are objectives or properties, not five isolated products to buy. Controls may support several properties at once. [S012](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S012) [S013](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S013) [S014](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S014) [S015](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S015) [S016](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S016)

| Property | Meaning to retain | Lecture example, with qualification |
|---|---|---|
| **Confidentiality — 機密性** | Restrict unauthorized access or disclosure. | File permissions can restrict readers. Having permissions configured is not proof that every leakage path is closed. |
| **Integrity — 完整性** | Protect against improper changes or destruction. | Check whether a file was altered or corrupted. A transmission check does not automatically establish long-term stored-file integrity. |
| **Availability — 可用性** | Timely and reliable access and use by authorized entities. | Failover can help a service remain accessible. Performance and data access also matter; encryption does not necessarily lock a whole file throughout every operation. |
| **Authenticity — 真實性／來源鑑真** | Establish that an entity or message is genuinely what it claims to be. | Was the policy actually issued by HR? Genuine origin does not make every statement in the policy factually correct. |
| **Non-repudiation — 不可否認性** | Provide evidence of origin or action that can be assessed by others. | A disputed email requires more than a visual assertion of identity. Technical evidence does not guarantee a particular legal judgment. |

**Evidence by row:** confidentiality [S012](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S012); integrity [S013](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S013); availability [S014](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S014); authenticity [S015](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S015); non-repudiation [S016](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S016) [S017](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S017). **Transcript:** T001:L535–L717. **Claims:** C062–C080.

<a id="email-evidence"></a>
## The banking-email example: what it proves and what it does not

*Source-derived: part 01, 2.6; qualifications retained.*

The lecturer imagines a client disputing an adviser’s investment email. Treat the scenario as a hypothetical about evidence, not a verified fraud case, a rule that every defendant denies everything, or financial advice. The numerical return example is internally garbled: `20%` to `−4%` differs by **24 percentage points**, while `20%` to `−10%` differs by **30 percentage points**. The transcript cannot establish which pair the lecturer intended. See [C074](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C074).

An email printout or a printed certificate fingerprint is not the same as verifying a digital signature over the original electronic message. S/MIME verification involves the signed representation and the relevant certificate/trust checks. A Message-ID is an identifier, not proof of who authored the message. Archives, server records and other evidence may corroborate events, but their trustworthiness and interpretation still matter. [S018](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S018) [S019](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S019)

The correct learning point is to preserve and evaluate evidence of origin and integrity, not to memorize “printed fingerprint = impossible to deny.” Neither the transcript nor the cited standards establishes that every bank email is signed. See [C075](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C075) [C076](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C076) [C077](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C077) [C078](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C078) [C079](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C079).

<a id="attack-categories"></a>
## Attack categories and TTPs

*Source-derived: part 01, 2.7; qualifications retained.*

The lecture groups attacks into passive, active, close-in, insider and distribution categories. Keep this as its teaching framework, but note that it mixes different dimensions: behavior, proximity, relationship and delivery path. A single event can belong to more than one category.

**Passive** concerns observation without alteration; it is not defined simply by “no connection.” **Active** concerns intervention, such as modifying or disrupting activity; a successfully established connection is not required. Packet capture may be passive, while the means used to obtain an observation position can involve separate active behavior. [S020](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S020) [S021](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S021)

**Close-in** is the normalized term in the contractor/server-room example. A propped door or an unescorted visitor can undermine a site’s access policy, but physical proximity does not guarantee compromise. **Insider** concerns misuse of trusted access; internal location does not automatically bypass all controls or make every insider incident the most severe. [S037](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S037)

**Distribution attack** in this lecture is broadly a supply-chain compromise before or during delivery. A legitimate supplier can itself be compromised; this need not mean the vendor intentionally planted malicious functionality. Do not confuse distribution with distributed denial of service. [S025](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S025)

For **TTPs**, retain this distinction: **tactic = objective/why; technique = method/how; procedure = a specific implementation**. These are a vocabulary for behavior, not a diagnosis of personality or a claim about someone’s educational background. [S052](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S052)

**Transcript:** T001:L805–L1043. **Key claims:** [C087](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C087) [C088](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C088) [C089](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C089) [C098](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C098) [C099](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C099) [C100](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C100); [C108](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C108).

<a id="vulnerabilities"></a>
## Vulnerability causes and the firewall example

*Source-derived: part 01, 2.8; qualifications retained.*

The lecture’s causes include misconfiguration, insecure design, inherent technology weaknesses and a partly garbled heading about neglecting end users/endpoints. **Inherent** means intrinsic or 固有, not simply inherited from an old version. Compatibility can re-enable a weak legacy mechanism, but not every compatibility feature is inherently insecure. [S022](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S022)

Turning off Windows Firewall removes a filtering boundary; it does not itself start network services. A previously blocked service may become reachable because a listener already existed. This separates three questions: is an application listening, can traffic reach it, and does the reachable service have an exploitable weakness? [S032](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S032) [S035](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S035)

The endpoint example also needs a condition: a compromised client can provide an avenue toward other systems, but propagation depends on privileges, authentication and segmentation. Reinstallation alone is not a proof that exposure elsewhere has been resolved. The original lesson does not establish that every endpoint must purchase a separate commercial antivirus license. [S037](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S037)

**Transcript:** T001:L870–L910. **Claims:** C091–C097.

<a id="actor-labels"></a>
## Actor labels, history and allegations

*Source-derived: part 01, 2.9; qualifications retained.*

White-hat, black-hat and gray-hat labels are introductory shorthand. The lecture’s blue-hat, red-hat and green-hat definitions are retained as **informal classroom terminology**, not uniformly standardized roles. A blue label is not a credential; a red-hat retaliation story is not the same thing as an authorized red team; a green label does not establish someone’s competence or permission. See [C116](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C116) [C117](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C117) [C118](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C118) [C137](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C137) [C138](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C138) [C139](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C139).

The historical state-surveillance passage needs substantial correction. **NSA** means **National Security Agency**, not the Department of Homeland Security. The 2014 PCLOB account distinguishes provider-assisted PRISM collection from upstream backbone collection. It does not establish the lecture’s claim that PRISM obtains universal access to every cable, router or satellite through preinstalled maintenance backdoors. [S038](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S038) [S039](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S039)

“All hardware and software contain a maintenance backdoor” is unsupported. A documented authorized repair interface and an undocumented bypass are not equivalent. The BIOS password story is model-dependent; the text’s key sequence is not a validated universal recovery method. [S041](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S041) [S042](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S042)

For Snowden’s departure from Hong Kong, the government’s June 23, 2013 statement records voluntary departure through lawful channels, not the asserted forced-departure deadline. This source does not establish his later asylum chronology or current legal status. [S040](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S040)

The unnamed semiconductor theft/apology allegations, rankings of countries by hacker strength, and the unspecified “this-year” conflict are not established facts in this audit. No company, person or contemporary conflict is guessed to fill those gaps. National-interest arguments and statements about genius, friendship or national workforces are kept outside the technical fact layer.

<a id="authorization"></a>
## Authorization, scope and the consultant example

*Source-derived: part 01, 2.10; qualifications retained.*

The strongest operational lesson in the recording is **do not assume permission expands because the tester means well or wants to finish**. In the consultant example, the agreement purportedly limits location, working time and IT accompaniment. If those are actual conditions, continuing alone over lunch or testing from home is not automatically permitted. The correct response is to stop or obtain a documented change, not reinterpret the scope after the fact. [S031](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S031) [S044](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S044)

Scope should identify the affected assets and time boundary; limitations constrain allowed actions and operational conditions. Excluded production or OT systems remain excluded even if reachable. An undated agreement does not, by itself, prove indefinite future access. Nor does any breach automatically establish every element of a criminal offense. The Taiwan statutory reference is included to illustrate the need for precise legal elements, not to adjudicate the lecture’s hypothetical dispute. [S045](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S045)

**Editorial completion criterion for an assessment report:** the reader can distinguish an observation from an inference, understand the potential impact, see the applicability and uncertainty, and identify a justified remediation or validation step. This develops the lecturer’s point that explaining the report matters more than merely pressing a scan button. It is a synthesis for study, not a claim that a specific client engagement met those conditions.

**Transcript:** T001:L1152–L1209; L1361–L1468. See [C143](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C143), [C144](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C144) and [C147](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#C147).

<a id="ai-assisted-testing"></a>
## AI-assisted testing and safe evidence boundaries

*Source-derived: part 01, 2.11; qualifications retained.*

The lecture correctly identifies assistance with explanations and code generation. It does not establish that security jobs can never be replaced, that every Indian technical-support job has already disappeared, or that only experts can benefit from AI. Research on occupational exposure is not proof of universal job elimination; future workforce outcomes must remain uncertain. [S046](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S046)

The SMTP/Nmap demonstration is too garbled to reproduce. No target identity, valid options or observed account list can be recovered. A written request, a model-generated command and a command’s actual result are distinct. No real scan or account enumeration was performed as part of producing this artifact.

**ShellGPT** here is the third-party `TheR1D/shell_gpt` project, not an official OpenAI-owned application. Its README describes Windows, Linux and macOS support, interactive generation and execution-capable configurations. Whether a command executes depends on the selected mode and functions; the product name alone does not establish automatic execution or a guaranteed human approval gate. [S047](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S047)

A prompt is not magical executable authority. Harm occurs when an application turns attacker-influenced model output into an action with sufficient permissions. Direct malicious instructions and indirect injection through a retrieved file should be distinguished. Defenses need to consider the input/output trust boundary, allowed tools, privileges, consequential-action approval and what actually ran—not simply whether a traditional malware file was uploaded. No individual filter guarantees complete protection. [S048](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S048) [S049](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S049)

Fluent answers can be wrong. Including an IP address does not, by itself, define every request as impermissible, and replacing it with a placeholder does not confer authorization. Check the actual purpose, scope and applicable tool policy. [S050](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S050) [S051](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-01-course-overview-m01.verified.md#S051)

**Transcript:** T001:L1469–L1553. The recording ends before the afternoon lesson.

<a id="intrusion-models"></a>
## Intrusion models and the USB scenario

*Source-derived: part 02, M01.1; qualifications retained.*

**Transcript coverage:** T002:L1–L133 (00:00:00–00:14:31). **Audit records:** [P2-C001](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C001) [P2-C002](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C002) [P2-C003](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C003) [P2-C004](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C004) [P2-C005](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C005) [P2-C006](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C006) [P2-C007](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C007) [P2-C008](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C008) [P2-C009](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C009) [P2-C010](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C010).

The USB story is a hypothetical about delivery, user execution and subsequent control. It does not measure the behavior of a population or show that inserting ordinary storage automatically runs malware. The recording starts in the middle of this discussion; earlier explanation is not reconstructed.

**Model distinctions.** The Cyber Kill Chain is a phase-oriented model. ATT&CK organizes adversary objectives and methods, not a compulsory sequence of steps. A tactic answers what objective an adversary pursues; a technique describes a method; a procedure is a concrete implementation. A defender can use these distinctions to ask what evidence and controls correspond to a behavior. Mapping a technique does not demonstrate that a detector works. [P2-S001](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S001)

The **Diamond Model** relates adversary, capability, infrastructure and victim. It is an analytical model for relating intrusion events, not only a simplified slide for executives. Capability may be acquired rather than custom written; the victim may include an organization or person rather than just a computer. [P2-S002](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S002)

**Editorial application:** describe one hypothetical incident using the four Diamond features; label each as observed, inferred or unknown. Present the decision, potential impact and evidence before tool-level detail. The lecturer’s judgments about a manager’s motives or a presenter’s career are opinions, not part of the model.

<a id="layered-controls"></a>
## Assurance, adaptive security and layered controls

*Source-derived: part 02, M01.2; qualifications retained.*

**Transcript coverage:** T002:L134–L265 (00:14:37–00:29:13). **Audit records:** [P2-C011](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C011) [P2-C012](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C012) [P2-C013](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C013) [P2-C014](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C014) [P2-C015](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C015) [P2-C016](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C016) [P2-C017](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C017) [P2-C018](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C018) [P2-C019](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C019) [P2-C020](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C020) [P2-C021](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C021).

**Information assurance (IA)** concerns protecting and defending information and systems with attention to relevant security properties and measures. The lecturer lists four properties; that is not an exhaustive universal IA definition or a literal guarantee that information cannot be wrong. [P2-S003](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S003)

The lecture’s adaptive loop is **protect → detect → respond → predict**. Preserve that course framing without confusing it with a universal mandated sequence. Protection reduces exposure, detection looks for relevant activity, response addresses events, and prediction estimates future conditions under uncertainty. This does not imply precise foreknowledge.

**Defense in depth** uses complementary controls across people, operations and technology, rather than relying on one permission setting. The transcript traverses policy, physical access, perimeter/DMZ, internal networking, hosts, applications and data. These are useful layers to examine, not a fixed product shopping list. A DMZ is a network zone with a controlled relationship to other zones; its label alone is not protection. [P2-S004](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S004)

**Editorial example:** combine a documented visitor procedure, appropriate physical access, restricted network paths and data protection for a hypothetical server room. Check whether the controls share a failure mode. Physical access barriers must also comply with applicable life-safety requirements; the lecture’s mantrap analogy is not an installation plan.

<a id="windows-permissions"></a>
## Windows SID, ACL and offline disk access

*Source-derived: part 02, M01.3; qualifications retained.*

**Transcript coverage:** T002:L217–L240 (00:23:07–00:26:07). **Audit records:** [P2-C014](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C014) [P2-C015](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C015) [P2-C016](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C016) [P2-C017](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C017) [P2-C018](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C018).

A **security identifier (SID)** identifies a Windows security principal. A **discretionary access-control list (DACL)** contains access-control entries evaluated against a caller’s security context. These are not just visible account-name strings. Moving a drive does not make its access rules disappear because a name cannot be resolved. [P2-S005](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S005) [P2-S006](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S006)

The valid security concern is different: an attacker controlling an offline environment may circumvent OS-enforced file permissions. Appropriate at-rest encryption can protect a stolen drive when the necessary keys remain unavailable. Permission checks and cryptographic protection address different boundaries. [P2-S007](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S007)

The theft story is hypothetical. The stated financial reward, fixed sentence and presumed guard response are not established. Taiwan’s criminal-proceeds confiscation rule alone is enough to show why keeping all proceeds after a fixed period in custody is not a valid general conclusion; it does not determine a sentence for this invented case. [P2-S025](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S025)

<a id="risk"></a>
## Risk and risk management

*Source-derived: part 02, M01.4; qualifications retained.*

**Transcript coverage:** T002:L266–L346 (00:29:15–00:37:08). **Audit records:** [P2-C022](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C022) [P2-C023](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C023) [P2-C024](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C024) [P2-C025](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C025) [P2-C026](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C026) [P2-C027](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C027) [P2-C028](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C028) [P2-C029](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C029).

**Core correction:** risk is not merely a known problem left unfixed, and risk level is not probability alone. Assess both likelihood and adverse consequences, while recording uncertainty. An unknown weakness can still create risk; discovering it changes knowledge, not whether a consequence was possible. [P2-S008](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S008)

The lecture’s management path is **identify → assess → treat → track → review**. Identification is substantive work: identify assets, possible events and consequences. Treatment can involve mitigation, avoidance, acceptance or sharing/transferring selected consequences. Insurance does not remove the technical weakness or all responsibilities. [P2-S009](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S009)

**Editorial workflow:** define the service and harm of concern; state current evidence; assess likelihood and impact; select a response with an owner; set review conditions; reassess after changes. A numerical formula is not required, and multiplying arbitrary ordinal labels does not make an estimate precise.

**Lecture scenario, qualified:** delaying a patch until Friday can be a controlled decision, but needs exposure assessment, change safeguards and responsible approval. Unsupported equipment does not force a choice between immediate replacement and doing nothing: isolation, reduced functionality or retirement may be alternatives. No one maintenance window is universally correct.

<a id="threat-intelligence"></a>
## Threat intelligence, SOC and CVE

*Source-derived: part 02, M01.5; qualifications retained.*

**Transcript coverage:** T002:L347–L389 (00:37:11–00:43:10). **Audit records:** [P2-C030](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C030) [P2-C031](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C031) [P2-C032](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C032) [P2-C033](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C033) [P2-C034](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C034).

**Cyber threat intelligence** is decision-relevant analysis of threat information, not merely a scrapbook of alarming news. Relevant inputs can include incident analysis, adversary behavior and indicators. Source quality, relevance and uncertainty still matter. [P2-S011](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S011)

Retain the course’s **strategic, tactical, operational and technical** audience categories as its organizing convention. They are not universal job-title routing rules. A **security operations center (SOC)** is a coordinated monitoring, analysis and response function; it can be internal, outsourced or hybrid and is not necessarily the owner of every organizational security duty. [P2-S072](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S072)

A **CVE identifier** names a publicly known vulnerability; it is not the identifier of every attack, an exploit result, or an environment-specific risk decision. [P2-S082](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S082)

**Editorial lifecycle:** define the intelligence question → collect relevant material → process and analyze → distribute to the relevant decision maker → gather feedback and update. The transcript’s lifecycle passage is incomplete; this is an organizing addition. Older intelligence can remain useful for behavior analysis and comparison. Familiarity alone does not make it worthless.

<a id="incident-response"></a>
## Threat modeling and incident management

*Source-derived: part 02, M01.6; qualifications retained.*

**Transcript coverage:** T002:L390–L529 (00:43:12–00:58:33). **Audit records:** [P2-C035](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C035) [P2-C036](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C036) [P2-C037](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C037) [P2-C038](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C038) [P2-C039](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C039) [P2-C040](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C040) [P2-C041](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C041) [P2-C042](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C042).

**Threat modeling** develops a structured account of what a system is trying to protect, how it works, what can go wrong and how to address it. The lecture lists security objectives, application overview, decomposition, threat identification and vulnerability identification. Decomposition should consider components, data movement and trust boundaries—not merely which employee receives a report. [P2-S012](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S012)

**Editorial example:** for an application, distinguish browser input, application logic, database access and administrative operations. State the permitted relationships before considering how a boundary might fail. Assign remediation to the relevant owner without assuming that all developers lack system knowledge or that all administrators cannot code.

An **artifact** is material useful to analysis, such as a log entry, file, message or error record. It is not automatically trustworthy or sufficient evidence. Preserve relevant context and distinguish observations from interpretation.

The incident-management headings in the lecture—vulnerability handling, artifacts, announcements, alerts, handling, response and disclosure—should not be read as a mandatory chronology. Immediate containment can precede complete root-cause analysis. The reviewed NIST SP 800-61 Rev. 3 publication record places response in broader risk management; detailed workflow below is editorial, not a quotation from its full PDF. [P2-S010](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S010)

**Editorial workflow:** receive a report → assess urgency and scope → preserve needed evidence → contain proportionately → investigate and coordinate recovery → review. Escalate capability or authority gaps instead of giving unsupported repair promises. Disclosure and notification duties can arise before resolution: GDPR Articles 33 and 34 have different thresholds and timing requirements. Do not postpone all notification until the system is fixed. [P2-S022](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S022)

The remembered Rakuten notice and the unnamed computer-company interviews are not independently authenticated. They remain anecdotes, not case studies with verified dates or quotations.

<a id="machine-learning"></a>
## Machine learning terminology

*Source-derived: part 02, M01.7; qualifications retained.*

**Transcript coverage:** T002:L530–L541 (00:58:41–01:00:13). **Audit records:** [P2-C043](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C043) [P2-C044](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C044).

**Supervised learning** uses target information with training examples; the target may be a category or a numerical value. **Unsupervised learning** seeks structure without those target labels. Neither definition promises that supervised learning starts accurate or that unsupervised learning necessarily starts inaccurate. Supervised versus unsupervised is not an exhaustive taxonomy of machine learning. [P2-S013](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S013)

**Editorial example:** a hypothetical email classifier learns from examples labeled unwanted or legitimate. A different model groups observations by similarity without those labels. Both need appropriate evaluation; the label “AI-powered” does not establish accuracy, robustness or the quality of the supplied training data.

<a id="law-and-standards"></a>
## Laws, standards and certification

*Source-derived: part 02, M01.8; qualifications retained.*

**Transcript coverage:** T002:L542–L740 (01:00:23–01:19:17). **Audit records:** [P2-C045](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C045) [P2-C046](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C046) [P2-C047](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C047) [P2-C048](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C048) [P2-C049](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C049) [P2-C050](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C050) [P2-C051](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C051) [P2-C052](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C052) [P2-C053](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C053) [P2-C054](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C054) [P2-C055](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C055) [P2-C056](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C056) [P2-C057](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C057) [P2-C058](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C058) [P2-C059](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-C059).

A law, regulation, contract, technical standard and certification are different sources of obligations or evidence. A voluntary standard can become relevant through a contract or legal requirement. An unregistered business is not exempt from applicable duties merely because an authority has not noticed it.

| Topic | Audited interpretation | Evidence |
|---|---|---|
| PCI DSS | Applies according to payment-account-data and cardholder-data-environment scope, including relevant merchants and service providers—not only card issuers. A discount card without payment functionality is not automatically the same case. | [P2-S014](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S014) |
| ISO/IEC 27001 | Specifies requirements for a scoped information security management system (ISMS). Documentation supports implementation, evaluation and improvement; buying templates is not proof of conformity. | [P2-S015](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S015) |
| Certification | ISO writes standards but does not itself certify organizations. Personnel lead-auditor training and organizational ISMS certification are different. | [P2-S016](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S016) |
| NIST versus ISO | Not an exclusive US-versus-rest-of-world division; applicability and adoption can overlap. | [P2-S081](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S081) [P2-S015](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S015) |
| HIPAA | US rules apply to defined covered entities and business associates. Do not extend that scope to every medical institution worldwide or substitute it for local clinical-consent rules. | [P2-S017](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S017) [P2-S018](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S018) |
| SOX-related retention | The SEC rule concerns specified audit/review records retained by auditors, including relevant electronic communications. Not every company email and tax record has a universal seven-year rule from this source. | [P2-S019](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S019) |
| DMCA | The 1998 Act addresses technological circumvention and online-service-provider matters; digital works were not excluded from copyright simply because they lacked paper. | [P2-S020](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S020) [P2-S021](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S021) |
| EU GDPR | Adopted in 2016; generally applicable from 25 May 2018. Scope and rights have conditions. Erasure, delisting and deletion of original content are not identical. | [P2-S022](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S022) |
| UK framework | The Data Protection Act 2018 and UK GDPR operate together; the Data (Use and Access) Act 2025 amends the framework. It is not accurately explained as a simple post-Brexit renaming. | [P2-S023](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S023) [P2-S024](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S024) [P2-S080](../../source/2026-09-20-ceh-week-01/ceh-week-01-part-02-m01-m03.verified.md#P2-S080) |

**Limits:** this is a source-linked course correction, not individualized legal advice or a complete compliance plan. The “50.5% of judges,” global superlatives, fixed criminal penalties and alleged political motives are not established by the reviewed evidence. Identify the entity, jurisdiction, date, data and relevant rule before applying a legal conclusion.

<a id="cross-part-synthesis"></a>
## Cross-part synthesis: properties, mechanisms and evidence

*Editorial synthesis of the linked claim records above.* The five properties describe what needs protection. An ACL, a firewall, a signature and a failover cluster are mechanisms. An observation establishes only what the actual check examined. This distinction connects both recordings and prevents a product name from standing in for assurance.

| Situation | Property or decision | Evidence needed | Connection |
| --- | --- | --- | --- |
| An unchanged file is disclosed to an unauthorized reader | Confidentiality | Access context and data actually disclosed | [September 15 permission example](../m05-vulnerability-analysis/lesson-01-weakness-to-harm.md) |
| A genuine sender's email contains a mistaken fact | Authenticity versus factual accuracy | Message/certificate context plus independent evidence for the fact | [Email evidence](#email-evidence) |
| A permission-protected disk is stolen | OS enforcement versus at-rest protection | Encryption/key state and actual access conditions | [Windows permissions](#windows-permissions) |
| A scanner recognizes a software version | Applicability and risk remain open | Installed fixes, configuration, exposure and impact | [M03 identification](m03-network-scanning.md#identification) |
| A model prints a plausible command or result | Proposed action versus observed execution | Permission, tool record, actual output and independent check | [AI research connection](connections.md) |

Risk treatment should end with an owner and review condition. For the lecture's patch-delay example, the useful question is which exposure remains during the delay and which change risks justify it. The answer depends on the specific system; a Friday window, a manager's verbal agreement or insurance coverage is not a universal solution.

A usable assessment explanation follows four sentences: describe the observation; state the supported interpretation; identify uncertainty and likely consequence; name the next permitted verification or remediation. This is an editorial communication pattern, not a new assignment or a claim that the source demonstrated an assessment.

## Current-law and source-check boundary

The law/standards comparison supports jurisdiction and obligation literacy. The [fresh-check receipt](../../source/2026-09-20-ceh-week-01/README.md#live-checks) records what was inspected, including Taiwan statutory text and official privacy/standards pages. It does not determine liability in the lecture's hypotheticals. The supplied audit's unsupported anecdotes remain unsupported. UK amendments require provision-specific commencement checks before any operational decision.

## Reuse within the current course

[M01 questions](../../assessments/practice-bank/m01.md) support the existing learning route. The [ROE notes](../../source/2026-09-04-antisyphon-roe-101/source.md) deepen the scope example; the [M05 lesson](../m05-vulnerability-analysis/lesson-01-weakness-to-harm.md) deepens vulnerability/risk distinctions. This capture adds no answers, confidence, retests or personal practical evidence.
