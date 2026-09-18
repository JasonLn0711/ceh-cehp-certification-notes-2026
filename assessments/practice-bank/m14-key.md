# M14 — Web Applications — instructor key v1.0.0

[Question form](m14.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M14-Q001

**Answer: C — Cross-site scripting**

XSS occurs when untrusted content is interpreted as executable script in a browser context.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Broken object authorization:** Broken object authorization lets a subject access or change an object without the required object-level permission.
- **B — Server-side request forgery:** SSRF causes a server to make unintended requests influenced by untrusted input, potentially crossing network trust boundaries.
- **D — OS command injection:** Command injection lets untrusted input alter the intended operating-system command or its execution structure.

Coverage: M14; CEH v5 domain 5; Application weakness classes.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q002

**Answer: C — Stored XSS**

Stored XSS persists malicious input in data later rendered to other users in an unsafe execution context.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Reflected XSS:** Reflected XSS returns request-supplied input in a response where the browser executes it.
- **B — DOM-based XSS:** DOM-based XSS arises when client-side code moves untrusted data into an unsafe browser sink.
- **D — Context-appropriate output encoding:** Encoding must match the output context so untrusted data remains data rather than executable syntax.

Coverage: M14; CEH v5 domain 5; XSS contexts.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q003

**Answer: B — Object-level authorization**

Check whether the subject may access the specific referenced object on every relevant request.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Deny-by-default access policy:** Reject access unless the applicable policy explicitly grants it, including newly added routes.
- **C — Function-level authorization:** Check whether the subject may invoke a privileged operation, not just whether the route is visible in the UI.
- **D — Tenant isolation:** Enforce tenant boundaries in data queries and operations so one tenant cannot reach another's resources.

Coverage: M14; CEH v5 domain 5; Server-side authorization.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q004

**Answer: D — Allowlisted input validation**

Validate expected type, format, bounds and permitted values where the application has a well-defined input contract.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Parameterized interpreter use:** Use APIs that keep data separate from executable command or query structure rather than concatenating syntax.
- **B — Canonical path containment:** Resolve paths consistently and verify that the final target remains within the authorized base location.
- **C — Safe file storage:** Store uploads with controlled names and permissions outside executable paths, and serve them through an appropriate access policy.

Coverage: M14; CEH v5 domain 5; Input and upload controls.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q005

**Answer: D — CORS policy**

CORS controls whether browser scripts may read certain cross-origin responses; it is not a substitute for server authorization.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Server-side validation:** The server must enforce important constraints because clients can modify or bypass browser-side checks.
- **B — Content Security Policy:** CSP can constrain browser resource and script execution as defense in depth, but does not replace fixing injection paths.
- **C — Business-logic validation:** Validate workflow-specific rules, sequence and state transitions rather than only input syntax.

Coverage: M14; CEH v5 domain 5; Browser and API trust.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q006

**Answer: B — Positive and negative authorization tests**

Check both permitted and forbidden operations with appropriate test identities so success is not judged from one allowed case.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Safe proof of impact:** Demonstrate the minimum authorized effect needed to establish a finding without unnecessary data exposure or damage.
- **C — State-change verification:** Verify the actual backend effect rather than assuming a response code proves the intended action occurred.
- **D — Regression coverage:** Retain tests for the repaired weakness and valid behavior so later changes can reveal a recurrence or broken function.

Coverage: M14; CEH v5 domain 5; Testing interpretation.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q007

**Answer: A — Broken object authorization**

Broken object authorization lets a subject access or change an object without the required object-level permission.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Cross-site scripting:** XSS occurs when untrusted content is interpreted as executable script in a browser context.
- **C — Server-side request forgery:** SSRF causes a server to make unintended requests influenced by untrusted input, potentially crossing network trust boundaries.
- **D — OS command injection:** Command injection lets untrusted input alter the intended operating-system command or its execution structure.

Coverage: M14; CEH v5 domain 5; Application weakness classes.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q008

**Answer: B — Reflected XSS**

Reflected XSS returns request-supplied input in a response where the browser executes it.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — DOM-based XSS:** DOM-based XSS arises when client-side code moves untrusted data into an unsafe browser sink.
- **C — Context-appropriate output encoding:** Encoding must match the output context so untrusted data remains data rather than executable syntax.
- **D — Stored XSS:** Stored XSS persists malicious input in data later rendered to other users in an unsafe execution context.

Coverage: M14; CEH v5 domain 5; XSS contexts.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q009

**Answer: A — Function-level authorization**

Check whether the subject may invoke a privileged operation, not just whether the route is visible in the UI.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Tenant isolation:** Enforce tenant boundaries in data queries and operations so one tenant cannot reach another's resources.
- **C — Object-level authorization:** Check whether the subject may access the specific referenced object on every relevant request.
- **D — Deny-by-default access policy:** Reject access unless the applicable policy explicitly grants it, including newly added routes.

Coverage: M14; CEH v5 domain 5; Server-side authorization.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q010

**Answer: A — Safe file storage**

Store uploads with controlled names and permissions outside executable paths, and serve them through an appropriate access policy.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Parameterized interpreter use:** Use APIs that keep data separate from executable command or query structure rather than concatenating syntax.
- **C — Allowlisted input validation:** Validate expected type, format, bounds and permitted values where the application has a well-defined input contract.
- **D — Canonical path containment:** Resolve paths consistently and verify that the final target remains within the authorized base location.

Coverage: M14; CEH v5 domain 5; Input and upload controls.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q011

**Answer: B — Content Security Policy**

CSP can constrain browser resource and script execution as defense in depth, but does not replace fixing injection paths.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Business-logic validation:** Validate workflow-specific rules, sequence and state transitions rather than only input syntax.
- **C — CORS policy:** CORS controls whether browser scripts may read certain cross-origin responses; it is not a substitute for server authorization.
- **D — Server-side validation:** The server must enforce important constraints because clients can modify or bypass browser-side checks.

Coverage: M14; CEH v5 domain 5; Browser and API trust.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q012

**Answer: A — State-change verification**

Verify the actual backend effect rather than assuming a response code proves the intended action occurred.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Regression coverage:** Retain tests for the repaired weakness and valid behavior so later changes can reveal a recurrence or broken function.
- **C — Safe proof of impact:** Demonstrate the minimum authorized effect needed to establish a finding without unnecessary data exposure or damage.
- **D — Positive and negative authorization tests:** Check both permitted and forbidden operations with appropriate test identities so success is not judged from one allowed case.

Coverage: M14; CEH v5 domain 5; Testing interpretation.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q013

**Answer: C — Server-side request forgery**

SSRF causes a server to make unintended requests influenced by untrusted input, potentially crossing network trust boundaries.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — OS command injection:** Command injection lets untrusted input alter the intended operating-system command or its execution structure.
- **B — Cross-site scripting:** XSS occurs when untrusted content is interpreted as executable script in a browser context.
- **D — Broken object authorization:** Broken object authorization lets a subject access or change an object without the required object-level permission.

Coverage: M14; CEH v5 domain 5; Application weakness classes.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q014

**Answer: A — DOM-based XSS**

DOM-based XSS arises when client-side code moves untrusted data into an unsafe browser sink.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Reflected XSS:** Reflected XSS returns request-supplied input in a response where the browser executes it.
- **C — Stored XSS:** Stored XSS persists malicious input in data later rendered to other users in an unsafe execution context.
- **D — Context-appropriate output encoding:** Encoding must match the output context so untrusted data remains data rather than executable syntax.

Coverage: M14; CEH v5 domain 5; XSS contexts.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q015

**Answer: C — Tenant isolation**

Enforce tenant boundaries in data queries and operations so one tenant cannot reach another's resources.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Object-level authorization:** Check whether the subject may access the specific referenced object on every relevant request.
- **B — Deny-by-default access policy:** Reject access unless the applicable policy explicitly grants it, including newly added routes.
- **D — Function-level authorization:** Check whether the subject may invoke a privileged operation, not just whether the route is visible in the UI.

Coverage: M14; CEH v5 domain 5; Server-side authorization.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q016

**Answer: A — Parameterized interpreter use**

Use APIs that keep data separate from executable command or query structure rather than concatenating syntax.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Allowlisted input validation:** Validate expected type, format, bounds and permitted values where the application has a well-defined input contract.
- **C — Safe file storage:** Store uploads with controlled names and permissions outside executable paths, and serve them through an appropriate access policy.
- **D — Canonical path containment:** Resolve paths consistently and verify that the final target remains within the authorized base location.

Coverage: M14; CEH v5 domain 5; Input and upload controls.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q017

**Answer: C — Server-side validation**

The server must enforce important constraints because clients can modify or bypass browser-side checks.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Content Security Policy:** CSP can constrain browser resource and script execution as defense in depth, but does not replace fixing injection paths.
- **B — CORS policy:** CORS controls whether browser scripts may read certain cross-origin responses; it is not a substitute for server authorization.
- **D — Business-logic validation:** Validate workflow-specific rules, sequence and state transitions rather than only input syntax.

Coverage: M14; CEH v5 domain 5; Browser and API trust.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q018

**Answer: B — Safe proof of impact**

Demonstrate the minimum authorized effect needed to establish a finding without unnecessary data exposure or damage.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — State-change verification:** Verify the actual backend effect rather than assuming a response code proves the intended action occurred.
- **C — Regression coverage:** Retain tests for the repaired weakness and valid behavior so later changes can reveal a recurrence or broken function.
- **D — Positive and negative authorization tests:** Check both permitted and forbidden operations with appropriate test identities so success is not judged from one allowed case.

Coverage: M14; CEH v5 domain 5; Testing interpretation.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q019

**Answer: D — OS command injection**

Command injection lets untrusted input alter the intended operating-system command or its execution structure.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Server-side request forgery:** SSRF causes a server to make unintended requests influenced by untrusted input, potentially crossing network trust boundaries.
- **B — Broken object authorization:** Broken object authorization lets a subject access or change an object without the required object-level permission.
- **C — Cross-site scripting:** XSS occurs when untrusted content is interpreted as executable script in a browser context.

Coverage: M14; CEH v5 domain 5; Application weakness classes.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q020

**Answer: D — Context-appropriate output encoding**

Encoding must match the output context so untrusted data remains data rather than executable syntax.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Reflected XSS:** Reflected XSS returns request-supplied input in a response where the browser executes it.
- **B — DOM-based XSS:** DOM-based XSS arises when client-side code moves untrusted data into an unsafe browser sink.
- **C — Stored XSS:** Stored XSS persists malicious input in data later rendered to other users in an unsafe execution context.

Coverage: M14; CEH v5 domain 5; XSS contexts.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q021

**Answer: C — Deny-by-default access policy**

Reject access unless the applicable policy explicitly grants it, including newly added routes.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Function-level authorization:** Check whether the subject may invoke a privileged operation, not just whether the route is visible in the UI.
- **B — Tenant isolation:** Enforce tenant boundaries in data queries and operations so one tenant cannot reach another's resources.
- **D — Object-level authorization:** Check whether the subject may access the specific referenced object on every relevant request.

Coverage: M14; CEH v5 domain 5; Server-side authorization.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q022

**Answer: D — Canonical path containment**

Resolve paths consistently and verify that the final target remains within the authorized base location.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Parameterized interpreter use:** Use APIs that keep data separate from executable command or query structure rather than concatenating syntax.
- **B — Safe file storage:** Store uploads with controlled names and permissions outside executable paths, and serve them through an appropriate access policy.
- **C — Allowlisted input validation:** Validate expected type, format, bounds and permitted values where the application has a well-defined input contract.

Coverage: M14; CEH v5 domain 5; Input and upload controls.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q023

**Answer: A — Business-logic validation**

Validate workflow-specific rules, sequence and state transitions rather than only input syntax.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Content Security Policy:** CSP can constrain browser resource and script execution as defense in depth, but does not replace fixing injection paths.
- **C — Server-side validation:** The server must enforce important constraints because clients can modify or bypass browser-side checks.
- **D — CORS policy:** CORS controls whether browser scripts may read certain cross-origin responses; it is not a substitute for server authorization.

Coverage: M14; CEH v5 domain 5; Browser and API trust.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q024

**Answer: D — Regression coverage**

Retain tests for the repaired weakness and valid behavior so later changes can reveal a recurrence or broken function.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — State-change verification:** Verify the actual backend effect rather than assuming a response code proves the intended action occurred.
- **B — Safe proof of impact:** Demonstrate the minimum authorized effect needed to establish a finding without unnecessary data exposure or damage.
- **C — Positive and negative authorization tests:** Check both permitted and forbidden operations with appropriate test identities so success is not judged from one allowed case.

Coverage: M14; CEH v5 domain 5; Testing interpretation.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q025

**Answer: C — Cross-site scripting**

XSS occurs when untrusted content is interpreted as executable script in a browser context.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — OS command injection:** Command injection lets untrusted input alter the intended operating-system command or its execution structure.
- **B — Server-side request forgery:** SSRF causes a server to make unintended requests influenced by untrusted input, potentially crossing network trust boundaries.
- **D — Broken object authorization:** Broken object authorization lets a subject access or change an object without the required object-level permission.

Coverage: M14; CEH v5 domain 5; Application weakness classes.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q026

**Answer: B — DOM-based XSS**

DOM-based XSS arises when client-side code moves untrusted data into an unsafe browser sink.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Reflected XSS:** Reflected XSS returns request-supplied input in a response where the browser executes it.
- **C — Context-appropriate output encoding:** Encoding must match the output context so untrusted data remains data rather than executable syntax.
- **D — Stored XSS:** Stored XSS persists malicious input in data later rendered to other users in an unsafe execution context.

Coverage: M14; CEH v5 domain 5; XSS contexts.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q027

**Answer: A — Function-level authorization**

Check whether the subject may invoke a privileged operation, not just whether the route is visible in the UI.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Tenant isolation:** Enforce tenant boundaries in data queries and operations so one tenant cannot reach another's resources.
- **C — Deny-by-default access policy:** Reject access unless the applicable policy explicitly grants it, including newly added routes.
- **D — Object-level authorization:** Check whether the subject may access the specific referenced object on every relevant request.

Coverage: M14; CEH v5 domain 5; Server-side authorization.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q028

**Answer: B — Safe file storage**

Store uploads with controlled names and permissions outside executable paths, and serve them through an appropriate access policy.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Allowlisted input validation:** Validate expected type, format, bounds and permitted values where the application has a well-defined input contract.
- **C — Parameterized interpreter use:** Use APIs that keep data separate from executable command or query structure rather than concatenating syntax.
- **D — Canonical path containment:** Resolve paths consistently and verify that the final target remains within the authorized base location.

Coverage: M14; CEH v5 domain 5; Input and upload controls.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q029

**Answer: C — CORS policy**

CORS controls whether browser scripts may read certain cross-origin responses; it is not a substitute for server authorization.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Content Security Policy:** CSP can constrain browser resource and script execution as defense in depth, but does not replace fixing injection paths.
- **B — Business-logic validation:** Validate workflow-specific rules, sequence and state transitions rather than only input syntax.
- **D — Server-side validation:** The server must enforce important constraints because clients can modify or bypass browser-side checks.

Coverage: M14; CEH v5 domain 5; Browser and API trust.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### CEH26-M14-Q030

**Answer: D — Positive and negative authorization tests**

Check both permitted and forbidden operations with appropriate test identities so success is not judged from one allowed case.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Safe proof of impact:** Demonstrate the minimum authorized effect needed to establish a finding without unnecessary data exposure or damage.
- **B — State-change verification:** Verify the actual backend effect rather than assuming a response code proves the intended action occurred.
- **C — Regression coverage:** Retain tests for the repaired weakness and valid behavior so later changes can reveal a recurrence or broken function.

Coverage: M14; CEH v5 domain 5; Testing interpretation.
Technical references: [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
