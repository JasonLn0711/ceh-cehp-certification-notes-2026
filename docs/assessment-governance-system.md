# CEH / CEHP Assessment Governance System

## Purpose

This repo uses a small Assessment Governance System for CEH / CEHP preparation.
The system turns each assessment result into a traceable learning decision:

`official scope -> weekly incident project -> execution evidence -> competency claim -> assessment -> remediation -> rerun/retest`

This makes pretests and posttests useful as learning controls, not only as
question practice.

## Adopted Source

The v0.2 design adopts the expert review preserved at:

`../source/2026-07-01-assessment-governance-expert-review/source.md`

## September 11 version and claim boundary

Jason approved four hours weekly, the full mastery target and choice-based
checks. [Current module contract](../assessments/posttests/module-posttest-template.md)
replaces the eight-item delivery prospectively. Formal feedback follows scoring;
tutoring feedback remains immediate. Practical performance remains independently
required. Learner-selected evidence/risk/defense/scope decisions replace prose
requirements in active preparation acceptance. Unaided verbal recall remains
`not assessed`; earlier short-answer scores retain their original meaning.
Existing provisional quizzes are not upgraded or merged into governed passes.

Form B v0.3.0 retains 50 points and 60 minutes: 25 foundational, 10 scenario,
10 evidence-interpretation and 5 safety-choice items. Require 38/50 and every
other readiness gate. Balance answer positions 13/13/12/12; vary sequence and
keep plausible distractors. Administer without hints or feedback until scored.
Then apply the correction/retest rule, retaining original error counts. A score
below 38/50 requires a fresh parallel 50-item Form B version for any eventual
passing aggregate; targeted retests never increase the original score. If the
weekly ceiling cannot accommodate it, preserve the open gate and gap brief.
Freeze question IDs, module/skill
mapping, critical tags, separate key and hashes by October 4. Replacement items
receive a new version; no exposed baseline wording is reused. This personal
pilot threshold is not an EC-Council official passing score.

## Governance Layers

| Layer | Operating role | Repo artifact |
| --- | --- | --- |
| Weekly incident project | Defines the real weekly outcome, historical anchor, mock instance, scope, acceptance check, execution state, and evidence locator. | `../projects/weekly-incident-projects/README.md` |
| Competency map | Defines CEH vocabulary readiness and CEHP practical readiness claims. | `../assessment-governance/competency_map.csv` |
| Item bank | Stores item metadata, official-scope mapping, scoring, remediation, and review status. | `../assessment-governance/item_bank.csv` |
| Assessment forms | Defines baseline form A, parallel form B, mini-posttests, and CEHP readiness forms. | `../assessment-governance/assessment_forms.csv` |
| Rubric | Defines scoring for MCQ, short answer, scenario, practical readiness, and critical safety items. | `../assessment-governance/rubric.md` |
| Attempt log | Records form version, score, confidence, decision, remediation, and retest result. | `../assessment-governance/attempt_log.csv` |
| Traceability matrix | Connects official scope, claim, evidence, item, rubric, attempt, decision, remediation, and retest. | `../assessment-governance/traceability_matrix.csv` |
| Dashboard | Tracks weak modules, safety errors, completion, scoring latency, remediation closure, and readiness gates. | `../assessment-governance/readiness_dashboard.md` |

## Readiness Gates

| Time | Assessment | Decision standard | Follow-up |
| --- | --- | --- | --- |
| `2026-07-01` to `2026-07-03` | Baseline form A | Creates weak-module map. | Route lowest five modules into preview repair. |
| After each mapped weekly project | execution acceptance plus v0.2.0 ten-item choice diagnostics | Declared project check passes, `>=8/10`, all applicable safety items clear and remediation complete. | Preserve the blocker, repair the implementation or understanding, then rerun and retest. |
| By `2026-10-11` | `preclass_form_b` v0.3.0 pilot | WP-2026-W37–W41 accepted, M01 acceptance evidenced in W36 or W37, `>=75%`, zero critical-safety errors, all twenty module posttests attempted and passed, and evidence routes for all nine UUU skills. | Use `preclass_ready` only when every criterion clears; otherwise issue a gap brief; use `coverage complete` only when all modules were attempted. |
| `2026-10-12` to `2026-10-16` | Daily class check | 3 evidence points, 3 weak points, 1 remediation action per day. | 20-minute repair before next class day. |
| `2026-10-17` to `2026-11-18` | CEHP practical bridge | At least 4 of 5 practical scenario classes at `pass`. | Lab notebook repair for remaining scenario classes. |
| `2026-11-18` | CEHP readiness gate | Complete one lab finding note with evidence, risk, authorization boundary, and next step. | Use CEHP class for targeted absorption and practical refinement. |

## Analytics Scope

This single-learner system uses deterministic analytics first:

- module score
- level score
- critical safety item result
- confidence calibration
- weak-module burn-down
- remediation closure rate
- retest improvement
- scoring latency
- accepted weekly incident projects
- blocker-to-rerun closure

Large-sample psychometrics such as IRT, DIF, and full distractor analysis become
future options after enough independent attempts exist.

## Pre-Class Form B Contract

Prepare and lock `preclass_form_b` by `2026-10-04`; administer it closed-book
on `2026-10-10`; issue the gap brief on `2026-10-11`.

- `50` items in `60` minutes;
- `25` foundational multiple-choice items, `10` scenario multiple-choice
  items, `10` evidence-interpretation multiple-choice items, and `5` multiple-choice safety judgments;
- coverage across all 20 CEH modules and all nine UUU skill outcomes, with additional weight on authorization,
  network fundamentals, web security, cloud shared responsibility, and
  cryptography;
- balanced answer-key positions and plausible distractors;
- a separate answer key and no verbatim reuse from the exposed baseline;
- pilot status until learner evidence and review support a stronger claim.

A missed gate keeps the October course active and creates a concise class-entry
brief: unresolved terms, practical evidence still awaiting the licensed lab,
critical-safety concepts, and questions to listen for during instruction.

## External Standards Used As Design Anchors

- UUU / UCOM CEH13 official course scope.
- UUU / UCOM CEHP Practical review course scope.
- EC-Council CEH knowledge and Practical exam framing.
- AERA / APA / NCME testing standards for validity, reliability, fairness,
  administration, and scoring control.
- Evidence-Centered Design for claim/evidence/task alignment.
- NIST NICE Framework for cybersecurity competency vocabulary.
- ADDIE for iterative training design.
- CDC Program Evaluation Framework for system use and improvement.
- 1EdTech Caliper Analytics as a reference model for learning activity data.
- Validated multiple-choice item-writing guidance for item quality.

## Next Build Steps

1. Complete WP-2026-W36 or preserve its state and close the M01 safety
   competency inside WP-2026-W37: Rules of Engagement correction,
   authorized localhost action, two policy refusals, and integrity evidence.
2. Complete the overdue M01 repair and fresh delayed choice transfer check at least 48 hours after correction; preserve the original September 7 due date.
3. Use the 16-hour W38–W41 ceiling for incident projects, focused research,
   reruns, choice-based decisions and mapped diagnostics under
   `study-plan/pre-course-prep.md`.
4. Prepare and lock `preclass_form_b` by `2026-10-04`.
5. Take and score Form B on `2026-10-10` or `2026-10-11`, then produce the
   class-entry brief.
6. Use the low-friction daily loop in `daily-closed-loop-plan.md`; collect
   confidence on every new scored item.

## Preserved Form B v0.2.0 definition

Superseded prospectively September 11, before administration. The prior form
specified 50 items in 60 minutes: 25 foundational MCQs, 10 scenario MCQs,
10 short answers and five safety judgments; at least 75% plus all module,
project, nine-skill and critical-safety gates. It had no recorded learner
attempt. v0.3.0 changes the response format and recall claim; old attempts are
never reclassified under the new rubric. The exposed baseline stays unchanged.

## Acceptance order

Review conceptual results, safety/remediation and practical artifact checks
independently. Then finalize module passes and weekly acceptance together when
all components clear. A weekly accepted label is not a prerequisite for
reviewing its component artifacts. [The module contract](../assessments/posttests/module-posttest-template.md)
defines partial attempts, failed-score replacement forms and delayed safety checks.
