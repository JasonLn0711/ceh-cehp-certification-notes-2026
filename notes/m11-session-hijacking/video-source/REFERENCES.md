# Content provenance and reading map

Reviewed online 2026-10-20 (Asia/Taipei). Original teaching prose and all Northstar scenarios are authored for this module; the fictional school examples are not reports of actual attacks. The local model is intentionally narrower than a production web application.

| Source | Use and boundary |
| --- | --- |
| [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) | Cross-check identifier lifecycle, rotation, expiry and browser attributes. No verbatim excerpts. The lesson's synthetic cases and acceptance reasoning are original. |
| [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) | Distinguish automatic credential inclusion, request authenticity and authorization; XSS can undermine request protections. |
| [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293.html) | TCP sequence/acknowledgment/window terminology. The offline interval check is a toy illustration, not a full TCP validator. |
| [RFC 8725](https://www.rfc-editor.org/rfc/rfc8725.html) | Token validation requires cryptographic policy and appropriate recipient/claim checks; decoding alone is insufficient. |
| [Existing M11 practice scope](../../../assessments/practice-bank/m11.md) | Repository curriculum coverage; film questions are newly authored, not official/recalled exam items. |

## Evidence separation

`lesson.txt` owns 40 narrated teaching/synthesis scenes. `authoring-questions.json` owns eight original film questions and explanations. `build_source.py` creates canonical scene, quiz and diagram manifests. The delivery source package also exposes the canonical quiz envelope as `questions.json`, separately from the authoring input. `offline_checks.py` executes a local symbolic model with explicit assertions and no networking. Real application testing, learner performance and official readiness require their own evidence.

The diagram ports represent declared relationships; comparison layouts omit causal arrows. Original props retain approved source hashes. The clock and ticket illustrations are conceptual, not measurements of a real incident. All Northstar evidence scenes carry SIMULATED OUTPUT.
