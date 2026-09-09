# Forgotten Portal Discovery — 2026-09-08 開場課筆記

## 來源、日期與證據狀態

- Project：`WP-2026-W37`；學習日：`2026-09-08`（Jason 於 9/9 指定為「昨天的 CEH task」）；保存日：`2026-09-09`，Asia/Taipei。
- Source：Jason 貼入的完整 opening lesson；[原文](opening-lesson-2026-09-08.source.md)完整保存標題、段落、表格、程式區塊、25 筆參考連結與原有語氣。只將聊天外層三引號移除，內容獨立保存。
- 狀態：`source preserved / learning support received`。Jason 提供課程內容，個人指令輸出、ROE 回答、實際時間、scan transcript、teach-back 與測驗分數留待後續實際記錄；weekly project 維持 `planned`。
- 來源包含引用與解釋；本次是 source capture 與本機文件／程式閱讀，引用來源的外部事實沿用 supplied-source attribution。本次未執行新的網路查核、mock、self-test、Nmap、curl 或學習驗收。
- 完整性：原文 285 行、29,731 bytes；SHA-256：`0e9a2930e9cb58302351c6e5ee83e609f439f07b2425a6c83e2827ebe60e9705`。這是保存文字的指紋，證明範圍為本次來源副本，與實驗證據雜湊分開。

## FIRST PRINCIPLE

稀缺資源是 W37 的 `240 min` 學習容量、可追溯的理解與操作證據。CEH repo 保存課程解釋、技術操作、引用、ROE 與未來 learner artifacts；Planning 保存 9/8 學習支援收到的事實、9/9 補記日期、容量與下一關。9/8 的 `70 min` 是既有配置，實際耗時仍待 Jason 記錄；後續執行使用新的真實時段。

本課的核心問題是：實際運行的服務是否與組織登記一致，差異由誰負責？可驗收成果是一張帶證據與責任狀態的 asset map。老師提供的預期、程式定義、實際回應與最後結論各有不同證據來源。

## 1. 授權與 ROE：先決定行動範圍

| 概念 | 本課定義與實際用途 | 判讀界線 |
| --- | --- | --- |
| Authorization／授權 | 有權批准者允許特定活動；本例 learner 為自有 mock 的 owner/operator | 技術可連線與活動授權分別確認 |
| Scope、target、method | 明列目標 `127.0.0.1`、TCP `8765–8767`；讀 register、最多兩次 connect scan、GET `/health` 與 `/service-info` | nearby port、其他 loopback IP、IPv6 或其他 path 需先有修訂授權 |
| Rules of Engagement | 執行前寫出授權者、方法、時段、限額、停止條件、證據保存與恢復責任 | ROE 要在操作前成立，真實日期與時段由 Jason 提供 |
| Request/rate control | 最多兩次掃描是上限；沿用 Nmap local default timing | 本文沒有額外 requests-per-second 數值；一次已足夠時即可停止 |
| Stop condition | 埠衝突、範圍不明、非 loopback、敏感資料、失穩、時段到期 | 保存 blocker，依原邊界停止 |
| Resumption authority | 變更活動前由 owner 寫 dated amendment | 新發現形成下一個授權問題 |
| Evidence handling | 保存 ROE、register、log、metadata、分析、hash 與本人說明 | 教學文字與預期輸出作為支援資料 |

來源：原文 §1、§7、Your first task；參考 [1]。原文的 **“Do not start the mock or run a scan yet.”** 是本次 lesson checkpoint；來源捕捉持續遵守這個步驟順序。

## 2. 資產與所有權：登記是待比對的資料

原始 fictional register 只有 `8765 / public portal / Digital Services` 與 `8767 / observability / Platform Operations`。課程 brief 說 mock 另有一個未登記服務；這項提示保留為 exercise design，learner discovery 由實際輸出建立。

- **Asset／資產**：需要管理或保護的服務、軟硬體或資訊；本例關注 running services。
- **Asset inventory／資產清冊**：供組織決策的資產與屬性紀錄；**service register** 是本例聚焦服務的登記表，支援「檔案記載了什麼」的結論。
- **System owner／service owner**：系統生命週期或特定服務成果的責任角色。**Accountability** 是確保必要決策與工作完成，執行維護的 administrator 可能是另一人。
- **Ownership gap**：可用紀錄中的責任缺口。「本 register 沒有 owner」能由檔案比對支持；全面宣稱沒有人負責需要更多組織證據。
- **Shadow IT**：在正式管理流程以外的業務科技使用。未登記服務提供查證線索，其成因、用途與是否違規各自確認。
- **Attack surface**：可被接觸或嘗試影響的介面集合；listener 的存在支持介面可見性，漏洞與利用另需證據及授權。

真實角色是 Jason 操作自有 mock；fictional owner 是教學情境中的組織責任。兩者在 asset map 分開記錄。來源：原文 §2；參考 [2]–[7]。

## 3. Reconnaissance → scanning → enumeration → validation

| 活動 | 要回答的問題 | 可保存的證據 | 可支持的判斷 |
| --- | --- | --- | --- |
| Passive reconnaissance | 現有資料記了什麼？ | supplied register 副本 | 記載的服務／owner；即時可達性另查 |
| Active reconnaissance | 接觸服務時發生什麼？ | 實際請求與回應 | 對特定介面的主動觀察；read-only GET 仍為 active |
| TCP scanning | 哪些允許埠從這裡可達？ | scan transcript | 當時、該執行環境、該 target 的 TCP reachability |
| Enumeration | 服務回報哪些具體資訊？ | `/service-info` response | claimed role／version／owner metadata |
| Validation | 哪個主張已獲得合適證據？ | 主張所需的原始與獨立紀錄 | metadata returned、actual deployment、owner acceptance 分別驗證 |
| Vulnerability assessment | 哪種弱點有何安全意義？ | 獨立評估資料 | 本 discovery exercise 的後續另案活動 |
| Exploitation | 是否能使用弱點造成效果？ | 明確授權下的獨立證據 | 本課 ROE 明確排除 exploitation、credential testing、brute force 等 |

服務版本是一條 validation lead；服務未登記是一項 inventory/ownership finding 的候選。只有相應的 learner artifacts 到位，才寫成自己的 finding。來源：原文 §3、§5；參考 [8]–[11]。

## 4. 網路概念與證據層次

- **IPv4** 是 32-bit addressing；`127.0.0.1` 是本次唯一允許地址。**Loopback** 回到執行命令所在的 networking environment；host、container、VM 的「本機」需要先辨識。
- **Localhost** 是 hostname，可涉及 IPv4 與 IPv6 `::1`；本課直接保留 ROE 的數字地址，避免改變 target。
- **TCP** 提供 connection-oriented、ordered byte stream；**port** 區分 transport endpoints；**listening socket** 表示等待連入的作業系統端點。
- **TCP three-way handshake**：SYN → SYN-ACK → ACK。`-sT` 請 OS 建立正常 TCP connection；讀 Nmap 的 `open` 與親自保存 packet capture 是兩種不同證據。
- **HTTP GET** 取得 resource representation；read-oriented semantics 容許 server logging 之類副作用。**Endpoint** 在本課指 scheme/address/port/path 組成的 requestable interface。
- 例子 `http://127.0.0.1:8765/service-info` 用來拆解 URL。可使用的 path 只有 `/health`、`/service-info`；health response 支持健康介面回應這一層。
- **Port-number service label** 可由 Nmap lookup table 得到；**banner** 與 metadata 來自服務通訊。兩者來源不同；role、version 與 owner 的真實性各自驗證。

來源：原文 §4；參考 [9]、[12]–[18]。完整定義、例子與原始限定語均保留在 source。

## 5. 證據、provenance 與 integrity

| Artifact／概念 | 回答的問題 | 保存時的注意事項 |
| --- | --- | --- |
| Terminal transcript | 當時終端顯示哪些操作與輸出？ | 與 packet capture、server log 分開 |
| Server log | server 設定會記錄的事件是什麼？ | logging coverage 有限；缺少 log 另需查證 |
| Asset map | 目標、觀察、claimed metadata、owner、gap 與下一步如何對應？ | 每項判斷連到實際 artifact |
| Decision log | 為什麼得出該結論，哪裡仍待驗證？ | 保留假設、推論、授權 gate 與 owner 決策 |
| Provenance | 來源、操作者、環境、時間與處理歷史為何？ | 檔名之外保留可追溯脈絡 |
| Integrity | 與基準紀錄相比，bytes 是否相同？ | 檔案可保持完整但內文仍可能錯誤 |
| SHA-256 | 內容的 256-bit digest | 是內容比對工具；與加密、作者證明、實驗正確性分開 |
| `sha256sum --check` | 計算值是否符合 manifest？ | 信任範圍包含基準 manifest 的 custody；只驗列出的檔案 |

原文揭示的 closeout 問題：教授 prompt 在停止 mock 前 hash，且只列五份 artifact。後續 server.log 的寫入會使舊 hash 失效。文件修正以「關閉產生者 → 等待 log 完成 → 完成所有紀錄 → 產生與驗證 manifest」為順序；新版 manifest 明列 ROE、register 與 decision log。這是未來流程修正，實際 learner hash 結果尚待產生。

結論用語依證據分層：**observation** 是實際看到的內容；**evidence** 支持特定主張；**inference** 帶假設的推論；**finding** 是證據支持的評估；**validation lead** 是待查問題；**proof** 只用於假設明確的限定主張。每次結論都回問：「哪份 artifact 支持這個精確主張，還留下什麼問題？」來源：原文 §5；參考 [19]–[22]。

## 6. 真實事件與 synthetic lab 的連結

| 事件 | 來源所述事實／日期 | 在本課的作用 | 證據界線 |
| --- | --- | --- | --- |
| Equifax ACIS dispute portal | 原文引 FTC complaint：2017-05-13 至 07-30 intrusion、09-07 disclosure；2019-07-22 complaint／settlement announcement；unpatched Struts、patch 通知未達維護者、3/15 scanner coverage 不全、inventory 不準確 | asset visibility → scanner coverage assurance → accountable owner → completion confirmation | complaint 的 allegations 與 mock observation 分開 |
| Equifax detection／segmentation | 原文記載 unrelated databases access、過期憑證妨礙 encrypted traffic inspection、legacy file-integrity monitoring 缺口；FTC announcement 約 147 million 受影響 | 找到資產後還需要治理、偵測與適當隔離 | 人數、機制均屬 supplied-source historical account |
| NASA JPL | 2018-04 發現 compromise；2019-06-18 OIG IG-19-022；未授權 Raspberry Pi、inventory gaps、compromised external-user account、跨網移動、約 500 MB／23 files | inventory-dependent controls 可能漏掉未登記資產 | 原文保留 initial exploit／default-password uncertainty；裝置類型本身是資產資訊 |

Equifax 是本週唯一主 anchor；JPL 是補充案例，留在相同 learning question。Northbridge Learning Clinic 是 fictional instance，隔離 inventory gap 與 owner 問題。原文的 §6 保留 FTC／NASA direct links 與 25 筆完整書目；本次 source capture 不宣稱完成 W37 live research gate。

## 7. 本機對照與採納的文件修正（2026-09-09）

| 項目 | 目前證據 | 對後續操作的作用 |
| --- | --- | --- |
| Mock 檔案 | 本 repo 的 `mock_services.py` 存在；本次靜態閱讀檔案 | 回答 source 最後的檔案存在問題；實際 runtime 仍由新輸出確認 |
| Author self-test | 原 professor prompt 記載 9/8 author validation passed | 保留歷史文字，與 Jason 的 self-test／scan 完成分開 |
| Self-test scope | `self_test()` 呼叫 `start_servers(use_ephemeral_ports=True)`，以 port `0` 取得動態埠，並對該埠 GET | 與 learner 固定埠 ROE 分開；使用前需 dated owner amendment，現有固定埠 learner 路徑先略過此 author check |
| Time wording | README 原為 60 min window；professor prompt／day 為 70 min learning block | 70 min 學習含至多 60 min active window，寫真實起訖；縮短可行，延長須 amendment |
| Metadata wording | README 原將 role/version/owner 稱為 established；lesson 強調 claimed | 改為 returned metadata；組織 ownership 與 deployment truth 各有驗證 |
| Hash sequence／coverage | README 原列四份，prompt 原列五份且關閉順序不同 | 統一七份 artifact；先停服務並完成紀錄，再 hash/check |

本次依 lesson 改善文件的安全性與一致性，保留 mock 程式與原 lesson 原文。完整演練、額外 self-test 與新的 scan window 都等待 Jason 的 learner checkpoint。

## 8. 下一個 learner checkpoint 與容量

下一步由 Jason 用自己的話完成 ROE：授權者、exact target／ports、methods、兩次 ceiling、時間／rate controls、prohibited activities、stop/resume、evidence custody。寫真實的 Asia/Taipei 日期與 70-minute block 起訖，active window 置於其中且至多 60 分鐘；過去的 9/8 時段留作歷史配置，實際恢復使用新日期。

| 狀態 | 後續證據／動作 | Owner／觸發點 |
| --- | --- | --- |
| pending | 本人 ROE teach-back、真實起訖與 scope comprehension | Jason 下次實際學習開場 |
| confirmed-static | `mock_services.py` 存在；self-test 動態埠控制已記錄 | 文件修正完成；執行前核對當時版本 |
| pending | 第一個固定埠 authorized result 或 exact blocker | ROE 與既有 M01 safety gate 成立後 |
| pending | W37 focused live research brief，回答實際 blocker／mechanism | 第一個 action 後，以當時主題與日期建立 `research-briefs/2026-W37.md` |
| pending | register、server/scan logs、metadata、asset map、decision、hash verification、本人解釋 | 依 professor checkpoints 收集 |
| pending | M02–M04 diagnostics；W36 M01 safety repair 的獨立狀態 | learner evidence 到位後評分，沿用 assessment governance |

Red capacity 採一個 25-minute micro-step 保存本人 ROE、register comparison 或第一個允許結果／blocker；實際做過才更新 `attempted`。既有 70-minute 配置、今日 30-minute CEH block 與 weekly 240-minute ceiling 由 Planning 管理，補記本身不增加時數或分數。

## Connection map

- [Weekly mission：授權、檔案、驗收與修正流程](README.md)

- [Professor prompt：既有五個 checkpoint 與教學節奏](professor-prompt-2026-09-08.md)

- [W36 M01 safety prerequisite：維持原週 evidence](../2026-W36-authorization-gate/README.md)

- [Assessment governance：後續診斷沿用既有驗收](../../../assessment-governance/README.md)

- [9/8 daily：原學習日期與 70-minute 配置](../../../../planning-everything-track/weeks/2026-W37/days/2026-09-08.md)

- [9/9 daily：補記與下一關](../../../../planning-everything-track/weeks/2026-W37/days/2026-09-09.md)

- [W37 plan：容量、planned state 與 live research gate](../../../../planning-everything-track/weeks/2026-W37/weekly-plan.md)

- [CEH control-plane locator：課程與證據路徑](../../../../planning-everything-track/data/projects/2026-07-ceh-cehp-certification-training.md)

## Capture validation — 2026-09-09

完整 source 與使用者引文逐字比對通過，25/25 reference definitions 保留；來源 hash 與本頁一致。兩個 repo 共 12 份變更 Markdown 的 87 個本地連結目標存在，兩邊 `git diff --check` 通過。Planning knowledge validation 為 176/176；repository validation 為 44 grandfathered warnings、0 new。這些是文件保存與一致性檢查；mock code 維持原版，learner runtime／實作／診斷結果留在各自驗收層。

## 2026-09-09 continuation

[30-minute M02 professor prompt](professor-prompt-2026-09-09.md) reuses the opening lesson and starts at the unfinished ROE checkpoint. It guides one bounded result/blocker and a diagnostic when ready. The earlier 70-minute plan remains historical; learner state stays `planned` until personal evidence is supplied.
