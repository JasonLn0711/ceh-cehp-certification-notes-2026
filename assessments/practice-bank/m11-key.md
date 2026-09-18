# M11 — Session Hijacking — instructor key v1.0.0

[Question form](m11.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M11-Q001

**Answer: B — Session fixation**

Session fixation reuses an identifier known before login when the application fails to rotate it after authentication.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Session prediction:** Prediction exploits insufficient randomness or structure that makes valid session identifiers guessable.
- **C — Session replay:** Replay presents previously obtained valid session material again; freshness and invalidation controls affect whether it succeeds.
- **D — Session-token theft:** Token theft obtains an existing valid session credential and may allow impersonation without knowing the password.

Coverage: M11; CEH v5 domain 4; Session weaknesses.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q002

**Answer: B — Secure**

The Secure attribute restricts cookie transmission to secure transport contexts; it does not prevent script access by itself.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Path and Domain scope:** Path and Domain influence where a cookie is sent; they should not be treated as a complete authorization boundary.
- **C — HttpOnly:** HttpOnly prevents ordinary client-side script access to the cookie, but does not stop all actions performed by injected script.
- **D — SameSite:** SameSite restricts cookie inclusion in specified cross-site request contexts, depending on its configured value and browser behavior.

Coverage: M11; CEH v5 domain 4; Cookie attributes.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q003

**Answer: C — Rotate after privilege change**

Issue a fresh session identifier after authentication or privilege elevation and invalidate the previous relevant state.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Reauthenticate sensitive actions:** Require fresh verification for sensitive operations when session possession alone is insufficient assurance.
- **B — Invalidate on logout:** Logout should revoke server-side session usability, not merely remove a page or local UI state.
- **D — Idle and absolute timeout:** Idle timeout limits inactivity while absolute timeout bounds total session lifetime regardless of activity.

Coverage: M11; CEH v5 domain 4; Session lifecycle defenses.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q004

**Answer: D — Cross-site request forgery**

CSRF induces a victim's browser to send an unwanted authenticated request using ambient credentials.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Origin validation:** Checking the request's origin information can support CSRF defenses when implemented with appropriate trust and fallback rules.
- **B — Authorization check:** Every protected operation still needs a server-side decision that the current subject may perform that specific action.
- **C — Anti-CSRF token:** An unpredictable request token tied to the expected context helps distinguish legitimate submissions from cross-site forgeries.

Coverage: M11; CEH v5 domain 4; CSRF and session scope.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q005

**Answer: B — TCP sequence validation**

TCP sequence numbers help a receiver place data within an expected stream; acceptable sequence state matters to forged segments.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — TLS peer authentication:** Correct peer authentication helps prevent an intermediary from impersonating the intended TLS endpoint.
- **C — Application session boundary:** An application session has its own credentials and lifecycle, distinct from the lifetime of a single transport connection.
- **D — On-path interception:** An on-path position can observe or influence traffic between peers; encryption and authentication constrain useful tampering.

Coverage: M11; CEH v5 domain 4; Transport-session concepts.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q006

**Answer: A — High-entropy identifier**

A session identifier should be generated with enough unpredictable randomness to resist guessing.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Token signature verification:** Verify a token's signature and intended algorithm with trusted keys before accepting its claims.
- **C — Revocation strategy:** Plan how compromised or logged-out credentials stop working, including the constraints of self-contained tokens.
- **D — Claim validation:** Validate context such as issuer, audience and expiry; a valid signature alone does not make every token suitable for every service.

Coverage: M11; CEH v5 domain 4; Token design.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q007

**Answer: D — Session-token theft**

Token theft obtains an existing valid session credential and may allow impersonation without knowing the password.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Session prediction:** Prediction exploits insufficient randomness or structure that makes valid session identifiers guessable.
- **B — Session fixation:** Session fixation reuses an identifier known before login when the application fails to rotate it after authentication.
- **C — Session replay:** Replay presents previously obtained valid session material again; freshness and invalidation controls affect whether it succeeds.

Coverage: M11; CEH v5 domain 4; Session weaknesses.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q008

**Answer: C — HttpOnly**

HttpOnly prevents ordinary client-side script access to the cookie, but does not stop all actions performed by injected script.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Secure:** The Secure attribute restricts cookie transmission to secure transport contexts; it does not prevent script access by itself.
- **B — SameSite:** SameSite restricts cookie inclusion in specified cross-site request contexts, depending on its configured value and browser behavior.
- **D — Path and Domain scope:** Path and Domain influence where a cookie is sent; they should not be treated as a complete authorization boundary.

Coverage: M11; CEH v5 domain 4; Cookie attributes.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q009

**Answer: D — Invalidate on logout**

Logout should revoke server-side session usability, not merely remove a page or local UI state.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Rotate after privilege change:** Issue a fresh session identifier after authentication or privilege elevation and invalidate the previous relevant state.
- **B — Idle and absolute timeout:** Idle timeout limits inactivity while absolute timeout bounds total session lifetime regardless of activity.
- **C — Reauthenticate sensitive actions:** Require fresh verification for sensitive operations when session possession alone is insufficient assurance.

Coverage: M11; CEH v5 domain 4; Session lifecycle defenses.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q010

**Answer: A — Anti-CSRF token**

An unpredictable request token tied to the expected context helps distinguish legitimate submissions from cross-site forgeries.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Origin validation:** Checking the request's origin information can support CSRF defenses when implemented with appropriate trust and fallback rules.
- **C — Authorization check:** Every protected operation still needs a server-side decision that the current subject may perform that specific action.
- **D — Cross-site request forgery:** CSRF induces a victim's browser to send an unwanted authenticated request using ambient credentials.

Coverage: M11; CEH v5 domain 4; CSRF and session scope.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q011

**Answer: A — On-path interception**

An on-path position can observe or influence traffic between peers; encryption and authentication constrain useful tampering.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Application session boundary:** An application session has its own credentials and lifecycle, distinct from the lifetime of a single transport connection.
- **C — TCP sequence validation:** TCP sequence numbers help a receiver place data within an expected stream; acceptable sequence state matters to forged segments.
- **D — TLS peer authentication:** Correct peer authentication helps prevent an intermediary from impersonating the intended TLS endpoint.

Coverage: M11; CEH v5 domain 4; Transport-session concepts.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q012

**Answer: A — Token signature verification**

Verify a token's signature and intended algorithm with trusted keys before accepting its claims.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Revocation strategy:** Plan how compromised or logged-out credentials stop working, including the constraints of self-contained tokens.
- **C — High-entropy identifier:** A session identifier should be generated with enough unpredictable randomness to resist guessing.
- **D — Claim validation:** Validate context such as issuer, audience and expiry; a valid signature alone does not make every token suitable for every service.

Coverage: M11; CEH v5 domain 4; Token design.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q013

**Answer: B — Session prediction**

Prediction exploits insufficient randomness or structure that makes valid session identifiers guessable.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Session fixation:** Session fixation reuses an identifier known before login when the application fails to rotate it after authentication.
- **C — Session replay:** Replay presents previously obtained valid session material again; freshness and invalidation controls affect whether it succeeds.
- **D — Session-token theft:** Token theft obtains an existing valid session credential and may allow impersonation without knowing the password.

Coverage: M11; CEH v5 domain 4; Session weaknesses.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q014

**Answer: D — SameSite**

SameSite restricts cookie inclusion in specified cross-site request contexts, depending on its configured value and browser behavior.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Path and Domain scope:** Path and Domain influence where a cookie is sent; they should not be treated as a complete authorization boundary.
- **B — Secure:** The Secure attribute restricts cookie transmission to secure transport contexts; it does not prevent script access by itself.
- **C — HttpOnly:** HttpOnly prevents ordinary client-side script access to the cookie, but does not stop all actions performed by injected script.

Coverage: M11; CEH v5 domain 4; Cookie attributes.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q015

**Answer: A — Idle and absolute timeout**

Idle timeout limits inactivity while absolute timeout bounds total session lifetime regardless of activity.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Reauthenticate sensitive actions:** Require fresh verification for sensitive operations when session possession alone is insufficient assurance.
- **C — Invalidate on logout:** Logout should revoke server-side session usability, not merely remove a page or local UI state.
- **D — Rotate after privilege change:** Issue a fresh session identifier after authentication or privilege elevation and invalidate the previous relevant state.

Coverage: M11; CEH v5 domain 4; Session lifecycle defenses.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q016

**Answer: D — Origin validation**

Checking the request's origin information can support CSRF defenses when implemented with appropriate trust and fallback rules.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Cross-site request forgery:** CSRF induces a victim's browser to send an unwanted authenticated request using ambient credentials.
- **B — Authorization check:** Every protected operation still needs a server-side decision that the current subject may perform that specific action.
- **C — Anti-CSRF token:** An unpredictable request token tied to the expected context helps distinguish legitimate submissions from cross-site forgeries.

Coverage: M11; CEH v5 domain 4; CSRF and session scope.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q017

**Answer: B — TLS peer authentication**

Correct peer authentication helps prevent an intermediary from impersonating the intended TLS endpoint.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — TCP sequence validation:** TCP sequence numbers help a receiver place data within an expected stream; acceptable sequence state matters to forged segments.
- **C — Application session boundary:** An application session has its own credentials and lifecycle, distinct from the lifetime of a single transport connection.
- **D — On-path interception:** An on-path position can observe or influence traffic between peers; encryption and authentication constrain useful tampering.

Coverage: M11; CEH v5 domain 4; Transport-session concepts.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q018

**Answer: C — Claim validation**

Validate context such as issuer, audience and expiry; a valid signature alone does not make every token suitable for every service.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Token signature verification:** Verify a token's signature and intended algorithm with trusted keys before accepting its claims.
- **B — Revocation strategy:** Plan how compromised or logged-out credentials stop working, including the constraints of self-contained tokens.
- **D — High-entropy identifier:** A session identifier should be generated with enough unpredictable randomness to resist guessing.

Coverage: M11; CEH v5 domain 4; Token design.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q019

**Answer: D — Session replay**

Replay presents previously obtained valid session material again; freshness and invalidation controls affect whether it succeeds.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Session fixation:** Session fixation reuses an identifier known before login when the application fails to rotate it after authentication.
- **B — Session-token theft:** Token theft obtains an existing valid session credential and may allow impersonation without knowing the password.
- **C — Session prediction:** Prediction exploits insufficient randomness or structure that makes valid session identifiers guessable.

Coverage: M11; CEH v5 domain 4; Session weaknesses.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q020

**Answer: C — Path and Domain scope**

Path and Domain influence where a cookie is sent; they should not be treated as a complete authorization boundary.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Secure:** The Secure attribute restricts cookie transmission to secure transport contexts; it does not prevent script access by itself.
- **B — SameSite:** SameSite restricts cookie inclusion in specified cross-site request contexts, depending on its configured value and browser behavior.
- **D — HttpOnly:** HttpOnly prevents ordinary client-side script access to the cookie, but does not stop all actions performed by injected script.

Coverage: M11; CEH v5 domain 4; Cookie attributes.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q021

**Answer: D — Reauthenticate sensitive actions**

Require fresh verification for sensitive operations when session possession alone is insufficient assurance.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Rotate after privilege change:** Issue a fresh session identifier after authentication or privilege elevation and invalidate the previous relevant state.
- **B — Idle and absolute timeout:** Idle timeout limits inactivity while absolute timeout bounds total session lifetime regardless of activity.
- **C — Invalidate on logout:** Logout should revoke server-side session usability, not merely remove a page or local UI state.

Coverage: M11; CEH v5 domain 4; Session lifecycle defenses.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q022

**Answer: B — Authorization check**

Every protected operation still needs a server-side decision that the current subject may perform that specific action.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Origin validation:** Checking the request's origin information can support CSRF defenses when implemented with appropriate trust and fallback rules.
- **C — Anti-CSRF token:** An unpredictable request token tied to the expected context helps distinguish legitimate submissions from cross-site forgeries.
- **D — Cross-site request forgery:** CSRF induces a victim's browser to send an unwanted authenticated request using ambient credentials.

Coverage: M11; CEH v5 domain 4; CSRF and session scope.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q023

**Answer: A — Application session boundary**

An application session has its own credentials and lifecycle, distinct from the lifetime of a single transport connection.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — TLS peer authentication:** Correct peer authentication helps prevent an intermediary from impersonating the intended TLS endpoint.
- **C — TCP sequence validation:** TCP sequence numbers help a receiver place data within an expected stream; acceptable sequence state matters to forged segments.
- **D — On-path interception:** An on-path position can observe or influence traffic between peers; encryption and authentication constrain useful tampering.

Coverage: M11; CEH v5 domain 4; Transport-session concepts.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q024

**Answer: D — Revocation strategy**

Plan how compromised or logged-out credentials stop working, including the constraints of self-contained tokens.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — High-entropy identifier:** A session identifier should be generated with enough unpredictable randomness to resist guessing.
- **B — Claim validation:** Validate context such as issuer, audience and expiry; a valid signature alone does not make every token suitable for every service.
- **C — Token signature verification:** Verify a token's signature and intended algorithm with trusted keys before accepting its claims.

Coverage: M11; CEH v5 domain 4; Token design.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q025

**Answer: A — Session fixation**

Session fixation reuses an identifier known before login when the application fails to rotate it after authentication.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Session replay:** Replay presents previously obtained valid session material again; freshness and invalidation controls affect whether it succeeds.
- **C — Session-token theft:** Token theft obtains an existing valid session credential and may allow impersonation without knowing the password.
- **D — Session prediction:** Prediction exploits insufficient randomness or structure that makes valid session identifiers guessable.

Coverage: M11; CEH v5 domain 4; Session weaknesses.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q026

**Answer: C — HttpOnly**

HttpOnly prevents ordinary client-side script access to the cookie, but does not stop all actions performed by injected script.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Secure:** The Secure attribute restricts cookie transmission to secure transport contexts; it does not prevent script access by itself.
- **B — SameSite:** SameSite restricts cookie inclusion in specified cross-site request contexts, depending on its configured value and browser behavior.
- **D — Path and Domain scope:** Path and Domain influence where a cookie is sent; they should not be treated as a complete authorization boundary.

Coverage: M11; CEH v5 domain 4; Cookie attributes.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q027

**Answer: B — Idle and absolute timeout**

Idle timeout limits inactivity while absolute timeout bounds total session lifetime regardless of activity.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Invalidate on logout:** Logout should revoke server-side session usability, not merely remove a page or local UI state.
- **C — Rotate after privilege change:** Issue a fresh session identifier after authentication or privilege elevation and invalidate the previous relevant state.
- **D — Reauthenticate sensitive actions:** Require fresh verification for sensitive operations when session possession alone is insufficient assurance.

Coverage: M11; CEH v5 domain 4; Session lifecycle defenses.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q028

**Answer: C — Anti-CSRF token**

An unpredictable request token tied to the expected context helps distinguish legitimate submissions from cross-site forgeries.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Origin validation:** Checking the request's origin information can support CSRF defenses when implemented with appropriate trust and fallback rules.
- **B — Authorization check:** Every protected operation still needs a server-side decision that the current subject may perform that specific action.
- **D — Cross-site request forgery:** CSRF induces a victim's browser to send an unwanted authenticated request using ambient credentials.

Coverage: M11; CEH v5 domain 4; CSRF and session scope.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q029

**Answer: A — TCP sequence validation**

TCP sequence numbers help a receiver place data within an expected stream; acceptable sequence state matters to forged segments.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — On-path interception:** An on-path position can observe or influence traffic between peers; encryption and authentication constrain useful tampering.
- **C — TLS peer authentication:** Correct peer authentication helps prevent an intermediary from impersonating the intended TLS endpoint.
- **D — Application session boundary:** An application session has its own credentials and lifecycle, distinct from the lifetime of a single transport connection.

Coverage: M11; CEH v5 domain 4; Transport-session concepts.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### CEH26-M11-Q030

**Answer: C — Claim validation**

Validate context such as issuer, audience and expiry; a valid signature alone does not make every token suitable for every service.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Token signature verification:** Verify a token's signature and intended algorithm with trusted keys before accepting its claims.
- **B — High-entropy identifier:** A session identifier should be generated with enough unpredictable randomness to resist guessing.
- **D — Revocation strategy:** Plan how compromised or logged-out credentials stop working, including the constraints of self-contained tokens.

Coverage: M11; CEH v5 domain 4; Token design.
Technical references: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
