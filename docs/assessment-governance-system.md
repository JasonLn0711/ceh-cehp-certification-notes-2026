# CEH / CEHP Assessment Governance System

## Purpose

This repo uses a small Assessment Governance System for CEH / CEHP preparation.
The system turns each assessment result into a traceable learning decision:

`official scope -> competency claim -> evidence -> item -> rubric -> remediation -> retest`

This makes pretests and posttests useful as learning controls, not only as
question practice.

## Adopted Source

The v0.2 design adopts the expert review preserved at:

`../source/2026-07-01-assessment-governance-expert-review/source.md`

## Governance Layers

| Layer | Operating role | Repo artifact |
| --- | --- | --- |
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
| After each CEH module preview | 8-item mini-posttest | `>=75%` and critical safety items clear. | `50-74%` gets review; `<50%` gets `activation_needed`. |
| By `2026-10-11` | `preclass_form_b` pilot | `>=75%`, zero critical-safety errors, and at least 16 of 20 modules at `review` or `pass`. | Produce the class-entry weak-topic brief before CEH class. |
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

Large-sample psychometrics such as IRT, DIF, and full distractor analysis become
future options after enough independent attempts exist.

## Pre-Class Form B Contract

Prepare and lock `preclass_form_b` by `2026-10-04`; administer it closed-book
on `2026-10-10` or `2026-10-11`.

- `50` items in `60` minutes;
- `25` foundational multiple-choice items, `10` scenario multiple-choice
  items, `10` short answers, and `5` safety judgments;
- coverage across all 20 CEH modules, with additional weight on authorization,
  network fundamentals, web security, cloud shared responsibility, and
  cryptography;
- balanced answer-key positions and plausible distractors;
- a separate answer key and no verbatim reuse from the exposed baseline;
- pilot status until learner evidence and review support a stronger claim.

A missed gate keeps the October course active and creates a concise class-entry
brief: unresolved terms, critical-safety concepts, and questions to listen for
during instruction.

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

1. Complete the M01 Rules of Engagement correction and authorized localhost
   exercise.
2. Retest the M01 critical-safety competency on `2026-09-07`.
3. Run the W37–W41 grouped module previews and eight-item posttests within the
   protected `4 h` weekly ceiling.
4. Prepare and lock `preclass_form_b` by `2026-10-04`.
5. Take and score Form B on `2026-10-10` or `2026-10-11`, then produce the
   class-entry brief.
6. Use the low-friction daily loop in `daily-closed-loop-plan.md`; collect
   confidence on every new scored item.
