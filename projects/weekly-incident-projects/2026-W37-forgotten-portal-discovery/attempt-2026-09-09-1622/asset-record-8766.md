# Asset Record — 127.0.0.1:8766/tcp

Date: 2026-09-09
Exercise: WP-2026-W37 — Forgotten Portal Discovery

## Target
127.0.0.1:8766/tcp

## Supplied register entry
No entry for TCP port 8766.

The supplied register contains:
- 8765/tcp — public portal — Digital Services
- 8767/tcp — observability — Platform Operations

## Actual observation
One authorized Nmap TCP connect scan reported:

8766/tcp open amcs

The mock startup log also reported:

LISTENING 127.0.0.1:8766 role=legacy-reporting

## Evidence files
- scan-transcript.txt
- mock-server.log
- supplied-register.md
- roe.md

## Evidence-backed inference
TCP port 8766 was reachable during the authorized test but was absent
from the supplied asset register.

This supports an inventory/register gap.

## Important evidence limitation
The Nmap SERVICE label "amcs" is not treated as verified application identity.

The scan demonstrated TCP reachability, not:
- a vulnerability
- exploitability
- verified organizational ownership
- verified software identity or version

The mock's role label "legacy-reporting" is runtime information reported
by the supplied training program and is kept separate from the Nmap
port-service label.

## Unverified claims
- Organizationally accountable owner of 8766
- Service-reported metadata from /service-info
- Software/version identity
- Vulnerability status
- Exploitability

## Next authorized action
No further active action is authorized under the expired testing window.

Under a future dated authorization window, the next bounded action may be
an HTTP GET to /service-info on the supplied mock, provided all ROE
conditions and stop conditions remain satisfied.

No exploitation or credential testing is justified by the current evidence.
