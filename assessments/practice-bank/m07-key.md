# M07 — Malware Threats — instructor key v1.0.0

[Question form](m07.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M07-Q001

**Answer: B — Virus**

A virus replicates by attaching to a host file or similar carrier and depends on that host's execution or activation.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Worm:** A worm can propagate between systems without needing to attach itself to an ordinary host file.
- **C — Ransomware:** Ransomware denies access to data or systems, commonly through encryption, and demands payment; some campaigns also steal data.
- **D — Trojan:** A Trojan presents an apparently useful or legitimate function while carrying hidden malicious behavior.

Coverage: M07; CEH v5 domain 3; Malware classes.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q002

**Answer: D — Keylogging**

Keylogging captures keystrokes and can expose entered secrets or sensitive content.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Fileless execution:** Fileless techniques emphasize memory or existing interpreters and system facilities; they can still leave observable artifacts.
- **B — Command and control:** Command-and-control communication lets an external controller coordinate or task an implanted component.
- **C — Botnet participation:** A bot joins a group of compromised devices controlled to perform coordinated activity.

Coverage: M07; CEH v5 domain 3; Malware behavior.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q003

**Answer: C — Static analysis**

Static analysis inspects a sample's code or structure without intentionally executing its behavior.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Dynamic analysis:** Dynamic analysis observes behavior while a sample runs in an appropriately controlled environment.
- **B — Memory analysis:** Memory analysis inspects volatile state such as loaded modules, processes and in-memory content.
- **D — Network analysis:** Network analysis studies communications, destinations, protocols and timing rather than relying only on file contents.

Coverage: M07; CEH v5 domain 3; Analysis methods.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q004

**Answer: A — Signature detection**

Signature detection matches known patterns; unseen or changed implementations may evade a particular signature.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Allowlisting:** Allowlisting permits only approved software or behavior under a defined policy, reducing the execution set.
- **C — Reputation checking:** Reputation uses previously collected trust or threat information about an indicator; an unknown reputation is not proof of safety.
- **D — Behavior-based detection:** Behavior-based detection looks for suspicious actions or sequences rather than only exact file patterns.

Coverage: M07; CEH v5 domain 3; Detection approaches.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q005

**Answer: D — Packing or obfuscation**

Packing and obfuscation alter representation to hinder inspection; their presence alone does not prove malicious intent.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Living off the land:** An attacker can misuse legitimate installed tools, so a trusted tool name alone does not establish benign intent.
- **B — False positive investigation:** An alert must be assessed against context and corroborating evidence before being treated as confirmed malicious behavior.
- **C — Sandbox awareness:** A sample may detect analysis conditions and suppress behavior, so a quiet run does not prove safety.

Coverage: M07; CEH v5 domain 3; Evasion and uncertainty.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q006

**Answer: B — Contain the affected system**

Containment limits further harm or spread while preserving the ability to investigate.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Recover and verify:** Recovery restores trusted service and checks that business function and security controls operate as expected.
- **C — Preserve relevant evidence:** Preservation retains necessary logs, volatile data or artifacts before actions that could destroy them, where operational safety permits.
- **D — Eradicate the cause:** Eradication removes malicious components and the access or weakness that enabled the incident.

Coverage: M07; CEH v5 domain 3; Response priorities.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q007

**Answer: A — Worm**

A worm can propagate between systems without needing to attach itself to an ordinary host file.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Ransomware:** Ransomware denies access to data or systems, commonly through encryption, and demands payment; some campaigns also steal data.
- **C — Trojan:** A Trojan presents an apparently useful or legitimate function while carrying hidden malicious behavior.
- **D — Virus:** A virus replicates by attaching to a host file or similar carrier and depends on that host's execution or activation.

Coverage: M07; CEH v5 domain 3; Malware classes.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q008

**Answer: C — Command and control**

Command-and-control communication lets an external controller coordinate or task an implanted component.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Fileless execution:** Fileless techniques emphasize memory or existing interpreters and system facilities; they can still leave observable artifacts.
- **B — Keylogging:** Keylogging captures keystrokes and can expose entered secrets or sensitive content.
- **D — Botnet participation:** A bot joins a group of compromised devices controlled to perform coordinated activity.

Coverage: M07; CEH v5 domain 3; Malware behavior.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q009

**Answer: C — Dynamic analysis**

Dynamic analysis observes behavior while a sample runs in an appropriately controlled environment.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Memory analysis:** Memory analysis inspects volatile state such as loaded modules, processes and in-memory content.
- **B — Network analysis:** Network analysis studies communications, destinations, protocols and timing rather than relying only on file contents.
- **D — Static analysis:** Static analysis inspects a sample's code or structure without intentionally executing its behavior.

Coverage: M07; CEH v5 domain 3; Analysis methods.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q010

**Answer: B — Behavior-based detection**

Behavior-based detection looks for suspicious actions or sequences rather than only exact file patterns.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Signature detection:** Signature detection matches known patterns; unseen or changed implementations may evade a particular signature.
- **C — Allowlisting:** Allowlisting permits only approved software or behavior under a defined policy, reducing the execution set.
- **D — Reputation checking:** Reputation uses previously collected trust or threat information about an indicator; an unknown reputation is not proof of safety.

Coverage: M07; CEH v5 domain 3; Detection approaches.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q011

**Answer: B — Sandbox awareness**

A sample may detect analysis conditions and suppress behavior, so a quiet run does not prove safety.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Packing or obfuscation:** Packing and obfuscation alter representation to hinder inspection; their presence alone does not prove malicious intent.
- **C — False positive investigation:** An alert must be assessed against context and corroborating evidence before being treated as confirmed malicious behavior.
- **D — Living off the land:** An attacker can misuse legitimate installed tools, so a trusted tool name alone does not establish benign intent.

Coverage: M07; CEH v5 domain 3; Evasion and uncertainty.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q012

**Answer: D — Preserve relevant evidence**

Preservation retains necessary logs, volatile data or artifacts before actions that could destroy them, where operational safety permits.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Contain the affected system:** Containment limits further harm or spread while preserving the ability to investigate.
- **B — Recover and verify:** Recovery restores trusted service and checks that business function and security controls operate as expected.
- **C — Eradicate the cause:** Eradication removes malicious components and the access or weakness that enabled the incident.

Coverage: M07; CEH v5 domain 3; Response priorities.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q013

**Answer: C — Trojan**

A Trojan presents an apparently useful or legitimate function while carrying hidden malicious behavior.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Ransomware:** Ransomware denies access to data or systems, commonly through encryption, and demands payment; some campaigns also steal data.
- **B — Worm:** A worm can propagate between systems without needing to attach itself to an ordinary host file.
- **D — Virus:** A virus replicates by attaching to a host file or similar carrier and depends on that host's execution or activation.

Coverage: M07; CEH v5 domain 3; Malware classes.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q014

**Answer: C — Botnet participation**

A bot joins a group of compromised devices controlled to perform coordinated activity.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Keylogging:** Keylogging captures keystrokes and can expose entered secrets or sensitive content.
- **B — Command and control:** Command-and-control communication lets an external controller coordinate or task an implanted component.
- **D — Fileless execution:** Fileless techniques emphasize memory or existing interpreters and system facilities; they can still leave observable artifacts.

Coverage: M07; CEH v5 domain 3; Malware behavior.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q015

**Answer: D — Memory analysis**

Memory analysis inspects volatile state such as loaded modules, processes and in-memory content.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Network analysis:** Network analysis studies communications, destinations, protocols and timing rather than relying only on file contents.
- **B — Static analysis:** Static analysis inspects a sample's code or structure without intentionally executing its behavior.
- **C — Dynamic analysis:** Dynamic analysis observes behavior while a sample runs in an appropriately controlled environment.

Coverage: M07; CEH v5 domain 3; Analysis methods.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q016

**Answer: B — Reputation checking**

Reputation uses previously collected trust or threat information about an indicator; an unknown reputation is not proof of safety.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Signature detection:** Signature detection matches known patterns; unseen or changed implementations may evade a particular signature.
- **C — Allowlisting:** Allowlisting permits only approved software or behavior under a defined policy, reducing the execution set.
- **D — Behavior-based detection:** Behavior-based detection looks for suspicious actions or sequences rather than only exact file patterns.

Coverage: M07; CEH v5 domain 3; Detection approaches.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q017

**Answer: B — Living off the land**

An attacker can misuse legitimate installed tools, so a trusted tool name alone does not establish benign intent.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — False positive investigation:** An alert must be assessed against context and corroborating evidence before being treated as confirmed malicious behavior.
- **C — Packing or obfuscation:** Packing and obfuscation alter representation to hinder inspection; their presence alone does not prove malicious intent.
- **D — Sandbox awareness:** A sample may detect analysis conditions and suppress behavior, so a quiet run does not prove safety.

Coverage: M07; CEH v5 domain 3; Evasion and uncertainty.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q018

**Answer: D — Eradicate the cause**

Eradication removes malicious components and the access or weakness that enabled the incident.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Recover and verify:** Recovery restores trusted service and checks that business function and security controls operate as expected.
- **B — Contain the affected system:** Containment limits further harm or spread while preserving the ability to investigate.
- **C — Preserve relevant evidence:** Preservation retains necessary logs, volatile data or artifacts before actions that could destroy them, where operational safety permits.

Coverage: M07; CEH v5 domain 3; Response priorities.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q019

**Answer: A — Ransomware**

Ransomware denies access to data or systems, commonly through encryption, and demands payment; some campaigns also steal data.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Trojan:** A Trojan presents an apparently useful or legitimate function while carrying hidden malicious behavior.
- **C — Worm:** A worm can propagate between systems without needing to attach itself to an ordinary host file.
- **D — Virus:** A virus replicates by attaching to a host file or similar carrier and depends on that host's execution or activation.

Coverage: M07; CEH v5 domain 3; Malware classes.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q020

**Answer: A — Fileless execution**

Fileless techniques emphasize memory or existing interpreters and system facilities; they can still leave observable artifacts.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Keylogging:** Keylogging captures keystrokes and can expose entered secrets or sensitive content.
- **C — Botnet participation:** A bot joins a group of compromised devices controlled to perform coordinated activity.
- **D — Command and control:** Command-and-control communication lets an external controller coordinate or task an implanted component.

Coverage: M07; CEH v5 domain 3; Malware behavior.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q021

**Answer: A — Network analysis**

Network analysis studies communications, destinations, protocols and timing rather than relying only on file contents.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Dynamic analysis:** Dynamic analysis observes behavior while a sample runs in an appropriately controlled environment.
- **C — Memory analysis:** Memory analysis inspects volatile state such as loaded modules, processes and in-memory content.
- **D — Static analysis:** Static analysis inspects a sample's code or structure without intentionally executing its behavior.

Coverage: M07; CEH v5 domain 3; Analysis methods.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q022

**Answer: C — Allowlisting**

Allowlisting permits only approved software or behavior under a defined policy, reducing the execution set.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Reputation checking:** Reputation uses previously collected trust or threat information about an indicator; an unknown reputation is not proof of safety.
- **B — Behavior-based detection:** Behavior-based detection looks for suspicious actions or sequences rather than only exact file patterns.
- **D — Signature detection:** Signature detection matches known patterns; unseen or changed implementations may evade a particular signature.

Coverage: M07; CEH v5 domain 3; Detection approaches.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q023

**Answer: D — False positive investigation**

An alert must be assessed against context and corroborating evidence before being treated as confirmed malicious behavior.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Packing or obfuscation:** Packing and obfuscation alter representation to hinder inspection; their presence alone does not prove malicious intent.
- **B — Living off the land:** An attacker can misuse legitimate installed tools, so a trusted tool name alone does not establish benign intent.
- **C — Sandbox awareness:** A sample may detect analysis conditions and suppress behavior, so a quiet run does not prove safety.

Coverage: M07; CEH v5 domain 3; Evasion and uncertainty.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q024

**Answer: B — Recover and verify**

Recovery restores trusted service and checks that business function and security controls operate as expected.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Eradicate the cause:** Eradication removes malicious components and the access or weakness that enabled the incident.
- **C — Contain the affected system:** Containment limits further harm or spread while preserving the ability to investigate.
- **D — Preserve relevant evidence:** Preservation retains necessary logs, volatile data or artifacts before actions that could destroy them, where operational safety permits.

Coverage: M07; CEH v5 domain 3; Response priorities.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q025

**Answer: D — Virus**

A virus replicates by attaching to a host file or similar carrier and depends on that host's execution or activation.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Worm:** A worm can propagate between systems without needing to attach itself to an ordinary host file.
- **B — Trojan:** A Trojan presents an apparently useful or legitimate function while carrying hidden malicious behavior.
- **C — Ransomware:** Ransomware denies access to data or systems, commonly through encryption, and demands payment; some campaigns also steal data.

Coverage: M07; CEH v5 domain 3; Malware classes.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q026

**Answer: A — Fileless execution**

Fileless techniques emphasize memory or existing interpreters and system facilities; they can still leave observable artifacts.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Botnet participation:** A bot joins a group of compromised devices controlled to perform coordinated activity.
- **C — Keylogging:** Keylogging captures keystrokes and can expose entered secrets or sensitive content.
- **D — Command and control:** Command-and-control communication lets an external controller coordinate or task an implanted component.

Coverage: M07; CEH v5 domain 3; Malware behavior.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q027

**Answer: A — Static analysis**

Static analysis inspects a sample's code or structure without intentionally executing its behavior.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Memory analysis:** Memory analysis inspects volatile state such as loaded modules, processes and in-memory content.
- **C — Dynamic analysis:** Dynamic analysis observes behavior while a sample runs in an appropriately controlled environment.
- **D — Network analysis:** Network analysis studies communications, destinations, protocols and timing rather than relying only on file contents.

Coverage: M07; CEH v5 domain 3; Analysis methods.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q028

**Answer: C — Reputation checking**

Reputation uses previously collected trust or threat information about an indicator; an unknown reputation is not proof of safety.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Allowlisting:** Allowlisting permits only approved software or behavior under a defined policy, reducing the execution set.
- **B — Behavior-based detection:** Behavior-based detection looks for suspicious actions or sequences rather than only exact file patterns.
- **D — Signature detection:** Signature detection matches known patterns; unseen or changed implementations may evade a particular signature.

Coverage: M07; CEH v5 domain 3; Detection approaches.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q029

**Answer: B — Packing or obfuscation**

Packing and obfuscation alter representation to hinder inspection; their presence alone does not prove malicious intent.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Living off the land:** An attacker can misuse legitimate installed tools, so a trusted tool name alone does not establish benign intent.
- **C — False positive investigation:** An alert must be assessed against context and corroborating evidence before being treated as confirmed malicious behavior.
- **D — Sandbox awareness:** A sample may detect analysis conditions and suppress behavior, so a quiet run does not prove safety.

Coverage: M07; CEH v5 domain 3; Evasion and uncertainty.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

### CEH26-M07-Q030

**Answer: D — Eradicate the cause**

Eradication removes malicious components and the access or weakness that enabled the incident.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Contain the affected system:** Containment limits further harm or spread while preserving the ability to investigate.
- **B — Preserve relevant evidence:** Preservation retains necessary logs, volatile data or artifacts before actions that could destroy them, where operational safety permits.
- **C — Recover and verify:** Recovery restores trusted service and checks that business function and security controls operate as expected.

Coverage: M07; CEH v5 domain 3; Response priorities.
Technical references: [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/) · [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)
