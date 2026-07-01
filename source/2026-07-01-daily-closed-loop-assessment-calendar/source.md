# 2026-07-01 Daily Closed-Loop Assessment Calendar

## Source Boundary

Status: `source preserved`

This file preserves the user-provided daily closed-loop plan for CEH / CEHP
assessment governance from `2026-07-01` to `2026-08-02`.

Canonical copied source file:

`ceh_cehp_assessment_calendar_plan_2026-07-01_to_2026-08-02.md`

Original local source:

`~/Downloads/ceh_cehp_assessment_calendar_plan_2026-07-01_to_2026-08-02.md`

SHA-256 at capture:

`53a75ae8fc9b0a07f4d7794807eb143ee03163942eadb0405e46fb12de30a914`

## 原始記錄

結論：你要用「低摩擦、每日閉環」來做。每天只做一個主任務、一個產出、一個紀錄更新。不要每天重新設計制度，否則制度本身會變成負擔。

我已經幫你做成兩個檔案：

[下載可匯入 Google Calendar / Apple Calendar 的 ICS 行事曆檔](sandbox:/mnt/data/ceh_cehp_assessment_calendar_2026-07-01_to_2026-08-02.ics)

[下載完整 Markdown 日程規劃檔](sandbox:/mnt/data/ceh_cehp_assessment_calendar_plan_2026-07-01_to_2026-08-02.md)

規劃依據：你 8/3–8/7 的 CEH13 台北 2046 班是 40 小時、09:00–18:00，官方課綱列 20 個模組；CEHP 26408 班是 9/6–9/13 每週日 09:00–17:00、14 小時，重點是 CEH Practical review。EC-Council 官方也說 CEH knowledge exam 是 4 小時 125 題，practical exam 是 6 小時 20 個實作挑戰。([恆逸教育訓練中心][1])

制度設計則採三個權威框架混合：測驗效度、信度、公平性與評分治理參考 AERA/APA/NCME Standards；資安能力語言參考 NIST NICE Framework；制度是否真的被使用，參考 CDC Program Evaluation Framework 的 context、program description、evaluation design、credible evidence、conclusion、action cycle。([NCME][2])

預設行事曆時段：平日 20:30–22:00，週六 09:30–12:00，週日 15:00–17:00。若當天有衝突，直接平移時段，不改任務順序。

| 日期 | 行事曆標題 | 當日任務 | 當日產出 |
| --- | --- | --- | --- |
| 7/1（三） | 制度啟動與 baseline pretest | 建立 project folder、確認十層制度欄位；完成 40 題 closed-book baseline pretest；標記 confidence 1–4。 | baseline raw score、unknown list、attempt_log 第 1 筆 |
| 7/2（四） | Baseline scoring 與弱點圖 | 評分；把 40 題映射到 20 模組；列 top 5 weak modules。 | weak_module_map_v0、readiness_rule_v0 |
| 7/3（五） | 題庫資料模型與 traceability v0 | 建立 item_bank、competency_map、traceability_matrix schema；baseline 40 題補 metadata。 | item_bank_v0、traceability_matrix_v0 |
| 7/4（六） | M01 Ethical Hacking | 預習 authorization、scope、stop condition、reporting path；設計並完成 M01 mini-posttest。 | M01 狀態、critical safety item 檢查 |
| 7/5（日） | M02 Reconnaissance | 預習 passive vs active discovery；設計 M02 mini-posttest；標記哪些行為需要授權。 | M02 posttest、recon evidence/control map |
| 7/6（一） | M03 Scanning Networks | 預習 host/port/service/vulnerability discovery；只解讀 toy output，不碰真實目標。 | M03 posttest、scan-output checklist |
| 7/7（二） | M04 Enumeration | 預習 users、shares、banners、service details；比較 scanning vs enumeration。 | M04 posttest、1 頁比較筆記 |
| 7/8（三） | Gate 1：M01–M04 修補 | 重測錯題；建立 parallel Form B 規格；更新 top weak modules。 | Gate 1 dashboard |
| 7/9（四） | M05 Vulnerability Analysis | 預習 severity、exploitability、impact、exposure、context、false positive。 | M05 posttest、risk/context/remediation note |
| 7/10（五） | M06 System Hacking 概念化 | 預習 credential、privilege、persistence、cleanup、least privilege；維持防禦與概念層級。 | M06 posttest、defensive lesson list |
| 7/11（六） | M07 Malware Threats | 預習 malware type、delivery、persistence、controls、evidence。 | M07 posttest、malware evidence/control map |
| 7/12（日） | M08 Sniffers + 週檢討 | 預習 packet、flow、protocol、anomaly、evidence；完成 Week 2 meta-evaluation。 | M08 posttest、週報 |
| 7/13（一） | Gate 2：M05–M08 修補 | 補錯題；短答 rubric 改成 0 / 0.5 / 1；更新 traceability。 | rubric_v1、Gate 2 dashboard |
| 7/14（二） | M09 Social Engineering | 預習 phishing、verification path、MFA、報告流程與人因控制。 | M09 posttest、control note |
| 7/15（三） | M10 Denial-of-Service | 預習 availability、resilience、rate limiting、monitoring、escalation。 | M10 posttest、availability map |
| 7/16（四） | M11 Session Hijacking | 預習 token/session risk、cookie flags、expiration、TLS、server-side validation。 | M11 posttest、session risk/control note |
| 7/17（五） | M12 Evasion / IDS / Firewall | 預習 detection limits、layered controls、logging、false negative。 | M12 posttest、defense-in-depth note |
| 7/18（六） | Gate 3：M09–M12 情境題校準 | 重測錯題；每個模組寫 1 題 evidence-based scenario；檢查 high-confidence wrong。 | 4 題 scenario items、Gate 3 dashboard |
| 7/19（日） | M13 Hacking Webservers | 預習 patching、configuration、least privilege、logging、default exposure。 | M13 posttest、webserver hardening checklist |
| 7/20（一） | M14 Web Application | 預習 auth、input validation、access control、error handling、logging。 | M14 posttest、web-app risk map |
| 7/21（二） | M15 SQL Injection 安全概念 | 預習 untrusted input、parameterized query、防禦與日誌跡象；不寫 exploit payload。 | M15 posttest、SQLi 防禦筆記 |
| 7/22（三） | M16 Wireless Network | 預習 WPA2/WPA3、guest separation、rogue AP、enterprise auth、弱協定。 | M16 posttest、wireless control note |
| 7/23（四） | Gate 4：M13–M16 修補 | 重測錯題；補 8 題 web/wireless Form B 題；更新 module status。 | Gate 4 dashboard |
| 7/24（五） | M17 Mobile Platforms | 預習 device、app、network、storage、identity risk。 | M17 posttest、mobile attack-surface note |
| 7/25（六） | M18 IoT / OT | 預習 physical safety、firmware、segmentation、patching constraint、downtime risk。 | M18 posttest、IT vs IoT/OT 差異表 |
| 7/26（日） | M19 Cloud Computing | 預習 shared responsibility、IAM、storage permission、logging、network rules。 | M19 posttest、cloud responsibility checklist |
| 7/27（一） | M20 Cryptography | 預習 encryption vs hashing、integrity、key management、TLS、常見誤用。 | M20 posttest、crypto misuse/control note |
| 7/28（二） | 20 模組總整理 | 每個模組寫 2–3 句：core risk、evidence type、main control。 | 20-module class-readiness map v1 |
| 7/29（三） | 正式 Pre-August Form B 建置 | 建立 50 題或 40 題 Form B；保留最多 8 題 anchor；補 metadata 與 rubric link。 | pre_august_form_b_v1 |
| 7/30（四） | Pre-August Readiness Test | closed-book 完成 Form B；評分；記錄 confidence；標記 critical safety error。 | Form B score、final repair queue |
| 7/31（五） | 修補封版與上課 notebook | 修補 Form B 最弱 5 題/模組；建立 CEH class notebook template。 | class_notebook_template_v1 |
| 8/1（六） | Final Gate：CEH readiness dry run | 口頭或文字完成 20 模組 2–3 句解釋；演練 evidence interpretation；整理課前問題。 | final_gate_result、課前問題清單 |
| 8/2（日） | Light Review + Logistics Lock | 只做輕量複習：authorization、20 module map、top weak topics；整理交通、設備、登入、睡眠。 | CEH Day 1 packet；不新增重內容 |

每日收尾只填這個，不要多：

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

8/2 的最低通過標準：baseline 已評分；20 模組都有狀態；至少 16 個模組達 pass 或 review；legal/authorization、network basics、web basics、cloud shared responsibility、crypto 至少 review；每個 activation_needed 模組都有一個具體補救行動。這樣你 8/3 進 CEH 課程時，重點就不是「第一次聽名詞」，而是能跟上老師、吸收 lab、抓考點、建立後續 CEHP practical bridge。

[1]: https://www.uuu.com.tw/Course/Show/2144/EC-Council-CEH%E9%A7%AD%E5%AE%A2%E6%8A%80%E8%A1%93%E5%B0%88%E5%AE%B6%E8%AA%8D%E8%AD%89%E8%AA%B2%E7%A8%8B
[2]: https://ncme.org/resources/books/testing-standards/

## Accepted Interpretation

The CEH / CEHP assessment lane adopts a low-friction daily closure model. Each
day has one primary task, one visible output, and one record update. The
Assessment Governance System remains useful by staying light enough to execute.

## Connections

- Daily closed-loop plan: `../../docs/daily-closed-loop-plan.md`
- Detailed calendar plan:
  `../../docs/daily-closed-loop-calendar-plan.md`
- Daily closeout template: `../../assessment-governance/daily_closeout_template.md`
- Assessment governance system: `../../docs/assessment-governance-system.md`
- Pre-course prep: `../../study-plan/pre-course-prep.md`
