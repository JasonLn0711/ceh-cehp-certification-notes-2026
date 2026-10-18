# M06 technical source and case review

Reviewed on 2026-10-18, Asia/Taipei. This review checks the authored teaching mechanisms and fictional evidence. It does not certify actual narration, subtitles, visuals or a rendered MP4.

## Primary-source checks

| Scenes / topic | Supported teaching distinction | Primary source checked live |
|---|---|---|
| S06–S14 identity/passwords/MFA | Authentication verifies control of authenticators; account acceptance does not establish all later actions. Online rate limiting differs from offline guesses against copied verifier data. Salting and suitable password hashing make offline guessing more costly; salt is not a secret encryption key. | [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html), [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) |
| S13 operating-system stores | Credential handling depends on provider/platform. Windows protected stores and Linux restricted shadow-file concepts are teaching-level descriptions, not universal present-day deployment details. No credential file is collected. | [Microsoft Passwords technical overview](https://learn.microsoft.com/en-us/windows-server/security/kerberos/passwords-technical-overview) |
| S17–S18 memory safety and mitigations | Overflow can corrupt or crash a program; exploitability is conditional. ASLR, DEP/NX and checks address different aspects and do not repair all bugs. No exploit bytes or active payloads are used. | [Microsoft Exploit protection reference](https://learn.microsoft.com/en-us/defender-endpoint/exploit-protection-reference) |
| S20–S25 permissions | Tokens carry process/thread security context, identity/group/privilege information. UAC manages elevation; a prompt is not the same as successful authentication or a universal security guarantee. | [Microsoft Access tokens](https://learn.microsoft.com/en-us/windows/win32/secauthz/access-tokens), [How UAC works](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/how-it-works) |
| S32–S36 continued access | Persistence concerns continued access across interruptions; normal startup features may be used legitimately. Unexpected startup entries require context rather than automatic malicious attribution. | [MITRE Persistence TA0003](https://attack.mitre.org/tactics/TA0003/) |
| S40–S48 logs and incident claims | Altered/cleared logs are a defender taxonomy topic; a gap alone has several possible causes. Original source sets retention/configuration/service health alongside malicious explanations. | [MITRE Clear Windows Event Logs](https://attack.mitre.org/techniques/T1070/001/) (direct page retrieved without extractable body; narrow taxonomy is retained as source-reported) |
| Whole M06 curriculum | The public course page supports topical alignment for System Hacking. This independently authored film does not claim exhaustive proprietary courseware coverage or exam equivalence. | [EC-Council CEH](https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/) |

The Microsoft password page includes historical compatibility details and some older policy advice. This film does not import those details as current general password-policy recommendations. The first attempted UAC URL failed; the correct current Microsoft application-security route above was read successfully. No external reference was used to invent a real CVE, victim or incident for Northstar.

## Fictional evidence cross-check

NORTHSTAR_EVIDENCE.json records E03 portal authentication 10:04, E04 lesson-plan read allowed 10:15, E05 payroll request denied 10:17, E06 lab service entry 10:26, E07 local log-health gap 10:33 and E08 partial central records 10:34, all UTC+08. The portal and lab events are on different systems; shared actor/session/causation is unproven. Payroll denial is not data theft. Service registration without a matching ticket is not confirmed hostile persistence. A local coverage gap is not proved intentional log deletion.

Two minimal chronology corrections are applied only in working production copy: S46 ten→twenty-two minutes and S47 afternoon→morning. Their source receipts are in source-corrections.json; original ZIP and all 271 manifest hashes remain unchanged. Narration remains 8,969 words. No other paragraph is summarized or replaced.

## Boundaries retained

All school records and identities are supplied fictional fixtures, labeled SIMULATED OUTPUT onscreen. No real host was scanned, no password guessed, no credential/token collected, no exploit/rootkit/keylogger/persistence installed, and no real log altered. Mechanism illustrations and read-only fixture interpretation do not establish a learner-executed security task or official readiness.

The source validator reports 1,065 checks in the final extracted pack, one more than the release report's 1,064 pre-release checks: the optional PACK_MANIFEST consistency assertion is present after packaging. These remain source-layer checks, separate from media validation.
