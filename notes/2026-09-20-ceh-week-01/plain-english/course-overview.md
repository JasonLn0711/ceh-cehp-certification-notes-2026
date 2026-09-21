# Course overview, twenty modules and laboratory context

[Reading map](README.md) · [Every source heading](coverage.md) · [Connections](connections.md) · [Unchanged source](../../../source/2026-09-21-ceh-merged-plain-english/CEH_Full_Merged_Plain_English.md)

Captured 2026-09-21, Asia/Taipei. The source-derived text below retains the supplied explanation, examples, correction labels, uncertainty and citations. Heading levels are adjusted for reading; explicit anchors and **Study connection — editorial** paragraphs are additions. References to recordings or earlier checking are the source author's statements, not new observations. This file covers original lines 1–339.

## Reading route

- [Part 1 · 1. What does CEH actually teach?](#p1-01)
- [Part 1 · 2. The twenty modules: What problem does each one address?](#p1-02)
- [Part 1 · 3. How do the classroom VMs, Parrot, and Windows Server fit together?](#p1-03)

<!-- source-derived-text-begin -->


<a id="en-h001"></a>

## CEH Course — Complete Merged Plain-English Translation

**Parts 1 and 2 | English edition | Prepared September 21, 2026**


<a id="en-h002"></a>

## About this edition

This document combines the full text of the two supplied files in course order. Part 1 comes from `Pasted markdown (2)(20260921-021600).md`; Part 2 comes from `Pasted markdown(20260921-021548).md`.

The supplied files are explanatory course notes based on recordings, rather than raw, timestamped, word-for-word transcripts. Their correction labels, teaching additions, examples, qualifications, and references are retained below. References to “the recording,” “the transcript,” or “the checked source” belong to those original notes. Their references and factual claims have not been independently rechecked for this translation, and missing audio, whiteboard content, commands, or credentials have not been reconstructed.

---


<a id="en-h003"></a>

## Part 1 — Course Overview and Ethical-Hacking Foundations

The main purpose of this class is not to learn a few hacking tools. It is to build a complete way of thinking:

**What am I protecting? → How could it go wrong? → How can I test that within the authorized scope? → How can I keep reliable evidence? → How can I make sure the problem is actually fixed?**

The first half of this recording introduces the twenty modules. The second half formally begins **Module 1: Introduction to Ethical Hacking**. The explanation below therefore introduces the concepts in all twenty modules before exploring the definitions and procedures in Module 1. It does not pretend that material from later, unrecorded classes was already covered in this transcript.

The school, company, and bank scenarios below are **teaching examples designed to explain the ideas, not accusations about real incidents**. Necessary corrections are marked wherever the technical explanation differs from the transcript.

---


<a id="en-h004"></a>

<a id="p1-01"></a>

## Part 1 · 1. What does CEH actually teach?

**Study connection — editorial:** Security testing starts with the intended permission rule and examines both allowed and forbidden behavior. [Chinese explanation](../handouts-zh/part-01.md#h1-01) · [Audited detail](../course-overview.md#course-purpose) · [Source coverage](coverage.md#en-h004). Source section: lines 25–56.

**CEH stands for Certified Ethical Hacker, a certification provided by EC-Council.** For now, understand ethical hacking as:

> Using methods that an attacker might use, within clearly defined permission and limits, to find security problems and help fix them. ([EC-Council Certification Lookup](https://cert.eccouncil.org/certified-ethical-hacker.html))

Suppose a university is preparing to launch a website where students can check their grades.

Ordinary functional testing asks, “After a student logs in, can they see their own grades?”

Security testing also asks, “Can a student see someone else's grades? Can they turn themselves into a teacher? Will the system accept actions that it should reject?”

Both types of testing examine the same website, but from different angles:

**Functional testing checks whether the things that should happen actually happen. Security testing also checks whether someone can make things happen that should not happen.**

The class repeatedly emphasizes permission because security testing can trigger alerts, add load to a system, or even change data or service conditions. “I want to help” is not the same as having permission.


<a id="en-h005"></a>

### Basic terms you need for the following sections

**Host, client, and server.** A host is a computer or computing environment that participates in a network. A client makes a request; a server provides a service. For example, your browser requests your grades, and the university website receives the request and returns the result. “Server” can mean either the software providing the service or the computer running that software. ([MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/How_does_the_Internet_work))

**IP address, domain name, and DNS.** An IP address is used to locate endpoints and deliver traffic on a network. A domain name is an easier-to-remember name. DNS is a system for looking up information associated with names; one important use is translating a name into an IP address. Think of this as looking up an address. Do not assume that a domain name always refers to one unchanging physical computer. ([MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/How_does_the_Internet_work))

**Port.** A port is a number used in network communication to distinguish service endpoints. It is not a physical USB socket. For example, one computer may provide a website and other services on different ports. An open port means that, under the conditions of that observation, a service is accepting the relevant communication. **It does not automatically mean that the service has a vulnerability.** ([Nmap](https://nmap.org/book/man-port-scanning-basics.html))

**Service.** Here, a service is software that provides a function, such as a website, file access, or email. A **protocol** is a set of rules for exchanging messages. FTP and SMTP, mentioned in the course, concern file transfer and email delivery respectively. They are not operating systems.

With those terms in place, we can look at the twenty course modules.

---


<a id="en-h006"></a>

<a id="p1-02"></a>

## Part 1 · 2. The twenty modules: What problem does each one address?

**Study connection — editorial:** Use the twenty modules to locate a problem; only M01–M03 receive detailed treatment in these handouts. [Chinese explanation](../handouts-zh/part-01.md#h1-02) · [Audited detail](../course-overview.md#module-map) · [Source coverage](coverage.md#en-h006). Source section: lines 57–291.


<a id="en-h007"></a>

### Module 1: Introduction to Ethical Hacking — Security and permission come first

This chapter starts with several questions: What is security? What is an attack? What is a vulnerability? Who may test a system? How far may the testing go?

These are not pointless preliminaries before using tools. They give the later actions a clear meaning. Without this foundation, you might obtain a scan report without understanding what it proves. This is the main topic of the second half of this recording.


<a id="en-h008"></a>

### Module 2: Footprinting and Reconnaissance

**Footprinting** means collecting and organizing the information a target leaves behind. **Reconnaissance** means investigating a target to understand it. Their coverage overlaps in introductory material; you do not need to memorize them as completely separate activities. The class uses the example of a burglar observing a house beforehand to explain the idea: understand the environment before deciding what to do next.

In an authorized test, the process can be understood as:

**Confirm the target → Gather relevant information → Build a list of assets and their relationships → Check which assets are within the authorized scope.**

For example, a university gives you a list of its production website, test website, and email systems. You first organize their purposes and relationships. You do not start testing every website that happens to contain the university's name.

The result of this step should be an understanding of the environment, not a claim that you have successfully broken in.


<a id="en-h009"></a>

### Module 3: Scanning Networks

Network scanning uses particular probes and their responses to understand the state of hosts, ports, and services. It can be divided into three questions:

“Which targets respond?”
“Which ports are reachable?”
“What services might be behind those ports?” ([Nmap](https://nmap.org/book/man-port-scanning-basics.html))

Teaching example: You perform an authorized check of a web-server VM that you created yourself. You observe that the web service responds, but another service does not.

What you can report is: “From this network location, using this type of probe, I observed these results.”

**Correction: No response does not mean that the host is turned off.** A firewall may be filtering traffic, there may be a routing problem, or that particular probe may not receive a response. Similarly, an open port does not establish that an exploitable vulnerability exists. ([Nmap](https://nmap.org/book/man-port-scanning-basics.html))


<a id="en-h010"></a>

### Module 4: Enumeration

Enumeration means asking a service further questions to obtain specific information about objects or settings, such as accounts, groups, shared resources, or software. How much you can obtain depends on the protocol, your permissions, and the system's configuration.

Think of a building:

Scanning is like finding out that a service desk is open. Enumeration is like asking the desk which departments are present and which resources are available.

A teaching workflow is:

**Discover a service → Understand which queries it supports → Make queries using the permitted level of access → Record the returned information.**

For example, you might check whether a test account can list shared folders that should not be publicly visible. That still does not mean the account can read every file inside those folders.


<a id="en-h011"></a>

### Module 5: Vulnerability Analysis

Vulnerability analysis asks:

> Do the versions, settings, permissions, or behaviors I observed have security problems? Does a suspected problem actually apply to this environment?

The introductory example in class is to identify a software version and compare it with vulnerability information.

A more complete teaching workflow is:

**Gather evidence → Identify possible vulnerabilities → Check the required conditions → Confirm whether this environment meets them → Assess the impact.**

For example, a tool reports that a server may be running a vulnerable version. You still need to check: Was the version identified correctly? Has a patch already been applied? Is the affected feature enabled? Does the tester have the privileges required for the vulnerability to apply?

**A matching version is a lead for investigation, not proof of a successful intrusion.**


<a id="en-h012"></a>

### Module 6: System Hacking — Testing system weaknesses and their impact

This module introduces the exploitation of system weaknesses and the effects they may have. In an authorized test, the point is to confirm a problem using permitted methods, not to take unlimited control of or damage the system.

Suppose a test website has a requirement that students must not gain access to teacher functions. A tester uses a prearranged test account and proves that the student role can enter a teacher-only function. That already provides important evidence.

There is no need to change the entire university's grades just to “prove it more thoroughly.”

Keep this distinction clear: **Proving that a security boundary can be crossed is not the same as increasing the damage.**


<a id="en-h013"></a>

### Module 7: Malware Threats

Malware is software used to perform improper or harmful actions. The class describes malicious content disguised as an update, email attachment, or pirated software so that users install it themselves.

A **Trojan** is defined by its disguise: it appears useful but includes behavior that the user is not meant to know about. A **backdoor** is defined by its function: it provides a route around normal security controls. These terms describe different aspects of software, and both may apply to the same malicious program.

Teaching scenario: An employee installs an unknown “required reader” to open a document. The software then performs unauthorized actions in the background.

Therefore, **an updated system does not make every program that a user later runs trustworthy**.


<a id="en-h014"></a>

### Module 8: Sniffing — Capturing network packets

Sniffing means observing or capturing network communication. For now, think of a **packet** as a unit of data sent over a network. It contains information needed for delivery and part of the content. In this section, the transcript's terms “storm” and “sleeping” should be read, from context, as “packet” and “sniffing.”

Legitimate uses include investigating why a website cannot be reached or why a connection keeps dropping. Watching other people's communication without permission is a different use of the same capability.

The basic process is:

**Choose a place where traffic can be observed → Capture the traffic → Filter the relevant data → Interpret the protocols and content.**

**Correction: Capturing packets does not mean you can see plaintext passwords inside them.** For example, a connection that properly uses HTTPS/TLS protects the transmitted content. Capturing the traffic does not automatically decrypt it. ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html))


<a id="en-h015"></a>

### Module 9: Social Engineering

Social engineering does not directly attack code. It exploits people's trust, habits, pressure, or working procedures to get them to do something they should not do. The classroom example involves tricking users into giving away authentication information.

**Phishing** is one form of social engineering. It uses apparently trustworthy messages to persuade someone to give away information, open content, or take an action.

For example, an employee receives a message claiming to be from the IT department and demanding immediate action on an account problem. The question is not just whether the message looks convincing. It is also whether the company has a trustworthy way to verify it and whether employees can stop and check under time pressure.

From the defender's perspective, ask: “Can a single email make someone change a payment, an account, or access permissions?”


<a id="en-h016"></a>

### Module 10: Denial-of-Service

A **DoS** attack aims to prevent legitimate users from using a service normally. It does not necessarily damage the computer or make it crash. The class illustrates this by describing an attacker consuming the external network bandwidth so that customers cannot reach a website.

Imagine a restaurant whose kitchen is still working, but whose entrance is blocked by a huge number of abnormal requests to join the queue. Real customers cannot get in.

The core process is:

**Consume a limited resource → Leave legitimate requests without enough resources → Reduce service quality or make the service unavailable.**

However, a slow website alone does not prove an attack. A normal peak in course-registration traffic can also exceed system capacity. You need traffic, request, and system evidence; you cannot infer intent from the outcome alone.


<a id="en-h017"></a>

### Module 11: Session Hijacking

A **session** is a mechanism for maintaining the state of an interaction. For example, after you log in to a website, you do not have to type your password again for every page.

For a typical website, the process is:

**Authentication succeeds → A logged-in state is established → The browser holds a related session ID or token → Later requests include it → The server recognizes the session.**

Cookies are a common way for a website and browser to exchange and store this information, but not every cookie is a login credential. ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html))

Session hijacking happens when an attacker uses session-identifying information they have obtained or control to impersonate the original user.

Everyday analogy: Your password is like the identity check at an entrance. A valid session token is like the pass you receive afterward. Someone who obtains the pass may not need to know the password you used at the entrance.

**Correction: Stealing a password, stealing an already authenticated session, and obtaining the AD authentication information mentioned in class should not all be treated as exactly the same mechanism.**


<a id="en-h018"></a>

### Module 12: Evading IDS, Firewalls, and Honeypots — Understanding defenses and their limits

First, distinguish several terms.

A **firewall** uses rules to decide which communication may pass. The classroom remark that some services become reachable after a firewall is turned off refers to this filtering boundary.

An **IDS**, or intrusion detection system, watches for suspicious activity and raises alerts. An **IPS**, or intrusion prevention system, can also try to block the activity. Neither guarantees that every attack will be detected. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/intrusion_detection_system))

A **honeypot** is a system or resource deliberately designed to attract intruders so that their activity can be observed. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/honeypot))

Using the building analogy: a firewall is like access control at the door; an IDS is like an alarm that detects unusual activity and notifies the manager; an IPS can also take blocking action; and a honeypot is a decoy designed to reveal improper access attempts.

This recording only introduces the module's direction. It does not provide a full lesson on evasion techniques.


<a id="en-h019"></a>

### Modules 13 and 14: Web Servers and Web Applications — Do not confuse these layers

A **web server** handles website communication, content delivery, and related tasks. From context, the products mentioned in class include IIS, Apache, and nginx. The transcript's “iOS” in the web-server section may be a speech-recognition error for IIS, rather than the mobile operating system iOS.

A **web application** handles business logic, such as logging in, registering for courses, calculating credits, and displaying grades.

A teaching model of the relationship is:

**The browser sends a request → The web service receives it → The application decides what to do → It reads or writes the database when needed → It returns a result.**

Module 13 focuses on server software, deployment, and configuration. Module 14 focuses more on application permissions, inputs, and workflows. Problems can occur in either layer.

The class uses the example of entering `10000.01` into a quantity field that expects an integer. The point is not that every program will crash. It is that a program cannot simply assume users will always behave as expected.

A more specific security problem is a student who logs in normally but is allowed to read a grade record without the application checking their permission for that record. **Successfully logging in and being authorized for every subsequent action are two different things.** ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html))


<a id="en-h020"></a>

### Module 15: SQL Injection

**SQL** is a language for interacting with relational databases. The central problem in SQL injection is:

> User input that should be treated as data becomes mixed into the structure of a command.

For example, a website only intends to look up one student. However, the program constructs the database command by unsafely joining strings, so the input changes the meaning of the command itself. ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html))

The key process is:

**Receive input → Build a database command unsafely → The database interprets part of the input as a command → An unintended query or operation is executed.**

One major defense is a **parameterized query**: define the command structure first, then pass the input to the database as data parameters instead of freely inserting it into the command. This separates commands from data; it is not merely a matter of deleting unusual symbols. ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html))

**Correction: SQL injection can be serious, but you cannot call it the most serious vulnerability in every case without considering the permissions, data, and environment.**


<a id="en-h021"></a>

### Module 16: Hacking Wireless Networks — Wireless network security

This module covers wireless standards, authentication, and encryption mechanisms. The source only previews a discussion of mechanisms that should not be used. It does not examine each one in this recording.

First, separate two questions:

**Authentication** asks, “Who may join or use this network?”
**Encryption** asks, “How is the transmitted content protected from people who cannot legitimately read it?”

Teaching example: A café's Wi-Fi may give visitors internet access. Successfully connecting should not also give a visitor administrative access to the café's checkout system.

The point is that **connecting to a network, reading its communication, and operating its internal systems are different levels of capability**.


<a id="en-h022"></a>

### Module 17: Hacking Mobile Platforms — Mobile platform security

The mobile platforms previewed in class include Android and iOS. This section does not fully develop the attack and defense processes for either platform.

As a starting point, think about the data and permissions on a phone. For example, does an app that only displays campus announcements have a reason to request access to all your contacts?

During a review, ask: What is the app supposed to do? Which permissions does it receive? Where does it store data? Where does it send that data?

These questions move mobile security beyond simply asking whether a phone has a virus. They turn it into an examination of data flows and permissions.


<a id="en-h023"></a>

### Module 18: IoT, OT, and ICS — From information systems to the physical world

In this class, **IoT**, the Internet of Things, refers to network-connected devices such as sensors and network cameras. **OT**, operational technology, includes systems that monitor or control physical equipment and processes. **ICS**, industrial control systems, is an important area within OT. ([NIST Computer Security Resource Center](https://csrc.nist.gov/pubs/sp/800/82/r3/final))

Teaching example: An ordinary website failure may prevent people from looking up information. A control-system failure may stop a conveyor belt, disrupt temperature control, or affect physical safety.

In these environments, you cannot ask only whether a patch can be installed. You must also consider how patching, restarting, or testing could affect reliability and safety. This is why you cannot directly apply ordinary laboratory procedures to an operating production line. ([NIST Computer Security Resource Center](https://csrc.nist.gov/pubs/sp/800/82/r3/final))


<a id="en-h024"></a>

### Module 19: Cloud Computing

Cloud computing is a model for obtaining configurable computing resources over a network when needed. Resources can be provided and released relatively quickly. Do not reduce the idea to “someone else's computer”: shared resources, on-demand allocation, and how those resources are managed are also important. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/cloud_computing))

Teaching example: A research laboratory temporarily needs a pool of computing resources. It releases them when the work is complete rather than first buying every physical machine.

From a security perspective, you still need to ask: Who may create resources? Who may read the data? Which settings could expose content that was supposed to remain private?

The original recording only previews cloud concepts and characteristics. It does not fully explain the different service models.


<a id="en-h025"></a>

### Module 20: Cryptography

The class emphasizes that this CEH course mainly teaches the use of cryptographic technology. It does not expect everyone to invent new algorithms.

First, learn a few basic concepts:

**Plaintext** is the original, understandable data. **Ciphertext** is data transformed by encryption. A **key** is an important parameter that controls a cryptographic operation. **Encryption** protects data, while **decryption** recovers the corresponding data. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/encryption))

**Asymmetric cryptography** uses a related public key and private key. For example, a private key can create a digital signature, and the corresponding public key can verify it. The private key must be protected; the public key can be given to people who need to verify signatures. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/asymmetric_key_cryptography))

As the following sections explain, **encryption, hashing, and digital signatures solve different problems. They cannot simply replace one another.**

---


<a id="en-h026"></a>

<a id="p1-03"></a>

## Part 1 · 3. How do the classroom VMs, Parrot, and Windows Server fit together?

**Study connection — editorial:** Separate the machine, operating system, directory role, remote interface and personal lab entitlement before describing an environment. [Chinese explanation](../handouts-zh/part-01.md#h1-03) · [Audited detail](../course-overview.md#virtualization) · [Source coverage](coverage.md#en-h026). Source section: lines 292–339.


<a id="en-h027"></a>

### 1. A VM is a virtual computer, not another hacking technique

A **virtual machine**, or VM, is a computing environment provided through virtualization. A **hypervisor** manages the relationship between guest operating systems and the underlying hardware resources. ([NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/virtual_machine))

For example, your physical computer may run Ubuntu, while a virtualization platform lets you create a Windows VM. The Ubuntu environment is the host side; Windows inside the VM is the guest operating system.

**Parrot OS is a Linux distribution. A Parrot VM is a virtual machine with Parrot OS installed.** The official documentation describes Parrot as a Debian-based distribution that provides security tools and a working environment. ([Parrot Security](https://parrotsec.org/docs/))

**Correction: The transcript's “para/parent virtual machine” most likely means Parrot VM. It should not be interpreted as the separate technical term “paravirtualization.”** Nor should Parrot be defined as a stripped-down version of Kali with exactly one-fifth as many tools.


<a id="en-h028"></a>

### 2. Lab machines can usually run alongside one another; they do not all need to run inside Parrot

The following is **a teaching example of a configuration, not a reconstruction of the missing classroom whiteboard**:

One physical computer provides the virtualization environment. It contains a Parrot testing VM and one or more Windows or Linux target VMs. They are separate virtual computers that communicate over a designated laboratory network.

In other words, Parrot is one participant in the lab. It is not a place where all the target VMs must live.

The whiteboard is missing from this transcript, so the exact service roles of each Windows Server, the IP-address plan, and whether nested virtualization was used cannot be reliably reconstructed.


<a id="en-h029"></a>

### 3. What are AD and a domain controller?

**Active Directory Domain Services**, or **AD DS**, is a directory service that centrally stores and manages information about users, computers, and resources. It also integrates authentication and access control. A **domain controller** is an important server role that provides these domain services. ([Microsoft Learn](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview))

Teaching example: A company has many computers. Administrators do not want each computer to maintain a separate, unrelated set of employee accounts, so they use centralized directory and account management.

An AD domain is part of an administrative and identity architecture. Do not treat it as identical to a website's domain name just because both use the word “domain.”


<a id="en-h030"></a>

### 4. What counts as a ready-to-use laboratory?

For a course like this, I suggest defining “the lab is ready” as follows: You know each machine's role, understand which communication is allowed, use test data, and have a way to return the environment to a repeatable starting state.

Success does not mean installing as many tools as possible. Nor does it mean simply being able to connect to outside systems.

The six-month online lab access mentioned in class still needs to be checked against the actual purchased package and activation records. The transcript alone cannot establish your personal expiration date.


<a id="en-h031"></a>

### 5. Separate examination facts from classroom advice

At the time of the source's check, the official CEH knowledge-exam information was **exam code 312-50, 125 questions, and 4 hours**. The passing threshold depends on the exam form; the official range given was **60%–85%**. Therefore, the classroom statement that “about 75% is enough to pass” should not be treated as a fixed rule. ([EC-Council Certification Lookup](https://cert.eccouncil.org/certified-ethical-hacker.html))

The checked version also addresses claims such as “you must stay for more than an hour to avoid an investigation,” “the answer with the most votes must be right,” and “you can get an unconditional refund after completing the course.” It marks these, respectively, as unsupported by official rules, an invalid inference, or a claim that ignores applicable conditions. They are not suitable preparation strategies.

The classroom question about a **64-bit block and three DES keys, each with 56 effective key bits**, identifies the historical three-key TDEA/Triple DES algorithm. **Recognizing an algorithm in an exam question does not mean it should be used to design a new system today.** NIST withdrew the related recommendation on **January 1, 2024**. ([NIST Computer Security Resource Center](https://csrc.nist.gov/pubs/sp/800/67/r2/final))

---


<!-- source-derived-text-end -->
