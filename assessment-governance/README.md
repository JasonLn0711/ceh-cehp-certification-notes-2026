# Assessment Governance

This folder is the minimum viable assessment system for CEH / CEHP preparation.

The system keeps assessment decisions traceable from official scope to
competency claim, evidence, item, rubric, remediation, and retest result.

## Files

- `competency_map.csv`
- `item_bank.csv`
- `assessment_forms.csv`
- `attempt_log.csv`
- `traceability_matrix.csv`
- `rubric.md`
- `readiness_dashboard.md`
- `daily_closeout_template.md`

Detailed calendar plan:

- `../docs/daily-closed-loop-calendar-plan.md`

Learning packet rule:

- `../docs/day-01-03-learning-package-rule.md`

## Operating Rule

Use these files before building any larger LMS or custom app. The first useful
system is a versioned, low-friction record that changes the next study action.

Question forms remain reusable and answer-free. Preserve each learner
submission under `../assessments/attempts/`, record its summary in
`attempt_log.csv`, and use `traceability_matrix.csv` for the evidence that
changes a learning decision.

## Current delivery — September 11

Use [the ten-item choice contract](../assessments/posttests/module-posttest-template.md), with separate key and practical acceptance. Form B v0.3.0 locks October 4, runs October 10, and feeds the October 11 gap brief. The [current preparation plan](../study-plan/pre-course-prep.md) owns the 240-minute weekly ceiling and evidence-first recovery.
