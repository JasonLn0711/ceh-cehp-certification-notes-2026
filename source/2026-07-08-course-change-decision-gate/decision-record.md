# 2026-07-08 CEH / CEHP 班別調整決策紀錄

Status: `source preserved`

## 原始記錄

> 我想要把 CEH 的班表日期改為 `台北 	2053 班 	2026/09/20 ~ 2026/11/01 每週日 	09:00~18:00` ，因為我 8/2-8/4 有涵那邊的家庭旅行，要去台中。然後 9/5 要去高雄聽W-inds.演唱會，所以才想要這樣改，但我想要先確認 Max 那邊的工作流程，再來決定，如果 VOISS AI 的 Max 確定書面給我 offer ，我確定要工作了，就改成 CEH 週末班，連續五週的週末都去上課，如果沒有正式錄取（雖然現在是 Max 口頭錄取），那就上週一到週五的班。所以，如果 VOISS AI 有正式錄取我，我就把 CEH 改成 2026/09/20 - 11/01 的班，而 CEHP 就改成 `台北 	26416 班 	2026/11/19 ~ 2026/11/20 每週四五 	09:00~17:00` 的班。請你幫我完整的記錄下來我需要的決策過程。

## 決策主軸

這次班別調整以 `VOISS AI / Max 書面 offer` 作為啟動 gate。口頭錄取是目前的正向訊號；正式工作安排需要等書面 offer 與工作流程確認後，才把 CEH / CEHP 班別改成工作相容版本。

## FIRST PRINCIPLE Router

- Scarce resource: `2026-08` to `2026-11` 的工作啟動、家庭旅行、演唱會、CEH / CEHP 上課與考證準備容量。
- Canonical home: this repo owns the CEH / CEHP decision gate, official course verification, study impact, and exam-readiness path.
- Planning role: `planning-everything-track` keeps the thin schedule / capacity mirror and next gate only.
- Evidence path: official UUU / UCOM course pages verified on `2026-07-08`, plus the preserved user-provided decision record above.
- Next gate: Max provides VOISS AI written offer and work-flow confirmation; then UCOM / UUU confirms class-change availability.

## Official Verification

Verified on `2026-07-08` from official UUU / UCOM course pages:

| Item | Status | Evidence |
| --- | --- | --- |
| CEH 台北 `2053` | `confirmed` | Official CEH13 page lists 台北 `2053`, `2026-09-20` to `2026-11-01`, Sundays, `09:00-18:00`: <https://www.uuu.com.tw/Course/Show/2144/EC-Council-CEH%E9%A7%AD%E5%AE%A2%E6%8A%80%E8%A1%93%E5%B0%88%E5%AE%B6%E8%AA%8D%E8%AD%89%E8%AA%B2%E7%A8%8B> |
| CEHP 台北 `26416` | `confirmed` | Official CEHP page lists 台北 `26416`, `2026-11-19` to `2026-11-20`, Thursday-Friday, `09:00-17:00`: <https://www.uuu.com.tw/Course/Show/1609/CEH%E5%A4%A7%E5%B8%AB%E9%9B%99%E8%AA%8D%E8%AD%89%E5%AF%A6%E6%88%B0%E8%80%83%E8%A9%A6%E7%B8%BD%E8%A4%87%E7%BF%92%E7%8F%AD> |
| Change from current registered classes to target classes | `pending confirmation` | UCOM / UUU must confirm class-change availability, seat status, package continuity, payment timing, and rights impact. |

## 目前基準方案

| 課程 | 目前已登記班別 | 使用條件 |
| --- | --- | --- |
| CEH | 台北 `2046`, `2026-08-03` to `2026-08-07`, Monday to Friday, `09:00-18:00` | Max 尚未提供書面 offer，或尚未確認正式錄取與工作流程前，維持平日密集班作為基準方案。 |
| CEHP | 台北 `26408`, `2026-09-06` and `2026-09-13`, Sundays, `09:00-17:00` | 搭配目前 CEH 平日班，保留原本九月複習節奏。 |

## 啟動條件

| Gate | 判準 | 決策效果 |
| --- | --- | --- |
| `offer_written_confirmed` | VOISS AI 的 Max 提供正式書面 offer。 | 啟動工作相容班表，向 UCOM / UUU 申請改 CEH 週末班與 CEHP 11 月班。 |
| `workflow_confirmed` | Max 那邊的入職流程、工作節奏、開始日期、平日可用時間有清楚確認。 | 確認週末上課是主要可行路徑，避免平日班與工作衝突。 |
| `no_formal_offer_yet` | 目前仍停留在口頭錄取，尚未完成正式錄取文件。 | 保留 CEH 平日班，不提前改班。 |

## 條件分支

### 分支 A：VOISS AI 正式錄取

當 Max 提供書面 offer，且工作流程確認後，採用工作相容班表：

| 課程 | 目標班別 | 節奏 | 使用理由 |
| --- | --- | --- | --- |
| CEH | 台北 `2053`, `2026-09-20` to `2026-11-01`, Sundays, `09:00-18:00` | 週末班，連續五週末上課 | 平日保留給正式工作與入職節奏，CEH 學習移到週末。 |
| CEHP | 台北 `26416`, `2026-11-19` to `2026-11-20`, Thursday-Friday, `09:00-17:00` | 11 月兩日複習班 | 接在 CEH 週末班之後，讓 CEHP 與 CEH 學習完成時間銜接。 |

### 分支 B：尚未正式錄取

如果 Max 尚未提供書面 offer，或正式錄取流程尚未完成，維持目前平日班：

| 課程 | 保留班別 | 節奏 | 使用理由 |
| --- | --- | --- | --- |
| CEH | 台北 `2046`, `2026-08-03` to `2026-08-07`, Monday-Friday, `09:00-18:00` | 一週密集班 | 在尚未確定工作前，保留最快完成 CEH 課程的路徑。 |
| CEHP | 台北 `26408`, `2026-09-06` and `2026-09-13`, Sundays, `09:00-17:00` | 兩個週日複習班 | 接續原 CEH 時程，維持原本九月 CEHP 準備節奏。 |

## 個人行程因素

| 日期 | 行程 | 對 CEH / CEHP 決策的影響 |
| --- | --- | --- |
| `2026-08-02` to `2026-08-04` | 涵那邊的家庭旅行，去台中 | 會壓縮原 CEH 平日班前一晚與前兩天的精神和交通安排；若正式工作成立，改週末班可讓八月初行程與工作轉換更從容。 |
| `2026-09-05` | 去高雄聽 W-inds. 演唱會 | 與原 CEHP `2026-09-06` 第一堂相鄰，可能增加交通與體力負擔；若正式工作成立，CEHP 改到 `2026-11-19` to `2026-11-20` 可降低九月初衝突。 |

## Scope Controls

- 這份紀錄只保存班別決策流程，不代表已向 UCOM / UUU 完成改班。
- 正式改班前，需要保留 UCOM / UUU 可改班、名額、費用、付款、開課通知與票券權益的確認層。
- VOISS AI 的 offer 文件與面試細節屬於職涯申請脈絡；本 repo 只記錄它對 CEH / CEHP 學習容量與班別 gate 的影響。
- 課程筆記仍維持教育、合法、授權、認證準備用途。

## Connection Map

- Current registration analysis: `../2026-07-01-ucom-registration/analysis-and-study-bridge.md` keeps the original registered CEH 台北 `2046` and CEHP 台北 `26408` facts, plus the payment / exam-rights gate.
- Study plan: `../../study-plan/pre-course-prep.md` carries this decision as an administrative gate so study work can continue without treating the class change as completed.
- Ownership bridge: `../../docs/ownership-and-planning-bridge.md` defines this repo as the canonical CEH / CEHP learning home and planning as the schedule / capacity mirror.
- Official scope map: `../../curriculum/official-scope-map.md` remains the study backbone in both branches because the class-change decision changes dates, not course scope.
- Planning mirror: `../../../planning-everything-track/data/projects/2026-07-ceh-cehp-certification-training.md` keeps the capacity impact and next gate without copying the full source record.
- Career context: VOISS AI / Max application details remain in the career application packet; this note records only the CEH / CEHP capacity consequence.

## Next Validation Layer

1. 向 Max 確認是否會提供 VOISS AI 書面 offer，以及入職流程與工作開始日期。
2. 書面 offer 到位後，確認 UCOM / UUU 是否可將 CEH 改到台北 `2053`、CEHP 改到台北 `26416`。
3. UCOM / UUU 確認可改班後，再更新 repo README、registration analysis、planning locator 與實際讀書時程。
4. 若書面 offer 未到位，維持目前 CEH 台北 `2046` 與 CEHP 台北 `26408` 的準備節奏。

## Connections

- Current registration analysis: `../2026-07-01-ucom-registration/analysis-and-study-bridge.md`
- Source index: `../README.md`
- Repo overview: `../../README.md`
- Planning mirror:
  `../../../planning-everything-track/data/projects/2026-07-ceh-cehp-certification-training.md`
