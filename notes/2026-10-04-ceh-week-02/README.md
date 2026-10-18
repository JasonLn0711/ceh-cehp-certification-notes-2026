# CEH Week 2 — M04–M06 reading and evidence map

This public-safe index connects the October 4 course topics to the existing learning route. Full instructor transcripts, licensed teaching materials, screenshots, credentials and training-target details remain outside this public repository.

## Topic map

| Module | Core question | Evidence to preserve |
| --- | --- | --- |
| M04 Enumeration | What information can a service expose, and what access is authorized? | Service/version/context, observed response, interpretation and scope |
| M05 Vulnerability Analysis | Which finding is valid and what should be fixed first? | Finding evidence, CVE/CWE/CVSS version, affected asset, remediation and retest |
| M06 System Hacking | How do authentication, privileges, storage and logs affect security? | Mechanism, prerequisites, defensive controls and bounded lab result |

## Review corrections

- Kerberos uses AS, TGS and service exchanges; a Windows access token is not an extra ticket exchanged for a TGT. See [RFC4120](https://www.rfc-editor.org/rfc/rfc4120).
- A challenge-response capture is not automatically a plaintext password or the stored NT hash. Keep the captured mechanism separate from any later verification.
- CVSS measures severity; prioritization also uses exposure, exploitation evidence and business impact. Preserve the score's version and source.
- IPsec protection depends on policy, authentication and mode; it does not repair application vulnerabilities.
- NTFS named streams support legitimate metadata as well as possible abuse. Their existence alone does not prove malware. See [Microsoft file streams](https://learn.microsoft.com/en-us/windows/win32/fileio/file-streams).
- Failed or missing logs, disabled protection and a SUID bit are evidence to investigate, not stand-alone proof of intrusion.
- Steganography hides a message's presence; encryption protects its content. Prepared demonstrations do not establish independent learner completion.

## Actual evidence status

Course attendance and source-note preparation were reported complete. A powered-on target resolved one enumeration attempt; an isolated challenge-response exercise supplied observed capture and offline-check stages. Those observations do not establish every practical family's acceptance, unauthorized access, exam readiness or new learning minutes.

The final image-steganography exercise was assigned; independent completion remains unconfirmed. Next learner step: perform only the already-authorized isolated exercise, preserve original/carrier/output/extracted-file identities and compare the harmless payload before marking acceptance. Use synthetic data, not real financial or personal content.

## Connections

- [M06 complete Northstar film and QA](../m06-system-hacking/video-production-2026-10-18.md): connects authentication, privilege, persistence and missing logs to the same evidence/alternative-explanation boundaries; source and film QA do not add learner results.

- [M05 Northstar film and QA](../m05-vulnerability-analysis/video-production-2026-10-18.md): connects enumeration evidence to finding validation, risk priority and repair/retest; current v1.1 uses eight 1-second quiz holds. Film production and learner evidence remain separate.
- [Current learning route](../../study-plan/uuu-aligned-ceh-cehp-2026-09-18.md)
- [Practice-bank entry](../../assessments/practice-bank/README.md)
- [Learner coverage](../../assessment-governance/course-coverage-2026-09-18.md)
- [Week 1 prerequisite notes](../2026-09-20-ceh-week-01/README.md)
- [Repository index](../../README.md)

Shared self-study ceiling remains 240 minutes per week and at most 25 minutes on course days. This index creates no new quota, accepted result or publication of private course evidence.

