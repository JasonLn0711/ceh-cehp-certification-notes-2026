# CEH M01-05｜Cyber Kill Chain 與 MITRE ATT&CK — v1.0.0

**狀態：2026-10-27 網站已正式發布並完成雙語內容讀回；本文件隨獨立 notes 草稿 PR 供審閱，合併結果另行核驗。**

## 教學與來源

- [完整繁中教學](../source/2026-10-27-one-concept/M01-05-teaching.md)與[英文教學](../source/2026-10-27-one-concept/M01-05-teaching-en.md)。
- [繁中參考解答](../source/2026-10-27-one-concept/M01-05-reference-answer.md)與[英文參考解答](../source/2026-10-27-one-concept/M01-05-reference-answer-en.md)獨立保留；網站預設收合，不當成實際使用者作答。
- [新路線](../study-plan/core-route-2026-10-27.md) · [穩定 ID 索引](../study-plan/core-concept-index-2026-10-27.md) · [現行呈現規範](public-teaching-bridge-2026-10-23.md#ceh-answer-presentation-2026-10-27)。

穩定概念 ID `M01-05`；正文依初學者需要提供完整白話解釋、生活例、條件與限制、防護及證據判讀，再以一題小檢核支持理解。所有案例為合成教學，沒有操作真實第三方目標。網站的正文與圖表直接呈現，程式碼採淺底深字，僅問答／參考答案預設收合。

## 網站與驗收證據

- 正式中文頁：<https://learn.cs-kairos.com/courses/ceh/v13/m01/concepts/m01-05/>
- 正式英文頁：<https://learn.cs-kairos.com/en/courses/ceh/v13/m01/concepts/m01-05/>
- [網站 PR #39](https://github.com/JasonLn0711/kairos-learning/pull/39)，實作 `e4433ec8222569339e1c9f2a6201661f018764a4`，合併 `a327811c6e025c3464639dc1019327a4b4b08584`。
- [品質 CI 40496309318](https://github.com/JasonLn0711/kairos-learning/actions/runs/40496309318) 與 [Pages 40496439963](https://github.com/JasonLn0711/kairos-learning/actions/runs/40496439963) 均完成且成功。
- 本課正式中英文各 **103 source blocks** 全文字讀回吻合，v1.0.0；每頁一個參考答案預設收合。整批 26 tests、Svelte 零錯誤／警告、224 HTML／200 CEH 頁驗證通過；全站 18 個允許的解答／問答 disclosure 均預設收合。
- 實際手機／桌面視覺與鍵盤互動未取得新的通過證據；HTTP／文字讀回不當作視覺驗收。
- 不將網址存在、草稿、提交、預排日期或網站測試當成實際交付／理解完成；公開文件不保存私人訊息 ID 或個人理解狀態。本輪文件整理未修改排程，也未操作 Planning。

## 完整來源檔案識別

- `M01-05-reference-answer-en.md`：1,110 bytes；SHA-256 `e79218ad2d2ee8fe9f9ff481628810c0dc07a6b245b58deb44e33cf8bcd46fe7`。
- `M01-05-reference-answer.md`：889 bytes；SHA-256 `9e76c3063abd9cccc874ffa9afe346694892fae2667c0a5909f6390ac228dba2`。
- `M01-05-teaching-en.md`：15,106 bytes；SHA-256 `6233e7409baea5ca9e4dd72ebe690838a7b618d377a792f3984f195116257dde`。
- `M01-05-teaching.md`：12,550 bytes；SHA-256 `bb195167dcfecfaf709ef0c71a8235745a4d369544226b58aaeb9f5edec34d44`。


<a id="user-source-revision-2026-10-27"></a>
## v1.1.0 使用者原文優先修訂 — 已發布核驗

**本節狀態：2026-10-27 完整原文已保存，網站 v1.1.0 已發布且完成正式雙語讀回。** 上方 v1.0.0 的來源、解答與發布歷史保持不變，不拿前次證據代表本次結果。

[原文完整快照](../source/2026-10-27-one-concept/M01-05-user-source-2026-10-27.md)為本輪主要教材，逐 byte 保留原始 UTF-8 文字、標題、表格、流程、題目與引用網址，不在快照清理排版或追蹤參數。實測 **19,588 bytes、650 個邏輯行（末行無換行）**；SHA-256 `8724d8be963699df5d29a9406fb4cfd56148417142586ee334aa22b03f33aa26`。

本次仍為同一 `M01-05` 概念、Cyber Kill Chain 與 MITRE ATT&CK，既有 ID、網址、新路線順序及初版教學保留。使用者原文是主要內容；[原 v1.0.0 教學](../source/2026-10-27-one-concept/M01-05-teaching.md)僅作可辨識的局部補充，不取代完整原文。網站正文與圖表直接呈現、程式碼淺底深字、白話繁中參考解答預設收合。

這是教材內容修訂，不新增交付次數、不變更排程，也不把參考答案公布當作本人回答或學會。公開文件不放私人訊息識別碼或個人理解紀錄，不更動其他課程或 Planning。

[公開詳細教學正規化稿](../source/2026-10-27-one-concept/M01-05-detailed-teaching.md)從本輪網站 JSON 轉譯，原文快照不變。

**本輪核驗範圍：** 九節正文、七表、兩份流程與三題完整性；雙語與來源查證／編修差異；網站 PR／commit／CI／Pages 與正式讀回。瀏覽器視覺未執行，仍保留限制。


### 本輪驗證與發布證據

網站 v1.1.0 雙語各 300 blocks，保留九節、七表、兩份文字流程與三題解答。本地 26 tests、224 HTML／200 CEH 頁 release 檢查通過；26 個允許的問答／參考答案 disclosures 預設收合。上述為本地構建結果；正式讀回證據另列如下。

[網站 PR #41](https://github.com/JasonLn0711/kairos-learning/pull/41) 的實作 head 為 `8ea59385b2cb94cacdd84f7d1d3e90a1578b0cc6`，合併 `713d94dc66ab7d9ce1d2f55cd3dd33a1e4d0d7a1`。[品質 CI 40532209604](https://github.com/JasonLn0711/kairos-learning/actions/runs/40532209604) 與 [Pages 40532428192](https://github.com/JasonLn0711/kairos-learning/actions/runs/40532428192) 全部步驟成功。

正式中英文各 300 blocks 全文讀回無缺漏，九節、七表、兩個直接呈現的 `pre` 流程、三個預設收合參考答案；v1.1.0 已確認。正式 CSS `ContentPage.CSSE-Kt5.css` 讀回程式碼背景 `#f2f6f5`、文字 `#18252c`。這是 HTTP／DOM／CSS 證據；本輪瀏覽器手機／桌面視覺與鍵盤互動未執行，不宣稱通過。

局部來源校訂包含歷史 T1193 與現行 T1566.001 的對照。Lockheed Martin 官方索引可供查核；直接讀取來源遇到 403 的限制另行標示，不聲稱受限原文已完整讀取。原始來源快照保持不變，正文中的校訂註與原文分開可辨。
