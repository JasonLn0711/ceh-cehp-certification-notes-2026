# CEH13-AI Live Syllabus And Source Decision

## Status

- Source status: `source_preserved`
- Verification date: `2026-09-04`, Asia/Taipei
- Course status: `confirmed` — UCOM / UUU Taipei class `2048`
- Curriculum status: `confirmed course-wide scope`; instructor-specific daily
  allocation remains `pending confirmation`
- External directory decision: `rejected_untrusted`; no files downloaded,
  copied, imported, or used for assessment preparation

## FIRST PRINCIPLE

- Scarce resource: trustworthy study time before the CEH class.
- Canonical home: this CEH / CEHP repository owns the syllabus, technical
  preparation, assessment evidence, and source decisions.
- Planning role: `planning-everything-track` owns the course-time commitment,
  capacity allocation, status, locator, and next gate.
- Evidence path: current UUU course page, EC-Council course outline and
  brochure, EC-Council Aspen courseware instructions, and CEH Candidate
  Handbook.
- Scope control: use official public outlines, licensed supporting references,
  Jason's registered courseware, authorized labs, and isolated toy exercises.
- Next gate: complete the `38 h` evidence-backed readiness sequence by
  `2026-10-11` and obtain the instructor's actual daily module allocation when
  UUU releases it.

## Official Sources

| Source | Role | URL |
| --- | --- | --- |
| UUU CEH13-AI course page | Current class, course objectives, modules, skills, prerequisite, materials, and learner rights | <https://www.uuu.com.tw/Course/Show/3236/1> |
| EC-Council CEH course outline | Module objectives, key topics, and representative labs | <https://www.eccouncil.org/certified-ethical-hacker-online-training/> |
| EC-Council CEH v13 brochure | CEH powered-by-AI framing, learning framework, course outline, and exam context | <https://www.eccouncil.org/wp-content/uploads/2024/09/EC-CEHv13-Course-Brochure-2.pdf> |
| EC-Council Aspen courseware guide | Official access route through a training-center subscription code | <https://aspen.eccouncil.org/Docs/UserGuides/AccessCourseware-UserGuide.pdf> |
| CEH Candidate Handbook v7 | Certification integrity, confidential exam material, and brain-dump restrictions | <https://cert.eccouncil.org/wp-content/uploads/2024/03/CEH-Handbook-v7.pdf> |

## Confirmed Course Identity

| Field | Confirmed value |
| --- | --- |
| Provider | UCOM / UUU, EC-Council authorized training delivery |
| Course | `CEH13-AI` — EC-Council CEH 駭客技術專家認證課程 |
| Class | Taipei `2048` |
| Dates | `2026-10-12` through `2026-10-16` |
| Time | Monday–Friday, `09:00–18:00` |
| Duration | `40 hours` |
| Materials | EC-Council official English materials |
| Audience | Network, system, and information-security practitioners and learners interested in authorized attack-and-defense methods |
| Suggested prerequisite | CND-level blue-team and network-defense capability |
| Official lab right | 180 days from activation |
| Completion certificate | Original course completion certificate after at least `80%` attendance |

## Course Purpose

The course teaches authorized security assessment through attacker methods,
defensive countermeasures, AI-assisted workflows, simulated environments, and
hands-on practice. It covers network and system discovery, vulnerability
assessment, exploitation concepts, detection, remediation, and policy controls.

The provider publishes the twenty-module course-wide sequence. It does not
publish which modules or labs the Taipei `2048` instructor will teach on each
individual day. The dated class-note schedule will be updated from the
instructor's handout or observed delivery rather than inferred as four modules
per day.

## Nine UUU Skill Outcomes

| ID | Provider outcome | Primary module route | Pre-class evidence |
| --- | --- | --- | --- |
| `S01` | Information-security and ethical-hacking foundations | M01 | closed-book authorization and Rules of Engagement explanation |
| `S02` | AI-assisted ethical-hacking methods | M01–M20 cross-module workflow | governed AI-use note with human verification and scope control |
| `S03` | Network intelligence gathering | M02–M04 | authorized discovery scenario and evidence interpretation |
| `S04` | Vulnerability scanning of systems and networks | M03 and M05 | isolated scan or supplied-output analysis with remediation priority |
| `S05` | Security testing across systems, networks, websites, mobile, wireless, IoT, and cloud | M06 and M11–M19 | one safe artifact for each platform family |
| `S06` | Malware and AI-related malware concepts and detection | M07 | static evidence-analysis exercise and control selection |
| `S07` | Social-engineering assessment of organizational awareness | M09 | consent-based scenario design and defensive verification workflow |
| `S08` | Recognition and mitigation of DoS and DDoS | M10 | traffic/evidence scenario and resilience response |
| `S09` | Cryptographic protection of data | M20 | hashing, encryption, certificate, and misuse explanation |

## Comprehensive Twenty-Module Syllabus

### M01 — Introduction to Ethical Hacking

- Purpose: establish information-security objectives, ethical-hacking roles,
  legal authority, standard procedures, and engagement governance.
- Core topics: information-security elements, attacker classes, the hacking
  lifecycle, Cyber Kill Chain, MITRE ATT&CK, risk and incident management,
  information assurance, legal and compliance context.
- Pre-class evidence: mock Rules of Engagement, one authorized localhost
  request, two correct refusals, retained evidence, and delayed retrieval.

### M02 — Footprinting and Reconnaissance

- Purpose: gather information that defines a target's exposed footprint.
- Core topics: passive and active footprinting, search and public sources,
  websites, email, WHOIS, DNS, traceroute, mirroring, competitive intelligence,
  and exposure reduction.
- Pre-class evidence: a bounded reconnaissance plan against a toy or expressly
  authorized target, with source provenance and a defensive exposure review.

### M03 — Scanning Networks

- Purpose: identify live hosts, ports, services, versions, and operating-system
  indicators inside an authorized range.
- Core topics: host discovery, port scanning, service/version discovery,
  banner grabbing, OS fingerprinting, scan interpretation, evasion concepts,
  countermeasures, and false-positive control.
- Pre-class evidence: interpret or produce one isolated discovery result and
  distinguish host discovery, service discovery, and vulnerability claims.

### M04 — Enumeration

- Purpose: obtain service-specific information after discovery establishes an
  authorized attack surface.
- Core topics: NetBIOS, SNMP, LDAP, NTP, NFS, SMTP, DNS, IPsec, VoIP, RPC,
  SMB, FTP, and Unix/Linux user enumeration with associated controls.
- Pre-class evidence: map a supplied service inventory to the next authorized
  enumeration question and record why scanning and enumeration differ.

### M05 — Vulnerability Analysis

- Purpose: identify, classify, verify, prioritize, and report weaknesses.
- Core topics: vulnerability research, scoring systems and databases,
  assessment types and tools, vulnerability-management lifecycle, reports,
  exploitability, asset context, and remediation priority.
- Pre-class evidence: triage a small finding set and distinguish scanner output,
  verified vulnerability, exploitability, impact, and remediation evidence.

### M06 — System Hacking

- Purpose: understand how credentials, exploitation, privilege escalation,
  persistence, artifacts, and cleanup affect a system assessment.
- Core topics: password attacks, exploitation, buffer overflow, privilege
  escalation, keyloggers and spyware, rootkits, steganography and steganalysis,
  persistence, post-exploitation, logs, and track-covering indicators.
- Pre-class evidence: use an isolated scenario to identify the minimum proof,
  containment action, evidence to preserve, and stop condition.

### M07 — Malware Threats

- Purpose: recognize malware families, behavior, evidence, analysis methods,
  and countermeasures.
- Core topics: Trojans, viruses, worms, ransomware, exploit kits, APT,
  fileless malware, static and dynamic analysis, detection, containment, and
  AI-related malware concepts.
- Pre-class evidence: analyze benign metadata or supplied indicators without
  executing unknown code; propose containment and verification steps.

### M08 — Sniffing

- Purpose: understand packet capture, local-network manipulation, evidence,
  detection, and prevention.
- Core topics: promiscuous capture, wiretapping, MAC flooding and spoofing,
  DHCP starvation, ARP spoofing/poisoning, STP attacks, DNS poisoning, MITM,
  packet analysis, and detection controls.
- Pre-class evidence: inspect an authorized packet capture and explain what it
  proves, what it cannot prove, and which controls reduce the exposure.

### M09 — Social Engineering

- Purpose: evaluate human-facing security risk through consent-based,
  governed assessment methods.
- Core topics: social-engineering types, phishing, identity theft, insider
  threats, verification failures, awareness testing, reporting, and controls.
- Pre-class evidence: design a no-send assessment scenario with explicit
  authorization, participant protection, measurement, stop, and reporting rules.

### M10 — Denial-of-Service

- Purpose: recognize DoS/DDoS mechanisms, evidence, resilience controls, and
  incident response.
- Core topics: DoS, DDoS, botnets, common techniques and tools, detection,
  rate and resource controls, upstream coordination, and recovery.
- Pre-class evidence: analyze a synthetic traffic incident and select detection,
  mitigation, escalation, and recovery actions; no live flooding is performed.

### M11 — Session Hijacking

- Purpose: identify weaknesses in session management, authentication,
  authorization, transport, and client behavior.
- Core topics: application- and network-level hijacking, fixation, replay,
  client-side attacks, man-in-the-browser, TCP/IP hijacking, CRIME, detection,
  token controls, and prevention.
- Pre-class evidence: inspect a toy session flow and identify secure cookie,
  rotation, expiry, transport, replay, and logging controls.

### M12 — Evading IDS, Firewalls, and Honeypots

- Purpose: understand how perimeter and endpoint detection can fail and how
  layered defenses improve coverage.
- Core topics: IDS/IPS, firewall types, honeypots, tunneling and fragmentation
  concepts, endpoint/NAC evasion, detection gaps, telemetry, and compensating
  controls.
- Pre-class evidence: compare a synthetic event with firewall, IDS, endpoint,
  and honeypot evidence and identify the missing detection layer.

### M13 — Hacking Web Servers

- Purpose: assess web-server infrastructure, configuration, services, patches,
  and logging.
- Core topics: server operation and reconnaissance, service enumeration, web
  server attacks, DNS hijacking, defacement, cache poisoning, patch management,
  audit methodology, and defensive tools.
- Pre-class evidence: review a local server configuration and produce a
  prioritized hardening and verification checklist.

### M14 — Hacking Web Applications

- Purpose: assess application architecture, exposed functionality, data flow,
  APIs, and common application weaknesses.
- Core topics: application architecture and threats, OWASP risks, spidering,
  reconnaissance, vulnerability scanning, authentication attacks, CSRF, XSS,
  web APIs, webhooks, web shells, and secure-development controls.
- Pre-class evidence: identify and remediate an intentionally vulnerable local
  application behavior using the smallest proof required.

### M15 — SQL Injection

- Purpose: understand injection mechanisms, evidence, testing methodology,
  detection, and prevention.
- Core topics: SQL injection types, blind injection, query construction,
  methodology, tools, signature evasion concepts, detection, parameterized
  queries, validation, and least privilege.
- Pre-class evidence: compare vulnerable and parameterized queries in a local
  toy example and record the evidence and remediation.

### M16 — Hacking Wireless Networks

- Purpose: assess wireless discovery, authentication, encryption, traffic,
  rogue access, and Bluetooth risks.
- Core topics: wireless terminology, WEP/WPA/WPA2, discovery, traffic analysis,
  cracking methodology, rogue access points, Bluetooth threats, auditing, and
  security controls.
- Pre-class evidence: analyze supplied capture/configuration evidence and
  recommend modern authentication, encryption, segmentation, and monitoring.

### M17 — Hacking Mobile Platforms

- Purpose: understand mobile attack surfaces, application/device controls,
  platform security, and management.
- Core topics: mobile attack vectors, OWASP mobile risks and controls,
  sandboxing, smishing, Android rooting/ADB/APK concepts, iOS jailbreaking,
  application security, device security, and MDM.
- Pre-class evidence: threat-model a toy mobile application and identify
  storage, transport, identity, permission, update, and device-control evidence.

### M18 — IoT and OT Hacking

- Purpose: understand connected-device and industrial-control architectures,
  evidence, attack paths, safety, and defensive segmentation.
- Core topics: IoT architecture and communication models, OWASP IoT risks,
  firmware and traffic exposure, IIoT, IT/OT convergence, ICS/SCADA,
  vulnerabilities, attack methodology, monitoring, and safety controls.
- Pre-class evidence: analyze a synthetic IoT/OT data flow and define trust
  boundaries, safe evidence collection, segmentation, and human stop authority.

### M19 — Cloud Computing

- Purpose: assess cloud identity, storage, network, workload, container,
  orchestration, and serverless risks under shared responsibility.
- Core topics: service and deployment models, providers, fog/edge computing,
  object storage, IAM, containers, Docker, Kubernetes, serverless, cloud risks,
  attack paths, logging, and security controls.
- Pre-class evidence: review a synthetic IAM and storage policy, identify
  excessive privilege or exposure, and state a safe remediation and verification.

### M20 — Cryptography

- Purpose: use and evaluate cryptographic mechanisms for integrity,
  confidentiality, identity, and protected storage.
- Core topics: cryptography and ciphers, hashes, symmetric and asymmetric
  encryption, algorithms, PKI, certificates, email and disk encryption, key
  stretching, attacks, cryptanalysis concepts, and common misuse.
- Pre-class evidence: hash a local artifact, verify integrity, use a toy
  encryption/certificate workflow, and explain the security property each step
  does and does not provide.

## Learning Framework And Depth Boundary

EC-Council describes CEH v13 as a twenty-module program with `221` hands-on
labs and a design that gives substantial course time to practical work. The
pre-class plan establishes concept retrieval, defensive reasoning, authorized
practice, and representative skill evidence. It does not claim completion of
every official lab before Jason receives and uses the licensed environment.

## External Directory Assessment

The user supplied:

`https://elhacker.info/Cursos/CEHv13/CEH%20v13%20PDF/`

Read-only inspection on `2026-09-04` showed a third-party directory containing
large PDFs labeled as CEHv13 module manuals, a lab manual, appendices, exam
sets, practice questions, and a file named `cehv13dump.pdf`.

Decision:

- The directory is not an EC-Council or UUU domain and provides no verified
  license or authorized-training provenance.
- Public reachability does not establish permission to copy commercial
  courseware.
- The exam-set and dump labels create a direct certification-integrity risk.
- This source is classified `rejected_untrusted`.
- No linked PDF, archive, ISO, virtual machine, executable, video, exam set,
  dump, or malware-related artifact enters the study repository.
- Jason's official courseware path is the UUU-issued EC-Council subscription
  code redeemed through Aspen. The registered course, official public outline,
  owned supporting references, and authorized lab environment provide the
  approved preparation path.

## Source Trust Register

| Class | Meaning | Current sources |
| --- | --- | --- |
| `official_primary` | Issuer or registered training provider; defines course scope and rights | UUU and EC-Council pages, brochure, Aspen guide, candidate handbook |
| `licensed_supporting` | Lawfully held reference used under the official course scope | registered Aspen courseware when issued; Matt Walker 2025 study guide in private Drive |
| `rejected_untrusted` | Provenance, copyright permission, safety, or exam-integrity controls do not support use | `elhacker.info` CEHv13 directory and its exam/dump files |

## Adopted Readiness Decision

The pre-class target is `evidence-backed syllabus readiness`:

- all twenty modules attempted and assessed;
- all nine UUU skill outcomes connected to learner evidence;
- one authorized exercise, evidence-analysis task, or defensive scenario for
  each module;
- every module reaches `pass` for a full readiness claim;
- Form B reaches `>=75%` with zero critical-safety errors;
- remaining official-lab work stays visible as a licensed-environment
  activation path.

If any module remains below `pass`, the truthful closeout is
`coverage complete; readiness incomplete`, followed by a class-entry gap brief.

## Connections

- Course scope: `../../curriculum/official-scope-map.md`
- Reference policy: `../../curriculum/important-references.md`
- Pre-course schedule: `../../study-plan/pre-course-prep.md`
- Assessment system: `../../docs/assessment-governance-system.md`
- Planning locator:
  `../../../planning-everything-track/data/projects/2026-07-ceh-cehp-certification-training.md`
