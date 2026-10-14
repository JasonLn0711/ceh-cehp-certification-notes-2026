# Service identification

## Service Identification

Service Identification uses probe responses to investigate the application
behind a port. A conventional port number is a useful clue, but services can
listen on other ports. Nmap version detection attempts to identify a service's
protocol, product, and version from responses.

## Service Evidence and Version Candidate

Service Evidence is our synthetic record of an example response, its conditions,
and its limitations. It supports Version Candidate: a fictional product version
that still needs corroboration. Service Identification produces Service Evidence
and feeds Vulnerability Assessment. Version Candidate informs Advisory
Applicability; matching a version string alone does not settle applicability.

## Why preserve the response?

Another reviewer needs the observation behind a label. Our sample deliberately
omits a real product, version, address, and vulnerability identifier. Evidence Gap
tracks the missing corroboration rather than inventing a finding.

## Source

[Nmap: Service and Version Detection](https://nmap.org/book/man-version-detection.html)
explains response-based identification and the limits of port-number lookup.
Source checked 2026-10-14. The evidence-record design is an original example.
