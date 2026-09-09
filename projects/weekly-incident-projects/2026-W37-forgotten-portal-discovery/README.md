# WP-2026-W37 — Forgotten Portal Discovery

## Identity

- Week: `2026-W37`, `2026-09-07` through `2026-09-13`
- Curriculum: CEH M02–M04; M01 safety repair remains available if needed
- Core capacity: `4 h`
- Learner state: `planned`
- Live-scan gate: refresh and record the W37 source scan during W37
- Acceptance: discover the omitted service and distinguish reconnaissance,
  scanning, and enumeration in an ownership-aware asset map

## Historical Incident Facts

- Source date: `2019-07-22`; locators checked `2026-09-05`.

The U.S. Federal Trade Commission's Equifax case states that an unpatched
Apache Struts vulnerability enabled the 2017 breach. The FTC also described an
incorrectly configured scanner and weaknesses in segmentation and detection:

- [Equifax settlement announcement](https://www.ftc.gov/news-events/news/press-releases/2019/07/equifax-pay-575-million-part-settlement-ftc-cfpb-states-related-2017-data-breach)
- [FTC complaint](https://search.ftc.gov/system/files/documents/cases/172_3203_equifax_complaint_7-22-19.pdf)

These sources motivate an asset-visibility exercise. They do not establish that
the fictional organization or services below existed at Equifax.

## Fictional Teaching Instance

Northbridge Learning Clinic has a local service register with two approved
entries:

| Port | Recorded service | Recorded owner |
| --- | --- | --- |
| `8765` | public portal | Digital Services |
| `8767` | observability | Platform Operations |

The supplied mock instance starts three loopback-only HTTP services. One is
missing from the register. All organization names, services, versions, owners,
and data are fictional.

## Prerequisites

- `python3`, `curl`, `nmap`, `script`, and `sha256sum`
- ports `8765–8767` available on `127.0.0.1`
- two terminals

Author-only environment check (historical validation is recorded in the professor prompt):

```bash
python3 mock_services.py --self-test
```

The self-test binds dynamically assigned loopback ports and requests metadata
from those ports. It requires a separate dated owner authorization before use;
the fixed-port learner ROE below covers only `8765–8767`. The learner path can
proceed with prerequisite checks and the authorized fixed-port mock after ROE
teach-back, keeping author self-test evidence separate.

## ROE

| Field | Authorized value |
| --- | --- |
| Authorizer and operator | learner as owner/operator of the local mock instance |
| Target | `127.0.0.1` ports `8765–8767` only |
| Methods | inspect supplied register; at most two TCP connect scans; HTTP `GET` to `/health` and `/service-info` |
| Time | learner records a dated `70 min` learning block and an active window of at most `60 min` within it, in `Asia/Taipei`; changed windows require a dated amendment |
| Request/rate control | local default `nmap` timing; no scripts, brute force, flooding, or paths outside the allowlist |
| Evidence | ROE, scan transcript, service metadata, asset map, decision log, hashes, explanation |
| Stop | port conflict, scope ambiguity, non-loopback target, unexpected sensitive data, instability, or expired window |
| Resume | dated learner-owner amendment before any changed action |

## Mission

Learning support: [GPT-6 Pro professor prompt](professor-prompt-2026-09-08.md)
defines the required concepts, procedures, real-world case boundary, guided
checkpoints, and learner-evidence contract for the `70 min` block.

Before starting either terminal, complete the ROE teach-back and record the
actual future/current window. Preserve `roe.md` and `supplied-register.md` in
one attempt directory. Use that directory for every output below; invoke the
mock using its actual repository path when working outside the project root.

In terminal one:

```bash
python3 mock_services.py 2>&1 | tee server.log
```

In terminal two, create an attempt directory and preserve the supplied register
as passive reconnaissance evidence. Then execute one bounded scan:

```bash
script -q -c 'nmap -sT -Pn -n -p 8765-8767 127.0.0.1' scan-transcript.txt
```

Treat Nmap's `SERVICE` column here as a preliminary port-number label. The
mock's returned role, version, and owner are claimed metadata from the
authorized `/service-info` enumeration step. Validate organizational ownership
and deployed-software claims with evidence appropriate to each claim.

Enumerate only the approved metadata endpoint:

```bash
for port in 8765 8766 8767; do
  curl --fail --silent --show-error "http://127.0.0.1:${port}/service-info"
  printf '\n'
done | tee service-info.txt
```

Stop the services with `Ctrl-C` and wait for the foreground process and `tee`
to finish writing `server.log`. Create `asset-map.md` with one row per
discovered service:

| Target | Discovery evidence | Enumerated role/version | Recorded owner | Ownership gap | Next authorized action |
| --- | --- | --- | --- | --- | --- |

Complete `decision-log.md` with observations, claimed metadata, inferences,
open validation, ownership decisions and any new authorization gate. Finalize
all seven named files in the same attempt directory, then finish with:

```bash
sha256sum roe.md supplied-register.md server.log scan-transcript.txt service-info.txt asset-map.md decision-log.md > SHA256SUMS
sha256sum --check SHA256SUMS
```

## Learner Questions

1. Which activity was passive reconnaissance?
2. Which evidence established that a TCP service was reachable?
3. Which action enumerated service-specific information?
4. Which service was absent from the register, and what ownership risk follows?
5. What does the evidence establish, and what does it leave unverified?
6. Which proposed next action requires a new authorization decision?

## Acceptance Check

The project is `accepted` when the learner:

- discovers all three allowed services without scanning outside `8765–8767`;
- identifies the observed service missing from the supplied register and
  records the ownership gap within that evidence scope;
- distinguishes passive reconnaissance, active scanning, and HTTP enumeration;
- preserves the ROE, transcripts, asset map, decision log, and verified hashes;
- states that version banners are evidence requiring validation rather than
  proof of vulnerability; and
- completes the mapped M02–M04 diagnostics and any still-open M01 safety repair.

## Red-Capacity Fallback

Use one `25 min` block to record the learner ROE and supplied-register
comparison, or perform the first fixed-port authorized action after the safety
gate. Preserve the actual result or blocker. Record `attempted` only after a
learner-produced action; the bounded scan, asset map and diagnostics establish
full acceptance. The ephemeral-port author self-test retains its separate
authorization path.

## Opening lesson receipt — recorded 2026-09-09

- [Complete supplied lesson](opening-lesson-2026-09-08.source.md): source for the 9/8 learning task, preserved with all 25 references.
- [Detailed notes and reconciliation](opening-lesson-2026-09-08.md): concepts, cases, evidence distinctions, local file check and next checkpoint.
- Learner state remains `planned`; source capture supplies learning support.
- Procedure revision: distinguish 70-minute learning from a maximum 60-minute active window; keep ephemeral-port self-tests under separate authorization; treat metadata as reported; finalize logs before hashing all seven named artifacts.
