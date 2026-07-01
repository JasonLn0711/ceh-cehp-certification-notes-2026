# Official Scope Map

## Source Boundary

This map is based on the official UCOM / UUU CEH13 and CEHP course pages checked
on `2026-07-01`. Use it as the study backbone before adding extra material.

## CEH13 Course Scope

| Order | Module | Preview output | Posttest file |
| --- | --- | --- | --- |
| 1 | Ethical hacking introduction | explain legal scope, attacker/defender vocabulary, engagement boundaries | `assessments/posttests/01-ethical-hacking-introduction.md` |
| 2 | Footprinting and reconnaissance | distinguish passive vs active discovery and defensive exposure reduction | `assessments/posttests/02-footprinting-reconnaissance.md` |
| 3 | Scanning networks | explain host, port, service, and vulnerability discovery at a high level | `assessments/posttests/03-scanning-networks.md` |
| 4 | Enumeration | identify why exposed services, users, and shares matter | `assessments/posttests/04-enumeration.md` |
| 5 | Vulnerability analysis | map findings to severity, exploitability, and remediation priority | `assessments/posttests/05-vulnerability-analysis.md` |
| 6 | System hacking | explain credential, privilege, persistence, and cleanup concepts defensively | `assessments/posttests/06-system-hacking.md` |
| 7 | Malware threats | distinguish malware types, delivery routes, and controls | `assessments/posttests/07-malware-threats.md` |
| 8 | Sniffers | explain packet capture risks and network protection controls | `assessments/posttests/08-sniffers.md` |
| 9 | Social engineering | identify human-risk patterns and verification controls | `assessments/posttests/09-social-engineering.md` |
| 10 | Denial of service | explain availability threats and resilience controls | `assessments/posttests/10-denial-of-service.md` |
| 11 | Session hijacking | explain session/token risk and defensive controls | `assessments/posttests/11-session-hijacking.md` |
| 12 | Evading IDS, firewalls, and honeypots | explain why detection can fail and how defense layers compensate | `assessments/posttests/12-evasion.md` |
| 13 | Hacking webservers | identify server exposure, patching, config, and logging risks | `assessments/posttests/13-webservers.md` |
| 14 | Hacking web applications | explain common app-layer weaknesses and secure-development controls | `assessments/posttests/14-web-applications.md` |
| 15 | SQL injection | explain injection risk, parameterization, and validation | `assessments/posttests/15-sql-injection.md` |
| 16 | Wireless networks | explain wireless authentication, encryption, and rogue-access risks | `assessments/posttests/16-wireless.md` |
| 17 | Mobile platforms | identify mobile app, device, and data-protection risks | `assessments/posttests/17-mobile.md` |
| 18 | IoT and OT | explain device, firmware, segmentation, and safety boundaries | `assessments/posttests/18-iot-ot.md` |
| 19 | Cloud computing | explain shared responsibility, identity, storage, and logging controls | `assessments/posttests/19-cloud.md` |
| 20 | Cryptography | explain hashes, symmetric/asymmetric crypto, certificates, and common misuse | `assessments/posttests/20-cryptography.md` |

## CEHP Review Scope

| Order | Module | Preview output | Posttest file |
| --- | --- | --- | --- |
| P1 | Network and vulnerability scanning | translate scan results into risk and next defensive action | `assessments/posttests/p1-network-vulnerability-scanning.md` |
| P2 | Network service banner grabbing and enumeration | explain service identity, exposure, and hardening paths | `assessments/posttests/p2-banner-grabbing-enumeration.md` |
| P3 | Network traffic analysis | explain what traffic evidence can and cannot prove | `assessments/posttests/p3-traffic-analysis.md` |
| P4 | System attack analysis | interpret compromise symptoms and defensive containment steps | `assessments/posttests/p4-system-attack-analysis.md` |
| P5 | Website attack analysis | interpret web-attack evidence and remediation priority | `assessments/posttests/p5-website-attack-analysis.md` |

## Minimum Preview Loop

For each module:

1. Read one short official or reputable overview.
2. Write a `10` line summary in `notes/`.
3. Answer the module posttest.
4. Mark outcome: `pass`, `review`, or `activation_needed`.
5. Add only failed topics to the weak-topic list.
