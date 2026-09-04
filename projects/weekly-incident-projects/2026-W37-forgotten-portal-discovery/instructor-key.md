# WP-2026-W37 Instructor Key

## Expected Inventory

| Port | Role | Version | Owner state |
| --- | --- | --- | --- |
| `8765` | `public-portal` | `1.4.2` | Digital Services in supplied register |
| `8766` | `legacy-reporting` | `0.8.1` | absent from register; ownership requires assignment |
| `8767` | `observability` | `2.1.0` | Platform Operations in supplied register |

## Expected Classification

- Passive reconnaissance: reading the supplied service register without
  interacting with a target service.
- Scanning: the bounded TCP connect scan used to identify listening
  endpoints. Nmap's `SERVICE` column is a port-number label here, not verified
  role or version evidence.
- Enumeration: requesting `/service-info` from each authorized HTTP service to
  collect service-specific role, version, and ownership metadata.

## Acceptance Rubric

| Area | Pass evidence |
| --- | --- |
| Scope | target, ports, methods, window, request limit, stop/resume, and evidence handling recorded before execution |
| Discovery | all three services found inside the approved port range |
| Interpretation | `8766` identified as the registry gap; banner/version evidence remains a validation lead rather than a vulnerability verdict |
| Ownership | missing owner receives an assignment/escalation action before patch or assessment responsibility is assumed |
| Evidence | transcripts, asset map, decision log, and SHA-256 verification are consistent |
| Learning | M02–M04 diagnostics completed; M01 safety repair included only when still open |

## Safety Refusals

The learner refuses non-loopback targets, ports outside `8765–8767`, Nmap
scripts, credential testing, exploitation, flooding, and unlisted HTTP paths.
An interesting adjacent service becomes an authorization question, not an
automatic expansion.

## Common Errors

- calling the supplied register an active scan;
- treating a listening port as proof of business ownership;
- treating the mock version string as proof of a real vulnerability;
- expanding to nearby ports for completeness;
- assigning remediation work without naming the service owner;
- copying author self-test output as learner execution evidence.
