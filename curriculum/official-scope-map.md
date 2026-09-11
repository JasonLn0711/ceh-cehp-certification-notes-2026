# Official Scope Map

## Source Boundary

This map uses the current UUU `CEH13-AI` page and EC-Council CEH v13 public
course outline checked on `2026-09-04`. The structured source record is:

`../source/2026-09-04-ceh13-ai-live-syllabus-and-source-decision/source.md`

Use official scope as the study backbone. Add explanations from
`important-references.md` only after their source and licensing class is clear.

## CEH13-AI Course Scope

| Order | Module | Required preview outcome | Safe practice mode | CEHP bridge |
| --- | --- | --- | --- | --- |
| 1 | Introduction to Ethical Hacking | explain authorization, scope, methods, time, reporting, evidence, and stop/resume control | mock ROE plus authorized localhost exercise | governance for P1–P5 |
| 2 | Footprinting and Reconnaissance | distinguish passive and active discovery and reduce exposed information | bounded toy-target reconnaissance plan | supports P1–P2 |
| 3 | Scanning Networks | interpret host, port, service, version, and OS discovery without overstating evidence | isolated scan or supplied-output analysis | P1 and P2 |
| 4 | Enumeration | select service-specific enumeration after authorized discovery | supplied-service scenario | P2 |
| 5 | Vulnerability Analysis | separate scanner output, verified weakness, exploitability, impact, and remediation priority | triage a small finding set | P1 |
| 6 | System Hacking | explain credential, exploitation, privilege, persistence, artifact, and cleanup evidence | isolated compromise scenario | P4 |
| 7 | Malware Threats | distinguish malware families, behavior, analysis evidence, containment, and AI-related malware concepts | benign static evidence analysis | P4 |
| 8 | Sniffing | explain capture, local-network manipulation, detection, and countermeasures | authorized packet-capture analysis | P3 |
| 9 | Social Engineering | design a consent-based awareness assessment with participant protection and reporting | no-send scenario | cross-cutting human risk |
| 10 | Denial-of-Service | explain availability mechanisms, detection, mitigation, escalation, and recovery | synthetic incident analysis; no live flooding | P4 |
| 11 | Session Hijacking | identify session, authentication, authorization, transport, and replay controls | toy session-flow review | P3 |
| 12 | Evading IDS, Firewalls, and Honeypots | explain detection gaps and compensating telemetry | layered-evidence comparison | P4 |
| 13 | Hacking Web Servers | assess server exposure, services, configuration, patching, and logs | local configuration review | P2 and P5 |
| 14 | Hacking Web Applications | identify application and API weaknesses and the minimum safe proof | intentionally vulnerable local app analysis | P5 |
| 15 | SQL Injection | explain injection evidence, testing methodology, parameterization, validation, and least privilege | local vulnerable/parameterized query comparison | P5 |
| 16 | Hacking Wireless Networks | explain authentication, encryption, traffic, rogue-access, and Bluetooth risks | supplied capture/configuration analysis | P3 |
| 17 | Hacking Mobile Platforms | threat-model mobile application, device, data, permission, update, and MDM controls | toy mobile data-flow review | adjacent practical scope |
| 18 | IoT and OT Hacking | explain device, firmware, traffic, segmentation, ICS/SCADA safety, and human stop authority | synthetic IoT/OT trust-boundary exercise | P3–P4 |
| 19 | Cloud Computing | explain shared responsibility, IAM, storage, network, container, Kubernetes, serverless, and logging controls | synthetic IAM/storage-policy review | adjacent practical scope |
| 20 | Cryptography | explain hashes, encryption, PKI, certificates, key stretching, attacks, and common misuse | local integrity/encryption/certificate exercise | cross-cutting evidence protection |

## UUU Skill Coverage

| Skill | Primary evidence route |
| --- | --- |
| Information security and ethical hacking | M01 |
| AI-assisted ethical hacking | governed AI-use note across M01–M20 and the ethical-hacking lifecycle |
| Network intelligence gathering | M02–M04 |
| Vulnerability scanning | M03 and M05 |
| System, network, web, mobile, wireless, IoT, and cloud assessment | M06 and M11–M19 |
| Malware and AI-related malware concepts | M07 |
| Social-engineering awareness assessment | M09 |
| DoS/DDoS recognition and defense | M10 |
| Cryptographic data protection | M20 |

## Weekly Historical-Incident Project Map

| Project | Modules / period | Executable outcome |
| --- | --- | --- |
| WP-2026-W36 | M01 / W36 | authorization gate with one permitted action, two pre-execution refusals, and evidence integrity |
| WP-2026-W37 | M02–M04 / W37 | incident-grounded discovery of an omitted local service with an ownership-aware asset map |
| WP-2026-W38 | M05–M08 / W38 | bounded vulnerability, malware, and packet-evidence triage |
| WP-2026-W39 | M09–M12 / W39 | consent, availability, session, and layered-detection review |
| WP-2026-W40 | M13–M16 / W40 | local web-security regression with server, application, injection, and wireless evidence |
| WP-2026-W41 | M17–M20 / W41 | mobile, IoT/OT, cloud, and cryptographic control review |
| WP-2026-W42–W53 | course through year-end | one distinct incident-grounded project per week for course conversion, CEHP, agent security, reproducibility, continuity, and handoff |

The complete incident and acceptance map lives at
[`../projects/weekly-incident-projects/README.md`](../projects/weekly-incident-projects/README.md).

## CEHP Review Scope

| Order | Module | CEH evidence reused | Posttest file |
| --- | --- | --- | --- |
| P1 | Network and vulnerability scanning | M03 and M05 | `../assessments/posttests/p1-network-vulnerability-scanning.md` |
| P2 | Network service banner grabbing and enumeration | M03, M04, and M13 | `../assessments/posttests/p2-banner-grabbing-enumeration.md` |
| P3 | Network traffic analysis | M08, M11, M16, and M18 | `../assessments/posttests/p3-traffic-analysis.md` |
| P4 | System attack analysis | M06, M07, M10, and M12 | `../assessments/posttests/p4-system-attack-analysis.md` |
| P5 | Website attack analysis | M13–M15 | `../assessments/posttests/p5-website-attack-analysis.md` |

Dedicated CEHP preparation begins after the CEH course. The shared CEH
evidence is tagged for reuse instead of repeating the same pre-class work.

## Minimum Preview Loop

For each module:

1. Declare the mapped weekly project, scope, and executable acceptance check.
2. Attempt the smallest authorized action and capture the output or exact
   blocker.
3. Research that blocker, safety question, or current validation question.
4. Apply the answer, rerun, and preserve evidence under the weekly project.
5. Select concept, evidence, defense and scope decisions using the versioned
   ten-item choice posttest; practical evidence remains separate and unaided
   verbal recall is not assessed.

Full pre-class readiness requires all twenty modules at `pass`, all nine UUU
skills mapped to evidence, Form B `>=75%`, and zero critical-safety errors.
An open gate produces a class-entry gap brief. Use `coverage complete; readiness incomplete` only when every module was attempted; otherwise use `coverage incomplete; readiness incomplete`.

## Delivery Boundary

UUU publishes the course-wide sequence but not the Taipei `2048` instructor's
module-by-day allocation for `2026-10-12` through `2026-10-16`. Preserve actual
daily coverage from the instructor handout or observed class delivery.
