# M15 — SQL Injection — instructor key v1.0.0

[Question form](m15.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M15-Q001

**Answer: B — Union-based SQL injection**

Union-based injection combines compatible query results so additional data may appear in the application's response.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Boolean-based blind SQL injection:** Boolean-based blind injection infers a condition from consistent differences between true and false responses.
- **C — Time-based blind SQL injection:** Time-based blind injection infers execution from controlled timing differences, which require repeated context-aware validation.
- **D — Error-based SQL injection:** Error-based injection uses database error behavior or disclosed error details to learn about query execution or data.

Coverage: M15; CEH v5 domain 5; SQL injection types.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q002

**Answer: A — Data interpreted as query syntax**

Injection arises when untrusted data can alter the intended SQL structure rather than remaining a bound value.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Least-privilege database identity:** The application's database account should have only the operations and objects required for its function.
- **C — Bound parameters:** Bound parameters keep supplied values separate from SQL syntax when used correctly by the database API.
- **D — Allowlisted structural choices:** Identifiers or sort directions that cannot be bound as values should be selected from explicit approved structural choices.

Coverage: M15; CEH v5 domain 5; Injection root cause.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q003

**Answer: D — Stored procedure review**

A stored procedure can still be injectable if it constructs unsafe dynamic SQL internally.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Input escaping limitation:** Escaping depends on context, encoding and database rules and is more error-prone than separating query structure from values.
- **B — Client-side check limitation:** Browser validation can be bypassed; the server and database interaction must enforce the security boundary.
- **C — WAF defense-in-depth limitation:** A WAF may block some patterns but does not remove unsafe query construction in the application.

Coverage: M15; CEH v5 domain 5; Misleading defenses.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q004

**Answer: C — Database-specific behavior**

SQL syntax, functions and error messages vary by database; a response must be interpreted in the correct implementation context.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Timing uncertainty:** Network jitter, caching and ordinary load can change response time, so one delay is not conclusive injection evidence.
- **B — Query execution evidence:** A finding needs evidence that input changed database execution, not merely that the application displayed an unusual response.
- **D — Error disclosure:** Detailed database errors reveal internal information, but hiding them does not repair unsafe query construction.

Coverage: M15; CEH v5 domain 5; Database evidence.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q005

**Answer: D — Unauthorized read**

A flaw can expose records that the current subject is not allowed to retrieve.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Availability impact:** A database operation can degrade or stop service through excessive work, locks or destructive changes.
- **B — Unauthorized modification:** A flaw can change or delete data beyond the application's intended permitted operation.
- **C — Authentication bypass:** A manipulated query can incorrectly satisfy an authentication decision when that decision relies on unsafe SQL construction.

Coverage: M15; CEH v5 domain 5; Impact boundaries.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q006

**Answer: A — Test literal handling**

Confirm that SQL-looking input is processed as ordinary data or rejected by the intended contract, not executed as syntax.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Review every query path:** Apply safe construction to all relevant paths, including alternate endpoints and background jobs using the same data.
- **C — Retest valid inputs:** Verify normal application behavior so an injection fix does not merely disable the feature.
- **D — Check database permissions:** Review the account's actual database privileges to limit damage if another application flaw appears.

Coverage: M15; CEH v5 domain 5; Fix verification.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q007

**Answer: C — Error-based SQL injection**

Error-based injection uses database error behavior or disclosed error details to learn about query execution or data.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Boolean-based blind SQL injection:** Boolean-based blind injection infers a condition from consistent differences between true and false responses.
- **B — Time-based blind SQL injection:** Time-based blind injection infers execution from controlled timing differences, which require repeated context-aware validation.
- **D — Union-based SQL injection:** Union-based injection combines compatible query results so additional data may appear in the application's response.

Coverage: M15; CEH v5 domain 5; SQL injection types.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q008

**Answer: D — Bound parameters**

Bound parameters keep supplied values separate from SQL syntax when used correctly by the database API.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Least-privilege database identity:** The application's database account should have only the operations and objects required for its function.
- **B — Allowlisted structural choices:** Identifiers or sort directions that cannot be bound as values should be selected from explicit approved structural choices.
- **C — Data interpreted as query syntax:** Injection arises when untrusted data can alter the intended SQL structure rather than remaining a bound value.

Coverage: M15; CEH v5 domain 5; Injection root cause.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q009

**Answer: A — Input escaping limitation**

Escaping depends on context, encoding and database rules and is more error-prone than separating query structure from values.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Client-side check limitation:** Browser validation can be bypassed; the server and database interaction must enforce the security boundary.
- **C — Stored procedure review:** A stored procedure can still be injectable if it constructs unsafe dynamic SQL internally.
- **D — WAF defense-in-depth limitation:** A WAF may block some patterns but does not remove unsafe query construction in the application.

Coverage: M15; CEH v5 domain 5; Misleading defenses.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q010

**Answer: B — Query execution evidence**

A finding needs evidence that input changed database execution, not merely that the application displayed an unusual response.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Database-specific behavior:** SQL syntax, functions and error messages vary by database; a response must be interpreted in the correct implementation context.
- **C — Error disclosure:** Detailed database errors reveal internal information, but hiding them does not repair unsafe query construction.
- **D — Timing uncertainty:** Network jitter, caching and ordinary load can change response time, so one delay is not conclusive injection evidence.

Coverage: M15; CEH v5 domain 5; Database evidence.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q011

**Answer: C — Unauthorized modification**

A flaw can change or delete data beyond the application's intended permitted operation.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Authentication bypass:** A manipulated query can incorrectly satisfy an authentication decision when that decision relies on unsafe SQL construction.
- **B — Unauthorized read:** A flaw can expose records that the current subject is not allowed to retrieve.
- **D — Availability impact:** A database operation can degrade or stop service through excessive work, locks or destructive changes.

Coverage: M15; CEH v5 domain 5; Impact boundaries.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q012

**Answer: B — Retest valid inputs**

Verify normal application behavior so an injection fix does not merely disable the feature.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Check database permissions:** Review the account's actual database privileges to limit damage if another application flaw appears.
- **C — Review every query path:** Apply safe construction to all relevant paths, including alternate endpoints and background jobs using the same data.
- **D — Test literal handling:** Confirm that SQL-looking input is processed as ordinary data or rejected by the intended contract, not executed as syntax.

Coverage: M15; CEH v5 domain 5; Fix verification.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q013

**Answer: D — Boolean-based blind SQL injection**

Boolean-based blind injection infers a condition from consistent differences between true and false responses.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Time-based blind SQL injection:** Time-based blind injection infers execution from controlled timing differences, which require repeated context-aware validation.
- **B — Error-based SQL injection:** Error-based injection uses database error behavior or disclosed error details to learn about query execution or data.
- **C — Union-based SQL injection:** Union-based injection combines compatible query results so additional data may appear in the application's response.

Coverage: M15; CEH v5 domain 5; SQL injection types.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q014

**Answer: B — Allowlisted structural choices**

Identifiers or sort directions that cannot be bound as values should be selected from explicit approved structural choices.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Data interpreted as query syntax:** Injection arises when untrusted data can alter the intended SQL structure rather than remaining a bound value.
- **C — Least-privilege database identity:** The application's database account should have only the operations and objects required for its function.
- **D — Bound parameters:** Bound parameters keep supplied values separate from SQL syntax when used correctly by the database API.

Coverage: M15; CEH v5 domain 5; Injection root cause.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q015

**Answer: D — Client-side check limitation**

Browser validation can be bypassed; the server and database interaction must enforce the security boundary.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Stored procedure review:** A stored procedure can still be injectable if it constructs unsafe dynamic SQL internally.
- **B — Input escaping limitation:** Escaping depends on context, encoding and database rules and is more error-prone than separating query structure from values.
- **C — WAF defense-in-depth limitation:** A WAF may block some patterns but does not remove unsafe query construction in the application.

Coverage: M15; CEH v5 domain 5; Misleading defenses.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q016

**Answer: C — Timing uncertainty**

Network jitter, caching and ordinary load can change response time, so one delay is not conclusive injection evidence.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Query execution evidence:** A finding needs evidence that input changed database execution, not merely that the application displayed an unusual response.
- **B — Error disclosure:** Detailed database errors reveal internal information, but hiding them does not repair unsafe query construction.
- **D — Database-specific behavior:** SQL syntax, functions and error messages vary by database; a response must be interpreted in the correct implementation context.

Coverage: M15; CEH v5 domain 5; Database evidence.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q017

**Answer: B — Authentication bypass**

A manipulated query can incorrectly satisfy an authentication decision when that decision relies on unsafe SQL construction.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Availability impact:** A database operation can degrade or stop service through excessive work, locks or destructive changes.
- **C — Unauthorized modification:** A flaw can change or delete data beyond the application's intended permitted operation.
- **D — Unauthorized read:** A flaw can expose records that the current subject is not allowed to retrieve.

Coverage: M15; CEH v5 domain 5; Impact boundaries.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q018

**Answer: D — Review every query path**

Apply safe construction to all relevant paths, including alternate endpoints and background jobs using the same data.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Test literal handling:** Confirm that SQL-looking input is processed as ordinary data or rejected by the intended contract, not executed as syntax.
- **B — Check database permissions:** Review the account's actual database privileges to limit damage if another application flaw appears.
- **C — Retest valid inputs:** Verify normal application behavior so an injection fix does not merely disable the feature.

Coverage: M15; CEH v5 domain 5; Fix verification.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q019

**Answer: A — Time-based blind SQL injection**

Time-based blind injection infers execution from controlled timing differences, which require repeated context-aware validation.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Union-based SQL injection:** Union-based injection combines compatible query results so additional data may appear in the application's response.
- **C — Error-based SQL injection:** Error-based injection uses database error behavior or disclosed error details to learn about query execution or data.
- **D — Boolean-based blind SQL injection:** Boolean-based blind injection infers a condition from consistent differences between true and false responses.

Coverage: M15; CEH v5 domain 5; SQL injection types.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q020

**Answer: A — Least-privilege database identity**

The application's database account should have only the operations and objects required for its function.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Bound parameters:** Bound parameters keep supplied values separate from SQL syntax when used correctly by the database API.
- **C — Allowlisted structural choices:** Identifiers or sort directions that cannot be bound as values should be selected from explicit approved structural choices.
- **D — Data interpreted as query syntax:** Injection arises when untrusted data can alter the intended SQL structure rather than remaining a bound value.

Coverage: M15; CEH v5 domain 5; Injection root cause.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q021

**Answer: C — WAF defense-in-depth limitation**

A WAF may block some patterns but does not remove unsafe query construction in the application.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Input escaping limitation:** Escaping depends on context, encoding and database rules and is more error-prone than separating query structure from values.
- **B — Stored procedure review:** A stored procedure can still be injectable if it constructs unsafe dynamic SQL internally.
- **D — Client-side check limitation:** Browser validation can be bypassed; the server and database interaction must enforce the security boundary.

Coverage: M15; CEH v5 domain 5; Misleading defenses.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q022

**Answer: C — Error disclosure**

Detailed database errors reveal internal information, but hiding them does not repair unsafe query construction.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Query execution evidence:** A finding needs evidence that input changed database execution, not merely that the application displayed an unusual response.
- **B — Timing uncertainty:** Network jitter, caching and ordinary load can change response time, so one delay is not conclusive injection evidence.
- **D — Database-specific behavior:** SQL syntax, functions and error messages vary by database; a response must be interpreted in the correct implementation context.

Coverage: M15; CEH v5 domain 5; Database evidence.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q023

**Answer: A — Availability impact**

A database operation can degrade or stop service through excessive work, locks or destructive changes.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Unauthorized modification:** A flaw can change or delete data beyond the application's intended permitted operation.
- **C — Authentication bypass:** A manipulated query can incorrectly satisfy an authentication decision when that decision relies on unsafe SQL construction.
- **D — Unauthorized read:** A flaw can expose records that the current subject is not allowed to retrieve.

Coverage: M15; CEH v5 domain 5; Impact boundaries.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q024

**Answer: B — Check database permissions**

Review the account's actual database privileges to limit damage if another application flaw appears.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Review every query path:** Apply safe construction to all relevant paths, including alternate endpoints and background jobs using the same data.
- **C — Retest valid inputs:** Verify normal application behavior so an injection fix does not merely disable the feature.
- **D — Test literal handling:** Confirm that SQL-looking input is processed as ordinary data or rejected by the intended contract, not executed as syntax.

Coverage: M15; CEH v5 domain 5; Fix verification.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q025

**Answer: B — Boolean-based blind SQL injection**

Boolean-based blind injection infers a condition from consistent differences between true and false responses.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Union-based SQL injection:** Union-based injection combines compatible query results so additional data may appear in the application's response.
- **C — Time-based blind SQL injection:** Time-based blind injection infers execution from controlled timing differences, which require repeated context-aware validation.
- **D — Error-based SQL injection:** Error-based injection uses database error behavior or disclosed error details to learn about query execution or data.

Coverage: M15; CEH v5 domain 5; SQL injection types.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q026

**Answer: A — Bound parameters**

Bound parameters keep supplied values separate from SQL syntax when used correctly by the database API.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Data interpreted as query syntax:** Injection arises when untrusted data can alter the intended SQL structure rather than remaining a bound value.
- **C — Allowlisted structural choices:** Identifiers or sort directions that cannot be bound as values should be selected from explicit approved structural choices.
- **D — Least-privilege database identity:** The application's database account should have only the operations and objects required for its function.

Coverage: M15; CEH v5 domain 5; Injection root cause.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q027

**Answer: B — Stored procedure review**

A stored procedure can still be injectable if it constructs unsafe dynamic SQL internally.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Input escaping limitation:** Escaping depends on context, encoding and database rules and is more error-prone than separating query structure from values.
- **C — WAF defense-in-depth limitation:** A WAF may block some patterns but does not remove unsafe query construction in the application.
- **D — Client-side check limitation:** Browser validation can be bypassed; the server and database interaction must enforce the security boundary.

Coverage: M15; CEH v5 domain 5; Misleading defenses.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q028

**Answer: D — Database-specific behavior**

SQL syntax, functions and error messages vary by database; a response must be interpreted in the correct implementation context.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Query execution evidence:** A finding needs evidence that input changed database execution, not merely that the application displayed an unusual response.
- **B — Timing uncertainty:** Network jitter, caching and ordinary load can change response time, so one delay is not conclusive injection evidence.
- **C — Error disclosure:** Detailed database errors reveal internal information, but hiding them does not repair unsafe query construction.

Coverage: M15; CEH v5 domain 5; Database evidence.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q029

**Answer: D — Unauthorized read**

A flaw can expose records that the current subject is not allowed to retrieve.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Availability impact:** A database operation can degrade or stop service through excessive work, locks or destructive changes.
- **B — Authentication bypass:** A manipulated query can incorrectly satisfy an authentication decision when that decision relies on unsafe SQL construction.
- **C — Unauthorized modification:** A flaw can change or delete data beyond the application's intended permitted operation.

Coverage: M15; CEH v5 domain 5; Impact boundaries.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

### CEH26-M15-Q030

**Answer: C — Review every query path**

Apply safe construction to all relevant paths, including alternate endpoints and background jobs using the same data.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Test literal handling:** Confirm that SQL-looking input is processed as ordinary data or rejected by the intended contract, not executed as syntax.
- **B — Retest valid inputs:** Verify normal application behavior so an injection fix does not merely disable the feature.
- **D — Check database permissions:** Review the account's actual database privileges to limit damage if another application flaw appears.

Coverage: M15; CEH v5 domain 5; Fix verification.
Technical references: [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)
