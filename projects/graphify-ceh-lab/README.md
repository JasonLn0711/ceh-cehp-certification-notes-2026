# Graphify CEH lab

Turn five short CEH notes into a graph you can inspect, question, and audit.
Start by tracing how a port observation informs an assessment and what evidence
is needed before closing a finding. The supplied observations are synthetic.

This is an optional prepared lab. Your own explanations and saved results are
the learner evidence. Follow the [active course route](../../study-plan/uuu-aligned-ceh-cehp-2026-09-18.md)
with the existing 240-minute weekly ceiling and 25-minute Red/class-day steps.
There is no new deadline, recurring task, or completed learning claim.

## Start with the installed example

From the CEH repository root:

```bash
cd projects/graphify-ceh-lab
graphify --version
python3 check_graph.py
open graphify-out/graph.html
graphify explain "Port Observation"
graphify path "Port Observation" "Verification Record"
graphify query "service evidence vulnerability assessment" --budget 1200
```

`open` is the macOS browser command. The generated HTML loads its visualization
library from `unpkg.com`; browser rendering needs that CDN to be reachable.
The CLI returns graph context; use the
source notes to write your explanation. The query words above come from the
graph's own vocabulary. Exact labels or IDs work best for `explain` and `path`.
An absent concept can return exit code 4, and an ambiguous name can return 3.
`--budget` is a size hint: the CLI may retain all relationships and exceed it.

Start with [Mission 1](missions.md#mission-1-ceh-concept-atlas), then save your
own response using the [worksheet](worksheet.md). Read the
[reference answers](reference-answers.md) after attempting the questions.

## What the graph means

| Term | Meaning in this lab |
|---|---|
| Node | A concept, source, or example entity, such as Service Identification. |
| Edge | A labelled relationship between two nodes, with a source and confidence tag. |
| Directed path | A sequence of relationships followed in their recorded direction. |
| Community | A group of connected nodes; useful for navigation, not a course syllabus. |
| EXTRACTED | The input explicitly states the relationship. The input still needs evaluation. |
| INFERRED | The model added an interpretation; inspect its support. |
| AMBIGUOUS | The relationship remains uncertain. |

The local graph is a map of these notes. A path is not proof of a vulnerability,
causation, exploitation, or remediation. Confidence scores follow Graphify's
extraction rubric; they are not measured security probabilities.

## Build or refresh through Codex

Open **this lab folder** as the Codex working directory. The installed skill
is available with `$graphify` on the next turn. Paste:

```text
$graphify ./corpus --directed
Build only this lab's five sample notes. Run commands from the lab directory
and keep all outputs under its graphify-out directory. Use the current Codex
session for semantic extraction; do not configure or call a separate model
provider. Set GRAPHIFY_OUT to this lab's absolute graphify-out path in pipeline
subprocesses so the semantic cache stays alongside the graph. Preserve
synthetic status and source references. Use a single
canonical node per named concept, with its defining file as the source.
Validate every extraction chunk before merging. Report missing evidence
honestly. If token usage is unavailable, label it unknown instead of free.
Run python3 check_graph.py and show the Port Observation to Verification Record
path after building. Do not record learner completion.
```

After changing a corpus note, use the same prompt with
`$graphify ./corpus --directed --update`. The skill detects changed documents,
extracts their new content, merges it with the graph, and refreshes outputs.
Keep unchanged concepts' IDs when updating a file. The terminal command
`graphify update` primarily refreshes code; it does not perform this document
semantic workflow. Rebuilding requires Codex; querying a saved graph does not.

## Files and ownership

- `corpus/`: the five original sample notes; the only extraction input.
- `graphify-out/`: ignored generated graph, report, HTML, cache, and manifest.
- `check_graph.py`: standard-library check for graph shape, confidence tags,
  source files/locations, sample coverage, and the example path.
- `missions.md`: five optional missions, each split into small steps.
- `worksheet.md` and `reference-answers.md`: learner work and separate guidance.
- `INSTALLATION.md`: installed version, source pin, checks, and removal route.

Keep your local responses in `.local/` or `evidence/*.local.md`. Publishing
outputs is a separate decision. The Graphify engine lives in the sibling
`../graphify` directory relative to the CEH repository root; its checkout
is independent of these learning files. From this lab the engine path is
`../../../graphify`.

## Sources and method

The corpus cites public Nmap documentation and NIST SP 800-115. Technical source
claims, original teaching design, and synthetic observations are labelled in
each note. See the [official quickstart](https://docs.graphify.com/quickstart)
and [pinned Codex skill](https://github.com/Graphify-Labs/graphify/blob/041771be72229bb2c8d8205b9cc6871c6be52b91/graphify/skill-codex.md)
for upstream behavior. We use the existing assistant session for semantic work;
no separate provider account, database server, or MCP service is required here.


## Planning connections

The [Planning locator](../../../planning-everything-track/data/projects/2026-10-graphify-ceh-lab.md)
connects the installation to the October 14 day receipt, W42 capacity and host
integration registry. This lab owns technical details and learner evidence;
Planning owns status and available time. Start from the existing course budget.
