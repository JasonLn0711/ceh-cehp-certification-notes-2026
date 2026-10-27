# M01-02 資產、威脅、弱點、風險｜初版發布

[公開教學來源](../source/2026-10-27-one-concept/M01-02-teaching.md) · [閱讀路線](../study-plan/core-reading-order-2026-10-27.md) · [中文頁](https://learn.cs-kairos.com/courses/ceh/v13/m01/concepts/m01-02/) · [英文頁](https://learn.cs-kairos.com/en/courses/ceh/v13/m01/concepts/m01-02/)

2026-10-27，v1.0.0／revision 1，全程閱讀順序 2。五節教學與一題開放檢核；實際 Q&A 留空，不表示理解已確認。下一單元 M01-03。Northstar 為合成紙上案例，沒有操作真實目標。

中文 30 個來源片段逐一保留；標題與時段改由頁面 metadata 表示，排除最後私人交付狀態句。原件另存私人來源位置，公開來源不含私人進度。正文直接呈現；本課文字條列足以清楚表達，未新增重複圖解。

[PR #34](https://github.com/JasonLn0711/kairos-learning/pull/34) 由 draft 經檢查後合併。實作 13cd752a242a9488ce2d6ecc1ccf9d0c9eabdd27；部署 dfed52f37f64c102e3b4468ac2a52a472e5b7b50。[品質 CI](https://github.com/JasonLn0711/kairos-learning/actions/runs/40453505939) 與 [Pages](https://github.com/JasonLn0711/kairos-learning/actions/runs/40453598286) 成功。

內容驗證、三個測試檔、Svelte 零錯誤／警告、draft/future 邊界建置、218 HTML release 檢查通過。194 CEH 頁僅既有四個實際 Q&A 收合。雙語結構／六錨點一致；GX10 Brave 本機與正式雙語 320／390／1280 無溢出，全文讀回，鍵盤錨點通過，前後概念為 M01-01／M01-03。三個遠端檔案 blob hash 與本機一致。

NIST Asset、Threat、Vulnerability、Risk、Residual Risk 原始詞彙頁已查核。未聲稱螢幕閱讀器完整認證。Planning 同步另列待處理，未重試先前被拒操作。


<a id="detailed-revision-2026-10-27"></a>
## v1.1.0 詳細修訂 — 2026-10-27

**狀態：2026-10-27 已部署並完成正式雙語全文與 SVG 讀回；瀏覽器視覺／鍵盤驗證未完成。** 上方 v1.0.0 的 PR、CI、部署與驗收證據完整保留，不能當成本次 v1.1.0 的發布證據。

[完整詳細教學](../source/2026-10-27-one-concept/M01-02-detailed-teaching.md)已保存。本次擴寫既有概念，ID `M01-02`、路線順序 2、中文／英文網址均保持不變。依詳細教學內容保存七節：咖啡廳四概念、各概念與合成醫院案例、Northstar 六步分析流程、三組常見混淆與 Severity/Risk 差別、觀察／推論／驗證、記憶口訣、兩組理解測驗。新增詳細說明屬 MINOR 內容版本；舊[初版文字](../source/2026-10-27-one-concept/M01-02-teaching.md)保留，不以新教學覆蓋歷史。

**教學校訂與限制：** `Risk ≈ Likelihood × Impact` 是入門簡化，不是假稱精確通用公式；風險需結合情境、防護與後果。修正權限不代表過去沒有複製資料；沒有存取紀錄不證明從未存取。公開衛教資料仍有完整性與可用性風險。咖啡廳、醫院與 Northstar 均為合成教學案例，只描述合法授權的測試與證據，不操作真實目標。

**參考解答：** 後續要求已明確採用預設收合、白話繁中解答，取代原稿第七節「先不公布答案」。這是教學參考答案，不新增虛構的學員 Q&A，也不證明讀者理解。程式碼採淺底深字，正文及圖表直接呈現；長期要求見[現行編修規範](public-teaching-bridge-2026-10-23.md#ceh-answer-presentation-2026-10-27)。

**關聯：** [新路線](../study-plan/core-route-2026-10-27.md) · [穩定概念索引](../study-plan/core-concept-index-2026-10-27.md) · [閱讀規則](../study-plan/concept-reading-2026-10-22.md) · [前置 M01-01 CIA](m01-01-publication.md) · [M05 弱點分析閱讀路線](../notes/m05-vulnerability-analysis/reading-route.md)。私人日誌／週計畫保持既有私密責任邊界，本次公開文件不寫入私人日誌或週計畫。

**本次發布證據：** [網站 PR #36](https://github.com/JasonLn0711/kairos-learning/pull/36)，實作 `34ccad102831433dc60f680c1bde8512f09d7a01`，main merge `730839f9e99e5f98781e916ddeca35d6948bd0df`。[品質 CI 40484954689](https://github.com/JasonLn0711/kairos-learning/actions/runs/40484954689) 與 [Pages 40485095723](https://github.com/JasonLn0711/kairos-learning/actions/runs/40485095723) 均成功。

本地內容驗證、24 個單元測試、Svelte 0 errors/0 warnings、draft/future 發布邊界及 218 HTML release checks 通過。194 CEH 頁只有 8 個 Q&A／參考解答 disclosure，皆預設收合；新課每語言各 2 個。Code `#18252c`／`#f2f6f5` 對比 14.39:1；npm audit 無 high/critical，沿用依賴仍有 3 low。

正式中英文 HTTPS 頁逐一對照各 138 個 source blocks 的可見文字（含表格、答案與圖解），無缺漏；四個 SVG 下載與來源 bytes 完全相同：evidence-levels en 1,868／zh 1,740 bytes，risk-context en 2,002／zh 1,820 bytes，皆小於 100,000 bytes。舊網址、ID 與初版歷史保留。完整 HTML 因建置產物差異未宣稱位元相等。

**驗證限制：** urllib HTTPS 403、web 工具無法開頁，標準 curl HTTPS 讀回成功。雲端 Chromium 因 sandbox socket 限制無法啟動，故 320／390／1280 的實際視覺、鍵盤與互動測試未完成，不能沿用 v1.0.0 的瀏覽器結果當成本版通過；未操作未授權的使用者電腦。
