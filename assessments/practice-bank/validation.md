# Material validation — 2026-09-18

[Bank](README.md) · [Current route](../../study-plan/uuu-aligned-ceh-cehp-2026-09-18.md) · [Actual learner coverage](../../assessment-governance/course-coverage-2026-09-18.md)

## Checked material

- 600 original practice items: 20 modules × 30, plus two separate 125-item mock forms; 850 distinct IDs and normalized stems.
- Four distinct options and one matching key per item; registry answer and rationale agree with the corresponding key. Three distractor explanations are present. Answer positions are balanced within batches, with no four-position run.
- Both mocks have domain counts 7 / 21 / 19 / 30 / 18 / 6 / 12 / 6 / 6. Module practice and mock forms do not share stems.
- 25 task/key pairs cover P1–P5 and connect to the broader Practical domains. Five local fixture checks passed: loopback TCP states, local HTTP 200/403, 2620-byte synthetic flow total, different benign content hashes, and parameterized versus deliberately unsafe in-memory SQL.
- All stems were authored explicitly. A text-similarity check within each practice module found one pair above 0.83: the SYN/ACK versus RST state questions in M03. The different response is the intended discriminating evidence, so both remain. Text similarity is not a semantic-uniqueness or psychometric certification.
- The author reviewed intended answers and boundaries. Independent SME review and learner-based item analysis remain pending. Initial questions emphasize mechanisms, interpretation and control selection; instructor-specific tooling and advanced depth are refined from actual class evidence.

## Reproduce

From the CEH repository root:

```sh
python3 assessments/practice-bank/check.py
python3 assessments/practice-bank/lab.py self-test
```

The check is standard-library-only. P1/P2 contact only short-lived services created by the process on 127.0.0.1; other fixtures are offline or in-memory. No external target, paid code, credential or cloud account is used. A successful check validates teaching materials, not Jason's operation or official exam readiness.

## Revision boundary

Use actual class delivery, recorded mistakes and current primary references to improve the next version. Hold ambiguous items out of readiness evidence until reviewed. Preserve already administered forms, keys and attempt versions; never count a revised or repeated core ID twice toward the 600. No new learner score, time, practical acceptance or attendance is created by this validation.
