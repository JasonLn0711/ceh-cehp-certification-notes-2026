# Authorized Security Workbench — Legacy Design

> Active route: [`../weekly-incident-projects/README.md`](../weekly-incident-projects/README.md).
> The weekly historical-incident system superseded this continuing-workbench
> model on `2026-09-05`. The original design remains below as a migration record
> for existing `WB-*` links; it does not define current learner status.

## Purpose

This continuing side project turns CEH, CEHP, and project-linked CTF learning
into lawful, executable security work. Each week advances one vertical slice:
define acceptance, attempt, inspect the blocker, research the missing mechanism,
apply it, rerun, and preserve evidence.

## FIRST PRINCIPLE

- Scarce resource: focused execution time before and after class.
- Canonical home: this directory owns the project spine; detailed source notes,
  assessments, and evidence remain in their existing repo folders.
- Evidence path: command or action, observed output, decision record, correction,
  rerun, acceptance check, and durable locator.
- Scope control: localhost, isolated labs, supplied artifacts, licensed course
  environments, and expressly authorized CTF targets. Social engineering uses
  no-send simulations; availability work uses synthetic or low-volume evidence;
  malware uses benign artifacts; wireless records stay sanitized.
- Historical next gate: accept `WB-01` and close the M01 delayed retest.

## State Vocabulary

Use `planned`, `attempted`, `blocked`, or `accepted`. Reading, prompts,
scaffolds, prepared labs, and posttests support a slice; only executed evidence
that passes the declared check makes it `accepted`.

## Slice Roadmap

| Slice | Period | Scope | Acceptance evidence | State |
| --- | --- | --- | --- | --- |
| WB-01 | W36–W37 | M01–M04 governed localhost discovery | signed mock ROE, one allowed request, two recorded refusals, client/server evidence, verified SHA-256 manifest, explanation, M01 retest | `planned` |
| WB-02 | W38 | M05–M08 evidence triage | bounded finding set, packet evidence, confidence labels, remediation priorities, reproducible analysis | `planned` |
| WB-03 | W39 | M09–M12 human/session/availability/detection | no-send consent plan, toy session review, synthetic availability incident, telemetry comparison | `planned` |
| WB-04 | W40 | M13–M16 local web regression | local server/app checks, safe injection comparison, sanitized wireless/config evidence, rerunnable result | `planned` |
| WB-05 | W41 | M17–M20 platform and cryptographic controls | mobile/IoT/cloud trust-boundary reviews plus local integrity, certificate, or encryption evidence | `planned` |
| WB-06 | W42 | CEH course execution | daily authorized lab receipts and a prioritized class-gap queue | `planned` |
| WB-07 | W43 | end-to-end local assessment | scoped plan, execution, findings, evidence custody, report, and retest path | `planned` |
| WB-08 | W44–W45 | regression repair and release candidate | failed checks repaired, regression suite rerun, workbench release candidate reviewed | `planned` |
| WB-09 | W46–W47 | CEHP P1–P5 missions and course | five timed, authorized missions with evidence and course-gap closure | `planned` |
| WB-10 | W48 | AI-agent task adapter | machine-readable scope gate blocks an out-of-scope proposed action before execution | `planned` |
| WB-11 | W49 | controlled comparison | declared manual/agent comparison with compatible evidence and honest result | `planned` |
| WB-12 | W50–W51 | verifier correction and reproducibility | independent rerun instructions, frozen evidence manifest, corrected verifier behavior | `planned` |
| WB-13 | W52–W53 | finals continuity and handoff | minimum continuity run, year-end evidence index, lessons, and next release gate | `planned` |

## WB-01 Current Gate

M01 remains open. The source study and ROE video record establish supporting
knowledge; Jason still needs to:

1. date and complete the mock ROE before execution;
2. start the loopback-only server and execute exactly one authorized `GET` to
   `http://127.0.0.1:8765/public.txt` inside the time window;
3. record `STOP — authorization required` for port `8766` and path
   `/private.txt` without sending either request;
4. preserve the client transcript, server log, decision table, and verified
   SHA-256 manifest;
5. stop the server, explain why reachability is not permission, and complete
   the delayed M01 retest.

## Daily Loop

1. Name today's slice and one acceptance check.
2. Execute the smallest safe action.
3. Preserve the first blocker or result.
4. Research only what unlocks safety, execution, or acceptance.
5. Apply, rerun, and record `attempted`, `blocked`, or `accepted`.

When capacity is Red, perform one 25-minute executable micro-step and preserve
its blocker or evidence. A CTF challenge counts only after Jason independently
reproduces it and links the mechanism or repair to the active slice.

## Connections

- Module mapping: [`../../curriculum/official-scope-map.md`](../../curriculum/official-scope-map.md)
- Pre-course capacity: [`../../study-plan/pre-course-prep.md`](../../study-plan/pre-course-prep.md)
- Assessment and readiness: [`../../docs/assessment-governance-system.md`](../../docs/assessment-governance-system.md)
- Weekly current research: [`../../research-briefs/2026-W36.md`](../../research-briefs/2026-W36.md)
- Planning locator: [`../../../planning-everything-track/data/projects/2026-07-ceh-cehp-certification-training.md`](../../../planning-everything-track/data/projects/2026-07-ceh-cehp-certification-training.md)
