# 第一堂 M01–M03 回報與課後規劃來源

收件日：2026-09-22（Asia/Taipei）。Jason 提供完整問答，要求完整筆記、強連接並可據此詳細規劃；明確指定「自學的時間分配等等就當成重要性的參考就好」。

- [未改寫完整原文](source.md)：保存開頭本人回報、20 章矩陣、Cycle 1、五循環、28 組 ports、16 組 commands、合成 mock、Card 範例、DoD 與四個引用，不含外層三引號。
- UTF-8：14,997 bytes；SHA-256：`ca9c60bbd534ec832e63c311754233e1de4380f5d3d6f22a19e740d4a08c83e3`。這是本次保存檔案的完整性值，並非使用者提供的獨立雜湊。
- [完整分析與可執行規劃](../../study-plan/course-synced-review-2026-09-22.md)保留全部內容與逐節覆蓋；[技術表](../../notes/2026-09-22-course-synced-review/ports-and-commands.md)補上 transport、工具限制及一手文件。

## 本人事實、建議與採用範圍

第一句為本人回報：UUU 共五堂，已上第一堂，M01–M03。結合既有正式課表對應 9/20 CEH 2053；作為出席／模組層級的本人證據，不推定教材版本、所有子題覆蓋、Lab 或精熟。其餘問答提供者／回答時間未另說明；其中第一人稱查找、效果判斷、深學分類、分鐘、模擬成績與提案均保留原證據角色。

採用：先鞏固 M01–M03、M04 預習、五循環框架、目的→證據→反制連接、依錯題調整，以及每模組一張既有筆記摘要。880 分鐘矩陣是相對參考；第一階段另依現有容量細化為跨 W39/W40 的最多 240 分鐘候選包。未採用：保證得分、依章節順序推定真實攻擊必然因果、把示例分數寫成個人成績、再新增 10–20 題／章配額或全文重讀義務。

## 四個原始引用的當日查核

| 原引用 | 一手頁面與讀到的內容 | 支持範圍／界線 |
| --- | --- | --- |
| [1] | [官方現行 CEH 頁](https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/)；先前同日已核對版本與格式 | 重用[同日 blueprint 查核](../2026-09-22-ceh-blueprint-weights/verification.md)，125 選擇題／4 小時；v13 教材與 v5 blueprint 分開 |
| [2] | [EC-Council 課程頁](https://ethicalhacking.eccouncil.org/)列 4,000+ tools、550+ techniques | 官方產品範圍自述；未逐一清點工具，也不能由數量證明教學效率或個人所需時間 |
| [3] | [作者 GitHub repo](https://github.com/Shivam-kumar-jha/CEH-v13-Lab-Notes)列 M03 discovery／scan／OS／evasion，M04 enumeration | 只證實作者頁面的內容與分類；技術定義依 Nmap、IANA、RFC、工具上游。其「Enumeration tells what's exploitable」過度簡化，列舉本身不證明可利用性 |
| [4] | [Training Camp](https://trainingcamp.com/ceh-practice-test/)自述 50 道 original scenario questions、90 分鐘與選項解析 | 作者／產品自述；沒有獨立稽核所有題目品質、合法性或正式考試代表性，不從題庫推估官方頻率 |

原文四個 URL 與追蹤參數不改；筆記使用清理過的來源連結。ports／commands 各列的技術來源、日期及未執行界線在技術表。

## Owner、容量與再利用

Jason 提供課堂狀態與規劃偏好；Codex 保存來源、連接已有題本與筆記、核對技術內容及配置容量。詳細教材、題目、本人結果由 CEH repo 擁有；[Planning 今日日誌](../../../planning-everything-track/weeks/2026-W39/days/2026-09-22.md#ceh-course-synced-review)擁有記錄狀態、日期與下一關。

保留共享每週 240 分鐘與課日最多 25 分鐘，9/25–28 不增加任務；時段啟動依實際已用與可用時間。此紀錄補上本人回報的上課範圍，但未新增個人首答、信心、實作或文章成果。使用對象為本人、教學代理及週回顧；不寫入全域記憶。

## 完成檢查

- 原文保存檔案 SHA-256 一致，20 列章節、四個引用具備；重要性矩陣加總 880 分鐘。
- C1 活動表合計 240 分鐘；日期視角 W39 75＋W40 165＝240，9/25–28 零新增配置，10/4 課日上限 25。兩個視角不相加。
- Ports／commands 完整核對 28／16 列，技術來源與適用限制另列；沒有執行網路命令。
- 目前兩庫待提交變更中的 158 個新增／修改相對連結及錨點檢查通過，涵蓋前一筆 blueprint 筆記與本次規劃。
- Planning repository／knowledge／metrics validators 通過；44 個既有 repository 警告、0 個新增。9/22、9/23、10/3、10/4 agenda 檢查通過；10/4 為 Red，其他抽查日仍 Unknown。兩庫 `git diff --check` 通過。
- 題目、答案、registry 與 fixtures 未變更，沿用同日已通過的 practice-bank 檢查；本次沒有重新施測或新增學員結果。
