# Rules of Engagement

Exercise: WP-2026-W37 — Forgotten Portal Discovery
Date: 2026-09-09
Time zone: Asia/Taipei

## Authorization
Owner-authorizer: learner/operator
Operator: learner/operator

## Target
Address: 127.0.0.1
Protocol: TCP
Ports: 8765-8767

## Permitted activity
- Read the supplied asset register.
- At most two TCP connect scans during the active-testing window.
- HTTP GET requests only to:
  - /health
  - /service-info

## Timing
Learning block: 16:22-16:52
Active-testing window: 16:27-16:47

## Scan history before this attempt
Learner-reported TCP connect scans against this target today: 0

## Rate control
Default local Nmap timing.

## Excluded activity
- Other IP addresses
- Other ports
- Other HTTP paths
- Nmap scripts
- Credential testing
- Exploitation
- Brute force
- Flooding

## Stop conditions
Stop immediately for:
- occupied authorized ports before mock startup
- ambiguous scope
- unexpected sensitive data
- instability
- a non-loopback target
- expiry of the active-testing window

## Resume rule
Resolve the stop condition first.
Any changed activity requires a dated owner amendment before resumption.

## Evidence handling
Preserve only evidence actually produced for this attempt:
- this ROE
- supplied register
- mock server logs
- command transcripts
- observations and decisions
- later integrity hashes after files are finalized

## Dated Amendment — 2026-09-09 18:18 Asia/Taipei

The practical exercise resumes after dinner.

Learning block: 18:18-18:48
Active-testing window: 18:20-18:43

All previously defined targets, methods, exclusions, rate controls,
stop conditions, and evidence-handling requirements remain unchanged.

TCP connect scans already used: 0
Maximum TCP connect scans permitted for today's exercise: 2 total

The period after 18:43 is reserved for mock shutdown, log finalization,
evidence review, and closeout. No new active testing is authorized after 18:43.
