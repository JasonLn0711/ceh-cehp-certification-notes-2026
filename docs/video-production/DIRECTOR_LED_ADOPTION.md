# 逐場景導演流程：來源、採納與驗證

日期：2026-10-21（Asia/Taipei）。Canonical owner：CEH repository。[工作流程](DIRECTOR_LED_WORKFLOW.md) · [Prompt 指南](DIRECTOR_PROMPTS.md) · [M11 製作紀錄](../../notes/m11-session-hijacking/video-production-2026-10-20.md)。

## Source preserved

以下是本次需求與選擇的原文；選項標籤中的「你／我」以當時助理對使用者提問的角度保留。

> 請問，我們在製作這樣的影片的時候，我其實都只有給你主題（例如： CEH M11），相關的細節以及內容都是由你構思的嗎？如果我們想要主導並設計相關內容、表現方式以及運鏡等等，可以怎麼做呢？我們可以怎麼優化呢？請協助我們優化

第一次選擇：

- `creative_control`: 「逐場景導演」
- `optimization_scope`: 「先完成通則與模板」

第二次選擇：

- `drafting_ownership`: 「你定內容、我設計畫面」
- 補充原文：「你要告訴我，我可以怎麼下 prompt」
- `review_batching`: 「一次審閱全片」

執行指令原文：

> Implement the plan.

## Accepted interpretation / adopted decision

使用者擁有內容與講稿決策，助理設計畫面、動作、運鏡與轉場。全片分鏡完成後一次送審，每場分別記錄使用者決定。本次採納的計畫範圍是通則、模板、prompt 指南、M11 S06 填寫範例及文件整合；不是完整影片改版或新運鏡實作。

既有 M11 自動製作與新的導演流程有不同決策責任。舊版 runtime、素材、影片與所有 QA 保持原狀，歷史 agent review 不轉寫成使用者創作確認。這些偏好寫入本專案文件，不修改全域記憶或 agent 設定。

## Implementation / evidence

- implemented：工作流程、內容簡報、分鏡、審閱／修改表、prompt 指南與 S06 範例；系列基線、設計／QA 文件、索引與 M11 紀錄的連結。
- tested：文件驗證結果見 [驗證收據](evidence/director-led-docs-2026-10-21.json)。測試範圍只有文件、來源對照與保留檢查。
- proposed：模板自動編譯、新的鏡頭狀態與運鏡、引擎創作核准 gate、視覺編輯器、實際預覽／改版。
- blocked：本次文件範圍無已知阻礙；待使用者確認的示例保留 pending，不假裝已接受。
- publication：本次未 commit、push 或公開上傳影片。

## Next validation layer

未來新片先填內容簡報與唯一講稿來源；助理交付完整分鏡及所有場景審閱清單。使用者選定版本與下一階段後，才開始該階段。新視覺能力屆時須有實際幾何、seek、截圖與音訊回歸證據。縮時效益仍待實測；文件完成不代表新的影片或運鏡已測試。

Later Git publication and Planning status: [October 22 closeout](PUBLICATION_2026-10-22.md). Earlier publication statements remain historical snapshots.
