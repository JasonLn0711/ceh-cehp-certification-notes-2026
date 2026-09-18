# M13 — Web Servers — instructor key v1.0.0

[Question form](m13.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M13-Q001

**Answer: D — Directory listing**

Directory listing reveals files when a server generates an index for a directory without a suitable default document or restriction.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Path traversal:** Path traversal uses input to access paths outside the intended directory boundary when path handling is unsafe.
- **B — Verbose error disclosure:** Detailed error responses can expose internal paths, versions or implementation information useful to an attacker.
- **C — Default content exposure:** Default pages, sample applications or unused administrative components can reveal information or add unnecessary attack surface.

Coverage: M13; CEH v5 domain 5; Web-server exposure.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q002

**Answer: D — Remove unused features**

Disable or remove unneeded handlers, modules and sample applications to reduce attack surface.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Run with limited privileges:** Give the web process only the operating-system and filesystem access its function needs.
- **B — Apply supported updates:** Use maintained software and verified relevant fixes; deployment and restart state must make the fix effective.
- **C — Separate writable and executable content:** Prevent user-controlled uploads or writable directories from being interpreted as server-side executable code.

Coverage: M13; CEH v5 domain 5; Server hardening.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q003

**Answer: B — GET**

GET requests a representation and is defined with safe semantics; applications should not use it for unintended state-changing operations.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — PUT:** PUT requests creation or replacement of the target resource's state; enabling it does not by itself prove unauthorized write access.
- **C — OPTIONS:** OPTIONS describes communication options for a target or server, but advertised methods do not prove they are usable by every identity.
- **D — POST:** POST submits data for resource-specific processing and may change state; authorization and CSRF controls still matter.

Coverage: M13; CEH v5 domain 5; HTTP method interpretation.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q004

**Answer: B — 401 Unauthorized**

HTTP 401 indicates that valid authentication credentials are required for the target resource; protocol details include the applicable challenge.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — 500 Internal Server Error:** HTTP 500 indicates an unexpected server-side condition; the response alone does not prove a particular exploit succeeded.
- **C — 403 Forbidden:** HTTP 403 indicates that the server understood the request but refuses it; the reason is not necessarily missing authentication.
- **D — 404 Not Found:** HTTP 404 reports that the target resource is not found or is not being disclosed; it does not prove a file never existed.

Coverage: M13; CEH v5 domain 5; Server response evidence.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q005

**Answer: A — Trusted proxy configuration**

Accept forwarding metadata only from defined trusted proxies, not arbitrary clients that can forge headers.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Host validation:** Validate host information before using it for routing, links or security-sensitive decisions.
- **C — Consistent HTTP parsing:** Frontends and backends must agree on request framing and interpretation to avoid boundary confusion.
- **D — Origin access restriction:** Restrict direct access to an origin when security controls are intended to be enforced by its reverse proxy.

Coverage: M13; CEH v5 domain 5; Proxy trust boundaries.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q006

**Answer: A — Access log**

An access log records request activity as configured, such as path, status, client information and timing.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — File integrity evidence:** Trusted file comparisons help detect unexpected changes to deployed content, subject to a trustworthy baseline.
- **C — Error log:** An error log records server or application failures and can provide context absent from the client response.
- **D — Process and endpoint evidence:** Host-level process, execution and connection information can corroborate what a web request actually caused.

Coverage: M13; CEH v5 domain 5; Web incident evidence.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q007

**Answer: C — Path traversal**

Path traversal uses input to access paths outside the intended directory boundary when path handling is unsafe.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Verbose error disclosure:** Detailed error responses can expose internal paths, versions or implementation information useful to an attacker.
- **B — Directory listing:** Directory listing reveals files when a server generates an index for a directory without a suitable default document or restriction.
- **D — Default content exposure:** Default pages, sample applications or unused administrative components can reveal information or add unnecessary attack surface.

Coverage: M13; CEH v5 domain 5; Web-server exposure.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q008

**Answer: A — Run with limited privileges**

Give the web process only the operating-system and filesystem access its function needs.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Remove unused features:** Disable or remove unneeded handlers, modules and sample applications to reduce attack surface.
- **C — Separate writable and executable content:** Prevent user-controlled uploads or writable directories from being interpreted as server-side executable code.
- **D — Apply supported updates:** Use maintained software and verified relevant fixes; deployment and restart state must make the fix effective.

Coverage: M13; CEH v5 domain 5; Server hardening.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q009

**Answer: C — POST**

POST submits data for resource-specific processing and may change state; authorization and CSRF controls still matter.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — GET:** GET requests a representation and is defined with safe semantics; applications should not use it for unintended state-changing operations.
- **B — PUT:** PUT requests creation or replacement of the target resource's state; enabling it does not by itself prove unauthorized write access.
- **D — OPTIONS:** OPTIONS describes communication options for a target or server, but advertised methods do not prove they are usable by every identity.

Coverage: M13; CEH v5 domain 5; HTTP method interpretation.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q010

**Answer: D — 403 Forbidden**

HTTP 403 indicates that the server understood the request but refuses it; the reason is not necessarily missing authentication.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — 500 Internal Server Error:** HTTP 500 indicates an unexpected server-side condition; the response alone does not prove a particular exploit succeeded.
- **B — 404 Not Found:** HTTP 404 reports that the target resource is not found or is not being disclosed; it does not prove a file never existed.
- **C — 401 Unauthorized:** HTTP 401 indicates that valid authentication credentials are required for the target resource; protocol details include the applicable challenge.

Coverage: M13; CEH v5 domain 5; Server response evidence.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q011

**Answer: C — Consistent HTTP parsing**

Frontends and backends must agree on request framing and interpretation to avoid boundary confusion.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Origin access restriction:** Restrict direct access to an origin when security controls are intended to be enforced by its reverse proxy.
- **B — Host validation:** Validate host information before using it for routing, links or security-sensitive decisions.
- **D — Trusted proxy configuration:** Accept forwarding metadata only from defined trusted proxies, not arbitrary clients that can forge headers.

Coverage: M13; CEH v5 domain 5; Proxy trust boundaries.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q012

**Answer: A — Error log**

An error log records server or application failures and can provide context absent from the client response.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Process and endpoint evidence:** Host-level process, execution and connection information can corroborate what a web request actually caused.
- **C — Access log:** An access log records request activity as configured, such as path, status, client information and timing.
- **D — File integrity evidence:** Trusted file comparisons help detect unexpected changes to deployed content, subject to a trustworthy baseline.

Coverage: M13; CEH v5 domain 5; Web incident evidence.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q013

**Answer: B — Default content exposure**

Default pages, sample applications or unused administrative components can reveal information or add unnecessary attack surface.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Path traversal:** Path traversal uses input to access paths outside the intended directory boundary when path handling is unsafe.
- **C — Verbose error disclosure:** Detailed error responses can expose internal paths, versions or implementation information useful to an attacker.
- **D — Directory listing:** Directory listing reveals files when a server generates an index for a directory without a suitable default document or restriction.

Coverage: M13; CEH v5 domain 5; Web-server exposure.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q014

**Answer: B — Separate writable and executable content**

Prevent user-controlled uploads or writable directories from being interpreted as server-side executable code.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Run with limited privileges:** Give the web process only the operating-system and filesystem access its function needs.
- **C — Remove unused features:** Disable or remove unneeded handlers, modules and sample applications to reduce attack surface.
- **D — Apply supported updates:** Use maintained software and verified relevant fixes; deployment and restart state must make the fix effective.

Coverage: M13; CEH v5 domain 5; Server hardening.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q015

**Answer: B — PUT**

PUT requests creation or replacement of the target resource's state; enabling it does not by itself prove unauthorized write access.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — POST:** POST submits data for resource-specific processing and may change state; authorization and CSRF controls still matter.
- **C — OPTIONS:** OPTIONS describes communication options for a target or server, but advertised methods do not prove they are usable by every identity.
- **D — GET:** GET requests a representation and is defined with safe semantics; applications should not use it for unintended state-changing operations.

Coverage: M13; CEH v5 domain 5; HTTP method interpretation.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q016

**Answer: D — 404 Not Found**

HTTP 404 reports that the target resource is not found or is not being disclosed; it does not prove a file never existed.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — 500 Internal Server Error:** HTTP 500 indicates an unexpected server-side condition; the response alone does not prove a particular exploit succeeded.
- **B — 401 Unauthorized:** HTTP 401 indicates that valid authentication credentials are required for the target resource; protocol details include the applicable challenge.
- **C — 403 Forbidden:** HTTP 403 indicates that the server understood the request but refuses it; the reason is not necessarily missing authentication.

Coverage: M13; CEH v5 domain 5; Server response evidence.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q017

**Answer: D — Origin access restriction**

Restrict direct access to an origin when security controls are intended to be enforced by its reverse proxy.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Host validation:** Validate host information before using it for routing, links or security-sensitive decisions.
- **B — Trusted proxy configuration:** Accept forwarding metadata only from defined trusted proxies, not arbitrary clients that can forge headers.
- **C — Consistent HTTP parsing:** Frontends and backends must agree on request framing and interpretation to avoid boundary confusion.

Coverage: M13; CEH v5 domain 5; Proxy trust boundaries.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q018

**Answer: C — File integrity evidence**

Trusted file comparisons help detect unexpected changes to deployed content, subject to a trustworthy baseline.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Error log:** An error log records server or application failures and can provide context absent from the client response.
- **B — Process and endpoint evidence:** Host-level process, execution and connection information can corroborate what a web request actually caused.
- **D — Access log:** An access log records request activity as configured, such as path, status, client information and timing.

Coverage: M13; CEH v5 domain 5; Web incident evidence.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q019

**Answer: A — Verbose error disclosure**

Detailed error responses can expose internal paths, versions or implementation information useful to an attacker.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Directory listing:** Directory listing reveals files when a server generates an index for a directory without a suitable default document or restriction.
- **C — Path traversal:** Path traversal uses input to access paths outside the intended directory boundary when path handling is unsafe.
- **D — Default content exposure:** Default pages, sample applications or unused administrative components can reveal information or add unnecessary attack surface.

Coverage: M13; CEH v5 domain 5; Web-server exposure.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q020

**Answer: A — Apply supported updates**

Use maintained software and verified relevant fixes; deployment and restart state must make the fix effective.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Run with limited privileges:** Give the web process only the operating-system and filesystem access its function needs.
- **C — Separate writable and executable content:** Prevent user-controlled uploads or writable directories from being interpreted as server-side executable code.
- **D — Remove unused features:** Disable or remove unneeded handlers, modules and sample applications to reduce attack surface.

Coverage: M13; CEH v5 domain 5; Server hardening.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q021

**Answer: D — OPTIONS**

OPTIONS describes communication options for a target or server, but advertised methods do not prove they are usable by every identity.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — PUT:** PUT requests creation or replacement of the target resource's state; enabling it does not by itself prove unauthorized write access.
- **B — GET:** GET requests a representation and is defined with safe semantics; applications should not use it for unintended state-changing operations.
- **C — POST:** POST submits data for resource-specific processing and may change state; authorization and CSRF controls still matter.

Coverage: M13; CEH v5 domain 5; HTTP method interpretation.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q022

**Answer: B — 500 Internal Server Error**

HTTP 500 indicates an unexpected server-side condition; the response alone does not prove a particular exploit succeeded.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — 403 Forbidden:** HTTP 403 indicates that the server understood the request but refuses it; the reason is not necessarily missing authentication.
- **C — 401 Unauthorized:** HTTP 401 indicates that valid authentication credentials are required for the target resource; protocol details include the applicable challenge.
- **D — 404 Not Found:** HTTP 404 reports that the target resource is not found or is not being disclosed; it does not prove a file never existed.

Coverage: M13; CEH v5 domain 5; Server response evidence.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q023

**Answer: B — Host validation**

Validate host information before using it for routing, links or security-sensitive decisions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Trusted proxy configuration:** Accept forwarding metadata only from defined trusted proxies, not arbitrary clients that can forge headers.
- **C — Consistent HTTP parsing:** Frontends and backends must agree on request framing and interpretation to avoid boundary confusion.
- **D — Origin access restriction:** Restrict direct access to an origin when security controls are intended to be enforced by its reverse proxy.

Coverage: M13; CEH v5 domain 5; Proxy trust boundaries.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q024

**Answer: C — Process and endpoint evidence**

Host-level process, execution and connection information can corroborate what a web request actually caused.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — File integrity evidence:** Trusted file comparisons help detect unexpected changes to deployed content, subject to a trustworthy baseline.
- **B — Error log:** An error log records server or application failures and can provide context absent from the client response.
- **D — Access log:** An access log records request activity as configured, such as path, status, client information and timing.

Coverage: M13; CEH v5 domain 5; Web incident evidence.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q025

**Answer: D — Directory listing**

Directory listing reveals files when a server generates an index for a directory without a suitable default document or restriction.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Verbose error disclosure:** Detailed error responses can expose internal paths, versions or implementation information useful to an attacker.
- **B — Default content exposure:** Default pages, sample applications or unused administrative components can reveal information or add unnecessary attack surface.
- **C — Path traversal:** Path traversal uses input to access paths outside the intended directory boundary when path handling is unsafe.

Coverage: M13; CEH v5 domain 5; Web-server exposure.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q026

**Answer: A — Run with limited privileges**

Give the web process only the operating-system and filesystem access its function needs.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Apply supported updates:** Use maintained software and verified relevant fixes; deployment and restart state must make the fix effective.
- **C — Separate writable and executable content:** Prevent user-controlled uploads or writable directories from being interpreted as server-side executable code.
- **D — Remove unused features:** Disable or remove unneeded handlers, modules and sample applications to reduce attack surface.

Coverage: M13; CEH v5 domain 5; Server hardening.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q027

**Answer: B — PUT**

PUT requests creation or replacement of the target resource's state; enabling it does not by itself prove unauthorized write access.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — POST:** POST submits data for resource-specific processing and may change state; authorization and CSRF controls still matter.
- **C — OPTIONS:** OPTIONS describes communication options for a target or server, but advertised methods do not prove they are usable by every identity.
- **D — GET:** GET requests a representation and is defined with safe semantics; applications should not use it for unintended state-changing operations.

Coverage: M13; CEH v5 domain 5; HTTP method interpretation.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q028

**Answer: C — 403 Forbidden**

HTTP 403 indicates that the server understood the request but refuses it; the reason is not necessarily missing authentication.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — 404 Not Found:** HTTP 404 reports that the target resource is not found or is not being disclosed; it does not prove a file never existed.
- **B — 500 Internal Server Error:** HTTP 500 indicates an unexpected server-side condition; the response alone does not prove a particular exploit succeeded.
- **D — 401 Unauthorized:** HTTP 401 indicates that valid authentication credentials are required for the target resource; protocol details include the applicable challenge.

Coverage: M13; CEH v5 domain 5; Server response evidence.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q029

**Answer: C — Trusted proxy configuration**

Accept forwarding metadata only from defined trusted proxies, not arbitrary clients that can forge headers.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Origin access restriction:** Restrict direct access to an origin when security controls are intended to be enforced by its reverse proxy.
- **B — Consistent HTTP parsing:** Frontends and backends must agree on request framing and interpretation to avoid boundary confusion.
- **D — Host validation:** Validate host information before using it for routing, links or security-sensitive decisions.

Coverage: M13; CEH v5 domain 5; Proxy trust boundaries.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M13-Q030

**Answer: A — File integrity evidence**

Trusted file comparisons help detect unexpected changes to deployed content, subject to a trustworthy baseline.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Process and endpoint evidence:** Host-level process, execution and connection information can corroborate what a web request actually caused.
- **C — Access log:** An access log records request activity as configured, such as path, status, client information and timing.
- **D — Error log:** An error log records server or application failures and can provide context absent from the client response.

Coverage: M13; CEH v5 domain 5; Web incident evidence.
Technical references: [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)
