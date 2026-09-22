# CEH 章節比重原文與查核回執

收件：2026-09-22（Asia/Taipei），使用者於對話提供完整問答，要求完整筆記及跨文件連接。作者、原始回答日期與原查找過程未提供；原文第一人稱查找描述屬來源說法。

- [完整原文](source.md)：保留二十章表、九 Domain、三層建議、概念鏈、版本比較、延伸提案及四個原始引用；不含外層三引號。
- UTF-8 檔案：7,328 bytes；SHA-256：`4c16e51e83afb55e7980eb30d7ee56ba5a4b20503e8d9923ba31b240b76a09eb`。此值核對本次保存檔案，並非使用者提供的獨立來源雜湊。
- [完整筆記及逐段覆蓋](../../curriculum/ceh-blueprint-weights-2026-09-22.md)：來源說法、官方事實、算術推論、編輯補註與未採用提案分開。
- [當日來源核對](verification.md)：官方 certification 入口、公告、v4／v5 PDF、課程考試頁與 CEHStudy 自述；資料檢索不等於個人學習驗收。

## 四個原始引用的處理

| 原引用 | 查核來源 | 處理 |
| --- | --- | --- |
| [1] | [官方 v5 PDF](https://cert.eccouncil.org/wp-content/uploads/2024/04/CEH-Exam-Blueprint-v5.pdf) | 二十列題數、九 Domain；補百分比加總 101% |
| [2] | [CEHStudy](https://cehstudy.com/) | 確認 200／20／10 是網站自述；記錄 M17–M19 對應差異，未逐題審核 |
| [3] | [官方 v4 PDF](https://cert.eccouncil.org/wp-content/uploads/2024/02/CEH-Exam-Blueprint-v4.0.pdf) | 保留歷史數字；用官方版本公告確認生效界線 |
| [4] | [官方現行 CEH 頁](https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/) | 原 north-america URL 重新導向此頁；區分課程與考試版本 |

原文 URL 保留 `utm_source`，筆記引用移除追蹤參數；未修改原文結論來掩蓋補註。完整筆記末節逐項對應全部內容，包括尚未採用的 M05 情境與工具／時間矩陣。

## Ownership 與使用

Jason 提供問題與原文；Codex 保存、核對並連接既有教材。CEH repo 擁有詳細技術／來源分析；[Planning 今日紀錄](../../../planning-everything-track/weeks/2026-W39/days/2026-09-22.md#ceh-blueprint-weights)擁有狀態、容量與下一關，供本人、後續教學代理及週回顧使用。

本次沒有採納新的高／中／低讀書排序，沒有新增題目、個人成績、閱讀分鐘、實作或 Blog 發布。9/22 下載原件與來源採用分開，詳見[原有來源信任決策及本次續註](../../curriculum/important-references.md#rejected-cehv13-download-directory)。

## 完成檢查

- Decimal 算術核對二十章題數與精確比例、兩份九 Domain 表；125 題、M02–M15 的 88 題及官方整數百分比 101% 均一致。
- 保存檔案 SHA-256 與回執一致；原文二十列及四個引用均存在，末節覆蓋表承接全部論點。
- 本次新增／修改的 79 個相對文件連結及錨點通過檢查。
- `python3 assessments/practice-bank/check.py` 通過：600 practice + 250 distinct mock MCQs、keys／registry、25 practical tasks、兩份 blueprint allocation 與五個 fixture checks；沒有個人學習結果。
- Planning repository／knowledge／metrics validators 通過；44 個既有 repository 警告、0 個新增。兩庫 `git diff --check` 通過。

以上為文件、題庫結構與 fixture 驗證，不是獨立心理計量審查或個人準備度驗收。
