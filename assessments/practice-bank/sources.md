# Technical source routes

Prepared 2026-09-18. Official UUU scope and current exam-blueprint links were checked during planning. Targeted live searches also checked Nmap, NIST assessment/OT/mobile/WLAN guidance, OWASP injection/session/password guidance, ATT&CK and cloud/Kubernetes documentation. The references below are technical reading routes; a URL listed here is not a claim that every paragraph or every vendor version was individually verified. Recheck version-sensitive behavior before a lab or item revision.

[Course-source verification and limitations](../../source/2026-09-18-uuu-learning-alignment/notes.md) · [Current scope map](../../curriculum/official-scope-map.md)

## M01 — Ethical Hacking

- [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)
- [NIST CSF 2.0](https://www.nist.gov/cyberframework)

M01 standards/law identification references: [European Commission](https://commission.europa.eu/law/law-topic/data-protection/legal-framework-eu-data-protection_en), [PCI SSC](https://www.pcisecuritystandards.org/standards/pci-dss/), [ISO/IEC 27001](https://www.iso.org/standard/27001). The public Commission and standards pages were read on September 18; the direct EUR-Lex page returned a browser challenge, so no claim is made that its full text was retrieved. This is instrument recognition, not an applicability or compliance assessment.

## M02 — Footprinting and Reconnaissance

- [DNS concepts RFC 1034](https://www.rfc-editor.org/rfc/rfc1034)
- [DNS implementation RFC 1035](https://www.rfc-editor.org/rfc/rfc1035)
- [RDAP RFC 9082](https://www.rfc-editor.org/rfc/rfc9082)

## M03 — Scanning Networks

- [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html)
- [Nmap scanning techniques](https://nmap.org/book/man-port-scanning-techniques.html)
- [Nmap host discovery](https://nmap.org/book/man-host-discovery.html)

## M04 — Enumeration

- [LDAP RFC 4511](https://www.rfc-editor.org/rfc/rfc4511)
- [SNMP architecture RFC 3411](https://www.rfc-editor.org/rfc/rfc3411)
- [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

## M05 — Vulnerability Analysis

- [FIRST CVSS](https://www.first.org/cvss/)
- [CWE](https://cwe.mitre.org/)
- [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

## M06 — System Hacking

- [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/)
- [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

## M07 — Malware Threats

- [MITRE ATT&CK Enterprise](https://attack.mitre.org/tactics/enterprise/)
- [NIST malware guide](https://csrc.nist.gov/pubs/sp/800/83/r1/final)

## M08 — Sniffing

- [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/)
- [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)
- [ARP RFC 826](https://www.rfc-editor.org/rfc/rfc826)

## M09 — Social Engineering

- [CISA phishing guidance](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing)
- [MITRE phishing](https://attack.mitre.org/techniques/T1566/)
- [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/115/final)

## M10 — Denial of Service

- [CISA DDoS guidance](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf)
- [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827)
- [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)

## M11 — Session Hijacking

- [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
- [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

## M12 — IDS Firewalls and Honeypots

- [NIST IDPS guidance](https://csrc.nist.gov/pubs/sp/800/94/final)
- [NIST firewall guidance](https://csrc.nist.gov/pubs/sp/800/41/r1/final)

## M13 — Web Servers

- [HTTP semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110)
- [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

## M14 — Web Applications

- [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

## M15 — SQL Injection

- [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

## M16 — Wireless Networks

- [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final)
- [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security)
- [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

## M17 — Mobile Platforms

- [OWASP MASVS](https://mas.owasp.org/MASVS/)
- [NIST enterprise mobile guidance](https://csrc.nist.gov/pubs/sp/800/124/r2/final)

## M18 — IoT and OT

- [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final)
- [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html)
- [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252)
- [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

## M19 — Cloud Computing

- [AWS shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/)
- [Kubernetes security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/)
- [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

## M20 — Cryptography

- [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
- [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html)
- [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final)
- [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

## Source use

Question scenarios and wording are original. These links support mechanisms and scope; they are not copied question sources. Public primary references support technical facts, the provider establishes course scope, and only learner records establish competence. Legacy protocols are taught for recognition with their limits, not recommended for new deployments.
