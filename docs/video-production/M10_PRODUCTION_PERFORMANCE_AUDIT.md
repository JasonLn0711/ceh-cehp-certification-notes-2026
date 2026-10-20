# M10 製片效能查核與修正追蹤

2026-10-20。完整來源與選項：[原始紀錄](../../source/2026-10-20-ceh-m10-performance-optimization/source.md)。[機器可讀發現](../../source/2026-10-20-ceh-m10-performance-optimization/findings.json)；[證據路徑及SHA-256](../../source/2026-10-20-ceh-m10-performance-optimization/evidence-index.json)。

Canonical owner：CEH repository；稀缺資源：操作者與原生GPU製片時間。大型媒體與原始QA留在Videos，不複製至Planning。

## PERF-001 — 總工作時間缺少共同起訖

四小時與一小時尚無同範圍統一計時，不能逐分鐘分攤。

## PERF-002 — 片長增加不足以解釋回退

128512→132727 frames；71:23.733→73:44.233；增加3.279849%。

## PERF-003 — 渲染工時回退

原始4365.641497s、最佳化1853.826443s、新版10630.082889s；章節加總含平行重疊，非wall time。

## PERF-004 — 實際主流程

7631.377713s；章節窗口6338.707376s包含於主流程，不相加。

## PERF-005 — 主要執行階段

capture_streaming合計9298.811s，占章節receipt工時87.476%；含串流編碼，不能獨斷SVG或GPU成本。

## PERF-006 — worker選型範圍不足

4改2；先前只比較1/2、S44十秒、同機QA負載，不證明優於4。

## PERF-007 — 長章節尾段

C11 14:01:44開始；C09 14:04:59最後其他章完成；C11 14:37:15完成；單章尾段1936.212783s。

## PERF-008 — 封裝連結展開

61006 files、82853930346 bytes暫存；中止並狹義排除boundary hosts，來源保留。

## PERF-009 — 封裝導致影音重驗

delivery.py整檔進audio-review指紋，包裝修正導致853.967594s重驗；master與165圖片未變。

## PERF-010 — 較晚發現共用幾何缺陷

shared connector、port normal與文字間距缺陷使多輪完整截圖、準備及審查失效。

## PERF-011 — 重複全域驗證

規劃與執行反覆建立graph、檢查render guard；獨立成本尚未量測。

## PERF-012 — 語音並非本輪主要成本

781 clips reused，完整remaster零Kokoro推論，processed1.4身分保留。

## PERF-013 — 卡片限制圖解

scene_art先為所有node畫card-frame，圖示被迫嵌入卡片。既有29個SVG道具可沿用。

## PERF-014 — 可重建重素材副本

章節資源、review hosts與合成音軌有重複；封裝需要明確來源與衍生產物清單。

## PERF-015 — 歷史計時覆寫

run-checks.json已被包裝修正重驗覆寫；full-production-run.log保有原7631秒結果。

## PERF-016 — 政策字串分支

多處ceh-en-v1.1判斷，新增政策可能漏驗，需登錄與fail-closed。

## 因果與驗收邊界

已確認實際渲染回退、排程尾段與包裝錯誤；尚未以profiler分解瀏覽器JS／繪製／GPU擷取／encoder成本。禁止把worker數量直接當線性加速比。328 native captures與165 encoded samples為既有能力；558 golden states、171邊界、905資產狀態及新幾何驗證須按本輪實際覆蓋區分。

本輪使用配對工作負載與一次正式完整發行，不另跑整片baseline。原始4h/1h描述保留，量測報告不把未知區間補成精確值。每項完成狀態以新run receipt更新；原始發現保留。

## 修正與原始碼定位（2026-10-20 實作檢查點）

下列行號對應本次工作樹，正式交付再以來源雜湊固定。`implemented` 表示程式已寫入；不代表完整影片已通過驗收。

| 發現 | 修正定位 | 狀態與驗證邊界 |
| --- | --- | --- |
| PERF-001、004、015 | `tools/ceh_video/ceh_video/run_record.py:11`、`:25`；`runner.py:282` | implemented；每次獨立 run ID、事件與摘要，失敗不覆寫，區分 stage work / wall / queue / tail；單元測試驗證保存與順序 |
| PERF-002、012、016 | `audio_policy.py:8`、`speech.py:27`、`:68`、`:131`、`timing_ledger.py:5` | implemented / tested；真實 58 場景 PCM、781 句重用、零推論、零重處理；新總長 215795200 stereo frames / 134872 video frames |
| PERF-003、005、006 | `benchmark.py`、`visual/remaster-runtime.js` | implemented；固定三種 30 秒工作量、三輪交錯設定；36 次片段渲染完成，選定 2×4，runtime 候選未採用；50% 改善尚未建立 |
| PERF-007 | `scheduling.py:5`；`runner.py:202` | implemented / unit tested；C11 依估計工作量優先，完整製片 tail 改善待實際執行 |
| PERF-008、014 | `packaging.py:39`、`:97`、`:109` | implemented；清單直接串流 ZIP、狹義排除 hosts、還原音軌雜湊；完整 ZIP 驗證待執行 |
| PERF-009 | `audio_review.py`；`graph.py:79`、`:90` | implemented / unit tested；包裝與音訊驗證的實作指紋分離，實際變更影響仍按圖傳播 |
| PERF-010 | `qa.py:10`、`:40`；`visual/remaster-qa.mjs:25`、`:181` | implemented；預檢→代表→受影響→全片；局部 QA 原先誤用全片覆蓋條件，已修正，原始日誌與證據缺口保留；134 張代表重驗及 S49 局部 golden 回歸通過 |
| PERF-011 | `runner.py:202` | implemented；單次執行重用 graph，結束時重查來源是否改變；減少的獨立成本未量測 |
| PERF-013 | `remaster.py:13`、`:89`、`:133`；project `design/asset-provenance-v1.2.json` | implemented；11 場景採獨立語義圖示；58 場景、558 張正式 golden 回歸通過，像素與 seek 差異均為 0 |

上表縮寫路徑皆相對 `tools/ceh_video/ceh_video/`。新工作區：`/home/jnlngx10/Videos/CEH_M10_efficiency_v1_2`。原始失敗 `qa/runs/20261020T081923Z-e0b69ac2/`：134 張代表截圖，幾何與 seek 零錯誤，兩項範圍覆蓋錯誤；不能將該次執行寫成 passed。新版正式視覺回歸已獨立執行並通過；原失敗狀態保留。

目前例外總表：本版新增例外 **0**。`LEGACY-M10-SUBTITLE-001` 僅涵蓋歷史 `CEH_M10_optimization_v1` 的 S01–S58；本版全部 58 場景均無此例外。獨立圖示變體是受約束元件設定，不是安全區豁免。

## 固定工作量比較結果（已執行）

同一批三種 30 秒片段：S23 拓樸、S44 資源狀態、S50 測驗；輸出 1920×1080 / 30 FPS，原生 HyperFrames 0.8.174，固定 Chromium headless shell 1234、GB10 hardware probe。每組三輪交錯執行。下表為整批 wall time，包含輸出完整解碼與三張抽樣影格驗證；不能解讀為單純 GPU 或 JavaScript 成本。

| 並行章節 × 每章 worker | 第1輪秒 | 第2輪秒 | 第3輪秒 | 中位數秒 |
| --- | ---: | ---: | ---: | ---: |
| 1 × 4 | 206.576 | 203.520 | 204.728 | 204.728 |
| 2 × 2 | 163.357 | 168.923 | 171.114 | 168.923 |
| 2 × 4 | 156.149 | 144.938 | 141.369 | 144.938 |

27 次基準輸出均通過規格、完整解碼與抽樣解碼影格一致性；27 份原始 log 的實際 GPU probe 均為指定 GB10 hardware。選擇 2×4：比 2×2 的批次中位數減少約 14.2%，差距超過預先採用的 5% 同等表現區間。

另以同一 2×4 設定執行三輪 runtime 配對：候選版中位數 146.942 秒，原版 144.938 秒，候選慢約 1.38%；解碼影格一致。DOM 參照快取與重複時間更新略過的候選**未採用**，來源保留於 `qa/runtime-optimized/`。機器比較報告的 `adopt_runtime=true` 僅代表通過 5% 非退步篩選；最終明確決策以 `qa/benchmark-production-decision.json` 為準，採用原 runtime。

限制：這是片段配對，不是全片 A/B；未建立 50% 加速或一小時全片承諾。基準早期有短暫靜態 lint、單元測試及總覽圖產生，沒有並行瀏覽器 QA 或模型推論；每次工作記錄主機 load。測試用 host 唯一 lint 警告為 `studio_missing_editable_id`，不影響渲染畫面，但未以此放寬正式影片的零警告要求。第一批 driver 未在開始時快照自身原始碼，固定場景來源、命令、原生 log 與 GPU probe 已保留並另行查核；後續 driver 增加來源快照。

證據：`qa/runs/20261020T082248Z-a5881e6c/benchmark.json`、`qa/runs/20261020T084850Z-81cdc3ec/benchmark.json`、`qa/benchmark-baseline-integrity.json`、`qa/benchmark-comparison.json`、`qa/benchmark-production-decision.json`。上述效能研究列入首次改版成本，不併入例行製片時間。

歷史 PERF-007 時間為 Asia/Taipei（UTC+08:00）：C11 開始 `2026-10-20T14:01:44.434670+08:00`；依 process started + render receipt elapsed，C09 完成 `14:04:59.277652`，C11 完成 `14:37:15.490435`。相減為 1936.212783 秒，並非額外加在渲染總窗口之外的時間。

新增查核：首輪局部 QA 的相容性輸出目錄被重跑覆寫，未保留原始完整 manifest；日誌與當時檢視總覽保留。詳見 `qa/visual-evidence-custody-correction.json`。新的局部輸出含 run ID，CLI 每次備份 manifest；局部回歸讀取正式 golden 的對應場景子集，無自動更新。


## 本次實作新增的中斷證據

原生準備主程序兩度收到 SIGTERM，來源尚待追查。首輪退出 143，末事件 elapsed 158.108383 秒；精確終止時間缺失，不能把觀察下限當完整 wall time。續跑 `20261020T092951Z-a9aeedcb` 在 root 檢查中收到 SIGTERM，已保存完整 interrupted 摘要（832.222151 秒，含已完成章節工作及 214.480868 秒未完成 root 檢查）。11 章既有成果與審查保留。CLI 新增 SIGTERM→既有中斷清理路徑，真實訊號 fixture 通過；訊號來源追查與新的完整渲染仍待執行。此項是本輪環境觀察，不能倒推為歷史四小時耗時原因。


新增實測：含音訊的整片 66 點 native check 因內建 deadline 失敗；含音訊單點通過但需 329.424 秒。保留完整 58 場景視覺與原始時間、只移除音訊元素的診斷 host，66 點及 59 個對比物件全部通過，耗時 98.327 秒。這支持將視覺 QA 與重複長音軌載入分離；不同取樣範圍、單次量測不構成正式加速百分比。引擎 `root_check.py` 實作受雜湊約束的分離驗證，`delivery.py` 強制檢查來源與覆蓋，PCM／AAC／完整 MP4 驗證維持必驗。此方案沿用既有 boundary QA 的 visual-only host 方法。

## 本輪完整製片結果與後續優化順序

`tested`：新片完整主流程6995.166090秒（1小時56分35秒），比歷史7631.377713秒少8.34%；章節渲染窗口4982.271554秒，比歷史6338.707376秒少21.40%；最後單章等待95.027198秒，比1936.212783秒少95.09%。C11第三個完成，最後是C08。這是不同發行與準備範圍的觀察比較，不能解讀為受控A/B。**整體50%改善及一小時目標未達成**。

本輪仍有重要成本：master組裝與實際影格計數1178.167320秒，全片解碼／音軌／抽樣驗證720.574466秒。83分2秒渲染窗口本身已超過一小時，單靠打包與QA微調無法達成一小時整片目標。主流程沿用186個已驗證上游節點，另行完成11章渲染；前置QA、首次工程改版、失敗重跑、人工或代理審查、交付封裝不冒充這個主流程範圍。

詳見 `qa/production-phase-accounting-v1.2.json`：每次run ID、原始kind、報表分類、parent、status、wall及未知區段均保留。兩次首輪QA誤標routine，報表視圖明確歸入首次改版，原紀錄不重寫。首次中斷只有158.108383秒觀察下限；精確wall未知。編碼與審查的未獨立計時作業不補造數字。來源行號與雜湊見 `qa/production-source-index-v1.2.json`。

下一輪優化是 `proposed`，本次不啟動第二次全片或擅改核准品質：

1. **優先分解capture_streaming成本。** 在既有三種固定30秒片段記錄JS/layout、paint/composite、GPU readback與encoder時間，保留環境與相同解碼影格。只有證據指出瓶頸後才改對應路徑；同品質三輪配對通過後才更換預設。停止條件：畫質、seek或幾何失敗，或結果未改善。
2. **分開量測連續AAC編碼、faststart及影格計數。** 本輪master階段合計1178秒，尚無可歸因的細分數值。先加入FFmpeg原生進度與獨立時鐘；任何快取需綁定完整PCM、codec/runtime與設定，不可直接串接可能有間隙的章節AAC。
3. **評估一次完整解碼同時取證。** 目前 `runtime/assemble_master.py` 的FFprobe count_frames與 `runtime/audit_rendered.py` 的黑畫面解碼各有目的。先以同一固定MP4做真實計數／黑畫面／錯誤偵測等價性測試；只有完整覆蓋一致才可合併，不能刪掉檢查取得較快結果。
4. **持續使用新排程與一次封裝。** 保留每次tail、queue、影音receipt與archive獨立結果。對包裝修正只執行影響分析和封裝驗證；一般迭代不產生ZIP。
5. **後續完整製片使用相同計時邊界。** 分列首次改版、例行、重跑、交付；至少取得可比較的例行紀錄再判定持續效能，避免把本輪單次值當服務承諾。

新增觀察：本輪完整渲染未收到SIGTERM，來源凍結重查通過。先前SIGTERM來源仍未確認，不能將其套用為歷史四小時原因。新字幕例外0；歷史 `LEGACY-M10-SUBTITLE-001` 僅限optimization-v1的S01–S58。本版變體場景：S01、S07、S17、S23、S27、S33、S40、S44、S47、S48、S49；全部58場景更新時間。完整人類觀看／聆聽待執行。

## 封裝與交付實測結案

`implemented / tested`：正式ZIP一次建立成功，6,722個成員、6,721份payload雜湊、1,818,201,690 bytes。直接串流來源2,733,577,276 bytes，打包前重素材暫存0 bytes；必要解壓驗證2,737,446,685 bytes另行記帳。CRC、解壓雜湊、165張編碼圖片、golden審查憑證，以及781句快取／12份PCM／12份HTML重建全部通過；零新推論、零tempo處理。這項修正沒有重跑影音驗證。

交付條件指令80.455046秒；封裝指令240.591311秒，其中真正package階段185.818452秒。兩個獨立指令合計321.046357秒，不包含中間文件與代理審查時間。新ZIP約1.82GB；歷史82.85GB數字是失敗的素材暫存展開量，兩者不能當同一種壓縮率比較。

最終證據：`qa/final-delivery-closeout-v1.2.json`、`engine-packaging.json`、`engine-extracted-reconstruction.json`。所有資料留在新工作區；封裝內文件保留封裝前檢查點，外部結案憑證完成最後驗收，不為了把自身雜湊寫入ZIP而反覆打包。完整人類觀看／聆聽、50%加速與一小時目標仍未完成，後續計畫維持上節所列範圍。

## PERF-017 — 畫面修正仍重編碼整段連續 AAC

新增 [engine 0.5.1 修正與證據](M10_HIGH_IMPACT_FIXES.md)：`master_audio_cache.py` 以完整 PCM、樣本數、voice/model/policy、編碼設定與 FFmpeg 身分決定重用。相同旁白的新 master 只複製 AAC；完整音訊 QA 保留。固定 60 秒三輪比較中位數 11.362825→0.546070 秒，屬於音軌 encode/mux 階段，不是全片製作比例。

## PERF-018 — master 計數與 checks 重複完整解碼

`media_scan.py` 將實際影格計數、黑畫面與 decoder error gate 合併一次掃描；後續檢查核對影片／程式／FFmpeg／log／progress 雜湊。固定 60 秒三輪中位數 10.159424→7.331926 秒。主片的 metadata probe 與 AAC continuity 保留。

## PERF-019 — 章節加速候選與更嚴格影格比較

強制 screenshot 與 filter_threads=1 都比目前路徑慢，未採用。共 12 部真實 30 秒 native outputs，兩個比較各在第一輪 gate 失敗停止。不同原路徑執行的 S23 也有 encoded-frame 雜湊差異；第一個差異 frame 96 的既有 pixelmatch 檢查為零 changed pixels，其餘差異未完整分類。保留原 native pipeline、worker 配置及 golden 門檻；詳見修正報告的拒絕候選與原始 artifacts。
