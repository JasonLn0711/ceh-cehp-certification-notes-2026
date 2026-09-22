# CEH 20 章考試比重、版本與複習判斷

查核日：2026-09-22（Asia/Taipei）。用途：回答「哪些章節考得較多、能否從考古題推估分布」，並把官方配置連回既有學習與評量。

**官方 v5.0 blueprint 的二十個子領域對應課程 M01–M20，每章列示 6 或 7 題；差異主要來自各 Domain 包含的章數。** 題數可作覆蓋基準，複習次序仍需結合實授主題、先備依賴、未解錯題與可用時間。[官方 v5 PDF](https://cert.eccouncil.org/wp-content/uploads/2024/04/CEH-Exam-Blueprint-v5.pdf)

[完整使用者原文](../source/2026-09-22-ceh-blueprint-weights/source.md) · [來源與完整性回執](../source/2026-09-22-ceh-blueprint-weights/README.md) · [獨立官方來源查核](../source/2026-09-22-ceh-blueprint-weights/verification.md) · [課程範圍](official-scope-map.md) · [現行學習路徑](../study-plan/uuu-aligned-ceh-cehp-2026-09-18.md)

## 1. 考試、教材與統計的對象

- **CEH Knowledge Exam**：官方公開格式為 125 道選擇題、4 小時。這份筆記談該考試的 blueprint；CEH Practical 的實作考試規格另外管理。[官方 CEH 頁面](https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/)
- **課程 v13 與 blueprint v5.0**：前者是課程版本，後者是考試配置版本，版本號不需要相同。官方 certification 入口目前仍連到 v5.0；官方公告列出 2024-04-10 起生效，v4 至 2024-04-09。[查核與官方連結](../source/2026-09-22-ceh-blueprint-weights/verification.md)
- **20 Modules／9 Domains**：教材的二十章與 blueprint 二十個 sub-domains 按名稱對應，Domain 是一個或數個章節的集合。PDF 題數欄在子領域層級，整數權重欄在 Domain 層級；不能把跨列的 24% 誤算成 M08 單章。
- **配置與實際考卷**：以下為公開 blueprint 的列示數字及推算，不是從多份真實考卷抽樣得到的出題頻率，也沒有取得個別考生的考卷或試題層級統計。

## 2. 二十章完整對照

「精確占比」均由列示題數除以 125 計算；Domain 編號依官方 PDF。模組名稱沿用[本庫官方範圍](official-scope-map.md)，題本連結指向既有原創練習，沒有新增題目或變更答案。

| Module | 課程章節 | Domain | v5 列示題數 | 題數／125 | 官方 PDF 頁 | 既有練習 |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| M01 | Introduction to Ethical Hacking | 1 | 7 | 5.6% | 2 | [30 題](../assessments/practice-bank/m01.md) |
| M02 | Footprinting and Reconnaissance | 2 | 7 | 5.6% | 2 | [30 題](../assessments/practice-bank/m02.md) |
| M03 | Scanning Networks | 2 | 7 | 5.6% | 2 | [30 題](../assessments/practice-bank/m03.md) |
| M04 | Enumeration | 2 | 7 | 5.6% | 2 | [30 題](../assessments/practice-bank/m04.md) |
| M05 | Vulnerability Analysis | 3 | 6 | 4.8% | 2 | [30 題](../assessments/practice-bank/m05.md) |
| M06 | System Hacking | 3 | 6 | 4.8% | 3 | [30 題](../assessments/practice-bank/m06.md) |
| M07 | Malware Threats | 3 | 7 | 5.6% | 3 | [30 題](../assessments/practice-bank/m07.md) |
| M08 | Sniffing | 4 | 6 | 4.8% | 3 | [30 題](../assessments/practice-bank/m08.md) |
| M09 | Social Engineering | 4 | 6 | 4.8% | 3 | [30 題](../assessments/practice-bank/m09.md) |
| M10 | Denial-of-Service | 4 | 6 | 4.8% | 3 | [30 題](../assessments/practice-bank/m10.md) |
| M11 | Session Hijacking | 4 | 6 | 4.8% | 3 | [30 題](../assessments/practice-bank/m11.md) |
| M12 | Evading IDS, Firewalls, and Honeypots | 4 | 6 | 4.8% | 3 | [30 題](../assessments/practice-bank/m12.md) |
| M13 | Hacking Web Servers | 5 | 6 | 4.8% | 4 | [30 題](../assessments/practice-bank/m13.md) |
| M14 | Hacking Web Applications | 5 | 6 | 4.8% | 4 | [30 題](../assessments/practice-bank/m14.md) |
| M15 | SQL Injection | 5 | 6 | 4.8% | 4 | [30 題](../assessments/practice-bank/m15.md) |
| M16 | Hacking Wireless Networks | 6 | 6 | 4.8% | 4 | [30 題](../assessments/practice-bank/m16.md) |
| M17 | Hacking Mobile Platforms | 7 | 6 | 4.8% | 4 | [30 題](../assessments/practice-bank/m17.md) |
| M18 | IoT and OT Hacking | 7 | 6 | 4.8% | 5 | [30 題](../assessments/practice-bank/m18.md) |
| M19 | Cloud Computing | 8 | 6 | 4.8% | 5 | [30 題](../assessments/practice-bank/m19.md) |
| M20 | Cryptography | 9 | 6 | 4.8% | 5 | [30 題](../assessments/practice-bank/m20.md) |
| 合計 | 20 章 | 9 Domains | 125 | 100.0% | 2–5 | 600 題 |

題數檢查：5 章 × 7 題 + 15 章 × 6 題 = 125。單章差距為 1 題，即總題數的 0.8 個百分點；7 題比 6 題多約 16.7%，但不能據此假定多花 16.7% 時間就有相同學習收益。[官方配置](https://cert.eccouncil.org/wp-content/uploads/2024/04/CEH-Exam-Blueprint-v5.pdf)

## 3. 九個 Domain：列示百分比與精確比例

| Domain | 主題群 | 對應 Module | 題數加總 | 官方列示權重 | 題數／125 |
| --- | --- | --- | ---: | ---: | ---: |
| D1 | Information Security and Ethical Hacking Overview | M01 | 7 | 6% | 5.6% |
| D2 | Reconnaissance Techniques | M02–M04 | 21 | 17% | 16.8% |
| D3 | System Hacking Phases and Attack Techniques | M05–M07 | 19 | 15% | 15.2% |
| D4 | Network and Perimeter Hacking | M08–M12 | 30 | 24% | 24.0% |
| D5 | Web Application Hacking | M13–M15 | 18 | 14% | 14.4% |
| D6 | Wireless Network Hacking | M16 | 6 | 5% | 4.8% |
| D7 | Mobile Platform, IoT, and OT Hacking | M17–M18 | 12 | 10% | 9.6% |
| D8 | Cloud Computing | M19 | 6 | 5% | 4.8% |
| D9 | Cryptography | M20 | 6 | 5% | 4.8% |
| 合計 | | M01–M20 | 125 | 101% | 100.0% |

官方表格的整數百分比加總是 **101%**，與各題數占比四捨五入至整數的結果一致。保留官方列示值並另列精確計算，不把它偷偷正規化為另一組「官方數字」。Domain 大小排序為 D4、D2、D3、D5、D7、D1，D6／D8／D9 同列。M14 單章是 6 題，不能以 D5 的 18 題或 14% 代替。[官方 v5 PDF，第 2–5 頁](https://cert.eccouncil.org/wp-content/uploads/2024/04/CEH-Exam-Blueprint-v5.pdf)

## 4. 原文三層複習建議：計算成立，排序仍需個人證據

| 原文層級 | 模組 | 章數 | 題數 | 精確比例 | 證據地位 |
| --- | --- | ---: | ---: | ---: | --- |
| 第一層 | M02–M15 | 14 | 21 + 19 + 30 + 18 = 88 | 70.4% | 題數推算；優先順序是原文建議 |
| 第二層 | M17–M18 | 2 | 12 | 9.6% | 同上；不是官方建議先後 |
| 最後補齊 | M01、M16、M19、M20 | 4 | 7 + 6 + 6 + 6 = 25 | 20.0% | 同上；每章仍保留覆蓋需求 |

**14／20 章本來就占章數的 70%。** M02–M15 占題數 70.4%，主要反映涵蓋範圍大，無法單憑這個加總證明它比其他模組有更高的單位時間得分收益。M17–M18 兩章的 12 題，也不能證明應先於其餘四章的 25 題。

M01 的授權、風險與方法是其他模組的先備；M20 的密碼學可支持無線、session 與雲端概念。這些連結支持穿插學習，不宜因 Domain 小就延後所有基礎。原文「漏一章可能掉近 5%」可理解為題數覆蓋風險；並非未讀該章就必然答錯全部題目，也不能把題數占比直接當成保證扣分或通過率預測。

目前保留[9/18 已採用順序](../study-plan/uuu-aligned-ceh-cehp-2026-09-18.md#weekly-route)：未完成題組／必要修正 → 實授主題 → 未覆蓋的先備與考綱。Blueprint 用來檢查覆蓋，尚未取得的錯題率、解題時間與熟悉度留空；本次沒有把原文建議採納為新排程。

## 5. 原文概念鏈的用途

原文依序串聯：Recon → Scanning → Enumeration → Vulnerability Analysis → System Hacking → Malware → Sniffing → Social Engineering → DoS → Session Hijacking → Firewall/IDS evasion → Web Server → Web App → SQL Injection。

這條鏈可以當教材導覽與概念關聯，並非官方要求每次都依序執行的攻擊流程。例如社交工程可影響不同階段，DoS 也不是學會 Web 前必須執行的一步。實作仍由授權範圍、目的與驗收決定，保留[官方範圍圖的安全練習方式](official-scope-map.md)。

可直接沿用的學習連結：

- [Week 1 M01–M03 完整英文筆記](../notes/2026-09-20-ceh-week-01/plain-english/README.md)：從授權、網路概念到偵察、掃描輸出的判讀，支持本週課程銜接。
- [M05 Lesson 1](../notes/m05-vulnerability-analysis/lesson-01-weakness-to-harm.md)：區分 vulnerability、threat、exploit、risk，連到 M06 利用與 M14 存取控制。原文「目前正在念 M05」只保留為原文情境；目前 W39 仍依 9/20 實授主題與 M01–M04 先備安排。
- [25 項實作與 P1–P5](../assessments/practice-bank/practical.md)：既有掃描、列舉、流量、系統及網站分析任務提供受控練習。這次整理不啟用新任務，也不產生個人完成紀錄。

## 6. 考古題、模擬題與統計能各自證明什麼

| 資料 | 可支持 | 本次限制 |
| --- | --- | --- |
| 官方 blueprint | 考試範圍與列示題數配置 | 不能證明某工具、port 或 command 在實際考卷出現幾次 |
| 公開原創練習庫 | 該題庫自身的題數、編排及解題練習 | 編者選題與分類不代表正式試題母體 |
| 社群回憶／標為 actual questions 的 dump | 最多是未驗證的第三方聲稱 | 沒有已核實的抽樣方法、完整母體、版本與真實性；不作正式分布證據 |
| 本庫原創題目與個人 attempt | 受控的練習覆蓋、實際錯題與信心 | 原創題數不是官方歷屆頻率；準備內容不等於學員成績 |

原文聲稱看過「1,000+ 題 dumps」，未提供可核對的網站清單或抽樣資料。本次保留來源說法，沒有重新取得或驗證這類題庫，也不虛構每章考古題常見程度。

### CEHStudy 的實際查核

[CEHStudy 首頁](https://cehstudy.com/)自述為獨立、非官方、非實際考題的原創練習資源，列有 200 題、20 組、每組 10 題。這支持「網站如此描述其配置」，本次沒有逐題審核 200 題正確性。均配題庫的比例是 5%／組，不能反推正式考試。

首頁模組入口亦與官方不同：M17 標成 Mobile Platforms & IoT、M18 為 Lateral Movement、M19 為 Post-Exploitation & Incident Response；官方 M17／M18／M19 則分別是 Mobile、IoT/OT、Cloud。因此使用前須按**主題內容重新映射**，不能直接套用該站編號。該站文字有時將 20 modules 稱為 domains，本筆記維持官方 20 Modules／9 Domains 的區分。[具體查核](../source/2026-09-22-ceh-blueprint-weights/verification.md)

### 與 9/22 下載檔案的關係

[Planning 下載回執](../../planning-everything-track/weeks/2026-W39/days/2026-09-22.md#cehv13-pdf-intake)證明已按要求保存 27 份 PDF，檔案大小及本機雜湊相符。來源的學習採用狀態另由[來源信任紀錄](important-references.md#rejected-cehv13-download-directory)管理，仍為 `rejected_untrusted`；使用者要求下載並未確認來源真實性或撤銷該採用界線。

這些檔案不作官方 blueprint 或考古題頻率的證據，也不加入本庫原創題庫。正式課程教材沿用 UUU／Aspen 與已核准參考資料。若要變更來源採用，須先提出可驗證的來源／使用依據，由 Jason 決定；本次保留已下載檔案，沒有搬動或刪除。

## 7. v4 → v5 版本差異

原文提到的三項變化均可由兩份官方 PDF 對照。下表為官方**列示百分比**，不是另行正規化的數字。

| Domain | v4 題數 | v4 列示 | v5 題數 | v5 列示 | 題數變動 |
| --- | ---: | ---: | ---: | ---: | ---: |
| D1 基礎 | 8 | 6% | 7 | 6% | -1 |
| D2 Recon | 26 | 21% | 21 | 17% | -5 |
| D3 System | 21 | 17% | 19 | 15% | -2 |
| D4 Network／Perimeter | 18 | 14% | 30 | 24% | +12 |
| D5 Web | 20 | 16% | 18 | 14% | -2 |
| D6 Wireless | 8 | 6% | 6 | 5% | -2 |
| D7 Mobile／IoT／OT | 10 | 8% | 12 | 10% | +2 |
| D8 Cloud | 7 | 6% | 6 | 5% | -1 |
| D9 Cryptography | 7 | 6% | 6 | 5% | -1 |
| 合計 | 125 | 100% | 125 | 101% | 0 |

[官方 v4 PDF，第 2–5 頁](https://cert.eccouncil.org/wp-content/uploads/2024/02/CEH-Exam-Blueprint-v4.0.pdf) · [官方 v5 PDF，第 2–5 頁](https://cert.eccouncil.org/wp-content/uploads/2024/04/CEH-Exam-Blueprint-v5.pdf)。舊頁的 Recon 21%、Web 16%、Network 14% 應保留為 v4 歷史；準備考試或預約前仍從官方 certification 入口重查適用版本。

## 8. 接回現有題庫、容量與下一步

- [600 題模組練習](../assessments/practice-bank/README.md)每章 30 題，是教學廣度配置；[兩份 125 題模擬卷](../assessments/practice-bank/README.md#mock-forms-and-practical-tasks)已採 Domain 題數 7／21／19／30／18／6／12／6／6。這次核對重用現成配置，未改題庫、答案或版本。
- [個人覆蓋登錄](../assessment-governance/course-coverage-2026-09-18.md)擁有首答、解析、修正、實作與分鐘；本筆記不填入未觀察的弱點或準備度。按 Domain 加權的練習分數也不能直接解讀成正式考試通過機率。
- [W39](../../planning-everything-track/weeks/2026-W39/weekly-plan.md#ceh-blueprint-weights)與[今日紀錄](../../planning-everything-track/weeks/2026-W39/days/2026-09-22.md#ceh-blueprint-weights)保持 CEH／CEHP 共用 240 分鐘、課日最多 25 分鐘、固定承諾與恢復。這是文件整理，不算個人閱讀、答題、官方機制學習查核或 Blog 完成。
- 下次已安排的學習區塊：Jason 確認 endpoint 與當週餘量，接續未完成題組或一個課堂疑問；需要判斷覆蓋缺口時查本表與個人登錄。M05 可由既有 Lesson 1 接續，前提是實際問題與當週路徑需要。
- 原文最後提出「20 章 × 官方題數 × 考古／模擬常見程度 × 工具／port／command × 時間」的延伸表。本次已完成有來源的官方配置與現有教材連接；常見程度沒有可信統計，個人時間分配缺少實際錯題與耗時，故保留為未採用提案。工具與命令先沿用[既有技術來源](../assessments/practice-bank/sources.md)，不建立沒有證據的必考清單。

## 9. 原文覆蓋與修訂索引

| 原文內容 | 本筆記位置 | 處理 |
| --- | --- | --- |
| 能否查考古題、官方 blueprint 更適合配置判斷 | §1、§6 | 保留問題與證據種類差異 |
| 二十章題數與百分比 | §2 | 20／20 全列，接現有題本 |
| 九 Domain 排序與每章歸屬 | §3 | 9／9 全列，補精確比例與 101% 說明 |
| M02–M15 的 88 題／70.4% | §4 | 驗算並補 14／20 章的分母 |
| 三層優先度、漏章風險 | §4 | 保留原文建議，限制其推論，不變更現行排程 |
| 完整攻擊概念鏈 | §5 | 全鏈保留，標為教材導覽 |
| 1,000+ dumps、第三方統計、CEHStudy | §6 | 分別標為來源聲稱、網站自述與新增課綱差異 |
| v4／v5 衝突 | §7 | 三項原文差異及完整九 Domain 對照 |
| 20 modules、125 題、4 小時 | §1 | 官方格式與版本區分 |
| 現在念 M05、延伸矩陣提案 | §5、§8 | 原文情境與待採用提案；連回現行 W39 |
| 四個引用 | 原文與來源回執 | 原 URL 原樣保存；查核另用清理追蹤參數的 URL |

## 後續採用更新 — September 22

Jason 隨後確認第一堂已上 M01–M03，允許詳細規劃，並指定時間數字作重要性參考。[新的五循環與 C1 細化](../study-plan/course-synced-review-2026-09-22.md)承接此決策：先鞏固 M01–M03、預習 M04。上方「未採用提案」保留為較早回合的狀態；新計畫採概念依賴與個人證據，不採先讀完 M02–M15 的三層排序，也不從外部題庫推估常考頻率。
