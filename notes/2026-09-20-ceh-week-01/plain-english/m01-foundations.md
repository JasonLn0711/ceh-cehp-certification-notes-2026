# M01 — Security foundations, authorization and management

[Reading map](README.md) · [Every source heading](coverage.md) · [Connections](connections.md) · [Unchanged source](../../../source/2026-09-21-ceh-merged-plain-english/CEH_Full_Merged_Plain_English.md)

Captured 2026-09-21, Asia/Taipei. The source-derived text below retains the supplied explanation, examples, correction labels, uncertainty and citations. Heading levels are adjusted for reading; explicit anchors and **Study connection — editorial** paragraphs are additions. References to recordings or earlier checking are the source author's statements, not new observations. This file covers original lines 340–1198.

## Reading route

- [Part 1 · 4. The core of Module 1: Five elements of information security](#p1-04)
- [Part 1 · 5. Attack, vulnerability, exploit, and compromise: Four terms that are not interchangeable](#p1-05)
- [Part 1 · 6. Where do vulnerabilities come from, and what does TTP mean?](#p1-06)
- [Part 1 · 7. Five attack categories: Use categories to ask the right defensive questions](#p1-07)
- [Part 1 · 8. White hats, black hats, gray hats, and red and blue teams](#p1-08)
- [Part 1 · 9. A complete ethical-hacking test: From permission to confirming the fix](#p1-09)
- [Part 1 · 10. AI-assisted hacking: What can AI help with, and what new problems can it introduce?](#p1-10)
- [Part 1 · 11. Bringing the class together: The abilities you actually need](#p1-11)
- [Part 2 · 1. Cyber Kill Chain, MITRE ATT&CK, and the Diamond Model: Three different analysis tools](#p2-01)
- [Part 2 · 2. Information assurance — Reliable protection, not a verbal promise](#p2-02)
- [Part 2 · 3. Defense in depth — Why one checkpoint is not enough](#p2-03)
- [Part 2 · 4. SID, ACL, and NTFS permissions — Why moving a disk to another computer does not automatically cancel permissions](#p2-04)
- [Part 2 · 5. Risk and risk management — Risk is not just probability](#p2-05)
- [Part 2 · 6. Cyber threat intelligence, SOC, and CVE — Turning information into something actionable](#p2-06)
- [Part 2 · 7. Threat modeling — Explain how things could go wrong before they do](#p2-07)
- [Part 2 · 8. Incident management — Manage impact and evidence when something happens](#p2-08)
- [Part 2 · 9. Supervised and unsupervised learning — The difference is in labels, not inherent accuracy](#p2-09)
- [Part 2 · 10. Laws, standards, and certifications — First distinguish what they are](#p2-10)

<!-- source-derived-text-begin -->


<a id="en-h032"></a>

<a id="p1-04"></a>

## Part 1 · 4. The core of Module 1: Five elements of information security

**Study connection — editorial:** Name the security property first, then the mechanism and the evidence needed to show that it works. [Chinese explanation](../handouts-zh/part-01.md#h1-04) · [Audited detail](../m01-foundations.md#security-properties) · [Source coverage](coverage.md#en-h032). Source section: lines 340–452.

The class introduces **confidentiality, integrity, availability, authenticity, and non-repudiation**, in that order. These are security goals, not five separate products.

We will use the same university grade system to understand all five.


<a id="en-h033"></a>

### 1. Confidentiality — People who are not allowed to see information must not see it

Confidentiality means preventing unauthorized access or disclosure. It does not mean that nobody may see the information. It means that only permitted people may see it. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/confidentiality))

For example, Student A may see their own grades. A teacher may see the grades for the course they teach. An unrelated visitor must not be able to read every student's records.

A typical process is:

**Receive a request → Identify the requester → Check their permission for this data → Allow or deny access.**

Two terms must be kept separate:

**Authentication: Who are you?**
**Authorization: What are you allowed to do?**

Knowing that you are a particular student does not mean you have permission to read the entire university's grades. ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html))

A practical failure occurs when a website checks only whether you are logged in, but not whether the requested data belongs to you.

Encryption can help protect data, but it cannot replace permission checks. Even if all communication is encrypted, data is still exposed if the website returns another person's grades to you through its normal response mechanism.


<a id="en-h034"></a>

### 2. Integrity — Data must not be improperly changed or destroyed

Here, integrity does not simply mean that no page is missing from a file. It means protecting data against improper modification and destruction. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/integrity))

For example, a teacher who follows the proper procedure to change a grade from 78 to 82 makes an authorized change. A student who changes their own grade from 58 to 98 violates integrity.

Integrity therefore does not mean that nothing can ever change. It means:

> Changes must follow permissions and rules, and we must be able to detect changes that should not have happened.

The class also points out that a computer restarting successfully after a crash does not establish that all its data is still correct. “The system can start” and “the data has integrity” are different claims.

**Teaching addition: Hashing.**

A hash function maps input data to a fixed-length digest. A cryptographic hash is also designed to have properties such as being difficult to reverse and making deliberate collisions difficult to find. It is not a way of encrypting a file for later decryption. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/hash_function))

A simplified file-checking process is:

**Obtain a trusted original file → Calculate and protect its digest → Recalculate the digest later → Compare the digests.**

For example, if the digest calculated after downloading a file differs from the digest published by a trusted source, there is reason to suspect that the files do not match.

However, if an attacker can replace both the file and the digest used for comparison, a match alone does not establish a trustworthy origin. **The digest itself also needs a trusted source.**


<a id="en-h035"></a>

### 3. Availability — Information or services must be usable when needed, under reasonable conditions

Availability emphasizes timely and reliable access to information or services for legitimate users. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/availability))

For example, the course-registration server may be powered on, but each operation takes so long that students cannot complete registration before the deadline. That is still an availability problem.

The class mentions **clusters** and **failover**: multiple nodes and a takeover mechanism can reduce the interruption caused by the failure of a single machine.

A teaching workflow is:

**Continuously check whether the service works → Detect a failure → Have another available node take over → Confirm that users can actually complete their work.**

The last step matters. You cannot merely check whether the backup machine's lights are on. You must verify the actual service capability of the data, network, and application.

**Correction: Encryption consumes resources, but not every encryption method makes an entire file completely unreadable for the whole operation.** The classroom example warns that processing performance can affect availability. It does not describe a fixed behavior of every system.


<a id="en-h036"></a>

### 4. Authenticity — Is the source or identity really what it claims to be?

Authenticity concerns whether a message, entity, or source is genuine and can be verified. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/authenticity))

The classroom example asks, “Did HR really publish this leave policy?”

A university example would be receiving a notice labeled “Academic Affairs Office,” complete with the university logo and an administrator's name. Looking official does not prove that it came from that office.

Distinguish these questions:

“Has the document's content remained unchanged?” is a question about integrity.
“Did the document really come from the Academic Affairs Office?” is a question about authenticity.

There is a further distinction: **A genuine source does not guarantee correct content.** The Academic Affairs Office may truly have issued a notice that contains a wrong date. Verifying the source cannot replace checking the facts.


<a id="en-h037"></a>

### 5. Non-repudiation — Evidence that a third party can use to assess an action

Non-repudiation does not make it impossible for someone to deny something. It means retaining enough evidence for a third party to assess whether a claimed source or action is established. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/non_repudiation))

For example, a teacher submits final grades, and a dispute arises later. The system needs reliable evidence to clarify what was submitted, which identity was used, and what processing occurred. Saying “your name was on the screen” is not enough.

The class uses a dispute over a bank email to illustrate proving origin and content. However, a printed name, a fingerprint code, or a Message-ID should not be treated as complete digital verification.


<a id="en-h038"></a>

### How does a digital signature work?

A **digital signature** is the result of a cryptographic operation on data. When used correctly, it can help verify origin and integrity and provide evidence relevant to non-repudiation. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/digital_signature))

A simplified process is:

1. The signer uses their **private key** to create a signature for specific electronic data.
2. The recipient obtains the original electronic data, the signature, and the corresponding **public key**.
3. The verification procedure checks whether the signature, data, and public key match correctly.
4. Separately, the recipient checks why this public key should be trusted as belonging to a particular identity. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/asymmetric_key_cryptography))

The fourth step cannot be skipped. Otherwise, anyone could create a key pair and label the public key “Academic Affairs Office.”

A **certificate** can carry information linking a public key to an identity. The verifier still needs to examine the relevant trust relationship. This is also why the original electronic data that can actually be verified should be preserved, rather than only its printed appearance.

A leaked private key, an impersonated account, or unreliable records may also affect how the evidence is interpreted. Do not turn “there is a digital signature” into “every dispute must have a particular outcome.”

**Putting the five elements together:**

Confidentiality asks who may see the information. Integrity asks whether it was improperly changed. Availability asks whether it can be used when needed. Authenticity asks whether the source is genuine. Non-repudiation asks whether reliable evidence remains to clarify what happened afterward.

---


<a id="en-h039"></a>

<a id="p1-05"></a>

## Part 1 · 5. Attack, vulnerability, exploit, and compromise: Four terms that are not interchangeable

**Study connection — editorial:** A weakness, a way of using it, and an observed loss of security are different stages of reasoning. [Chinese explanation](../handouts-zh/part-01.md#h1-05) · [Audited detail](../m01-foundations.md#vulnerabilities) · [Source coverage](coverage.md#en-h039). Source section: lines 453–494.


<a id="en-h040"></a>

### Attack — An activity that attempts to violate security goals

The class points out that attacks are not limited to crashing servers. They also include stealing data and observing communication without permission.

However, do not go to the opposite extreme and call every use of a probing tool a malicious attack. The same observation or testing method may be used in authorized testing, troubleshooting, or unauthorized activity. You must consider the purpose, permission, and actual behavior.


<a id="en-h041"></a>

### Vulnerability — A weakness that may be exploited

Vulnerabilities are not limited to code. They may exist in a system's design, configuration, processes, or controls. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/vulnerability))

Example: A grade website checks that a student is logged in but does not check whether the student is allowed to read the particular grade record requested.

The vulnerability exists even if nobody has exploited it yet.


<a id="en-h042"></a>

### Exploit — A way of turning a weakness into an effect

In the example above, someone takes advantage of the missing permission check to make a read request that the system should reject. That is exploiting a vulnerability. “Exploit” can also mean the program or method used to take advantage of a weakness.

Therefore, discovering a vulnerability and successfully exploiting it are different conclusions.


<a id="en-h043"></a>

### Compromise — A state in which security has been affected

For example, if someone without permission has read Student B's grades, the confidentiality of that data has been compromised.

**Correction: A compromise does not require an attacker to first turn off antivirus software or a firewall.** Unauthorized disclosure, modification, or use of sensitive information may already constitute a compromise. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/compromise))

A simple way to remember the three central terms is:

**A vulnerability is the weakness. An exploit is a way to use the weakness. A compromise is the resulting state in which security has been violated.**


<a id="en-h044"></a>

### Teaching addition: Threat and risk

A **threat** is a circumstance or event that may cause an adverse effect. **Risk** requires considering both the likelihood of an event and its impact. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/threat))

For example, the same configuration error in a disposable, offline practice VM and in an internet-facing system containing the whole university's grades should not receive the same priority merely because the vulnerability has the same name.

This is why a security report cannot just list vulnerability names. It also needs to explain the environment and consequences.

---


<a id="en-h045"></a>

<a id="p1-06"></a>

## Part 1 · 6. Where do vulnerabilities come from, and what does TTP mean?

**Study connection — editorial:** Conditions explain whether an action can work; TTP describes the purpose, method and actual implementation. [Chinese explanation](../handouts-zh/part-01.md#h1-06) · [Audited detail](../m01-foundations.md#attack-categories) · [Source coverage](coverage.md#en-h045). Source section: lines 495–562.


<a id="en-h046"></a>

### 1. Misconfiguration

Software may provide security features, but the user may configure permissions, networking, or services incorrectly.

The class uses turning off the Windows firewall as an example. More precisely, **turning off a firewall does not create a running network service out of nothing. It may make a service reachable when that service was already running but its traffic was blocked.**

Ask three separate questions:

**Is a program listening? Is it reachable over the network? Once reached, does it have an exploitable problem?**

These questions do not mean the same thing.


<a id="en-h047"></a>

### 2. Insecure design

A problem may have existed since the design stage, rather than arising from a missing patch later.

For example, a designer assumes that anyone who can log in is a trusted insider and therefore fails to create suitable permission rules for different users and data.

A longer password alone cannot fix this problem. The system's model of who may do what was incomplete from the beginning. ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html))


<a id="en-h048"></a>

### 3. Inherent technology weaknesses

**“Inherent” means built into the nature of something. It does not mean “inherited.”**

Some technologies have security limitations in their original design. Re-enabling an old feature for compatibility may also expose an old problem again. However, this does not justify saying that every compatibility feature is unsafe.

Learn to ask: “What does this feature provide? What limitations does it introduce? Does it still meet our current needs?”


<a id="en-h049"></a>

### 4. Ignoring users and endpoints

In this context, an **endpoint** is a device such as an employee's computer. The class warns against protecting only the servers in the machine room while assuming that an employee's compromised computer can simply be reinstalled and forgotten.

Teaching example: After gaining control of an employee's computer, an attacker may try to use resources that the computer can access.

Activity that starts from an established position and extends to other systems illustrates **lateral movement**. Whether it succeeds still depends on permissions, authentication, and network segmentation. One infected computer does not automatically mean that every computer will be infected.


<a id="en-h050"></a>

### 5. How should we read the classroom “conditions for attack success”?

The transcript discusses motivation, methods, and weaknesses, but the formula itself was not recognized clearly enough to reconstruct it as a precise scientific law.

The useful idea is that desire alone does not make an attack work. There must be conditions and a path that can produce the effect. The classroom example is that a camera without a motor cannot be made to physically rotate through a remote command. Technical actions are also limited by physical capabilities.

Failing to find a software vulnerability does not establish that the whole system has no other weaknesses. Accounts, procedures, and human interactions may still need to be examined.


<a id="en-h051"></a>

### 6. TTP — Describing behavior at three levels

**TTP stands for tactics, techniques, and procedures.** The class uses it to discuss planning and methods, while the MITRE ATT&CK terminology provides a more precise set of levels. ([MITRE ATT&CK](https://attack.mitre.org/resources/faq/))

**Tactic: The goal.** What is this step trying to achieve? For example, obtaining initial access.

**Technique: The type of method.** What kind of method is used to achieve the goal? For example, phishing.

**Procedure: The specific implementation.** What actually happened in a particular activity? For example, which notice, delivery method, and sequence of actions were used in that situation?

A non-attack analogy may help:

Goal: Get into the library.
Method: Use a valid student ID to pass the access gate.
Specific procedure: Go to a particular entrance that afternoon, place the card on the reader, and enter after the gate opens.

Likewise, when analyzing a security incident, do not merely say that the attacker was highly skilled. Describe the goal, the method, and the actual behavior.

**Correction: TTP is not a personality assessment. It cannot establish whether someone with a particular educational background will or will not become a hacker.** Also, the order of course chapters does not mean that all attacks follow a fixed sequence. ([MITRE ATT&CK](https://attack.mitre.org/resources/faq/))

---


<a id="en-h052"></a>

<a id="p1-07"></a>

## Part 1 · 7. Five attack categories: Use categories to ask the right defensive questions

**Study connection — editorial:** Attack categories describe different dimensions and may overlap; use each to identify a defensive question. [Chinese explanation](../handouts-zh/part-01.md#h1-07) · [Audited detail](../m01-foundations.md#attack-categories) · [Source coverage](coverage.md#en-h052). Source section: lines 563–612.

The class groups attacks as **passive, active, close-in, insider, and distribution** attacks. These categories mix several viewpoints, so one incident may belong to more than one category. They are not five mutually exclusive boxes.


<a id="en-h053"></a>

### Passive attack

The central idea is observation without changing the system or data, such as listening to communication without permission. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/passive_attack))

**Correction: “Not connecting to the target” is not an adequate definition.** You need to examine whether the activity changes data, state, or communication.

Teaching example: Someone gains an opportunity to observe communication but does not alter what they see. The defensive questions are: “What information could be exposed? Is the content protected?”


<a id="en-h054"></a>

### Active attack

The central idea is active intervention, such as modifying, forging, or disrupting systems or communication, rather than simply observing them. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/active_attack))

For example, an attacker tries to change grades rather than merely read them, or disrupts a website rather than simply observing its traffic.

**Correction: Failing to establish an ordinary connection does not rule out an active attack.** Classification cannot depend only on whether a connection succeeded.


<a id="en-h055"></a>

### Close-in attack

This category focuses on opportunities created by getting physically close to people, equipment, or a location.

In the classroom example, a contractor enters the server room, but the escort leaves and may even leave the door open for convenience. Everyday behavior can therefore defeat the intended access controls.

Defenders should ask: What can visitors reach? Who must escort them? How is their departure confirmed when the job is complete?

Physical proximity does not guarantee a successful intrusion. It creates a set of conditions that need their own controls.


<a id="en-h056"></a>

### Insider attack

This category concerns the misuse of existing trust and access. The class notes that insiders may already have accounts and know the company's environment.

For example, an employee is allowed to view some customer records for work but uses those records for an unauthorized purpose.

Remember: **A legitimate account does not make every use of it legitimate or compliant. Being on the internal network does not justify having every permission.**

On the other hand, the name “insider attack” alone does not establish that it is always more serious than an external attack.


<a id="en-h057"></a>

### Distribution attack — Attacks through delivery or the supply chain

The classroom description involves tampering with hardware, software, or its delivery process, so that users encounter the problem when they receive the product. In modern analysis, this can be connected with **supply chain compromise**. ([MITRE ATT&CK](https://attack.mitre.org/techniques/T1195/))

Teaching example: An otherwise legitimate software company has its update-release process compromised, causing customers to receive a modified update.

**Correction: The supplier is not necessarily acting maliciously; it may also be a victim.** A distribution attack is not the same as distributed denial-of-service. The names are similar, but they describe different things.

---


<a id="en-h058"></a>

<a id="p1-08"></a>

## Part 1 · 8. White hats, black hats, gray hats, and red and blue teams

**Study connection — editorial:** Evaluate actual behavior and permission. A hat color or actor label supplies neither authority nor proof of attribution. [Chinese explanation](../handouts-zh/part-01.md#h1-08) · [Audited detail](../m01-foundations.md#actor-labels) · [Source coverage](coverage.md#en-h058). Source section: lines 613–646.

These labels are easy to remember, but they can lead people to mistake a role name for proof of skill or proof that an action is justified.

In this class, a **white hat** is someone who has permission and performs security testing within scope. A **black hat** describes someone who maliciously breaks into systems or abuses security weaknesses.

The material describes a **gray hat** as someone who sometimes works within permission and sometimes crosses the boundary. This is an introductory label, not a legal category that can replace analysis of the actual behavior.

The class uses **script kiddie** for someone who mainly runs ready-made tools without understanding the underlying principles well. The point is limited understanding, not age. Using existing tools is not itself a problem; the question is whether you can explain the action, result, and risks.

Other colors should be read in the context of this particular material:

**Blue hat:** In this course, an outside expert temporarily invited to help with testing.
**Red hat:** In this course, someone who attacks black hats in return.
**Green hat:** In this course, a beginner who is willing to learn.

These are not uniformly or rigorously standardized professional qualifications. In particular, calling someone a red hat does not automatically authorize them to attack another person's system.


<a id="en-h059"></a>

### Red teams and blue teams are not the same as red hats and blue hats

In an authorized exercise, the **red team** simulates the attacking side, while the **blue team** defends, observes, and responds. The class introduces this distinction through “information warfare,” but does not develop a complete theoretical framework for information warfare.

Teaching example: The red team tests an agreed attack path. The blue team checks whether it detects the activity, can assess the impact, and can stop or handle it.

The useful learning questions are: “Which steps succeeded? Which defenses failed? How can we improve?” The point is not whose title sounds more impressive.


<a id="en-h060"></a>

### How should the other actor labels be understood?

The class also mentions **hacktivists, state-sponsored hackers, corporate or industrial spies, and cyber terrorists**. These labels concern purposes, state support, theft of business intelligence, or terrorism-related contexts. They should not be assigned solely on the basis of nationality, religion, or personal political views. The original file also lacks adequate names and evidence for some incidents, so the checked version does not present those incidents as established facts.

For your current technical learning, it is more important to record separately **what behavior was observed, which assets were affected, and what evidence supports attribution**, rather than choosing an identity label first and forcing all the information to fit it.

---


<a id="en-h061"></a>

<a id="p1-09"></a>

## Part 1 · 9. A complete ethical-hacking test: From permission to confirming the fix

**Study connection — editorial:** A useful assessment closes the loop from an authorized question to limited evidence, a fix, a retest and cleanup. [Chinese explanation](../handouts-zh/part-01.md#h1-09) · [Audited detail](../m01-foundations.md#authorization) · [Source coverage](coverage.md#en-h061). Source section: lines 647–733.

The following is **a teaching workflow assembled from the class concepts**. It is not a claim that the original transcript listed exactly these steps.


<a id="en-h062"></a>

### Step 1: Confirm the objective and permission

First, state the question the test needs to answer.

For example, “Check whether a student account can read only that student's own grades” is much clearer than “See whether the website is secure.”

Then confirm who has authority to approve the test, which assets are included, and which actions are allowed. **Rules of Engagement**, or **ROE**, are an important way to agree on the methods and limits in advance. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/rules_of_engagement))


<a id="en-h063"></a>

### Step 2: Distinguish scope from limitations

**Scope:** What will be tested, and during what time period?
**Limitations:** How may it be tested, what is prohibited, and what conditions must be met?

For example, the scope may be a designated test website and two test accounts. The limitations may prohibit using production data, performing denial-of-service tests, or adding targets without approval.

“This machine is reachable” describes a network condition, not permission.


<a id="en-h064"></a>

### Step 3: Establish a baseline of normal behavior

First, confirm what should happen during normal use.

Student A should see A's grades. Student B should see B's grades. Someone who is not logged in should be denied access.

This gives you a standard for comparison. You should not declare a vulnerability merely because you see a particular screen.


<a id="en-h065"></a>

### Step 4: Form and test a limited security hypothesis

For example:

“The system may return grades based only on the record number in the request, without checking the relationship between that record and the logged-in user.”

Use prearranged test accounts and dummy data to examine this hypothesis within the authorized scope. Server-side authorization must not depend only on the front end hiding a button. ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html))


<a id="en-h066"></a>

### Step 5: Keep evidence that supports the conclusion

Suppose Account A obtains Student B's test grades. Record the account's role, the request and response, the time, and the conditions of the action.

At this point, distinguish:

**Observation:** “A obtained this particular test record belonging to B.”
**Inference:** “Other similar records may also be affected.”
**Not yet verified:** “Whether every record can be read.”

Do not inflate the first statement into the third.

The checked version specifically emphasizes keeping observations, inferences, applicable conditions, and uncertainties distinct in reports.


<a id="en-h067"></a>

### Step 6: Explain the problem rather than merely delivering tool output

At a minimum, a useful finding should tell the reader:

“What rule was expected?”
“What was actually observed?”
“What could be harmed?”
“Why did it happen?”
“Where should it be fixed?”

The class says that a security engineer's value is not simply pressing the scan button. It is helping the customer understand the report and know how to improve. This is an important point throughout the recording.


<a id="en-h068"></a>

### Step 7: Test again after the fix

After the developer fixes the permission check, confirm that Student A can no longer read B's data and can still read A's own data normally.

This distinguishes fixing the security problem from simply breaking the entire feature.

This is where the course's **technical skills**—systems, networking, and programming—connect with its **nontechnical skills**—communication, understanding rules, and industry requirements.


<a id="en-h069"></a>

### Step 8: End the test and clean up

At closure, confirm how test accounts, test data, and temporary settings will be handled. State what remains unverified and stop the testing activity.

**Completion does not mean “I have tried every tool.” It means the agreed questions have been answered adequately, the evidence is understandable, and the responsibilities for what happens next are clear.**


<a id="en-h070"></a>

### What does the classroom example of the overtime consultant actually teach?

The contract requires testing at specified times and places, with an IT employee present. A consultant cannot extend that permission merely by saying they are being diligent—for example, by continuing alone during lunch or reconnecting from home afterward.

The right response is to request and confirm a change when the existing conditions are insufficient. It is not to cross the boundary first and explain the good intention afterward.

However, the material's hat-color analogy should not be treated as a legal conclusion about a specific case. **The actual actions, permission, and applicable rules still require separate analysis.**

---


<a id="en-h071"></a>

<a id="p1-10"></a>

## Part 1 · 10. AI-assisted hacking: What can AI help with, and what new problems can it introduce?

**Study connection — editorial:** Keep generated advice, authorized tool execution and observed results separate; external content is input rather than permission. [Chinese explanation](../handouts-zh/part-01.md#h1-10) · [Audited detail](../m01-foundations.md#ai-assisted-testing) · [Source coverage](coverage.md#en-h071). Source section: lines 734–785.


<a id="en-h072"></a>

### 1. Separate generating text from taking action

AI can explain concepts, organize results, generate code, or suggest test steps. However, there are at least three distinct stages:

**The model produces a suggestion → Software passes the suggestion to a tool → The tool runs in an environment with particular permissions.**

A model writing a command does not establish that the command was executed successfully. Nor does the presence of code establish that the code is correct. The checked version keeps this distinction for the SMTP/Nmap demonstration in the recording: the original text is insufficient to reconstruct a valid command, target, or execution result.


<a id="en-h073"></a>

### 2. What is ShellGPT?

A **shell** is a command environment through which a user interacts with an operating system. A **script** is a text program containing a sequence of operations that can be run.

The **ShellGPT** mentioned in this class corresponds to the third-party project `TheR1D/shell_gpt`. Having “GPT” in the name does not make it an official OpenAI application.

**Correction: It does not always execute immediately after generating a command.** The project documentation includes an interactive shell mode with confirmation and configurations that can call execution functions. Whether execution is automatic depends on the actual mode and settings. ([GitHub](https://github.com/TheR1D/shell_gpt))


<a id="en-h074"></a>

### 3. Prompt injection

The central problem in prompt injection is that input which should not have authority to give instructions influences a model and redirects it away from its intended task. Content in an outside website or file causing this problem is a typical case of indirect prompt injection. ([OWASP Gen AI Security Project](https://genai.owasp.org/llmrisk/llm01-prompt-injection/))

Teaching example: You ask an AI to summarize a security report, but the report contains instructions telling the AI to do another task.

The report should be data to read, not an authority allowed to direct your AI.

Here, a **trust boundary** can be understood directly as:

> Which sources may provide information, and which sources are allowed to ask the system to take action?


<a id="en-h075"></a>

### 4. Why does the problem become larger when tools are connected?

Suppose the AI can only produce text. A misleading instruction might make the summary go off topic.

But if the application connects the AI to tools for deleting files, changing databases, or sending email, and gives those tools excessive permissions, the same kind of input problem may cause a real external action. The impact depends on the application and the capabilities granted to the agent system. ([OWASP Gen AI Security Project](https://genai.owasp.org/llmrisk/llm01-prompt-injection/))

The classroom warning should therefore be understood precisely:

**The danger is not that a sentence has magical power. It is that the system converts untrusted content into an action with real permissions.**


<a id="en-h076"></a>

### 5. How can AI be included in a controlled testing workflow?

For practical work in this class, I suggest first using AI to explain and propose options. Keep human review for actions that change data or systems. Limit tool capabilities and execution privileges. Record the actions that actually ran and their results. Do not treat the content of external documents as permission.

These measures can reduce impact. They do not establish that a single filter can reliably block every prompt injection. ([OWASP Gen AI Security Project](https://genai.owasp.org/llmrisk/llm01-prompt-injection/))

Claims in the class that AI will never replace security workers, or broad claims about employment based on particular occupations or nationalities, are not conclusions this material can prove. More useful learning questions are:

**Which tasks may AI draft? Which judgments require evidence? Which actions must be decided by someone with both authority and responsibility?**

---


<a id="en-h077"></a>

<a id="p1-11"></a>

## Part 1 · 11. Bringing the class together: The abilities you actually need

**Study connection — editorial:** A clear explanation identifies the problem, the evidence, the remaining uncertainty and the next responsible action. [Chinese explanation](../handouts-zh/part-01.md#h1-11) · [Audited detail](../m01-foundations.md#cross-part-synthesis) · [Source coverage](coverage.md#en-h077). Source section: lines 786–803.

Unconfirmed whiteboard content, unclear commands, vendor anecdotes, and claims such as “all hardware and software have backdoors” should not be treated as reliable technical knowledge. In particular, **a normal maintenance or recovery mechanism should not automatically be equated with a secret backdoor that bypasses security controls**.

After this class, you should be able to make three distinctions in a concrete case:

**First, distinguish security goals.** Someone else's grades being seen is a confidentiality problem. Unauthorized grade changes are an integrity problem. An unusable registration service is an availability problem. A forged Academic Affairs notice concerns authenticity. A dispute over a submission with inadequate reliable evidence concerns non-repudiation.

**Second, distinguish the strength of evidence.** A responding host does not prove a vulnerable service. A matching version does not prove exploitability. Successfully reading one test record does not establish that every record can be read.

**Third, distinguish capability from permission.** A tool being able to do something does not mean you may do it. An account being able to access something does not establish authorization. An AI being willing to generate a command does not establish that the command is safe, correct, or approved to run.

Your first learning deliverable can be small. Write one page on whether Student A can read Student B's test grades. Explain the security goal, authorized scope, normal behavior, possible weakness, test method, evidence, and confirmation of the fix.

**The completion criterion is not the number of technical terms you use. It is whether another student can explain, after reading your work, where the problem is, how you know, what remains unknown, and what should happen next.**

---


<a id="en-h078"></a>

## Part 2 — Security Management, Reconnaissance, and Network Scanning

This second recording focuses on connecting security work into a complete process:

**First understand the system and its risks. Then gather information and observe system behavior. Finally, use the evidence to decide how to protect and improve the system.**

The material covers **the second half of Module 1, Module 2: Footprinting and Reconnaissance, and Module 3: Scanning Networks**, in that order. The explanation below follows the same sequence. Statements from class that need correction are marked “Fact-check correction.” The company, website, and account scenarios are teaching examples, not confirmed incidents.


<a id="en-h079"></a>

## Section A: Module 1 — From knowing about attacks to managing security


<a id="en-h080"></a>

<a id="p2-01"></a>

## Part 2 · 1. Cyber Kill Chain, MITRE ATT&CK, and the Diamond Model: Three different analysis tools

**Study connection — editorial:** Use the Kill Chain for progression, ATT&CK for behavior, and the Diamond Model for relationships; unknown attribution stays unknown. [Chinese explanation](../handouts-zh/part-02.md#h2-01) · [Audited detail](../m01-foundations.md#intrusion-models) · [Source coverage](coverage.md#en-h080). Source section: lines 814–878.

All three models help us understand intrusions, but they answer different questions.


<a id="en-h081"></a>

### Cyber Kill Chain: How might an intrusion progress?

“Cyber Kill Chain” is commonly translated into Chinese as “cyberattack chain” or “cyber kill chain.” For now, understand it as **dividing an intrusion into stages so that defenders can identify opportunities to detect or stop it**.

This recording begins partway through the USB-drive example and does not preserve the earlier introduction to the model in full. The seven stages below are a teaching addition that completes the explanation of the model, not a reconstruction of the missing recording.

The typical seven stages are:

**Reconnaissance:** Learn about the target.
**Weaponization:** Prepare tools or content for the intrusion.
**Delivery:** Bring that content to a place where it can reach the target.
**Exploitation:** Use a weakness or a particular behavior to cause an action that should not occur.
**Installation:** Install relevant software in the affected environment or establish conditions for later activity.
**Command and Control, or C2:** Allow a controlled program and its controller to exchange commands or information.
**Actions on Objectives:** Carry out the final goals, such as stealing data, changing systems, or disrupting services. ([CIS](https://www.cisecurity.org/insights/spotlight/ei-isac-cybersecurity-spotlight-cyber-kill-chain))

In the classroom USB scenario, putting a suspicious program on a drive is preparation. Getting the drive into a user's hands is delivery. The user running the program is another important step. Successful installation and remote control each require further conditions.

**Fact-check correction: Inserting an ordinary USB drive does not mean its files automatically run. Running a file does not automatically give someone complete control.** These are separate events, and the conditions between them must not be skipped.

For defenders, the model helps frame questions such as: “Do we block the file when it arrives? Detect it when it runs? Or only notice it after an unusual connection appears?”


<a id="en-h082"></a>

### MITRE ATT&CK: What is the attacker trying to achieve, and by what method?

ATT&CK is a knowledge base that organizes attacker behavior. Remember the three levels introduced in the previous class:

**Tactic:** What goal is this behavior trying to achieve?
**Technique:** What type of method is used to achieve it?
**Procedure:** How was it actually carried out in a particular activity? ([MITRE ATT&CK](https://attack.mitre.org/resources/faq/))

For example, in a hypothetical incident:

Obtaining initial access is the goal. Using phishing messages to persuade a user to act is the method. The actual messages, delivery route, and sequence of actions in that incident are the procedure.

**Fact-check correction: ATT&CK is not an attack workflow that must be followed from left to right.** Attackers may skip, repeat, or interleave activities. It is more accurate to treat it as a language for classifying and analyzing behavior than as a fixed timetable. ([MITRE ATT&CK](https://attack.mitre.org/resources/faq/))

A practical use is:

**Observe behavior → Find the corresponding technique category → Check which records can substantiate it → Identify controls that can address it.**

Writing an ATT&CK identifier in a report does not establish that the detection system can actually detect the behavior. Classification and real defensive effectiveness remain separate issues.


<a id="en-h083"></a>

### Diamond Model: Who used what, through which infrastructure, to affect whom?

The **Diamond Model of Intrusion Analysis** describes an event through four elements:

**Adversary:** Who is carrying out the activity?
**Capability:** What tools, techniques, or resources are being used?
**Infrastructure:** Which servers, domains, or other facilities support the activity?
**Victim:** Which person, organization, or system is affected?

Teaching example: A company discovers an employee's computer connecting to a suspicious domain. You know some of the infrastructure and the affected computer, but you may not know who is behind the activity.

In that situation, write “actor unknown.” Do not see an IP address associated with a country and immediately conclude that the actor is a person from that country.

The three models can be compared as follows:

**The Cyber Kill Chain describes progression. ATT&CK describes goals and methods. The Diamond Model describes relationships among the elements of an event.**

---


<a id="en-h084"></a>

<a id="p2-02"></a>

## Part 2 · 2. Information assurance — Reliable protection, not a verbal promise

**Study connection — editorial:** Assurance joins a security requirement to implemented controls and evidence that supports confidence in them. [Chinese explanation](../handouts-zh/part-02.md#h2-02) · [Audited detail](../m01-foundations.md#layered-controls) · [Source coverage](coverage.md#en-h084). Source section: lines 879–904.

**Information assurance**, or **IA**, concerns protecting information and information systems so that their relevant security properties have dependable support.

Here, assurance does not mean “I promise nothing will ever go wrong.” It means having measures and evidence that support confidence in security. NIST's definition includes availability, integrity, confidentiality, authentication, and non-repudiation. The four items listed in the recording should not be treated as the only complete definition. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/information_assurance))

For example, a company says, “Only HR staff may see salaries.”

That is just a requirement. You still need to know how the system identifies HR staff, how permissions are configured, how access is revoked when someone leaves, and whether the settings have actually been tested.

A **security control** is a measure used to achieve a security goal. It may be technical, procedural, or organizational; it does not have to be a device. The later discussion of defense in depth considers these measures at different layers.


<a id="en-h085"></a>

### The class's ongoing adjustment cycle

The recording uses:

**Protect → Detect → Respond → Predict**

That means protecting first, detecting continuously, responding when a problem is found, and using the available information to estimate which risks need attention next. This is the organizing model used in this class, not a mandatory sequence for every security framework.

Teaching example: A company restricts file permissions, monitors unusual downloads, handles affected accounts when an incident occurs, and then adjusts the rules based on what happened.

“Predict” means making predictions under uncertainty. It does not mean knowing for certain who will break in tomorrow.

---


<a id="en-h086"></a>

<a id="p2-03"></a>

## Part 2 · 3. Defense in depth — Why one checkpoint is not enough

**Study connection — editorial:** Look for complementary controls and shared failure conditions, rather than counting products or checkpoints. [Chinese explanation](../handouts-zh/part-02.md#h2-03) · [Audited detail](../m01-foundations.md#layered-controls) · [Source coverage](coverage.md#en-h086). Source section: lines 905–928.

**Defense in depth** means using complementary controls rather than placing all security on one mechanism.

The class discusses policy, physical security, the perimeter network, the internal network, hosts, applications, and data. These are layers for examining security, not a shopping list of products that must all be purchased.

Consider a company's file server:

A **security policy** states who is responsible and which actions are allowed. A **standard operating procedure**, or **SOP**, explains how the work is done. For example, who approves a contractor's entry to the server room, who escorts them, and how equipment removal is checked.

**Physical security** addresses people's access to equipment. Even excellent account credentials do not remove the need to consider someone carrying away a disk.

The **perimeter** concerns communication between outside and inside networks. For now, understand the **DMZ** mentioned in class as a network zone whose communication with other zones is controlled. A public website may sit in that zone without being allowed unrestricted access to the internal payroll system.

The **internal network** also needs restrictions. Joining the company Wi-Fi should not automatically provide access to every server.

Host logins, application permissions, and data access each still need their own controls. Passing an earlier checkpoint does not justify removing later checks.

The classroom term **mantrap** refers to a controlled passage, such as a two-door access-control arrangement. Actual designs must also consider personal safety and emergency evacuation. Being able to trap someone cannot be the only measure of success.

**Important teaching judgment: The number of checkpoints is not the same as the quality of defense.** If several checkpoints all depend on one stolen administrator account, they may fail together. Ask whether the measures really provide different forms of protection.

---


<a id="en-h087"></a>

<a id="p2-04"></a>

## Part 2 · 4. SID, ACL, and NTFS permissions — Why moving a disk to another computer does not automatically cancel permissions

**Study connection — editorial:** Separate operating-system access checks from the protection needed when someone controls the offline reading environment. [Chinese explanation](../handouts-zh/part-02.md#h2-04) · [Audited detail](../m01-foundations.md#windows-permissions) · [Source coverage](coverage.md#en-h087). Source section: lines 929–965.

This section deserves close attention because the transcript mixes two different questions:

**How does an operating system check permissions?**
**Are the original protections sufficient when an attacker controls the entire disk and the environment used to read it?**


<a id="en-h088"></a>

### Start with the terms

**NTFS** is one of the file systems used by Windows. The important point here is that it can store security information and access-control rules for files.

A **SID**, or **Security Identifier**, identifies Windows security principals such as users and groups. A display name is like a person's name; a SID is closer to the identifier the system uses to recognize that identity. Two accounts both named Alex are not necessarily the same identity. ([Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/ad/how-security-groups-are-used-in-access-control))

An **ACL**, or **Access Control List**, contains control entries. A **DACL**, which concerns allowing and denying access, contains **ACEs**, or **Access Control Entries**.

Think of an ACE as saying, “This SID may read this object,” or “This operation is not allowed.” ([Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/secauthz/access-control-lists))

An **access token** carries security information about the current execution identity and related groups. When checking file access, the system uses the security context and DACL to decide whether the request is allowed. ([Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/secauthz/how-dacls-control-access-to-an-object))

A simplified process is:

**A program requests a file read → The system checks the requesting identity → It compares the request with the file's access rules → It allows or denies access.**


<a id="en-h089"></a>

### Fact-check correction: Failure to display a SID's name does not automatically invalidate permissions

After a disk is connected to another computer, a SID may no longer display as the original account name. But failure to resolve a name does not make the DACL disappear or give everyone permission to read the file.

The real concern is that **file permissions are mainly enforced by the running operating system. Someone who controls the offline reading environment may read the disk without going through the original permission-checking mechanism.**

Appropriate encryption of data at rest addresses a different security boundary. Even if someone obtains the disk, its content remains cryptographically protected as long as they do not also obtain the necessary keys.

The main conclusion is:

**File permissions restrict access within a managed environment. Encryption can provide further protection for data outside that original environment. They are not the same thing.**

---


<a id="en-h090"></a>

<a id="p2-05"></a>

## Part 2 · 5. Risk and risk management — Risk is not just probability

**Study connection — editorial:** Risk decisions need both likelihood and consequences, together with ownership, assumptions and a review trigger. [Chinese explanation](../handouts-zh/part-02.md#h2-05) · [Audited detail](../m01-foundations.md#risk) · [Source coverage](coverage.md#en-h090). Source section: lines 966–1011.

The transcript explains risk as leaving a known problem unfixed and describes high risk as a high probability of occurrence. Both explanations need correction.

**Risk** requires considering the likelihood of an adverse event and its consequences. **Likelihood** is the chance that it occurs; **impact** or **consequence** is what happens if it does. Not knowing about a problem does not mean the risk is absent. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/risk))

Teaching example: One problem frequently causes a small, five-minute inconvenience. Another is rare, but could destroy all your research data. You cannot choose the order of treatment merely by asking which happens more often.

Do not force every risk into a supposedly precise formula, either. When reliable data is unavailable, clear assumptions, evidence, and uncertainty are more useful than multiplying numbers into a score that only looks precise.


<a id="en-h091"></a>

### The classroom risk-management process

**Identify → Assess → Treat → Track → Review**

**Risk identification:** Identify the assets to protect, possible events, and their consequences. It does not mean that identification is unnecessary because the problem is already known.

**Risk assessment:** Judge likelihood and impact, and state what remains unknown.

**Risk treatment:** Decide how to respond.

**Risk tracking:** Follow the problem, the progress of treatment, and changes in conditions.

**Review:** Check whether the original judgment and treatment were effective.


<a id="en-h092"></a>

### Risk treatment is not limited to fixing the problem or leaving it alone

**Reduce or mitigate:** For example, patch a vulnerability or reduce the group of people who can reach a service.

**Avoid:** Stop an unnecessary activity or feature whose risk is too high.

**Accept:** An appropriately authorized and accountable person accepts some remaining risk after understanding the conditions and consequences, with tracking and reassessment conditions in place.

**Transfer or share some consequences:** For example, use a contract or insurance to address particular losses. Insurance does not automatically fix a vulnerability or remove every responsibility.


<a id="en-h093"></a>

### When is “wait until Friday evening to update” reasonable?

The class uses delayed patching to illustrate risk acceptance. The example can be retained, but the decision conditions need to be added.

**Teaching workflow: Confirm that the update applies → Assess exposure from not updating → Assess the risk that the update disrupts service → Test and prepare recovery → Approve the change → Carry it out → Verify the result.**

This is the thinking behind **change management**. It is neither applying every update immediately without conditions nor postponing updates forever out of fear.

For example, if an old service cannot be updated immediately, access may be restricted while replacement is arranged. “We cannot afford a new machine” does not automatically mean “we can do nothing to protect it.”

---


<a id="en-h094"></a>

<a id="p2-06"></a>

## Part 2 · 6. Cyber threat intelligence, SOC, and CVE — Turning information into something actionable

**Study connection — editorial:** Information becomes useful intelligence when it answers a decision question for a responsible recipient. [Chinese explanation](../handouts-zh/part-02.md#h2-06) · [Audited detail](../m01-foundations.md#threat-intelligence) · [Source coverage](coverage.md#en-h094). Source section: lines 1012–1045.

**Cyber threat intelligence** is not collecting every security news story. It is analyzing relevant information so that particular people can make better security decisions.

For example, “A company was breached” is a piece of news.

Questions closer to useful intelligence are: “What behavior enabled entry? Do we use similar systems? Can our existing records reveal the same behavior? Who needs to act?”


<a id="en-h095"></a>

### The four categories used in class

**Strategic intelligence:** Supports longer-term or higher-level decisions. For example, does a particular supply-chain risk justify changing how the company allocates resources?

**Tactical intelligence:** Focuses on actors' TTPs, helping defenders understand their methods and adjust detection and protection.

**Operational intelligence:** Focuses on more specific attack activities, targets, or campaign circumstances.

**Technical intelligence:** Provides specific leads for technical analysis, such as incident-related domains, file hashes, or vulnerability information. These categories overlap. A particular job title is not limited to reading only one type.

A **SOC**, or **Security Operations Center**, coordinates monitoring, analysis, and response. It may be an internal team, an outsourced service, or a combination. Its existence does not make the SOC solely responsible for every aspect of security.

**CVE**, or **Common Vulnerabilities and Exposures**, provides identifiers for publicly known vulnerabilities. A CVE number identifies a weakness. It does not announce that a particular computer has been compromised or completely describe the company's risk.


<a id="en-h096"></a>

### The intelligence life cycle

The checked source organizes the incomplete recording into this teaching workflow:

**Define the question → Gather relevant information → Organize and analyze it → Deliver it to the people who need to decide → Collect feedback and update it.**

For example, a SOC should not merely forward a vulnerability notice to the whole company. It should identify potentially affected devices and send the information to the relevant administrators.

**Fact-check correction: Intelligence does not automatically lose its value because everyone has already heard about it.** Older incidents may still help identify repeated behavior or compare changes.

---


<a id="en-h097"></a>

<a id="p2-07"></a>

## Part 2 · 7. Threat modeling — Explain how things could go wrong before they do

**Study connection — editorial:** Map components, data flows and trust boundaries so that the security rule can be checked where it matters. [Chinese explanation](../handouts-zh/part-02.md#h2-07) · [Audited detail](../m01-foundations.md#incident-response) · [Source coverage](coverage.md#en-h097). Source section: lines 1046–1065.

**Threat modeling** is a structured way to describe what a system needs to protect, how it works, where problems could occur, and how to address them. It is more than listing vulnerability names. ([OWASP Foundation](https://owasp.org/www-community/Threat_Modeling))

The classroom sequence is:

**Identify security objectives → Understand the application → Decompose the application → Identify threats → Identify vulnerabilities.**

For a company's expense-reimbursement system, a security objective might be: “Employees may read only their own reimbursement records, and managers may approve only requests within their area of responsibility.”

Then understand how data moves: the browser submits a claim, the application checks and processes it, the database stores the result, and a manager approves it through another function.

To **decompose** the system is to break it into components, data flows, and permission relationships. A **trust boundary** is a point where security assumptions or permission conditions change. For example, user input entering a server must not be trusted simply because it came from a web form. ([OWASP Foundation](https://owasp.org/www-community/Threat_Modeling))

Then ask specific questions: “Does the server simply trust the employee number entered in the form? Could a student or employee use another person's number?”

**Fact-check correction: Decomposition is not merely deciding which colleague should receive a report.** Identifying component owners matters, but threat modeling also needs to explain how data and permissions cross boundaries.

---


<a id="en-h098"></a>

<a id="p2-08"></a>

## Part 2 · 8. Incident management — Manage impact and evidence when something happens

**Study connection — editorial:** Triage alerts, preserve useful evidence and limit ongoing harm; response activities may need to overlap. [Chinese explanation](../handouts-zh/part-02.md#h2-08) · [Audited detail](../m01-foundations.md#incident-response) · [Source coverage](coverage.md#en-h098). Source section: lines 1066–1105.

First, separate three commonly confused terms.

**Event:** Something that happens in a system, such as a login or the creation of a file.

**Alert:** A signal that a rule or detection mechanism considers worth attention.

**Security incident:** An event that needs to be handled according to its security impact and the organization's procedures. Alerts need assessment; not every alert is a confirmed intrusion. This distinction is needed to understand the classroom discussion of alerts, handling, and response.

An **artifact** may be a log, file, error message, email, or other material left behind. It can support analysis, but calling something an artifact does not automatically make it reliable.

For example, a user saying “my computer is broken” provides little information. Preserving the error screen, time, and actions being performed gives the analysis a firmer basis.


<a id="en-h099"></a>

### Response does not need to wait until every cause has been investigated

The class mentions vulnerability handling, artifact handling, announcements, alerts, incident handling, response, and disclosure. These are related activities, not a fixed schedule that must be completed in that order.

A more practical teaching workflow is:

**Receive a report → Assess severity and scope → Preserve necessary evidence → Appropriately limit ongoing impact → Investigate and address the causes → Restore service → Review.**

For example, if data is actively leaking, you should not insist on completing the entire root-cause investigation before limiting the activity. But you also should not turn off every system without considering data and operational conditions. The response depends on the situation. The NIST incident-response guidance referred to in the source also places response within a broader risk-management context. ([NIST Computer Security Resource Center](https://csrc.nist.gov/pubs/sp/800/61/r3/final))


<a id="en-h100"></a>

### Escalation — Reporting upward or obtaining support

Here, escalation does not mean increasing computer privileges. It means bringing the problem to someone with the necessary capability or decision-making authority.

Teaching example: An engineer recognizes that the problem exceeds their abilities. They should explain what is known, what is unknown, and what help is needed, rather than repeatedly promising that it will be fixed in a moment.

The useful management lessons in this passage are communication, coordination, and obtaining resources—not judging managers by gender or seniority.


<a id="en-h101"></a>

### Disclosure — Reporting and notification may be required before repairs are complete

Reporting to a regulator, notifying affected people, and making a public statement are different actions.

For example, in a personal-data breach covered by GDPR, the thresholds and deadlines for notifying the supervisory authority and notifying individuals differ. Notification to the authority generally involves a requirement linked to 72 hours after awareness, with applicable exceptions. This must not be interpreted as waiting until everything is fixed before notifying anyone. ([European Commission](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/obligations_en))

---


<a id="en-h102"></a>

<a id="p2-09"></a>

## Part 2 · 9. Supervised and unsupervised learning — The difference is in labels, not inherent accuracy

**Study connection — editorial:** Labels define the learning setup, while evaluation establishes performance; false alarms and missed incidents remain separate errors. [Chinese explanation](../handouts-zh/part-02.md#h2-09) · [Audited detail](../m01-foundations.md#machine-learning) · [Source coverage](coverage.md#en-h102). Source section: lines 1106–1128.

**Supervised learning** uses training examples with target information. The target may be a category or a numerical value.

For example, a model receives many emails labeled as spam or legitimate mail. It learns relationships between input features and labels, then predicts labels for new emails. ([Google for Developers](https://developers.google.com/machine-learning/intro-to-ml/supervised))

A teaching workflow is:

**Prepare data and labels → Train the model → Evaluate it on data not used in training → Use it to predict new data → Continue monitoring errors.**

**Unsupervised learning** looks for structure without those target labels. For example, it may group connection behaviors by similarity so that an analyst can examine which groups deserve further attention.

**Fact-check correction: Unsupervised learning is not necessarily inaccurate because its data is messy. Supervised learning is not accurate from the start simply because labels exist.** Labels may be wrong, training data may not represent future conditions, and the model may learn inappropriate relationships.

Security applications must also consider two kinds of error:

**False positive:** Normal activity is classified as abnormal.
**False negative:** An actual abnormality is missed.

Therefore, saying that a system uses AI describes its method. It does not replace an evaluation of its effectiveness.

---


<a id="en-h103"></a>

<a id="p2-10"></a>

## Part 2 · 10. Laws, standards, and certifications — First distinguish what they are

**Study connection — editorial:** Identify the jurisdiction, entity, data, time and applicable obligation before applying a law or standard. [Chinese explanation](../handouts-zh/part-02.md#h2-10) · [Audited detail](../m01-foundations.md#law-and-standards) · [Source coverage](coverage.md#en-h103). Source section: lines 1129–1198.

This section does not ask you to memorize every country's laws. It asks you to understand **which problems different rules address, whom they apply to, and how not to misuse them**.

**Laws and regulations** create obligations when their conditions of application are met.
**Standards** provide requirements or shared practices. Compliance may be required by law, contract, or an organization's commitments.
**Certification** provides evidence of conformity within a particular scope and certification system.

“A standard is not a law” does not mean that standards can always be ignored. Nor does being unregistered or not yet inspected remove applicable obligations.


<a id="en-h104"></a>

### PCI DSS: The Payment Card Industry Data Security Standard

PCI DSS stands for **Payment Card Industry Data Security Standard**.

It concerns the security of payment-card account data and related environments. Its scope is not limited to issuing banks. It may include merchants and service providers that process, transmit, or store the data, or can affect the security of the relevant environment. ([PCI Security Standards Council](https://www.pcisecuritystandards.org/faqs/1092/))

Teaching example: An online store outsourcing payment processing does not make every related responsibility disappear. It needs to understand how the data flows, what the provider is responsible for, and which responsibilities remain with the store.

Conversely, a membership card used only for discounts does not automatically create a payment-card environment merely because it looks like a card.


<a id="en-h105"></a>

### ISO/IEC 27001: An information security management system

ISO/IEC 27001 sets requirements for an **ISMS**, or **Information Security Management System**.

Here, “system” does not mean only computer software. It includes the management scope, risk treatment, responsibilities, implementation, evaluation, and continual improvement. ([ISO](https://www.iso.org/standard/27001))

Teaching example: A company does not merely write that accounts must be canceled when employees leave. Someone must carry out the task, retain records, and check whether the process works.

**Fact-check correction: Buying document templates does not establish compliance with the standard.** The documents must match actual practice. ISO develops standards; it does not directly certify organizations. An employee completing lead-auditor training also does not mean that the company has obtained ISMS certification. ([ISO](https://www.iso.org/certification.html))


<a id="en-h106"></a>

### NIST: Not an American version of ISO certification

NIST provides many standards, frameworks, and guidelines. The classroom simplification that the United States uses NIST while other countries use ISO is inaccurate.

An organization may use both. Whether a particular document is mandatory depends on the applicable rules and the actual situation.


<a id="en-h107"></a>

### HIPAA: U.S. rules concerning particular health information

HIPAA is a U.S. law. Its related rules apply to defined **covered entities** and **business associates**, not automatically to every hospital in the world. ([HHS.gov](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html))

Teaching example: An organization within scope must consider the relevant administrative, physical, and technical safeguards when managing electronic health information. However, invoking HIPAA alone cannot resolve a question about consent to a particular medical procedure in Taiwan. ([HHS.gov](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html))


<a id="en-h108"></a>

### SOX: Not a blanket rule that all email must be kept for seven years

SOX stands for the **Sarbanes–Oxley Act**.

The checked source narrows the classroom seven-year retention claim to SEC requirements for certain audit and review records, which may include relevant electronic communication. **One rule does not require every company to keep every email and all tax data for seven years.** ([SEC](https://www.sec.gov/rules-regulations/2003/01/retention-records-relevant-audits-reviews))

The right practical question is: “Which entity must retain which types of records, for how long, under which rule?”


<a id="en-h109"></a>

### DMCA: The Digital Millennium Copyright Act

The **Digital Millennium Copyright Act**, or DMCA, concerns issues including circumvention of technological protection measures and copyright matters involving online service providers.

**Fact-check correction: It was not the first law to recognize that creative work can be copyrighted without being on paper.** The existence of copyright in digital works should not be attributed entirely to this law. ([U.S. Copyright Office](https://www.copyright.gov/dmca/))


<a id="en-h110"></a>

### GDPR: Rules about personal data and rights have conditions of application

GDPR stands for **General Data Protection Regulation**. It was adopted in 2016, and its main provisions became applicable on **May 25, 2018**. ([EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679))

The right to erasure is not an unconditional right to make any information disappear everywhere in the world. Whether information must be erased depends on scope, the purpose of processing, legal obligations, and other exceptions. ([European Commission](https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en))

Also distinguish **removal from search results, removal by a platform, and removal from the original website**. These are three different outcomes.


<a id="en-h111"></a>

### The UK's DPA and UK GDPR

The **Data Protection Act 2018** and **UK GDPR** are related but distinct parts of the UK framework. The **Data (Use and Access) Act 2025** further amended that framework. This is not simply GDPR under another name. ([ICO](https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/the-data-use-and-access-act-2025-what-does-it-mean-for-organisations/))

When reading rules like these, first identify the country, time period, entity, and type of data. That is more useful than memorizing a claim that one law is the strictest.


<!-- source-derived-text-end -->
