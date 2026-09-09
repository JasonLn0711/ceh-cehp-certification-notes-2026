# Forgotten Portal Discovery — opening lesson

**Our central question is: “Does what actually runs match what the organization has recorded, and who is responsible for any difference?”**

This is not an exploitation exercise. Your lab asks you to discover services within a very small authorized boundary, compare the results with a supplied register, and preserve evidence without claiming more than it establishes. We have not yet seen your command outputs, so no practical step counts as completed. 

The supplied fictional register is:

| Port   | Recorded service | Recorded owner      |
| ------ | ---------------- | ------------------- |
| `8765` | public portal    | Digital Services    |
| `8767` | observability    | Platform Operations |

The brief says the Python mock starts three services and deliberately leaves one out of this register. That is information supplied by the exercise—not yet a discovery you have demonstrated. 

Keep this distinction in mind throughout:

> **What the instructions promise, what a program reports, what you observe, and what you can conclude are different things.**

## 1. Authorization: what you may do, where, and when

### Permission is not the same as technical access

**Authorization** means permission from someone entitled to approve the activity. In this lab, you act as the owner and operator of the supplied local mock. Being able to connect to a service does not itself give permission to test it. Likewise, owning the mock does not mean this exercise authorizes testing every other program on your computer. 

**Scope** is the boundary of that permission. A **target** is the particular thing you may examine; a **method** is the way you may examine it. Here, the target is exactly `127.0.0.1`, TCP ports `8765–8767`. The methods include inspecting the supplied register, performing at most two TCP connect scans, and sending HTTP `GET` requests only to `/health` and `/service-info`. Changing a port or requesting another path changes the authorized activity, even when the address stays the same. 

The **Rules of Engagement**, or **ROE**, are the written instructions that bring these limits together: who authorizes the work, what is allowed, when it may happen, and when it must stop. They are established before testing, not written afterward to justify whatever happened. NIST describes ROE as the guidelines and constraints governing a security test. ([NIST Computer Security Resource Center][1])

For example, “I may inspect my local mock during this dated window using these specific methods” is meaningful authorization. “It is only a local address, so anything is allowed” is not.

### Limits must control the activity, not merely describe it

**Request control** limits which interactions you make and how many. **Rate control** limits how quickly you make them. Your brief specifies default local Nmap timing and a maximum of two TCP connect scans. Two is a ceiling, not a requirement to scan twice. The brief does not specify a numerical requests-per-second limit, so we should not invent one. 

A **stop condition** is an event that requires you to pause. For this exercise, stop for a port conflict, unclear scope, a non-loopback target, unexpected sensitive data, instability, or an expired window. For example, a message that a required port is already occupied is a blocker—not an invitation to choose a nearby port. 

**Resumption authority** identifies who may approve continuing under changed conditions. Here, you must write a dated owner amendment before changing the target, methods, window, or another authorized action. Finding something interesting does not automatically extend permission. 

**Evidence handling** means collecting, identifying, preserving, and protecting the records of the work. In our lab, that means keeping the ROE, logs, transcripts, metadata, analysis, and hash records. An explanation written by me can help you learn, but it cannot substitute for output you actually produced.  

## 2. Assets and ownership: why finding a service is only the beginning

An **asset** is something of value that an organization needs to manage or protect. It can be a physical computer, software, a service, or information—not just an expensive device. In this exercise, the running services are the assets we are examining. ([NIST Computer Security Resource Center][2])

An **asset inventory** is an organized, maintained record of assets and their relevant attributes. A list becomes useful when it supports decisions: what exists, where it is, what it does, and who is responsible. Merely having a spreadsheet does not establish that its contents are complete or current. ([Cyber.gov.au][3])

A **service register** is the service-focused record used in this exercise. Its two rows tell us what has been recorded about two ports. They do not independently establish that those services are currently running, that no other service exists, or that the named teams still accept responsibility. We will compare the register with new evidence rather than treating it as a perfect description of reality. 

### An owner is an accountable role, not a network property

A **system owner** has overall responsibility for a system’s development, operation, maintenance, or related lifecycle decisions. A **service owner** is accountable for a particular service and its outcomes. These roles may overlap, but they are not automatically the same person as the administrator who can restart a process. ([NIST Computer Security Resource Center][4])

**Accountability** means being answerable for ensuring that necessary decisions and work happen. For example, an owner may arrange patching rather than personally install every patch. Knowing who performs a task is therefore related to—but not identical to—knowing who must ensure its completion. ([DDaT Capability Framework][5])

In this lab, distinguish your real role as owner/operator of the mock from the fictional organizational owners in the register. You can know that you launched the mock while still recording that a fictional service lacks a recorded business owner. Those statements do not conflict.  

An **ownership gap**, as we will use the term, is missing or unresolved responsibility in the available records. “No owner appears in this register” is supportable from a missing entry. “Nobody anywhere is responsible” is a much stronger claim that the register alone cannot establish. The asset map must keep that distinction visible. 

**Shadow IT** refers to business-used technology that is outside the organization’s normal asset-management and IT processes. An undocumented service may be a lead suggesting shadow IT, but a missing register entry alone does not prove deliberate rule-breaking or malicious intent. It could reflect an incomplete record. ([National Cyber Security Centre][6])

The **attack surface** is the collection of places where an attacker could attempt to enter a system, affect it, or obtain information. A listening service contributes an interface to examine; its existence does not automatically mean it contains an exploitable weakness. In this exercise, we inspect only the tiny portion of the surface covered by the ROE. ([NIST Computer Security Resource Center][7])

## 3. Reconnaissance, scanning, and enumeration are different activities

Think of these activities as answering increasingly specific questions.

### Passive reconnaissance: “What do existing records tell us?”

**Reconnaissance** is information gathering about a target. **Passive reconnaissance** gathers information without directly probing the target service.

Reading the supplied register is passive because you are examining an existing document, not sending requests to the mock. It can establish what that document records. It cannot establish present-day reachability. The important distinction is the interaction, not whether you use a terminal or a graphical application. 

### Active reconnaissance: “What happens when we contact it?”

**Active reconnaissance** deliberately interacts with the target to obtain information. A connection attempt or an HTTP request is active because it causes the target’s networking or application components to respond.

“Read-only” does not mean “passive.” Asking a server for information is still an active interaction, even when the request is not intended to change its data. NIST distinguishes passive observation from active discovery that sends queries to obtain responses. ([NIST Publications][8])

### Scanning and service discovery: “What appears reachable?”

**Scanning** is systematic probing of selected targets or interfaces. Here, it means testing the three approved TCP ports.

**Service discovery** is the task of identifying available services. A port scan contributes to that task by finding listening ports, but it may not identify the actual application. For example, finding an open port answers a reachability question; determining whether it speaks HTTP requires additional evidence. ([Nmap][9])

### Enumeration: “What details does this service provide?”

**Enumeration** gathers structured, service-specific information. In this lab, requesting `/service-info` is enumeration because it asks each service for details beyond whether a connection is possible.

Suppose a future response contains a role and a version. The immediate observation would be that the response contains those values. It would not independently prove the organization’s ownership arrangements or the presence of a vulnerability. 

### Validation, vulnerability assessment, and exploitation

**Validation** checks a particular claim against suitable evidence. The method depends on the claim. A saved HTTP response can validate that certain metadata was returned; it cannot, by itself, validate that the metadata accurately describes the deployed software. An ownership claim requires ownership evidence, not merely another connection attempt. This is why the lab distinguishes established facts, claimed metadata, and open validation. 

A **vulnerability assessment** examines potential weaknesses and their security significance. It asks more than “What is running?” A service can be reachable without being vulnerable, and identifying a weakness does not necessarily require exploiting it. ([NIST Computer Security Resource Center][10])

**Exploitation** means using a weakness to produce an effect, such as obtaining access that should not be available. It is different from collecting a version string or identifying a possible weakness. Your exercise explicitly excludes exploitation, credential testing, brute force, and other unlisted activity. Finding an omitted service does not change that boundary. ([NIST Computer Security Resource Center][11]) 

## 4. What the network terms actually mean

### IPv4, loopback, and localhost

**IPv4** means Internet Protocol version 4. It uses 32-bit addresses, commonly written as four numbers separated by dots. `127.0.0.1` is an IPv4 address. The dots are a readable notation for an address—not a description of a service or its owner. ([RFC Editor][12])

A **loopback address** directs communication back into the local networking environment rather than to another machine over the ordinary network. `127.0.0.1` belongs to IPv4’s reserved loopback range. For this exercise, however, permission covers that exact address—not every address in the loopback range. ([IANA][13]) 

**Localhost** is a special hostname associated with loopback. It is a name, whereas `127.0.0.1` is a numeric address. Localhost may also resolve to the IPv6 loopback address, `::1`. We therefore retain the exact numeric target from the ROE rather than assuming the two forms are interchangeable for this exercise. ([RFC Editor][14])

A useful practical question is always: “Local to the environment where which command is running?” Do not assume a command inside a separate virtual machine or container is examining the host environment you intended.

### TCP, ports, and listening sockets

**TCP**, the Transmission Control Protocol, provides a connection-oriented, ordered byte stream between applications. A **port** is a numbered transport endpoint used to distinguish communication destinations within a host. In our lab, the address selects the local target and the port selects one of the interfaces being examined. A port number is not a physical connector or a business owner. ([RFC Editor][15])

A **listening socket** is an operating-system networking endpoint waiting for incoming connections. For our mock, the intended listeners use the approved local address and ports. “Listening” describes networking state; it does not establish that every application function works. ([RFC Editor][15])

The **TCP three-way handshake** establishes a normal TCP connection: the client sends a synchronization request, the server acknowledges it and sends its own synchronization information, and the client acknowledges that. These messages are commonly abbreviated `SYN`, `SYN-ACK`, and `ACK`. The exchange establishes transport connectivity, not a successful application transaction or authorization to use the application. ([RFC Editor][15])

A **TCP connect scan** asks the operating system to attempt ordinary TCP connections. Nmap selects this method with `-sT`. Successful connections to listening ports complete the connection process; this is not merely reading a local list of port names. ([Nmap][16])

Consequently, an `open` result supports a bounded conclusion about reachability from the scanning environment at that time. It does not establish business ownership, Internet exposure, or vulnerability. Also, reading Nmap’s result is not the same as personally capturing and inspecting the handshake packets. ([Nmap][9])

### HTTP, GET, and endpoints

**HTTP**, the Hypertext Transfer Protocol, defines application-level requests and responses. An **HTTP service** is an application that accepts such requests. In this mock, those requests travel over TCP.

An **HTTP `GET`** requests a representation of a resource. It has read-oriented semantics, but that does not guarantee absolutely no side effects: a server may still record the request, for example. Nor does the name `GET` provide permission to request any resource you discover. ([RFC Editor][17])

An **endpoint**, in this lesson, is a specific requestable interface within a service. Consider this address as an illustration, not an instruction to run anything yet:

```text
http://127.0.0.1:8765/service-info
```

It specifies the HTTP scheme, target address, port, and path. Your ROE permits only two paths: `/health` and `/service-info`. The brief uses `/service-info` for metadata enumeration; it does not provide the complete response schema for either path. We must inspect actual responses rather than invent their contents. A health response would not, by itself, certify that the whole service is secure.  

### Labels, banners, roles, and versions

A **port-number service label** is a name associated with a port in a lookup table. Nmap’s `SERVICE` column can come from such an association. Software can run on an unexpected port, so a familiar label is not independent confirmation of the application.

A **banner** is identifying information presented by a service, such as a software name or version. Unlike a port-number label, it comes from the service’s communications—but it remains information to interpret, not an unquestionable guarantee. Nmap’s documentation explicitly separates port-based identification from additional service and version probing. ([Nmap][18])

A **role** describes a service’s claimed function, such as “public portal.” **Version metadata** describes a claimed software release. A role is not an owner, and a release string is not proof of vulnerability. In this lab, these values belong in the “claimed metadata” category until the relevant claims have been validated.  

## 5. Evidence: preserving what happened without overstating it

### The different records serve different purposes

An **artifact** is a saved product of the work: a log, transcript, metadata file, or analysis document. An artifact is not automatically good evidence for every claim. Its usefulness depends on what produced it and what it actually contains. Your brief requires several distinct artifacts because no single record answers every question. 

A **terminal transcript** records terminal activity and output. The lab uses `script` to capture the Nmap session. This helps preserve the displayed scan results, but it is not a packet capture or an independent guarantee that every displayed statement is true. ([Ubuntu Manpages][19])

A **server log** records what the server is configured to report. It gives the server-side perspective, while the scan transcript gives the scanning-side perspective. Missing log entries do not automatically prove that nothing happened; logging has coverage limits. In this exercise, the actual mock implementation and output will determine what `server.log` contains. 

An **asset map** organizes discovered targets, evidence, claimed metadata, recorded owners, gaps, and next actions. A **decision log** explains what you conclude, what remains unresolved, and why a particular next action is appropriate. The map organizes the situation; the decision log records the reasoning. Neither should replace or rewrite the underlying raw evidence. 

### Provenance and integrity answer different questions

**Provenance** means origin and history: where a record came from and how it was produced or handled. For example, a transcript associated with a command, operator, environment, and time has more useful provenance than an unexplained text snippet. A filename alone is not a trustworthy history. ([NIST Computer Security Resource Center][20])

**Integrity** concerns protection against improper alteration. For our saved files, a central question is whether their bytes have changed since a recorded reference point. Integrity is different from truth: an unchanged file can still contain an incorrect statement. ([NIST Computer Security Resource Center][21])

A **hash** is a calculated digest of data. **SHA-256** is the particular hash algorithm used here, producing a 256-bit digest. Think of it as a compact value for comparing file contents—not encryption and not a certificate that an experiment was performed correctly. ([Ubuntu Manpages][22])

`sha256sum --check` reads recorded expected hashes, calculates hashes for the named files, and compares them. A successful check establishes that the calculated and recorded digest values match. It supports an unchanged-content claim relative to that reference; it does not establish who created the files, whether their contents are true, or whether the manifest itself is trustworthy. ([Ubuntu Manpages][22])

There is a detail in the supplied procedure to watch at closeout: it checks hashes before stopping the mock. A later write to `server.log` would change the file after that check. Also, its listed hash command covers five named artifacts, not the ROE or register. We must not describe unlisted files as hash-verified. 

### Use precise language for conclusions

For this lab, use these distinctions:

| Term                | Meaning and correct use                                                                            | Tempting overstatement                                             |
| ------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Observation**     | What you directly saw, such as a particular line in your actual output.                            | “I observed every underlying network event.”                       |
| **Evidence**        | A preserved record that supports a specified claim.                                                | “Any screenshot proves the whole test.”                            |
| **Inference**       | A conclusion drawn from observations and assumptions.                                              | Presenting a likely explanation as directly observed.              |
| **Finding**         | A supported assessment conclusion, such as an observed service missing from the supplied register. | Declaring the service malicious because it is omitted.             |
| **Validation lead** | Information identifying a question worth checking next, such as a reported version.                | Treating the lead as a confirmed vulnerability.                    |
| **Proof**           | Evidence sufficient for a precisely bounded claim under stated assumptions.                        | Claiming complete security or complete compromise from one result. |

These distinctions implement the brief’s requirement to separate direct observations, inferences, claimed metadata, and unresolved validation.  

The practical habit is simple: **after each conclusion, ask, “Which artifact supports this exact claim, and what does it leave unanswered?”**

## 6. Real-world anchor: the 2017 Equifax breach

The affected system was Equifax’s **Automated Consumer Interview System**, or **ACIS**, dispute portal. The FTC complaint describes intrusions between **May 13 and July 30, 2017**, with public disclosure on **September 7, 2017**. The complaint and settlement announcement are dated **July 22, 2019**. ([Federal Trade Commission][23])

According to the complaint, the portal contained an unpatched Apache Struts vulnerability. The patch instruction did not reach the employee responsible for maintaining the portal. A March 15 scan failed to identify vulnerable systems because the scanner was not configured to cover all potentially vulnerable assets; Equifax’s inventory of public-facing Struts technology was also inaccurate. ([Federal Trade Commission][23])

The complaint further describes inadequate **network segmentation**—separation intended to limit access between parts of a network—and weak detection. Attackers reached unrelated databases. Expired certificates prevented tools from inspecting suspicious encrypted traffic, and legacy systems lacked file-integrity monitoring. These are allegations documented in the FTC complaint, not findings from our lab. ([Federal Trade Commission][23])

The FTC announcement reported that the breach affected approximately **147 million people**. The operational consequence was not merely an inaccurate inventory: attackers obtained enormous amounts of sensitive personal information. ([Federal Trade Commission][24])

Direct sources: [FTC settlement announcement](https://www.ftc.gov/news-events/news/press-releases/2019/07/equifax-pay-575-million-part-settlement-ftc-cfpb-states-related-2017-data-breach) and [FTC complaint](https://search.ftc.gov/system/files/documents/cases/172_3203_equifax_complaint_7-22-19.pdf).

**The lesson I draw for our exercise:** asset visibility tells you what needs attention; configuration assurance checks whether the scanner actually examines that population; ownership makes someone answerable for acting and confirming completion. A scan that reports no vulnerabilities is not reassuring when you have not established its coverage.

The fictional Northbridge Learning Clinic mock does **not** recreate Equifax. It isolates a smaller learning problem: discovering a register gap and handling the resulting evidence and ownership questions. 

### Additional case: NASA’s Jet Propulsion Laboratory

**Event:** compromise discovered in April 2018. **Source:** NASA Office of Inspector General report published June 18, 2019. The report concerns JPL, an attacker, and JPL’s connected mission-network environment. ([NASA Office of Inspector General][25])

The report connects the incident to an unauthorized Raspberry Pi on JPL’s network and describes incomplete asset records. It also describes a compromised external-user account, movement across the network, and theft of approximately 500 megabytes from 23 files. The public report does not justify inventing a specific initial exploit or assuming default passwords were involved. ([NASA Office of Inspector General][25])

My takeaway is that an unrecorded device or service can escape the processes that depend on the inventory. However, “Raspberry Pi” is not itself a vulnerability, just as “omitted portal” will not automatically mean “exploitable portal” in our lab.

Direct source: [NASA OIG report IG-19-022](https://oig.nasa.gov/docs/IG-19-022.pdf).

## 7. The concept map

```text
AUTHORIZATION AND ROE
Define target, methods, timing, limits, and stop conditions.
                         |
                         v
PASSIVE RECONNAISSANCE
Read and preserve the supplied register.
Question: What is recorded?
                         |
                         v
ACTIVE SCANNING
Attempt approved TCP connections.
Question: What is reachable from here, now?
                         |
                         v
ENUMERATION
Request only approved service information.
Question: What does each service claim?
                         |
                         v
EVIDENCE PRESERVATION AND INTEGRITY
Keep the records, their origins, and verified hashes.
Question: What supports each claim?
                         |
                         v
OWNERSHIP-AWARE ASSET MAP
Compare observations with the register.
Question: What is missing or unresolved?
                         |
                         v
NEXT AUTHORIZATION DECISION
Record what may happen next and what needs new permission.
```

Evidence capture runs throughout this process; it is not something we reconstruct from memory at the end. The map follows the sequence required by your brief.  

## Your first task: state the ROE in your own words

**Do not start the mock or run a scan yet.**

Write a short authorization statement covering who authorizes the work, the exact address and ports, permitted methods, the two-scan ceiling, timing controls, prohibited activities, stop conditions, evidence preservation, and the dated amendment needed before any change.

Include an actual date and start/end times for your **70-minute learning block**, plus a dated **active scan window within that block**, using `Asia/Taipei`. Choose the times you genuinely intend to use; do not backdate them.

Also tell me whether `mock_services.py` is already on your computer. The uploaded text names that script but does not contain its implementation, so its behavior and self-test results remain unverified. 

[1]: https://csrc.nist.gov/glossary/term/rules_of_engagement "Rules of Engagement (ROE) - Glossary | CSRC"
[2]: https://csrc.nist.gov/glossary/term/asset "asset - Glossary | CSRC"
[3]: https://www.cyber.gov.au/business-government/secure-design/operational-technology-environments/foundations-for-ot-cybersecurity-asset-inventory-guidance-for-owners-and-operators?utm_source=chatgpt.com "Asset inventory guidance for owners and operators"
[4]: https://csrc.nist.gov/glossary/term/information_system_owner "information system owner (or program manager) - Glossary | CSRC"
[5]: https://ddat-capability-framework.service.gov.uk/role/service-owner?utm_source=chatgpt.com "Service owner"
[6]: https://www.ncsc.gov.uk/guidance/shadow-it?utm_source=chatgpt.com "Shadow IT guidance"
[7]: https://csrc.nist.gov/glossary/term/attack_surface "attack surface - Glossary | CSRC"
[8]: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-115.pdf "Technical guide to information security testing and assessment"
[9]: https://nmap.org/book/man-port-scanning-basics.html?utm_source=chatgpt.com "Port Scanning Basics"
[10]: https://csrc.nist.gov/glossary/term/vulnerability_assessment "vulnerability assessment - Glossary | CSRC"
[11]: https://csrc.nist.gov/glossary/term/penetration_testing "penetration testing - Glossary | CSRC"
[12]: https://www.rfc-editor.org/rfc/rfc791.html "www.rfc-editor.org"
[13]: https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml "IPv4 Special-Purpose Address Space"
[14]: https://www.rfc-editor.org/rfc/rfc6761.html "www.rfc-editor.org"
[15]: https://www.rfc-editor.org/rfc/rfc9293.html "RFC 9293: Transmission Control Protocol (TCP)"
[16]: https://nmap.org/book/man-port-scanning-techniques.html "Port Scanning Techniques | Nmap Network Scanning"
[17]: https://www.rfc-editor.org/rfc/rfc9110.html "RFC 9110: HTTP Semantics"
[18]: https://nmap.org/book/man-version-detection.html "Service and Version Detection | Nmap Network Scanning"
[19]: https://manpages.ubuntu.com/manpages/noble/man1/script.1.html "Ubuntu Manpage: script - make typescript of terminal session"
[20]: https://csrc.nist.gov/glossary/term/provenance "provenance - Glossary | CSRC"
[21]: https://csrc.nist.gov/glossary/term/integrity "integrity - Glossary | CSRC"
[22]: https://manpages.ubuntu.com/manpages/noble/en/man1/sha256sum.1.html "Ubuntu Manpage: sha256sum - compute and check SHA256 message digest"
[23]: https://search.ftc.gov/system/files/documents/cases/172_3203_equifax_complaint_7-22-19.pdf "Equifax, Inc.: Complaint for Permanent Injunction and Other Relief - July 22, 2019"
[24]: https://www.ftc.gov/news-events/news/press-releases/2019/07/equifax-pay-575-million-part-settlement-ftc-cfpb-states-related-2017-data-breach "Equifax to Pay $575 Million as Part of Settlement with FTC, CFPB, and States Related to 2017 Data Breach | Federal Trade Commission"
[25]: https://oig.nasa.gov/docs/IG-19-022.pdf "Final Report - IG-19-022 - Cybersecurity Management and Oversight at the Jet Propulsion Laboratory"
