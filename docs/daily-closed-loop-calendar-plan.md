# CEH / CEHP 十層評量制度：2026-07-01 至 2026-08-02 日曆執行版

> 班別範圍更新（`2026-07-13`）：本檔保留原始準備序列。現行確認班別為
> CEH 台北 `2048`（`2026-10-12` 至 `2026-10-16`）與 CEHP 台北 `26416`
>（`2026-11-19` 至 `2026-11-20`）；現行 readiness gates 維護於
> `assessment-governance-system.md` 與 `../study-plan/pre-course-prep.md`。
## 使用假設
- 時區：Asia/Taipei。
- 平日預設 20:30–22:00；週六預設 09:30–12:00；週日預設 15:00–17:00。若當天行程衝突，直接平移時段，不改任務順序。
- 所有練習僅限官方教材、toy scenario、授權 lab 或本地安全資料；不對真實第三方目標操作。
- 每天最後 5 分鐘都要更新 attempt_log、module_status、weak_topic_queue。
## 十層縮寫
- L1: 能力地圖
- L2: 測驗藍圖
- L3: 前後測設計
- L4: 題目 metadata
- L5: 評分規準
- L6: readiness gate
- L7: traceability matrix
- L8: 分析制度
- L9: 制度落地健康指標
- L10: 落地資料系統

## 每日行事曆任務
| 日期 | 時段 | 行事曆標題 | 任務 | 當日產出 | 對應層 |
|---|---:|---|---|---|---|
| 7/1（三） | 20:30-22:00 | CEH制度 Day 01：制度啟動與 baseline pretest | 建立 project folder、確認十層制度欄位；完成 40 題 closed-book baseline pretest；作答時標記 confidence 1-4。 | 產出 attempt_log 第 1 筆、baseline raw score、unknown list。 | L1,L3,L8,L10 |
| 7/2（四） | 20:30-22:00 | CEH制度 Day 02：Baseline scoring 與弱點圖 | 依 answer key/rubric 評分；把 40 題映射到 20 模組；列出 top 5 weak modules；建立 pass/review/activation_needed 初始門檻。 | 產出 weak_module_map_v0、readiness_rule_v0。 | L1,L5,L6,L8 |
| 7/3（五） | 20:30-22:00 | CEH制度 Day 03：題庫資料模型與 traceability v0 | 建立 item_bank schema、competency_map schema、traceability_matrix schema；把 baseline 40 題補上 item_id、module、claim、evidence_required。 | 產出 item_bank_v0、traceability_matrix_v0。 | L2,L4,L7,L10 |
| 7/4（六） | 09:30-12:00 | CEH制度 Day 04：M01 Ethical Hacking + 安全邊界 | 預習 M01；寫出 authorization/scope/stop condition/reporting path；設計 M01 mini-posttest 8 題；完成 posttest。 | M01 狀態 pass/review/activation_needed；critical safety item 檢查。 | L1,L4,L5,L6,L7 |
| 7/5（日） | 15:00-17:00 | CEH制度 Day 05：M02 Reconnaissance + passive/active | 預習 M02；建立 passive vs active discovery 對照；設計 M02 mini-posttest；記錄哪些行為需要授權。 | M02 posttest 結果；recon evidence/control map。 | L1,L4,L7,L8 |
| 7/6（一） | 20:30-22:00 | CEH制度 Day 06：M03 Scanning Networks | 預習 host/port/service/vulnerability discovery；只使用 toy output 解讀，不做真實目標操作；設計 M03 posttest。 | M03 posttest 結果；scan-output interpretation checklist。 | L1,L4,L5,L7 |
| 7/7（二） | 20:30-22:00 | CEH制度 Day 07：M04 Enumeration | 預習 users/shares/banners/service details 概念；設計 M04 posttest；比較 scanning vs enumeration。 | M04 posttest 結果；enumeration vs scanning 1 頁筆記。 | L1,L4,L7,L8 |
| 7/8（三） | 20:30-22:00 | CEH制度 Day 08：Gate 1：M01-M04 修補與 Form B 架構 | 重測 M01-M04 錯題；建立 parallel posttest Form B 規格；更新 top weak modules；檢查 execution health。 | Gate 1 dashboard：4 模組狀態、修補清單、制度摩擦點。 | L2,L3,L6,L8,L9,L10 |
| 7/9（四） | 20:30-22:00 | CEH制度 Day 09：M05 Vulnerability Analysis | 預習 severity、exploitability、impact、exposure、context、false positive；設計 M05 posttest。 | M05 posttest 結果；risk/context/remediation priority note。 | L1,L4,L5,L7 |
| 7/10（五） | 20:30-22:00 | CEH制度 Day 10：M06 System Hacking 概念化 | 預習 credential、privilege、persistence、cleanup、least privilege；保持防禦與概念層級；設計 M06 posttest。 | M06 posttest 結果；system hacking defensive lesson list。 | L1,L4,L5,L7 |
| 7/11（六） | 09:30-12:00 | CEH制度 Day 11：M07 Malware Threats | 預習 malware type、delivery、persistence、controls、evidence；設計 M07 posttest。 | M07 posttest 結果；malware evidence/control map。 | L1,L4,L7,L8 |
| 7/12（日） | 15:00-17:00 | CEH制度 Day 12：M08 Sniffers + 週檢討 | 預習 packet/flow/protocol/anomaly/evidence；設計 M08 posttest；完成 Week 2 meta-evaluation。 | M08 posttest；週報：completion、latency、repair closure、confidence-error gap。 | L1,L4,L6,L8,L9 |
| 7/13（一） | 20:30-22:00 | CEH制度 Day 13：Gate 2：M05-M08 修補與短答 rubric 強化 | 補 M05-M08 錯題；將短答 rubric 改為 0/0.5/1 並加範例；更新 traceability。 | Gate 2 dashboard；rubric_v1；重複失敗題清單。 | L5,L6,L7,L8,L9 |
| 7/14（二） | 20:30-22:00 | CEH制度 Day 14：M09 Social Engineering | 預習 phishing、verification path、MFA、報告流程與人因控制；設計 M09 posttest。 | M09 posttest；social engineering detection/control note。 | L1,L4,L5,L7 |
| 7/15（三） | 20:30-22:00 | CEH制度 Day 15：M10 Denial-of-Service | 預習 availability、resilience、rate limiting、monitoring、escalation；設計 M10 posttest。 | M10 posttest；availability/resilience map。 | L1,L4,L7,L8 |
| 7/16（四） | 20:30-22:00 | CEH制度 Day 16：M11 Session Hijacking | 預習 token/session risk、cookie flags、expiration、TLS、server-side validation；設計 M11 posttest。 | M11 posttest；session management risk/control note。 | L1,L4,L5,L7 |
| 7/17（五） | 20:30-22:00 | CEH制度 Day 17：M12 Evasion / IDS / Firewall / Honeypot | 預習 detection limits、layered controls、logging、false negative；設計 M12 posttest。 | M12 posttest；defense-in-depth failure-mode note。 | L1,L4,L7,L8 |
| 7/18（六） | 09:30-12:00 | CEH制度 Day 18：Gate 3：M09-M12 情境題校準 | 重測 M09-M12 錯題；將 4 個模組各寫 1 題 evidence-based scenario；檢查 confidence calibration。 | Gate 3 dashboard；scenario item 4 題；high-confidence wrong list。 | L2,L3,L4,L6,L8,L9 |
| 7/19（日） | 15:00-17:00 | CEH制度 Day 19：M13 Hacking Webservers | 預習 patching、configuration、least privilege、logging、default exposure；設計 M13 posttest。 | M13 posttest；webserver hardening checklist。 | L1,L4,L5,L7 |
| 7/20（一） | 20:30-22:00 | CEH制度 Day 20：M14 Web Application | 預習 auth、input validation、access control、error handling、logging；設計 M14 posttest。 | M14 posttest；web-app risk/evidence/control map。 | L1,L4,L7,L8 |
| 7/21（二） | 20:30-22:00 | CEH制度 Day 21：M15 SQL Injection 安全概念 | 預習 untrusted input 改變 query meaning、parameterized query、防禦與日誌跡象；不寫 exploit payload；設計 M15 posttest。 | M15 posttest；SQLi 防禦概念筆記。 | L1,L4,L5,L7 |
| 7/22（三） | 20:30-22:00 | CEH制度 Day 22：M16 Wireless Network | 預習 WPA2/WPA3、guest separation、rogue AP、enterprise auth、弱協定；設計 M16 posttest。 | M16 posttest；wireless risk/control note。 | L1,L4,L7,L8 |
| 7/23（四） | 20:30-22:00 | CEH制度 Day 23：Gate 4：M13-M16 web/wireless 修補 | 重測 M13-M16 錯題；補 8 題 web/wireless Form B 題；更新 module status。 | Gate 4 dashboard；web/wireless weak topic burn-down。 | L2,L3,L4,L6,L8,L9 |
| 7/24（五） | 20:30-22:00 | CEH制度 Day 24：M17 Mobile Platforms | 預習 device/app/network/storage/identity risk；設計 M17 posttest。 | M17 posttest；mobile attack-surface/control note。 | L1,L4,L5,L7 |
| 7/25（六） | 09:30-12:00 | CEH制度 Day 25：M18 IoT / OT | 預習 physical safety、firmware、segmentation、patching constraint、downtime risk；設計 M18 posttest。 | M18 posttest；IT vs IoT/OT 差異表。 | L1,L4,L7,L8 |
| 7/26（日） | 15:00-17:00 | CEH制度 Day 26：M19 Cloud Computing | 預習 shared responsibility、IAM、storage permission、logging、network rules；設計 M19 posttest。 | M19 posttest；cloud customer responsibility checklist。 | L1,L4,L5,L7 |
| 7/27（一） | 20:30-22:00 | CEH制度 Day 27：M20 Cryptography | 預習 encryption vs hashing、integrity、key management、TLS、常見誤用；設計 M20 posttest。 | M20 posttest；crypto misuse/control note。 | L1,L4,L7,L8 |
| 7/28（二） | 20:30-22:00 | CEH制度 Day 28：20 模組總整理 | 每個模組寫 2-3 句：core risk、evidence type、main control；把 20 模組全部標記 pass/review/activation_needed。 | 20-module class-readiness map v1。 | L1,L6,L7,L8,L10 |
| 7/29（三） | 20:30-22:00 | CEH制度 Day 29：正式 Pre-August Form B 建置 | 建立 50 題或 40 題 Form B：與 baseline 等比例，但不同情境；保留最多 8 題 anchor；補 metadata 與 rubric link。 | pre_august_form_b_v1；form blueprint 對照表。 | L2,L3,L4,L5,L7 |
| 7/30（四） | 20:30-22:00 | CEH制度 Day 30：Pre-August Readiness Test | closed-book 完成 Form B；評分；記錄 confidence；標記 critical safety error；產生最終 3 天修補清單。 | Form B score；critical safety status；final repair queue。 | L3,L5,L6,L8,L9 |
| 7/31（五） | 20:30-22:00 | CEH制度 Day 31：修補封版與上課 notebook | 修補 Form B 最弱 5 題/模組；建立 CEH class notebook template：date/module/instructor cue/lab evidence/weak topic/next action。 | final repair closure；class_notebook_template_v1。 | L6,L7,L8,L9,L10 |
| 8/1（六） | 09:30-12:30 | CEH制度 Day 32：Final Gate：CEH class readiness dry run | 口頭或文字完成 20 模組 2-3 句解釋；演練 evidence interpretation；整理課前問老師的問題。 | final_gate_result；20-module oral checklist；question list for class。 | L1,L6,L7,L8,L9 |
| 8/2（日） | 15:00-16:30 | CEH制度 Day 33：Light Review + Logistics Lock | 只做輕量複習：authorization、20 module map、top weak topics；整理明天上課資料、交通、設備、登入、睡眠。 | CEH Day 1 packet；不新增重內容；就緒狀態確認。 | L6,L9,L10 |

## 每日固定收尾格式
```text
date:
module_or_gate:
outcome: pass / review / activation_needed
score:
confidence_error:
critical_safety_error: yes/no
weak_topics:
next_action:
files_updated:
```

## Readiness Gate 判準
- pass：核心風險、關鍵詞、證據型態、主要控制都能說清楚，posttest ≥75%，critical safety item 無錯。
- review：方向正確但不穩，posttest 50–74%，隔日或 gate 日補 20–30 分鐘。
- activation_needed：低於 50%、高信心錯誤、或 critical safety item 錯誤；先補前置概念，不硬推下一層。
- 8/2 最低標準：baseline 已評分；20 模組皆有狀態；至少 16 模組達 pass/review；legal/authorization、network basics、web basics、cloud shared responsibility、crypto 至少 review；每個 activation_needed 模組都有一個明確補救行動。
