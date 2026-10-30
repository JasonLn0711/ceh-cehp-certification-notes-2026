# M02-01 — Passive vs. Active Reconnaissance

Stable unit: M02-01 / CEH26-M02-C01. Route position: 14 of 161 teaching-design units; this is not an official exam-mandated unit count.

- Full bilingual public teaching and four reference answers: `notes/m02/M02-01-teaching.zh-TW.md`, `notes/m02/M02-01-teaching.en.md`, and paired answer files.
- Website preparation follows the existing `JasonLn0711/kairos-learning` pipeline, one concept page per module. Four paired SVGs explain request paths, DNS caching, evidence and authorization.
- Prior unit: M09-06. Next unit: M02-02 (OSINT Sources & Source Validation). This document records teaching material, not individual mastery or a calendar-derived completion claim.
- [Draft website PR #54](https://github.com/JasonLn0711/kairos-learning/pull/54), exact head `4db3927f57c0e7f1d06425441cd4557c2ec2d0ea`, is prepared. Its tree `b20f3343b5e3940577a9c1c8e035262d62786304` matches the locally tested tree. 51 tests, Svelte zero errors/warnings, publication-boundary and full static release checks passed. Production readback and browser/mobile interaction checks remain unverified. Publication is pending; a prepared lesson or source commit does not establish live deployment. PR, exact-head checks and deployed evidence must be recorded separately after verification.
- Technical primary sources: MITRE ATT&CK TA0043/T1595/T1593; IETF RFC 1034; NIST SP 800-115 (2008).

## Exact-head CI verification

[Course quality and preview run 41007168555](https://github.com/JasonLn0711/kairos-learning/actions/runs/41007168555) completed successfully for head `4db3927f57c0e7f1d06425441cd4557c2ec2d0ea`. PR #54 remains draft, open and unmerged. CI success is not a production deployment or browser readback claim.

## 2026-10-30 — Approved publication and deployment evidence

PR #54 was marked ready and merged after verifying the approved head and successful exact-head CI. Merge commit: `f6082d462853402ccc91c36e1e902ecacefda507`; merge tree `b20f3343b5e3940577a9c1c8e035262d62786304` exactly matches the tested PR tree.

[Publish learning notes / Pages run 41008823477](https://github.com/JasonLn0711/kairos-learning/actions/runs/41008823477) completed successfully for that exact merge commit. The deploy-pages step succeeded at 05:31:26 UTC (13:31:26 Asia/Taipei); the job completed at 05:31:28 UTC, and the workflow was updated to completed/success at 05:31:29 UTC.

- [Traditional Chinese lesson](https://learn.cs-kairos.com/courses/ceh/v13/m02/concepts/m02-01/) · [English lesson](https://learn.cs-kairos.com/en/courses/ceh/v13/m02/concepts/m02-01/)
- Four paired native SVGs and four closed-by-default reference answers. Normal text and tables remain expanded. New diagram text is capped at article body size and shrinks with narrower columns.
- 51 automated tests, zero Svelte errors/warnings, content/publication-boundary/static-release checks, preserved-download checksums and high-severity audit gate passed in the deployment workflow.
- **Production body and downloadable-asset readback, browser/mobile rendering and keyboard interaction remain unverified.** Prior restricted access was not retried or bypassed. Successful Pages deployment is distinct from those acceptance checks.

Earlier draft/pending statements above are retained as historical snapshots; this section is the latest publication status. Next route unit remains M02-02. Reference answers are public teaching, not personal learner responses.
