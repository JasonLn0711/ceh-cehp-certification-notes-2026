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

Verify the environment code before the learner week with:

```bash
python3 mock_services.py --self-test
```

## ROE

| Field | Authorized value |
| --- | --- |
| Authorizer and operator | learner as owner/operator of the local mock instance |
| Target | `127.0.0.1` ports `8765–8767` only |
| Methods | inspect supplied register; at most two TCP connect scans; HTTP `GET` to `/health` and `/service-info` |
| Time | learner records one dated `60 min` window in `Asia/Taipei` |
| Request/rate control | local default `nmap` timing; no scripts, brute force, flooding, or paths outside the allowlist |
| Evidence | ROE, scan transcript, service metadata, asset map, decision log, hashes, explanation |
| Stop | port conflict, scope ambiguity, non-loopback target, unexpected sensitive data, instability, or expired window |
| Resume | dated learner-owner amendment before any changed action |

## Mission

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
mock's role, version, and owner are established through the authorized
`/service-info` enumeration step.

Enumerate only the approved metadata endpoint:

```bash
for port in 8765 8766 8767; do
  curl --fail --silent --show-error "http://127.0.0.1:${port}/service-info"
  printf '\n'
done | tee service-info.txt
```

Stop the services with `Ctrl-C`. Create `asset-map.md` with one row per
discovered service:

| Target | Discovery evidence | Enumerated role/version | Recorded owner | Ownership gap | Next authorized action |
| --- | --- | --- | --- | --- | --- |

Finish with:

```bash
sha256sum server.log scan-transcript.txt service-info.txt asset-map.md > SHA256SUMS
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
- identifies the omitted service and its missing owner;
- distinguishes passive reconnaissance, active scanning, and HTTP enumeration;
- preserves the ROE, transcripts, asset map, decision log, and verified hashes;
- states that version banners are evidence requiring validation rather than
  proof of vulnerability; and
- completes the mapped M02–M04 diagnostics and any still-open M01 safety repair.

## Red-Capacity Fallback

Use one `25 min` block to complete the ROE, run the supplied self-test, compare
the register with the self-test output, and preserve the first evidence or
blocker. The project remains `attempted` until the bounded scan and asset map
pass acceptance.
