# Pre-Course Prep Plan

## Objective

Reach the target CEH13 class on `2026-10-12` with enough vocabulary and baseline
structure to learn from the instructor instead of hearing every concept for the
first time.

## Rules

- Keep each preview module to `25-40` minutes.
- End every preview with a posttest.
- Repair confirmed weak topics first and verify every module before the CEH
  class. Module posttests decide where additional repair time goes.
- Keep the note system compact before class and expand only from official
  course needs.

## Phase 0: Baseline

- [x] Take `assessments/00-baseline-pretest.md`.
- [x] Score with `assessments/00-baseline-pretest-answer-key.md`.
- [x] Pick the first `5` provisional weak modules and verify them through
  module posttests.
- [ ] Use `source/2026-07-01-ucom-registration/analysis-and-study-bridge.md`
  as the registration gate and exam-rights reference.
- [ ] Share `docs/expert-assessment-packet.md` / Downloads packet with the
  expert for question-bank and readiness-gate review.
- [ ] Use `docs/assessment-governance-system.md` and
  `assessment-governance/` as the v0.2 Assessment Governance System before
  drafting formal form A and parallel form B.
- [ ] Follow `docs/daily-closed-loop-plan.md`: one primary task, one visible
  output, and one record update per day.
- [ ] Use `docs/daily-closed-loop-calendar-plan.md` as the detailed daily
  execution calendar through `2026-08-02`.
- [ ] Use `docs/day-01-03-learning-package-rule.md` as the package rule for
  Day 1-3 and later compact module packets.

## Phase 1: CEH Zero-To-Ready Preview

- [ ] Preview modules 1-4: ethics, reconnaissance, scanning, enumeration.
- [ ] Preview modules 5-8: vulnerability, system hacking, malware, sniffing.
- [ ] Preview modules 9-12: social engineering, DoS, sessions, evasion.
- [ ] Preview modules 13-16: webservers, web apps, SQL injection, wireless.
- [ ] Preview modules 17-20: mobile, IoT / OT, cloud, cryptography.

### 2026-09-07 to 2026-10-11 Cadence

Protect `4 h` each week. Every module preview ends with the eight-item pilot
posttest; every active cybersecurity week also receives a fresh topic-driven
source scan and brief.

| Week | Module group | Focus |
| --- | --- | --- |
| `2026-W37` | M01–M04 | close M01 critical-safety gate; verify reconnaissance, scanning, and enumeration |
| `2026-W38` | M05–M08 | prioritize M07 malware persistence and M08 packet-sniffing defenses |
| `2026-W39` | M09–M12 | verify social engineering, availability, session, and detection concepts |
| `2026-W40` | M13–M16 | prioritize M14 web applications and M16 wireless security; prepare Form B |
| `2026-W41` | M17–M20 | prioritize M20 cryptography; take and score the pre-class Form B |

The Form B gate on `2026-10-10` or `2026-10-11` targets `>=75%`, zero
critical-safety errors, and at least `16` of `20` modules at `review` or
`pass`. A lower result produces a class-entry weak-topic brief for targeted
listening during the October course.

## Phase 2: CEHP Practical Readiness Preview

- [ ] Preview P1: network and vulnerability scanning.
- [ ] Preview P2: service banner grabbing and enumeration.
- [ ] Preview P3: traffic analysis.
- [ ] Preview P4: system attack analysis.
- [ ] Preview P5: website attack analysis.

## Administrative Gates

| Gate | Target date | Owner | Activation | Next action |
| --- | --- | --- | --- | --- |
| UCOM / UUU class-change confirmation | confirmed `2026-07-13 16:08` | Jason | CEH 台北 `2048` and CEHP 台北 `26416` are active classes | use the verified transfer source; treat `2046` and `26408` as superseded history |
| VOISS AI written offer and employer schedule discussion | when written offer arrives | Jason | opens a second class-compatibility review | confirm start date, work hours, and leave arrangement with the employer; adjust classes again only when the agreed work schedule calls for it |
| UCOM / UUU payment and class reminder | around `2026-07-20` | Jason | waiting for provider notice | confirm payment/card flow and class-opening notice |
| CEH voucher and lab activation | after `2026-10-16` | Jason | opens after CEH class | record voucher, lab start date, retake rules, and booking flow |
| CEH exam date | after CEH weak-topic review | Jason | opens after pass/review evidence | book after high-risk modules have pass/review evidence |
| CEHP exam logistics | before `2026-11-20` | Jason | opens before Practical booking | confirm Practical booking, proctoring, and environment checks |

## Weak Topic List

| Topic | Source | Status | Next action |
| --- | --- | --- | --- |
| M01 authorization and scope | [`ATT-20260903-01`](../assessments/attempts/2026-09-03-baseline-diagnostic.md) | `activation_needed`; critical-safety gate open | complete the ROE correction and localhost exercise; retest `2026-09-07` |
| M07 malware persistence | `ATT-20260903-01` | provisional | verify in `2026-W38` module posttest |
| M08 packet-sniffing defenses | `ATT-20260903-01` | provisional | verify in `2026-W38` module posttest |
| M16 wireless security | `ATT-20260903-01` | provisional | verify in `2026-W40` module posttest |
| M20 cryptography | `ATT-20260903-01` | provisional | verify in `2026-W41` module posttest |
| M14 web applications / P2 banner grabbing | `ATT-20260903-01` | tied candidate | verify in the matching CEH and CEHP checks |
