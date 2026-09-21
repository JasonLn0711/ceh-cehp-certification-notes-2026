# CEH 兩份中文講義：完整筆記與連結索引

整理：2026-09-21，Asia/Taipei。此補充讓「保護什麼、怎麼出問題、可驗什麼、證據支持什麼、修復如何確認」連成同一條學習路徑。

| 閱讀入口 | 內容 |
| --- | --- |
| [講義一完整筆記](part-01.md) | 11 節：二十模組、實驗室、五要素、風險詞彙、TTP、分類、角色、授權、AI、一頁成果 |
| [講義二完整筆記](part-02.md) | 30 節與收斂案例：管理、偵察、協定、掃描、偽冒與防禦 |
| [概念與跨專案連結](connections.md) | 每個連結的用途、共同機制、證據 owner 與推論界線 |
| [68 個來源條目與選定 live checks](sources.md) | 講義一 33 條、講義二 35 條，獨立編號；五項本次官方核對 |
| [既有英文筆記](../README.md)／[354 主張與 75 段追溯](../coverage.md) | 原始查核稿的詳細英文解釋、claim ID、ASR 與證據狀態 |

## 來源與成果界線

Jason 提供兩份中文教學講義並要求完整筆記及相關連結；Codex 重組為臺灣繁體中文筆記、覆蓋表及連結。此頁日期是收件整理日，原資料夾的 9/20 是先前筆記的 locator，不推論錄音時間或出席。這是中文閱讀補充，保留既有英文筆記及原始 audited copies，並未改寫原始檔。

每節保留定義、機制、例子／更正及結論限制；不是貼文逐字副本。來源清單保存全部引用網址，講義本身的逐字內容以本次對話為來源。校園、公司、銀行、FTP 與 USB 例子均按教學情境閱讀；缺白板、原始命令或結果的內容不補成實測。原講義的「查核更正」屬提供的教學層，只有 sources 中五項明列為本次新查。

本次是教材整理完成，不記錄學員閱讀、題目、信心、分鐘、實作或 Blog 完成；不啟動掃描、研究專案或公開發布。下一步依[現行課程路徑](../../../study-plan/uuu-aligned-ceh-cehp-2026-09-18.md)在既有時段按問題查閱。

## 逐節覆蓋

下表一一對應使用者講義的主節。第一份 §2 另完整涵蓋 M01–M20；第二份 §27 保留七個命令、§28 保留八項機制；末尾掃描判讀另列。這個覆蓋表不取代原有 transcript claim coverage。

### 講義1：11 節

| 原節 | 完整筆記入口 |
| --- | --- |
| 1 | [CEH 的學習目標與基礎詞彙](part-01.md#h1-01) |
| 2 | [二十模組的完整概念地圖](part-01.md#h1-02) |
| 3 | [VM、Parrot、AD、實驗室與考試資訊](part-01.md#h1-03) |
| 4 | [五個安全要素與數位簽章](part-01.md#h1-04) |
| 5 | [Attack、Vulnerability、Exploit、Compromise、Threat、Risk](part-01.md#h1-05) |
| 6 | [弱點來源與 TTP](part-01.md#h1-06) |
| 7 | [五類攻擊與防守問題](part-01.md#h1-07) |
| 8 | [帽色、紅藍隊與行為者歸因](part-01.md#h1-08) |
| 9 | [授權到修復的八步流程](part-01.md#h1-09) |
| 10 | [AI-assisted Hacking 與提示詞注入](part-01.md#h1-10) |
| 11 | [能力收斂與可重用的一頁成果](part-01.md#h1-11) |

### 講義2：30 節

| 原節 | 完整筆記入口 |
| --- | --- |
| 1 | [Cyber Kill Chain、ATT&CK 與 Diamond Model](part-02.md#h2-01) |
| 2 | [Information Assurance 與持續調整](part-02.md#h2-02) |
| 3 | [Defense in Depth：互補控制與共同失效](part-02.md#h2-03) |
| 4 | [SID、ACL、NTFS 與離線磁碟](part-02.md#h2-04) |
| 5 | [Risk 與變更管理](part-02.md#h2-05) |
| 6 | [CTI、SOC、CVE 與情報生命週期](part-02.md#h2-06) |
| 7 | [Threat Modeling：資料流與信任邊界](part-02.md#h2-07) |
| 8 | [Incident Management 與升級／揭露](part-02.md#h2-08) |
| 9 | [監督式、非監督式與偵測錯誤](part-02.md#h2-09) |
| 10 | [法律、標準與認證的用途](part-02.md#h2-10) |
| 11 | [Footprinting、Reconnaissance 與主動／被動](part-02.md#h2-11) |
| 12 | [搜尋工具觀察面的差別](part-02.md#h2-12) |
| 13 | [Competitive Intelligence 與 OSINT](part-02.md#h2-13) |
| 14 | [Dark Web、Tor、Bitcoin](part-02.md#h2-14) |
| 15 | [WHOIS、RDAP、DNS 與地理線索](part-02.md#h2-15) |
| 16 | [Traceroute、TTL、CDN](part-02.md#h2-16) |
| 17 | [Email Headers 與來源證據](part-02.md#h2-17) |
| 18 | [社交工程與資訊暴露對策](part-02.md#h2-18) |
| 19 | [RDP、VM、Terminal、Shell、root](part-02.md#h2-19) |
| 20 | [Host、Port、Service、Socket](part-02.md#h2-20) |
| 21 | [Packet、Header、Payload、MTU](part-02.md#h2-21) |
| 22 | [TCP、UDP 與可靠性的層次](part-02.md#h2-22) |
| 23 | [TCP Flags、三向交握、FIN](part-02.md#h2-23) |
| 24 | [Host Discovery：ARP 與 ICMP](part-02.md#h2-24) |
| 25 | [Port States、Connect Scan、SYN Scan](part-02.md#h2-25) |
| 26 | [Banner、Version、OS、NSE](part-02.md#h2-26) |
| 27 | [七個命令的問題與證據界線](part-02.md#h2-27) |
| 28 | [分片、路由、偽冒、檢查碼](part-02.md#h2-28) |
| 29 | [Proxy、VPN、No-logs](part-02.md#h2-29) |
| 30 | [防禦措施的精確保護範圍](part-02.md#h2-30) |

另見[講義二收斂案例](part-02.md#worked-example)：ARP 有回覆／ICMP 沉默／TCP 21 open／FTP 線索的分層判讀。

## 文件品質與可重用性

驗收範圍是主節覆蓋、引用條目、Markdown 路徑／錨點、雙向入口、原始查核稿保持不變，以及未寫入學員成績或操作紀錄。`anti-ai-rhetoric-lint` 未列於本次可用 skills，已依 Planning voice contract 人工檢查語氣與證據邊界，未宣稱該 skill 已執行。這不是完整學習 packet 或新測驗，因此沿用既有題本與驗收，不另生成題庫。

本次實際檢查結果：五份中文文件、41 個主節、20 模組、68 引用條目均通過數量與入口檢查；166 個文件內本地連結及錨點通過，既有文件新增連結亦可解析。兩份原始 audited Markdown 的 SHA-256 仍與收件紀錄相同。兩個 repo 的 `git diff --check` 通過；Planning repository validation 通過（44 項沿用警告、0 項新增），knowledge validation 通過（176 metadata notes／176 catalog entries）。檢查驗證文件結構與來源保留，並不等於所有技術主張重新獨立查核或人工學習驗收。
