# M03-05 source and factual review

- Checked: 2026-11-03, Asia/Taipei.
- Reviewed artifact: `../notes/m03/M03-05-teaching.zh-TW.md`.
- Scope: factual review of the lesson against official technical documentation; no target scans, no public writes, no claim of visual/accessibility acceptance.
- Result: **No material factual errors identified.** This is a technical source review, not a certification of the deployed page or learner understanding.

## Primary route row and preservation

Public route repository: `JasonLn0711/ceh-cehp-certification-notes-2026`.
Route files: `study-plan/core-route-2026-10-27.json` and `study-plan/core-route-2026-10-27.md`.
Complete semantic source row:

| Field | Value |
|---|---|
| Route | CEH26-20261027 |
| Stable unit | CEH26-M03-C05 |
| Display/concept | CEH M03-05 / M03-05 |
| Module | M03, fourth module in the designated route |
| Source section / row | 三/M03 / 5 |
| Reading order | 26 |
| Title | Service Version & Banner Grabbing |
| Importance / difficulty | 5 / 3 |
| Original reason | 從服務回應推測軟體資訊，並認識偽裝、代理和版本誤判。 |
| Legacy IDs | None |
| Legacy relation / mode | new_scope / new_teaching |
| Original planned state | planned |
| Original planned slot | 2026-11-04 13:00 Asia/Taipei, 下午 |

The planned slot above is historical scheduling metadata, **not actual delivery evidence**. The lesson keeps service-response interpretation, disguise, proxy ambiguity and version misidentification together as one unit; it does not split them into additional counted units. It carries forward the M03 observation-versus-intrusion distinction and limits OS fingerprinting to a boundary explanation, leaving detailed OS work to the next unit. The release process also read the latest remote route and the designated primary manuscript row. Actual delivery evidence remains in private records, separate from planned schedule metadata.

## Official sources and supported claims

1. **Nmap, Service and Version Detection** (living documentation; checked 2026-11-03): <https://nmap.org/book/man-version-detection.html>
   Port-name lookup alone does not establish software identity. `-sV` uses service probes and response patterns; not every service supplies every detail. `-A` enables more functionality than version detection. Version probes can have effects on target devices; default exclusions must not be treated as a guarantee of harmlessness.
2. **Nmap, Technique Described** (living documentation; checked 2026-11-03): <https://nmap.org/book/vscan-technique.html>
   TCP NULL probing follows connection establishment and waits for service greetings before application payloads. Subsequent probes may refine identification; encrypted services require suitable connection handling. Calling this whole process passive collection would be wrong; the lesson correctly avoids that claim.
3. **Nmap, nmap-service-probes File Format** (living documentation; checked 2026-11-03): <https://nmap.org/book/vscan-fileformat.html>
   `match` interprets response patterns; `softmatch` restricts subsequent probes to the indicated service type while searching for more detail. It is not a published percentage of version certainty. Exclusion behavior includes printer services because probe content may be printed. The lesson avoids prescribing a fixed exclusion-port range, which differs in wording across official pages.
4. **Nmap, OS Detection** (living documentation; checked 2026-11-03): <https://nmap.org/book/man-os-detection.html>
   `-O` examines TCP/IP stack responses. Its mechanism differs from application-service identification. OS-match confidence must not be relabeled as service-version confidence.
5. **Nmap, Version Detection Introduction** (living documentation; checked 2026-11-03): <https://nmap.org/book/vscan.html>
   Version information can be misleading because of backports or spoofing. Application-platform hints and stack-derived OS findings may differ, including in forwarded-service deployments.
6. **RFC 9110, HTTP Semantics**, June 2022, §§3.7, 7.2, 10.2.4, 17.12: <https://www.rfc-editor.org/rfc/rfc9110.html>
   Reverse proxies can represent origins while forwarding requests. Host/authority identifies the requested namespace. The Server response field is optional, and needlessly detailed product disclosure is discouraged. These rules support the lesson's cautious treatment of external headers.
7. **Red Hat, Backporting Security Fixes** (living vendor documentation; checked 2026-11-03): <https://access.redhat.com/security/updates/backporting>
   Security fixes can be applied to maintained older versions. Upstream version-only checks can therefore misclassify patched vendor packages. The lesson correctly requests full package and vendor-fix evidence rather than assuming vulnerability from a banner.
8. **RFC 6066, TLS Extension Definitions**, January 2011, §3: <https://www.rfc-editor.org/rfc/rfc6066.html#section-3>
   Server Name Indication supplies a hostname during TLS negotiation for virtual servers. This is supplementary support for preserving hostname context; the delivered lesson does not introduce SNI as an additional required concept.

## Fact, inference, and teaching illustration boundaries

- **Observed text:** a service sends a string; the original string and request context should be preserved. This is distinct from verifying the installed package or running process.
- **Tool inference:** product/version identification is the tool's interpretation of response patterns, not proof of exact patch state or exploitability.
- **Architecture inference:** a reverse proxy can make the externally observed endpoint differ from the backend. The lesson says “may,” not that every Server field necessarily describes a proxy.
- **Operational recommendations:** internal package/advisory/configuration comparison, running-process checks after updates, logging, access limitation, and evidence retention are defensive recommendations, not claims that any real device was checked.
- **Synthetic material:** ExampleSSH, ExampleWeb, example-app, and the example hostnames/output are explicitly teaching-only. No real vulnerability identifier or live-target result is attached to them.
- **Safety:** the command contains a non-executable explanatory placeholder, is scoped to an expressly authorized isolated lab, and is not executed. The actual exercise is offline interpretation.
- **Uncertainty:** absent banners, partial matches, proxy ambiguity and unknown patch status remain unresolved until additional evidence is obtained. Nothing in the lesson equates identification with login, exploitation or successful intrusion.

## Review disposition

No factual correction is required before preparing the public lesson. Preserve the distinctions above during English translation and model conversion. Publication, route progression, bilingual parity, visual layout, keyboard/focus operation and production provenance are not established by this source review and require their own recorded checks.
