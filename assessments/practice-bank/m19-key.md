# M19 — Cloud Computing — instructor key v1.0.0

[Question form](m19.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M19-Q001

**Answer: C — Infrastructure as a Service**

IaaS exposes infrastructure resources while customers typically manage guest operating systems and their workloads.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Software as a Service:** SaaS delivers an application operated by the provider, while customer identities, use and configuration still carry responsibilities.
- **B — Shared responsibility:** Security duties depend on the service and contract; using a provider does not eliminate the customer's responsibilities.
- **D — Platform as a Service:** PaaS manages more of the application platform, while customers still manage their application logic, data and relevant configuration.

Coverage: M19; CEH v5 domain 8; Service models.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q002

**Answer: A — Least-privilege IAM**

Grant only the cloud actions and resources required for a role, with conditions where appropriate.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Short-lived workload credentials:** Use temporary workload identity or credentials rather than distributing long-lived static secrets when supported.
- **C — Explicit resource policy review:** Review resource-level access together with identity policy because both can affect who can use an object or service.
- **D — Privileged-account protection:** Protect high-impact administrative identities with strong authentication, controlled use and recovery procedures.

Coverage: M19; CEH v5 domain 8; Cloud identity.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q003

**Answer: A — Public access control**

Review whether storage resources permit anonymous or unintended principals, including effective policy combinations.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Data classification and placement:** Classify information and choose approved storage locations, retention and handling requirements for that class.
- **C — Encryption and key control:** Storage encryption protects data under a key-management model; it does not replace authorization to read decrypted objects.
- **D — Versioning and recovery:** Retained versions or backups can support recovery, subject to retention, deletion privileges and restore testing.

Coverage: M19; CEH v5 domain 8; Storage and data.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q004

**Answer: B — Security-group policy**

A workload-level network policy constrains permitted traffic according to the cloud service's supported semantics.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Public exposure inventory:** Track public addresses, listeners and service endpoints rather than assuming a resource is private by name.
- **C — Private service connectivity:** Use supported private access paths where appropriate to reduce unnecessary public routing, while retaining authentication and authorization.
- **D — Metadata-service protection:** Protect access to workload metadata and credentials, especially against server-side request paths that can reach it.

Coverage: M19; CEH v5 domain 8; Cloud network paths.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q005

**Answer: A — Container isolation boundary**

Containers usually share a host kernel; isolation is not equivalent to a completely independent hardware machine.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Orchestrator RBAC:** Restrict which identities can perform operations on cluster resources, including sensitive administrative actions.
- **C — Image provenance and maintenance:** Use trustworthy images and maintain their dependencies; a signed origin alone does not mean the contents are vulnerability-free.
- **D — Secret delivery:** Deliver secrets through appropriate restricted mechanisms rather than embedding them in images, code or broadly visible configuration.

Coverage: M19; CEH v5 domain 8; Containers and orchestration.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q006

**Answer: D — Function event validation**

Validate untrusted event data and authorization even when a managed platform invokes the function.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Region and service coverage:** Logging and controls must cover the actual regions and services in use rather than assuming one configured location covers everything.
- **B — Execution and concurrency limits:** Bound function work and concurrency to control availability and cost exposure within platform capabilities.
- **C — Cloud audit trail:** Audit records capture supported management or data events; configuration, retention and protection determine their investigative usefulness.

Coverage: M19; CEH v5 domain 8; Serverless and audit.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q007

**Answer: D — Platform as a Service**

PaaS manages more of the application platform, while customers still manage their application logic, data and relevant configuration.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Shared responsibility:** Security duties depend on the service and contract; using a provider does not eliminate the customer's responsibilities.
- **B — Infrastructure as a Service:** IaaS exposes infrastructure resources while customers typically manage guest operating systems and their workloads.
- **C — Software as a Service:** SaaS delivers an application operated by the provider, while customer identities, use and configuration still carry responsibilities.

Coverage: M19; CEH v5 domain 8; Service models.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q008

**Answer: B — Short-lived workload credentials**

Use temporary workload identity or credentials rather than distributing long-lived static secrets when supported.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Least-privilege IAM:** Grant only the cloud actions and resources required for a role, with conditions where appropriate.
- **C — Explicit resource policy review:** Review resource-level access together with identity policy because both can affect who can use an object or service.
- **D — Privileged-account protection:** Protect high-impact administrative identities with strong authentication, controlled use and recovery procedures.

Coverage: M19; CEH v5 domain 8; Cloud identity.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q009

**Answer: B — Encryption and key control**

Storage encryption protects data under a key-management model; it does not replace authorization to read decrypted objects.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Versioning and recovery:** Retained versions or backups can support recovery, subject to retention, deletion privileges and restore testing.
- **C — Public access control:** Review whether storage resources permit anonymous or unintended principals, including effective policy combinations.
- **D — Data classification and placement:** Classify information and choose approved storage locations, retention and handling requirements for that class.

Coverage: M19; CEH v5 domain 8; Storage and data.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q010

**Answer: C — Public exposure inventory**

Track public addresses, listeners and service endpoints rather than assuming a resource is private by name.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Security-group policy:** A workload-level network policy constrains permitted traffic according to the cloud service's supported semantics.
- **B — Private service connectivity:** Use supported private access paths where appropriate to reduce unnecessary public routing, while retaining authentication and authorization.
- **D — Metadata-service protection:** Protect access to workload metadata and credentials, especially against server-side request paths that can reach it.

Coverage: M19; CEH v5 domain 8; Cloud network paths.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q011

**Answer: B — Image provenance and maintenance**

Use trustworthy images and maintain their dependencies; a signed origin alone does not mean the contents are vulnerability-free.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Container isolation boundary:** Containers usually share a host kernel; isolation is not equivalent to a completely independent hardware machine.
- **C — Secret delivery:** Deliver secrets through appropriate restricted mechanisms rather than embedding them in images, code or broadly visible configuration.
- **D — Orchestrator RBAC:** Restrict which identities can perform operations on cluster resources, including sensitive administrative actions.

Coverage: M19; CEH v5 domain 8; Containers and orchestration.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q012

**Answer: C — Execution and concurrency limits**

Bound function work and concurrency to control availability and cost exposure within platform capabilities.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Region and service coverage:** Logging and controls must cover the actual regions and services in use rather than assuming one configured location covers everything.
- **B — Function event validation:** Validate untrusted event data and authorization even when a managed platform invokes the function.
- **D — Cloud audit trail:** Audit records capture supported management or data events; configuration, retention and protection determine their investigative usefulness.

Coverage: M19; CEH v5 domain 8; Serverless and audit.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q013

**Answer: C — Software as a Service**

SaaS delivers an application operated by the provider, while customer identities, use and configuration still carry responsibilities.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Platform as a Service:** PaaS manages more of the application platform, while customers still manage their application logic, data and relevant configuration.
- **B — Shared responsibility:** Security duties depend on the service and contract; using a provider does not eliminate the customer's responsibilities.
- **D — Infrastructure as a Service:** IaaS exposes infrastructure resources while customers typically manage guest operating systems and their workloads.

Coverage: M19; CEH v5 domain 8; Service models.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q014

**Answer: D — Explicit resource policy review**

Review resource-level access together with identity policy because both can affect who can use an object or service.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Privileged-account protection:** Protect high-impact administrative identities with strong authentication, controlled use and recovery procedures.
- **B — Least-privilege IAM:** Grant only the cloud actions and resources required for a role, with conditions where appropriate.
- **C — Short-lived workload credentials:** Use temporary workload identity or credentials rather than distributing long-lived static secrets when supported.

Coverage: M19; CEH v5 domain 8; Cloud identity.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q015

**Answer: B — Versioning and recovery**

Retained versions or backups can support recovery, subject to retention, deletion privileges and restore testing.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Public access control:** Review whether storage resources permit anonymous or unintended principals, including effective policy combinations.
- **C — Encryption and key control:** Storage encryption protects data under a key-management model; it does not replace authorization to read decrypted objects.
- **D — Data classification and placement:** Classify information and choose approved storage locations, retention and handling requirements for that class.

Coverage: M19; CEH v5 domain 8; Storage and data.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q016

**Answer: A — Metadata-service protection**

Protect access to workload metadata and credentials, especially against server-side request paths that can reach it.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Public exposure inventory:** Track public addresses, listeners and service endpoints rather than assuming a resource is private by name.
- **C — Security-group policy:** A workload-level network policy constrains permitted traffic according to the cloud service's supported semantics.
- **D — Private service connectivity:** Use supported private access paths where appropriate to reduce unnecessary public routing, while retaining authentication and authorization.

Coverage: M19; CEH v5 domain 8; Cloud network paths.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q017

**Answer: A — Orchestrator RBAC**

Restrict which identities can perform operations on cluster resources, including sensitive administrative actions.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Image provenance and maintenance:** Use trustworthy images and maintain their dependencies; a signed origin alone does not mean the contents are vulnerability-free.
- **C — Secret delivery:** Deliver secrets through appropriate restricted mechanisms rather than embedding them in images, code or broadly visible configuration.
- **D — Container isolation boundary:** Containers usually share a host kernel; isolation is not equivalent to a completely independent hardware machine.

Coverage: M19; CEH v5 domain 8; Containers and orchestration.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q018

**Answer: B — Cloud audit trail**

Audit records capture supported management or data events; configuration, retention and protection determine their investigative usefulness.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Function event validation:** Validate untrusted event data and authorization even when a managed platform invokes the function.
- **C — Region and service coverage:** Logging and controls must cover the actual regions and services in use rather than assuming one configured location covers everything.
- **D — Execution and concurrency limits:** Bound function work and concurrency to control availability and cost exposure within platform capabilities.

Coverage: M19; CEH v5 domain 8; Serverless and audit.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q019

**Answer: D — Shared responsibility**

Security duties depend on the service and contract; using a provider does not eliminate the customer's responsibilities.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Platform as a Service:** PaaS manages more of the application platform, while customers still manage their application logic, data and relevant configuration.
- **B — Software as a Service:** SaaS delivers an application operated by the provider, while customer identities, use and configuration still carry responsibilities.
- **C — Infrastructure as a Service:** IaaS exposes infrastructure resources while customers typically manage guest operating systems and their workloads.

Coverage: M19; CEH v5 domain 8; Service models.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q020

**Answer: D — Privileged-account protection**

Protect high-impact administrative identities with strong authentication, controlled use and recovery procedures.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Explicit resource policy review:** Review resource-level access together with identity policy because both can affect who can use an object or service.
- **B — Short-lived workload credentials:** Use temporary workload identity or credentials rather than distributing long-lived static secrets when supported.
- **C — Least-privilege IAM:** Grant only the cloud actions and resources required for a role, with conditions where appropriate.

Coverage: M19; CEH v5 domain 8; Cloud identity.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q021

**Answer: D — Data classification and placement**

Classify information and choose approved storage locations, retention and handling requirements for that class.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Encryption and key control:** Storage encryption protects data under a key-management model; it does not replace authorization to read decrypted objects.
- **B — Public access control:** Review whether storage resources permit anonymous or unintended principals, including effective policy combinations.
- **C — Versioning and recovery:** Retained versions or backups can support recovery, subject to retention, deletion privileges and restore testing.

Coverage: M19; CEH v5 domain 8; Storage and data.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q022

**Answer: A — Private service connectivity**

Use supported private access paths where appropriate to reduce unnecessary public routing, while retaining authentication and authorization.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Metadata-service protection:** Protect access to workload metadata and credentials, especially against server-side request paths that can reach it.
- **C — Security-group policy:** A workload-level network policy constrains permitted traffic according to the cloud service's supported semantics.
- **D — Public exposure inventory:** Track public addresses, listeners and service endpoints rather than assuming a resource is private by name.

Coverage: M19; CEH v5 domain 8; Cloud network paths.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q023

**Answer: C — Secret delivery**

Deliver secrets through appropriate restricted mechanisms rather than embedding them in images, code or broadly visible configuration.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Orchestrator RBAC:** Restrict which identities can perform operations on cluster resources, including sensitive administrative actions.
- **B — Image provenance and maintenance:** Use trustworthy images and maintain their dependencies; a signed origin alone does not mean the contents are vulnerability-free.
- **D — Container isolation boundary:** Containers usually share a host kernel; isolation is not equivalent to a completely independent hardware machine.

Coverage: M19; CEH v5 domain 8; Containers and orchestration.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q024

**Answer: B — Region and service coverage**

Logging and controls must cover the actual regions and services in use rather than assuming one configured location covers everything.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Cloud audit trail:** Audit records capture supported management or data events; configuration, retention and protection determine their investigative usefulness.
- **C — Function event validation:** Validate untrusted event data and authorization even when a managed platform invokes the function.
- **D — Execution and concurrency limits:** Bound function work and concurrency to control availability and cost exposure within platform capabilities.

Coverage: M19; CEH v5 domain 8; Serverless and audit.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q025

**Answer: B — Infrastructure as a Service**

IaaS exposes infrastructure resources while customers typically manage guest operating systems and their workloads.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Platform as a Service:** PaaS manages more of the application platform, while customers still manage their application logic, data and relevant configuration.
- **C — Software as a Service:** SaaS delivers an application operated by the provider, while customer identities, use and configuration still carry responsibilities.
- **D — Shared responsibility:** Security duties depend on the service and contract; using a provider does not eliminate the customer's responsibilities.

Coverage: M19; CEH v5 domain 8; Service models.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q026

**Answer: D — Short-lived workload credentials**

Use temporary workload identity or credentials rather than distributing long-lived static secrets when supported.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Privileged-account protection:** Protect high-impact administrative identities with strong authentication, controlled use and recovery procedures.
- **B — Explicit resource policy review:** Review resource-level access together with identity policy because both can affect who can use an object or service.
- **C — Least-privilege IAM:** Grant only the cloud actions and resources required for a role, with conditions where appropriate.

Coverage: M19; CEH v5 domain 8; Cloud identity.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q027

**Answer: D — Encryption and key control**

Storage encryption protects data under a key-management model; it does not replace authorization to read decrypted objects.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Public access control:** Review whether storage resources permit anonymous or unintended principals, including effective policy combinations.
- **B — Data classification and placement:** Classify information and choose approved storage locations, retention and handling requirements for that class.
- **C — Versioning and recovery:** Retained versions or backups can support recovery, subject to retention, deletion privileges and restore testing.

Coverage: M19; CEH v5 domain 8; Storage and data.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q028

**Answer: A — Security-group policy**

A workload-level network policy constrains permitted traffic according to the cloud service's supported semantics.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Metadata-service protection:** Protect access to workload metadata and credentials, especially against server-side request paths that can reach it.
- **C — Public exposure inventory:** Track public addresses, listeners and service endpoints rather than assuming a resource is private by name.
- **D — Private service connectivity:** Use supported private access paths where appropriate to reduce unnecessary public routing, while retaining authentication and authorization.

Coverage: M19; CEH v5 domain 8; Cloud network paths.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q029

**Answer: C — Container isolation boundary**

Containers usually share a host kernel; isolation is not equivalent to a completely independent hardware machine.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Secret delivery:** Deliver secrets through appropriate restricted mechanisms rather than embedding them in images, code or broadly visible configuration.
- **B — Image provenance and maintenance:** Use trustworthy images and maintain their dependencies; a signed origin alone does not mean the contents are vulnerability-free.
- **D — Orchestrator RBAC:** Restrict which identities can perform operations on cluster resources, including sensitive administrative actions.

Coverage: M19; CEH v5 domain 8; Containers and orchestration.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

### CEH26-M19-Q030

**Answer: C — Function event validation**

Validate untrusted event data and authorization even when a managed platform invokes the function.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Region and service coverage:** Logging and controls must cover the actual regions and services in use rather than assuming one configured location covers everything.
- **B — Execution and concurrency limits:** Bound function work and concurrency to control availability and cost exposure within platform capabilities.
- **D — Cloud audit trail:** Audit records capture supported management or data events; configuration, retention and protection determine their investigative usefulness.

Coverage: M19; CEH v5 domain 8; Serverless and audit.
Technical references: [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) · [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) · [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
