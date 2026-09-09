# Metadata Comparison — 127.0.0.1:8766

Date: 2026-09-09
Request time: 20:01:21+08:00
Exercise: WP-2026-W37 — Forgotten Portal Discovery

## Observation

One authorized HTTP GET to:

http://127.0.0.1:8766/service-info

returned HTTP 200 from:
- remote IP: 127.0.0.1
- remote port: 8766

Response body:

{"environment": "fictional-loopback-training", "owner": "Unassigned", "role": "legacy-reporting", "version": "0.8.1"}

## Self-reported claims

The service reports:
- environment = fictional-loopback-training
- owner = Unassigned
- role = legacy-reporting
- version = 0.8.1

These are service-reported metadata claims, not independent organizational verification.

## Register evidence

The supplied register contains:
- 8765/tcp — public portal — Digital Services
- 8767/tcp — observability — Platform Operations

There is no supplied-register entry for 8766/tcp.

## Comparison with prior asset record

The prior asset record already identified 127.0.0.1:8766/tcp
as reachable but absent from the supplied register.

This continuation adds service-reported metadata:
- role = legacy-reporting
- owner = Unassigned
- version = 0.8.1

## Bounded inference

The evidence supports:
- 8766/tcp was reachable during the earlier authorized scan.
- 8766/tcp is absent from the supplied register.
- The service at 8766 reports itself as legacy-reporting version 0.8.1.
- The service reports owner=Unassigned.

This strengthens the inventory/ownership-gap finding.

## Still unverified

The current evidence does not independently establish:
- accountable organizational ownership
- deployed software identity beyond self-reported metadata
- vulnerability status
- exploitability

No exploitation, credential testing or additional scanning is justified
by this evidence alone.

## Continuation activity count

- Additional TCP scans: 0
- HTTP GET requests: 1
- Request path: /service-info
- Target: 127.0.0.1:8766
