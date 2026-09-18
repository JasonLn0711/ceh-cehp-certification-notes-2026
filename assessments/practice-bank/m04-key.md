# M04 — Enumeration — instructor key v1.0.0

[Question form](m04.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M04-Q001

**Answer: A — LDAP**

LDAP queries directory objects and attributes, with access constrained by authentication and directory permissions.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — SMB:** SMB provides file-sharing and related services, with access governed by authentication, share and file permissions.
- **C — SNMP:** SNMP exposes management data through defined objects; security depends on version and access configuration.
- **D — SMTP:** SMTP transfers email; some server commands or responses can reveal recipient information when enabled.

Coverage: M04; CEH v5 domain 2; Enumeration protocols.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q002

**Answer: A — SNMPv1/v2c community model**

SNMPv1 and v2c use community strings and do not provide the cryptographic protections offered by SNMPv3 USM.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Management-plane restriction:** Restricting management traffic to approved sources reduces who can reach the service.
- **C — Read-only management access:** Read-only permissions limit queries to reading permitted management objects rather than modifying them.
- **D — SNMPv3 authPriv:** The authPriv security level adds message authentication and privacy when correctly configured.

Coverage: M04; CEH v5 domain 2; SNMP security.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q003

**Answer: D — DNS zone transfer**

A zone transfer can disclose an entire zone when the server permits the requesting client to obtain it.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — NetBIOS name information:** NetBIOS name data can expose host or service naming information but does not prove the underlying system is compromised.
- **B — NFS export enumeration:** NFS export information identifies shared filesystem paths and allowed clients; advertised access still needs scoped verification.
- **C — RPC service discovery:** RPC service discovery reveals registered remote procedure services or their mapped endpoints.

Coverage: M04; CEH v5 domain 2; Service-specific enumeration.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q004

**Answer: A — Anonymous information exposure**

Anonymous exposure occurs when useful information can be read without supplying an authenticated identity.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Excessive read permission:** Excessive read access grants an authenticated account more information than its role requires.
- **C — Name-only evidence:** A discovered name is a lead; it does not establish that the account is active, accessible or authorized for testing.
- **D — Excessive write permission:** Excessive write access lets an account alter resources outside its legitimate responsibilities.

Coverage: M04; CEH v5 domain 2; Identity and access findings.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q005

**Answer: B — Service identity corroboration**

Confirm service identity with protocol behavior or trusted host information instead of relying only on a conventional port number.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Scope-preserving continuation:** Continue only within authorized targets and methods; newly discovered endpoints do not automatically expand scope.
- **C — Sensitive-output protection:** Protect enumeration output because account names, paths and configuration details may aid later misuse.
- **D — Effective permission testing:** Check the actual allowed operation under the specific identity; listed configuration alone may not show the effective result.

Coverage: M04; CEH v5 domain 2; Enumeration result quality.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q006

**Answer: C — Disable unnecessary anonymous queries**

Reduce unauthenticated information disclosure while preserving required service behavior.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Remove unnecessary legacy services:** Retire unused legacy discovery or sharing services to reduce avoidable exposure.
- **B — Monitor query patterns:** Log and review unusual enumeration volume or sensitive-object queries within appropriate operational limits.
- **D — Apply least-privilege access:** Grant directory, share and management access only to the identities and data needed for each role.

Coverage: M04; CEH v5 domain 2; Enumeration countermeasures.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q007

**Answer: B — SNMP**

SNMP exposes management data through defined objects; security depends on version and access configuration.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — SMB:** SMB provides file-sharing and related services, with access governed by authentication, share and file permissions.
- **C — LDAP:** LDAP queries directory objects and attributes, with access constrained by authentication and directory permissions.
- **D — SMTP:** SMTP transfers email; some server commands or responses can reveal recipient information when enabled.

Coverage: M04; CEH v5 domain 2; Enumeration protocols.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q008

**Answer: C — SNMPv3 authPriv**

The authPriv security level adds message authentication and privacy when correctly configured.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Management-plane restriction:** Restricting management traffic to approved sources reduces who can reach the service.
- **B — Read-only management access:** Read-only permissions limit queries to reading permitted management objects rather than modifying them.
- **D — SNMPv1/v2c community model:** SNMPv1 and v2c use community strings and do not provide the cryptographic protections offered by SNMPv3 USM.

Coverage: M04; CEH v5 domain 2; SNMP security.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q009

**Answer: D — NFS export enumeration**

NFS export information identifies shared filesystem paths and allowed clients; advertised access still needs scoped verification.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — RPC service discovery:** RPC service discovery reveals registered remote procedure services or their mapped endpoints.
- **B — NetBIOS name information:** NetBIOS name data can expose host or service naming information but does not prove the underlying system is compromised.
- **C — DNS zone transfer:** A zone transfer can disclose an entire zone when the server permits the requesting client to obtain it.

Coverage: M04; CEH v5 domain 2; Service-specific enumeration.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q010

**Answer: C — Excessive read permission**

Excessive read access grants an authenticated account more information than its role requires.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Anonymous information exposure:** Anonymous exposure occurs when useful information can be read without supplying an authenticated identity.
- **B — Excessive write permission:** Excessive write access lets an account alter resources outside its legitimate responsibilities.
- **D — Name-only evidence:** A discovered name is a lead; it does not establish that the account is active, accessible or authorized for testing.

Coverage: M04; CEH v5 domain 2; Identity and access findings.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q011

**Answer: C — Effective permission testing**

Check the actual allowed operation under the specific identity; listed configuration alone may not show the effective result.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Scope-preserving continuation:** Continue only within authorized targets and methods; newly discovered endpoints do not automatically expand scope.
- **B — Sensitive-output protection:** Protect enumeration output because account names, paths and configuration details may aid later misuse.
- **D — Service identity corroboration:** Confirm service identity with protocol behavior or trusted host information instead of relying only on a conventional port number.

Coverage: M04; CEH v5 domain 2; Enumeration result quality.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q012

**Answer: B — Apply least-privilege access**

Grant directory, share and management access only to the identities and data needed for each role.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Remove unnecessary legacy services:** Retire unused legacy discovery or sharing services to reduce avoidable exposure.
- **C — Disable unnecessary anonymous queries:** Reduce unauthenticated information disclosure while preserving required service behavior.
- **D — Monitor query patterns:** Log and review unusual enumeration volume or sensitive-object queries within appropriate operational limits.

Coverage: M04; CEH v5 domain 2; Enumeration countermeasures.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q013

**Answer: B — SMB**

SMB provides file-sharing and related services, with access governed by authentication, share and file permissions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — SMTP:** SMTP transfers email; some server commands or responses can reveal recipient information when enabled.
- **C — SNMP:** SNMP exposes management data through defined objects; security depends on version and access configuration.
- **D — LDAP:** LDAP queries directory objects and attributes, with access constrained by authentication and directory permissions.

Coverage: M04; CEH v5 domain 2; Enumeration protocols.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q014

**Answer: C — Read-only management access**

Read-only permissions limit queries to reading permitted management objects rather than modifying them.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — SNMPv3 authPriv:** The authPriv security level adds message authentication and privacy when correctly configured.
- **B — SNMPv1/v2c community model:** SNMPv1 and v2c use community strings and do not provide the cryptographic protections offered by SNMPv3 USM.
- **D — Management-plane restriction:** Restricting management traffic to approved sources reduces who can reach the service.

Coverage: M04; CEH v5 domain 2; SNMP security.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q015

**Answer: A — RPC service discovery**

RPC service discovery reveals registered remote procedure services or their mapped endpoints.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — NetBIOS name information:** NetBIOS name data can expose host or service naming information but does not prove the underlying system is compromised.
- **C — NFS export enumeration:** NFS export information identifies shared filesystem paths and allowed clients; advertised access still needs scoped verification.
- **D — DNS zone transfer:** A zone transfer can disclose an entire zone when the server permits the requesting client to obtain it.

Coverage: M04; CEH v5 domain 2; Service-specific enumeration.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q016

**Answer: A — Excessive write permission**

Excessive write access lets an account alter resources outside its legitimate responsibilities.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Excessive read permission:** Excessive read access grants an authenticated account more information than its role requires.
- **C — Anonymous information exposure:** Anonymous exposure occurs when useful information can be read without supplying an authenticated identity.
- **D — Name-only evidence:** A discovered name is a lead; it does not establish that the account is active, accessible or authorized for testing.

Coverage: M04; CEH v5 domain 2; Identity and access findings.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q017

**Answer: D — Scope-preserving continuation**

Continue only within authorized targets and methods; newly discovered endpoints do not automatically expand scope.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Effective permission testing:** Check the actual allowed operation under the specific identity; listed configuration alone may not show the effective result.
- **B — Sensitive-output protection:** Protect enumeration output because account names, paths and configuration details may aid later misuse.
- **C — Service identity corroboration:** Confirm service identity with protocol behavior or trusted host information instead of relying only on a conventional port number.

Coverage: M04; CEH v5 domain 2; Enumeration result quality.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q018

**Answer: D — Remove unnecessary legacy services**

Retire unused legacy discovery or sharing services to reduce avoidable exposure.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Apply least-privilege access:** Grant directory, share and management access only to the identities and data needed for each role.
- **B — Monitor query patterns:** Log and review unusual enumeration volume or sensitive-object queries within appropriate operational limits.
- **C — Disable unnecessary anonymous queries:** Reduce unauthenticated information disclosure while preserving required service behavior.

Coverage: M04; CEH v5 domain 2; Enumeration countermeasures.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q019

**Answer: B — SMTP**

SMTP transfers email; some server commands or responses can reveal recipient information when enabled.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — LDAP:** LDAP queries directory objects and attributes, with access constrained by authentication and directory permissions.
- **C — SMB:** SMB provides file-sharing and related services, with access governed by authentication, share and file permissions.
- **D — SNMP:** SNMP exposes management data through defined objects; security depends on version and access configuration.

Coverage: M04; CEH v5 domain 2; Enumeration protocols.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q020

**Answer: A — Management-plane restriction**

Restricting management traffic to approved sources reduces who can reach the service.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Read-only management access:** Read-only permissions limit queries to reading permitted management objects rather than modifying them.
- **C — SNMPv1/v2c community model:** SNMPv1 and v2c use community strings and do not provide the cryptographic protections offered by SNMPv3 USM.
- **D — SNMPv3 authPriv:** The authPriv security level adds message authentication and privacy when correctly configured.

Coverage: M04; CEH v5 domain 2; SNMP security.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q021

**Answer: A — NetBIOS name information**

NetBIOS name data can expose host or service naming information but does not prove the underlying system is compromised.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — RPC service discovery:** RPC service discovery reveals registered remote procedure services or their mapped endpoints.
- **C — DNS zone transfer:** A zone transfer can disclose an entire zone when the server permits the requesting client to obtain it.
- **D — NFS export enumeration:** NFS export information identifies shared filesystem paths and allowed clients; advertised access still needs scoped verification.

Coverage: M04; CEH v5 domain 2; Service-specific enumeration.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q022

**Answer: C — Name-only evidence**

A discovered name is a lead; it does not establish that the account is active, accessible or authorized for testing.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Anonymous information exposure:** Anonymous exposure occurs when useful information can be read without supplying an authenticated identity.
- **B — Excessive write permission:** Excessive write access lets an account alter resources outside its legitimate responsibilities.
- **D — Excessive read permission:** Excessive read access grants an authenticated account more information than its role requires.

Coverage: M04; CEH v5 domain 2; Identity and access findings.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q023

**Answer: A — Sensitive-output protection**

Protect enumeration output because account names, paths and configuration details may aid later misuse.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Service identity corroboration:** Confirm service identity with protocol behavior or trusted host information instead of relying only on a conventional port number.
- **C — Effective permission testing:** Check the actual allowed operation under the specific identity; listed configuration alone may not show the effective result.
- **D — Scope-preserving continuation:** Continue only within authorized targets and methods; newly discovered endpoints do not automatically expand scope.

Coverage: M04; CEH v5 domain 2; Enumeration result quality.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q024

**Answer: B — Monitor query patterns**

Log and review unusual enumeration volume or sensitive-object queries within appropriate operational limits.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Remove unnecessary legacy services:** Retire unused legacy discovery or sharing services to reduce avoidable exposure.
- **C — Apply least-privilege access:** Grant directory, share and management access only to the identities and data needed for each role.
- **D — Disable unnecessary anonymous queries:** Reduce unauthenticated information disclosure while preserving required service behavior.

Coverage: M04; CEH v5 domain 2; Enumeration countermeasures.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q025

**Answer: D — LDAP**

LDAP queries directory objects and attributes, with access constrained by authentication and directory permissions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — SMTP:** SMTP transfers email; some server commands or responses can reveal recipient information when enabled.
- **B — SNMP:** SNMP exposes management data through defined objects; security depends on version and access configuration.
- **C — SMB:** SMB provides file-sharing and related services, with access governed by authentication, share and file permissions.

Coverage: M04; CEH v5 domain 2; Enumeration protocols.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q026

**Answer: C — SNMPv3 authPriv**

The authPriv security level adds message authentication and privacy when correctly configured.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Management-plane restriction:** Restricting management traffic to approved sources reduces who can reach the service.
- **B — Read-only management access:** Read-only permissions limit queries to reading permitted management objects rather than modifying them.
- **D — SNMPv1/v2c community model:** SNMPv1 and v2c use community strings and do not provide the cryptographic protections offered by SNMPv3 USM.

Coverage: M04; CEH v5 domain 2; SNMP security.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q027

**Answer: D — NFS export enumeration**

NFS export information identifies shared filesystem paths and allowed clients; advertised access still needs scoped verification.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — DNS zone transfer:** A zone transfer can disclose an entire zone when the server permits the requesting client to obtain it.
- **B — RPC service discovery:** RPC service discovery reveals registered remote procedure services or their mapped endpoints.
- **C — NetBIOS name information:** NetBIOS name data can expose host or service naming information but does not prove the underlying system is compromised.

Coverage: M04; CEH v5 domain 2; Service-specific enumeration.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q028

**Answer: B — Excessive read permission**

Excessive read access grants an authenticated account more information than its role requires.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Anonymous information exposure:** Anonymous exposure occurs when useful information can be read without supplying an authenticated identity.
- **C — Excessive write permission:** Excessive write access lets an account alter resources outside its legitimate responsibilities.
- **D — Name-only evidence:** A discovered name is a lead; it does not establish that the account is active, accessible or authorized for testing.

Coverage: M04; CEH v5 domain 2; Identity and access findings.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q029

**Answer: B — Effective permission testing**

Check the actual allowed operation under the specific identity; listed configuration alone may not show the effective result.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Sensitive-output protection:** Protect enumeration output because account names, paths and configuration details may aid later misuse.
- **C — Service identity corroboration:** Confirm service identity with protocol behavior or trusted host information instead of relying only on a conventional port number.
- **D — Scope-preserving continuation:** Continue only within authorized targets and methods; newly discovered endpoints do not automatically expand scope.

Coverage: M04; CEH v5 domain 2; Enumeration result quality.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

### CEH26-M04-Q030

**Answer: D — Apply least-privilege access**

Grant directory, share and management access only to the identities and data needed for each role.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Monitor query patterns:** Log and review unusual enumeration volume or sensitive-object queries within appropriate operational limits.
- **B — Disable unnecessary anonymous queries:** Reduce unauthenticated information disclosure while preserving required service behavior.
- **C — Remove unnecessary legacy services:** Retire unused legacy discovery or sharing services to reduce avoidable exposure.

Coverage: M04; CEH v5 domain 2; Enumeration countermeasures.
Technical references: [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511) · [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411) · [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)
