# CEH Course — Complete Merged Plain-English Translation

**Parts 1 and 2 | English edition | Prepared September 21, 2026**

## About this edition

This document combines the full text of the two supplied files in course order. Part 1 comes from `Pasted markdown (2)(20260921-021600).md`; Part 2 comes from `Pasted markdown(20260921-021548).md`.

The supplied files are explanatory course notes based on recordings, rather than raw, timestamped, word-for-word transcripts. Their correction labels, teaching additions, examples, qualifications, and references are retained below. References to “the recording,” “the transcript,” or “the checked source” belong to those original notes. Their references and factual claims have not been independently rechecked for this translation, and missing audio, whiteboard content, commands, or credentials have not been reconstructed.

---

## Part 1 — Course Overview and Ethical-Hacking Foundations

The main purpose of this class is not to learn a few hacking tools. It is to build a complete way of thinking:

**What am I protecting? → How could it go wrong? → How can I test that within the authorized scope? → How can I keep reliable evidence? → How can I make sure the problem is actually fixed?**

The first half of this recording introduces the twenty modules. The second half formally begins **Module 1: Introduction to Ethical Hacking**. The explanation below therefore introduces the concepts in all twenty modules before exploring the definitions and procedures in Module 1. It does not pretend that material from later, unrecorded classes was already covered in this transcript.

The school, company, and bank scenarios below are **teaching examples designed to explain the ideas, not accusations about real incidents**. Necessary corrections are marked wherever the technical explanation differs from the transcript.

---

### 1. What does CEH actually teach?

**CEH stands for Certified Ethical Hacker, a certification provided by EC-Council.** For now, understand ethical hacking as:

> Using methods that an attacker might use, within clearly defined permission and limits, to find security problems and help fix them. ([EC-Council Certification Lookup](https://cert.eccouncil.org/certified-ethical-hacker.html))

Suppose a university is preparing to launch a website where students can check their grades.

Ordinary functional testing asks, “After a student logs in, can they see their own grades?”

Security testing also asks, “Can a student see someone else's grades? Can they turn themselves into a teacher? Will the system accept actions that it should reject?”

Both types of testing examine the same website, but from different angles:

**Functional testing checks whether the things that should happen actually happen. Security testing also checks whether someone can make things happen that should not happen.**

The class repeatedly emphasizes permission because security testing can trigger alerts, add load to a system, or even change data or service conditions. “I want to help” is not the same as having permission.

#### Basic terms you need for the following sections

**Host, client, and server.** A host is a computer or computing environment that participates in a network. A client makes a request; a server provides a service. For example, your browser requests your grades, and the university website receives the request and returns the result. “Server” can mean either the software providing the service or the computer running that software. ([MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/How_does_the_Internet_work))

**IP address, domain name, and DNS.** An IP address is used to locate endpoints and deliver traffic on a network. A domain name is an easier-to-remember name. DNS is a system for looking up information associated with names; one important use is translating a name into an IP address. Think of this as looking up an address. Do not assume that a domain name always refers to one unchanging physical computer. ([MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/How_does_the_Internet_work))

**Port.** A port is a number used in network communication to distinguish service endpoints. It is not a physical USB socket. For example, one computer may provide a website and other services on different ports. An open port means that, under the conditions of that observation, a service is accepting the relevant communication. **It does not automatically mean that the service has a vulnerability.** ([Nmap](https://nmap.org/book/man-port-scanning-basics.html))

**Service.** Here, a service is software that provides a function, such as a website, file access, or email. A **protocol** is a set of rules for exchanging messages. FTP and SMTP, mentioned in the course, concern file transfer and email delivery respectively. They are not operating systems.

With those terms in place, we can look at the twenty course modules.

---

### 2. The twenty modules: What problem does each one address?

#### Module 1: Introduction to Ethical Hacking — Security and permission come first

This chapter starts with several questions: What is security? What is an attack? What is a vulnerability? Who may test a system? How far may the testing go?

These are not pointless preliminaries before using tools. They give the later actions a clear meaning. Without this foundation, you might obtain a scan report without understanding what it proves. This is the main topic of the second half of this recording.

#### Module 2: Footprinting and Reconnaissance

**Footprinting** means collecting and organizing the information a target leaves behind. **Reconnaissance** means investigating a target to understand it. Their coverage overlaps in introductory material; you do not need to memorize them as completely separate activities. The class uses the example of a burglar observing a house beforehand to explain the idea: understand the environment before deciding what to do next.

In an authorized test, the process can be understood as:

**Confirm the target → Gather relevant information → Build a list of assets and their relationships → Check which assets are within the authorized scope.**

For example, a university gives you a list of its production website, test website, and email systems. You first organize their purposes and relationships. You do not start testing every website that happens to contain the university's name.

The result of this step should be an understanding of the environment, not a claim that you have successfully broken in.

#### Module 3: Scanning Networks

Network scanning uses particular probes and their responses to understand the state of hosts, ports, and services. It can be divided into three questions:

“Which targets respond?”
“Which ports are reachable?”
“What services might be behind those ports?” ([Nmap](https://nmap.org/book/man-port-scanning-basics.html))

Teaching example: You perform an authorized check of a web-server VM that you created yourself. You observe that the web service responds, but another service does not.

What you can report is: “From this network location, using this type of probe, I observed these results.”

**Correction: No response does not mean that the host is turned off.** A firewall may be filtering traffic, there may be a routing problem, or that particular probe may not receive a response. Similarly, an open port does not establish that an exploitable vulnerability exists. ([Nmap](https://nmap.org/book/man-port-scanning-basics.html))

#### Module 4: Enumeration

Enumeration means asking a service further questions to obtain specific information about objects or settings, such as accounts, groups, shared resources, or software. How much you can obtain depends on the protocol, your permissions, and the system's configuration.

Think of a building:

Scanning is like finding out that a service desk is open. Enumeration is like asking the desk which departments are present and which resources are available.

A teaching workflow is:

**Discover a service → Understand which queries it supports → Make queries using the permitted level of access → Record the returned information.**

For example, you might check whether a test account can list shared folders that should not be publicly visible. That still does not mean the account can read every file inside those folders.

#### Module 5: Vulnerability Analysis

Vulnerability analysis asks:

> Do the versions, settings, permissions, or behaviors I observed have security problems? Does a suspected problem actually apply to this environment?

The introductory example in class is to identify a software version and compare it with vulnerability information.

A more complete teaching workflow is:

**Gather evidence → Identify possible vulnerabilities → Check the required conditions → Confirm whether this environment meets them → Assess the impact.**

For example, a tool reports that a server may be running a vulnerable version. You still need to check: Was the version identified correctly? Has a patch already been applied? Is the affected feature enabled? Does the tester have the privileges required for the vulnerability to apply?

**A matching version is a lead for investigation, not proof of a successful intrusion.**

#### Module 6: System Hacking — Testing system weaknesses and their impact

This module introduces the exploitation of system weaknesses and the effects they may have. In an authorized test, the point is to confirm a problem using permitted methods, not to take unlimited control of or damage the system.

Suppose a test website has a requirement that students must not gain access to teacher functions. A tester uses a prearranged test account and proves that the student role can enter a teacher-only function. That already provides important evidence.

There is no need to change the entire university's grades just to “prove it more thoroughly.”

Keep this distinction clear: **Proving that a security boundary can be crossed is not the same as increasing the damage.**

#### Module 7: Malware Threats

Malware is software used to perform improper or harmful actions. The class describes malicious content disguised as an update, email attachment, or pirated software so that users install it themselves.

A **Trojan** is defined by its disguise: it appears useful but includes behavior that the user is not meant to know about. A **backdoor** is defined by its function: it provides a route around normal security controls. These terms describe different aspects of software, and both may apply to the same malicious program.

Teaching scenario: An employee installs an unknown “required reader” to open a document. The software then performs unauthorized actions in the background.

Therefore, **an updated system does not make every program that a user later runs trustworthy**.

#### Module 8: Sniffing — Capturing network packets

Sniffing means observing or capturing network communication. For now, think of a **packet** as a unit of data sent over a network. It contains information needed for delivery and part of the content. In this section, the transcript's terms “storm” and “sleeping” should be read, from context, as “packet” and “sniffing.”

Legitimate uses include investigating why a website cannot be reached or why a connection keeps dropping. Watching other people's communication without permission is a different use of the same capability.

The basic process is:

**Choose a place where traffic can be observed → Capture the traffic → Filter the relevant data → Interpret the protocols and content.**

**Correction: Capturing packets does not mean you can see plaintext passwords inside them.** For example, a connection that properly uses HTTPS/TLS protects the transmitted content. Capturing the traffic does not automatically decrypt it. ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html))

#### Module 9: Social Engineering

Social engineering does not directly attack code. It exploits people's trust, habits, pressure, or working procedures to get them to do something they should not do. The classroom example involves tricking users into giving away authentication information.

**Phishing** is one form of social engineering. It uses apparently trustworthy messages to persuade someone to give away information, open content, or take an action.

For example, an employee receives a message claiming to be from the IT department and demanding immediate action on an account problem. The question is not just whether the message looks convincing. It is also whether the company has a trustworthy way to verify it and whether employees can stop and check under time pressure.

From the defender's perspective, ask: “Can a single email make someone change a payment, an account, or access permissions?”

#### Module 10: Denial-of-Service

A **DoS** attack aims to prevent legitimate users from using a service normally. It does not necessarily damage the computer or make it crash. The class illustrates this by describing an attacker consuming the external network bandwidth so that customers cannot reach a website.

Imagine a restaurant whose kitchen is still working, but whose entrance is blocked by a huge number of abnormal requests to join the queue. Real customers cannot get in.

The core process is:

**Consume a limited resource → Leave legitimate requests without enough resources → Reduce service quality or make the service unavailable.**

However, a slow website alone does not prove an attack. A normal peak in course-registration traffic can also exceed system capacity. You need traffic, request, and system evidence; you cannot infer intent from the outcome alone.

#### Module 11: Session Hijacking

A **session** is a mechanism for maintaining the state of an interaction. For example, after you log in to a website, you do not have to type your password again for every page.

For a typical website, the process is:

**Authentication succeeds → A logged-in state is established → The browser holds a related session ID or token → Later requests include it → The server recognizes the session.**

Cookies are a common way for a website and browser to exchange and store this information, but not every cookie is a login credential. ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html))

Session hijacking happens when an attacker uses session-identifying information they have obtained or control to impersonate the original user.

Everyday analogy: Your password is like the identity check at an entrance. A valid session token is like the pass you receive afterward. Someone who obtains the pass may not need to know the password you used at the entrance.

**Correction: Stealing a password, stealing an already authenticated session, and obtaining the AD authentication information mentioned in class should not all be treated as exactly the same mechanism.**

#### Module 12: Evading IDS, Firewalls, and Honeypots — Understanding defenses and their limits

First, distinguish several terms.

A **firewall** uses rules to decide which communication may pass. The classroom remark that some services become reachable after a firewall is turned off refers to this filtering boundary.

An **IDS**, or intrusion detection system, watches for suspicious activity and raises alerts. An **IPS**, or intrusion prevention system, can also try to block the activity. Neither guarantees that every attack will be detected. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/intrusion_detection_system))

A **honeypot** is a system or resource deliberately designed to attract intruders so that their activity can be observed. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/honeypot))

Using the building analogy: a firewall is like access control at the door; an IDS is like an alarm that detects unusual activity and notifies the manager; an IPS can also take blocking action; and a honeypot is a decoy designed to reveal improper access attempts.

This recording only introduces the module's direction. It does not provide a full lesson on evasion techniques.

#### Modules 13 and 14: Web Servers and Web Applications — Do not confuse these layers

A **web server** handles website communication, content delivery, and related tasks. From context, the products mentioned in class include IIS, Apache, and nginx. The transcript's “iOS” in the web-server section may be a speech-recognition error for IIS, rather than the mobile operating system iOS.

A **web application** handles business logic, such as logging in, registering for courses, calculating credits, and displaying grades.

A teaching model of the relationship is:

**The browser sends a request → The web service receives it → The application decides what to do → It reads or writes the database when needed → It returns a result.**

Module 13 focuses on server software, deployment, and configuration. Module 14 focuses more on application permissions, inputs, and workflows. Problems can occur in either layer.

The class uses the example of entering `10000.01` into a quantity field that expects an integer. The point is not that every program will crash. It is that a program cannot simply assume users will always behave as expected.

A more specific security problem is a student who logs in normally but is allowed to read a grade record without the application checking their permission for that record. **Successfully logging in and being authorized for every subsequent action are two different things.** ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html))

#### Module 15: SQL Injection

**SQL** is a language for interacting with relational databases. The central problem in SQL injection is:

> User input that should be treated as data becomes mixed into the structure of a command.

For example, a website only intends to look up one student. However, the program constructs the database command by unsafely joining strings, so the input changes the meaning of the command itself. ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html))

The key process is:

**Receive input → Build a database command unsafely → The database interprets part of the input as a command → An unintended query or operation is executed.**

One major defense is a **parameterized query**: define the command structure first, then pass the input to the database as data parameters instead of freely inserting it into the command. This separates commands from data; it is not merely a matter of deleting unusual symbols. ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html))

**Correction: SQL injection can be serious, but you cannot call it the most serious vulnerability in every case without considering the permissions, data, and environment.**

#### Module 16: Hacking Wireless Networks — Wireless network security

This module covers wireless standards, authentication, and encryption mechanisms. The source only previews a discussion of mechanisms that should not be used. It does not examine each one in this recording.

First, separate two questions:

**Authentication** asks, “Who may join or use this network?”
**Encryption** asks, “How is the transmitted content protected from people who cannot legitimately read it?”

Teaching example: A café's Wi-Fi may give visitors internet access. Successfully connecting should not also give a visitor administrative access to the café's checkout system.

The point is that **connecting to a network, reading its communication, and operating its internal systems are different levels of capability**.

#### Module 17: Hacking Mobile Platforms — Mobile platform security

The mobile platforms previewed in class include Android and iOS. This section does not fully develop the attack and defense processes for either platform.

As a starting point, think about the data and permissions on a phone. For example, does an app that only displays campus announcements have a reason to request access to all your contacts?

During a review, ask: What is the app supposed to do? Which permissions does it receive? Where does it store data? Where does it send that data?

These questions move mobile security beyond simply asking whether a phone has a virus. They turn it into an examination of data flows and permissions.

#### Module 18: IoT, OT, and ICS — From information systems to the physical world

In this class, **IoT**, the Internet of Things, refers to network-connected devices such as sensors and network cameras. **OT**, operational technology, includes systems that monitor or control physical equipment and processes. **ICS**, industrial control systems, is an important area within OT. ([NIST Computer Security Resource Center](https://csrc.nist.gov/pubs/sp/800/82/r3/final))

Teaching example: An ordinary website failure may prevent people from looking up information. A control-system failure may stop a conveyor belt, disrupt temperature control, or affect physical safety.

In these environments, you cannot ask only whether a patch can be installed. You must also consider how patching, restarting, or testing could affect reliability and safety. This is why you cannot directly apply ordinary laboratory procedures to an operating production line. ([NIST Computer Security Resource Center](https://csrc.nist.gov/pubs/sp/800/82/r3/final))

#### Module 19: Cloud Computing

Cloud computing is a model for obtaining configurable computing resources over a network when needed. Resources can be provided and released relatively quickly. Do not reduce the idea to “someone else's computer”: shared resources, on-demand allocation, and how those resources are managed are also important. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/cloud_computing))

Teaching example: A research laboratory temporarily needs a pool of computing resources. It releases them when the work is complete rather than first buying every physical machine.

From a security perspective, you still need to ask: Who may create resources? Who may read the data? Which settings could expose content that was supposed to remain private?

The original recording only previews cloud concepts and characteristics. It does not fully explain the different service models.

#### Module 20: Cryptography

The class emphasizes that this CEH course mainly teaches the use of cryptographic technology. It does not expect everyone to invent new algorithms.

First, learn a few basic concepts:

**Plaintext** is the original, understandable data. **Ciphertext** is data transformed by encryption. A **key** is an important parameter that controls a cryptographic operation. **Encryption** protects data, while **decryption** recovers the corresponding data. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/encryption))

**Asymmetric cryptography** uses a related public key and private key. For example, a private key can create a digital signature, and the corresponding public key can verify it. The private key must be protected; the public key can be given to people who need to verify signatures. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/asymmetric_key_cryptography))

As the following sections explain, **encryption, hashing, and digital signatures solve different problems. They cannot simply replace one another.**

---

### 3. How do the classroom VMs, Parrot, and Windows Server fit together?

#### 1. A VM is a virtual computer, not another hacking technique

A **virtual machine**, or VM, is a computing environment provided through virtualization. A **hypervisor** manages the relationship between guest operating systems and the underlying hardware resources. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/virtual_machine))

For example, your physical computer may run Ubuntu, while a virtualization platform lets you create a Windows VM. The Ubuntu environment is the host side; Windows inside the VM is the guest operating system.

**Parrot OS is a Linux distribution. A Parrot VM is a virtual machine with Parrot OS installed.** The official documentation describes Parrot as a Debian-based distribution that provides security tools and a working environment. ([Parrot Security](https://parrotsec.org/docs/))

**Correction: The transcript's “para/parent virtual machine” most likely means Parrot VM. It should not be interpreted as the separate technical term “paravirtualization.”** Nor should Parrot be defined as a stripped-down version of Kali with exactly one-fifth as many tools.

#### 2. Lab machines can usually run alongside one another; they do not all need to run inside Parrot

The following is **a teaching example of a configuration, not a reconstruction of the missing classroom whiteboard**:

One physical computer provides the virtualization environment. It contains a Parrot testing VM and one or more Windows or Linux target VMs. They are separate virtual computers that communicate over a designated laboratory network.

In other words, Parrot is one participant in the lab. It is not a place where all the target VMs must live.

The whiteboard is missing from this transcript, so the exact service roles of each Windows Server, the IP-address plan, and whether nested virtualization was used cannot be reliably reconstructed.

#### 3. What are AD and a domain controller?

**Active Directory Domain Services**, or **AD DS**, is a directory service that centrally stores and manages information about users, computers, and resources. It also integrates authentication and access control. A **domain controller** is an important server role that provides these domain services. ([Microsoft Learn](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview))

Teaching example: A company has many computers. Administrators do not want each computer to maintain a separate, unrelated set of employee accounts, so they use centralized directory and account management.

An AD domain is part of an administrative and identity architecture. Do not treat it as identical to a website's domain name just because both use the word “domain.”

#### 4. What counts as a ready-to-use laboratory?

For a course like this, I suggest defining “the lab is ready” as follows: You know each machine's role, understand which communication is allowed, use test data, and have a way to return the environment to a repeatable starting state.

Success does not mean installing as many tools as possible. Nor does it mean simply being able to connect to outside systems.

The six-month online lab access mentioned in class still needs to be checked against the actual purchased package and activation records. The transcript alone cannot establish your personal expiration date.

#### 5. Separate examination facts from classroom advice

At the time of the source's check, the official CEH knowledge-exam information was **exam code 312-50, 125 questions, and 4 hours**. The passing threshold depends on the exam form; the official range given was **60%–85%**. Therefore, the classroom statement that “about 75% is enough to pass” should not be treated as a fixed rule. ([EC-Council Certification Lookup](https://cert.eccouncil.org/certified-ethical-hacker.html))

The checked version also addresses claims such as “you must stay for more than an hour to avoid an investigation,” “the answer with the most votes must be right,” and “you can get an unconditional refund after completing the course.” It marks these, respectively, as unsupported by official rules, an invalid inference, or a claim that ignores applicable conditions. They are not suitable preparation strategies.

The classroom question about a **64-bit block and three DES keys, each with 56 effective key bits**, identifies the historical three-key TDEA/Triple DES algorithm. **Recognizing an algorithm in an exam question does not mean it should be used to design a new system today.** NIST withdrew the related recommendation on **January 1, 2024**. ([NIST Computer Security Resource Center](https://csrc.nist.gov/pubs/sp/800/67/r2/final))

---

### 4. The core of Module 1: Five elements of information security

The class introduces **confidentiality, integrity, availability, authenticity, and non-repudiation**, in that order. These are security goals, not five separate products.

We will use the same university grade system to understand all five.

#### 1. Confidentiality — People who are not allowed to see information must not see it

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

#### 2. Integrity — Data must not be improperly changed or destroyed

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

#### 3. Availability — Information or services must be usable when needed, under reasonable conditions

Availability emphasizes timely and reliable access to information or services for legitimate users. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/availability))

For example, the course-registration server may be powered on, but each operation takes so long that students cannot complete registration before the deadline. That is still an availability problem.

The class mentions **clusters** and **failover**: multiple nodes and a takeover mechanism can reduce the interruption caused by the failure of a single machine.

A teaching workflow is:

**Continuously check whether the service works → Detect a failure → Have another available node take over → Confirm that users can actually complete their work.**

The last step matters. You cannot merely check whether the backup machine's lights are on. You must verify the actual service capability of the data, network, and application.

**Correction: Encryption consumes resources, but not every encryption method makes an entire file completely unreadable for the whole operation.** The classroom example warns that processing performance can affect availability. It does not describe a fixed behavior of every system.

#### 4. Authenticity — Is the source or identity really what it claims to be?

Authenticity concerns whether a message, entity, or source is genuine and can be verified. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/authenticity))

The classroom example asks, “Did HR really publish this leave policy?”

A university example would be receiving a notice labeled “Academic Affairs Office,” complete with the university logo and an administrator's name. Looking official does not prove that it came from that office.

Distinguish these questions:

“Has the document's content remained unchanged?” is a question about integrity.
“Did the document really come from the Academic Affairs Office?” is a question about authenticity.

There is a further distinction: **A genuine source does not guarantee correct content.** The Academic Affairs Office may truly have issued a notice that contains a wrong date. Verifying the source cannot replace checking the facts.

#### 5. Non-repudiation — Evidence that a third party can use to assess an action

Non-repudiation does not make it impossible for someone to deny something. It means retaining enough evidence for a third party to assess whether a claimed source or action is established. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/non_repudiation))

For example, a teacher submits final grades, and a dispute arises later. The system needs reliable evidence to clarify what was submitted, which identity was used, and what processing occurred. Saying “your name was on the screen” is not enough.

The class uses a dispute over a bank email to illustrate proving origin and content. However, a printed name, a fingerprint code, or a Message-ID should not be treated as complete digital verification.

#### How does a digital signature work?

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

### 5. Attack, vulnerability, exploit, and compromise: Four terms that are not interchangeable

#### Attack — An activity that attempts to violate security goals

The class points out that attacks are not limited to crashing servers. They also include stealing data and observing communication without permission.

However, do not go to the opposite extreme and call every use of a probing tool a malicious attack. The same observation or testing method may be used in authorized testing, troubleshooting, or unauthorized activity. You must consider the purpose, permission, and actual behavior.

#### Vulnerability — A weakness that may be exploited

Vulnerabilities are not limited to code. They may exist in a system's design, configuration, processes, or controls. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/vulnerability))

Example: A grade website checks that a student is logged in but does not check whether the student is allowed to read the particular grade record requested.

The vulnerability exists even if nobody has exploited it yet.

#### Exploit — A way of turning a weakness into an effect

In the example above, someone takes advantage of the missing permission check to make a read request that the system should reject. That is exploiting a vulnerability. “Exploit” can also mean the program or method used to take advantage of a weakness.

Therefore, discovering a vulnerability and successfully exploiting it are different conclusions.

#### Compromise — A state in which security has been affected

For example, if someone without permission has read Student B's grades, the confidentiality of that data has been compromised.

**Correction: A compromise does not require an attacker to first turn off antivirus software or a firewall.** Unauthorized disclosure, modification, or use of sensitive information may already constitute a compromise. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/compromise))

A simple way to remember the three central terms is:

**A vulnerability is the weakness. An exploit is a way to use the weakness. A compromise is the resulting state in which security has been violated.**

#### Teaching addition: Threat and risk

A **threat** is a circumstance or event that may cause an adverse effect. **Risk** requires considering both the likelihood of an event and its impact. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/threat))

For example, the same configuration error in a disposable, offline practice VM and in an internet-facing system containing the whole university's grades should not receive the same priority merely because the vulnerability has the same name.

This is why a security report cannot just list vulnerability names. It also needs to explain the environment and consequences.

---

### 6. Where do vulnerabilities come from, and what does TTP mean?

#### 1. Misconfiguration

Software may provide security features, but the user may configure permissions, networking, or services incorrectly.

The class uses turning off the Windows firewall as an example. More precisely, **turning off a firewall does not create a running network service out of nothing. It may make a service reachable when that service was already running but its traffic was blocked.**

Ask three separate questions:

**Is a program listening? Is it reachable over the network? Once reached, does it have an exploitable problem?**

These questions do not mean the same thing.

#### 2. Insecure design

A problem may have existed since the design stage, rather than arising from a missing patch later.

For example, a designer assumes that anyone who can log in is a trusted insider and therefore fails to create suitable permission rules for different users and data.

A longer password alone cannot fix this problem. The system's model of who may do what was incomplete from the beginning. ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html))

#### 3. Inherent technology weaknesses

**“Inherent” means built into the nature of something. It does not mean “inherited.”**

Some technologies have security limitations in their original design. Re-enabling an old feature for compatibility may also expose an old problem again. However, this does not justify saying that every compatibility feature is unsafe.

Learn to ask: “What does this feature provide? What limitations does it introduce? Does it still meet our current needs?”

#### 4. Ignoring users and endpoints

In this context, an **endpoint** is a device such as an employee's computer. The class warns against protecting only the servers in the machine room while assuming that an employee's compromised computer can simply be reinstalled and forgotten.

Teaching example: After gaining control of an employee's computer, an attacker may try to use resources that the computer can access.

Activity that starts from an established position and extends to other systems illustrates **lateral movement**. Whether it succeeds still depends on permissions, authentication, and network segmentation. One infected computer does not automatically mean that every computer will be infected.

#### 5. How should we read the classroom “conditions for attack success”?

The transcript discusses motivation, methods, and weaknesses, but the formula itself was not recognized clearly enough to reconstruct it as a precise scientific law.

The useful idea is that desire alone does not make an attack work. There must be conditions and a path that can produce the effect. The classroom example is that a camera without a motor cannot be made to physically rotate through a remote command. Technical actions are also limited by physical capabilities.

Failing to find a software vulnerability does not establish that the whole system has no other weaknesses. Accounts, procedures, and human interactions may still need to be examined.

#### 6. TTP — Describing behavior at three levels

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

### 7. Five attack categories: Use categories to ask the right defensive questions

The class groups attacks as **passive, active, close-in, insider, and distribution** attacks. These categories mix several viewpoints, so one incident may belong to more than one category. They are not five mutually exclusive boxes.

#### Passive attack

The central idea is observation without changing the system or data, such as listening to communication without permission. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/passive_attack))

**Correction: “Not connecting to the target” is not an adequate definition.** You need to examine whether the activity changes data, state, or communication.

Teaching example: Someone gains an opportunity to observe communication but does not alter what they see. The defensive questions are: “What information could be exposed? Is the content protected?”

#### Active attack

The central idea is active intervention, such as modifying, forging, or disrupting systems or communication, rather than simply observing them. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/active_attack))

For example, an attacker tries to change grades rather than merely read them, or disrupts a website rather than simply observing its traffic.

**Correction: Failing to establish an ordinary connection does not rule out an active attack.** Classification cannot depend only on whether a connection succeeded.

#### Close-in attack

This category focuses on opportunities created by getting physically close to people, equipment, or a location.

In the classroom example, a contractor enters the server room, but the escort leaves and may even leave the door open for convenience. Everyday behavior can therefore defeat the intended access controls.

Defenders should ask: What can visitors reach? Who must escort them? How is their departure confirmed when the job is complete?

Physical proximity does not guarantee a successful intrusion. It creates a set of conditions that need their own controls.

#### Insider attack

This category concerns the misuse of existing trust and access. The class notes that insiders may already have accounts and know the company's environment.

For example, an employee is allowed to view some customer records for work but uses those records for an unauthorized purpose.

Remember: **A legitimate account does not make every use of it legitimate or compliant. Being on the internal network does not justify having every permission.**

On the other hand, the name “insider attack” alone does not establish that it is always more serious than an external attack.

#### Distribution attack — Attacks through delivery or the supply chain

The classroom description involves tampering with hardware, software, or its delivery process, so that users encounter the problem when they receive the product. In modern analysis, this can be connected with **supply chain compromise**. ([MITRE ATT&CK](https://attack.mitre.org/techniques/T1195/))

Teaching example: An otherwise legitimate software company has its update-release process compromised, causing customers to receive a modified update.

**Correction: The supplier is not necessarily acting maliciously; it may also be a victim.** A distribution attack is not the same as distributed denial-of-service. The names are similar, but they describe different things.

---

### 8. White hats, black hats, gray hats, and red and blue teams

These labels are easy to remember, but they can lead people to mistake a role name for proof of skill or proof that an action is justified.

In this class, a **white hat** is someone who has permission and performs security testing within scope. A **black hat** describes someone who maliciously breaks into systems or abuses security weaknesses.

The material describes a **gray hat** as someone who sometimes works within permission and sometimes crosses the boundary. This is an introductory label, not a legal category that can replace analysis of the actual behavior.

The class uses **script kiddie** for someone who mainly runs ready-made tools without understanding the underlying principles well. The point is limited understanding, not age. Using existing tools is not itself a problem; the question is whether you can explain the action, result, and risks.

Other colors should be read in the context of this particular material:

**Blue hat:** In this course, an outside expert temporarily invited to help with testing.
**Red hat:** In this course, someone who attacks black hats in return.
**Green hat:** In this course, a beginner who is willing to learn.

These are not uniformly or rigorously standardized professional qualifications. In particular, calling someone a red hat does not automatically authorize them to attack another person's system.

#### Red teams and blue teams are not the same as red hats and blue hats

In an authorized exercise, the **red team** simulates the attacking side, while the **blue team** defends, observes, and responds. The class introduces this distinction through “information warfare,” but does not develop a complete theoretical framework for information warfare.

Teaching example: The red team tests an agreed attack path. The blue team checks whether it detects the activity, can assess the impact, and can stop or handle it.

The useful learning questions are: “Which steps succeeded? Which defenses failed? How can we improve?” The point is not whose title sounds more impressive.

#### How should the other actor labels be understood?

The class also mentions **hacktivists, state-sponsored hackers, corporate or industrial spies, and cyber terrorists**. These labels concern purposes, state support, theft of business intelligence, or terrorism-related contexts. They should not be assigned solely on the basis of nationality, religion, or personal political views. The original file also lacks adequate names and evidence for some incidents, so the checked version does not present those incidents as established facts.

For your current technical learning, it is more important to record separately **what behavior was observed, which assets were affected, and what evidence supports attribution**, rather than choosing an identity label first and forcing all the information to fit it.

---

### 9. A complete ethical-hacking test: From permission to confirming the fix

The following is **a teaching workflow assembled from the class concepts**. It is not a claim that the original transcript listed exactly these steps.

#### Step 1: Confirm the objective and permission

First, state the question the test needs to answer.

For example, “Check whether a student account can read only that student's own grades” is much clearer than “See whether the website is secure.”

Then confirm who has authority to approve the test, which assets are included, and which actions are allowed. **Rules of Engagement**, or **ROE**, are an important way to agree on the methods and limits in advance. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/rules_of_engagement))

#### Step 2: Distinguish scope from limitations

**Scope:** What will be tested, and during what time period?
**Limitations:** How may it be tested, what is prohibited, and what conditions must be met?

For example, the scope may be a designated test website and two test accounts. The limitations may prohibit using production data, performing denial-of-service tests, or adding targets without approval.

“This machine is reachable” describes a network condition, not permission.

#### Step 3: Establish a baseline of normal behavior

First, confirm what should happen during normal use.

Student A should see A's grades. Student B should see B's grades. Someone who is not logged in should be denied access.

This gives you a standard for comparison. You should not declare a vulnerability merely because you see a particular screen.

#### Step 4: Form and test a limited security hypothesis

For example:

“The system may return grades based only on the record number in the request, without checking the relationship between that record and the logged-in user.”

Use prearranged test accounts and dummy data to examine this hypothesis within the authorized scope. Server-side authorization must not depend only on the front end hiding a button. ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html))

#### Step 5: Keep evidence that supports the conclusion

Suppose Account A obtains Student B's test grades. Record the account's role, the request and response, the time, and the conditions of the action.

At this point, distinguish:

**Observation:** “A obtained this particular test record belonging to B.”
**Inference:** “Other similar records may also be affected.”
**Not yet verified:** “Whether every record can be read.”

Do not inflate the first statement into the third.

The checked version specifically emphasizes keeping observations, inferences, applicable conditions, and uncertainties distinct in reports.

#### Step 6: Explain the problem rather than merely delivering tool output

At a minimum, a useful finding should tell the reader:

“What rule was expected?”
“What was actually observed?”
“What could be harmed?”
“Why did it happen?”
“Where should it be fixed?”

The class says that a security engineer's value is not simply pressing the scan button. It is helping the customer understand the report and know how to improve. This is an important point throughout the recording.

#### Step 7: Test again after the fix

After the developer fixes the permission check, confirm that Student A can no longer read B's data and can still read A's own data normally.

This distinguishes fixing the security problem from simply breaking the entire feature.

This is where the course's **technical skills**—systems, networking, and programming—connect with its **nontechnical skills**—communication, understanding rules, and industry requirements.

#### Step 8: End the test and clean up

At closure, confirm how test accounts, test data, and temporary settings will be handled. State what remains unverified and stop the testing activity.

**Completion does not mean “I have tried every tool.” It means the agreed questions have been answered adequately, the evidence is understandable, and the responsibilities for what happens next are clear.**

#### What does the classroom example of the overtime consultant actually teach?

The contract requires testing at specified times and places, with an IT employee present. A consultant cannot extend that permission merely by saying they are being diligent—for example, by continuing alone during lunch or reconnecting from home afterward.

The right response is to request and confirm a change when the existing conditions are insufficient. It is not to cross the boundary first and explain the good intention afterward.

However, the material's hat-color analogy should not be treated as a legal conclusion about a specific case. **The actual actions, permission, and applicable rules still require separate analysis.**

---

### 10. AI-assisted hacking: What can AI help with, and what new problems can it introduce?

#### 1. Separate generating text from taking action

AI can explain concepts, organize results, generate code, or suggest test steps. However, there are at least three distinct stages:

**The model produces a suggestion → Software passes the suggestion to a tool → The tool runs in an environment with particular permissions.**

A model writing a command does not establish that the command was executed successfully. Nor does the presence of code establish that the code is correct. The checked version keeps this distinction for the SMTP/Nmap demonstration in the recording: the original text is insufficient to reconstruct a valid command, target, or execution result.

#### 2. What is ShellGPT?

A **shell** is a command environment through which a user interacts with an operating system. A **script** is a text program containing a sequence of operations that can be run.

The **ShellGPT** mentioned in this class corresponds to the third-party project `TheR1D/shell_gpt`. Having “GPT” in the name does not make it an official OpenAI application.

**Correction: It does not always execute immediately after generating a command.** The project documentation includes an interactive shell mode with confirmation and configurations that can call execution functions. Whether execution is automatic depends on the actual mode and settings. ([GitHub](https://github.com/TheR1D/shell_gpt))

#### 3. Prompt injection

The central problem in prompt injection is that input which should not have authority to give instructions influences a model and redirects it away from its intended task. Content in an outside website or file causing this problem is a typical case of indirect prompt injection. ([OWASP Gen AI Security Project](https://genai.owasp.org/llmrisk/llm01-prompt-injection/))

Teaching example: You ask an AI to summarize a security report, but the report contains instructions telling the AI to do another task.

The report should be data to read, not an authority allowed to direct your AI.

Here, a **trust boundary** can be understood directly as:

> Which sources may provide information, and which sources are allowed to ask the system to take action?

#### 4. Why does the problem become larger when tools are connected?

Suppose the AI can only produce text. A misleading instruction might make the summary go off topic.

But if the application connects the AI to tools for deleting files, changing databases, or sending email, and gives those tools excessive permissions, the same kind of input problem may cause a real external action. The impact depends on the application and the capabilities granted to the agent system. ([OWASP Gen AI Security Project](https://genai.owasp.org/llmrisk/llm01-prompt-injection/))

The classroom warning should therefore be understood precisely:

**The danger is not that a sentence has magical power. It is that the system converts untrusted content into an action with real permissions.**

#### 5. How can AI be included in a controlled testing workflow?

For practical work in this class, I suggest first using AI to explain and propose options. Keep human review for actions that change data or systems. Limit tool capabilities and execution privileges. Record the actions that actually ran and their results. Do not treat the content of external documents as permission.

These measures can reduce impact. They do not establish that a single filter can reliably block every prompt injection. ([OWASP Gen AI Security Project](https://genai.owasp.org/llmrisk/llm01-prompt-injection/))

Claims in the class that AI will never replace security workers, or broad claims about employment based on particular occupations or nationalities, are not conclusions this material can prove. More useful learning questions are:

**Which tasks may AI draft? Which judgments require evidence? Which actions must be decided by someone with both authority and responsibility?**

---

### 11. Bringing the class together: The abilities you actually need

Unconfirmed whiteboard content, unclear commands, vendor anecdotes, and claims such as “all hardware and software have backdoors” should not be treated as reliable technical knowledge. In particular, **a normal maintenance or recovery mechanism should not automatically be equated with a secret backdoor that bypasses security controls**.

After this class, you should be able to make three distinctions in a concrete case:

**First, distinguish security goals.** Someone else's grades being seen is a confidentiality problem. Unauthorized grade changes are an integrity problem. An unusable registration service is an availability problem. A forged Academic Affairs notice concerns authenticity. A dispute over a submission with inadequate reliable evidence concerns non-repudiation.

**Second, distinguish the strength of evidence.** A responding host does not prove a vulnerable service. A matching version does not prove exploitability. Successfully reading one test record does not establish that every record can be read.

**Third, distinguish capability from permission.** A tool being able to do something does not mean you may do it. An account being able to access something does not establish authorization. An AI being willing to generate a command does not establish that the command is safe, correct, or approved to run.

Your first learning deliverable can be small. Write one page on whether Student A can read Student B's test grades. Explain the security goal, authorized scope, normal behavior, possible weakness, test method, evidence, and confirmation of the fix.

**The completion criterion is not the number of technical terms you use. It is whether another student can explain, after reading your work, where the problem is, how you know, what remains unknown, and what should happen next.**

---

## Part 2 — Security Management, Reconnaissance, and Network Scanning

This second recording focuses on connecting security work into a complete process:

**First understand the system and its risks. Then gather information and observe system behavior. Finally, use the evidence to decide how to protect and improve the system.**

The material covers **the second half of Module 1, Module 2: Footprinting and Reconnaissance, and Module 3: Scanning Networks**, in that order. The explanation below follows the same sequence. Statements from class that need correction are marked “Fact-check correction.” The company, website, and account scenarios are teaching examples, not confirmed incidents.

### Section A: Module 1 — From knowing about attacks to managing security

#### 1. Cyber Kill Chain, MITRE ATT&CK, and the Diamond Model: Three different analysis tools

All three models help us understand intrusions, but they answer different questions.

##### Cyber Kill Chain: How might an intrusion progress?

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

##### MITRE ATT&CK: What is the attacker trying to achieve, and by what method?

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

##### Diamond Model: Who used what, through which infrastructure, to affect whom?

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

#### 2. Information assurance — Reliable protection, not a verbal promise

**Information assurance**, or **IA**, concerns protecting information and information systems so that their relevant security properties have dependable support.

Here, assurance does not mean “I promise nothing will ever go wrong.” It means having measures and evidence that support confidence in security. NIST's definition includes availability, integrity, confidentiality, authentication, and non-repudiation. The four items listed in the recording should not be treated as the only complete definition. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/information_assurance))

For example, a company says, “Only HR staff may see salaries.”

That is just a requirement. You still need to know how the system identifies HR staff, how permissions are configured, how access is revoked when someone leaves, and whether the settings have actually been tested.

A **security control** is a measure used to achieve a security goal. It may be technical, procedural, or organizational; it does not have to be a device. The later discussion of defense in depth considers these measures at different layers.

##### The class's ongoing adjustment cycle

The recording uses:

**Protect → Detect → Respond → Predict**

That means protecting first, detecting continuously, responding when a problem is found, and using the available information to estimate which risks need attention next. This is the organizing model used in this class, not a mandatory sequence for every security framework.

Teaching example: A company restricts file permissions, monitors unusual downloads, handles affected accounts when an incident occurs, and then adjusts the rules based on what happened.

“Predict” means making predictions under uncertainty. It does not mean knowing for certain who will break in tomorrow.

---

#### 3. Defense in depth — Why one checkpoint is not enough

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

#### 4. SID, ACL, and NTFS permissions — Why moving a disk to another computer does not automatically cancel permissions

This section deserves close attention because the transcript mixes two different questions:

**How does an operating system check permissions?**
**Are the original protections sufficient when an attacker controls the entire disk and the environment used to read it?**

##### Start with the terms

**NTFS** is one of the file systems used by Windows. The important point here is that it can store security information and access-control rules for files.

A **SID**, or **Security Identifier**, identifies Windows security principals such as users and groups. A display name is like a person's name; a SID is closer to the identifier the system uses to recognize that identity. Two accounts both named Alex are not necessarily the same identity. ([Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/ad/how-security-groups-are-used-in-access-control))

An **ACL**, or **Access Control List**, contains control entries. A **DACL**, which concerns allowing and denying access, contains **ACEs**, or **Access Control Entries**.

Think of an ACE as saying, “This SID may read this object,” or “This operation is not allowed.” ([Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/secauthz/access-control-lists))

An **access token** carries security information about the current execution identity and related groups. When checking file access, the system uses the security context and DACL to decide whether the request is allowed. ([Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/secauthz/how-dacls-control-access-to-an-object))

A simplified process is:

**A program requests a file read → The system checks the requesting identity → It compares the request with the file's access rules → It allows or denies access.**

##### Fact-check correction: Failure to display a SID's name does not automatically invalidate permissions

After a disk is connected to another computer, a SID may no longer display as the original account name. But failure to resolve a name does not make the DACL disappear or give everyone permission to read the file.

The real concern is that **file permissions are mainly enforced by the running operating system. Someone who controls the offline reading environment may read the disk without going through the original permission-checking mechanism.**

Appropriate encryption of data at rest addresses a different security boundary. Even if someone obtains the disk, its content remains cryptographically protected as long as they do not also obtain the necessary keys.

The main conclusion is:

**File permissions restrict access within a managed environment. Encryption can provide further protection for data outside that original environment. They are not the same thing.**

---

#### 5. Risk and risk management — Risk is not just probability

The transcript explains risk as leaving a known problem unfixed and describes high risk as a high probability of occurrence. Both explanations need correction.

**Risk** requires considering the likelihood of an adverse event and its consequences. **Likelihood** is the chance that it occurs; **impact** or **consequence** is what happens if it does. Not knowing about a problem does not mean the risk is absent. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/risk))

Teaching example: One problem frequently causes a small, five-minute inconvenience. Another is rare, but could destroy all your research data. You cannot choose the order of treatment merely by asking which happens more often.

Do not force every risk into a supposedly precise formula, either. When reliable data is unavailable, clear assumptions, evidence, and uncertainty are more useful than multiplying numbers into a score that only looks precise.

##### The classroom risk-management process

**Identify → Assess → Treat → Track → Review**

**Risk identification:** Identify the assets to protect, possible events, and their consequences. It does not mean that identification is unnecessary because the problem is already known.

**Risk assessment:** Judge likelihood and impact, and state what remains unknown.

**Risk treatment:** Decide how to respond.

**Risk tracking:** Follow the problem, the progress of treatment, and changes in conditions.

**Review:** Check whether the original judgment and treatment were effective.

##### Risk treatment is not limited to fixing the problem or leaving it alone

**Reduce or mitigate:** For example, patch a vulnerability or reduce the group of people who can reach a service.

**Avoid:** Stop an unnecessary activity or feature whose risk is too high.

**Accept:** An appropriately authorized and accountable person accepts some remaining risk after understanding the conditions and consequences, with tracking and reassessment conditions in place.

**Transfer or share some consequences:** For example, use a contract or insurance to address particular losses. Insurance does not automatically fix a vulnerability or remove every responsibility.

##### When is “wait until Friday evening to update” reasonable?

The class uses delayed patching to illustrate risk acceptance. The example can be retained, but the decision conditions need to be added.

**Teaching workflow: Confirm that the update applies → Assess exposure from not updating → Assess the risk that the update disrupts service → Test and prepare recovery → Approve the change → Carry it out → Verify the result.**

This is the thinking behind **change management**. It is neither applying every update immediately without conditions nor postponing updates forever out of fear.

For example, if an old service cannot be updated immediately, access may be restricted while replacement is arranged. “We cannot afford a new machine” does not automatically mean “we can do nothing to protect it.”

---

#### 6. Cyber threat intelligence, SOC, and CVE — Turning information into something actionable

**Cyber threat intelligence** is not collecting every security news story. It is analyzing relevant information so that particular people can make better security decisions.

For example, “A company was breached” is a piece of news.

Questions closer to useful intelligence are: “What behavior enabled entry? Do we use similar systems? Can our existing records reveal the same behavior? Who needs to act?”

##### The four categories used in class

**Strategic intelligence:** Supports longer-term or higher-level decisions. For example, does a particular supply-chain risk justify changing how the company allocates resources?

**Tactical intelligence:** Focuses on actors' TTPs, helping defenders understand their methods and adjust detection and protection.

**Operational intelligence:** Focuses on more specific attack activities, targets, or campaign circumstances.

**Technical intelligence:** Provides specific leads for technical analysis, such as incident-related domains, file hashes, or vulnerability information. These categories overlap. A particular job title is not limited to reading only one type.

A **SOC**, or **Security Operations Center**, coordinates monitoring, analysis, and response. It may be an internal team, an outsourced service, or a combination. Its existence does not make the SOC solely responsible for every aspect of security.

**CVE**, or **Common Vulnerabilities and Exposures**, provides identifiers for publicly known vulnerabilities. A CVE number identifies a weakness. It does not announce that a particular computer has been compromised or completely describe the company's risk.

##### The intelligence life cycle

The checked source organizes the incomplete recording into this teaching workflow:

**Define the question → Gather relevant information → Organize and analyze it → Deliver it to the people who need to decide → Collect feedback and update it.**

For example, a SOC should not merely forward a vulnerability notice to the whole company. It should identify potentially affected devices and send the information to the relevant administrators.

**Fact-check correction: Intelligence does not automatically lose its value because everyone has already heard about it.** Older incidents may still help identify repeated behavior or compare changes.

---

#### 7. Threat modeling — Explain how things could go wrong before they do

**Threat modeling** is a structured way to describe what a system needs to protect, how it works, where problems could occur, and how to address them. It is more than listing vulnerability names. ([OWASP Foundation](https://owasp.org/www-community/Threat_Modeling))

The classroom sequence is:

**Identify security objectives → Understand the application → Decompose the application → Identify threats → Identify vulnerabilities.**

For a company's expense-reimbursement system, a security objective might be: “Employees may read only their own reimbursement records, and managers may approve only requests within their area of responsibility.”

Then understand how data moves: the browser submits a claim, the application checks and processes it, the database stores the result, and a manager approves it through another function.

To **decompose** the system is to break it into components, data flows, and permission relationships. A **trust boundary** is a point where security assumptions or permission conditions change. For example, user input entering a server must not be trusted simply because it came from a web form. ([OWASP Foundation](https://owasp.org/www-community/Threat_Modeling))

Then ask specific questions: “Does the server simply trust the employee number entered in the form? Could a student or employee use another person's number?”

**Fact-check correction: Decomposition is not merely deciding which colleague should receive a report.** Identifying component owners matters, but threat modeling also needs to explain how data and permissions cross boundaries.

---

#### 8. Incident management — Manage impact and evidence when something happens

First, separate three commonly confused terms.

**Event:** Something that happens in a system, such as a login or the creation of a file.

**Alert:** A signal that a rule or detection mechanism considers worth attention.

**Security incident:** An event that needs to be handled according to its security impact and the organization's procedures. Alerts need assessment; not every alert is a confirmed intrusion. This distinction is needed to understand the classroom discussion of alerts, handling, and response.

An **artifact** may be a log, file, error message, email, or other material left behind. It can support analysis, but calling something an artifact does not automatically make it reliable.

For example, a user saying “my computer is broken” provides little information. Preserving the error screen, time, and actions being performed gives the analysis a firmer basis.

##### Response does not need to wait until every cause has been investigated

The class mentions vulnerability handling, artifact handling, announcements, alerts, incident handling, response, and disclosure. These are related activities, not a fixed schedule that must be completed in that order.

A more practical teaching workflow is:

**Receive a report → Assess severity and scope → Preserve necessary evidence → Appropriately limit ongoing impact → Investigate and address the causes → Restore service → Review.**

For example, if data is actively leaking, you should not insist on completing the entire root-cause investigation before limiting the activity. But you also should not turn off every system without considering data and operational conditions. The response depends on the situation. The NIST incident-response guidance referred to in the source also places response within a broader risk-management context. ([NIST Computer Security Resource Center](https://csrc.nist.gov/pubs/sp/800/61/r3/final))

##### Escalation — Reporting upward or obtaining support

Here, escalation does not mean increasing computer privileges. It means bringing the problem to someone with the necessary capability or decision-making authority.

Teaching example: An engineer recognizes that the problem exceeds their abilities. They should explain what is known, what is unknown, and what help is needed, rather than repeatedly promising that it will be fixed in a moment.

The useful management lessons in this passage are communication, coordination, and obtaining resources—not judging managers by gender or seniority.

##### Disclosure — Reporting and notification may be required before repairs are complete

Reporting to a regulator, notifying affected people, and making a public statement are different actions.

For example, in a personal-data breach covered by GDPR, the thresholds and deadlines for notifying the supervisory authority and notifying individuals differ. Notification to the authority generally involves a requirement linked to 72 hours after awareness, with applicable exceptions. This must not be interpreted as waiting until everything is fixed before notifying anyone. ([European Commission](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/obligations_en))

---

#### 9. Supervised and unsupervised learning — The difference is in labels, not inherent accuracy

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

#### 10. Laws, standards, and certifications — First distinguish what they are

This section does not ask you to memorize every country's laws. It asks you to understand **which problems different rules address, whom they apply to, and how not to misuse them**.

**Laws and regulations** create obligations when their conditions of application are met.
**Standards** provide requirements or shared practices. Compliance may be required by law, contract, or an organization's commitments.
**Certification** provides evidence of conformity within a particular scope and certification system.

“A standard is not a law” does not mean that standards can always be ignored. Nor does being unregistered or not yet inspected remove applicable obligations.

##### PCI DSS: The Payment Card Industry Data Security Standard

PCI DSS stands for **Payment Card Industry Data Security Standard**.

It concerns the security of payment-card account data and related environments. Its scope is not limited to issuing banks. It may include merchants and service providers that process, transmit, or store the data, or can affect the security of the relevant environment. ([PCI Security Standards Council](https://www.pcisecuritystandards.org/faqs/1092/))

Teaching example: An online store outsourcing payment processing does not make every related responsibility disappear. It needs to understand how the data flows, what the provider is responsible for, and which responsibilities remain with the store.

Conversely, a membership card used only for discounts does not automatically create a payment-card environment merely because it looks like a card.

##### ISO/IEC 27001: An information security management system

ISO/IEC 27001 sets requirements for an **ISMS**, or **Information Security Management System**.

Here, “system” does not mean only computer software. It includes the management scope, risk treatment, responsibilities, implementation, evaluation, and continual improvement. ([ISO](https://www.iso.org/standard/27001))

Teaching example: A company does not merely write that accounts must be canceled when employees leave. Someone must carry out the task, retain records, and check whether the process works.

**Fact-check correction: Buying document templates does not establish compliance with the standard.** The documents must match actual practice. ISO develops standards; it does not directly certify organizations. An employee completing lead-auditor training also does not mean that the company has obtained ISMS certification. ([ISO](https://www.iso.org/certification.html))

##### NIST: Not an American version of ISO certification

NIST provides many standards, frameworks, and guidelines. The classroom simplification that the United States uses NIST while other countries use ISO is inaccurate.

An organization may use both. Whether a particular document is mandatory depends on the applicable rules and the actual situation.

##### HIPAA: U.S. rules concerning particular health information

HIPAA is a U.S. law. Its related rules apply to defined **covered entities** and **business associates**, not automatically to every hospital in the world. ([HHS.gov](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html))

Teaching example: An organization within scope must consider the relevant administrative, physical, and technical safeguards when managing electronic health information. However, invoking HIPAA alone cannot resolve a question about consent to a particular medical procedure in Taiwan. ([HHS.gov](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html))

##### SOX: Not a blanket rule that all email must be kept for seven years

SOX stands for the **Sarbanes–Oxley Act**.

The checked source narrows the classroom seven-year retention claim to SEC requirements for certain audit and review records, which may include relevant electronic communication. **One rule does not require every company to keep every email and all tax data for seven years.** ([SEC](https://www.sec.gov/rules-regulations/2003/01/retention-records-relevant-audits-reviews))

The right practical question is: “Which entity must retain which types of records, for how long, under which rule?”

##### DMCA: The Digital Millennium Copyright Act

The **Digital Millennium Copyright Act**, or DMCA, concerns issues including circumvention of technological protection measures and copyright matters involving online service providers.

**Fact-check correction: It was not the first law to recognize that creative work can be copyrighted without being on paper.** The existence of copyright in digital works should not be attributed entirely to this law. ([U.S. Copyright Office](https://www.copyright.gov/dmca/))

##### GDPR: Rules about personal data and rights have conditions of application

GDPR stands for **General Data Protection Regulation**. It was adopted in 2016, and its main provisions became applicable on **May 25, 2018**. ([EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679))

The right to erasure is not an unconditional right to make any information disappear everywhere in the world. Whether information must be erased depends on scope, the purpose of processing, legal obligations, and other exceptions. ([European Commission](https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en))

Also distinguish **removal from search results, removal by a platform, and removal from the original website**. These are three different outcomes.

##### The UK's DPA and UK GDPR

The **Data Protection Act 2018** and **UK GDPR** are related but distinct parts of the UK framework. The **Data (Use and Access) Act 2025** further amended that framework. This is not simply GDPR under another name. ([ICO](https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/the-data-use-and-access-act-2025-what-does-it-mean-for-organisations/))

When reading rules like these, first identify the country, time period, entity, and type of data. That is more useful than memorizing a claim that one law is the strictest.

### Section B: Module 2 — Footprinting and Reconnaissance

#### 11. Footprinting and reconnaissance — Turning scattered information into an understanding that can be tested

In this class, **footprinting** and **reconnaissance** both involve gathering information about a target and its environment. Their scopes overlap, but they do not need to be declared identical in every context.

The class broadly groups the information into organizational, personnel, network, and system information. Examples include what the company does, where it operates, which domains it uses, and which IP addresses or systems may be associated with it.

A genuinely useful process is:

**Define the purpose and scope → Gather information you are allowed to obtain → Record its source and time → Separate observation from inference → Identify the next question that needs verification.**

Teaching example: A job advertisement requiring CCNA supports the conclusion that the job needs related knowledge. It does not necessarily prove that the company uses one particular brand throughout its internal network. The company may be recruiting for customer projects.

Likewise, an email username of `alex` does not prove that the person's internal AD username is also `alex`. This example also cannot establish a fixed percentage of successful guesses.

##### Passive and active reconnaissance

**Passive reconnaissance** can use existing third-party information to understand a target without initiating new probes against it.

**Active reconnaissance** creates probes or other interactions with the target's infrastructure. A completed TCP connection is not required for it to count as active.

**Fact-check correction: Sending a probe through a proxy or third-party tool does not automatically make it passive.**

Ask whether this operation causes a new interaction with the target, not merely whether packets leave your own computer directly.

---

#### 12. Search engines, Shodan, DNSDumpster, and the Wayback Machine — Different views of the environment

##### Search operators

Search operators narrow a query. For example:

```text
site:example.org filetype:pdf
```

`site:` limits the website scope, and `filetype:` limits the file type. This is a search query, not a terminal command. Search results reflect the search engine's index, not a complete inventory of the website's current state.

Teaching example: A company wants to check whether its public PDFs contain information that should not have been published. It can limit a query to its own domain, then review how it manages public documents.

##### Google Hacking Database, or GHDB

GHDB is a third-party collection of example searches. It is not a Google product. It shows how search conditions can locate particular kinds of information.

For defenders, the point is understanding which accidental exposures may be searchable. Finding a result does not justify unrestricted access to any private information it contains.

##### Shodan

Shodan indexes information about internet-connected services and devices. It observes a different aspect of the internet from an ordinary web-content search engine.

Teaching example: An organization can check whether a device it believed was internal-only has left records of an externally available service.

However, appearing in Shodan does not prove a current vulnerability. The absence of a login page also does not mean the data owner has permitted everyone to use it.

##### DNSDumpster

DNSDumpster organizes domain-related information and relationships. It helps generate initial asset leads. It is not the company's complete DNS database or a map of the routes that packets actually travel.

For example, a record associated with a cloud provider supports the existence of some service relationship. It does not prove that the company's entire network runs through that provider.

##### Wayback Machine

The Wayback Machine provides historical captures of web pages.

**Fact-check correction: A capture timestamp is not necessarily the time the website was changed.** A snapshot taken on a particular day shows what that capture preserved. It does not establish that the website was modified at that exact moment.

Teaching example: Comparing a company's past and present public service offerings can provide historical leads. But a company name changing in a page footer is not enough to establish the legal relationship or business motives behind an acquisition.

---

#### 13. Competitive intelligence and OSINT tools — Public information does not guarantee a correct inference

**Competitive intelligence** means gathering and analyzing information about business competitors. Lawful analysis of public information is not the same as stealing trade secrets.

Teaching example: A company compares competitors' public products, job advertisements, and patent information to identify developments worth watching.

However, a patent application or publication does not guarantee that a related product will launch soon. The lighting in an interview photograph also cannot prove that the interview was paid for, much less reveal its price.

##### theHarvester

theHarvester is an information-gathering tool. The `-d`, `-b`, and `-l` options mentioned in class concern the query target, data sources, and result limits, respectively.

Tool versions and supported sources may change. **Understanding an option's purpose does not establish that an old combination of services in the recording still works.** Check the documentation for the installed version before using it; do not guess options from speech-recognition output.

##### OSINT Framework

**OSINT** stands for **Open-Source Intelligence**. “Open source” here refers to the public availability of the information sources. It does not mean that the software used must have publicly available source code.

OSINT Framework is a resource directory that helps users find services and tools by task. It does not guarantee that every link is free or that every tool is open-source software.

The recording may also mention Maltego, Recon-ng, and FOCA, but those names are interpretations based on context. The original does not provide complete versions or operating instructions, so these mentions should not be expanded into supposedly verified lab procedures.

---

#### 14. The dark web, Tor, and Bitcoin — Three concepts at different levels

The class discusses dark-web access, Tor, and Bitcoin together, but they are not the same technology.

The **dark web**, in this context, concerns services that require particular networks or software to access. Not all information missing from search engines belongs to the dark web.

**Tor Browser** uses the Tor network. A **Tor relay** is not simply another name for a commercial VPN server. Tor's design uses relays and layered protection to distribute knowledge about a connection. ([Support](https://support.torproject.org/about-tor/how-tor-works/key-management/))

An ordinary website may see a Tor exit relay as the source address. **Onion services** use a different connection arrangement, so the diagram of reaching an ordinary website through an exit relay should not be applied directly to them.

Therefore, visiting an IP-checking website and observing a changed address only shows that the source address observed by that website changed. It does not prove that all activity is impossible to link together.

**Bitcoin** is a separate subject involving payments and a ledger. Its transaction history is public. Decentralization does not mean that transactions cannot be traced, while public transactions do not mean the identity behind every address can be established directly. ([bitcoin.org](https://bitcoin.org/en/protect-your-privacy))

The particular data-sale incidents mentioned in the recording lack enough identifying information to be treated as verified cases. Those descriptions also cannot establish what proportions of all Bitcoin transactions serve different purposes.

---

#### 15. WHOIS, RDAP, and DNS — Names, registration data, and addresses are different things

##### WHOIS and RDAP

WHOIS is a traditional service for querying registration data. **RDAP**, the **Registration Data Access Protocol**, provides a more modern, standardized way to query that data.

From **January 28, 2025**, ICANN made RDAP the definitive source for generic top-level domain registration data. This does not mean that WHOIS for every country-code top-level domain stopped on the same day. ([ICANN](https://www.icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en))

Teaching example: You look up a domain's registration status, registrar, or publicly available date information. You are obtaining registration data, not the configuration of all the website's servers. You may also be unable to obtain everyone's private contact details.

##### DNS and resource records

**DNS**, the **Domain Name System**, does more than translate website names into IP addresses. It stores different types of **resource records** for different purposes.

The records relevant to this class include:

**A:** An IPv4 address associated with a name.
**MX:** Information about the servers handling mail for the domain.
**NS:** Information about the name servers responsible for the zone.
**CNAME:** A name alias.
**TXT:** Text information used for particular configuration or verification purposes.
**PTR:** A record commonly used for reverse name lookups. ([RFC Editor](https://www.rfc-editor.org/rfc/rfc1035))

##### Forward and reverse lookups

**Forward lookup:** Start with a name and look up associated information, such as an address.

**Reverse lookup:** Start with an IP address and look up an associated name, usually through separately managed PTR records.

**Fact-check correction: Reverse DNS is not the mathematical inverse of a forward lookup.** A successful forward lookup does not guarantee a reverse lookup will return the same name. A PTR result also does not verify the actual user or device owner.

**IP geolocation** should also be treated as a lead. An estimated address location, the service provider's location, and the actual user's location are not necessarily the same.

---

#### 16. Traceroute, TTL, and CDNs — Why one number cannot prove an operating system

##### What does traceroute do?

Traceroute tries to identify some of the intermediate nodes on the path from a source to a target. On Windows, the common command name is `tracert`. Different platforms do not necessarily use identical probe methods.

**TTL**, or **Time To Live**, is a field in an IP packet that limits how long or how far it can be forwarded. In ordinary routing, the TTL decreases at each router. Once it is exhausted, the packet cannot continue traveling indefinitely.

Traceroute uses probes with different TTL values and their responses to observe the path step by step. A hop that does not respond does not mean that no device exists there, nor does it necessarily mean that the connection is broken.

A teaching analogy is sending test letters with different permitted numbers of forwarding steps, then using reports from intermediate stops to learn which places they pass through.

##### Values such as 64 and 128 are only clues

The class mentions 64 as a common initial TTL for Linux and 128 for Windows. These can be introductory memory aids, but TTL is configurable and is not an identity marker exclusive to one operating system.

More importantly:

**The number of hops on the outward path does not necessarily equal the number of hops taken by the reply.**

If you receive a TTL of 58 and add the six outward hops shown by traceroute, the arithmetic gives 64. However, that does not necessarily recover the correct initial TTL, and it certainly does not prove that a website's back end runs Linux.

DNS records also have a TTL, but it concerns cache lifetime. It is not the same field as the IP-packet TTL discussed here. ([RFC Editor](https://www.rfc-editor.org/rfc/rfc1035))

##### A CDN is not simply a high-speed submarine cable

A **CDN**, or **Content Delivery Network**, is a distributed architecture for delivering content. For now, think of multiple service nodes in different places helping respond to users' content requests.

Teaching example: A user may first reach a CDN edge node rather than the origin server that actually produces business data.

The observed response, IP address, or network characteristics may therefore belong to that edge node. **The operating system on the front-facing node does not establish that the back-end business system runs the same operating system.**

Likewise, using a cloud service or CDN does not establish that denial-of-service is impossible.

---

#### 17. Email headers — Clues to a delivery route, not a complete network map

An **email header** contains information related to the processing of a message. **SMTP**, the **Simple Mail Transfer Protocol**, is an important protocol for delivering email.

SMTP servers add relevant `Received` fields while handling a message, so the original email can provide some clues about its delivery path. ([RFC Editor](https://www.rfc-editor.org/rfc/rfc5321))

A teaching workflow is:

**Preserve the original email → Examine its headers → Identify trustworthy processing nodes → Compare timestamps and other server records → Form a limited conclusion about the delivery path.**

The class illustrates possible processing with an email gateway, spam checks, archiving, and a mail server. These roles may exist, but not every company uses the same sequence.

**Fact-check correction: Not every email allows you to map an entire company's network.** Some internal processing is not visible in the headers, and some earlier fields may be untrustworthy.

Likewise, `Message-ID` identifies a message. It is not a digital signature that, on its own, proves the sender's true identity.

---

#### 18. Social engineering and information exposure — Focus on how procedures are bypassed

In this class, **social engineering** means exploiting people's trust, habits, pressure, or interactions to make them disclose information or take an improper action.

The classroom example of a caller impersonating IT illustrates how an identity claim and pressure can make someone skip normal verification. It is not a phone script to try on coworkers.

The abstract process is:

**Contact the person → Build trust or apply pressure → Ask them to depart from the normal procedure → Obtain information or cause an action.**

The matching defensive questions are: Is there an independent, trusted channel to verify someone claiming to be IT? Can a person pause to verify a request before performing a sensitive action?

##### Four classroom terms

**Eavesdropping:** Obtaining information that one should not hear. For example, a bystander overhears sensitive work being discussed in a public place.

**Shoulder surfing:** Watching another person's input or screen. For example, seeing an account name or sensitive document from beside them.

**Dumpster diving:** Obtaining information from discarded documents or media, such as printouts that were not properly disposed of.

**Impersonation:** Claiming another person's identity or role, such as pretending to be a manager or support worker. These methods are not mutually exclusive, and they are not all the same form of deception.

**Fact-check correction: A photograph's appearance, a wrong answer to a geography question, or a single conversational response is not enough to reliably determine whether someone is a bot or a criminal.**

##### Countermeasures should address the actual source of exposure

The class discusses security policies, training, social-media use, and directory listing.

**Directory listing** is a website feature that lists the files or subdirectories in a directory. It can accidentally expose content, but it also has legitimate uses, such as deliberately providing an index of public files.

The key distinction is:

**Not listing a filename is not the same as preventing access to the file.**

Teaching example: A backup file remains in a public website directory, but directory listing is disabled. Someone who knows the full path may still request the file directly. Protect the content itself rather than merely hiding its index.

Likewise, blocking social-media access on the company network does not remove information that was already made public. A platform's ability to obtain information about off-site activity also does not establish that every use of its built-in browser steals every password.

---

#### 19. Remote desktop, VMs, terminals, and root — Know which layer you are operating in

This recording explicitly identifies four laboratory VMs:

**Parrot, Windows Server 2019, Windows Server 2022, and Windows 11.**

The class operates through a designated remote-desktop environment. However, the whiteboard and login manual are missing, so a complete IP-address plan or each person's credentials cannot be guessed from the automatic transcript.

**RDP**, the **Remote Desktop Protocol**, supports interaction with a remote-desktop environment. Windows `mstsc` is a related connection program. A remote desktop and a VM are not the same thing: the first is a way to connect and interact, while the second is a virtual computer.

A **terminal** is the interface where you type text commands and see their results. A **shell** is the program that interprets commands and interacts with the operating system. They often appear together, but they are different concepts.

**root** is a highly privileged Linux account. **sudo** runs a command as a specified identity according to system policy, commonly to perform operations that require administrative privileges.

**whoami** only displays the current effective username. It does not raise your privileges. Even a result of root only describes your local execution identity. It does not authorize you to test arbitrary devices on the network.

### Section C: Module 3 — Understand networking before interpreting scan results

#### 20. Hosts, ports, services, and sockets — How does a packet reach the right program?

In the classroom scanning context, **host** is used broadly for a target device. It may be a desktop computer or another network device. Strict internet architecture still distinguishes end hosts from roles such as routers.

A **service** is software that provides a function, such as a website or file transfer.

A **port** is a number that distinguishes endpoints at the transport layer. It is not a physical USB socket. TCP and UDP ports belong to separate protocol spaces.

Teaching example: One server may provide both a website and FTP. A request needs to reach the correct service endpoint.

##### Common port numbers are conventions, not proof of service identity

TCP port 21 is commonly used for FTP control connections. TCP port 80 is commonly used for HTTP.

But an open TCP port 21 only supports a conclusion about the behavior of that TCP endpoint. The number alone does not prove that it is FTP, much less that it has a vulnerability.

##### Fact-check correction: The `services` file is not the packet-dispatch center

Linux `/etc/services` and the corresponding Windows `services` file map common service names to port numbers.

**Actual delivery to a program depends on sockets and the operating system's network processing. It does not require looking up every packet in this name table.**

A **socket** can be understood as an endpoint through which a program communicates over a network. A server program creates a socket, binds the relevant address and port, and enters the appropriate receiving state. The operating system uses protocol and connection information to deliver data to the matching endpoint.

Changing the number associated with `http` in `/etc/services` therefore does not automatically change the listening port of a running web service.

---

#### 21. Packets, headers, payloads, and MTU — Not every way of splitting data is the same

A **packet** is a unit of data transmitted over a network. A **header** contains the information its layer needs to process the data. The **payload** is the content carried by that layer.

Payload is relative to the layer. For example, an IP packet's payload may contain both a TCP header and TCP data. Headers from different layers should not all be treated as one header.

**Fact-check correction: Source and destination IP addresses are in the IP header. TCP source and destination ports are in the TCP header.**

##### Three different processes

**Packetization:** Organizing data into units that can be transmitted.

**TCP segmentation:** Organizing a byte stream into TCP segments.

**IP fragmentation:** Dividing an IP packet into fragments under applicable conditions, with corresponding reassembly needed later.

These processes are related, but they are not synonyms.

**MTU**, or **Maximum Transmission Unit**, describes the maximum unit size that can be sent under particular link conditions. It should not be treated directly as the amount of application data in every packet.

Teaching calculation: Suppose the IP MTU is 1,500 bytes, the IPv4 header is 20 bytes, the TCP header is 20 bytes, and there are no additional options. The space remaining for TCP data is:

**1,500 − 20 − 20 = 1,460 bytes.**

This calculation applies under the stated conditions. It is not a fixed value for every network or packet. The classroom phrase “1.5K per packet” should be read as an illustration.

Packetization is not merely a response to poor historical line quality. Limited-size transmission units also relate to sharing network resources, traveling over different links, and retransmission efficiency.

---

#### 22. TCP and UDP — Reliability, delay, and application needs

**TCP**, the **Transmission Control Protocol**, provides an ordered byte stream with reliability mechanisms.

**UDP**, the **User Datagram Protocol**, sends datagrams. It does not itself provide TCP's connection-establishment, ordering, and reliable-delivery mechanisms.

##### What does a TCP acknowledgment acknowledge?

TCP uses sequence numbers, acknowledgments, and retransmissions when necessary to handle data delivery. It does not guarantee success regardless of network conditions, and it is not an encryption mechanism. ([RFC Editor](https://www.rfc-editor.org/rfc/rfc9293.html))

Teaching example: You upload a file. TCP helps move the data between the communication endpoints. The application must still confirm that the file was validated and successfully written to storage.

Therefore:

**Receiving a TCP ACK does not establish that a business operation has completed.**

For example, the network stack receiving a request's data does not automatically mean that the database has finished updating.

##### UDP does not make acknowledgment impossible; it simply does not provide it for you

An application using UDP can design its own acknowledgment or retransmission mechanism.

The teaching trade-off is that file transfer usually places high importance on complete, correctly ordered content. Some real-time interactions place more importance on timely arrival. Data that arrives too late may no longer have its original value.

**Fact-check correction: UDP is not guaranteed to be faster in every situation. The choice between TCP and UDP is also not always impossible to change through implemented configuration options.** However, an administrator cannot unilaterally switch a TCP-only application to UDP and expect the other endpoint to understand it automatically.

---

#### 23. TCP flags and the three-way handshake — More than memorizing three abbreviations

A **flag** is a bit that expresses a control state. The class emphasizes six traditional TCP flags, but these are not the complete set of TCP control bits.

| Flag | Meaning to understand | Do not confuse it with |
| --- | --- | --- |
| **SYN** | Synchronizes sequence numbers; commonly used to establish a connection. | A simple request for permission to perform an operation. |
| **ACK** | Indicates that the acknowledgment-number field is meaningful. | A requirement to send a separate reply for every packet. |
| **FIN** | Indicates that this direction has no more data to send. | Something unrelated to closing a connection. |
| **RST** | Resets, rejects, or aborts the relevant connection state. | The only way to end a connection normally. |
| **PSH** | Relates to pushing data to the receiving application. | Immediately emptying every buffer. |
| **URG** | Indicates that the urgent-pointer field is meaningful. | Giving the entire packet the highest processing priority. |

These are the meanings retained after the source's fact-checking. In particular, URG does not tell the operating system to execute the entire packet's content immediately at top priority.

##### A typical three-way handshake

The ordinary case can be written as:

```text
Client → Server: SYN
Server → Client: SYN + ACK
Client → Server: ACK
```

This is not merely exchanging greetings. It involves synchronizing both sides' sequence numbers and confirming connection state.

The following numbers are a teaching example, not a reconstruction of the classroom whiteboard:

The client sends SYN with an initial sequence number of 100. The server responds with SYN using its own initial sequence number of 500 and acknowledges the client's SYN with ACK 101. The client then acknowledges the server's SYN with ACK 501.

This shows that each side has its own sequence-number space and needs to acknowledge the other's starting information. Later ACK values concern the position of the next expected byte, not simply which numbered packet was seen. ([RFC Editor](https://www.rfc-editor.org/rfc/rfc9293.html))

##### FIN and normal connection closure

The two directions of a TCP connection can close separately. A FIN from A means that A has no more data to send in that direction. It does not necessarily mean that B also has nothing left to send.

Common diagrams show FIN and ACK messages from both sides, but acknowledgments can be combined and packets can be retransmitted. “Closing always takes exactly four packets” is not an exception-free rule.

---

#### 24. Host discovery — ARP and ICMP ask different questions

##### ARP: Finding address mappings on a local network

**ARP**, the **Address Resolution Protocol**, handles address resolution on the local IPv4 link in this context.

A **MAC address** is an address used at the link layer. Do not think of it as an unchangeable personal identity card that remains the same across the entire internet.

The simplified classroom process is:

**Ask which device corresponds to this IP address → Receive a relevant reply → Obtain link-layer address information.**

This is a useful way to observe hosts on a local network.

**Fact-check correction: ARP is not a device for measuring whether a computer's power is on.** A reply establishes that a corresponding protocol response was received. It does not directly prove that a particular physical computer has fully booted or that its application is healthy. Proxy replies, virtualization, and other factors may affect interpretation.

##### ICMP Echo: Did this type of probe receive a reply?

**ICMP**, the **Internet Control Message Protocol**, provides network-control and error-reporting messages. The common `ping` utility uses Echo Request and Echo Reply.

A simplified process is:

**Send an Echo Request → The target or relevant network entity processes it → Receive an Echo Reply if permitted.**

No reply may result from filtering, the path, configuration, or the target's state. “The computer is off” is not the only possible explanation.

##### An important detail when experimenting with Nmap

On a local Ethernet network, Nmap may use ARP for host discovery even when another probe method has been selected.

Therefore, **putting an ICMP option in the command does not establish that an ICMP response caused the result**. Understand the tool's actual behavior and environment rather than relying only on the command's name. ([Nmap](https://nmap.org/book/man-host-discovery.html))

---

#### 25. Port scanning — What do open, closed, and filtered mean?

**Port scanning** uses probes and responses to judge the state a particular port presents under the conditions of that observation.

**Open:** Behavior consistent with accepting the relevant communication was observed.

**Closed:** The target can respond, but the port does not present a state that accepts service connections.

**Filtered:** Filtering or related factors prevent the tool from determining whether the port is open or closed. ([Nmap](https://nmap.org/book/man-port-scanning-basics.html))

These are results from a particular place, time, and method of observation. They are not permanent certificates of state.

##### TCP connect scan: `-sT`

A TCP connect scan uses the operating system's connection functions to try to establish an ordinary TCP connection. For an open endpoint, it normally completes the handshake and then ends the test connection. ([Nmap](https://nmap.org/book/man-port-scanning-techniques.html))

It asks, “Can a TCP connection be established this way?”

A successful TCP connection does not establish that every application function is working.

##### TCP SYN scan: `-sS`

A SYN scan judges state from earlier TCP responses without completing the ordinary full connection-establishment process. This is why it is often called a **half-open scan**. ([Nmap](https://nmap.org/book/man-port-scanning-techniques.html))

Typically, a SYN+ACK response to SYN is a clue that the endpoint is open. RST is often a clue that it is closed. No response or certain error reports need further interpretation according to the tool's rules.

**Fact-check correction: Half-open does not mean unlogged, and it certainly does not mean undetectable.** Even if the application has no complete connection record, network devices, packet monitoring, or an IDS may still observe the probes. Nmap's documentation explicitly notes that an appropriate IDS can detect both scan types. ([Nmap](https://nmap.org/book/man-port-scanning-techniques.html))

Also, Nmap does not necessarily start at port 1 and scan every port in numerical order. The actual range depends on its defaults and options.

---

#### 26. Banners, version detection, and OS fingerprinting — Three different types of evidence

##### Banner: Identification information supplied by the service

A **banner** may be a welcome message or identification information returned when interaction with a service begins.

For example, an FTP service may include its product name in a response. This is a useful clue, but the content may be omitted, changed, or disguised.

**Fact-check correction: Not every service or operating system returns a banner from which the version can be read directly.**

##### Service and version detection: `-sV`

Nmap's `-sV` identifies services and versions using probes, response patterns, and related information. It does not merely print a table of conventional service names for port numbers. ([Nmap](https://nmap.org/book/man-version-detection.html))

Teaching example: First, TCP port 21 is observed to be open. Further probing produces a response consistent with a particular FTP product. That provides more evidence than saying port 21 is usually FTP, but it still does not establish exploitability.

Remember this distinction:

**`-v` increases output verbosity. `-sV` performs service and version detection. Capitalization and option combinations matter.**

##### OS fingerprinting: `-O`

**Operating-system fingerprinting** may compare the response characteristics of a TCP/IP stack with known patterns.

It does not require the target to announce “I am Windows,” and it is not simply banner reading. ([Nmap](https://nmap.org/book/man-os-detection.html))

Teaching example: If a tool reports that the target may belong to a particular Windows family, retain that uncertainty and the matching conditions. Do not rewrite it as a confirmed exact version and patch state.

##### NSE and `smb-os-discovery`

**NSE**, the **Nmap Scripting Engine**, allows scripts to perform different kinds of tasks.

The `smb-os-discovery` script mentioned in class tries to obtain system information through information exposed by SMB. The target must provide the relevant service and permit the information to be obtained. Not every run will return every field.

`.nse` is the extension for these script files. `/usr/share/nmap/scripts` is a common Linux package path, not a universal path for every platform.

**A script name that sounds like a simple query does not mean every script is harmless.** Check what it does and whether it is within the authorized scope before running it.

---

#### 27. How should the classroom commands be read?

The following are documented examples supplied by the checked source, not word-for-word reconstructions of missing commands. `<LAB_IP>` is a placeholder. It should not be pasted unchanged into a terminal and does not designate an already authorized target.

| Example | Main purpose |
| --- | --- |
| `nmap -sn -PR <LAB_IP>` | Perform ARP host discovery in a suitable local IPv4 environment, without an ordinary port scan. |
| `nmap -sn -PE <LAB_IP>` | Request ICMP Echo host discovery; still account for actual behavior such as local ARP use. |
| `nmap -sT <LAB_IP>` | Perform a TCP connect scan. |
| `nmap -sS <LAB_IP>` | Perform a TCP SYN scan. |
| `nmap -p 21 -sV <LAB_IP>` | Select port 21 and perform service/version detection. |
| `nmap -O <LAB_IP>` | Perform operating-system fingerprinting. |
| `nmap --script smb-os-discovery <LAB_IP>` | Select the specified script for obtaining SMB information. |

These purposes and limitations are listed in the checked source's command reference.

The point is not to memorize seven commands. It is to be able to answer, every time:

**Am I observing a host, a port, a service, or an operating system? What kind of conclusion can this result support?**

---

#### 28. Evasion and spoofing concepts from class — Understand the mechanisms, not supposed guarantees of success

##### Fragmentation: Differences in reassembly and inspection

IP fragmentation can have legitimate uses, but it also creates reassembly and processing costs. If an intermediate device and the receiving host handle fragments differently, they may interpret the security significance differently. ([RFC Editor](https://www.rfc-editor.org/rfc/rfc8900.html))

A teaching explanation is that a defensive device may inspect separate pieces while the receiver interprets their reassembled content. The two may therefore see different meanings.

**Fact-check correction: “Every fragment is an attack, so drop them all without exception” is not a universal rule.** Whether and how to restrict fragments depends on the protocol, network requirements, and device capabilities.

##### Source routing: Routing information supplied by the source

**Source routing** involves a packet's source providing some routing information rather than leaving the path entirely to ordinary forwarding decisions.

It may conflict with security policy, but not all routing functions are the same. Identify the specific mechanism and whether it is needed.

##### Source-port manipulation is not the same as destination-port abuse

The **source port** belongs to the sending endpoint; the **destination port** belongs to the receiving endpoint.

Using a particular source-port number to fool an insufficiently strict rule into trusting traffic is different from placing an external data-receiving service on destination port 80.

**Fact-check correction: The classroom heading may refer to source-port manipulation, but the example of sending data out to port 80 mainly concerns the destination port and outbound-connection policy.**

This also shows why allowing only ports 80 or 443 does not establish that all permitted content is legitimate business traffic.

##### Decoys: Making source identification more confusing

Here, a **decoy** is an apparent additional source. Packets appearing to come from several sources do not mean the tester owns those IP addresses, and they do not guarantee that defensive equipment will be misled.

Several claimed source addresses should not be interpreted as several verified real identities.

##### IP spoofing: Falsifying the source claimed by a packet

**IP spoofing** makes a packet's source information differ from its actual sending source.

Teaching example: A sends a message to B but writes C as the reply address. If B replies to that address, the response may go to C rather than A. This helps explain **reflection**.

However, changing a source IP address does not automatically allow the sender to receive all traffic in a two-way connection. Reply paths and protocol state still matter.

##### MAC spoofing: Changing a link-layer address

Some devices and system configurations allow the MAC address in use to be changed, but this is not identical across all equipment. It is also not an identity-hiding function that spans the whole internet.

##### Packet builders and checksums

A **packet builder** creates packets with specified fields or content. The class mentions **Colasoft Packet Builder** to show that packet content is not only something to observe passively; software can construct it.

A **checksum** checks for certain data errors over a defined portion of data. The covered data and rules differ across protocols.

**Fact-check correction: A checksum is not a digital signature and does not prove a trusted source.** Someone who can change the content may also be able to calculate a matching checksum. Likewise, the broad claim that an intentionally wrong checksum lets traffic pass through a firewall cannot be accepted without examining the device and protocol.

---

#### 29. Proxies, VPNs, and no-logs claims — A different intermediary does not remove the trust problem

A **proxy** communicates with another party on someone's behalf. Which communication it supports depends on the proxy type and configuration.

A **VPN**, or **Virtual Private Network**, is a different mechanism for establishing network connections and protecting communication. It should not be treated merely as a larger web proxy.

These arrangements may change the source address seen by the target, but the activity still interacts with it. **Accessing a target through a proxy does not make the activity passive reconnaissance.**

Teaching example: An employee accesses an outside website through a company-controlled proxy. The website may see the proxy's connection, while the company can still control allowed destinations through its policies.

**No-logs** is a claim about record retention. You still need to ask: Which records? Over what period? On which systems? How can the claim be verified?

**Fact-check correction: Multiple VPN layers, foreign IP addresses, or no-logs claims do not guarantee that activity cannot be linked. Nor do they establish that every investigation must fail.**

---

#### 30. Final defensive measures — What does each one actually protect?

##### ICMP: Restricting Echo is not the same as blocking all ICMP

ICMP is used for more than ping. It also supports network-control and error-reporting functions.

Restricting Echo Requests from particular sources is therefore different from dropping every ICMP message. The latter may affect normal network functions.

##### IDS and IPS: Detection is not the same as blocking

An **IDS**, or **Intrusion Detection System**, primarily provides detection and alerts.

An **IPS**, or **Intrusion Prevention System**, can block activity when deployed with appropriate rules and placement.

An IDS alert does not establish that traffic was blocked. No alert does not establish that nothing went wrong. Keep this distinction whenever the class treats detection equipment as automatically providing prevention.

##### Do not confuse these two Apache settings

`ServerSignature Off` controls the related signature information in server-generated pages.

`ServerTokens` controls the information exposed in the HTTP `Server` header. For example, a less detailed setting may still show the product name rather than removing the header entirely. ([Apache HTTP Server](https://httpd.apache.org/docs/2.4/mod/core.html))

**Fact-check correction: `ServerSignature Off` does not mean the HTTP `Server` header has been removed.**

Reducing version disclosure also does not fix a vulnerability. The real software version, permission issues, and configuration problems remain.

##### TTL and IP ID: An unusual value is a clue, not proof of spoofing

Different TTL values may result from different paths or settings. The IPv4 ID is also not necessarily a system-wide counter that increases by one for every packet.

Therefore, large differences in TTL or IP ID do not, by themselves, prove a spoofed source.

One relevant defense against source-address spoofing is **source-address validation**: checking whether a source address should appear from that network location. ([RFC Editor](https://www.rfc-editor.org/rfc/rfc2827.html))

##### Encryption: State the boundary it protects

Encryption can protect the confidentiality of the relevant content. Combined with suitable authentication and integrity mechanisms, it can also support other security goals.

However, encryption is not a universal filter for forged packets. It does not automatically repair infected endpoints or prevent limited bandwidth from being exhausted.

**The claim that encryption solves 80% of network problems is not supported by evidence in this material.** The right question is: “Which part of the communication, which data, and which security properties does this encryption protect?”

### Bringing the class together: An interpretation you should be able to make

Suppose you observe a designated VM in **an authorized laboratory** and obtain the following teaching scenario:

ARP receives a reply. ICMP Echo does not. TCP port 21 is reported as open. Service detection returns a result consistent with a particular FTP product.

The correct conclusion is not: “This computer is confirmed to be fully booted and healthy, runs an exact version, and can be hacked.”

A more accurate interpretation is:

**The ARP reply** provides an observation about local address resolution.
**The missing ICMP reply** means that this probe did not receive the expected response; the cause still needs assessment.
**TCP port 21 being open** provides evidence that the endpoint was reachable under those conditions at that time.
**The service-detection result** adds a clue about the product or protocol, but is not proof of successful exploitation. This is why the checked source requires recording the probe type, source location, time, version, and limitations.

The next step should follow the original testing objective. Are you checking the asset inventory, identifying an unnecessary service, or assessing whether a specific vulnerability applies? Do not keep expanding the test simply because the tool has more options.

The most useful thinking sequence to take from this class is:

**Gather information to generate leads. Design probes to obtain observations. Check conditions to form judgments. Keep evidence to support conclusions. Fix and retest to confirm improvement.**

Your first exercise can be a one-page **scan-interpretation record**. State the testing purpose, authorized scope, probe method, actual observations, supported conclusions, and what remains uncertain.

**The standard for completion is not how many commands you can recite. It is whether you can explain to another student what question the tool asked, what the system actually answered, and why your conclusion does not go beyond the evidence.**
