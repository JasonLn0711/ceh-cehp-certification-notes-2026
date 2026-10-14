# Port observations

## Port Observation

Port Observation describes how a probe result appeared from a particular place
and time. It references Lab Gateway and Lab Vantage Point. In our synthetic
record, a TCP endpoint is Open Port from the internal viewpoint. Port Observation
feeds Service Identification, which investigates what is listening.

## Open Port and Filtered Port

Open Port means an application accepts communication on that port. Filtered Port
means filtering prevents the scanner from deciding whether it is open. These
labels describe the scanner's observation; viewpoints can yield different states.
An Open Port alone does not establish a vulnerable application.

## Evidence boundary

The example has no packet capture, actual tool execution, or second viewpoint.
Which device applies filtering remains an Evidence Gap. Treat a proposed
filtering cause as uncertain until relevant observations support it.

## Source

[Nmap: Port Scanning Basics](https://nmap.org/book/man-port-scanning-basics.html)
defines port states and explains viewpoint dependence. Source checked
2026-10-14. The example observation is synthetic.
