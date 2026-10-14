# Five Graphify practice missions

Choose one step that supports the active CEH topic. Each step has a maximum
25-minute timebox; stop with a saved result or precise blocker. These missions
have no assigned dates and share the existing course budget. Installation and
agent verification are preparation, not your completed learning.

## Mission 1: CEH concept atlas

**Build:** a small map you can explain to another learner.

1. Open `graphify-out/graph.html`, search for Port Observation, and inspect its
   neighbours. Explain five nodes in your own words. Save them in the worksheet.
2. Run `graphify path "Port Observation" "Verification Record"`. Check three
   relationships against the indicated source sections and explain the chain.

**Done:** five definitions, three source checks, and one explanation of why a
graph connection cannot prove exploitation. **Variation:** start from Scope
Record and explain why assessment conditions matter.

## Mission 2: Evidence detective

**Build:** a five-row evidence-audit casebook.

1. Pick five edges from the graph. Record source, target, relation, confidence
   tag, exact supporting sentence, and whether it concerns a fictional example.
2. Review the claim "the open endpoint proves a vulnerable application."
   Decide whether the notes support it and list the missing evidence. Separate
   a wrong extraction from a faithfully extracted but unsupported source claim.

**Done:** five audited edges and a supported correction of the claim. If the
graph contains only EXTRACTED edges, report that fact; do not manufacture an
INFERRED example. **Variation:** evaluate whether a filtered result identifies
the device doing the filtering.

## Mission 3: Living study map

**Build:** a graph that reflects one documented change.

1. Add one short new section to a sample note with an explicitly stated
   relationship and a citation or a clear original-example label. Save the old
   graph in `.local/` before updating. Use the Codex semantic `--update` prompt
   in the README, keeping concept IDs stable.
2. Run `python3 check_graph.py`, query the added concept, and inspect its source.
   Check that the other four notes are still represented. Ask for another
   update without changing anything; it should detect no changed files.

**Done:** before/after evidence, the new source-backed relationship, and a
no-change result. **Variation:** correct an existing statement; ensure the old
relationship is removed rather than simply adding its correction.

## Mission 4: Study-gap finder

**Build:** a tiny source-backed study guide.

1. Ask three questions using terms from the graph. For each, save the command,
   supporting nodes, source sections, and your explanation.
2. Ask "Which real CVE affects Lab Gateway?" Record that the corpus deliberately
   lacks a real product and advisory. Explain which evidence could answer it.

**Done:** three supported answers and one explicit evidence gap.
**Variation:** after separate selection of a public advisory, make an original
summary and connect its affected conditions to the assessment workflow. Keep
that later research distinct from this fictional example.

## Mission 5: Graph versus text search

**Build:** a small tool-evaluation report.

1. Answer the five questions below by reading/searching the corpus. Record
   elapsed time and source sections, without viewing the reference answers.
2. Answer them using Graphify and record the same fields. Compare correctness,
   source traceability, time, and cases where either method missed context.

Questions: What constrains Port Observation? Why is a port number insufficient
for service identification? What informs Advisory Applicability? What is
missing before a Candidate Finding is supported? What informs Closure Decision?

**Done:** a five-row comparison and one practical rule for choosing a tool.
Reusing questions creates a practice/order effect; report it. This tiny exercise
does not establish a general speed or token-saving benchmark.

## Other projects this prepares you for

- Map a small codebase's functions and imports to understand a change's impact.
- Connect public paper summaries to methods, evidence, and research questions.
- Build an incident timeline from selected public reports, retaining source
  disagreement and uncertainty.

These are future options. Activate one only when it supports an existing
priority and has a bounded input set and completion check.
