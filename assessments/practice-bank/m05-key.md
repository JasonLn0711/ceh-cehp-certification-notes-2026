# M05 — Vulnerability Analysis — instructor key v1.0.0

[Question form](m05.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M05-Q001

**Answer: A — Vulnerability**

A vulnerability is a weakness that could be exploited under relevant conditions.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Risk:** Risk concerns the likelihood and consequences of an adverse event in a particular context.
- **C — Exploit:** An exploit is a method or mechanism that takes advantage of a vulnerability.
- **D — Threat:** A threat is a potential cause of an adverse event, such as an actor or harmful circumstance.

Coverage: M05; CEH v5 domain 3; Weakness and risk.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q002

**Answer: B — CVE**

A CVE identifier names a publicly disclosed vulnerability record; the identifier itself is not a severity score.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — CVSS:** CVSS expresses technical vulnerability severity using metrics and a versioned scoring method.
- **C — CWE:** CWE classifies weakness types, such as improper input handling or missing authorization.
- **D — CISA KEV:** The Known Exploited Vulnerabilities catalog identifies listed vulnerabilities with evidence of exploitation in the wild.

Coverage: M05; CEH v5 domain 3; Classification systems.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q003

**Answer: C — True positive**

A true positive correctly identifies a condition that is actually present.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — False positive:** A false positive reports a problem that is not actually present under the assessed conditions.
- **B — False negative:** A false negative fails to report a problem that actually exists.
- **D — True negative:** A true negative correctly leaves an absent condition unreported.

Coverage: M05; CEH v5 domain 3; Finding accuracy.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q004

**Answer: B — Credentialed assessment**

A credentialed assessment uses authorized access to inspect information unavailable to an unauthenticated probe.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Unauthenticated assessment:** An unauthenticated assessment observes exposure without logging in; its visibility is limited to that perspective.
- **C — Configuration review:** A configuration review compares settings and effective controls with defined requirements.
- **D — Manual validation:** Manual validation investigates a finding's applicability or behavior beyond an automated label.

Coverage: M05; CEH v5 domain 3; Assessment access.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q005

**Answer: D — Exposure and exploitability**

Reachability, required conditions and credible exploitation evidence affect practical urgency.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Compensating control:** An alternate control can reduce exposure or impact while the underlying weakness is being repaired.
- **B — Business impact:** The affected asset's function and the potential harm determine organizational consequences.
- **C — Residual risk:** Residual risk is the risk that remains after controls or remediation have been applied.

Coverage: M05; CEH v5 domain 3; Remediation priority.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q006

**Answer: C — Apply and verify the fix**

Confirm that the intended change removes the relevant vulnerable condition, rather than only recording that a patch command ran.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Document accepted risk:** When an authorized owner accepts remaining risk, record the scope, reason, owner and review conditions.
- **B — Check for regression:** Verify that the change preserves required behavior and has not introduced a new failure.
- **D — Retest the original finding:** Repeat the permitted check that originally demonstrated the problem and compare the result.

Coverage: M05; CEH v5 domain 3; Remediation lifecycle.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q007

**Answer: A — Threat**

A threat is a potential cause of an adverse event, such as an actor or harmful circumstance.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Risk:** Risk concerns the likelihood and consequences of an adverse event in a particular context.
- **C — Exploit:** An exploit is a method or mechanism that takes advantage of a vulnerability.
- **D — Vulnerability:** A vulnerability is a weakness that could be exploited under relevant conditions.

Coverage: M05; CEH v5 domain 3; Weakness and risk.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q008

**Answer: D — CWE**

CWE classifies weakness types, such as improper input handling or missing authorization.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — CVSS:** CVSS expresses technical vulnerability severity using metrics and a versioned scoring method.
- **B — CISA KEV:** The Known Exploited Vulnerabilities catalog identifies listed vulnerabilities with evidence of exploitation in the wild.
- **C — CVE:** A CVE identifier names a publicly disclosed vulnerability record; the identifier itself is not a severity score.

Coverage: M05; CEH v5 domain 3; Classification systems.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q009

**Answer: D — False positive**

A false positive reports a problem that is not actually present under the assessed conditions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — True negative:** A true negative correctly leaves an absent condition unreported.
- **B — True positive:** A true positive correctly identifies a condition that is actually present.
- **C — False negative:** A false negative fails to report a problem that actually exists.

Coverage: M05; CEH v5 domain 3; Finding accuracy.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q010

**Answer: C — Unauthenticated assessment**

An unauthenticated assessment observes exposure without logging in; its visibility is limited to that perspective.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Credentialed assessment:** A credentialed assessment uses authorized access to inspect information unavailable to an unauthenticated probe.
- **B — Manual validation:** Manual validation investigates a finding's applicability or behavior beyond an automated label.
- **D — Configuration review:** A configuration review compares settings and effective controls with defined requirements.

Coverage: M05; CEH v5 domain 3; Assessment access.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q011

**Answer: D — Business impact**

The affected asset's function and the potential harm determine organizational consequences.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Residual risk:** Residual risk is the risk that remains after controls or remediation have been applied.
- **B — Exposure and exploitability:** Reachability, required conditions and credible exploitation evidence affect practical urgency.
- **C — Compensating control:** An alternate control can reduce exposure or impact while the underlying weakness is being repaired.

Coverage: M05; CEH v5 domain 3; Remediation priority.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q012

**Answer: A — Retest the original finding**

Repeat the permitted check that originally demonstrated the problem and compare the result.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Check for regression:** Verify that the change preserves required behavior and has not introduced a new failure.
- **C — Apply and verify the fix:** Confirm that the intended change removes the relevant vulnerable condition, rather than only recording that a patch command ran.
- **D — Document accepted risk:** When an authorized owner accepts remaining risk, record the scope, reason, owner and review conditions.

Coverage: M05; CEH v5 domain 3; Remediation lifecycle.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q013

**Answer: C — Exploit**

An exploit is a method or mechanism that takes advantage of a vulnerability.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Risk:** Risk concerns the likelihood and consequences of an adverse event in a particular context.
- **B — Vulnerability:** A vulnerability is a weakness that could be exploited under relevant conditions.
- **D — Threat:** A threat is a potential cause of an adverse event, such as an actor or harmful circumstance.

Coverage: M05; CEH v5 domain 3; Weakness and risk.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q014

**Answer: D — CVSS**

CVSS expresses technical vulnerability severity using metrics and a versioned scoring method.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — CVE:** A CVE identifier names a publicly disclosed vulnerability record; the identifier itself is not a severity score.
- **B — CISA KEV:** The Known Exploited Vulnerabilities catalog identifies listed vulnerabilities with evidence of exploitation in the wild.
- **C — CWE:** CWE classifies weakness types, such as improper input handling or missing authorization.

Coverage: M05; CEH v5 domain 3; Classification systems.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q015

**Answer: B — False negative**

A false negative fails to report a problem that actually exists.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — False positive:** A false positive reports a problem that is not actually present under the assessed conditions.
- **C — True positive:** A true positive correctly identifies a condition that is actually present.
- **D — True negative:** A true negative correctly leaves an absent condition unreported.

Coverage: M05; CEH v5 domain 3; Finding accuracy.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q016

**Answer: A — Configuration review**

A configuration review compares settings and effective controls with defined requirements.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Unauthenticated assessment:** An unauthenticated assessment observes exposure without logging in; its visibility is limited to that perspective.
- **C — Credentialed assessment:** A credentialed assessment uses authorized access to inspect information unavailable to an unauthenticated probe.
- **D — Manual validation:** Manual validation investigates a finding's applicability or behavior beyond an automated label.

Coverage: M05; CEH v5 domain 3; Assessment access.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q017

**Answer: C — Compensating control**

An alternate control can reduce exposure or impact while the underlying weakness is being repaired.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Exposure and exploitability:** Reachability, required conditions and credible exploitation evidence affect practical urgency.
- **B — Business impact:** The affected asset's function and the potential harm determine organizational consequences.
- **D — Residual risk:** Residual risk is the risk that remains after controls or remediation have been applied.

Coverage: M05; CEH v5 domain 3; Remediation priority.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q018

**Answer: B — Check for regression**

Verify that the change preserves required behavior and has not introduced a new failure.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Retest the original finding:** Repeat the permitted check that originally demonstrated the problem and compare the result.
- **C — Document accepted risk:** When an authorized owner accepts remaining risk, record the scope, reason, owner and review conditions.
- **D — Apply and verify the fix:** Confirm that the intended change removes the relevant vulnerable condition, rather than only recording that a patch command ran.

Coverage: M05; CEH v5 domain 3; Remediation lifecycle.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q019

**Answer: B — Risk**

Risk concerns the likelihood and consequences of an adverse event in a particular context.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Exploit:** An exploit is a method or mechanism that takes advantage of a vulnerability.
- **C — Vulnerability:** A vulnerability is a weakness that could be exploited under relevant conditions.
- **D — Threat:** A threat is a potential cause of an adverse event, such as an actor or harmful circumstance.

Coverage: M05; CEH v5 domain 3; Weakness and risk.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q020

**Answer: C — CISA KEV**

The Known Exploited Vulnerabilities catalog identifies listed vulnerabilities with evidence of exploitation in the wild.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — CVSS:** CVSS expresses technical vulnerability severity using metrics and a versioned scoring method.
- **B — CWE:** CWE classifies weakness types, such as improper input handling or missing authorization.
- **D — CVE:** A CVE identifier names a publicly disclosed vulnerability record; the identifier itself is not a severity score.

Coverage: M05; CEH v5 domain 3; Classification systems.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q021

**Answer: C — True negative**

A true negative correctly leaves an absent condition unreported.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — True positive:** A true positive correctly identifies a condition that is actually present.
- **B — False positive:** A false positive reports a problem that is not actually present under the assessed conditions.
- **D — False negative:** A false negative fails to report a problem that actually exists.

Coverage: M05; CEH v5 domain 3; Finding accuracy.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q022

**Answer: A — Manual validation**

Manual validation investigates a finding's applicability or behavior beyond an automated label.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Credentialed assessment:** A credentialed assessment uses authorized access to inspect information unavailable to an unauthenticated probe.
- **C — Unauthenticated assessment:** An unauthenticated assessment observes exposure without logging in; its visibility is limited to that perspective.
- **D — Configuration review:** A configuration review compares settings and effective controls with defined requirements.

Coverage: M05; CEH v5 domain 3; Assessment access.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q023

**Answer: B — Residual risk**

Residual risk is the risk that remains after controls or remediation have been applied.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Compensating control:** An alternate control can reduce exposure or impact while the underlying weakness is being repaired.
- **C — Business impact:** The affected asset's function and the potential harm determine organizational consequences.
- **D — Exposure and exploitability:** Reachability, required conditions and credible exploitation evidence affect practical urgency.

Coverage: M05; CEH v5 domain 3; Remediation priority.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q024

**Answer: C — Document accepted risk**

When an authorized owner accepts remaining risk, record the scope, reason, owner and review conditions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Check for regression:** Verify that the change preserves required behavior and has not introduced a new failure.
- **B — Apply and verify the fix:** Confirm that the intended change removes the relevant vulnerable condition, rather than only recording that a patch command ran.
- **D — Retest the original finding:** Repeat the permitted check that originally demonstrated the problem and compare the result.

Coverage: M05; CEH v5 domain 3; Remediation lifecycle.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q025

**Answer: B — Vulnerability**

A vulnerability is a weakness that could be exploited under relevant conditions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Threat:** A threat is a potential cause of an adverse event, such as an actor or harmful circumstance.
- **C — Exploit:** An exploit is a method or mechanism that takes advantage of a vulnerability.
- **D — Risk:** Risk concerns the likelihood and consequences of an adverse event in a particular context.

Coverage: M05; CEH v5 domain 3; Weakness and risk.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q026

**Answer: D — CVE**

A CVE identifier names a publicly disclosed vulnerability record; the identifier itself is not a severity score.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — CISA KEV:** The Known Exploited Vulnerabilities catalog identifies listed vulnerabilities with evidence of exploitation in the wild.
- **B — CVSS:** CVSS expresses technical vulnerability severity using metrics and a versioned scoring method.
- **C — CWE:** CWE classifies weakness types, such as improper input handling or missing authorization.

Coverage: M05; CEH v5 domain 3; Classification systems.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q027

**Answer: B — False positive**

A false positive reports a problem that is not actually present under the assessed conditions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — True negative:** A true negative correctly leaves an absent condition unreported.
- **C — False negative:** A false negative fails to report a problem that actually exists.
- **D — True positive:** A true positive correctly identifies a condition that is actually present.

Coverage: M05; CEH v5 domain 3; Finding accuracy.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q028

**Answer: A — Credentialed assessment**

A credentialed assessment uses authorized access to inspect information unavailable to an unauthenticated probe.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Unauthenticated assessment:** An unauthenticated assessment observes exposure without logging in; its visibility is limited to that perspective.
- **C — Manual validation:** Manual validation investigates a finding's applicability or behavior beyond an automated label.
- **D — Configuration review:** A configuration review compares settings and effective controls with defined requirements.

Coverage: M05; CEH v5 domain 3; Assessment access.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q029

**Answer: D — Business impact**

The affected asset's function and the potential harm determine organizational consequences.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Compensating control:** An alternate control can reduce exposure or impact while the underlying weakness is being repaired.
- **B — Residual risk:** Residual risk is the risk that remains after controls or remediation have been applied.
- **C — Exposure and exploitability:** Reachability, required conditions and credible exploitation evidence affect practical urgency.

Coverage: M05; CEH v5 domain 3; Remediation priority.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### CEH26-M05-Q030

**Answer: A — Apply and verify the fix**

Confirm that the intended change removes the relevant vulnerable condition, rather than only recording that a patch command ran.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Check for regression:** Verify that the change preserves required behavior and has not introduced a new failure.
- **C — Retest the original finding:** Repeat the permitted check that originally demonstrated the problem and compare the result.
- **D — Document accepted risk:** When an authorized owner accepts remaining risk, record the scope, reason, owner and review conditions.

Coverage: M05; CEH v5 domain 3; Remediation lifecycle.
Technical references: [FIRST CVSS](https://www.first.org/cvss/) · [CWE](https://cwe.mitre.org/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
