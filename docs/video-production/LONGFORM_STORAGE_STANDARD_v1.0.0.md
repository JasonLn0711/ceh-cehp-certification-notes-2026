# CEH 與課業複習長片：製作、封裝與儲存規範

| 欄位 | 值 |
| --- | --- |
| 文件 ID | `longform-storage` |
| 規範版本 | `1.0.0`；機器識別 `longform-storage-v1.0.0` |
| 建立／生效／最後更新日期 | 2026-10-22（Asia/Taipei） |
| 對應引擎 | `ceh-video 0.5.5`，本機維護版 |
| 適用範圍 | CEH 英文長片、課業華語概念長片、MATLAB 實作長片；未來製作及具名改版 |
| 決策來源 | [使用者要求原文](../../source/2026-10-22-longform-storage-policy/source.md) |
| 驗證範圍 | 程式回歸測試、合成資料封裝、實際工作區只讀盤點；沒有重製或重封既有長片 |

本規範補充 [CEH v1.2](PRODUCTION_STANDARD_v1.2.md)與[中文課業交付契約](MANDARIN_WORKSHOP_DELIVERY.md)。它接管新版本的暫存、封裝與保存方式；教學、視覺、語音、時間政策及既有交付狀態沿用各片的具名版本。

## 1. 目的、責任與適用邊界

稀缺資源是本機 SSD 容量、重製時間與人工審閱時間。CEH repository 擁有共用引擎、規範、測試與容量盤點；課務資料夾擁有課業教材、逐字稿、執行截圖與交付證據；`~/Videos/<release>/` 擁有大型製作檔案。Planning 僅保留定位、狀態、容量影響與下一關。

操作者負責新建具名版本、執行 QA、封裝與記錄。Jason／授課團隊負責既有契約要求的內容確認與人工聽看。機器驗證、內容接受、影片公開及學員完成維持各自的證據。

本次不啟動 TTS、渲染或效能比較；不改變已交付影片或進行歷史目錄清理。歷史證據中的 `extracted_root` 仍指向當時實際目錄，保持原文。新收據以驗證方式、位元組數、雜湊與暫存保留狀態描述結果。

## 2. 問題與量測方式

2026-10-22 的[盤點](evidence/longform-storage-inventory-2026-10-22.json)顯示，容量來源包括多版本完整工作區、語音來源／處理後 PCM、章節 host 複本、來源封裝 staging、解壓驗證目錄與測試工作副本。例如 CEH M10 optimization 的重複工作目錄分類約 11.68 GiB；課業概念片 v3 的解壓驗證分類約 2.77 GiB。這些是待核對的占用量，不是已核准刪除量。

盤點按每個工作區內的唯一 regular-file inode 計數；符號連結不跟隨、hardlink 不在同一工作區重複計算。`logical_bytes` 為檔案長度，`allocated_bytes` 為配置區塊數 × 512。跨工作區 hardlink／reflink 共享空間、目錄本身與外部連結目標未做完整歸戶，因此不把工作區加總當成精確可回收容量。掃描中變動的工作區只是當時快照；刪除前必須重新核對。

## 3. 每部長片的製作順序

| 階段 | 必做工作與保存資料 | 進入下一階段的條件 |
| --- | --- | --- |
| 需求／版本 | 固定對象、學習成果、來源、片長範圍、locale、release ID、規範版本與引擎版本 | 來源與內容範圍明確；沿用各片現有內容確認契約 |
| 講稿／分鏡 | 單一 canonical 講稿；穩定 scene／shot ID；圖像來源、旁白錨點、測驗與答案時機 | 具名版本審閱完成，或明確維持 draft |
| 素材／語音 | 保存原始採用音訊、供應者時間戳、處理配方及雜湊；核對素材授權與字型 | 語音、素材與來源身分一致，無重複速度處理 |
| 代表場景 | 先檢查高密度文字、圖板、長標籤、章節銜接與測驗揭露 | 實際尺寸、讀字、安全區、seek 與字幕邊界通過 |
| 章節迭代 | 只重建輸入改變的場景與其下游；保留可驗證的音訊、章節與母片快取 | 所有必要來源、輸出與 QA 雜湊匹配 |
| 正式影片 | 完整編碼／解碼、字幕、音訊銜接、測驗靜音、成片畫面抽查與既有人工 gate | 對應版本的技術交付檢查通過；人工未完成時明確 pending |
| 封裝 | 明列 payload、直接寫暫存 ZIP、逐檔 CRC／SHA-256、驗證後 atomic rename | 正式 ZIP、外部收據與雜湊相符 |
| 保存／交接 | 指定工作版、交付版及封存位置；留下容量、驗證與下一關 | 還原能力與保存副本核對完成後，才處理具名可重建項目 |

迭代時使用 `run --intent iteration`；交付時才使用 `run --intent release`。此區分適用共用 graph 的英文與中文概念片；MATLAB 實作片仍使用其課務腳本，先完成 `delivery-media.json` 的六支影片與畫面驗證再封裝。

講稿／語音改變時，重新計算其字幕、動畫錨點、場景時間與下游檢查。純封裝修改只應影響封裝；引擎使用檔案級雜湊的共用模組變動，可能保守地使多個檢查失效，必須以 plan 為準。本次把中文封裝移出 `mandarin_delivery.py`，首次遷移會使引用該舊模組的 audio-review／checks／delivery receipt 失效；後續獨立封裝模組修改不需修改該模組。歷史 workspace 不直接升級重跑。

## 4. 畫質、教學與語音細節

- 保留每片已採用的解析度、FPS、字型、角色、配色、構圖與安全區；不以降解析度、縮字或刪除教學來取得容量改善。
- CEH 英文沿用 `ceh-en-v1.2` 的 af_heart、baseline 0.73、spoken PCM 一次 atempo=1.4、畫面 1×、八題各 48,000 zero PCM frames，及既有段落／章節時間規則。
- 中文第一部、概念第二部、實作第三部分別讀取自己的 profile／課務規範。第二部 v3 的 1.3×、0.45 秒靜音與教材圖板不能套用到其他片；第三部的 MATLAB 真實執行截圖與接受紀錄保持原來範圍。
- 編碼後完整解碼、音訊／字幕／題目揭露檢查及人工聽看保持各自 gate。CRC 與 SHA-256 只證明檔案完整性，不能證明內容正確或觀看品質。
- 原始講稿、教材來源、實作證據與最終採用聲音是保存資產。重新呼叫 TTS 未必產生相同聲音，不能把語音來源當成一般可丟棄快取。

## 5. 檔案保存矩陣

| 類別 | 製作中 | 結案／封存後 |
| --- | --- | --- |
| canonical 講稿、分鏡、資料、素材來源、授權、設定、鎖定版本 | 保存；小型文字由 owning repo 管理 | 保存於可還原來源包與 owning repo 的適當範圍 |
| 採用語音、baseline／processed PCM、時間戳、配方、對齊 | 保存，按內容與配方驗證重用 | 保存還原必需檔案；本版不自動刪除 speech-cache |
| 正式 MP4、SRT／VTT、PPTX／PDF、SHA、交付收據 | 保留目前候選與最近已接受版 | 正式發行版保持可定位；公開網址不能替代本機／備份原件 |
| QA、人工審閱、來源雜湊、失敗／成功 run 紀錄 | 保存 | 保留可解釋決策與驗證結果的證據；歷史實驗資料另依其契約 |
| chapter host、合併音訊、章節片、AAC 快取 | 保留以支援增量迭代 | 先證明可還原，並核對章節片是否也是交付品；再列具名清理清單 |
| `node_modules`、`.venv`、可重新取得的 runtime | 依 pin 使用；可共用相容版本 | 排除於教材包；保存 lockfile、安裝方式與 runtime 身分 |
| 本次 `verify-package-*` 解壓目錄／partial ZIP | 僅供該次封裝使用 | 正常成功、例外與可處理中斷後清除本次所有暫存 |
| 舊 `archive-verification`、`engine_project_source`、測試 workspace | 列入只讀盤點 | 核對 run、使用程序、封裝與證據後再決定；名稱本身不構成刪除理由 |

工作版保留完整增量快取。已接受舊版可以移到外接磁碟／NAS 的封存區；先完成目的端雜湊核對與還原檢查，記下新位置，再處理本機重複副本。尚未指定備份目的地與歷史版本保留期限，因此本版不自動搬移、不依檔齡刪除。

## 6. 封裝實作契約

### CEH 英文 v1.2 路線

沿用直接 manifest-to-ZIP、排除可重建 host／combined audio、實際解壓 CRC／SHA、零次新推論的音訊／host 重建檢查。0.5.5 增加本次 partial ZIP 的例外／中斷清理。既有 TemporaryDirectory 解壓方式保留。失敗不替換已驗證交付包；closed release 改變時使用新版本 workspace。

### 課業中文概念路線

`mandarin_package.py` 直接引用當前引擎檔案，不再先拷貝到 `project/vendor`。保留來源、語音、成片、教材、必要 QA；排除 runtime、歷史解壓副本及本次驗證目錄。未知來源符號連結明確失敗，以免教材遺漏被當成成功。

容量預檢要求可用空間至少 `2 × payload logical bytes + 128 MiB`，涵蓋暫存 ZIP、一次解壓與基本餘裕；這是保守操作門檻，不是峰值量測。其他程序同時占用空間仍可能造成失敗。寫入時核對來源 SHA，解壓時 CRC 自動檢查，再核對每個 payload 及 manifest。移除額外的 `testzip()` 全量重讀。全部通過且解壓暫存清除後，才將 partial ZIP 改名成正式檔。

已壓縮的 MP4／MP3／PNG／JPEG／PPTX／PDF／ZIP 採 ZIP_STORED；其他資料採 DEFLATE level 1。這只改外層封裝方式，payload 位元組不變；沒有宣稱最佳壓縮率或實測縮時。

### 課業 MATLAB 實作路線

`practice_package.py` 核對六支影片與 `delivery-media.json` 的 SHA。直接封裝後，以串流讀取每個 ZIP member 到 EOF，同時驗證 CRC 與 manifest SHA；不另建完整解壓樹。容量門檻為 `payload logical bytes + 128 MiB`。收據標示 `stream_all_members_crc_sha256`，不把這項檢查稱為完整重建測試。新包帶入本次封裝模組，支援離線讀取來源後再次驗證。

三條路線都保留已交付 ZIP。新版本應建立新的 release workspace／內容修訂，不能以覆寫舊成品完成升級。第三部的舊 `scripts/package_work.py` 是草稿工具，正式交付使用 `scripts/package_delivery.py`。

### 失敗、強制中止與進度

可處理的例外、KeyboardInterrupt 和既有 `run` 的 SIGTERM 路由會離開 context 並清除本次暫存；SIGKILL、主機斷電或直接呼叫未註冊 SIGTERM handler 的函式不保證清除。殘留檔案進入下次盤點，不掃描刪除其他 run 的暫存。失敗保留 run log、錯誤和來源；正式收據只在驗證通過後寫入。若正式檔改名成功但收據落盤失敗，維持待核對狀態，不能自動覆寫重試。

共用 CLI 使用 stderr 顯示實際階段、檔數／位元組數與耗時，stdout 保持 JSON。未知掃描總量只報已掃檔數，不捏造百分比。TTY／plain 沿用 `Progress`。不改動進行中的渲染程序。

## 7. 容量盤點與清理操作

從 CEH repo 執行只讀盤點，明確列出每個工作區：

```bash
PYTHONPATH=tools/ceh_video python3 -m ceh_video.storage --plain \
  "$HOME/Videos/CEH_M10_optimization_v1" \
  "$HOME/Videos/Island_Workshop_MATLAB_Concepts_v3_images_gpu" \
  "$HOME/Videos/island-workshop-matlab-practice-v1"
```

輸出包含規範版本、UTC 量測時間、各分類占用、略過的連結與掃描錯誤。掃描不完整時返回非零 exit code；`reclaimable_bytes` 維持 null。本版沒有 `--delete` 或自動清理歷史檔案的指令。

歷史清理必須形成具名清單：絕對路徑、所屬 release／run、分類、配置容量、是否活躍、最後可還原來源、已驗證封裝位置、保存決定與執行日期。確認沒有活躍程序或其他資料依賴，保留完整證據及唯一素材，再執行明確範圍的清理。移動到同一顆磁碟的垃圾桶不計為釋放容量。

## 8. 發行 metadata 與檔案命名

每次新發行記錄 `release_id`、語言／音訊政策、建立時間與時區、引擎版本、規範版本、來源 revision／SHA manifest、runtime pins、影片與字幕 SHA、技術 gate、人工 gate、公開狀態、保存位置及下一關。依據資料夾名稱推測的版本不能替代收據。

建議新工作區格式：`<series>_<topic>_<locale>_v<major>_<minor>_<patch>`。現有路徑與引用保持不變；日後遷移須保留舊→新定位與 checksum map。

規範使用 SemVer：破壞還原／保存契約增加 major；新增相容流程增加 minor；文字或相容修正增加 patch。文件版本、引擎版本與每部影片版本分開管理。更新時新增日期、變更理由、受影響路線、驗證、遷移與回退方式。

## 9. 驗證、落地範圍與後續門檻

[驗證紀錄](evidence/longform-storage-validation-2026-10-22.json)保存測試命令、結果、程式身分與限制；[盤點紀錄](evidence/longform-storage-inventory-2026-10-22.json)保存實際目錄容量。

已實作：只讀分類盤點、CEH partial 清理、中文直接來源封裝／暫存解壓／atomic promotion、MATLAB 實作片串流 CRC／SHA 驗證、已交付版本保護。測試覆蓋檔案異動、雜湊失敗、磁碟不足、例外、中斷、舊檔保護、hardlink／symlink 與 JSON 輸出。

尚未啟動：跨版本內容定址共享資產庫、全域快取配額／LRU、歷史工作區自動刪除、NAS 搬移、編碼器／畫質變更及全長效能比較。這些項目須有獨立需求、還原與品質證據，不能因本規範存在而自動執行。

下一部新版本應採本規範，完成實際全片與新封裝驗證後，記錄製作前、峰值與結束後容量。當前測試支持程式行為，不代表已釋放歷史空間或取得全片縮時數據。

## 10. 版本紀錄

| 日期（Asia/Taipei） | 版本 | 變更 | 驗證與遷移 |
| --- | --- | --- | --- |
| 2026-10-22 | 1.0.0 | 建立共用製作／保存契約；引擎 0.5.5 儲存維護；涵蓋英文、中文概念與 MATLAB 實作三路線 | 回歸測試與只讀盤點；新版本採用；歷史影片與 ZIP 維持原狀 |
