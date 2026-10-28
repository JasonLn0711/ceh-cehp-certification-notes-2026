# CEH M01-06｜Security Controls、Defense in Depth — v1.1.0

**結論：2026-10-28 完整原文修訂已發布，繁中與英文正式頁已讀回核實。**

[來源索引](../source/2026-10-28-one-concept/README.md) · [新路線](../study-plan/core-route-2026-10-27.md) · [穩定概念索引](../study-plan/core-concept-index-2026-10-27.md)

## 教材與版本歷史

- v1.0.0：八節完整教學及一題檢核，已先於對話交付。完整中英教學與參考答案仍保存於來源目錄，未覆寫或刪除。
- v1.1.0／revision 2：使用者提供的九節完整原文作主要教材，舊稿僅作歷史及局部補充。這是同一 M01-06 的內容修訂，不新增概念交付，不改排程或個人理解紀錄。
- 保留既有 ID 與網址；本筆同步只含 M01-06，不混入其他待發布課程或 M01-05 修訂。

<a id="user-source-revision-2026-10-28"></a>
## 原文、英文翻譯與公開編修稿

[完整原文快照](../source/2026-10-28-one-concept/M01-06-user-source-2026-10-28.md)逐 byte 保留：17,685 bytes、568 個邏輯行，末行無換行；SHA-256 `fe7be76b83875763d665b0be74f2209a7c30b2c74aae77e3c7b2566a43939418`。

[完整英文翻譯](../source/2026-10-28-one-concept/M01-06-user-source-2026-10-28.en.md)、[繁中詳細稿](../source/2026-10-28-one-concept/M01-06-detailed-teaching-2026-10-28.md)與[英文詳細稿](../source/2026-10-28-one-concept/M01-06-detailed-teaching-2026-10-28-en.md)分開保存。公開詳細稿從網站 JSON 轉譯，每語 225 blocks、九節、五表、七份文字流程與三個預設收合解答；五項局部校訂及概念橋接明示區隔，不改原始快照。

NIST SP 800-53 CP-9／CP-10 官方 PDF 可讀，支援備份及復原檢驗補充；原引用 CISA PDF 取得 403，保留查核限制，不宣稱已讀取該受限全文。

### 概念連結

- [M01-02 資產／風險](m01-02-publication.md)：先辨認資產及可能損害，再選擇控制措施。
- [M01-03 授權／ROE](m01-03-publication.md)：測試控制有效性仍須在明確授權內進行。
- [M01-05 攻擊階段與行為](m01-05-publication.md)：用攻擊路徑思考多層控制，但單一告警不等於完整攻擊已成立。
- M01-07 風險管理／事件應變與 M09-01 社交工程／人際信任為相關教學，正式發布仍待核驗；此處僅連到[既有概念索引](../study-plan/core-concept-index-2026-10-27.md)，不宣稱相關新頁已上線。

## 發布收據

- [繁中正式頁](https://learn.cs-kairos.com/courses/ceh/v13/m01/concepts/m01-06/) · [英文正式頁](https://learn.cs-kairos.com/en/courses/ceh/v13/m01/concepts/m01-06/)
- 網站 [PR #42](https://github.com/JasonLn0711/kairos-learning/pull/42)，核實 head `164b73aa005b23a3b78a1cb539c9b35d3937c69c`。
- Merge commit：`bfc7bb7d4115ba9d5346be6641391242fb0ac646`。
- [CI 40699684096](https://github.com/JasonLn0711/kairos-learning/actions/runs/40699684096)：success。
- [Pages 40699936665](https://github.com/JasonLn0711/kairos-learning/actions/runs/40699936665)：success。
- 正式中英頁 curl HTTP 200；各 225 blocks 的正文、表格儲存格、七份流程與三題答案全文讀回零缺漏，版本 v1.1.0。
- 各頁九節、五表、七份直接呈現流程、三個預設收合答案；正式 CSS 淺底 `#f2f6f5`、深字 `#18252c` 已核實。

## 測試、證據界線與驗收

本地 27 tests 通過，Svelte 零錯誤／警告，publication boundary 通過；226 HTML／202 CEH 頁 release 檢查通過，32 個允許的問答／參考解答 disclosure 預設收合。原文 byte 數與 SHA-256 已核對。

以上涵蓋構建、正式文字／DOM 與 CSS 證據，不宣稱已完成瀏覽器視覺驗收。urllib／部分網頁工具曾收到 403；正式讀回採成功的 curl 回應，工具限制與發布結果分開記錄。

維持初學者完整教學、台灣慣用語繁體中文、首見術語白話說明及生活例。正文與圖表直接呈現，程式碼淺底深字，答案預設收合。參考答案不等於個人回答或理解；公開文件不包含私人訊息識別碼、原始私人筆記或個人理解狀態。合法授權的合成教學不操作第三方目標。
