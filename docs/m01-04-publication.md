# CEH M01-04｜攻擊面與攻擊向量 — v1.0.0

**狀態：2026-10-27 網站已正式發布並完成雙語內容讀回；本文件隨獨立 notes 草稿 PR 供審閱，合併結果另行核驗。**

## 教學與來源

- [完整繁中教學](../source/2026-10-27-one-concept/M01-04-teaching.md)與[英文教學](../source/2026-10-27-one-concept/M01-04-teaching-en.md)。
- [繁中參考解答](../source/2026-10-27-one-concept/M01-04-reference-answer.md)與[英文參考解答](../source/2026-10-27-one-concept/M01-04-reference-answer-en.md)獨立保留；網站預設收合，不當成實際使用者作答。
- [新路線](../study-plan/core-route-2026-10-27.md) · [穩定 ID 索引](../study-plan/core-concept-index-2026-10-27.md) · [現行呈現規範](public-teaching-bridge-2026-10-23.md#ceh-answer-presentation-2026-10-27)。

穩定概念 ID `M01-04`；正文依初學者需要提供完整白話解釋、生活例、條件與限制、防護及證據判讀，再以一題小檢核支持理解。所有案例為合成教學，沒有操作真實第三方目標。網站的正文與圖表直接呈現，程式碼採淺底深字，僅問答／參考答案預設收合。

## 網站與驗收證據

- 正式中文頁：<https://learn.cs-kairos.com/courses/ceh/v13/m01/concepts/m01-04/>
- 正式英文頁：<https://learn.cs-kairos.com/en/courses/ceh/v13/m01/concepts/m01-04/>
- [網站 PR #39](https://github.com/JasonLn0711/kairos-learning/pull/39)，實作 `e4433ec8222569339e1c9f2a6201661f018764a4`，合併 `a327811c6e025c3464639dc1019327a4b4b08584`。
- [品質 CI 40496309318](https://github.com/JasonLn0711/kairos-learning/actions/runs/40496309318) 與 [Pages 40496439963](https://github.com/JasonLn0711/kairos-learning/actions/runs/40496439963) 均完成且成功。
- 本課正式中英文各 **86 source blocks** 全文字讀回吻合，v1.0.0；每頁一個參考答案預設收合。整批 26 tests、Svelte 零錯誤／警告、224 HTML／200 CEH 頁驗證通過；全站 18 個允許的解答／問答 disclosure 均預設收合。
- 實際手機／桌面視覺與鍵盤互動未取得新的通過證據；HTTP／文字讀回不當作視覺驗收。
- 不將網址存在、草稿、提交、預排日期或網站測試當成實際交付／理解完成；公開文件不保存私人訊息 ID 或個人理解狀態。本輪文件整理未修改排程，也未操作 Planning。

## 完整來源檔案識別

- `M01-04-reference-answer-en.md`：1,455 bytes；SHA-256 `7cb9e68a60cdaf030830565d0e192e8297abd49756f18d208f0172b08cba15e6`。
- `M01-04-reference-answer.md`：1,012 bytes；SHA-256 `90cffe18a3aec595b0a68efd3bcad2d569a8f969ba3132221a14335be2429c39`。
- `M01-04-teaching-en.md`：14,658 bytes；SHA-256 `5207f17a26fb7eaadedb67660366cfd1b798ca04b68752e167826f621ba08fcb`。
- `M01-04-teaching.md`：11,951 bytes；SHA-256 `d29123390dc604736e24a61090f007ddeb96f21af84a35f146fdfd308979e2db`。


<a id="user-source-revision-2026-10-27"></a>
## v1.1.0 使用者原文優先修訂 — 已發布核驗

**本節狀態：2026-10-27 原文已完整保存，網站 v1.1.0 已部署且完成正式雙語讀回。** 上方 v1.0.0 的完整來源、參考解答及已核實的發布歷史均保留，不以新版本覆蓋。

[原文完整快照](../source/2026-10-27-one-concept/M01-04-user-source-2026-10-27.md)是本輪主要教材，逐 byte 保存 UTF-8 原檔，包含原來的標題、段落、表格、流程與引用網址，不清理來源快照。實測 **15,097 bytes、456 個邏輯行（末行無換行）**；SHA-256 `e3450aadc4bf34bed9a03b01c84e780fc0ebce3ae21231898a7e968c668ef599`。

本次在相同 `M01-04` 概念與既有中英文網址上擴充完整教學。原先[初版教學](../source/2026-10-27-one-concept/M01-04-teaching.md)保留，可作局部且可辨識的補充，不拿較短版本取代使用者原文。正文與圖表直接呈現，程式碼採淺底深字，理解測驗的白話參考解答預設收合。公開教學正規化與來源快照分開記錄。

這是已交付概念的內容修訂，不新增交付次數、不更動學習路線或排程，也不代表讀者已回答或理解。公開文件不存私人訊息識別碼與個人學習狀態；不變更 M01-03／M01-05 或 Planning。

[公開詳細教學正規化稿](../source/2026-10-27-one-concept/M01-04-detailed-teaching.md)從網站本輪 v1.1.0 JSON 產生，與原文快照分開保存。雙語各 186 blocks、七節、五表、三份文字流程與三個預設收合參考解答；逐行／儲存格原文核對無遺漏。

本輪局部補充包含 NCSC 官方來源、Authorization 在存取控制與測試許可兩層意義，以及合成案例提示。NIST 路徑大小寫、OWASP 缺少的 `.html` 與引用追蹤參數屬公開頁顯示／連結正規化；原始快照不變。

**本輪發布核驗：** [網站 PR #40](https://github.com/JasonLn0711/kairos-learning/pull/40)，實作 `f7d85b7d775144b3d8c8e8731df2efc2117da5eb`，合併 `70de41952d1c4f6ac9af6769a04a2637d012c768`。[品質 CI 40498644379](https://github.com/JasonLn0711/kairos-learning/actions/runs/40498644379) 與 [Pages 40498781216](https://github.com/JasonLn0711/kairos-learning/actions/runs/40498781216) 均完成且成功。正式中英文 v1.1.0 各 186 blocks 全文讀回無缺漏；每頁三題參考答案預設收合，三份文字流程直接呈現。

本地 26 tests、Svelte 零錯誤／警告、224 HTML／200 CEH 頁檢查通過；全站 22 個允許的解答／問答 disclosure 均預設收合。實際手機／桌面視覺與鍵盤互動沒有本輪新通過證據，HTTP／DOM 與內容讀回不冒充視覺驗收。

本輪另讀回正式 CSS：程式碼背景 `#f2f6f5`、文字 `#18252c`；中文正式 HTML 三個 `pre` 直接呈現。這是 CSS／DOM 證據，不取代未完成的視覺／鍵盤檢查。
