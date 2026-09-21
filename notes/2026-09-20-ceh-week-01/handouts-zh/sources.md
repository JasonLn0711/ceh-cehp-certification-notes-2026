# 兩份中文講義來源表與本次核對界線

[中文筆記總覽](README.md) · [講義一](part-01.md) · [講義二](part-02.md)

Jason 於 2026-09-21 對話貼入兩份講義；本次將其重組為完整主題筆記，沒有把原文重新命名為逐字錄音。對話貼文是本次收件來源；此資料夾不是原文逐字副本。原先 9/20 保存的兩份 audited Markdown 是另一層來源，保持原檔不動，見[原始收件與雜湊](../../../source/2026-09-20-ceh-week-01/README.md)。本次沒有取得新錄音、白板、PCAP 或學員輸出。

H1/H2 分開編號，保留原講義兩組各自從 1 開始的引用，避免混成同一個 `[1]`。68 個來源條目不等於 68 個唯一網址；重複來源保留各自位置。下表是使用者所附引用的完整路由，除明列 live check 者外，不宣稱本次重新閱讀或獨立驗證全文。原文對該來源的引用也不自動代表來源支持附近每一句補充；例如 H1-26 的 threat 頁，風險定義應連 H2-07。Diamond Model 本次依講義及既有查核記錄整理，不新增原始論文已讀的主張。

<a id="live-checks"></a>
## 2026-09-21 選定來源 live checks（Asia/Taipei）

此工作是來源整理中的五項核對，未執行學員實驗，也未宣告完整週研究或全部 68 條重新查核完成。

| 來源 | 本次實際支持的範圍 | 未涵蓋 |
| --- | --- | --- |
| [EC-Council CEH](https://cert.eccouncil.org/certified-ethical-hacker.html) | 官方頁仍列 312-50、125 題、4 小時；各試卷 cut score 範圍 60%–85% | 個人 voucher、退款、實驗室到期與報考權益 |
| [Nmap host discovery](https://nmap.org/book/man-host-discovery.html) | 本地 Ethernet 的 ARP／ND 行為可優先於其他 `-P*` 選項；`-sn` 不執行後續一般 port scan | 未驗本機版本、權限、封包或目標狀態 |
| [Apache core](https://httpd.apache.org/docs/2.4/mod/core.html) | ServerSignature 控制產生頁面的 footer；ServerTokens 控制 Server response header，Prod 範例仍顯示 Apache | 未修改或測試任何部署 |
| [NIST SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | 官方列 April 2025，取代 Rev.2；將事件應變整合進 CSF 2.0 風險管理 | 非組織應變合規驗收 |
| [ICO DUAA](https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/the-data-use-and-access-act-2025-what-does-it-mean-for-organisations/) | DUAA 修正而非取代 UK GDPR、DPA 2018、PECR | 未聲稱每條規定都同日生效或適用本地個案 |

## 講義一：33 個來源

| 代號 | 原講義引用來源 |
| --- | --- |
| H1-01 | [EC-Council CEH](https://cert.eccouncil.org/certified-ethical-hacker.html) |
| H1-02 | [MDN Internet mechanics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/How_does_the_Internet_work) |
| H1-03 | [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) |
| H1-04 | [OWASP session management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) |
| H1-05 | [NIST IDS](https://csrc.nist.gov/glossary/term/intrusion_detection_system) |
| H1-06 | [NIST honeypot](https://csrc.nist.gov/glossary/term/honeypot) |
| H1-07 | [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) |
| H1-08 | [OWASP SQL injection prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) |
| H1-09 | [NIST OT security SP 800-82r3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) |
| H1-10 | [NIST cloud computing](https://csrc.nist.gov/glossary/term/cloud_computing) |
| H1-11 | [NIST encryption](https://csrc.nist.gov/glossary/term/encryption) |
| H1-12 | [NIST asymmetric key cryptography](https://csrc.nist.gov/glossary/term/asymmetric_key_cryptography) |
| H1-13 | [NIST virtual machine](https://csrc.nist.gov/glossary/term/virtual_machine) |
| H1-14 | [Parrot documentation](https://parrotsec.org/docs/) |
| H1-15 | [Microsoft AD DS overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview) |
| H1-16 | [NIST TDEA SP 800-67r2](https://csrc.nist.gov/pubs/sp/800/67/r2/final) |
| H1-17 | [NIST confidentiality](https://csrc.nist.gov/glossary/term/confidentiality) |
| H1-18 | [NIST integrity](https://csrc.nist.gov/glossary/term/integrity) |
| H1-19 | [NIST hash function](https://csrc.nist.gov/glossary/term/hash_function) |
| H1-20 | [NIST availability](https://csrc.nist.gov/glossary/term/availability) |
| H1-21 | [NIST authenticity](https://csrc.nist.gov/glossary/term/authenticity) |
| H1-22 | [NIST non-repudiation](https://csrc.nist.gov/glossary/term/non_repudiation) |
| H1-23 | [NIST digital signature](https://csrc.nist.gov/glossary/term/digital_signature) |
| H1-24 | [NIST vulnerability](https://csrc.nist.gov/glossary/term/vulnerability) |
| H1-25 | [NIST compromise](https://csrc.nist.gov/glossary/term/compromise) |
| H1-26 | [NIST threat](https://csrc.nist.gov/glossary/term/threat) |
| H1-27 | [MITRE ATT&CK FAQ](https://attack.mitre.org/resources/faq/) |
| H1-28 | [NIST passive attack](https://csrc.nist.gov/glossary/term/passive_attack) |
| H1-29 | [NIST active attack](https://csrc.nist.gov/glossary/term/active_attack) |
| H1-30 | [MITRE T1195 supply chain compromise](https://attack.mitre.org/techniques/T1195/) |
| H1-31 | [NIST rules of engagement](https://csrc.nist.gov/glossary/term/rules_of_engagement) |
| H1-32 | [ShellGPT upstream](https://github.com/TheR1D/shell_gpt) |
| H1-33 | [OWASP prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) |

## 講義二：35 個來源

| 代號 | 原講義引用來源 |
| --- | --- |
| H2-01 | [CIS Cyber Kill Chain](https://www.cisecurity.org/insights/spotlight/ei-isac-cybersecurity-spotlight-cyber-kill-chain) |
| H2-02 | [MITRE ATT&CK FAQ](https://attack.mitre.org/resources/faq/) |
| H2-03 | [NIST information assurance](https://csrc.nist.gov/glossary/term/information_assurance) |
| H2-04 | [Microsoft security groups](https://learn.microsoft.com/en-us/windows/win32/ad/how-security-groups-are-used-in-access-control) |
| H2-05 | [Microsoft ACL](https://learn.microsoft.com/en-us/windows/win32/secauthz/access-control-lists) |
| H2-06 | [Microsoft DACL evaluation](https://learn.microsoft.com/en-us/windows/win32/secauthz/how-dacls-control-access-to-an-object) |
| H2-07 | [NIST risk](https://csrc.nist.gov/glossary/term/risk) |
| H2-08 | [OWASP threat modeling](https://owasp.org/www-community/Threat_Modeling) |
| H2-09 | [NIST incident response SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) |
| H2-10 | [European Commission obligations](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/obligations_en) |
| H2-11 | [Google supervised learning](https://developers.google.com/machine-learning/intro-to-ml/supervised) |
| H2-12 | [PCI SSC applicability FAQ](https://www.pcisecuritystandards.org/faqs/1092/) |
| H2-13 | [ISO 27001](https://www.iso.org/standard/27001) |
| H2-14 | [ISO certification](https://www.iso.org/certification.html) |
| H2-15 | [HHS covered entities](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html) |
| H2-16 | [HHS Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html) |
| H2-17 | [SEC audit record retention](https://www.sec.gov/rules-regulations/2003/01/retention-records-relevant-audits-reviews) |
| H2-18 | [US Copyright Office DMCA](https://www.copyright.gov/dmca/) |
| H2-19 | [EUR-Lex GDPR](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679) |
| H2-20 | [European Commission individual rights](https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en) |
| H2-21 | [ICO DUAA 2025](https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/the-data-use-and-access-act-2025-what-does-it-mean-for-organisations/) |
| H2-22 | [Tor key management](https://support.torproject.org/about-tor/how-tor-works/key-management/) |
| H2-23 | [Bitcoin privacy](https://bitcoin.org/en/protect-your-privacy) |
| H2-24 | [ICANN RDAP transition](https://www.icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en) |
| H2-25 | [RFC 1035 DNS](https://www.rfc-editor.org/rfc/rfc1035) |
| H2-26 | [RFC 5321 SMTP](https://www.rfc-editor.org/rfc/rfc5321) |
| H2-27 | [RFC 9293 TCP](https://www.rfc-editor.org/rfc/rfc9293.html) |
| H2-28 | [Nmap host discovery](https://nmap.org/book/man-host-discovery.html) |
| H2-29 | [Nmap port states](https://nmap.org/book/man-port-scanning-basics.html) |
| H2-30 | [Nmap scan techniques](https://nmap.org/book/man-port-scanning-techniques.html) |
| H2-31 | [Nmap version detection](https://nmap.org/book/man-version-detection.html) |
| H2-32 | [Nmap OS detection](https://nmap.org/book/man-os-detection.html) |
| H2-33 | [RFC 8900 IP fragmentation](https://www.rfc-editor.org/rfc/rfc8900.html) |
| H2-34 | [Apache core directives](https://httpd.apache.org/docs/2.4/mod/core.html) |
| H2-35 | [RFC 2827 source filtering](https://www.rfc-editor.org/rfc/rfc2827.html) |

## 英文合併檔引用對照

[英文來源收件與引用表](../../../source/2026-09-21-ceh-merged-plain-english/README.md#citation-register)逐一列出 66 個唯一網址、英文來源行號與本表 H1／H2 編號。英文有 88 處 inline 引用，本表有 68 個分篇條目，唯一網址集合一致；不同數量反映編排而非新增查核來源。
