# M09-04｜情境編造、誘餌與尾隨進入

2026-10-29；Module 09：Social Engineering。現行 161 單元教學設計中的第 11 單元；161 是教學規劃數量，不是假稱官方固定考點數。

## 教學與發布界線

完整初學者繁中與配對英文教材、4 組雙語原生 SVG 及 3 項參考解答已備妥。網站發布與正式內容核驗另行追蹤；此文件不是上線證明。正文、表格、圖形直接呈現，僅參考解答預設收合；編輯參考解答不冒充實際學員 Q&A。

## 概念與圖形

**合理故事、誘人的東西、已開啟的門，都不等於這次行動已獲授權。**

- Pretexting：情境編造，以理由使異常請求顯得合理；不等於電話或簡訊管道，也不完全等同冒充身分。
- Baiting：以誘因促使不安全行動；結果可能是資料揭露或惡意程式，不限定 USB，也不表示所有贈品都是攻擊。
- Tailgating：未完成本人的進入檢查，利用他人的通行跨越實體管制邊界。Tailgating／Piggybacking 命名因來源而異，不武斷將是否知情列為通用必要差別。
- 4 組圖依序為概念關係、獨立查證決策、未知內容安全處理、實體邊界／人員與門禁證據。虛線關聯、實線流程、假設風險分別標示；不是一條必然發生的攻擊鏈。
- 防護採既有可信聯絡來源、工作與授權範圍查核、最小權限、訪客程序與正式通報。未知 USB 不接到工作或家用裝置，交由獲授權人員決定受控處理。
- 證據分層：找到 USB、不等於已插入、不等於已執行或外洩；刷卡紀錄不等於每個進入者都已獲准。

## 第一手來源

1. [Canadian Centre for Cyber Security：Social engineering ITSAP.00.166](https://www.cyber.gc.ca/en/guidance/social-engineering-itsap00166)
2. [Australian Cyber Security Centre：Learn about social engineering](https://www.cyber.gov.au/guidance/learn-about-social-engineering)
3. [PNG National Cyber Security Centre：Social Engineering](https://www.ncsc.gov.pg/social-engineering/)
4. [University of Florida Information Security：Tailgating](https://it.ufl.edu/security/learn-security/social-engineering/tailgating/)

## 關聯

[閱讀規則](../study-plan/concept-reading-2026-10-22.md) · [現行路線](../study-plan/core-route-2026-10-27.md) · [前課 M09-03](m09-03-publication.md) · [公開教學橋接](public-teaching-bridge-2026-10-23.md#m09-04-2026-10-29)。本課連結 M01 資產、CIA、授權與安全控制；下一單元 M09-05 聚焦內部威脅與身分竊盜。

目標頁（尚未據此宣稱上線）：[繁中](https://learn.cs-kairos.com/courses/ceh/v13/m09/concepts/m09-04/) · [English](https://learn.cs-kairos.com/en/courses/ceh/v13/m09/concepts/m09-04/)。私人聊天識別、交付回執、作答與理解狀態只留私人正本。


## 2026-10-29｜網站草稿 PR #50

[Draft PR #50](https://github.com/JasonLn0711/kairos-learning/pull/50)已建立，初始 head `fe21a1554035731d7618875020210b32f74397c8`，基於已合併的 M09-03 安全 inline SVG 共用元件。中英各 76 個內容區塊、4 張 inline SVG、3 段參考解答；只有問答預設收合。新單元 M09-05 只補齊待交付導覽，不建立空白教材頁。

本機 39 項測試、型別檢查、發布邊界、完整靜態 release／本單元 verifier、歷史下載 checksum 通過；套件稽核無高／重大風險，仍有 5 個 low 項目。8 張產出 SVG 已實際渲染檢查，英文緊密標籤作等義簡化。上述不代表正式手機／瀏覽器或網站上線已核驗。

**狀態仍為草稿；精確 head 的 CI、後續共用 responsive 修訂整合、使用者批准、合併部署及正式讀回未在本節確認。** 不以 PR 建立或本機測試通過宣稱發布。後續若 sanitizer 變更，須重新生成本課 SVG bundle 並重新核驗。
