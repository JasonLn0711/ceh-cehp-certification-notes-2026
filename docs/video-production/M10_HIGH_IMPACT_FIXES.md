# M10 兩項優先效能修正

本次範圍：章節渲染，以及主片組裝／完整解碼驗證。沿用已完成的長章節優先排程與封裝依賴分離。Canonical owner 為本 repository；稀缺資源為 GPU 製片與操作者等待時間。原始媒體、逐次測量與失敗紀錄保存在 `/home/jnlngx10/Videos/CEH_M10_perf_fix_20261020/evidence/`。本輪不發布 Planning 狀態、不重製或覆蓋已交付影片。

## 起點與驗收範圍

既有 v1.2 主流程 6995.166090 秒，其中章節窗口 4982.271554 秒、master 1178.167320 秒、checks 720.574466 秒。以上是既有紀錄，並非本輪對照組；C11 排程與封裝已改善，不能再重複計算收益。

保留 1920×1080、30 FPS、delivery 編碼品質、原字體／色彩／Tally、旁白基線 0.73、一次 atempo=1.4、句間 0.3 秒、章間 0.8 秒與八個 48000 stereo-frame quiz holds。新場景維持底部 8% 安全區；本輪不新增視覺例外。既有 `LEGACY-M10-SUBTITLE-001` 的範圍不變。

## 修正一：重用同一份連續 AAC 音軌

`master_audio_cache.py` 將完整連續 AAC 與原始 PCM SHA-256、整數 audio frames、語音設定、模型、政策、AAC 192k／48kHz 編碼設定、FFmpeg binary／version 與 cache implementation 綁定。畫面改版而 PCM 不變時，master 使用 `-c:a copy`；首次製作或身分變更仍執行原始 AAC 編碼。它不拼接各章 AAC，也不再執行 atempo。

完成原始編碼後才以 stream copy 保留 AAC。快取內容或收據不符時，重新編碼；收據沒有代表全片驗收。每一部新 master 仍須完整音軌 continuity、八題邊界、時間軸與人工審查門檻。只有 QA 程式改變時，不應因此作廢 AAC 編碼快取。

這是本機可重建的 `.production/master-audio` 快取，不新增一份必須打包的重素材。`master-audio-cache.json` 記錄本次是否重用，delivery 另核對影片與參考 PCM 身分。

目前狀態：`implemented`、`tested`。小型 cold／warm 組裝、固定片段三輪效能與完整 M10 暖快取重組均通過。

## 章節渲染候選：實測後不採用

原計畫先處理最大的章節渲染窗口。兩種不改設計的候選均未通過，所以沒有修改正式 GPU／worker／擷取預設：

| 候選 | 原路徑批次秒數 | 候選批次秒數 | 結果 |
| --- | ---: | ---: | --- |
| 強制 screenshot | 160.831267 | 212.823 | 較慢，S23 影格亦不同，拒絕 |
| FFmpeg filter_threads=1 | 163.436 | 284.747 | 較慢，S23 影格亦不同，拒絕 |

每個批次包含 S23、S44、S50 各 30 秒、2 jobs × 4 workers、delivery 品質與全部解碼影格雜湊。兩個比較各在第一輪品質 gate 失敗後停止，沒有執行原計畫的三輪；共保留 12 部片段。批次時間包含解碼驗證，不能當作全片渲染時間。

不同原路徑執行的 S23 也出現解碼差異；本次 gate 比以前抽三張圖嚴格。這不能全部歸因於候選參數，也不能憑畫面成功輸出就宣稱全影格一致。既有 screenshot pixelmatch 與 geometry 門檻保持原值；未自動更新 golden。

失敗候選的 wrapper、測試及程式快照保存在本輪 evidence/filter/engine；沒有併入正式引擎。原生 HyperFrames、共享 node_modules、核准元件及設計不變。原資料顯示 chapter capture 與 streaming encode 重疊，本輪不把全部成本歸給 SVG 或 GPU。章節渲染的進一步加速仍為 `proposed`，待能同時通過品質與效能的獨立方案。

## 修正二：合併重複完整解碼

先前 master 使用 `ffprobe -count_frames` 完整讀取；checks 再以 FFmpeg 完整解碼檢查黑畫面。新流程由一次完整解碼同時提供實際影格數、黑畫面檢查與 decoder error gate。metadata probe 保留，但不再使用它替代實際解碼證據。

`media_scan.py` 要求終止 `progress=end`、實際影格數等於 timing ledger、無黑畫面，並使用 `-xerror -err_detect explode`。`-fps_mode passthrough` 避免輸出同步補幀混入計數。收據綁定影片、檢查程式、FFmpeg、原始 log 與 progress hashes；checks 使用當前收據，任何身分變更即失敗。失敗重跑先撤除先前通過收據，避免留下成功假象。

`master-ffprobe.json` 的 `nb_read_frames` 為實際解碼數，另以 `ceh_frame_count_evidence` 明確標註來源。新 artifact audit 和 delivery gate 檢查相同影片身分。graph 將新收據與其依賴納入指紋；不影響 speech、alignment 或 scene recipes。

保留獨立 AAC 全音軌 continuity／quiz boundary residual 驗證、所有 encoded screenshots 與人工審查責任。無損 PCM 不變。這項修正不宣稱已消除首次 AAC 編碼成本。

`master-stage-timing.json` 分開記錄 PCM 組裝、AAC 編碼＋mux／faststart、完整解碼、metadata probe、參考 PCM 保存；`master-assembly.progress` 保存原生進度。AAC 與 faststart 尚在同一 FFmpeg 呼叫中，不宣稱已有兩者獨立耗時。

目前狀態：`implemented`、`tested`。真實 decoder 正向／負向測試、三輪效能比較及整部 134872-frame master 掃描均通過。

## 回滾與邊界

既有 `CEH_M10_efficiency_v1_2` 的 master、PCM、ZIP、QA 收據保持凍結。新驗證只讀既有影片。保留此輪失敗候選及來源碼，不以成功重跑覆蓋失敗證據。

AAC 快取回滾為還原 assembly 的音訊輸入至原始 PCM 並使用原 AAC 編碼參數；既有快取可保留而不使用。合併掃描回滾須一起還原 master、checks、delivery 與 graph 的相依變更，恢復兩次完整解碼；不要只移除 gate。既有封存 ZIP 含舊引擎，可獨立還原歷史發行，不需覆寫目前工作樹中其他變更。

完整新影片的端到端時間仍須後續同範圍製片實測。片段收益不能直接乘上全片，這一輪不宣稱達成一小時或減半。

## 實作與測試定位

| 行為 | 維護中的程式位置 |
| --- | --- |
| AAC cache key／驗證／保留 | [master_audio_cache.py](../../tools/ceh_video/ceh_video/master_audio_cache.py#L13)，第 13、25、40 行 |
| 終止進度／綁定收據／完整解碼 | [media_scan.py](../../tools/ceh_video/ceh_video/media_scan.py#L36)，第 36、44、62 行 |
| 真正採用音軌快取與單次掃描 | [assemble_master.py](../../tools/ceh_video/ceh_video/runtime/assemble_master.py#L47)，第 47–68 行 |
| QA 驗證收據、免去重複解碼 | [audit_rendered.py](../../tools/ceh_video/ceh_video/runtime/audit_rendered.py#L12)，第 12–14 行 |
| 宣告新 implementation／output fingerprints | [graph.py](../../tools/ceh_video/ceh_video/graph.py#L82)，第 82–86 行與 delivery helper fingerprints |
| 交付端重新核對影片、PCM 與計數來源 | [delivery.py](../../tools/ceh_video/ceh_video/delivery.py#L122)，第 122 行起 |
| 真實 decoder 正向／負向測試 | [test_media_scan.py](../../tools/ceh_video/tests/test_media_scan.py) |
| PCM／模型／編碼身分與壞快取測試 | [test_master_audio_cache.py](../../tools/ceh_video/tests/test_master_audio_cache.py) |
| 真正 cold／warm 組裝、章節與逐樣本解碼相等 | [test_master_scan_integration.py](../../tools/ceh_video/tests/test_master_scan_integration.py) |

執行測試：

```bash
PYTHONPATH=tools/ceh_video \
  /home/jnlngx10/Videos/CEH_M10_efficiency_v1_2/project/.venv/bin/python \
  -m unittest discover -s tools/ceh_video/tests
```

完整測試在 `evidence/tests-final-v2.log`：111 tests passed。測試含真實 FFmpeg 與小型 PCM fixture，沒有執行 Kokoro，也不冒充完整交付驗收。

## 當次效能證據與失敗紀錄

所有秒數為 wall time；三輪使用相同素材、相同本機 FFmpeg，交錯測試順序。同機仍有既有背景程式，結果為描述性比較，不是隔離主機的統計推論。

| 60 秒固定素材 | 原流程中位數 | 新流程中位數 | 階段降低 |
| --- | ---: | ---: | ---: |
| AAC encode／mux 對比 cache lookup／stream-copy mux | 11.362825 s | 0.546070 s | 95.19% |
| 兩次完整解碼對比一次合併掃描＋收據驗證 | 10.159424 s | 7.331926 s | 27.83% |

AAC 表格不含首次填入快取及後續完整 QA；它衡量相同旁白的再次組裝，不代表首次新片製作也可省略編碼。三輪六份輸出全部浮點 PCM 解碼 SHA-256 相同。掃描表格包含新增雜湊／收據檢查，不把 metadata header 當作實際影格數。不得加總兩個百分比或直接套用到 83 分鐘章節渲染窗口。

原始比較：`evidence/aac-v2/comparison.json`、`evidence/decode/comparison.json`。執行 driver：`audio_cache_probe_v2.py`、`scan_probe.py`，均留在 evidence；這些為當次固定輸出路徑的執行紀錄，重跑必須使用新的空 run-root，不覆寫已封存證據。

初版 AAC cache 意外繼承章節 metadata，雖解碼雜湊相同，仍觸發 `Referenced QT chapter track not found`。已加入 `-map_chapters -1`，測試要求純音軌、零章節。初版完整掃描由操作者明確送 SIGTERM 中止，failed stage 29.540995 秒；原因、程式快照與先前比較保存在 `full-remux/qa/attempt.json`。這不是原因不明的歷史 SIGTERM。修正版使用 `aac-v2`、`full-remux-v2`，解碼比較因未受修改影響而保留，不重跑。

S23 兩次原路徑輸出有 154 個 encoded-frame hash 差異；第一個差異為 frame 96。以既有 pixelmatch threshold .05、includeAA=false 比對該影格，結果為 0 changed pixels。`evidence/s23-variance/` 保存兩張 PNG、diff 與報告；其餘差異尚未逐張分類。這項結果只解釋單一抽查，沒有放寬全影格 gate 或改寫 golden。


## 整片實測與最終狀態

[機器可讀 closeout](evidence/M10-high-impact-fixes-2026-10-20.json) 記錄完整原始比較、程式／測試／log SHA-256 及來源路徑。實驗模式 `other`，`execution_status=LIVE_FULL_COMPLETED`、`runtime_validity=valid_target_runtime`、`gate_outcome=pass`；此狀態僅適用於**既有章節的完整重組與影音驗證**。章節渲染候選為真實執行的負結果，未採用。

驗證工作區：`/home/jnlngx10/Videos/CEH_M10_perf_fix_20261020/full-remux-v2/`。它明確從已驗證的原 master 匯入連續 AAC，來源 master／reference／continuity receipt 雜湊保存在 `qa/seed-provenance.json`。這是暖快取案例；產品不會自動信任任意舊影片，也未宣稱每個新工作區已具備 AAC 快取。

| 整片組裝階段 | 實測秒數 |
| --- | ---: |
| PCM 組裝 | 1.013371 |
| AAC cache lookup | 1.398351 |
| AAC stream-copy／mux／faststart | 14.901866 |
| 全片解碼、計數、黑畫面及 decoder integrity | 487.693000 |
| 確認保留 AAC 快取 | 1.541744 |
| Metadata probe | 0.332739 |
| 保留 PCM reference | 0.413966 |
| Driver 實測完整 assembly wall | 507.543961 |

507.54 秒不含先前章節渲染、後續 AAC continuity、encoded screenshot QA、人工審閱或交付打包；不可將它稱為整部製片總時間。首次沒有 AAC 快取仍須編碼。以前的 1178.167 秒 master 是歷史參考，不是這次同時量測的 cold 全片對照。

實際驗證：

- 134872 個 video frames、4495.733333 秒、11 個章節；完整 decoder 掃描通過，零黑畫面，零補幀／丟幀。
- 全部 215795200 個 stereo reference frames 經 AAC continuity 比對；11 章的 SNR／correlation／block metrics 與原片完全相同。
- 八個 quiz PCM holds 各 48000 frames，總計 384000，逐樣本全部為零。
- AAC 解碼為 215795712 frames，尾端 codec padding 512；quiz 最大殘留 0.000028022011974826455，與原片一致。沒有宣稱 AAC 逐樣本零值。
- 原片與重組片的 video/audio stream payload SHA-256 一致；codec、像素格式、FPS、time base、start PTS、duration、色彩 metadata、sample rate、channels、extradata hash 及 11 個 chapter records 一致。
- 原交付 MP4、ZIP、74 項鎖定資產雜湊均通過；完整 reference PCM SHA-256 相同。未重新推論語音、調整字幕時間、重新生成設計或更新 goldens。
- 111 個 Python 測試通過；調整直接執行入口後，6 個 decoder 測試另行通過。`git diff --check` 通過。

採用：AAC 重用、單次完整解碼、分段計時、收據／cache／delivery 身分檢查。未採用：兩個渲染候選。待後續獨立評估：章節擷取本身加速、S23 其餘 encoded-frame 差異分類、新完整製片 wall time。人工完整觀看／聆聽及公開發布均不屬於本次已完成驗證。未提交或推送 Git。

## 第二輪：縮小章節與成片 QA 的重跑範圍（engine 0.5.2）

使用者後續要求：「請再修正影響最大的兩大因素，謝謝」。本輪承接上述紀錄，優先處理仍昂貴的章節渲染與成片驗證。這兩項改動改善相同內容的修改／重試路徑；首次新片的 83 分鐘章節窗口仍未取得加速證據。不能把可避免的重跑時間視為每次必然節省的時間。

### 原因與選擇

`graph.py` 的 render 依賴 prepare 的 key 與 QA 輸出；prepare 又含 capture、review、runner 實作身分。因此前置檢查變動可使 render 階段失效，即使實際章節 HTML、音訊、字體與其他資產相同。原有 reference-import 重用只處理特定已匯入的歷史來源，沒有一般「當前已成功編碼章節」的重用收據。這是從程式依賴確認的重跑風險，沒有追溯證據證明它占歷史四小時中的多少分鐘。

同時，舊 checks 依序執行 `audit_rendered.py`、`audit_audio_continuity.py`、`capture_late_diagrams.py`；任何一項程式改動都使三項一起失效。它還依賴 audio-review，使旁白審查收據更新可能連帶再次執行完整成片驗證。原始 full-decode、PCM／AAC 界線、視覺審查仍是必要門檻；本輪縮小失效範圍，不降低門檻。

先以同一個既有 60 秒 M10 片段測試解碼執行緒。三輪交錯、兩種命令、三種設定，共 18 次真實執行：

| 檢查／中位數秒 | 自動（原設定） | 1 thread | 4 threads |
| --- | ---: | ---: | ---: |
| 章節 ffprobe 完整計數 | 3.357047 | 3.969782 | 6.959704 |
| 成片完整解碼＋blackdetect | 7.130952 | 20.720317 | 8.772806 |

兩種限制都較慢，維持原設定。兩項命令仍讀取全部 1800 個影格；未改影片、濾鏡或 QA 容差。這項實驗為 `LIVE_MINIMUM_COMPLETED`、runtime `target`、performance gate `fail`、decision `rejected`。同機背景負載未隔離，數字只代表本輪片段對照。AAC 重複解碼合併與 GPU capture 加速仍為 `proposed`，本輪沒有宣稱完成。

### 修正一：當前章節編碼成果的獨立重用

`render_reuse.py` 在新章節實際成功渲染與 codec 驗證後，寫入 `.production/encoded-chapters/Cxx.json`。收據只保存身分與雜湊，不複製 MP4、素材或模型。

重用身分包含章節實際輸入指紋、完整 runtime／output 設定、影響 renderer 的環境設定、lockfile、HyperFrames launcher／dist、Chromium 與 FFmpeg binary、渲染實作。比對 MP4、原生 stdout／stderr、codec 驗證收據的全部雜湊。runner 在查快取之前執行當前 visual／review gates；cache hit 還必須通過當前 checked fingerprint、lint／runtime／layout／contrast 零錯誤與零警告檢查。歷史一般 render.json 不會自動升格成新快取證據。

來源、runtime、影片或證據改變即失效。`--force` 仍執行渲染；嘗試開始先撤除舊快取收據，失敗不留通過狀態。原本 reference-import 相容路徑保留，不擴大它的範圍。新快取首次沒有收據時仍須渲染；不假設能直接省掉下一次冷啟動製片。

狀態：`implemented`；`tested` 為真實 FFmpeg 小型影片加上實際 runner action 的回歸測試。測試中的 worker 替代了 HyperFrames，因此只證明 runner 重用／失效／審查控制，不證明原生章節效能。完整 M10 新版本重製與暖快取節省分鐘數為 `proposed`。

### 修正二：成片 QA 分項驗證與計時

v1.2 English graph 新增：

- `checks:frames`：實際編碼圖片、黑畫面完整解碼收據、master 與 chapter 的 quiz silence。
- `checks:audio`：完整 AAC 對無損 PCM 的逐區塊 continuity 與有損邊界殘留。
- `checks:late`：每個非 quiz 場景的後段圖解截圖。
- `checks`：匯集上述結果及 audio-review，保留 delivery 前全部驗收責任。

每項有獨立 implementation key、輸出雜湊、執行收據與既有 RunRecord 階段計時。修正 late 圖解擷取程式時，只重跑 late 項；audio-review 更新時仍重做聚合 gate，但不單獨使三項成片檢查失效。master 改變仍使三項失效，沒有假設新 master 的媒體身分相同。新版 renderer cache 也沒有消除後續 master dependency 的失效，這一點留待後續量測。

所有中點、章節、quiz／邊界、late PNG 與 contact-sheet JPG 都加入相應輸出清單；刪除或改動任一圖片會使該項驗證失效。沒有新增 golden、變更 pixel tolerance、縮減抽樣點，或自動接受人工審查。v1.0／v1.1 及其他語言路徑維持原 checks 執行方式。

狀態：`implemented`、`tested`。實際 graph／receipt 測試確認修改 late validator 後 audio／frames 可重用、late 必須執行；刪除 midpoint PNG 後 frames 必須執行。打包因包含程式碼仍需更新，這是正確的影響範圍，並非影音 QA 重新執行。

### 證據、限制與回滾

原始命令／stdout／stderr／progress／逐次計時：`/home/jnlngx10/Videos/CEH_M10_decode_tuning_20261020/`。固定素材沿用前輪 `evidence/decode/fixed-60s.mp4`，不變動封存影片。新回歸檔為 `tools/ceh_video/tests/test_scoped_reuse.py`。使用前述 unittest discover 命令；新增五項測試涵蓋真實影片 bytes、輸入／runtime／log 失效、當前審查、強制／失敗重跑及分項 QA 收據。精確測試結果與 source hashes 記在 `evidence/M10-scoped-reuse-2026-10-20.json`。

初次測試將 package 也失效視為錯誤；檢視後確認打包必須納入改動後的引擎，修正測試期望，未取消打包指紋。首次量測啟動使用不存在的 `python` 名稱而失敗，改用現有 `python3` 後完成 18 次量測；這個啟動失敗不列入效能數據。

回滾時還原 runner 的章節重用分支，以及 graph／runner 的分項 checks 路由，恢復原本三項順序執行；配套還原新增測試及版本資訊。新 `.production/encoded-chapters` 收據可以留存而不使用，沒有須還原的重素材。已封存發行、字體、Tally、旁白、0.3 秒句間／0.8 秒章間與八段精確靜音均未改動；視覺例外零新增，既有 `LEGACY-M10-SUBTITLE-001` 範圍不變。

下一個正式檢查：在新的製片 workspace 完成一次原生章節編碼，接著只修改 QA 實作並重跑，確認 native render 呼叫數為零、當前 gates 通過且 encoded hash 相同；再以相同 master 檢查只修改一項 validator 的 RunRecord。這是尚未執行的全製片環境驗證，不以本輪 fixture 代替。第一輪製片本身的加速與一小時目標仍未完成。


## Source, ownership and publication route — October 20

[Preserved request and publication authorization](../../source/2026-10-20-ceh-m10-performance-optimization/source.md) → [production index](README.md#ceh-m10-efficiency-2026-10-20) → [engine guide](../../tools/ceh_video/README.md#scoped-retries-engine-052). The [Planning day](../../../planning-everything-track/weeks/2026-W43/days/2026-10-20.md#ceh-m10-efficiency-2026-10-20), [project](../../../planning-everything-track/data/projects/2026-07-ceh-cehp-certification-training.md#ceh-m10-efficiency-2026-10-20) and [week](../../../planning-everything-track/weeks/2026-W43/weekly-plan.md#ceh-m10-efficiency-2026-10-20) retain outcome, capacity and next-gate links. Local raw evidence remains at the paths above; publishing code and compact receipts does not publish the large film or establish human acceptance. Historical source hashes in receipts identify their captured revision; later connection-only edits do not replace those snapshots.
