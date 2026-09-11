# WP-2026-W36 — Authorization Gate

> Active acceptance amendment — September 11: use the
> [choice-based contract](../../../assessments/posttests/module-posttest-template.md)
> prospectively for learner decisions and mapped assessments. Required prose
> explanations become selected evidence/risk/defense/scope decisions; independent
> practical evidence, dated ROE, refusal timing, hashes and target boundaries
> remain required. Unaided verbal recall is not assessed. Existing attempts and
> their scores remain unchanged; this amendment grants no active testing scope.
> [Current dashboard](../../../assessment-governance/readiness_dashboard.md) owns
> the current state; dated receipts below retain their event-time claims.

## Identity

- Week: `2026-W36`, `2026-08-31` through `2026-09-06`
- Curriculum: CEH M01, Introduction to Ethical Hacking
- Core capacity: `2 h`
- Learner state: `planned`
- Canonical research: [`../../../research-briefs/2026-W36.md`](../../../research-briefs/2026-W36.md)
- Acceptance: one authorized action, two pre-execution refusals, verified
  evidence integrity, and a closed-book explanation

## Historical Incident Facts

- Source dates: `2026-07-30` incident report and `2026-08-31` mitigation
  update; locators checked `2026-09-05`.

Anthropic reported that models in cybersecurity evaluations reached real
systems outside intended simulated environments. Its incident and mitigation
reports describe explicit scope, isolation, monitoring, action blocking, and
human escalation as parts of the response:

- [Investigating three real-world incidents in our cybersecurity evaluations](https://www.anthropic.com/research/investigating-incidents-cybersecurity-evals)
- [Improving our alignment and security practices](https://www.anthropic.com/news/improving-alignment-security-efforts)

The weekly research brief owns the broader NIST, Taiwan-law, and agent-security
source analysis.

## Fictional Teaching Instance

The learner is the authorized operator for a local training artifact. The
server, filename, authorization window, request count, and evidence files are
instructional elements. They do not reconstruct Anthropic's evaluation
environment or any external system.

## Prerequisites

- `python3`, `curl`, `script`, and `sha256sum`
- TCP port `8765` available on `127.0.0.1`
- one uninterrupted ten-minute execution window in `Asia/Taipei`
- two terminals

Confirm the port before creating the ROE:

```bash
ss -ltn '( sport = :8765 )'
```

An existing listener activates the stop condition. Identify it and choose a
new documented port through an ROE amendment before continuing.

## Mock ROE

Copy this table into the attempt directory and fill every pending field before
starting the server.

| Field | Authorized value |
| --- | --- |
| Authorizer | Jason Lin, owner of the local training environment |
| Operator | Jason Lin |
| Purpose | CEH M01 authorization and scope exercise |
| Host | `127.0.0.1` |
| Port | `8765` |
| Path | `/public.txt` |
| Method | exactly one `GET` |
| Window | pending: dated ten-minute `Asia/Taipei` window |
| Evidence | ROE, decisions, client transcript, server log, hashes, explanation, reflection |
| Stop | ambiguity, expiry, unexpected target, sensitive data, instability, or unexpected impact |
| Resume | dated amendment from the authorizer covering target, action, and time |

## Mission

Create an attempt directory outside the project source, for example:

```bash
attempt_dir="$(mktemp -d)"
printf 'authorized local artifact\n' > "$attempt_dir/public.txt"
cd "$attempt_dir"
```

In terminal one, after the ROE is complete and its window has started:

```bash
python3 -m http.server 8765 --bind 127.0.0.1 2>&1 | tee server.log
```

Before every proposed action, compare operator, target, method, time, count,
and stop state with the ROE.

| Proposed action | Required decision |
| --- | --- |
| `GET http://127.0.0.1:8765/public.txt` | `ALLOW` and execute exactly once |
| `GET http://127.0.0.1:8766/public.txt` | `STOP — authorization required`; do not send |
| `GET http://127.0.0.1:8765/private.txt` | `STOP — authorization required`; do not send |

In terminal two, record only the allowed request:

```bash
script -q -c 'curl --fail --silent --show-error http://127.0.0.1:8765/public.txt' client-transcript.txt
```

Stop the server with `Ctrl-C`, then preserve integrity evidence:

```bash
sha256sum public.txt server.log client-transcript.txt > SHA256SUMS
sha256sum --check SHA256SUMS
```

## Evidence Checklist

- completed and dated `roe.md`
- `decision-table.md` containing all three decisions and policy reasons
- `client-transcript.txt`
- `server.log`
- `SHA256SUMS` and successful verification output
- `explanation.md` answering who, what, how, when, stop, resume, evidence, and
  why reachability does not grant permission
- `reflection.md` recording the first blocker, focused research, correction,
  rerun, and next action

## Acceptance Check

The project is `accepted` only when:

- the authorized request occurred exactly once inside the declared window;
- neither excluded request was sent;
- client and server evidence agree on the allowed request;
- the hash verification passes;
- the learner explains the authorization predicate closed-book; and
- the M01 delayed retest is completed under the assessment-governance rules.

Prepared instructions and author validation keep learner state at `planned`.

## Red-Capacity Fallback

Use one `25 min` block to complete the dated ROE and decision table. Preserve
the result as `attempted`; execution and acceptance remain open.
