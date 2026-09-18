# M17 — Mobile Platforms — instructor key v1.0.0

[Question form](m17.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M17-Q001

**Answer: A — Application sandbox**

A sandbox separates application resources and constrains access, though flaws or granted interfaces can cross that boundary.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Trusted update chain:** A trusted update chain authenticates software updates and relies on supported, correctly deployed versions.
- **C — Permission model:** Permissions control access to protected capabilities or data; an app should request only what its function needs.
- **D — Rooting or jailbreaking:** Rooting or jailbreaking changes platform restrictions and can weaken assumptions made by applications and management controls.

Coverage: M17; CEH v5 domain 7; Mobile platform boundaries.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q002

**Answer: C — Sensitive-data minimization**

Avoid storing secrets or personal data that the mobile workflow does not actually need.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Local encryption boundary:** Encryption protects stored data only within its key and threat model; an unlocked compromised runtime may still access plaintext.
- **B — Platform-protected key storage:** Use appropriate platform-backed key facilities rather than hardcoding private keys or keeping them as ordinary files.
- **D — Backup and log review:** Backups and diagnostic logs can expose data even when the main app screen hides it.

Coverage: M17; CEH v5 domain 7; Mobile data storage.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q003

**Answer: A — TLS trust validation**

Validate peer identity and trust for protected connections instead of accepting any certificate.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Cleartext transport exposure:** Unprotected transport can expose application data to observers or modification on the path.
- **C — Backend authorization:** The server must validate subject and object permissions regardless of checks performed by the mobile client.
- **D — Certificate pinning tradeoff:** Pinning constrains acceptable credentials but needs a careful rotation and recovery design; it is not a replacement for sound TLS handling.

Coverage: M17; CEH v5 domain 7; Mobile network security.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q004

**Answer: A — Unsafe deep-link handling**

Deep links can deliver untrusted parameters or navigation requests and must not bypass authentication or validation.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Clipboard exposure:** Sensitive content placed on a clipboard may be available beyond the intended app, depending on platform behavior and context.
- **C — Exposed interprocess component:** An exported component can receive calls from other applications; intended caller permissions and input handling matter.
- **D — Unsafe WebView boundary:** A WebView that exposes privileged bridges or loads untrusted content can cross from web input into app capabilities.

Coverage: M17; CEH v5 domain 7; Application interaction.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q005

**Answer: B — Sideloaded malicious app**

An application obtained outside the intended trusted distribution path may carry unreviewed harmful behavior; provenance still needs assessment.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Malicious profile or management enrollment:** An untrusted configuration profile or management relationship can change device settings and trust boundaries.
- **C — SIM-swap risk:** Transfer of a phone number can expose workflows relying on that number for recovery or authentication.
- **D — Lost-device exposure:** A lost device creates risks depending on its lock state, stored data, keys and remote management controls.

Coverage: M17; CEH v5 domain 7; Mobile threat scenarios.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q006

**Answer: D — MDM policy**

Mobile device management enforces supported device policies and configuration, subject to enrollment and platform capabilities.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Conditional access:** Access decisions can consider managed-device posture and other signals, while accounting for signal reliability.
- **B — Remote response actions:** Remote lock, wipe or session revocation can reduce incident exposure, but depend on reachability, scope and platform behavior.
- **C — Work-profile separation:** Separate managed work data and applications from personal contexts where the platform supports that boundary.

Coverage: M17; CEH v5 domain 7; Enterprise mobile controls.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q007

**Answer: D — Permission model**

Permissions control access to protected capabilities or data; an app should request only what its function needs.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Trusted update chain:** A trusted update chain authenticates software updates and relies on supported, correctly deployed versions.
- **B — Application sandbox:** A sandbox separates application resources and constrains access, though flaws or granted interfaces can cross that boundary.
- **C — Rooting or jailbreaking:** Rooting or jailbreaking changes platform restrictions and can weaken assumptions made by applications and management controls.

Coverage: M17; CEH v5 domain 7; Mobile platform boundaries.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q008

**Answer: B — Platform-protected key storage**

Use appropriate platform-backed key facilities rather than hardcoding private keys or keeping them as ordinary files.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Sensitive-data minimization:** Avoid storing secrets or personal data that the mobile workflow does not actually need.
- **C — Local encryption boundary:** Encryption protects stored data only within its key and threat model; an unlocked compromised runtime may still access plaintext.
- **D — Backup and log review:** Backups and diagnostic logs can expose data even when the main app screen hides it.

Coverage: M17; CEH v5 domain 7; Mobile data storage.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q009

**Answer: B — Cleartext transport exposure**

Unprotected transport can expose application data to observers or modification on the path.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Certificate pinning tradeoff:** Pinning constrains acceptable credentials but needs a careful rotation and recovery design; it is not a replacement for sound TLS handling.
- **C — TLS trust validation:** Validate peer identity and trust for protected connections instead of accepting any certificate.
- **D — Backend authorization:** The server must validate subject and object permissions regardless of checks performed by the mobile client.

Coverage: M17; CEH v5 domain 7; Mobile network security.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q010

**Answer: C — Exposed interprocess component**

An exported component can receive calls from other applications; intended caller permissions and input handling matter.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Unsafe deep-link handling:** Deep links can deliver untrusted parameters or navigation requests and must not bypass authentication or validation.
- **B — Clipboard exposure:** Sensitive content placed on a clipboard may be available beyond the intended app, depending on platform behavior and context.
- **D — Unsafe WebView boundary:** A WebView that exposes privileged bridges or loads untrusted content can cross from web input into app capabilities.

Coverage: M17; CEH v5 domain 7; Application interaction.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q011

**Answer: C — SIM-swap risk**

Transfer of a phone number can expose workflows relying on that number for recovery or authentication.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Lost-device exposure:** A lost device creates risks depending on its lock state, stored data, keys and remote management controls.
- **B — Sideloaded malicious app:** An application obtained outside the intended trusted distribution path may carry unreviewed harmful behavior; provenance still needs assessment.
- **D — Malicious profile or management enrollment:** An untrusted configuration profile or management relationship can change device settings and trust boundaries.

Coverage: M17; CEH v5 domain 7; Mobile threat scenarios.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q012

**Answer: B — Work-profile separation**

Separate managed work data and applications from personal contexts where the platform supports that boundary.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Conditional access:** Access decisions can consider managed-device posture and other signals, while accounting for signal reliability.
- **C — Remote response actions:** Remote lock, wipe or session revocation can reduce incident exposure, but depend on reachability, scope and platform behavior.
- **D — MDM policy:** Mobile device management enforces supported device policies and configuration, subject to enrollment and platform capabilities.

Coverage: M17; CEH v5 domain 7; Enterprise mobile controls.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q013

**Answer: A — Rooting or jailbreaking**

Rooting or jailbreaking changes platform restrictions and can weaken assumptions made by applications and management controls.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Trusted update chain:** A trusted update chain authenticates software updates and relies on supported, correctly deployed versions.
- **C — Permission model:** Permissions control access to protected capabilities or data; an app should request only what its function needs.
- **D — Application sandbox:** A sandbox separates application resources and constrains access, though flaws or granted interfaces can cross that boundary.

Coverage: M17; CEH v5 domain 7; Mobile platform boundaries.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q014

**Answer: A — Backup and log review**

Backups and diagnostic logs can expose data even when the main app screen hides it.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Platform-protected key storage:** Use appropriate platform-backed key facilities rather than hardcoding private keys or keeping them as ordinary files.
- **C — Sensitive-data minimization:** Avoid storing secrets or personal data that the mobile workflow does not actually need.
- **D — Local encryption boundary:** Encryption protects stored data only within its key and threat model; an unlocked compromised runtime may still access plaintext.

Coverage: M17; CEH v5 domain 7; Mobile data storage.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q015

**Answer: B — Backend authorization**

The server must validate subject and object permissions regardless of checks performed by the mobile client.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Cleartext transport exposure:** Unprotected transport can expose application data to observers or modification on the path.
- **C — TLS trust validation:** Validate peer identity and trust for protected connections instead of accepting any certificate.
- **D — Certificate pinning tradeoff:** Pinning constrains acceptable credentials but needs a careful rotation and recovery design; it is not a replacement for sound TLS handling.

Coverage: M17; CEH v5 domain 7; Mobile network security.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q016

**Answer: D — Unsafe WebView boundary**

A WebView that exposes privileged bridges or loads untrusted content can cross from web input into app capabilities.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Exposed interprocess component:** An exported component can receive calls from other applications; intended caller permissions and input handling matter.
- **B — Unsafe deep-link handling:** Deep links can deliver untrusted parameters or navigation requests and must not bypass authentication or validation.
- **C — Clipboard exposure:** Sensitive content placed on a clipboard may be available beyond the intended app, depending on platform behavior and context.

Coverage: M17; CEH v5 domain 7; Application interaction.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q017

**Answer: C — Lost-device exposure**

A lost device creates risks depending on its lock state, stored data, keys and remote management controls.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Sideloaded malicious app:** An application obtained outside the intended trusted distribution path may carry unreviewed harmful behavior; provenance still needs assessment.
- **B — Malicious profile or management enrollment:** An untrusted configuration profile or management relationship can change device settings and trust boundaries.
- **D — SIM-swap risk:** Transfer of a phone number can expose workflows relying on that number for recovery or authentication.

Coverage: M17; CEH v5 domain 7; Mobile threat scenarios.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q018

**Answer: D — Conditional access**

Access decisions can consider managed-device posture and other signals, while accounting for signal reliability.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Work-profile separation:** Separate managed work data and applications from personal contexts where the platform supports that boundary.
- **B — MDM policy:** Mobile device management enforces supported device policies and configuration, subject to enrollment and platform capabilities.
- **C — Remote response actions:** Remote lock, wipe or session revocation can reduce incident exposure, but depend on reachability, scope and platform behavior.

Coverage: M17; CEH v5 domain 7; Enterprise mobile controls.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q019

**Answer: B — Trusted update chain**

A trusted update chain authenticates software updates and relies on supported, correctly deployed versions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Permission model:** Permissions control access to protected capabilities or data; an app should request only what its function needs.
- **C — Rooting or jailbreaking:** Rooting or jailbreaking changes platform restrictions and can weaken assumptions made by applications and management controls.
- **D — Application sandbox:** A sandbox separates application resources and constrains access, though flaws or granted interfaces can cross that boundary.

Coverage: M17; CEH v5 domain 7; Mobile platform boundaries.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q020

**Answer: D — Local encryption boundary**

Encryption protects stored data only within its key and threat model; an unlocked compromised runtime may still access plaintext.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Sensitive-data minimization:** Avoid storing secrets or personal data that the mobile workflow does not actually need.
- **B — Backup and log review:** Backups and diagnostic logs can expose data even when the main app screen hides it.
- **C — Platform-protected key storage:** Use appropriate platform-backed key facilities rather than hardcoding private keys or keeping them as ordinary files.

Coverage: M17; CEH v5 domain 7; Mobile data storage.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q021

**Answer: A — Certificate pinning tradeoff**

Pinning constrains acceptable credentials but needs a careful rotation and recovery design; it is not a replacement for sound TLS handling.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Backend authorization:** The server must validate subject and object permissions regardless of checks performed by the mobile client.
- **C — Cleartext transport exposure:** Unprotected transport can expose application data to observers or modification on the path.
- **D — TLS trust validation:** Validate peer identity and trust for protected connections instead of accepting any certificate.

Coverage: M17; CEH v5 domain 7; Mobile network security.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q022

**Answer: B — Clipboard exposure**

Sensitive content placed on a clipboard may be available beyond the intended app, depending on platform behavior and context.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Unsafe deep-link handling:** Deep links can deliver untrusted parameters or navigation requests and must not bypass authentication or validation.
- **C — Unsafe WebView boundary:** A WebView that exposes privileged bridges or loads untrusted content can cross from web input into app capabilities.
- **D — Exposed interprocess component:** An exported component can receive calls from other applications; intended caller permissions and input handling matter.

Coverage: M17; CEH v5 domain 7; Application interaction.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q023

**Answer: D — Malicious profile or management enrollment**

An untrusted configuration profile or management relationship can change device settings and trust boundaries.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — SIM-swap risk:** Transfer of a phone number can expose workflows relying on that number for recovery or authentication.
- **B — Lost-device exposure:** A lost device creates risks depending on its lock state, stored data, keys and remote management controls.
- **C — Sideloaded malicious app:** An application obtained outside the intended trusted distribution path may carry unreviewed harmful behavior; provenance still needs assessment.

Coverage: M17; CEH v5 domain 7; Mobile threat scenarios.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q024

**Answer: C — Remote response actions**

Remote lock, wipe or session revocation can reduce incident exposure, but depend on reachability, scope and platform behavior.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — MDM policy:** Mobile device management enforces supported device policies and configuration, subject to enrollment and platform capabilities.
- **B — Conditional access:** Access decisions can consider managed-device posture and other signals, while accounting for signal reliability.
- **D — Work-profile separation:** Separate managed work data and applications from personal contexts where the platform supports that boundary.

Coverage: M17; CEH v5 domain 7; Enterprise mobile controls.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q025

**Answer: C — Permission model**

Permissions control access to protected capabilities or data; an app should request only what its function needs.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Trusted update chain:** A trusted update chain authenticates software updates and relies on supported, correctly deployed versions.
- **B — Application sandbox:** A sandbox separates application resources and constrains access, though flaws or granted interfaces can cross that boundary.
- **D — Rooting or jailbreaking:** Rooting or jailbreaking changes platform restrictions and can weaken assumptions made by applications and management controls.

Coverage: M17; CEH v5 domain 7; Mobile platform boundaries.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q026

**Answer: C — Backup and log review**

Backups and diagnostic logs can expose data even when the main app screen hides it.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Sensitive-data minimization:** Avoid storing secrets or personal data that the mobile workflow does not actually need.
- **B — Platform-protected key storage:** Use appropriate platform-backed key facilities rather than hardcoding private keys or keeping them as ordinary files.
- **D — Local encryption boundary:** Encryption protects stored data only within its key and threat model; an unlocked compromised runtime may still access plaintext.

Coverage: M17; CEH v5 domain 7; Mobile data storage.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q027

**Answer: D — TLS trust validation**

Validate peer identity and trust for protected connections instead of accepting any certificate.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Certificate pinning tradeoff:** Pinning constrains acceptable credentials but needs a careful rotation and recovery design; it is not a replacement for sound TLS handling.
- **B — Cleartext transport exposure:** Unprotected transport can expose application data to observers or modification on the path.
- **C — Backend authorization:** The server must validate subject and object permissions regardless of checks performed by the mobile client.

Coverage: M17; CEH v5 domain 7; Mobile network security.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q028

**Answer: A — Unsafe deep-link handling**

Deep links can deliver untrusted parameters or navigation requests and must not bypass authentication or validation.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Clipboard exposure:** Sensitive content placed on a clipboard may be available beyond the intended app, depending on platform behavior and context.
- **C — Unsafe WebView boundary:** A WebView that exposes privileged bridges or loads untrusted content can cross from web input into app capabilities.
- **D — Exposed interprocess component:** An exported component can receive calls from other applications; intended caller permissions and input handling matter.

Coverage: M17; CEH v5 domain 7; Application interaction.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q029

**Answer: B — SIM-swap risk**

Transfer of a phone number can expose workflows relying on that number for recovery or authentication.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Malicious profile or management enrollment:** An untrusted configuration profile or management relationship can change device settings and trust boundaries.
- **C — Lost-device exposure:** A lost device creates risks depending on its lock state, stored data, keys and remote management controls.
- **D — Sideloaded malicious app:** An application obtained outside the intended trusted distribution path may carry unreviewed harmful behavior; provenance still needs assessment.

Coverage: M17; CEH v5 domain 7; Mobile threat scenarios.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

### CEH26-M17-Q030

**Answer: D — Work-profile separation**

Separate managed work data and applications from personal contexts where the platform supports that boundary.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Remote response actions:** Remote lock, wipe or session revocation can reduce incident exposure, but depend on reachability, scope and platform behavior.
- **B — MDM policy:** Mobile device management enforces supported device policies and configuration, subject to enrollment and platform capabilities.
- **C — Conditional access:** Access decisions can consider managed-device posture and other signals, while accounting for signal reliability.

Coverage: M17; CEH v5 domain 7; Enterprise mobile controls.
Technical references: [OWASP MASVS](https://mas.owasp.org/MASVS/) · [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)
