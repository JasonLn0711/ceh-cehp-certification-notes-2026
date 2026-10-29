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


<a id="m09-04-publication-1-0-0-2026-10-29"></a>
## 2026-10-29｜M09-04 v1.0.0 已部署；正式讀回待核

**[PR #50](https://github.com/JasonLn0711/kairos-learning/pull/50) 已於 10:11:28 UTC 合併；merge SHA `1f6db6817d0ef0098ef1ab9137cdff175aab0e0f`。[Pages 40855575160](https://github.com/JasonLn0711/kairos-learning/actions/runs/40855575160) completed／success，部署完成於 10:12:18 UTC（台灣 18:12:18）。** PR 合併狀態與全部部署步驟已重新讀回；精確 merge-SHA 與完成時間由發布流程核實。

本課先整合已部署的 [PR #51](https://github.com/JasonLn0711/kairos-learning/pull/51)（`505534eb29cc8b7b051bb7c44adc090dc701a15e`），重新產生全部 8 張 SVG、inline bundle 與 ZIP。SVG 以 `viewBox`／`preserveAspectRatio` 等比例適應欄寬，不保留固定根節點寬高；沿用已核准的安全 SVG serializer／共用顯示元件。

- [繁中教材](https://learn.cs-kairos.com/courses/ceh/v13/m09/concepts/m09-04/) · [英文教材](https://learn.cs-kairos.com/en/courses/ceh/v13/m09/concepts/m09-04/)
- 中英各 **78 個內容區塊、4 張 inline SVG、3 段預設收合參考解答**；正文與圖表直接呈現，實際 Q&A 維持獨立。
- 最終 head `0f4a1a3282c73dc1f124a0d1e1252f081ab7a5bd` 的 [CI 40855355914](https://github.com/JasonLn0711/kairos-learning/actions/runs/40855355914) 通過；發布流程核實 tree `2aec766f1efca7c0c70d24005899c2f6e0cf37f2` 與本機已測試版本相同。
- 41 項測試、型別、內容、發布邊界、完整靜態 release、下載 checksum 檢查通過；audit 無 high／critical，保留 5 個既有 low 項目，不宣稱零風險。Pages 的 `deploy-pages` 步驟亦為 success。
- **正式網站正文／下載內容讀回、瀏覽器／手機呈現與鍵盤操作仍未完成驗證。** 未重試受限路徑；部署成功不等同全部呈現與互動驗收通過。先前 Inkscape 圖形幾何檢查不冒充正式瀏覽器測試。

上方草稿及 76 區塊為較早快照；本節為最新發布狀態。穩定概念 ID、既有主稿來源與前後課連結保持；M09-05 仍是待交付導覽而非已發布教材。
