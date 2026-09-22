# CEH 課後整合、五循環與自學配置 — 2026-09-22

**目前先鞏固已上課的 M01–M03，接到 M04 Enumeration；不用從 M05 重新開始。** Jason 確認 UUU CEH 共五次課、已完成第一次，內容為 M01–M03，並授權依本分析詳細規劃；原文分鐘數只作重要性參考。以下是現行課程路徑的執行細化，實際學習仍需起始時間、剩餘容量及本人結果。

[完整原文／收件與查核](../source/2026-09-22-course-synced-review/README.md) · [9/18 現行總路徑](uuu-aligned-ceh-cehp-2026-09-18.md) · [官方比重分析](../curriculum/ceh-blueprint-weights-2026-09-22.md) · [Ports／commands 完整核對](../notes/2026-09-22-course-synced-review/ports-and-commands.md) · [個人覆蓋](../assessment-governance/course-coverage-2026-09-18.md)

## 1. 已知進度與規劃權限

- 9/22 本人回報：第一堂由 M01 開始，教到 M03；依既有正式課表，對應 CEH 2053 的 9/20 第一堂。這是**本人回報的出席與模組範圍**；不能推定所有子題均已講完、獨立精熟或已完成 Lab。
- 後四堂日期沿用正式紀錄：10/4、10/18、10/25、11/1。第二至第五堂實授章節仍未知；五個私人 Study Cycles 不等於五堂教師課程。
- 學習主線：課堂提供範圍與案例，課後用提取、情境題、概念連接和有證據的修正，把剛學內容轉成可解釋與可應用的能力。先處理已開的題組與錯題；M04 是下一個預習核心。
- 稀缺資源：注意力、自學時間、先備理解及可信的學員證據。CEH repo 擁有詳細筆記／題目／實作；Planning 擁有日期、容量、狀態與下一關。
- 原文 20 章分鐘加總 **880 分鐘（14 小時 40 分）**。這是相對投入建議，並未納入每題解析、三變式修正、實作、Blog 等完整成本，不把它當成全課完成估計或另加 880 分鐘任務。

## 2. 學習單位：從目的到反制

每個新概念用這條提問鏈整理：

**目的 → 原理 → protocol／transport／port → technique → tool → command 特徵 → 可觀察結果 → 證據限制 → countermeasure。**

原文已有目的到反制的鏈；此處加上 transport 與證據限制，避免把數字、工具名稱或掃描結果直接等同弱點。EC-Council 頁面宣傳 4,000+ 工具與 550+ 技術，支持課程範圍很廣；它沒有提供「全部工具必背」的清單，也沒有證明特定記憶法的效果。[官方課程說明](https://ethicalhacking.eccouncil.org/)

範例：UDP 161 → SNMP 查詢 → 可取得哪些管理物件 → 身分驗證／存取控制 → 列舉結果 → 暴露範圍與防護。Community string 屬 v1／v2c 情境，不能泛化為全部 SNMP；v3 要辨識安全機制。完整技術細節由[ports／commands](../notes/2026-09-22-course-synced-review/ports-and-commands.md)管理。

## 3. 二十章的重要性與讀法

「深學++／深學／穩拿」保留為原文的教學分類，不是官方難度、已測量依賴性或保證得分。「穩拿」在執行上指辨識、比較與情境判讀，同樣保留完整覆蓋。右欄均為**參考權重分鐘，不是配額**；所有模組題數由[官方配置](../curriculum/ceh-blueprint-weights-2026-09-22.md)追溯。

| M | 模組 | v5 題數 | 原文讀法 | 第一輪核心與連接 | 參考分鐘 |
| --- | --- | ---: | --- | --- | ---: |
| 01 | Ethical Hacking | 7 | 穩拿 | CIA、生命週期、法律、控制、威脅詞彙；所有實作先有授權 | 30 |
| 02 | Footprinting & Recon | 7 | 深學 | 主動／被動、WHOIS／DNS／OSINT／搜尋語法；連 M03 的可驗證線索 | 45 |
| 03 | Scanning Networks | 7 | 深學++ | TCP、port states、Nmap、host／service／OS；輸出與推論分開 | 55 |
| 04 | Enumeration | 7 | 深學++ | SMB／SNMP／LDAP／NFS／DNS／SMTP；服務細節與授權條件 | 55 |
| 05 | Vulnerability Analysis | 6 | 深學 | CVE／CVSS／CWE、scanner、false positive、評估流程；連 M03／M04 證據 | 45 |
| 06 | System Hacking | 6 | 深學++ | 密碼攻擊、提權、持久化、logs；區分權限與觀察 | 60 |
| 07 | Malware Threats | 7 | 深學 | virus／worm／trojan／ransomware／rootkit／fileless、分析與防護 | 45 |
| 08 | Sniffing | 6 | 深學++ | ARP／MAC／DHCP／DNS poisoning、Wireshark；連 P3 流量判讀 | 55 |
| 09 | Social Engineering | 6 | 穩拿 | phishing／spear phishing／vishing／smishing／impersonation；條件與反制 | 30 |
| 10 | DoS／DDoS | 6 | 穩拿 | SYN flood、amplification、botnet、reflection；可用性與防護 | 30 |
| 11 | Session Hijacking | 6 | 深學 | session／token／cookie、TCP 與應用劫持；連 M14 驗證／授權 | 35 |
| 12 | IDS／Firewall／Honeypot Evasion | 6 | 深學++ | IDS／IPS、firewall／NAC、fragmentation／evasion；可見性限制 | 45 |
| 13 | Web Servers | 6 | 深學 | attack surface、misconfiguration、patching、Nikto；主機與應用分層 | 40 |
| 14 | Web Applications | 6 | 深學++ | auth／authz、XSS／CSRF／SSRF、input validation、Burp；session 與輸入邊界 | 60 |
| 15 | SQL Injection | 6 | 深學++ | UNION／error／blind／time-based、sqlmap、防禦；語法與資料分離 | 55 |
| 16 | Wireless | 6 | 深學 | 802.11、WEP／WPA／WPA2／WPA3／WPS、Aircrack-ng；認證與密碼學 | 40 |
| 17 | Mobile | 6 | 穩拿 | Android／iOS、root／jailbreak、ADB／MDM；裝置與應用信任邊界 | 30 |
| 18 | IoT & OT | 6 | 穩拿 | IoT／ICS／SCADA、MQTT／CoAP／Modbus；可用性與實體安全 | 30 |
| 19 | Cloud | 6 | 深學 | IaaS／PaaS／SaaS、IAM、containers／serverless、misconfiguration | 40 |
| 20 | Cryptography | 6 | 深學++ | symmetric／asymmetric／hash／PKI／TLS／signature／certificates；跨模組先備 | 55 |
| 合計 | 20 模組 | 125 | 教學參考 | 實際熟悉度尚未測量 | 880 |

M03／M04／M06／M08／M12／M14／M15／M20 可優先用「解釋機制＋判讀情境」補先備；不因此跳過其他章。M20 的必要 TLS／hash 概念可以提前按需補充，不需等 Cycle 5 才首次接觸。各模組完整題本仍在[既有 600 題](../assessments/practice-bank/README.md)，不複製另一份題庫。

## 4. Cycle 1：9/22 至第二堂課的可縮小工作包

目標是鞏固 M01–M03 並建立 M04 入門判讀。原文的 20＋35＋50＋55＋30＋50＝240 分鐘已占滿一週上限，未另列修正、實作與 Blog。因此本次把它調整為**跨 W39／W40、最多 240 分鐘的第一階段工作包**；每週其他 CEH／CEHP 已用時間照常扣除，這不是每週再加 240 分鐘。

### 工作包上限：內容與活動只計一次

| 工作 | 原文分鐘 | 本次參考上限 | 預期保留結果 |
| --- | ---: | ---: | --- |
| M01 retrieval | 20 | 15 | 用自己的話說授權／lifecycle／CIA／controls，指出一個未清楚處 |
| M02 整合 | 35 | 25 | 主動／被動案例與 DNS／登記資訊的證據限制 |
| M03 機制與輸出判讀 | 50 | 40 | TCP、port states、九個 Nmap 選項的目的及限制 |
| M04 預習 | 55 | 40 | 六項服務可列舉什麼、權限條件與觀察限制 |
| Ports／protocol 情境提取 | 30 | 20 | 先關聯核心服務，再補完整表；不以 1–2 秒作驗收門檻 |
| 既有 M01–M04 題目／原題解析 | 50 | 40 | 實際答到的 ID、choice、confidence、assistance；組可跨日 |
| 必要補教／三變式複測 | 未分列 | 25 | 原題分數不變，保存已做／待做複測 |
| P1／P2 相關受控實作或阻塞 | 未分列 | 15 | 本人輸出與宣告檢查，或權限／環境／時間阻塞 |
| Card 整理、本人 Blog 解釋／確認與收尾 | 未分列 | 20 | 一張在用摘要、下一步；文章依實際驗收保持 partial／published |
| 合計 | 240 | 240 | 上限，不是完成時間保證 |

上述章節時間是概念理解與提取，題目／解析、複測、實作、文章整理分別計在活動列；同一分鐘只記一列。40 分鐘題目預算不能保證答完 40 題；複測或寫作超過預留時，先減未啟動的預習／延伸工具內容，再保留剩餘缺口。不得壓縮必要修正來湊新題數，也不以加時填滿表格。

### 日期候選窗：先核對可用，再啟動

| 日期 | 候選上限 | 當次焦點與具體下一步 | 容量條件 |
| --- | ---: | --- | --- |
| 9/22 | 25 分 | 先核對未答組；M01 retrieval＋M02 主動／被動；記一個弱點 | TA 18:20–21:30、Seminar 缺稿與恢復優先 |
| 9/23 | 25 分 | M03 TCP／open／closed／filtered，讀一段既有輸出 | FinTech、MGMT30096 草稿、Seminar 55 分優先 |
| 9/24 | 25 分 | M03 選項判讀與已開題組；若卡住便只修正 | 幹細胞／HAI 與課務優先 |
| 9/25–28 | 0 分新增配置 | 保護連假／恢復，不搬入未完成債務 | 沿用既有非工作界線 |
| 9/29 | 25 分 | M04：SMB／SNMP／LDAP 的資料與權限 | TA、已用週額度與恢復優先 |
| 9/30 | 25 分 | M04：NFS／SMTP／DNS，連 ports／protocols | FinTech、課務交付優先 |
| 10/1 | 25 分 | M01–M04 已開題組與錯題；按需要回查章節 | HAI 與既有課務優先 |
| 10/2 | 25 分 | 補教／retests，整理本人 Card 與文章說明 | Seminar 70 分與交件檢查優先 |
| 10/3 | 40 分 | P1／P2 最小實作、四項入門 gate 與第二堂問題清單 | 先確認可用性；25＋15 分兩段，第二段須新 endpoint |
| 10/4 | 25 分 | 第二堂實授模組／疑問收件，決定下一個循環 | CEH 09:00–18:00、通勤與恢復；課日最多 25 分 |
| 合計 | 240 分 | W39 候選 75；W40 候選 165 | 未確認的可用時間仍是未知 |

這是可調整的執行提案，不是固定鐘點或已預約時段。每次實際可用量取「該日候選上限、每週 240 扣已用、本人確認可用量」最小值；任一必要值未知先確認，不把未知當零已用或全部可用。開始即記 endpoint，最後幾分鐘保存實際成果。若今天已無空檔，保留下一題，不擠壓 TA 或重排睡眠。

日期窗與上方工作包是**同一批時間的兩個視角**，不可相加成 480 分鐘。未完成只帶一個具體問題／下一題到下次正常區塊，第二堂後重新排序；不承諾 10/4 前一定精熟，也不把 10/4 課後分鐘用作課前完成證據。

### 最小 25 分鐘執行法

預設 3 分鐘核對前題／目標，12 分鐘聚焦概念或已開題組，7 分鐘解析／必要修正，3 分鐘保存結果與下一步，共 25 分鐘；可依阻塞調整，不強迫在一次完成十題。若本次重點是實作或本人文章說明，直接替換中間內容，總長不變。題目／選項／提示維持專業英文，解釋用 plain English。

十題首答／信心、必要修正與本人確認且驗證公開的雙語 Blog 仍是既有 daily completion 要件；本工作包的 20 分鐘寫作／收尾只是預留，無法保證每個啟動日完成文章。到 endpoint 未達成即記 partial，不變更驗收、不增加連假補寫。Card 是摘要材料，不自動等於 Blog。

## 5. 五循環：私人的進展框架

| Cycle | 核心與原文參考分鐘合計 | 對應既有週路徑／檢查點 | 主要驗收與下一步 |
| --- | --- | --- | --- |
| C1 | M01–M04：185 | W39–W40；10/4 第二堂收件 | 下節四項入門 gate；M01–M03 是本人回報已授、M04 是預習 |
| C2 | M05–M08：205 | W41–W42；依 10/4／10/18 實授調整 | findings→適用性／風險，權限、malware 類型、封包判讀；接 P1/P3/P4 |
| C3 | M09–M12：140 | W43；10/18／10/25 收件 | 社交工程／可用性／session／防護差異；回接 C2 M08 才涵蓋完整 D4 |
| C4 | M13–M16：195 | W44 起；11/1 結課檢查 | server／app／SQLi 分層、wireless 認證；接 P5 與所需 M20 先備 |
| C5 | M17–M20：155 | W44–W48；穿插全科修正與 CEHP | Mobile／IoT／OT／Cloud／Crypto，跨域案例與未覆蓋子題；11/29 首輪檢查 |

原文 C3 說「完整吃掉 Network & Perimeter」，本次補明它還包含 C2 的 M08。五循環依既有週架構連接，C4／C5 在 W44 都有入門覆蓋需求；目前沒有速度證據保證一週完成八章，若未完成即列缺口並在 W45–W48 的既有空間重排，不加週工時。11/1 與 11/29 是檢查點；600 題和五類個人實作目標保持，預估是否可達仍為 unknown／有容量風險。

原文 causal chain 以 Recon、Scanning、Enumeration、Vulnerability、System、Persistence／Malware、Network、Evasion、Web、Wireless／Mobile／IoT／Cloud 到 Cryptography 串接。這是**教學關聯圖**，不是所有攻擊必須依序發生的因果律；Cryptography 是跨域先備，Enumeration 得到資料也不等於已證明可利用弱點。

當授課提前到後段章節，保留該堂疑問與最低先備，不以 C1 尚未精熟阻止課堂收件；個人深挖仍集中於一個未解 gate。原文「目前不要碰 M05–M20 細節」採作避免額外廣度的預設，必要的 M20／M05 概念橋可以按當前問題使用。

## 6. Recon／Scanning／Enumeration：第一階段的中心問題

| 階段 | 原文例子 | 能支持什麼 | 不能直接推定 |
| --- | --- | --- | --- |
| Recon | example.com、DNS、WHOIS、employee names | 得到可能的資產、組織與服務線索 | 資料仍新、資產全部屬同一主體或已有測試授權 |
| Scanning | 192.0.2.10；22／80／445 open；可能 Windows | 依方法觀察到主機／port 回應；服務／OS 是待核對線索 | 開埠就是弱點、445 就必然 Windows、filtered 就 closed |
| Enumeration | 向 SMB 查詢 usernames／shares／domain | 在該服務、權限與設定下取得可用的具體資料 | 所有 SMB 均匿名列出使用者、已取得存取權或可利用性 |

這三者可重疊：Scanning 是主動偵察的一種，service detection 也可蒐集服務資訊；教學上用「目的與證據細度」區分，不宣稱工具彼此互斥。example.com 與 192.0.2.10 是文件示例，此處僅解讀，不執行網路掃描。

M04 最小服務矩陣：

| 服務 | 可能查得的資料（視授權與配置） | 必須能說出的限制 |
| --- | --- | --- |
| SMB | shares、server／domain、部分帳號資訊 | 認證、權限及伺服器策略會限制列舉 |
| SNMP | 管理物件、裝置／介面資訊 | v1/v2c community 與 v3 安全機制不同 |
| LDAP | 允許查詢的目錄物件／屬性／群組 | bind、ACL、查詢範圍與 transport 保護 |
| NFS | export／分享資訊 | showmount/MOUNT 與 NFSv4-only 可見性不同 |
| SMTP | 伺服器功能、依配置回應的帳號線索 | VRFY／EXPN 可停用，回覆不是郵件身分的充分證明 |
| DNS | 指定記錄、權威／服務線索 | 普通查詢不等於允許完整 zone transfer |

[完整 28 組 ports 與 16 組 commands](../notes/2026-09-22-course-synced-review/ports-and-commands.md)補 transport、來源與適用條件。先把 53／135／137–139／161–162／389／445／636／2049／25 與 M03/M04 情境連起來，其餘按章節補齊；不把全表變成新增每日背誦量。

## 7. 題目、錯題與自適應配置

三層證據各司其職：官方 blueprint 決定範圍及配置；已核准原創練習提供題型與觀念診斷；本人回答／信心／錯題決定下一個修正。後者對個人排序最直接，但一次小樣本不足以證明永久精熟。

原文模擬分數完整保留為**合成例子**：M03 7/7、M04 3/7、M06 3/6、M14 5/6、M20 2/6。它支持優先檢查 M04／M06／M20 的錯因；M03／M14 則可減少重複、保留少量延遲提取。沒有 Jason 的實際作答，不寫入 attempt log，也不因 7/7 就永久停止複習。

每個正常區塊用以下排序，不建立假精確加權分數：

1. 先處理未解授權／安全概念、已開題組及必需複測。
2. 在當前循環中處理擋住後續理解的先備與實授問題。
3. 補尚未覆蓋的官方範圍；同等條件下才參考本表的重要性。
4. 已穩定答對且信心合理的題目減少重複，用後續混題確認保持度。
5. 每次保存實際耗時、已答 ID、錯因與剩餘複測，於既有週回顧重估；超出容量就顯示 at risk，不追加新題債務。

既有每週 60 題／後段目標與 600 題總目標保留為覆蓋目標，**不是這個 240 分鐘工作包保證完成的數量**。C1 可先使用 M01–M04 各章原有 Q001–Q010 的未答題作核心覆蓋，再依結果決定後續；避免已做過的題重新計入。十題一組可跨日，必要三變式與原分數分開。

[Training Camp](https://trainingcamp.com/ceh-practice-test/)自述有 50 道原創情境題與解析、90 分鐘計時；這支持它的產品自述，不是獨立驗證題目品質、授權或正式考試代表性。本次不引入它的 50 題作新目標，先重用[本庫 600 題與兩份 mocks](../assessments/practice-bank/README.md)。[公開 GitHub lab notes](https://github.com/Shivam-kumar-jha/CEH-v13-Lab-Notes)可核對作者如何整理 M03/M04，但作者的完成記號不是 Jason 的實作，技術定義仍追到工具／協定官方文件。

## 8. CEH Card：每章一張入口，逐步形成

把 Card 放在既有模組筆記的一個摘要段落，或當前學習紀錄中；到該模組時才補，不預建二十份空檔。完整來源、例子與訂正留在原筆記；Card 壓縮的是入口，不刪除追溯資料。

```text
MODULE / PURPOSE
CORE CONCEPTS
PROTOCOLS / TRANSPORT / PORTS
TOOLS / COMMAND FEATURES
TECHNIQUE / OBSERVABLE RESULT / LIMIT
COUNTERMEASURE
COMMON CONFUSIONS
QUESTION IDS / ORIGINAL CHOICE + CONFIDENCE / ERROR REASON
RETEST LINKS / OPEN GATE / NEXT ACTION
SOURCE / LAST CHECKED
```

原文列的 PURPOSE、CORE CONCEPTS、PROTOCOLS/PORTS、TOOLS、COMMANDS、ATTACK/TECHNIQUE、COUNTERMEASURE、COMMON CONFUSIONS、10–20 QUESTIONS 都保留其用途。「10–20 QUESTIONS」在本次執行上改成**連結既有題目 ID／錯因**，不再出另一套 200–400 題。

M03 的起始摘要（**編輯準備稿，待 Jason 自己解釋**）：目的為發現可觀察主機／ports／services／OS 線索；核心為 TCP handshake、scan types 與六種 Nmap port states。工具先取 Nmap；原文提及 Masscan／hping3 只保留為延伸索引，未增加安裝或實作。選項連到 ports／commands 參考；易混淆為 SYN／connect、open／filtered、scan／enumeration。反制可連分段、限制不必要服務及監測；辨識工具輸出仍不能證明弱點。接[既有 M03 題本](../assessments/practice-bank/m03.md)與[完整 M03 筆記](../notes/2026-09-20-ceh-week-01/plain-english/m03-network-scanning.md)，本人答案／錯因目前留空。

## 9. C1 入門 gate 與完成界線

| Gate | Jason 應留下的可觀察成果 | 維持開放的條件 |
| --- | --- | --- |
| M01 | 用自己的話說一個 ethical-hacking lifecycle，連到授權、目的、證據與回報 | 只背階段名、無法區分授權／範圍 |
| M02 | 對一個情境解釋 passive／active recon，說出資訊來源與直接互動差別 | 把所有 DNS 或公開資料取得一律視為被動且無風險 |
| M03 | 讀懂提供的基本 Nmap 選項與 open／closed／filtered，解釋 -Pn、-A 的邊界 | 把 OS 推測當事實、把 filtered 當關閉或 -Pn 當隱形 |
| M04 | 說出 SMB／SNMP／LDAP／NFS／SMTP／DNS 各可查的資訊及至少一個條件 | 把可查資訊一概視為匿名可得或已證明可利用 |

C1 入門 gate 支持往 C2 移動；它不等於四章全部子題完成、600 題首輪完成、CEHP 實作通過、正式考試準備度或 daily Blog 完成。題目與三變式修正依原契約保存；沒有實際回答時四項仍為 planned。M01–M04 的官方配置合計 28／125＝22.4%，此數值可描述覆蓋，不能單獨量化投資報酬率。

下次可直接開啟[現行 tutor prompt](professor-prompt-uuu-aligned-2026-09-18.md)，帶入本人確認的剩餘時間、已開題組與這份 C1 計畫。先記一個實際結果或阻塞，再決定是否續做。保持五堂課收件與個人證據各自更新。

## 10. 原文全覆蓋與再利用

| 原文區段 | 保存／解釋位置 |
| --- | --- |
| 不從 M05 開始、Class 1 M01–M03 | §1；本人回報與後四堂未知分開 |
| 125 題／4 小時／blueprint 與 4,000+／550 | §2、官方比重筆記、來源回執 |
| 20 章分類／核心／30–60 分建議 | §3 全 20 列，880 分僅作參考 |
| Cycle 1 原 240 分、M03→M04 | §4、§6；重分活動並給日期候選窗 |
| 五循環與 causal chain | §5；補 D4 包含 M08、M20 先備和課堂自適應 |
| 28 組 ports、SNMP 情境 | ports／commands 全表＋§2／§6 |
| 16 組 commands、Nmap 示例 | ports／commands 全表與來源核對；只解讀 |
| 三層題目證據、合成 mock 分數 | §7；完整保留，無個人成績寫入 |
| 一章一卡、M03 範例與 10–20 題 | §8；摘要模板與既有題目引用 |
| 四項 DoD、28／125、下一循環 | §9；入門 gate 與其他驗收分開 |
| 四個原始引用與查核限制 | 完整原文／來源回執；原網址不改寫 |

[Planning 今日](../../planning-everything-track/weeks/2026-W39/days/2026-09-22.md#ceh-course-synced-review) · [W39](../../planning-everything-track/weeks/2026-W39/weekly-plan.md#ceh-course-synced-review) · [W40](../../planning-everything-track/weeks/2026-W40/weekly-plan.md#ceh-course-synced-review) · [CEH 專案入口](../../planning-everything-track/data/projects/2026-07-ceh-cehp-certification-training.md#ceh-course-synced-review)。
