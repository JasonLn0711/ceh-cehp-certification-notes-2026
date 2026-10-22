# 長片製作與儲存流程要求

記錄日期：2026-10-22（Asia/Taipei）。來源：本次使用者對話。

## 原始要求

> 為什麼做完影片之後，會留下很多很大的檔案呢？我們可以怎麼優化，來節省硬體空間呢？

> 請優化我們做的 ceh 以及 課業複習的長片的製作流程以及細節，並且寫成規範（規範中要留下日期、版本號等等）。

## 採用解讀與範圍

改善 CEH 英文長片、課業中文概念長片及 MATLAB 實作長片的儲存與封裝流程，記錄可重用的製作、交付和保存規範。共用引擎與規範由 CEH repository 維護；各課業教材、逐字稿與原交付證據留在課務資料夾。這項要求授權流程實作與規範更新；本次以新建測試資料驗證，不刪除既有成片、封裝、語音、歷史工作區或實驗紀錄。

## 實作與證據入口

- [長片製作與儲存規範 v1.0.0](../../docs/video-production/LONGFORM_STORAGE_STANDARD_v1.0.0.md)
- [只讀容量盤點](../../docs/video-production/evidence/longform-storage-inventory-2026-10-22.json)
- [驗證紀錄](../../docs/video-production/evidence/longform-storage-validation-2026-10-22.json)

規範採納、程式測試、既有影片技術驗證、人工聽看、公開發布與學員學習各自記錄。新的封裝實作未用於重封任何歷史交付包。

## 第一批歷史副本清理授權 — 2026-10-22

接續原始要求：

> 若我們想要刪除一些舊檔，我們可以怎麼處理。

使用者選擇：`驗證副本與暫存 (Recommended)`。完整方案限定四個課業工作區的 `output/archive-verification/`；核對後將 CEH M11 的 partial 檔排除，因它是具名保留的歷史製作證據。方案要求重新核對保留 ZIP、全部內容、使用狀態與精確路徑，留下清理前後紀錄；正式交付、來源與語音保留。

使用者執行指示原文：

> Implement the plan.

本段授權接續前述「本次未清理」的流程實作快照。這次清理的實際結果以[獨立批次紀錄](../../docs/video-production/evidence/longform-cleanup-2026-10-22/)為準；未授權擴大到 CEH 測試工作區或其他版本。

## 第二輪優化授權 — 2026-10-22

使用者要求原文：

> 請再一次優化我們的製片以及存儲空間

方案選擇記錄：`流程＋已驗證副本`、`解壓後一鍵還原`、`代表片段＋完整還原`。採用範圍為華語章節／母片／QA 的輸入與輸出雜湊重用、精確位元組去重封裝與離線還原、三條真實封裝路線完整還原、原生代表片段比較，以及七個具名舊 staging 目錄的全檔核對。唯一資料、使用中的依賴及不明狀態整個目錄保留。

使用者執行指示原文：

> Implement the plan.

此輪維持既有音質、畫質、語速、時間政策及併發上限；不產生新 TTS、不重製整部長片、不覆寫歷史正式 ZIP。版本為引擎 `0.6.0`、規範 `2.0.0`。實際執行與未通過項目以[第二輪證據](../../docs/video-production/evidence/longform-round2-2026-10-22/)為準。

## Publication request — 2026-10-22

```text
Using FIRST PRINCIPLE, and please take notes on my day note in the `planning-everything-track` repo, and update the relevant docs, files, and contents for it.
Please update all the commits separately on git, and push this branch to the remote main branch of the github repo. (If there were conflict among commits, i would like to keep both local commits and remote commits.)
And build strong connection with all other relevant files, docs, and contents.
```

Accepted scope: publish the completed long-form production/storage implementation, standards and evidence; connect the Planning day, project and week records. Preserve unrelated work and both Git histories. Git publication is separate from public media delivery and human acceptance.
