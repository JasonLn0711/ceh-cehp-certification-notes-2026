# Graphify installation and verification — 2026-10-14

Graphify is installed on this Mac, and the CEH sample graph is built. The CLI,
graph integrity, and semantic document update passed the checks below. Browser
rendering remains a manual check because the browser tool rejected the local
`file:` URL under its HTTP(S)-only URL policy.

## Installed components

| Component | Verified value |
|---|---|
| Source | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) |
| Revision | `041771be72229bb2c8d8205b9cc6871c6be52b91`, detached checkout from `v8` |
| Checkout | `../graphify` relative to the CEH repository root |
| Package / CLI | `graphifyy` / `graphify`, version `0.9.90` |
| Installation | Editable source installation in an isolated `uv` tool environment |
| Interpreter | Python `3.12.15`, selected explicitly |
| Runtime environment | `~/.local/share/uv/tools/graphifyy/` |
| Executables | `~/.local/bin/graphify`, `~/.local/bin/graphify-mcp` |
| Codex skill | `~/.codex/skills/graphify/SKILL.md`, plus eight reference files |
| Semantic extraction | Current Codex session; one extraction worker per batch |
| Clustering | NetworkX Louvain fallback; optional Leiden dependencies were not installed |

The source was cloned, checked out at the revision above, and installed with
the following commands, with `graphify` as the working directory:

```bash
uv tool install --python /opt/homebrew/bin/python3.12 --editable .
graphify install --platform codex
graphify --version
```

The native installer handles the upstream `skill-codex.md` and reference
sidecars. The generic skill installer expects a repository directory already
containing `SKILL.md`, so it does not match this upstream packaging.
The installed skill is available on the next Codex turn.

Global Codex instructions and configuration, Planning instructions, and CEH
instructions have the same before/after SHA256 values. No Codex hooks file was
created. The Graphify source checkout has no tracked modifications. Installing
the `graphify-mcp` executable does not register or start an MCP server.

## Verified results

| Check | Observed result |
|---|---|
| Dependency consistency | `uv pip check` passed for 30 installed packages. |
| Skill references | All eight referenced files exist and match the pinned source bytes. |
| Initial extraction | Five notes, about 834 words; 24 nodes and 32 edges. |
| Final graph | Five notes, about 872 words; 25 nodes, 34 edges, six communities. |
| Confidence tags | All 34 relationships are EXTRACTED with score 1.0; input examples remain synthetic. |
| Integrity | No missing/dangling endpoints, self-loops, duplicate edges, or directed edge collapse. |
| Sources | Every node and edge resolves to a corpus file and a real section; all five notes represented. |
| CLI | Query, explanation, and the four-hop Port Observation → Verification Record path pass. |
| Absent concept | `explain zzzz_missing_concept_7391` returns no match and exit 4. |
| Semantic update | One changed note re-extracted; Review Gate adds one node and two edges. |
| Update preservation | All 18 nodes and 27 edges attributed to unchanged notes are retained. |
| Incremental recheck | Zero changed/deleted files after saving the updated manifest. |
| Validator failure cases | Dangling endpoint, out-of-corpus source, missing section, invalid confidence score, and missing graph are rejected. |
| HTML static checks | Embedded node/edge data matches the final graph; three inline scripts pass JavaScript syntax checks. |
| Browser rendering | Pending manual opening; local file navigation was blocked by the browser tool's URL policy. |

The initial graph and update trace are retained in ignored `.local/` files.
The new Review Gate section remains in the fifth note as the reproducible result
of the update test. This acceptance is for the prepared tooling and sample,
not the learner's mission completion or a real security assessment.

## Practical limits

The HTML loads `vis-network` from `unpkg.com`; it needs that CDN reachable.
The terminal query's `--budget` may be exceeded to retain relationships.
Graph confidence describes extraction, not truth or security assurance.

The host extraction tools did not expose token usage. The report explicitly
labels usage unavailable. `cost.json` preserves numeric zero fields for upstream
compatibility and carries an unavailable-usage notice; those fields are not
measured zero usage. No separate model-provider API was configured or invoked.

The local `anti-ai-rhetoric-lint` skill was unavailable. The prose was checked
against the existing voice contract, preserving synthetic status, uncertainty,
source attribution, and learner ownership.

## Reuse, upgrade, and removal

Use [the README](README.md) for build prompts and working commands. Keep source
upgrades explicit: this editable installation follows the checkout's files,
so changing its revision changes the running code. Record the old revision,
inspect the selected new revision, reinstall with Python 3.12, refresh the skill,
and rerun this lab's checks before treating an upgrade as verified.

For removal, first move only `~/.codex/skills/graphify/` to a uniquely named
backup directory outside the skill roots, then run:

```bash
uv tool uninstall graphifyy
```

Keep the source checkout and lab files until you choose to remove them. Avoid
the upstream broad uninstall/purge route when you only intend to remove this
installation. The installation stage made no Git commits or pushes. The later
October 14 request authorizes separate publication of the authored lab and
Planning records; generated outputs stay local. See the
[Planning locator](../../../planning-everything-track/data/projects/2026-10-graphify-ceh-lab.md)
for ownership and the delivery response for verified commit IDs. No schedules
or global learning-rule changes were made.

## Contribution and next action

Audience: Jason's personal CEH practice. Jason selected the CEH track, fresh
sample inputs, a runnable starter, and the current Codex session. The assistant
installed the tool, authored the sample and missions, and verified the graph
workflow. These artifacts can support future study notes and a small portfolio
demonstration after Jason produces his own explanations and results.

Next action: open the HTML locally, then attempt Mission 1 within an existing
learning block. Preserve the first explanation in the worksheet; editorial help
and any publication follow the existing course acceptance rules.
