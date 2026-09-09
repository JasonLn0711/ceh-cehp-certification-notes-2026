# Focused Research Note

Date researched: 2026-09-09
Exercise: WP-2026-W37 — Forgotten Portal Discovery

## Question

What does Nmap's TCP connect scan (-sT) establish, and does the
SERVICE column prove the identity of the application running on a port?

## Primary sources

1. Nmap Network Scanning — Port Scanning Techniques
   https://nmap.org/book/man-port-scanning-techniques.html

2. Nmap Network Scanning — nmap-services
   https://nmap.org/book/nmap-services.html

## Supported claims

### TCP connect scan

Nmap documents that -sT is a TCP connect scan.

Instead of creating raw packets itself, Nmap asks the operating system
to establish a connection to the target port using the connect()
system call.

Therefore, the observation:

8766/tcp open

supports the bounded claim that a TCP connection could be established
to that port during the scan.

### SERVICE column

Nmap maintains an nmap-services database that associates port numbers
and protocols with service names.

Therefore, the SERVICE label:

amcs

must not by itself be interpreted as verified application identity.

## Effect on today's decision

The scan provides runtime evidence that 127.0.0.1:8766/tcp was
reachable during the authorized test.

The label "amcs" is not sufficient evidence that the actual application
running there was AMCS.

Because 8766/tcp was absent from the supplied register, today's evidence
supports an inventory/register gap.

The current evidence does not establish:
- a vulnerability
- exploitability
- verified organizational ownership
- verified software identity
