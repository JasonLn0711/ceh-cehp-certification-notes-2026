# M06 — System Hacking — instructor key v1.0.0

[Question form](m06.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M06-Q001

**Answer: C — Password spraying**

Password spraying tries a small number of likely passwords across many accounts, often to avoid per-account lockout.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Offline password guessing:** Offline guessing tests candidate passwords against acquired verifiers without sending each attempt to the login service.
- **B — Credential stuffing:** Credential stuffing reuses previously obtained username/password pairs against other services.
- **D — Brute-force login guessing:** Online brute-force guessing tries many password candidates through a live authentication interface.

Coverage: M06; CEH v5 domain 3; Credential attacks.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q002

**Answer: B — Vertical privilege escalation**

Vertical escalation gains permissions above the current privilege level on a system or application.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Lateral movement:** Lateral movement extends access to other systems or resources within an environment.
- **C — Horizontal access violation:** Horizontal access violates boundaries between subjects at a similar privilege level, such as two customer accounts.
- **D — Persistence:** Persistence provides a way to retain or regain access after interruptions such as restart or session loss.

Coverage: M06; CEH v5 domain 3; Privilege and movement.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q003

**Answer: A — Pass-the-hash**

Pass-the-hash uses an appropriate password hash as authentication material where the protocol and conditions permit it.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Kerberoasting:** Kerberoasting obtains suitable service-ticket material for offline guessing of a service account password.
- **C — Credential dumping:** Credential dumping extracts credential material from memory or stored system data; the material may take several forms.
- **D — Pass-the-ticket:** Pass-the-ticket reuses Kerberos ticket material rather than recovering the user's plaintext password.

Coverage: M06; CEH v5 domain 3; Windows credential concepts.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q004

**Answer: B — Unique salt**

A unique salt makes equal passwords produce different stored verifiers and reduces reuse of precomputed tables.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Pepper held separately:** A pepper is an additional secret kept apart from the password database; losing only the database need not expose it.
- **C — Multifactor authentication:** MFA requires additional authentication factors, reducing reliance on a password alone; it does not repair weak password storage.
- **D — Password key-derivation function:** A purpose-built password KDF makes each guess expensive through configurable computational or memory cost.

Coverage: M06; CEH v5 domain 3; Password storage.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q005

**Answer: A — Process injection**

Process injection runs code within another process, potentially changing the apparent execution context.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Alternate data stream:** On a supporting filesystem, an alternate data stream associates additional data with a file beyond its primary unnamed stream.
- **C — Log tampering:** Log tampering alters or removes audit records and can damage the ability to reconstruct activity.
- **D — Rootkit behavior:** A rootkit hides or manipulates system views to conceal activity, often requiring privileged access.

Coverage: M06; CEH v5 domain 3; Execution and hiding.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q006

**Answer: D — Patch the vulnerable component**

Patching removes a known software weakness when the relevant fix is installed and effective.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Centralized audit collection:** Forwarding logs to a protected separate system reduces dependence on a potentially altered endpoint's local records.
- **B — Restrict credential exposure:** Protect credential stores, reduce unnecessary privileged logons and limit reusable credential material.
- **C — Application control:** Application control restricts execution according to an approved policy rather than trusting any executable a user can write.

Coverage: M06; CEH v5 domain 3; Host defense.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q007

**Answer: D — Credential stuffing**

Credential stuffing reuses previously obtained username/password pairs against other services.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Brute-force login guessing:** Online brute-force guessing tries many password candidates through a live authentication interface.
- **B — Password spraying:** Password spraying tries a small number of likely passwords across many accounts, often to avoid per-account lockout.
- **C — Offline password guessing:** Offline guessing tests candidate passwords against acquired verifiers without sending each attempt to the login service.

Coverage: M06; CEH v5 domain 3; Credential attacks.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q008

**Answer: B — Horizontal access violation**

Horizontal access violates boundaries between subjects at a similar privilege level, such as two customer accounts.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Lateral movement:** Lateral movement extends access to other systems or resources within an environment.
- **C — Persistence:** Persistence provides a way to retain or regain access after interruptions such as restart or session loss.
- **D — Vertical privilege escalation:** Vertical escalation gains permissions above the current privilege level on a system or application.

Coverage: M06; CEH v5 domain 3; Privilege and movement.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q009

**Answer: A — Pass-the-ticket**

Pass-the-ticket reuses Kerberos ticket material rather than recovering the user's plaintext password.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Credential dumping:** Credential dumping extracts credential material from memory or stored system data; the material may take several forms.
- **C — Pass-the-hash:** Pass-the-hash uses an appropriate password hash as authentication material where the protocol and conditions permit it.
- **D — Kerberoasting:** Kerberoasting obtains suitable service-ticket material for offline guessing of a service account password.

Coverage: M06; CEH v5 domain 3; Windows credential concepts.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q010

**Answer: C — Password key-derivation function**

A purpose-built password KDF makes each guess expensive through configurable computational or memory cost.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Multifactor authentication:** MFA requires additional authentication factors, reducing reliance on a password alone; it does not repair weak password storage.
- **B — Pepper held separately:** A pepper is an additional secret kept apart from the password database; losing only the database need not expose it.
- **D — Unique salt:** A unique salt makes equal passwords produce different stored verifiers and reduces reuse of precomputed tables.

Coverage: M06; CEH v5 domain 3; Password storage.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q011

**Answer: B — Alternate data stream**

On a supporting filesystem, an alternate data stream associates additional data with a file beyond its primary unnamed stream.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Process injection:** Process injection runs code within another process, potentially changing the apparent execution context.
- **C — Log tampering:** Log tampering alters or removes audit records and can damage the ability to reconstruct activity.
- **D — Rootkit behavior:** A rootkit hides or manipulates system views to conceal activity, often requiring privileged access.

Coverage: M06; CEH v5 domain 3; Execution and hiding.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q012

**Answer: C — Restrict credential exposure**

Protect credential stores, reduce unnecessary privileged logons and limit reusable credential material.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Patch the vulnerable component:** Patching removes a known software weakness when the relevant fix is installed and effective.
- **B — Centralized audit collection:** Forwarding logs to a protected separate system reduces dependence on a potentially altered endpoint's local records.
- **D — Application control:** Application control restricts execution according to an approved policy rather than trusting any executable a user can write.

Coverage: M06; CEH v5 domain 3; Host defense.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q013

**Answer: A — Offline password guessing**

Offline guessing tests candidate passwords against acquired verifiers without sending each attempt to the login service.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Credential stuffing:** Credential stuffing reuses previously obtained username/password pairs against other services.
- **C — Brute-force login guessing:** Online brute-force guessing tries many password candidates through a live authentication interface.
- **D — Password spraying:** Password spraying tries a small number of likely passwords across many accounts, often to avoid per-account lockout.

Coverage: M06; CEH v5 domain 3; Credential attacks.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q014

**Answer: C — Lateral movement**

Lateral movement extends access to other systems or resources within an environment.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Persistence:** Persistence provides a way to retain or regain access after interruptions such as restart or session loss.
- **B — Horizontal access violation:** Horizontal access violates boundaries between subjects at a similar privilege level, such as two customer accounts.
- **D — Vertical privilege escalation:** Vertical escalation gains permissions above the current privilege level on a system or application.

Coverage: M06; CEH v5 domain 3; Privilege and movement.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q015

**Answer: A — Kerberoasting**

Kerberoasting obtains suitable service-ticket material for offline guessing of a service account password.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Pass-the-hash:** Pass-the-hash uses an appropriate password hash as authentication material where the protocol and conditions permit it.
- **C — Credential dumping:** Credential dumping extracts credential material from memory or stored system data; the material may take several forms.
- **D — Pass-the-ticket:** Pass-the-ticket reuses Kerberos ticket material rather than recovering the user's plaintext password.

Coverage: M06; CEH v5 domain 3; Windows credential concepts.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q016

**Answer: D — Pepper held separately**

A pepper is an additional secret kept apart from the password database; losing only the database need not expose it.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Multifactor authentication:** MFA requires additional authentication factors, reducing reliance on a password alone; it does not repair weak password storage.
- **B — Unique salt:** A unique salt makes equal passwords produce different stored verifiers and reduces reuse of precomputed tables.
- **C — Password key-derivation function:** A purpose-built password KDF makes each guess expensive through configurable computational or memory cost.

Coverage: M06; CEH v5 domain 3; Password storage.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q017

**Answer: D — Rootkit behavior**

A rootkit hides or manipulates system views to conceal activity, often requiring privileged access.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Log tampering:** Log tampering alters or removes audit records and can damage the ability to reconstruct activity.
- **B — Alternate data stream:** On a supporting filesystem, an alternate data stream associates additional data with a file beyond its primary unnamed stream.
- **C — Process injection:** Process injection runs code within another process, potentially changing the apparent execution context.

Coverage: M06; CEH v5 domain 3; Execution and hiding.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q018

**Answer: A — Application control**

Application control restricts execution according to an approved policy rather than trusting any executable a user can write.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Patch the vulnerable component:** Patching removes a known software weakness when the relevant fix is installed and effective.
- **C — Centralized audit collection:** Forwarding logs to a protected separate system reduces dependence on a potentially altered endpoint's local records.
- **D — Restrict credential exposure:** Protect credential stores, reduce unnecessary privileged logons and limit reusable credential material.

Coverage: M06; CEH v5 domain 3; Host defense.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q019

**Answer: B — Brute-force login guessing**

Online brute-force guessing tries many password candidates through a live authentication interface.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Password spraying:** Password spraying tries a small number of likely passwords across many accounts, often to avoid per-account lockout.
- **C — Offline password guessing:** Offline guessing tests candidate passwords against acquired verifiers without sending each attempt to the login service.
- **D — Credential stuffing:** Credential stuffing reuses previously obtained username/password pairs against other services.

Coverage: M06; CEH v5 domain 3; Credential attacks.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q020

**Answer: D — Persistence**

Persistence provides a way to retain or regain access after interruptions such as restart or session loss.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Vertical privilege escalation:** Vertical escalation gains permissions above the current privilege level on a system or application.
- **B — Lateral movement:** Lateral movement extends access to other systems or resources within an environment.
- **C — Horizontal access violation:** Horizontal access violates boundaries between subjects at a similar privilege level, such as two customer accounts.

Coverage: M06; CEH v5 domain 3; Privilege and movement.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q021

**Answer: B — Credential dumping**

Credential dumping extracts credential material from memory or stored system data; the material may take several forms.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Pass-the-hash:** Pass-the-hash uses an appropriate password hash as authentication material where the protocol and conditions permit it.
- **C — Pass-the-ticket:** Pass-the-ticket reuses Kerberos ticket material rather than recovering the user's plaintext password.
- **D — Kerberoasting:** Kerberoasting obtains suitable service-ticket material for offline guessing of a service account password.

Coverage: M06; CEH v5 domain 3; Windows credential concepts.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q022

**Answer: D — Multifactor authentication**

MFA requires additional authentication factors, reducing reliance on a password alone; it does not repair weak password storage.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Password key-derivation function:** A purpose-built password KDF makes each guess expensive through configurable computational or memory cost.
- **B — Unique salt:** A unique salt makes equal passwords produce different stored verifiers and reduces reuse of precomputed tables.
- **C — Pepper held separately:** A pepper is an additional secret kept apart from the password database; losing only the database need not expose it.

Coverage: M06; CEH v5 domain 3; Password storage.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q023

**Answer: D — Log tampering**

Log tampering alters or removes audit records and can damage the ability to reconstruct activity.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Rootkit behavior:** A rootkit hides or manipulates system views to conceal activity, often requiring privileged access.
- **B — Process injection:** Process injection runs code within another process, potentially changing the apparent execution context.
- **C — Alternate data stream:** On a supporting filesystem, an alternate data stream associates additional data with a file beyond its primary unnamed stream.

Coverage: M06; CEH v5 domain 3; Execution and hiding.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q024

**Answer: B — Centralized audit collection**

Forwarding logs to a protected separate system reduces dependence on a potentially altered endpoint's local records.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Application control:** Application control restricts execution according to an approved policy rather than trusting any executable a user can write.
- **C — Restrict credential exposure:** Protect credential stores, reduce unnecessary privileged logons and limit reusable credential material.
- **D — Patch the vulnerable component:** Patching removes a known software weakness when the relevant fix is installed and effective.

Coverage: M06; CEH v5 domain 3; Host defense.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q025

**Answer: D — Offline password guessing**

Offline guessing tests candidate passwords against acquired verifiers without sending each attempt to the login service.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Credential stuffing:** Credential stuffing reuses previously obtained username/password pairs against other services.
- **B — Brute-force login guessing:** Online brute-force guessing tries many password candidates through a live authentication interface.
- **C — Password spraying:** Password spraying tries a small number of likely passwords across many accounts, often to avoid per-account lockout.

Coverage: M06; CEH v5 domain 3; Credential attacks.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q026

**Answer: C — Vertical privilege escalation**

Vertical escalation gains permissions above the current privilege level on a system or application.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Lateral movement:** Lateral movement extends access to other systems or resources within an environment.
- **B — Horizontal access violation:** Horizontal access violates boundaries between subjects at a similar privilege level, such as two customer accounts.
- **D — Persistence:** Persistence provides a way to retain or regain access after interruptions such as restart or session loss.

Coverage: M06; CEH v5 domain 3; Privilege and movement.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q027

**Answer: A — Kerberoasting**

Kerberoasting obtains suitable service-ticket material for offline guessing of a service account password.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Pass-the-ticket:** Pass-the-ticket reuses Kerberos ticket material rather than recovering the user's plaintext password.
- **C — Credential dumping:** Credential dumping extracts credential material from memory or stored system data; the material may take several forms.
- **D — Pass-the-hash:** Pass-the-hash uses an appropriate password hash as authentication material where the protocol and conditions permit it.

Coverage: M06; CEH v5 domain 3; Windows credential concepts.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q028

**Answer: C — Password key-derivation function**

A purpose-built password KDF makes each guess expensive through configurable computational or memory cost.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Pepper held separately:** A pepper is an additional secret kept apart from the password database; losing only the database need not expose it.
- **B — Unique salt:** A unique salt makes equal passwords produce different stored verifiers and reduces reuse of precomputed tables.
- **D — Multifactor authentication:** MFA requires additional authentication factors, reducing reliance on a password alone; it does not repair weak password storage.

Coverage: M06; CEH v5 domain 3; Password storage.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q029

**Answer: A — Process injection**

Process injection runs code within another process, potentially changing the apparent execution context.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Log tampering:** Log tampering alters or removes audit records and can damage the ability to reconstruct activity.
- **C — Alternate data stream:** On a supporting filesystem, an alternate data stream associates additional data with a file beyond its primary unnamed stream.
- **D — Rootkit behavior:** A rootkit hides or manipulates system views to conceal activity, often requiring privileged access.

Coverage: M06; CEH v5 domain 3; Execution and hiding.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### CEH26-M06-Q030

**Answer: C — Restrict credential exposure**

Protect credential stores, reduce unnecessary privileged logons and limit reusable credential material.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Centralized audit collection:** Forwarding logs to a protected separate system reduces dependence on a potentially altered endpoint's local records.
- **B — Application control:** Application control restricts execution according to an approved policy rather than trusting any executable a user can write.
- **D — Patch the vulnerable component:** Patching removes a known software weakness when the relevant fix is installed and effective.

Coverage: M06; CEH v5 domain 3; Host defense.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
