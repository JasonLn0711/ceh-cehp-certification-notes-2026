不用從我正在念的 M05 開始做。可以依照你的安排來做規劃。目前我們 在 uuu 上的 CEH 課程，是從 M01 開始，共五次上課，現在已經上了一次課，內容是 M01 to M03 。
可以。既然 UUU 的五次課程第 1 次已經完成 M01–M03，我建議不要重新從頭平均念 20 章，而是採「課堂負責廣度，我們的複習負責考試權重、知識連結與弱點修補」。

我重新核對了目前 EC-Council 官方資料：CEH v13 Knowledge Exam 仍是 125 題、4 小時；官方 Blueprint v5.0 把 125 題精確分配到各 subdomain。([EC-Council][1]) 這也是我下面規劃的主要依據，而不是網路 dumps。

另外一個重要策略是：EC-Council 自己說 CEH 涵蓋 4,000+ tools、550 attack techniques。([EC-Council][2]) 所以「把所有工具背完」是錯誤策略。我們應該背的是：

> 攻擊目的 → 原理 → protocol/port → technique → 常見 tool → command 特徵 → 結果 → countermeasure

這比背工具名稱有效很多。

## 一、我會把 20 個 Module 這樣處理

「深學」不是代表官方題數比較多，而是代表這些章節有較高的知識依賴性：學懂之後會幫助其他章節。「穩拿」則是題數一樣重要，但通常比較適合用辨識、比較與 scenario practice 建立分數。

| M  | Module                        | 官方約題數 | 我的讀法     | 第一輪要抓住的東西                                                | 建議自學 |
| -- | ----------------------------- | ----: | -------- | -------------------------------------------------------- | ---: |
| 01 | Ethical Hacking               |     7 | 穩拿       | CIA、attack phases、laws、controls、threat terminology       |  30m |
| 02 | Footprinting & Recon          |     7 | 深學       | passive/active recon、WHOIS、DNS、OSINT、Google dorking      |  45m |
| 03 | Scanning Networks             |     7 | **深學++** | TCP、port states、Nmap、host/service/OS discovery           |  55m |
| 04 | Enumeration                   |     7 | **深學++** | SMB、SNMP、LDAP、NFS、DNS、SMTP enumeration                   |  55m |
| 05 | Vulnerability Analysis        |     6 | 深學       | CVE/CVSS/CWE、scanner、false positive、assessment workflow  |  45m |
| 06 | System Hacking                |     6 | **深學++** | password attacks、privilege escalation、persistence、logs   |  60m |
| 07 | Malware Threats               |     7 | 深學       | virus/worm/trojan/ransomware/rootkit/fileless、analysis   |  45m |
| 08 | Sniffing                      |     6 | **深學++** | ARP、MAC、DHCP、DNS poisoning、Wireshark                     |  55m |
| 09 | Social Engineering            |     6 | 穩拿       | phishing、spear phishing、vishing、smishing、impersonation   |  30m |
| 10 | DoS/DDoS                      |     6 | 穩拿       | SYN flood、amplification、botnet、reflection                |  30m |
| 11 | Session Hijacking             |     6 | 深學       | session/token/cookie、TCP vs application hijacking        |  35m |
| 12 | IDS/Firewall/Honeypot Evasion |     6 | **深學++** | IDS vs IPS、firewall、NAC、fragmentation、evasion            |  45m |
| 13 | Web Servers                   |     6 | 深學       | server attack surface、misconfiguration、patching、Nikto    |  40m |
| 14 | Web Applications              |     6 | **深學++** | auth/authz、XSS、CSRF、SSRF、input validation、Burp           |  60m |
| 15 | SQL Injection                 |     6 | **深學++** | UNION/error/blind/time-based、sqlmap、defenses             |  55m |
| 16 | Wireless                      |     6 | 深學       | 802.11、WEP/WPA/WPA2/WPA3、WPS、Aircrack-ng                 |  40m |
| 17 | Mobile                        |     6 | 穩拿       | Android/iOS、root/jailbreak、ADB、MDM                       |  30m |
| 18 | IoT & OT                      |     6 | 穩拿       | IoT/ICS/SCADA、MQTT、CoAP、Modbus                           |  30m |
| 19 | Cloud                         |     6 | 深學       | IaaS/PaaS/SaaS、IAM、containers、serverless、misconfig       |  40m |
| 20 | Cryptography                  |     6 | **深學++** | symmetric/asymmetric/hash/PKI/TLS/signature/certificates |  55m |

官方 Blueprint 本身確認了 M01 約 7 題、M02–M04 各約 7 題；M05 約 6、M06 約 6、M07 約 7。 M08–M12 各約 6 題，整個 Network & Perimeter Hacking domain 約占 24%，是最大的 domain。 M13–M15 各約 6 題、合計約 14%；M16 約 5%，M17–18 合計約 10%，M19、M20 各約 5%。

因此有個很重要的結論：

**不要把「深學」誤解成「其他章節可以放棄」。**

CEH 的 module 題數其實異常平均，最低大約 6 題、最高大約 7 題。我的優先級主要是在決定「哪裡值得花更多時間建立真正的理解」。

---

## 二、你現在的位置：Class 1 已完成 M01–M03

我不建議現在立刻一路自己讀到 M20。

最好的節奏是：

**UUU 課堂稍微走在前面 → 你在課後把剛學內容壓實 → 再預習下一個核心 module。**

這樣老師講第二次時，你會從「第一次接觸」變成「第二次 encoding」。

你之前給自己設定 CEH 每週最多約 240 分鐘，我會保留這個限制，而不是因為考試逼近就無限制增加。

### Cycle 1：現在 → 第二次 UUU 課程

你的任務不是重讀 M01–M03。

這一輪重點是：

| 工作                                                   |       時間 |
| ---------------------------------------------------- | -------: |
| M01 retrieval：不看講義自己講 hacking lifecycle、CIA、controls |      20m |
| M02：Recon / Footprinting 整理                          |      35m |
| **M03：Nmap + TCP/IP + scanning 深入**                  |  **50m** |
| **預習 M04 Enumeration**                               |  **55m** |
| Ports / protocols flashcards                         |      30m |
| M01–M04 mixed questions                              |      50m |
| **合計**                                               | **240m** |

現在最值得投入的是 **M03 → M04 的界線**。

你應該能清楚回答：

> Reconnaissance、Scanning、Enumeration 到底差在哪？

例如：

```text
Recon
↓
知道 example.com 是目標
找到 DNS、WHOIS、employee names

Scanning
↓
發現 192.0.2.10 活著
22、80、445 ports open
可能是 Windows Server

Enumeration
↓
進一步詢問 SMB
得到 usernames、shares、domain information
```

這個 distinction CEH 後面會一直反覆使用。

---

## 三、接下來五個 Study Cycles

UUU 實際第二到第五堂怎麼分 Module，我們暫時不用猜；你的私人學習路線採這個 sequence。

| Cycle | 核心                              | 原因                                                |
| ----- | ------------------------------- | ------------------------------------------------- |
| 1     | **M01–M04**                     | 把已上過的 M01–03 固化，預習 Enumeration                    |
| 2     | **M05–M08**                     | vulnerability → exploitation → malware → sniffing |
| 3     | **M09–M12**                     | 完整吃掉 Network & Perimeter domain                   |
| 4     | **M13–M16**                     | Web + SQLi + Wireless                             |
| 5     | **M17–M20 + cumulative review** | Mobile/IoT/Cloud/Crypto + 全科整合                    |

這個順序不是隨便按教材。

它其實建立一條 causal chain：

```text
Recon
 ↓
Scanning
 ↓
Enumeration
 ↓
Vulnerability Analysis
 ↓
System Hacking
 ↓
Persistence / Malware
 ↓
Network attacks
 ↓
Defense evasion
 ↓
Web / Application attacks
 ↓
Wireless / Mobile / IoT / Cloud
 ↓
Cryptography
```

你最後看到 scenario 時，要能判斷「攻擊者現在位於哪一階段」，而不是只記得某個工具出現在某一頁。

---

# 四、CEH 第一批真正要背的 Ports

我不建議一次背 60 個。

先做到下面這批看到號碼可以在 1–2 秒內反應：

|      Port | Protocol   | CEH connection                  |
| --------: | ---------- | ------------------------------- |
|     20/21 | FTP        | file transfer / enumeration     |
|        22 | SSH        | secure remote login             |
|        23 | Telnet     | plaintext remote login          |
|        25 | SMTP       | mail / enumeration              |
|        53 | DNS        | footprinting / enumeration      |
|     67/68 | DHCP       | DHCP attacks                    |
|        69 | TFTP       | unauthenticated/simple transfer |
|        80 | HTTP       | web                             |
|        88 | Kerberos   | AD authentication               |
|       110 | POP3       | email                           |
|       123 | NTP        | enumeration / amplification     |
|       135 | RPC        | Windows enumeration             |
|   137–139 | NetBIOS    | Windows enumeration             |
|       143 | IMAP       | email                           |
|   161/162 | SNMP       | **very important enumeration**  |
|       389 | LDAP       | directory enumeration           |
|       443 | HTTPS      | TLS/web                         |
|       445 | SMB        | **very important**              |
|       636 | LDAPS      | encrypted LDAP                  |
|      1433 | MSSQL      | SQL Server                      |
|      1521 | Oracle     | database                        |
|      2049 | NFS        | Unix/Linux shares               |
|      3306 | MySQL      | database                        |
|      3389 | RDP        | Windows remote desktop          |
|      5432 | PostgreSQL | database                        |
|      5900 | VNC        | remote desktop                  |
| 5985/5986 | WinRM      | Windows remote management       |
| 5060/5061 | SIP        | VoIP                            |

不要背成：

> 161 = SNMP

要背成：

> **UDP 161 → SNMP query → community string → device information → enumeration**

這樣一道題換成 scenario，你仍然會做。

---

# 五、Commands：目前只需要先攻 M03/M04

你現在剛學完 M03，所以我會要求這些先達到「看到 command 就知道它在幹嘛」。

| Command            | 意義                        |
| ------------------ | ------------------------- |
| `nmap -sn`         | host discovery            |
| `nmap -sS`         | TCP SYN scan              |
| `nmap -sT`         | TCP connect scan          |
| `nmap -sU`         | UDP scan                  |
| `nmap -sV`         | service/version detection |
| `nmap -O`          | OS detection              |
| `nmap -A`          | aggressive detection      |
| `nmap -p`          | specify ports             |
| `nmap -Pn`         | skip host discovery       |
| `nslookup` / `dig` | DNS queries               |
| `whois`            | registration information  |
| `snmpwalk`         | SNMP enumeration          |
| `nbtstat`          | NetBIOS information       |
| `smbclient`        | SMB interaction           |
| `enum4linux`       | SMB/Windows enumeration   |
| `showmount -e`     | NFS exports               |

公開的 CEH v13 lab notes也可以看到 M03 練習高度集中在 Nmap host discovery、SYN/TCP/UDP scans、service detection、OS fingerprinting 與 firewall/IDS evasion；這與官方 M03 blueprint 相當吻合。([GitHub][3])

但我不要求你現在死背 command syntax。

例如：

```bash
nmap -sS -sV -O 192.0.2.10
```

你至少要立即讀得出：

```text
-sS
→ TCP SYN scan

-sV
→ identify service/version

-O
→ OS fingerprinting
```

---

# 六、我會怎麼處理「考古題」

這裡我要改變我們的策略。

網路上確實有號稱幾百甚至上千題的「312-50v13 actual questions」，但來源、版本、答案正確性以及是否真的來自考試都無法可靠驗證。我不會拿那些數字告訴你「SQLi 最近出了 13 題」之類的假精確統計。

我們改用三層證據：

**最高權重：Official Blueprint**

決定「哪些內容一定在考試範圍內、官方預計多少題」。

**第二層：合法 original practice tests**

拿來觀察 CEH 題目的 scenario 表達方式。例如目前有 2026 practice tests 明確表示題目是自行編寫、不是 brain dump，題型會要求從情境判斷 reconnaissance、rainbow tables、ARP spoofing 等概念。([Training Camp][4])

**第三層：你的錯題**

到後期，這反而最重要。

假設你第一次 125-question mock：

```text
M03  7/7
M04  3/7
M06  3/6
M14  5/6
M20  2/6
```

那我們完全不應該再按照官方權重平均讀。

下一輪：

```text
M04  ↑↑↑
M06  ↑↑↑
M20  ↑↑↑

M03  幾乎不讀
M14  少量維持
```

這才會逐漸變成真正個人化的 preparation system。

---

# 七、每一章最後只產生一張「CEH Card」

我建議我們接下來不要把 CEH 筆記無限膨脹。

每個 Module 最後都壓縮成：

```text
M03 — Scanning Networks

PURPOSE
找到 live hosts / ports / services / OS

CORE CONCEPTS
TCP handshake
port states
scan types

PROTOCOLS / PORTS
...

TOOLS
Nmap
Masscan
hping3

COMMANDS
-sS
-sT
-sU
-sV
-O
...

ATTACK / TECHNIQUE
...

COUNTERMEASURE
...

COMMON CONFUSIONS
-sS vs -sT
open vs filtered
scan vs enumeration

10–20 QUESTIONS
錯題原因
```

20 個 Module 最後就是 **20 張 cards**。

而不是 2,500 頁教材再讀一次。

---

## 你現在的具體 Definition of Done

你目前不要碰 M05–M20 的細節。

先把第一階段完成到：

**M01–M04。**

尤其這四件事必須做到：

> M01：能講出 ethical hacking lifecycle
> M02：能分 passive / active reconnaissance
> M03：能讀懂基本 Nmap scan 與 TCP port states
> M04：知道 SMB / SNMP / LDAP / NFS / SMTP / DNS 分別能 enumerate 什麼

做到之後，再正式進入：

**M05 → M06 → M07 → M08。**

這比現在直接開始背 20 章的工具名稱有效得多。

而且從考試角度看，光 M01–M04 就大約是 **28 / 125 = 22.4%** 的題目；你第一堂 UUU 課已經碰到其中 M01–M03，所以目前最有投資報酬率的動作其實不是向後狂衝，而是先把這一段真正變成可以取分的知識。

[1]: https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh-v13-north-america/?utm_source=chatgpt.com "Certified Ethical Hacker (CEH) | #1 Ethical Hacking Certification | EC-Council"
[2]: https://ethicalhacking.eccouncil.org/?utm_source=chatgpt.com "World's No.1 Ethical Hacking Training Course Online | EC-Council"
[3]: https://github.com/Shivam-kumar-jha/CEH-v13-Lab-Notes?utm_source=chatgpt.com "GitHub - Shivam-kumar-jha/CEH-v13-Lab-Notes: Personal CEH v13 lab notes — Scanning, Enumeration & beyond · GitHub"
[4]: https://trainingcamp.com/ceh-practice-test/?utm_source=chatgpt.com "Free CEH Practice Test 2026 (312-50 v13) | Training Camp"
