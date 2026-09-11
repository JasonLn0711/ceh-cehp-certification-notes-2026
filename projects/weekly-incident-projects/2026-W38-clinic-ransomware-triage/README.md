# WP-2026-W38 — Clinic Ransomware Triage

- Week: September 14–20; learner state: `planned`; packet: runnable offline.
- Outcome: prioritize three synthetic assets using patch, process, file and
  traffic evidence, then preserve one checked containment/remediation decision table.
- Modules: M05 vulnerability analysis, M06 system compromise/persistence,
  M07 malware evidence and M08 traffic interpretation.
- Capacity: all study remains within 240 minutes; default project allowance
  75 minutes. Red fallback: one 25-minute worksheet action and saved blocker.

## Historical facts and source check

The [NAO investigation](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/)
examines the WannaCry attack affecting the NHS on May 12, 2017. It motivates
patching, incident triage and service continuity in this exercise. Microsoft's
[MS17-010 bulletin, March 14, 2017](https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010)
describes Windows SMBv1 vulnerabilities and the corresponding security update.
These are historical incident/technical sources, checked during author
preparation September 11, Asia/Taipei. The older CISA incident locator returned
HTTP 403; use NAO as the readable primary anchor. These checks do not fulfill
W38's fresh research gate. Exact malware attribution is outside the fixture evidence.

## Fictional instance and scope

All asset names, observations and findings in `fixtures.csv` are synthetic.
They do not reconstruct NHS systems or actual WannaCry telemetry. No malware,
packet capture, credentials or operational system is supplied. The worksheet
records proposed actions only; its checker cannot contain, patch or scan hosts.

At activation record a dated study endpoint and the learner's authorization
for reading these fixtures, editing a new local attempt worksheet and running
`check.py` against that worksheet. No network requests, service starts, external
captures, exploit testing, malware downloads or real-host changes are included.
Stop on real sensitive data, an external target, an unexpected executable or
expiry. A changed action requires fresh authorization. A preparation request
is not a learner attempt.

## Start with one observable decision

Prerequisite: Python 3 and access to these plain-text files. Work from this
packet directory. Preserve outputs in a new learner-owned attempt directory;
never overwrite the original fixtures, worksheet or a previous attempt.

1. Read this scope and the eight fixture rows. Copy `worksheet.csv` into the
   new attempt directory; fill only clinic-a as the first attempt. Save it.
2. Compare patch exposure, compromise behavior and network observations.
   Record one exact uncertainty or blocker before wider reading.
3. During W38, verify the relevant mechanism in a fresh official source and
   record the date, source, question and changed decision in
   `../../../research-briefs/2026-W38.md`. If there is no blocker, verify the
   scanner-finding versus confirmed-condition distinction. The tutor curates
   the full weekly brief under the repository contract; learner reading stays
   inside the same time budget.
4. Complete the other rows; run the artifact check below. Preserve the first
   result, apply a correction and rerun if needed. If no correction is needed,
   preserve that fact and repeat the check to confirm the saved artifact.
5. Hash the fixtures, final worksheet and saved check outputs. Record the
   actual focused minutes, evidence limits, chosen decisions and next action.
   A hash establishes byte integrity relative to the saved baseline, not truth.

```bash
python3 check.py /path/to/your/attempt/decisions.csv
```

`check.py` contains the instructor validation key: use its CLI only until the
formal task is scored. Exit 1 means the artifact needs review; exit 2 means
input/usage needs correction. Neither a prepared packet nor a passing author
self-test counts as learner work.

## Worksheet choices and policy

Use one value per field. Priorities 1, 2 and 3 rank these assets relative to
each other. Policy: prioritize correlated suspected active compromise, then
corroborated exposure without observed compromise, then a disputed scanner finding.

- Verdict: `suspected_compromise`, `exposed_weakness`, `unverified_finding`.
- Next action: `contain_in_plan`, `patch_in_plan`, `verify_in_plan`.
- Evidence IDs: semicolon-separated IDs from the supplied fixture rows.
- `contain_in_plan`: preserve evidence and propose approved isolation with
  continuity review; do not execute a real containment action.
- `patch_in_plan`: propose approved patching and reducing unnecessary SMBv1
  exposure, followed by validation; do not modify any machine.
- `verify_in_plan`: reconcile scanner method with authenticated patch evidence;
  do not claim confirmed vulnerability or discard the conflicting source.

## Acceptance and module mapping

| Module | Independent learner evidence |
| --- | --- |
| M05 | Three-row priority table separates compromise, exposure and disputed scanner output |
| M06 | clinic-a decision cites persistence evidence; access vector and privilege level remain unverified |
| M07 | clinic-a correlates file behavior; no named-family or AI-generated attribution accepted without evidence |
| M08 | clinic-a/clinic-b traffic evidence distinguishes attempts/reachability from successful exploitation |

Weekly acceptance requires the learner's first saved attempt, exact blocker
or validation question, fresh W38 research, correction or justified no-change
plus rerun, passing artifact check, integrity record, selected evidence/scope
decisions and all four governed module passes. Avoid a circular gate: score
module conceptual results first; accept practical requirements independently;
then finalize the module pass and weekly acceptance together only when both
sets of checks clear. M01 remains a separate safety prerequisite for any later
active testing. Unfinished W37 non-safety work stays attached to W37.

Use [M05–M08 choice forms](../../../assessments/posttests/m01-m08-choice-v0.2.0.md)
and the [assessment contract](../../../assessments/posttests/module-posttest-template.md).
The AI skill route is a short record of whether AI was used, permitted synthetic
inputs, one independently checked suggestion when used, and human ownership.
Mark AI-use evidence pending when no suggestion was actually checked.

## Copy-ready tutor prompt

Teach me as a computer science professor using this W38 packet and the current
choice contract. Begin by confirming my remaining weekly minutes and a dated
endpoint. Explain vulnerability versus compromise, persistence, ransomware-like
behavior, packet evidence and containment plainly. Keep historical source facts
separate from these synthetic observations. Read the fixture rows with me; ask
me to select and save the first asset decision, then wait for my actual artifact.
Use that attempt's blocker to drive same-week official-source research. Help me
apply a correction, rerun the check and preserve evidence. Introduce the purpose
before each action. Stay entirely offline except explicitly scoped public-source
reading; do not scan, capture traffic, fetch malware or change real hosts.
Reuse the mapped ten-question module tests rather than adding generic quizzes.
In formal mode show one question at a time, collect choice and low/medium/high
confidence and withhold feedback until the originals are scored. In tutoring
mode explain immediately. Reteach every error and give at least three varied
retests one at a time; keep original and retest scores separate. Stop at the
endpoint and record partial work. Selected answers do not establish unaided
verbal recall, and your generated output never becomes my execution evidence.
Close with actual artifact state, original scores, confidence, separate retests,
practical acceptance and the smallest next action. Keep the full record in CEH;
Planning receives only state, capacity, evidence locator and next gate.

## Instructor preparation

[Instructor key](instructor-key.md) explains the artifact decisions. Author
validation: `python3 check.py --self-test`, using only temporary synthetic files
and no network activity. Record its result separately from learner evidence.
W39 packet preparation remains due September 20.
