# Baseline Diagnostic Attempt — 2026-09-03

## Identity

- Attempt ID: `ATT-20260903-01`
- Form: `baseline_diagnostic_40`
- Form version: `0.1.0`
- Administration: closed-book requested; actual elapsed time and per-item
  confidence were not recorded
- Decision: `activation_needed`

## Source-Preserved Submission

The text below preserves Jason's complete submission without wording
corrections.

> Baseline Pretest (/home/jnclaw/every_on_git_jnclaw/phd-life-system/ceh-cehp-certification-notes-2026/assessments/00-baseline-pretest.md):
> - My answer (260903):
>     - multiple choice:
>         - 1c 2b 3a 4a 5a 6b 7? 8a 9a 10a 11a 12a 13a 14? 15a 16? 17a 18a 19a 20? 21? 22a 23a 24a 25a
>     - short answer:
>         1.  I have no idea about what the security test is. So, maybe I would like to guess a security test will be authorized by the project owner.
>         2.  Scanning is to find the attack surface. On the other hand, enumeration is to find further information of these found attack surfaces.
>         3.  I have no deep understanding. Maybe the vulnerability scan result may connect with other outputs.
>         4.  I have no idea about the answer to the following questions.

## Prior Working-Copy Receipt

- Before normalization, `assessments/00-baseline-pretest.md` contained the
  inline submission above and renumbered short answers.
- Working-copy SHA-256:
  `c069d2821d56e1b076cf237409e177fb6cc7a0e021d2851b370277045ef59779`.
- The local package
  `/home/jnclaw/Downloads/CEH-baseline-pretest-package-2026-09-03.zip`
  preserves the earlier packaging snapshot. Its SHA-256 is
  `b318ad322e073da12cdf87c7403ef7af08f7990bee1f6622baa1f4ce9c5fcdc3`.

## Scoring

### Multiple Choice

- Score: `18/25`
- Incorrect or unanswered:
  - Q1: submitted `C`; keyed answer `B`
  - Q7: submitted `?`; keyed answer `B`
  - Q8: submitted `A`; keyed answer `B`
  - Q14: submitted `?`; keyed answer `A`
  - Q16: submitted `?`; keyed answer `A`
  - Q20: submitted `?`; keyed answer `A`
  - Q21: submitted `?`; keyed answer `A`

### Short Answer

- Score: `2/15`
- Q26: `0.5` — identifies an owner direction; the repair adds written
  permission, target, methods, timeframe, reporting path, and stop conditions.
- Q27: `1` — distinguishes surface discovery from deeper information
  collection.
- Q28: `0.5` — points toward corroborating outputs; the repair adds context,
  exposure, compensating controls, false positives, business impact,
  exploitability, and remediation priority.
- Q29–Q40: `0`. Jason confirmed that these blanks represent knowledge gaps.

### Result

- Total: `20/40`
- Percent: `50.0%`
- Diagnostic band: begin with vocabulary and defensive concepts before tools.
- Critical-safety items not cleared: Q1 and Q26.

## Interpretation

The result supports a foundational repair path. CEH and CEHP readiness remains
a future evidence gate.

The recognition and recall evidence remain separate. The multiple-choice key
uses `A` for 20 of 25 items, so `18/25` provides limited evidence of broad
module knowledge. The `2/15` short-answer result provides the stronger signal:
unaided explanation is the current learning constraint.

## Learning Decision

- Confirmed first repair: M01 authorization, scope, reporting, and stop/resume
  conditions.
- Provisional next repairs: M07 malware persistence, M08 packet-sniffing
  defenses, M16 wireless security, and M20 cryptography.
- Additional tied candidates: M14 web applications and P2 banner grabbing.
- All 20 CEH modules receive a short verification pass before the October
  class; posttests determine where additional repair time goes.

## Remediation and Retest

- Remediation: complete the W36 M01 mock Rules of Engagement correction and
  authorized localhost exercise.
- Retest due: `2026-09-07`.
- Retest gate: explain authorization, scope, permitted methods, reporting,
  stop conditions, and resume conditions without copying the prior answer.
- Current retest result: pending learner evidence.

## Connections

- [Question form](../00-baseline-pretest.md) and [separate answer
  key](../00-baseline-pretest-answer-key.md)
- [Readiness dashboard](../../assessment-governance/readiness_dashboard.md)
- [Week 36 M01 research brief](../../research-briefs/2026-W36.md)
- [Pre-course repair cadence](../../study-plan/pre-course-prep.md)
- [Planning day note for 2026-09-03](../../../planning-everything-track/weeks/2026-W36/days/2026-09-03.md)
- [Planning week 37 activation plan](../../../planning-everything-track/weeks/2026-W37/weekly-plan.md)

## Evidence Boundary

This is one low-friction personal learning diagnostic. The form is a pilot
learning control; psychometric validation remains a future evidence layer. A
future pre-class Form B uses a separate question set and answer key.
