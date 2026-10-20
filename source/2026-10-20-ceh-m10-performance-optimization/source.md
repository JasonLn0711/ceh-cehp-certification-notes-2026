# 原始要求與採納決策

記錄日期：2026-10-20，Asia/Taipei。

## 原始要求（逐字）

> 請將這次的所有發現通通詳實的記錄下來，並且規劃完整的優化方案，優化目標以「大幅縮短工作時間」、「調整長章節排程，降低最後只剩 C11 的等待」、「修正反覆重複整理並打包重素材以及所有東西」、「拆開打包與影音驗證的依賴，讓打包修正只重驗受影響項目」、「先用小範圍檢查修正共用元件，再執行完整 QA，減少整批截圖作廢重跑」、「建立每次執行的獨立階段計時，分開呈現首次改版、例行製片、失敗重跑與交付時間」、「每一句旁白的間隔修正為 0.3秒、每一章中間的間隔修正為 0.8秒」、「影片製作的靈活性設計不應只有文字方塊等 blocks ，還應該有各種圖示等等」為目標，來優化並修正影片生成規範。

## 實作授權（逐字）

> Implement the plan.

## 使用者選項答案（逐字）

- 章間：合計 0.8 秒 (Recommended)
- 交付：迭代增量、發行完整 (Recommended)
- 視覺：圖示與語意圖解 (Recommended)
- 時間目標：減半為主、一小時為進階目標 (Recommended)
- 最終驗收：產出一次新版完整 M10 (Recommended)
- 句間範圍：只改場景內句間 (Recommended)
- 基準成本：配對片段＋一次完整發行 (Recommended)

## 採納的解釋

章間 0.8 秒是結尾 0.5＋開場 0.3，不再新增第三段。影格對齊另列。句間 0.3 秒只適用同場景相鄰旁白；quiz 優先維持一秒。日常不封裝，正式發行一個可獨立還原 ZIP。保留核准聲音、字體、風格、內容與歷史發行。效能目標不授權降低品質。配對片段可證明其範圍內改善；整片歷史比較不冒充受控 A/B。

狀態：source preserved；adopted decision；implementation in progress。公開發布與人工作品驗收分開。


## 後續聚焦與記錄／發布授權（逐字）

> 先修正影響最大的兩大因素，謝謝

> 請再修正影響最大的兩大因素，謝謝

> Using FIRST PRINCIPLE, and please take notes on my day note in the `planning-everything-track` repo, and update the relevant docs, files, and contents for it.
> Please update all the commits separately on git, and push this branch to the remote main branch of the github repo. (If there were conflict among commits, i would like to keep both local commits and remote commits.)
> And build strong connection with all other relevant files, docs, and contents.

## 2026-10-20 接續狀態與路由

上方 implementation in progress 保留為當時狀態。後續 [v1.2 執行紀錄](../../docs/video-production/M10_EFFICIENCY_IMPLEMENTATION.md)已有完整本機交付；[0.5.1／0.5.2 維護報告](../../docs/video-production/M10_HIGH_IMPACT_FIXES.md)分別記錄實測改善、拒絕的候選與尚未執行的原生續跑驗證。公開程式碼提交與完整影片人工驗收分開。

FIRST PRINCIPLE：稀缺資源為製片／覆核等待與可信效能證據。CEH 持原文、規範、程式與驗證；大型媒體留在既有本機 Videos workspace。Planning 僅持 [10/20 日誌](../../../planning-everything-track/weeks/2026-W43/days/2026-10-20.md#ceh-m10-efficiency-2026-10-20)、[專案狀態](../../../planning-everything-track/data/projects/2026-07-ceh-cehp-certification-training.md#ceh-m10-efficiency-2026-10-20)與容量／下一關。這次授權涵蓋兩個 repository 的分開提交與 main 推送；btop、其他工作及公開影片上傳保持各自範圍。
