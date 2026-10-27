# M04-12 列舉防護｜初版發布

[公開教學來源](../source/2026-10-27-one-concept/M04-12-teaching.md) · [中文頁](https://learn.cs-kairos.com/courses/ceh/v13/m04/concepts/m04-12/) · [英文頁](https://learn.cs-kairos.com/en/courses/ceh/v13/m04/concepts/m04-12/)

初版 v1.0.0、revision 1：五節教學、一題未作答小檢核，說明服務／網路、身分／權限、資料／傳輸與維護／監控，以及修改設定和驗證行為的差別。沒有執行設備操作。下一核心 M05-01；12 核心與 7 選讀是教學設計，選讀不阻擋 M05。

技術原文與順序保留，標題、摘要、項目符號依網站語意呈現；僅排除結尾私人交付／理解狀態片語，保留邀請回答與課程路線說明。精確原文另存私人來源庫。新增並列驗證圖明標「網頁補充」，比較限制訪客與保留正常監控，沒有暗示雙因素認證。HTML/CSS 響應式重排，SVG 固定布局縮放；中文 1478 bytes、英文 1716 bytes。正文圖解直接呈現，沒有新增收合或虛構 Q&A。

## 發布與驗證

[PR #32](https://github.com/JasonLn0711/kairos-learning/pull/32) 先以 draft 建立，品質檢查通過後合併。實作 `4087e7252be332cbcd8bedb7eb2169419a99646e`；部署 `89923ed66e8ef599d55a42b3eeebbbbd07aa78bc`。[品質 CI](https://github.com/JasonLn0711/kairos-learning/actions/runs/40424845837) 與 [Pages](https://github.com/JasonLn0711/kairos-learning/actions/runs/40424973473) 均成功。

內容驗證、三個測試檔、Svelte 零錯誤／警告、發布邊界建置及 214 HTML release 檢查通過。190 CEH 頁僅既有 4 個真正 Q&A 收合。每語言 44 個正文／圖解片段核對。GX10 Brave 正式雙語全文與本機一致；320／390／1280px 無水平溢出，錨點完整、鍵盤導航通過。正式雙語 SVG DOM 與本機相同。

四個原文主要來源 RFC 5936、NIST SP 800-53、Microsoft LDAP signing 及 NCSC reduce exposure 均成功讀取；連結保留於教學。

限制：先前待批准的原生存檔未重試，未宣稱原生下載或正式 HTTP 位元組比對通過；未進行完整螢幕閱讀器認證。
