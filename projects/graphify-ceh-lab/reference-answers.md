# Reference answers — read after your attempt

These are prepared guidance, not learner answers or scores. Use the actual graph
and note sections to check your wording; a future extraction can vary.

## Core chain

Port Observation feeds Service Identification, which feeds Vulnerability
Assessment. Vulnerability Assessment informs Remediation Plan, which requires
Verification Record. These statements define the original sample workflow;
they describe no real scan or remediation. Graphify may represent the workflow
with generic relationship labels such as `references`.

## Mission 1

A node names something; an edge records a relationship. A path follows connected
relationships. A community groups connected nodes. EXTRACTED says the input
stated an edge, while INFERRED and AMBIGUOUS identify interpretation or
uncertainty. None of those tags turns a fictional example into a measured fact.

## Mission 2

An open endpoint supports an observation about an accepting application under
the observation conditions. The corpus supplies no actual product, advisory,
configuration, or exploit evidence. It cannot support a vulnerability claim.
Read [port observations](corpus/02-port-observations.md) and
[vulnerability assessment](corpus/04-vulnerability-assessment.md).

A filtering observation alone does not identify the filtering device. A model
that adds a specific firewall without source support has over-interpreted the
record. Mark or remove that relationship with an explicit reason.

## Mission 3

Success means the graph includes the changed statement with the correct source,
preserves unaffected notes, and detects no further changes after the manifest
is saved. Node counts can change; equal counts alone do not establish a correct
update. A missing source or stale relationship is a useful blocker to record.

## Mission 4

Supported answers cite note sections. The CVE question remains unanswered
because the example deliberately omits a real product/version and advisory.
Explain the missing evidence instead of choosing a plausible CVE.

## Mission 5

1. **Scope Record** constrains Port Observation: `01-assets-and-scope.md`.
2. Services can use unexpected ports; response evidence helps identify them:
   `03-service-identification.md`.
3. **Version Candidate** informs Advisory Applicability, with corroboration:
   `03-service-identification.md`.
4. Product corroboration, applicable advisory text, and configuration evidence
   remain missing: `04-vulnerability-assessment.md`.
5. **Verification Record** informs Closure Decision, which remains pending:
   `05-remediation-verification.md`.

A graph is often useful for connected questions, while a direct source read is
necessary to check the words behind an edge. Your five-question exercise should
show where each helped you, not assume one must win.
