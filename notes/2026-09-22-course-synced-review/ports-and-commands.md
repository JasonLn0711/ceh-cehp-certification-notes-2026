# M03–M04：Ports、Protocols 與 Commands 參考

查核日期：2026-09-22（Asia/Taipei）。依[使用者提供的完整原文](../../source/2026-09-22-course-synced-review/source.md)保存 **28 組 port 對照、16 組 command 辨識**，補上傳輸協定與判讀界線。這是課後參考資料；尚未產生 Jason 的作答、掃描或實作證據。

閱讀路徑：攻擊／管理目的 → 協定 → port → 工具／選項 → 回應 → 可支持的判斷 → 防禦。Port 是服務線索，實際服務可改用其他 port，須用回應與設定確認。Nmap 的 `open` 表示有應用程式接受對應連線或封包；它本身不證明存在漏洞。`filtered` 表示探測受阻、無法確定開啟或關閉，不能直接寫成 `closed`。[服務辨識](https://nmap.org/book/man-version-detection.html)、[port 狀態](https://nmap.org/book/man-port-scanning-basics.html)

## 28 組常見 Ports

「常用 transport」以日常服務及考試辨識為主，並非列出 IANA 中每一種註冊傳輸方式。IANA 登錄、產品預設及實際部署是三種不同證據；尤其 Oracle 1521 採 Oracle 文件確認慣例，不能只查登錄名稱就判斷服務。基本對照參考 [IANA 登錄表](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)及 [Microsoft 服務連接埠說明](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements)，特殊情況另附來源。

| # | Port | 服務／常用 transport | M03–M04 連結與辨識重點 |
| ---: | --- | --- | --- |
| 1 | 20/21 | FTP；TCP | 21 為控制通道；主動模式資料通道傳統上由伺服器 TCP 20 發起，被動模式使用協商出的伺服器資料 port；不能把所有 FTP 資料傳輸寫成 20。[FTP 規範](https://www.rfc-editor.org/rfc/rfc959) |
| 2 | 22 | SSH；TCP | 加密遠端登入；與 Telnet 比較傳輸保護。 |
| 3 | 23 | Telnet；TCP | 遠端終端協定；原始 Telnet 本身未提供加密保護。 |
| 4 | 25 | SMTP；TCP | 郵件傳遞；可辨識 SMTP 服務，是否允許特定列舉命令依設定而異。 |
| 5 | 53 | DNS；UDP、TCP | DNS 查詢與名稱解析；TCP 也用於一般 DNS，不能只記「查詢 UDP、zone transfer TCP」。[DNS over TCP](https://www.rfc-editor.org/rfc/rfc7766) |
| 6 | 67/68 | DHCPv4；UDP | 67 伺服器、68 用戶端；理解位址配置與偽造 DHCP 服務情境。 |
| 7 | 69 | TFTP；UDP | 簡單檔案傳輸，原協定沒有使用者驗證；初始請求送至 69，後續傳輸使用協商的 transfer IDs／UDP ports。[TFTP](https://datatracker.ietf.org/doc/html/rfc1350) |
| 8 | 80 | HTTP；TCP | Web 服務線索；能否存取、實際應用與安全性須另外確認。 |
| 9 | 88 | Kerberos；TCP、UDP | 身分驗證，常連結 AD；不要限定成只用 UDP。 |
| 10 | 110 | POP3；TCP | 郵件收取；服務辨識不代表可讀取他人郵件。 |
| 11 | 123 | NTP；UDP | 時間同步；列舉或放大風險仍取決於服務版本、功能及設定。 |
| 12 | 135 | Microsoft RPC Endpoint Mapper；常用 TCP | 用於找出 RPC endpoint；後續 RPC 可能使用動態高位 port，不能把全部 RPC 流量等同 135。 |
| 13 | 137–139 | NetBIOS；137 常用 UDP、138 UDP、139 TCP | 137 名稱服務，138 datagram，139 session；137 另有 TCP 登錄。逐一辨識，不把三個 port 全寫為同一 transport。 |
| 14 | 143 | IMAP；TCP | 郵件存取；與 POP3 的使用模式比較。 |
| 15 | 161/162 | SNMP；通常 UDP | 161 查詢／回應，162 通知接收（trap／inform）；community string 屬 v1/v2c 模型，v3 使用安全模型，不沿用 community string。[SNMP 傳輸](https://www.rfc-editor.org/rfc/rfc3417)、[Net-SNMP 版本選項](https://www.net-snmp.org/docs/man/snmpcmd.html) |
| 16 | 389 | LDAP；通常 TCP；CLDAP／AD 特定查詢可用 UDP | 目錄資訊查詢；可見物件依驗證身分及 ACL 決定。 |
| 17 | 443 | HTTPS；TCP；HTTP/3 使用 QUIC／UDP | TLS 保護傳輸；不能推論 Web 應用沒有漏洞。[HTTP/3](https://www.rfc-editor.org/rfc/rfc9114) |
| 18 | 445 | SMB 直接承載；TCP | 分享與檔案服務；帳號、share、domain 資訊能見度依協定及權限。 |
| 19 | 636 | LDAPS；TCP | 建立 TLS 後交換 LDAP；LDAP 也可在 389 使用 StartTLS，不宜以 389／636 單獨判定全部加密狀態。[LDAP TLS](https://www.rfc-editor.org/rfc/rfc4513) |
| 20 | 1433 | SQL Server Database Engine；TCP 預設執行個體常用 | Named instance 可用其他／動態 port；SQL Server Browser 的 UDP 1434 是另一項服務。[SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/install/configure-the-windows-firewall-to-allow-sql-server-access) |
| 21 | 1521 | Oracle Net Listener；TCP 常見預設 | Listener 可改用其他 port；1521 開啟只提供慣例線索，不能直接證明產品、資料庫可存取或有漏洞。[Oracle Listener](https://docs.oracle.com/en/database/oracle/oracle-database/19/netag/configuring-and-administering-oracle-net-listener.html) |
| 22 | 2049 | NFS；TCP 常見，較舊版本亦可用 UDP | Unix/Linux 網路檔案系統；`showmount` 依賴 MNT 服務，NFSv4-only 可能不提供，空結果不證明沒有 NFS。[showmount 手冊](https://man7.org/linux/man-pages/man8/showmount.8.html) |
| 23 | 3306 | MySQL 傳統 client/server 協定；TCP | 資料庫服務辨識；不涵蓋所有 MySQL 協定／部署 port。[MySQL 連線](https://dev.mysql.com/doc/refman/8.4/en/connecting.html) |
| 24 | 3389 | RDP；TCP、UDP | 遠端桌面；實際可用 transport 依版本與設定。 |
| 25 | 5432 | PostgreSQL；TCP | 資料庫服務常見預設。[PostgreSQL 連線設定](https://www.postgresql.org/docs/current/runtime-config-connection.html) |
| 26 | 5900 | VNC／RFB；TCP 常見 | 遠端畫面；其他 display／部署可使用其他 port。 |
| 27 | 5985/5986 | WinRM；TCP | 預設 HTTP 5985、HTTPS 5986；HTTP transport 不足以獨自判斷訊息是否有其他加密保護，須查驗證與服務設定。[WinRM](https://learn.microsoft.com/en-us/windows/win32/winrm/installation-and-configuration-for-windows-remote-management) |
| 28 | 5060/5061 | SIP；5060 常用 UDP／TCP；5061 TLS over TCP | 通話訊號服務；SIP 訊號與媒體流使用的協定／port 要分開辨識。[SIP](https://www.rfc-editor.org/rfc/rfc3261) |

SNMP 的記憶鏈可寫為「UDP 161 → 查詢 → v1/v2c community 或 v3 安全設定 → 允許取得的裝置資訊 → enumeration」。查到服務只是起點；任何資訊揭露或漏洞判斷都要保留實際回應及權限條件。

## 16 組 Commands：先能讀懂目的與限制

以下保留原文的指令／選項辨識形式。未附 target 的片段不是完整操作程序；本次沒有執行掃描、查詢目標或建立自動化掃描腳本。

| # | 原文 Command | 功能與必要修正 | 一手來源 |
| ---: | --- | --- | --- |
| 1 | `nmap -sn` | Host discovery 後不做 port scan；仍可能發送 ICMP、TCP 或區網 ARP／ND 探測，不能寫成「不發封包」。 | [Host discovery](https://nmap.org/book/man-host-discovery.html) |
| 2 | `nmap -sS` | TCP SYN scan；通常不完成 TCP 三向交握。Unix 通常需 root／等效 raw-packet 權限；半開式不等於不可偵測。 | [Scan techniques](https://nmap.org/book/man-port-scanning-techniques.html) |
| 3 | `nmap -sT` | 透過作業系統 `connect()` 建立 TCP 連線；適用無 raw-packet 權限情境，開啟 port 的連線可完成交握。 | [Scan techniques](https://nmap.org/book/man-port-scanning-techniques.html) |
| 4 | `nmap -sU` | UDP scan；無回應常只能判為 `open\|filtered`，不能直接視為 open 或 closed。 | [Scan techniques](https://nmap.org/book/man-port-scanning-techniques.html) |
| 5 | `nmap -sV` | 發送服務探測以辨識協定、產品與版本；結果是辨識證據，仍需確認適用設定與漏洞條件。 | [Version detection](https://nmap.org/book/man-version-detection.html) |
| 6 | `nmap -O` | 依 TCP/IP stack 回應做 OS fingerprinting；需適當封包權限，結果可能不確定，開啟及關閉 port 的可見性影響辨識。 | [OS detection](https://nmap.org/book/man-os-detection.html)、[Privileges](https://nmap.org/book/man-port-scanning-techniques.html) |
| 7 | `nmap -A` | 啟用 `-O`、`-sV`、預設 NSE scripts（`-sC`）及 traceroute；不包含 `-T4`。需權限的功能僅在權限足夠時啟用；預設 scripts 也需納入授權範圍。 | [Miscellaneous options](https://nmap.org/book/man-misc-options.html)、[NSE](https://nmap.org/book/man-nse.html) |
| 8 | `nmap -p` | 必須接 port 清單或範圍，例如 `-p 22,80,445`；本身不選擇 UDP scan，也不等於全 port。 | [Port specification](https://nmap.org/book/man-port-specification.html) |
| 9 | `nmap -Pn` | 跳過一般 host discovery，把所列目標視為啟用而嘗試後續指定掃描；不是 stealth 開關，也不保證目標存活。區網可能仍需 ARP／ND。 | [Host discovery](https://nmap.org/book/man-host-discovery.html) |
| 10 | `nslookup` / `dig` | 查詢 DNS 記錄；記錄類型、查詢伺服器與回應決定能支持的判斷。一般查詢不等於取得完整 zone。 | [BIND tools](https://bind9.readthedocs.io/en/latest/manpages.html) |
| 11 | `whois` | 取得 WHOIS 服務提供的登錄資訊；不是 DNS 查詢，欄位可能被遮蔽或服務已調整。 | [WHOIS protocol](https://www.rfc-editor.org/rfc/rfc3912) |
| 12 | `snmpwalk` | 沿 OID subtree 逐項取得 SNMP 資訊；需要指定版本及有效安全參數，回應受存取控制限制。v3 不使用 v1/v2c 的 community 參數模型。 | [snmpwalk](https://www.net-snmp.org/docs/man/snmpwalk.html)、[snmpcmd](https://www.net-snmp.org/docs/man/snmpcmd.html) |
| 13 | `nbtstat` | 檢視 NetBIOS over TCP/IP 名稱、cache 或 session；選項決定本機／遠端範圍，`-a` 使用名稱、`-A` 使用 IP。 | [Microsoft nbtstat](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nbtstat) |
| 14 | `smbclient` | SMB 用戶端；可列出服務／shares 或進入 share，視選項與權限而定。它也有檔案寫入功能，不能將整個工具稱為唯讀列舉。 | [Samba smbclient](https://www.samba.org/samba/docs/current/man-html/smbclient.1.html) |
| 15 | `enum4linux` | Windows／Samba 列舉工具，整合 Samba 工具取得多種資訊；版本、選項及目標權限影響輸出，不能保證一定取得 users／shares。 | [Upstream enum4linux](https://github.com/CiscoCXSecurity/enum4linux) |
| 16 | `showmount -e` | 向指定伺服器的 MNT 服務詢問 exports；未指定 host 時查本機。NFSv4-only 不一定暴露 MNT，因此不能用失敗／空輸出判定沒有 NFS。 | [nfs-utils showmount](https://man7.org/linux/man-pages/man8/showmount.8.html) |

## 原文示例的閱讀方式

原文 `nmap -sS -sV -O 192.0.2.10` 的意思是：針對示意位址，組合 TCP SYN scan、服務／版本辨識與 OS fingerprinting。它沒有指定 `-p`，因此不能解讀為全 port；也沒有 `-Pn`，不能說已跳過 host discovery。`192.0.2.10` 位於文件示例用 TEST-NET-1 範圍，本筆記僅解讀字面意義，未對該位址送出探測。[RFC 5737](https://www.rfc-editor.org/rfc/rfc5737)

原文 Recon → Scanning → Enumeration 圖可作學習分層：先找資產線索，再確認可達主機／port／服務，接著向特定協定取得更細資訊。現場工具功能可能跨層；例如 `-sV` 已會與服務互動。只有 22、80、445 open 的資訊不足以確定 Windows Server；需另有 OS／服務辨識證據，SMB 分享也可能由 Samba 提供。

## 完成與證據界線

本次完成 28 組 port 與 16 組 command 的覆蓋核對，以及官方文件／上游手冊查核；IANA CSV 也已核對原文涉及的數字。未測試本機工具安裝、目標服務、實際權限、網路可達性或學員熟練度。當 Jason 能解釋一個情境的目的、所需資訊與輸出限制，再依課程授權環境安排實作並保存結果。

後續閱讀：[完整原文](../../source/2026-09-22-course-synced-review/source.md)、[既有 UUU 課程路線](../../study-plan/uuu-aligned-ceh-cehp-2026-09-18.md)。所有閱讀、練習及整理沿用 CEH／CEHP 共享每週 240 分鐘與課程日最多 25 分鐘的限制。

[五循環、C1 時間配置與驗收](../../study-plan/course-synced-review-2026-09-22.md)將本表接回已授 M01–M03 與 M04 預習；只在實際問題需要時查閱。
