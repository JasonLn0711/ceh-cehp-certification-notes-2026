# Recurring distinctions, ports and command reading

[Collection index](README.md) · [All items](items.csv) · [Key audit](quality-audit.md)

These tables synthesize the supplied scenarios. An observation supports the stated mechanism only under its prerequisites. Use the item notes to recover exact source wording, marked answers and qualifications.

## Evidence and assessment

| Distinction | Evidence that separates them | Source examples |
| --- | --- | --- |
| Authorized activity / actor color | Owner permission, scope and stop conditions establish authority; a color label is informal | Bank Q1/Q54/Q189; Mock 03 Q124 |
| Scanner result / exploitable weakness | Applicable build/configuration, reachable feature, required access and an authorized reproducible proof | Bank Q75/Q231/Q427/Q438 |
| CVSS severity / local risk | Versioned vector versus exposure, asset criticality, threat evidence and business consequence | Bank Q451; Mock 03 Q29 |
| Remediation / verification | Changing the system versus retesting the changed condition | Bank Q108/Q296; Mock 01 Q22 |
| Credentialed / internal | Successful host authentication versus where the scanner runs | Bank Q246/Q275; Mock 02 Q115 |
| True positive / false positive | Alert matches verified attack versus verified benign activity | Mock 02 Q10; Bank Q204/Q350 |
| Prepared notes / learner result | Source/annotation existence versus an actual answer or independently executed operation | Existing assessment workflow; no attempt is generated here |

## Credentials, sessions and access

| Mechanism | Essential cue | Common confusion |
| --- | --- | --- |
| Password spraying | Few guessed passwords across many accounts | Credential stuffing reuses known pairs |
| Credential stuffing | Breached/reused username-password pairs | A high success rate alone does not prove the source of passwords |
| Pass-the-hash | Compatible hash-derived authentication without cracking | A captured challenge-response is not the underlying NT hash |
| Pass-the-ticket | Reuse of Kerberos tickets | Kerberoasting is a different offline-guessing path |
| Session fixation | Attacker-known value exists before victim login and survives it | Stolen post-login tokens are replay/sidejacking |
| Session prediction | Weak generation/entropy permits anticipating a valid value | Unequal token lengths do not establish weak encryption |
| CSRF | Browser uses the victim's session for an unwanted action | It need not steal or alter the token |
| IDOR/BOLA | Valid identity can access the wrong object after an ID change | Authentication success does not authorize every object |
| Active / blind TCP hijacking | Injection changes the flow / attacker lacks flow visibility | Active does not necessarily mean blind |
| Forged TCP reset | Accepted reset tears down a connection | Termination does not automatically transfer the session |
| Vertical escalation | Standard user gains higher authority | Lateral movement crosses systems and horizontal access crosses same-tier resources |

[Sessions](modules/m11.md) · [Credentials](modules/m06.md) · [API authorization](modules/m14.md)

## Network and protocol reference

Assignments describe common or registered use. Verify the observed protocol and deployment; a listening number alone does not prove the named software or a vulnerability. [IANA registry](references.md#r26) and [Microsoft service transports](references.md#r08) support the relevant assignments.

| Port / transport | Service or role | Interpretation detail |
| --- | --- | --- |
| TCP 21 | FTP control | Data channels have separate active/passive behavior |
| TCP 22 | SSH | An advisory needs an actual affected build/configuration |
| TCP 23 | Telnet | A banner can disclose a claimed OS/software version |
| TCP 25 | SMTP | VRFY/EXPN/RCPT responses may disclose accounts |
| UDP and TCP 53 | DNS | AXFR uses TCP; DNSSEC adds authenticated data, not confidentiality |
| UDP 67/68 | DHCP server/client | Inspect offers/options for rogue DHCP and leases for starvation |
| TCP 80/443 | HTTP/HTTPS | HTTP/3 commonly also uses UDP 443 |
| TCP 102 | ISO-TSAP; used by S7 | Not unique proof of a Siemens PLC model |
| UDP 123 | NTP | Diagnostic/control disclosure depends on daemon policy |
| UDP 137/138; TCP 139 | NetBIOS name/datagram/session | Name-table queries and SMB share enumeration are distinct |
| UDP 161/162 | SNMP queries / notifications | Community-based v1/v2c access is different from SNMPv3 authentication/privacy |
| TCP 389/636 | LDAP / LDAP over TLS | Active Directory also has UDP 389 functionality; query access depends on ACLs |
| TCP 445 | Direct SMB | Anonymous IPC$ and enumeration are policy-dependent |
| TCP 502 | Classic Modbus TCP | Secure variants and deployment safeguards need their own identification |
| TCP 1433 | SQL Server service | Port registration is a lead, not proof of a server version |
| TCP/UDP 1434 | Microsoft SQL Monitor registration | Common SQL Browser behavior and actual transport should be checked |
| TCP/UDP 2049 | NFS deployments | Export discovery, mounting and file access are separate checks |
| TCP 3268/3269 | Global Catalog / Global Catalog over TLS | The mock's UDP 3268 label is held as a source error |
| TCP 5555 | Legacy network ADB mode | Modern pairing/debug modes differ; exposed debugging is a separate control decision |

## Command semantics and transcription repairs

The following are reading references, not commands executed by this capture. Parameter names in angle brackets identify values that an authorized operator would supply. Original command strings remain unchanged in the source attachments.

| Source pattern | What it requests | Qualification or repair |
| --- | --- | --- |
| `nmap -sS` / `-sT` / `-sU` | SYN / OS connect / UDP scanning | All are observable; only suitable raw scans are affected by raw-packet spoofing options |
| `nmap -O` / `-sV` | OS detection / service version probing | A service string is not a complete OS or vulnerability proof |
| `nmap -sn -PE <authorized-range>` | No port scan; request ICMP Echo discovery | Local-link ARP may still be used; no stealth guarantee follows |
| `--spoof-mac 0` / vendor name | Random MAC / matching vendor-prefix MAC for raw Ethernet | MACs are local-link information; `-sT --spoof-mac Dell` does not establish spoofed connect traffic |
| `-T5` | Aggressive timing preset | Faster settings can reduce accuracy and stress services |
| `dig @<dns-server> <authorized-zone> AXFR` | Request a specific zone transfer | Source forms missing the server/zone are incomplete; the query is active |
| `dig +norecurse <name>` | Ask without requesting recursive resolution | Empty NOERROR is not proof that no client recently accessed a name |
| `ldapsearch -H ldap://<authorized-host> -x -s base -b "" "(objectClass=*)" namingContexts` | Query naming contexts from RootDSE | Host URI, base, scope and later search filter are separate; do not reuse a missing-host source form |
| `snmpwalk` / NSE `snmp-processes` | Walk accessible MIB objects / request supported process information | Credentials, agent MIB support and tool version determine results |
| `ntpq -p <authorized-host>` | Display NTP peer associations | Query restrictions and implementation determine availability |
| `nbtstat -A <authorized-ip>` | Query NetBIOS names | Does not enumerate shared folders by itself |
| `route print` | Show Windows local routing table | Different from tracing a remote path |
| `ip.addr == 10.0.0.5` | Wireshark IPv4 display filter | This is not packet-capture filter syntax |
| `nc -l -p 4444` | Traditional netcat listener form | Syntax differs by implementation; no listener was created here |

[Scanning evidence](modules/m03.md) · [Enumeration](modules/m04.md) · [Primary Nmap documentation](references.md#r01) · [OpenLDAP arguments](references.md#r27)

## Web, wireless and cryptography traps

| Pair | Reliable distinction |
| --- | --- |
| Traversal / LFI / RFI | Path escape / local inclusion sink / remote inclusion sink under supported runtime configuration |
| Response splitting / request smuggling | Outbound header/message structure / conflicting inbound framing between parsers |
| XSS / open redirect | Script execution in browser context / navigation to another destination without required script execution |
| Wrapper / dropper / downloader | Bundles programs / places another payload / retrieves another payload; roles can coexist |
| Rogue AP / evil twin | Unapproved AP / additionally impersonates a trusted network |
| WEP / WPA-TKIP / WPA2 / WPA3 | Identify protocol, cipher and AKM rather than infer a generation solely from AES or a handshake |
| KRACK / PSK dictionary attack | Key reinstallation/nonce reuse / offline testing of password candidates |
| RF replay / relay / jamming | Reuse old message / forward live exchange / disrupt communication |
| CRIME / BREACH | TLS/SPDY compression / HTTP response compression under exploitable input/secret conditions |
| Hash / HMAC / signature | Unkeyed digest / shared-key authenticity / private signing with public verification |
| Content encryption / traffic-analysis resistance | Protect plaintext / also address visible sizes, timing and endpoints |
| Cloud backup diversity / tamper protection | Multiple copies / restricted, isolated or immutable write access plus tested recovery |
| Code signing / secure boot / anti-rollback | Package authenticity / verified boot chain / rejecting disallowed older firmware |
| Post-quantum key mechanisms / bulk encryption | Key encapsulation/signatures / symmetric protection of large data; plan the whole lifecycle |

## Worked reading examples

A prelogin session ID survives authentication. The decisive cue is that an attacker can know the ID before the victim signs in, so rotation and invalidation address fixation. TLS protects transport but does not change that lifecycle.

A scanner reports an old service version. Record the claimed version and observed response, then check the actual build/advisory and configuration. A backported fix may leave an old-looking banner; a published exploit may require a disabled feature. Neither the banner nor the exploit listing is the final applicability proof.

A kernel rootkit and a firmware implant both hide activity. A trusted OS rebuild can address the former layer while the latter needs firmware-specific recovery evidence. Repeated OS reinstall success does not establish that every persistence layer is clean.
