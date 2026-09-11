# W38 instructor key

Keep this file and the source of `check.py` separate from the learner-facing
brief until scoring. The checker owns the exact validation constants.

| Asset | Verdict | Rank | Proposed action | Required evidence | Reason |
| --- | --- | --- | --- | --- | --- |
| clinic-a | suspected_compromise | 1 | contain_in_plan | e02;e03;e04 | Correlate persistence, file disruption and attempted peer connections; preserve evidence and continuity before approved containment. The fixture does not prove family, initial vector, privilege or peer compromise. |
| clinic-b | exposed_weakness | 2 | patch_in_plan | e05;e06 | Applicable missing update plus unnecessary SMBv1 exposure supports remediation; no observed compromise is not proof of absence. |
| clinic-c | unverified_finding | 3 | verify_in_plan | e07;e08 | Banner finding conflicts with authenticated patch evidence; reconcile without erasing either source. |

Accept additional evidence IDs for the same asset, but reject fabricated or
cross-asset IDs. All three rows must be present exactly once. If a learner
proposes another defensible operational action, preserve it for human review;
the checker scores only the explicitly stated synthetic policy. Never change
a fixture or key to make a recorded learner attempt pass.

The exercise supplies no malware and performs no real containment, patching,
scanning or packet capture. `artifact_checks_passed` is one acceptance component;
research, learner provenance, integrity, mapped module checks and the weekly
review remain independent. Tutor-generated worksheets and author checks never
advance learner state. Discuss disagreements before revealing the full key.
