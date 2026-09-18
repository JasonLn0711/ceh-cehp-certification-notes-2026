# M02 — Footprinting and Reconnaissance — instructor key v1.0.0

[Question form](m02.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M02-Q001

**Answer: D — Passive-source research**

Passive-source research uses already available third-party information without probing the target service directly.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Data minimization:** Data minimization limits collection to information actually needed for the authorized purpose.
- **B — Source corroboration:** Corroboration compares independent evidence because a single public record may be incomplete, stale or misleading.
- **C — Active reconnaissance:** Active reconnaissance sends requests or probes to the target or its infrastructure and requires appropriate scope.

Coverage: M02; CEH v5 domain 2; Passive and active reconnaissance.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q002

**Answer: D — A record**

An A record maps a name to an IPv4 address.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — MX record:** An MX record identifies mail exchangers for a domain and includes preference values.
- **B — AAAA record:** An AAAA record maps a name to an IPv6 address.
- **C — CNAME record:** A CNAME record makes one name an alias of another canonical name.

Coverage: M02; CEH v5 domain 2; DNS records.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q003

**Answer: C — NS record**

An NS record identifies an authoritative name server for a DNS zone.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — SOA record:** An SOA record carries zone authority metadata including a serial number and timing values.
- **B — TXT record:** A TXT record carries text, including formats used by some email policies and ownership checks.
- **D — PTR record:** A PTR record maps a reverse-DNS name toward a host name; it does not prove service ownership.

Coverage: M02; CEH v5 domain 2; Additional DNS data.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q004

**Answer: C — RDAP registration data**

RDAP provides structured registration information; privacy redaction and registry differences limit what it reveals.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Document metadata:** Document metadata can reveal properties such as authoring software or author fields, which may be stale or user-controlled.
- **B — Search-engine indexing:** A search engine exposes its indexed view of content; cached results can lag behind current deployment.
- **D — Certificate transparency logs:** Certificate transparency records publicly logged certificates and can reveal names, but not whether a service is currently live.

Coverage: M02; CEH v5 domain 2; Reconnaissance sources.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q005

**Answer: D — Traceroute**

Traceroute infers path hops from probe responses, often using time-to-live or hop-limit expiry; missing replies do not prove a broken path.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Reverse proxy or CDN:** A reverse proxy or CDN can terminate public requests while hiding or separating the origin server.
- **B — Autonomous-system data:** AS and routing data identify network routing relationships or announced prefixes, not automatic testing permission.
- **C — Geolocation estimate:** IP geolocation estimates an address's location; VPNs, shared infrastructure and stale databases limit precision.

Coverage: M02; CEH v5 domain 2; Network footprint interpretation.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q006

**Answer: A — Reduce published metadata**

Remove unnecessary author, path and software details from public documents and pages.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Restrict zone transfers:** Allow DNS zone transfers only to the intended authorized secondary servers.
- **C — Inventory public dependencies:** Track public names, certificates and vendor links so abandoned or unexpected dependencies can be investigated.
- **D — Use approved public contact roles:** Publish necessary role-based contacts while avoiding unnecessary personal staff details.

Coverage: M02; CEH v5 domain 2; Exposure reduction.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q007

**Answer: C — Active reconnaissance**

Active reconnaissance sends requests or probes to the target or its infrastructure and requires appropriate scope.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Passive-source research:** Passive-source research uses already available third-party information without probing the target service directly.
- **B — Data minimization:** Data minimization limits collection to information actually needed for the authorized purpose.
- **D — Source corroboration:** Corroboration compares independent evidence because a single public record may be incomplete, stale or misleading.

Coverage: M02; CEH v5 domain 2; Passive and active reconnaissance.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q008

**Answer: A — AAAA record**

An AAAA record maps a name to an IPv6 address.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — A record:** An A record maps a name to an IPv4 address.
- **C — MX record:** An MX record identifies mail exchangers for a domain and includes preference values.
- **D — CNAME record:** A CNAME record makes one name an alias of another canonical name.

Coverage: M02; CEH v5 domain 2; DNS records.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q009

**Answer: B — SOA record**

An SOA record carries zone authority metadata including a serial number and timing values.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — PTR record:** A PTR record maps a reverse-DNS name toward a host name; it does not prove service ownership.
- **C — TXT record:** A TXT record carries text, including formats used by some email policies and ownership checks.
- **D — NS record:** An NS record identifies an authoritative name server for a DNS zone.

Coverage: M02; CEH v5 domain 2; Additional DNS data.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q010

**Answer: B — Certificate transparency logs**

Certificate transparency records publicly logged certificates and can reveal names, but not whether a service is currently live.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — RDAP registration data:** RDAP provides structured registration information; privacy redaction and registry differences limit what it reveals.
- **C — Search-engine indexing:** A search engine exposes its indexed view of content; cached results can lag behind current deployment.
- **D — Document metadata:** Document metadata can reveal properties such as authoring software or author fields, which may be stale or user-controlled.

Coverage: M02; CEH v5 domain 2; Reconnaissance sources.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q011

**Answer: D — Autonomous-system data**

AS and routing data identify network routing relationships or announced prefixes, not automatic testing permission.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Reverse proxy or CDN:** A reverse proxy or CDN can terminate public requests while hiding or separating the origin server.
- **B — Geolocation estimate:** IP geolocation estimates an address's location; VPNs, shared infrastructure and stale databases limit precision.
- **C — Traceroute:** Traceroute infers path hops from probe responses, often using time-to-live or hop-limit expiry; missing replies do not prove a broken path.

Coverage: M02; CEH v5 domain 2; Network footprint interpretation.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q012

**Answer: B — Restrict zone transfers**

Allow DNS zone transfers only to the intended authorized secondary servers.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Reduce published metadata:** Remove unnecessary author, path and software details from public documents and pages.
- **C — Inventory public dependencies:** Track public names, certificates and vendor links so abandoned or unexpected dependencies can be investigated.
- **D — Use approved public contact roles:** Publish necessary role-based contacts while avoiding unnecessary personal staff details.

Coverage: M02; CEH v5 domain 2; Exposure reduction.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q013

**Answer: B — Source corroboration**

Corroboration compares independent evidence because a single public record may be incomplete, stale or misleading.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Passive-source research:** Passive-source research uses already available third-party information without probing the target service directly.
- **C — Data minimization:** Data minimization limits collection to information actually needed for the authorized purpose.
- **D — Active reconnaissance:** Active reconnaissance sends requests or probes to the target or its infrastructure and requires appropriate scope.

Coverage: M02; CEH v5 domain 2; Passive and active reconnaissance.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q014

**Answer: A — MX record**

An MX record identifies mail exchangers for a domain and includes preference values.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — CNAME record:** A CNAME record makes one name an alias of another canonical name.
- **C — A record:** An A record maps a name to an IPv4 address.
- **D — AAAA record:** An AAAA record maps a name to an IPv6 address.

Coverage: M02; CEH v5 domain 2; DNS records.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q015

**Answer: D — PTR record**

A PTR record maps a reverse-DNS name toward a host name; it does not prove service ownership.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — SOA record:** An SOA record carries zone authority metadata including a serial number and timing values.
- **B — NS record:** An NS record identifies an authoritative name server for a DNS zone.
- **C — TXT record:** A TXT record carries text, including formats used by some email policies and ownership checks.

Coverage: M02; CEH v5 domain 2; Additional DNS data.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q016

**Answer: B — Search-engine indexing**

A search engine exposes its indexed view of content; cached results can lag behind current deployment.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — RDAP registration data:** RDAP provides structured registration information; privacy redaction and registry differences limit what it reveals.
- **C — Document metadata:** Document metadata can reveal properties such as authoring software or author fields, which may be stale or user-controlled.
- **D — Certificate transparency logs:** Certificate transparency records publicly logged certificates and can reveal names, but not whether a service is currently live.

Coverage: M02; CEH v5 domain 2; Reconnaissance sources.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q017

**Answer: D — Geolocation estimate**

IP geolocation estimates an address's location; VPNs, shared infrastructure and stale databases limit precision.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Traceroute:** Traceroute infers path hops from probe responses, often using time-to-live or hop-limit expiry; missing replies do not prove a broken path.
- **B — Autonomous-system data:** AS and routing data identify network routing relationships or announced prefixes, not automatic testing permission.
- **C — Reverse proxy or CDN:** A reverse proxy or CDN can terminate public requests while hiding or separating the origin server.

Coverage: M02; CEH v5 domain 2; Network footprint interpretation.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q018

**Answer: A — Use approved public contact roles**

Publish necessary role-based contacts while avoiding unnecessary personal staff details.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Restrict zone transfers:** Allow DNS zone transfers only to the intended authorized secondary servers.
- **C — Reduce published metadata:** Remove unnecessary author, path and software details from public documents and pages.
- **D — Inventory public dependencies:** Track public names, certificates and vendor links so abandoned or unexpected dependencies can be investigated.

Coverage: M02; CEH v5 domain 2; Exposure reduction.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q019

**Answer: C — Data minimization**

Data minimization limits collection to information actually needed for the authorized purpose.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Passive-source research:** Passive-source research uses already available third-party information without probing the target service directly.
- **B — Source corroboration:** Corroboration compares independent evidence because a single public record may be incomplete, stale or misleading.
- **D — Active reconnaissance:** Active reconnaissance sends requests or probes to the target or its infrastructure and requires appropriate scope.

Coverage: M02; CEH v5 domain 2; Passive and active reconnaissance.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q020

**Answer: C — CNAME record**

A CNAME record makes one name an alias of another canonical name.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — MX record:** An MX record identifies mail exchangers for a domain and includes preference values.
- **B — AAAA record:** An AAAA record maps a name to an IPv6 address.
- **D — A record:** An A record maps a name to an IPv4 address.

Coverage: M02; CEH v5 domain 2; DNS records.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q021

**Answer: D — TXT record**

A TXT record carries text, including formats used by some email policies and ownership checks.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — SOA record:** An SOA record carries zone authority metadata including a serial number and timing values.
- **B — NS record:** An NS record identifies an authoritative name server for a DNS zone.
- **C — PTR record:** A PTR record maps a reverse-DNS name toward a host name; it does not prove service ownership.

Coverage: M02; CEH v5 domain 2; Additional DNS data.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q022

**Answer: C — Document metadata**

Document metadata can reveal properties such as authoring software or author fields, which may be stale or user-controlled.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Search-engine indexing:** A search engine exposes its indexed view of content; cached results can lag behind current deployment.
- **B — RDAP registration data:** RDAP provides structured registration information; privacy redaction and registry differences limit what it reveals.
- **D — Certificate transparency logs:** Certificate transparency records publicly logged certificates and can reveal names, but not whether a service is currently live.

Coverage: M02; CEH v5 domain 2; Reconnaissance sources.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q023

**Answer: C — Reverse proxy or CDN**

A reverse proxy or CDN can terminate public requests while hiding or separating the origin server.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Geolocation estimate:** IP geolocation estimates an address's location; VPNs, shared infrastructure and stale databases limit precision.
- **B — Autonomous-system data:** AS and routing data identify network routing relationships or announced prefixes, not automatic testing permission.
- **D — Traceroute:** Traceroute infers path hops from probe responses, often using time-to-live or hop-limit expiry; missing replies do not prove a broken path.

Coverage: M02; CEH v5 domain 2; Network footprint interpretation.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q024

**Answer: B — Inventory public dependencies**

Track public names, certificates and vendor links so abandoned or unexpected dependencies can be investigated.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Restrict zone transfers:** Allow DNS zone transfers only to the intended authorized secondary servers.
- **C — Use approved public contact roles:** Publish necessary role-based contacts while avoiding unnecessary personal staff details.
- **D — Reduce published metadata:** Remove unnecessary author, path and software details from public documents and pages.

Coverage: M02; CEH v5 domain 2; Exposure reduction.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q025

**Answer: B — Active reconnaissance**

Active reconnaissance sends requests or probes to the target or its infrastructure and requires appropriate scope.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Passive-source research:** Passive-source research uses already available third-party information without probing the target service directly.
- **C — Source corroboration:** Corroboration compares independent evidence because a single public record may be incomplete, stale or misleading.
- **D — Data minimization:** Data minimization limits collection to information actually needed for the authorized purpose.

Coverage: M02; CEH v5 domain 2; Passive and active reconnaissance.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q026

**Answer: B — MX record**

An MX record identifies mail exchangers for a domain and includes preference values.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — AAAA record:** An AAAA record maps a name to an IPv6 address.
- **C — A record:** An A record maps a name to an IPv4 address.
- **D — CNAME record:** A CNAME record makes one name an alias of another canonical name.

Coverage: M02; CEH v5 domain 2; DNS records.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q027

**Answer: D — PTR record**

A PTR record maps a reverse-DNS name toward a host name; it does not prove service ownership.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — NS record:** An NS record identifies an authoritative name server for a DNS zone.
- **B — TXT record:** A TXT record carries text, including formats used by some email policies and ownership checks.
- **C — SOA record:** An SOA record carries zone authority metadata including a serial number and timing values.

Coverage: M02; CEH v5 domain 2; Additional DNS data.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q028

**Answer: A — Certificate transparency logs**

Certificate transparency records publicly logged certificates and can reveal names, but not whether a service is currently live.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Search-engine indexing:** A search engine exposes its indexed view of content; cached results can lag behind current deployment.
- **C — Document metadata:** Document metadata can reveal properties such as authoring software or author fields, which may be stale or user-controlled.
- **D — RDAP registration data:** RDAP provides structured registration information; privacy redaction and registry differences limit what it reveals.

Coverage: M02; CEH v5 domain 2; Reconnaissance sources.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q029

**Answer: A — Traceroute**

Traceroute infers path hops from probe responses, often using time-to-live or hop-limit expiry; missing replies do not prove a broken path.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Autonomous-system data:** AS and routing data identify network routing relationships or announced prefixes, not automatic testing permission.
- **C — Geolocation estimate:** IP geolocation estimates an address's location; VPNs, shared infrastructure and stale databases limit precision.
- **D — Reverse proxy or CDN:** A reverse proxy or CDN can terminate public requests while hiding or separating the origin server.

Coverage: M02; CEH v5 domain 2; Network footprint interpretation.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

### CEH26-M02-Q030

**Answer: A — Restrict zone transfers**

Allow DNS zone transfers only to the intended authorized secondary servers.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Reduce published metadata:** Remove unnecessary author, path and software details from public documents and pages.
- **C — Inventory public dependencies:** Track public names, certificates and vendor links so abandoned or unexpected dependencies can be investigated.
- **D — Use approved public contact roles:** Publish necessary role-based contacts while avoiding unnecessary personal staff details.

Coverage: M02; CEH v5 domain 2; Exposure reduction.
Technical references: [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) · [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) · [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)
