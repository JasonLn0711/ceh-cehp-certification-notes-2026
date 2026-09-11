# WP-2026-W36 Instructor Key

September 11 prospective amendment: assess the explanation component through
learner-selected evidence/scope decisions under choice v0.2.0, linked from the
project README. Unaided verbal recall is not assessed. Preserve independent
practical, pre-execution refusal and delayed safety checks; old learner sources
and scores retain their original meaning.

## Expected Decisions

| Proposed action | Expected result | Reason |
| --- | --- | --- |
| `GET 127.0.0.1:8765/public.txt` | `ALLOW`, once | host, port, path, method, count, time, operator, and stop state match the ROE |
| `GET 127.0.0.1:8766/public.txt` | `STOP — authorization required` | port is outside the allowlist |
| `GET 127.0.0.1:8765/private.txt` | `STOP — authorization required` | path is outside the allowlist |

## Acceptance Rubric

| Area | Pass evidence |
| --- | --- |
| Authorization | named authorizer and operator, purpose, target, method, window, stop/resume, reporting, and evidence handling precede execution |
| Execution | one successful permitted request; no evidence of either excluded request |
| Evidence | client transcript and server log agree; SHA-256 verification passes |
| Explanation | learner distinguishes capability/reachability from authority and explains fail-closed ambiguity handling |
| Assessment | delayed M01 retest completed with no critical-safety error |

## Common Errors

- writing the ROE after the request;
- treating all localhost ports or paths as authorized;
- using a broader method or request count than the ROE permits;
- recording a refusal while still sending the excluded request;
- claiming that a hash proves authorship, confidentiality, or trusted time;
- treating author-generated smoke evidence as learner completion.

## Evidence Limitation

The `8765` server log cannot prove that no connection reached another port.
The decision record, controlled procedure, and client transcript are sufficient
for this learning objective. A forensic investigation would require broader
host or network audit evidence.

