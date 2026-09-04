# Antisyphon Rules of Engagement 101 — M01 Study Record

## Status

- Source status: `source preserved` in ignored local custody
- Study activity: `confirmed` from Jason's `2026-09-04` self-report
- M01 competency: `activation_needed`
- Learner interpretation: pending session-start retrieval and reflection
- Source URL:
  <https://www.youtube.com/watch?v=VGs5ZETSthY>

## FIRST PRINCIPLE

- Scarce resource: trustworthy learner evidence before the CEH13-AI course.
- Canonical home: this source folder owns the supplied transcript and its
  evidence-bounded interpretation.
- Planning role: retain the study receipt, current M01 status, and next gate.
- Evidence path: Jason's source-and-study report, the supplied transcript in
  ignored `.local/` custody, and YouTube oEmbed metadata checked on
  `2026-09-04`.
- Scope control: this practitioner source supplements the required official,
  legal, and first-party readings. Learner understanding remains a separate
  retrieval and exercise claim.
- Next gate: Jason completes the session-start closed-book response, required
  readings, mock ROE, localhost evidence, closeout, and delayed retest.

## Source Context

- Title: *Penetration Testing: Rules of Engagement 101 w/ Kent, Kevin, and
  David*
- Publisher: Antisyphon Training
- Speakers: Kent, Kevin, and David, as named in the video title
- Learning date: `2026-09-04`, Asia/Taipei
- Metadata verification: title and publisher confirmed through YouTube oEmbed
  on `2026-09-04`; publication date was not established in this intake
- Transcript provenance: user-provided transcript preserved without wording
  correction at
  `.local/source/2026-09-04-antisyphon-roe-101/transcript-user-provided.txt`
- Transcript SHA-256:
  `b22d40e0b97da5944a968cd62b721fdc6f4586af4079f6b6f97a5bbb6cb076eb`
- Transcript quality: the supplied text contains natural speech repetition and
  possible transcription errors; those features remain in the source layer

Jason reported that he had just studied this video and asked for the activity
to become part of the CEH M01 learning record. This confirms the study activity.
The mechanisms below are source-supported synthesis; Jason's independent
recall and personal reflection remain open learner evidence.

## Source-Supported Mechanisms

### ROE purpose and operating value

- A Rules of Engagement discussion aligns the client and testers on the
  assessment objective, operational boundaries, responsibilities, and expected
  result before testing begins.
- The ROE reduces legal, operational, and relationship risk by making the
  authorized target, time, technique, access, reporting, and escalation paths
  reviewable.
- Success follows the client's security objective. Gaining the highest
  privilege is one possible result, while a focused review, verified weakness,
  or business-relevant finding may be the intended outcome.

### Scoping, SOW, and ROE

- The speakers distinguish commercial scoping from operational ROE. Scoping
  estimates the assessment type, environment size, people, and effort; the ROE
  confirms how the assigned engagement will run.
- A Statement of Work establishes the purchased service and effort. The ROE
  turns that agreement into executable boundaries, contacts, constraints, and
  coordination rules.
- A changed target, unavailable application, new pivot, or different testing
  objective activates a documented scope or commercial change path rather than
  an operator expanding the engagement alone.

### People and mutual responsibilities

- Useful ROE participants include the client decision owner, technical owners
  who understand the target, legal or security representatives when relevant,
  the penetration-test lead, and the operators who will perform the work.
- The client prepares objectives, scope inputs, access, credentials when
  included, sensitive periods, change freezes, and reachable escalation
  contacts.
- The testing team follows the stated scope and method restrictions,
  communicates at the agreed cadence, preserves sensitive deliverables, and
  escalates unexpected behavior.

### Operational fields

The source supports recording these fields before execution:

- assessment objective and successful outcome;
- named testers and client points of contact;
- targets, environments, accounts, access paths, and third-party dependencies;
- start and end dates, time zones, holidays, freezes, and sensitive windows;
- permitted and restricted techniques, including rate or availability
  controls;
- escalation tree for outages, unexpected access, compromise indicators, and
  scope changes;
- evidence and report handling, encryption, delivery routes, retention, and
  audience-specific deliverables;
- the amendment path for newly valuable work or changed conditions.

### Stop, escalate, and resume

- Unexpected service failure, suspected pre-existing compromise, ambiguous
  targets, unavailable authorized systems, and newly discovered pivots require
  communication through the named escalation route.
- The operator preserves the current evidence and waits for the authority that
  owns the engagement decision when the proposed action is outside or unclear.
- A documented amendment identifies the new target, technique, purpose, and
  applicable time before the new work begins.

### Special engagement contexts

- Third-party hosting, cloud services, customer-of-customer accounts, breached
  credentials, and session material can cross ownership and authorization
  boundaries even when they are technically accessible.
- Social-engineering work benefits from advance review of the ruse, target
  population, cultural sensitivity, legal considerations, and approval owner.
- Wireless and physical work requires exact spatial and technique boundaries.
  Authorization for a wireless survey does not automatically authorize lock
  manipulation or another form of physical testing.
- International work adds time-zone, holiday, travel, tool-transport, and data-
  protection questions that should be settled before execution.

## Case Lessons Preserved From the Source

- In the courthouse story, a tester conducting a wireless assessment entered a
  mantrap and chose the contact-and-escalation path instead of manipulating a
  lock outside the authorized technique scope.
- In the web-application story, unavailable or replaced applications activated
  client contact and previously discussed fallback scope, preserving useful
  assessment time.
- The discussion of breadth versus depth connects test effort to the client's
  objective: a first broad assessment may prioritize coverage, while a focused
  assessment may spend more effort establishing impact on selected systems.
- Report format, remediation validation, collaborative demonstrations, and
  retesting have capacity consequences that belong in the engagement or a
  separately activated work package.

## Accepted Interpretation for CEH M01

The video adds practitioner workflow to the M01 foundation. It shows that ROE
is a live coordination system: the participants prepare internally, name the
people who can make decisions, translate the engagement objective into
operational boundaries, and maintain an escalation path when conditions
change.

The current M01 exercise keeps the stricter execution rule already recorded in
the learning package:

```text
Clearly permitted       -> ALLOW
Clearly outside scope   -> STOP / DENY
Unclear or ambiguous    -> STOP / ASK
```

The localhost exercise may resume after ambiguity or expiry only when the named
mock authority issues an explicit dated amendment covering the new target,
action, and time window. A casual message, tutor suggestion, or retrospective
email does not change the exercise authorization.

## Evidence and Claim Controls

- Statements about criminal liability in the transcript are practitioner
  commentary. Taiwan Criminal Code Articles 358–360 and qualified legal advice
  remain the appropriate legal evidence paths for a real situation.
- Cloud-provider authorization policies change. Any Azure, AWS, EC2, or other
  provider-specific testing rule mentioned in the transcript requires a fresh
  check against the provider's current official policy before use.
- Examples involving breached credentials, cookies, password spraying,
  physical entry, lock tools, or social engineering are conceptual learning
  material. They do not authorize Jason to perform those actions.
- The video does not replace the three required M01 source groups: NIST SP
  800-115, Taiwan Criminal Code Articles 358–360, and Anthropic's incident and
  mitigation reports.
- Source study does not prove independent recall, practical execution, or a
  passing posttest. Those claims activate only from Jason's own saved evidence.
- The complete third-party transcript remains in ignored local study custody.
  External publication activates only after a separate rights review.

## Remaining M01 Gates

| Gate | Current state | Required evidence |
| --- | --- | --- |
| Practitioner source study | `confirmed` | Jason's `2026-09-04` report and this preserved source |
| Session-start retrieval | `pending` | Jason's unaided response after viewing the video |
| Three required readings | `pending` | `1–3` learner-paraphrased mechanisms from each source group |
| Mock ROE | `pending` | complete dated record written before the server starts |
| Authorized localhost exercise | `pending` | one permitted GET, two declined proposals, transcript, server log, and verified hashes |
| Learner closeout | `pending` | corrected statement, stop/resume answer, reflection, and remaining question |
| M01 posttest and retest | `pending` | `6–8/8`, critical-safety item clear, and delayed retrieval result |

## Immediate Learner Action

Without reopening the transcript or research brief, Jason answers:

> Before a security test begins, what must be defined about authorization,
> targets, permitted methods, time, reporting, and stop/resume conditions?

Because explanatory material has already been viewed, preserve the response as
`session-start closed-book retrieval`, not pristine `before-reading` evidence.

## Connection Map

- User-provided transcript: complete supplied source layer in ignored local
  custody at
  `.local/source/2026-09-04-antisyphon-roe-101/transcript-user-provided.txt`;
  integrity is recorded by the SHA-256 value above.
- [W36 research brief](../../research-briefs/2026-W36.md): canonical M01
  mechanisms, required sources, exercise, and weekly closeout.
- [Baseline attempt](../../assessments/attempts/2026-09-03-baseline-diagnostic.md):
  Q1/Q26 evidence and the `activation_needed` decision.
- [Readiness dashboard](../../assessment-governance/readiness_dashboard.md):
  current competency status and remaining gate.
- [Pre-course plan](../../study-plan/pre-course-prep.md): M01–M20 completion
  contract.
- [Planning day note](../../../planning-everything-track/weeks/2026-W36/days/2026-09-04.md):
  partial-progress receipt and immediate action.
- [Planning project locator](../../../planning-everything-track/data/projects/2026-07-ceh-cehp-certification-training.md):
  durable status, evidence path, and next gate.
