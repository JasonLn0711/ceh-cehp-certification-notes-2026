# 2026-07-01 Assessment Governance Expert Review

## Source Boundary

Status: `source preserved`

This file preserves the user-provided expert review about upgrading the CEH /
CEHP project from a question-bank packet into an Assessment Governance System.

## 原始記錄

結論：你這個 CEH / CEHP 專案不要只做「題庫」，要做一個小型但嚴謹的 **Assessment Governance System**。核心是：每一道題都要能回溯到「官方範圍 → 能力主張 → 證據 → 題目 → 評分規準 → 補救行動 → 再測結果」。這樣才知道前測、後測不是形式，而是真的能衡量學習落差、修補效果與 CEHP 實作準備度。

我檢視你上傳的 assessment packet。它目前已經有 baseline pretest、answer key、rubric、assessment system、question-writing spec、preview plan。方向正確，但還偏「個人讀書計畫＋初階診斷」。要變成專業制度，需要補上四件事：一是 item metadata，二是 parallel pre/post forms，三是 traceability matrix，四是 implementation health metrics。

你目前的專案事實基礎如下：恆逸 UUU 的 CEH13 課程頁面顯示 CEH 駭客技術專家認證課程為 40 小時，台北 2046 班是 2026/08/03–2026/08/07，09:00–18:00；課程內容列出 20 個模組，從 Introduction to Ethical Hacking 到 Cryptography。([恆逸教育訓練中心][1]) CEHP 課程頁面顯示「CEH 大師雙認證實戰考試總複習班 / CEH Practical Exam Review」為 14 小時，台北 26408 班是 2026/09/06–2026/09/13，每週日 09:00–17:00，且適合已取得 CEH 或已完成 CEH 課程、想準備 CEH Practical 的人。([恆逸教育訓練中心][2]) EC-Council 官方 CEH 頁面說明 CEH knowledge exam 是 4 小時 125 題選擇題，CEH Practical 是 6 小時 20 個實作挑戰；CEH Master 則需要通過知識考與 practical exam。([EC-Council][3])

權威方法上，沒有一套「專門給 CEH 個人準備」的官方前後測制度。比較正確的做法，是組合幾個成熟標準：用 AERA/APA/NCME 的教育與心理測驗標準來約束效度、信度、公平性、施測與評分；NCME 說這套 Standards 是 AERA、APA、NCME 共同產品，並稱其為美國及國際測驗實務的 gold standard。([NCME][4]) 用 Evidence-Centered Design 把「想測什麼能力」轉成「要看什麼證據」與「題目怎麼引出證據」；ECD 的重點就是用 evidentiary reasoning 設計評量，讓證據蒐集與解釋能對應到底層知識與評量目的。([ERIC][5]) 用 NIST NICE Framework 作為資安能力語言，因為 NICE 用 Task、Knowledge、Skill 描述資安工作與能力，是資安教育、訓練與人才發展的共同詞彙。([NIST][6]) 用 ADDIE 管教學設計流程；ADDIE 是 Analyze、Design、Develop、Implement、Evaluate，適合把你的準備路徑做成可迭代訓練系統。([The University of Washington Bothell][7]) 用 CDC Program Evaluation Framework 管制度是否真的被使用，因為它把評估拆成 stakeholders、program description、evaluation design、evidence、conclusions、use/share lessons 等步驟。([CDC][8])

最適合你的完整架構如下。

第一層是「能力地圖」。不要從題目開始，而是先定義能力。對 CEH 前測來說，能力不是「會不會打工具指令」，而是能不能辨識法律授權邊界、理解 20 模組的基本風險、讀懂簡單 evidence，例如 port list、service banner、web log、cloud IAM risk、crypto misuse。對 CEHP 後測來說，能力才進入實作流程：讀 scan output、判斷 service/version clues、整理 lab evidence、寫 finding、提出 remediation priority。這樣切分符合你的時間線：8/3 前是 CEH vocabulary / workflow readiness，9/6 前是 CEHP practical readiness。

第二層是「測驗藍圖」。建議你不要只用目前 40 題 baseline。保留它作為低壓力 no-study diagnostic，但新增一份正式 baseline form A。正式版建議 50 題、60 分鐘：25 題基本選擇題、10 題 evidence-based scenario MCQ、10 題短答、5 題安全判斷題。比例建議是 CEH 20 模組平均覆蓋，每個模組至少 2 題；法律授權、network basics、web basics、cloud shared responsibility、cryptography 必須額外加權，因為這些是後續吸收課程的前置骨架。

第三層是「前後測設計」。前測 form A 不能直接拿來當後測，不然你測到的是記憶題目，不是能力成長。做法是建立 parallel form B，題型、模組比例、難度層級相同，但情境與選項不同。可以保留 8–10 題 anchor items，用來比較前後測，但不要超過 20%。前後測都要記錄 confidence rating，例如 1–4 分，因為資安學習有一個很常見問題：錯得很有自信，這比單純不知道更危險。

第四層是「題目 metadata」。每一題都必須有固定欄位。最小可行格式如下：

```yaml
item_id: CEH-M03-L2-004
version: 1.0.0
status: pilot
module: "M03 Scanning Networks"
level: "L2 evidence interpretation"
claim: "Learner can interpret basic scan output and choose a safe next step."
evidence_required: "Chooses evidence-preserving, authorized, non-destructive next action."
task_type: "scenario_mcq"
source_map:
  official_scope: "CEH Module 03 / UUU CEH13 course outline"
  nice_mapping: "NICE Task/Knowledge/Skill mapping pending"
rubric_id: "RUB-SCAN-01"
critical_safety_item: false
correct_answer: "B"
rationale: "The selected action preserves authorization boundary and validates service exposure."
remediation_if_missed: "Review host/port/service distinction and scan result interpretation."
author: "AI draft + human review"
reviewer: "SME / Jason"
created_at: "2026-07-01"
last_reviewed_at: "2026-07-01"
```

第五層是「評分規準」。選擇題可以 0/1，但短答與實作題不要只看答案，要看 reasoning。建議短答用 0、0.5、1；實作 readiness 用 0、1、2。2 分代表能正確描述 evidence、風險、授權邊界與下一步；1 分代表方向對但證據不足；0 分代表錯誤、空泛或不安全。凡是法律授權、未授權測試、破壞性操作、刪除證據、公開揭露敏感資訊這類題目，應設為 critical safety item；即使總分高，只要 critical safety item 失敗，就不能判定 ready。

第六層是「readiness gate」。你現在最需要的不是精細排名，而是決策門檻。建議如下：

| 時點                  |                          測驗 | 通過標準                             | 失敗處理                                 |
| ------------------- | --------------------------: | -------------------------------- | ------------------------------------ |
| 7/1–7/3             |             Baseline form A | 不要求通過，只產生弱點圖                     | 取最低 5 個模組進入 preview repair           |
| 每個 CEH 模組 preview 後 |           8 題 mini-posttest | ≥75%，且 critical safety 無錯        | 50–74% review；<50% activation_needed |
| 8/1–8/2             | Pre-August readiness form B | ≥75%，20 模組中至少 16 個達 review/pass  | 未達標者只補 prerequisite，不硬讀工具            |
| 8/3–8/7 每日課後        |           Daily class check | 能列出當日 3 個 evidence、3 個弱點、1 個補救行動 | 隔天課前 20 分鐘修補                         |
| 8/8–9/5             |       CEHP practical bridge | 5 類 scenario 至少 4 類達 pass        | 失敗類別安排 lab notebook repair           |
| 9/5                 |         CEHP readiness gate | 能完成一份完整 lab finding note         | 未達標則 CEHP 課中以跟課吸收為主，不急著考 practical   |

第七層是「資料彙整與可回溯性」。你需要一張 traceability matrix。每一個學習結論都要能往回查。格式如下：

| Trace layer | 問題                                       |
| ----------- | ---------------------------------------- |
| Source      | 這個能力來自哪個官方模組、NIST NICE 類別或課程要求？          |
| Claim       | 我們聲稱學習者具備什麼能力？                           |
| Evidence    | 什麼回答、紀錄或 lab output 能支持這個聲稱？             |
| Item        | 哪一題或哪個 scenario 引出這個 evidence？           |
| Rubric      | 用哪個規準評分？                                 |
| Attempt     | 哪一次作答、哪個版本、花多久、信心幾分？                     |
| Decision    | 判定 pass/review/activation_needed 的依據是什麼？ |
| Remediation | 指派哪個補救行動？                                |
| Retest      | 補救後是否改善？改善多少？                            |

第八層是「分析制度」。單人專案不要假裝可以做大型 psychometrics。Cronbach’s alpha、IRT、DIF 這些要有足夠樣本才有意義；你現在應該先做 deterministic analytics。也就是：模組分數、層級分數、critical safety error、confidence calibration、weak module burn-down、補救完成率、再測改善幅度。等未來有 30–50 人以上作答，再做 item difficulty、discrimination、distractor analysis；有更大樣本後才考慮 IRT。

第九層是「制度是否真的能運作」的 meta-evaluation。這是你問的重點：制度再漂亮，如果太重，就會中斷。建議設定 execution health metrics：

| 指標                       |             目標值 | 意義                |
| ------------------------ | --------------: | ----------------- |
| posttest completion rate |            ≥85% | 制度沒有重到做不下去        |
| scoring latency          |          ≤24 小時 | 測驗結果能立刻影響學習       |
| remediation closure rate |            ≥75% | 錯題有真的被修補          |
| weak-module reduction    | 每週至少下降 2 個高風險模組 | 有學習改善             |
| critical safety error    |     0 tolerance | 安全與授權邊界不能模糊       |
| repeated failure count   |   同一模組連續失敗 ≤2 次 | 連續失敗第 3 次要換教材或換方法 |
| confidence-error gap     |       高信心錯誤逐週下降 | 避免自信錯誤變成實務風險      |

第十層是「制度落地設計」。我建議你採用 Minimum Viable Assessment System，而不是一開始就做完整 LMS。先用 6 個檔案即可：`competency_map.csv`、`item_bank.csv`、`assessment_forms.csv`、`attempt_log.csv`、`rubric.md`、`readiness_dashboard.md`。題庫與表單用 Git version control；每次測驗結果用 CSV 或 SQLite 存；每週產生一次 dashboard。1EdTech 的 Caliper Analytics 是正式學習資料標準，可用來理解 learning activity / usage data 如何被蒐集與分析；Caliper 規格本身也說它提供結構化 vocabulary 來蒐集 learning and usage data，支援決策與 learner success。([1EdTech][9]) 你現在不必真的上 Caliper，但資料模型可以先模仿它的精神。

題目品質上，要避免目前 baseline 裡面太多「明顯錯選項」。例如「ethical hacking 最重要邊界是 authorization and scope」這類題可以保留少量當暖身，但不能用來判斷 readiness。正式題應改成情境判斷，例如：某 lab instruction 給了 target range，但掃描結果看到旁邊網段也開放，下一步是什麼？正確答案應該是停在授權範圍內、記錄觀察、詢問授權邊界，而不是繼續掃。多選題設計也要根據 validated item-writing guidelines：每題測單一明確能力、避免瑣碎內容、使用新情境測高層次理解、題幹要有中心問題、干擾選項要合理；Haladyna、Downing、Rodriguez 的 multiple-choice item-writing review 就整理並驗證了 31 類指引，並指出這些格式也可用於大型 assessment。([UFVJM][10])

整個制度的實作節奏，我會這樣排：

7/1–7/3 做正式 baseline form A，產出 weak-module map。7/4–7/31 每天 25–40 分鐘 preview，結束後做 8 題 mini-posttest。8/1–8/2 做 pre-August readiness form B，只判斷能不能有效進入 40 小時 CEH 課，不追求滿分。8/3–8/7 每天課後做 daily class check，記錄 instructor cue、lab evidence、弱點。8/8–9/5 進入 CEHP bridge，把重點從「懂概念」切到「能用 notebook 安全地記錄 evidence、判斷下一步、寫 finding」。9/5 做 CEHP readiness gate。

你的制度成功標準不是「題庫很多」，而是這三件事：

第一，任何一個 pass/review/activation_needed 判斷，都能回溯到題目版本、官方模組、作答證據、rubric 與補救紀錄。

第二，測驗結果會改變下一步學習安排。如果測完只是存檔，這個制度是假的。

第三，制度本身低摩擦。每個 module posttest 控制在 8–12 分鐘，每週只做一次 30 分鐘 review。資料欄位固定，不能每次重新發明格式。只收會影響決策的資料，不收漂亮但沒用的資料。

最終建議：你現在上傳的 packet 可以作為 v0.1；下一版應升級成 v0.2「可回溯評量系統」。具體改動是：把 baseline 題目改成 50 題正式 form A；建立 parallel form B；為每題補 metadata；建立 traceability matrix；加上 execution health metrics；把 20 個 CEH 模組與 5 類 CEHP practical scenario 都納入 dashboard。這樣才不是普通讀書計畫，而是可審查、可修正、可持續運作的專業前後測制度。

[1]: https://www.uuu.com.tw/Course/Show/2144/EC-Council-CEH%E9%A7%AD%E5%AE%A2%E6%8A%80%E8%A1%93%E5%B0%88%E5%AE%B6%E8%AA%8D%E8%AD%89%E8%AA%B2%E7%A8%8B
[2]: https://www.uuu.com.tw/Course/Show/1609/CEH%E5%A4%A7%E5%B8%AB%E9%9B%99%E8%AA%8D%E8%AD%89%E5%AF%A6%E6%88%B0%E8%80%83%E8%A9%A6%E7%B8%BD%E8%A4%87%E7%BF%92%E7%8F%AD
[3]: https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/
[4]: https://ncme.org/resources/books/testing-standards/
[5]: https://files.eric.ed.gov/fulltext/ED483399.pdf
[6]: https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center/nice-framework-current-versions
[7]: https://www.uwb.edu/it/addie
[8]: https://www.cdc.gov/evaluation/php/evaluation-framework/index.html
[9]: https://www.1edtech.org/standards/caliper
[10]: https://site.ufvjm.edu.br/fammuc/files/2016/05/item-writing-guidelines.pdf

## Accepted Interpretation

This repo adopts the expert recommendation as v0.2 direction: the CEH / CEHP
assessment lane is an Assessment Governance System, not only a question bank.
The system should preserve traceability from official scope to competency claim,
evidence, item, rubric, remediation, and retest result.

## Adopted Decisions

- Keep the current 40-question baseline as a low-friction no-study diagnostic.
- Create a formal baseline `form_a` with `50` items and a parallel `form_b` for
  pre-August readiness.
- Add item metadata for every formal item.
- Add a traceability matrix and deterministic analytics before psychometrics.
- Use critical safety items as readiness gates.
- Track execution health metrics so the system remains usable.
- Keep the minimum viable assessment system in simple versioned files before
  introducing an LMS or analytics platform.

## Connections

- Assessment governance design: `../../docs/assessment-governance-system.md`
- Expert packet locator: `../../docs/expert-assessment-packet.md`
- Minimum viable assessment files: `../../assessment-governance/`
- Current baseline pretest: `../../assessments/00-baseline-pretest.md`
- Pre-course plan: `../../study-plan/pre-course-prep.md`
