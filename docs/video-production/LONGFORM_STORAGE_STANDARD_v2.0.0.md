# CEH 與課業長片：製作與儲存規範 v2.0.0

| 欄位 | 值 |
| --- | --- |
| 文件 ID／版本 | `longform-storage`／`2.0.0` |
| 建立、生效與最後更新 | 2026-10-22，Asia/Taipei |
| 引擎 | `ceh-video 0.6.0`，本機維護版 |
| 前版 | [v1.0.0](LONGFORM_STORAGE_STANDARD_v1.0.0.md)，保留歷史適用範圍與驗證快照 |
| 授權與採用選擇 | [原始要求及第二輪範圍](../../source/2026-10-22-longform-storage-policy/source.md) |
| 執行證據 | [第二輪紀錄](evidence/longform-round2-2026-10-22/README.md) |

## 目的與責任

稀缺資源為 SSD 空間、渲染時間及審閱時間。CEH repo 擁有共用引擎、規範與執行證據；課業 repo 擁有教材、逐字稿及課務驗收；`~/Videos/<release>/` 保存大型來源與交付品。Planning 保留定位、容量、狀態及下一關。各片既有的聲音、畫質、語速、字幕、測驗、內容與人工審閱契約持續適用。

本版接管新版本的封裝與快取規則。正式交付的 ZIP、影片、收據及原始來源保持原版；改版使用新工作區。`production.json` 未指定 `package_format` 時沿用舊格式；新建工作區選用 `"package_format": "compact-v1"`。英文 migration 已帶入此預設；手動建立華語／實作工作區時必須明列。

## 製作順序與增量重用

1. 固定教材來源、對象、講稿、分鏡、scene ID、release ID、引擎及規範版本。保留來源雜湊、採用素材與授權。
2. 保存原始音訊及處理後音訊，逐段對應講稿與時間戳。只執行版本配方指定的速度處理；不同位元組的 baseline 與 processed 音訊各自保存。
3. 先驗證代表場景：中文長標題、教學圖片、字幕及測驗停頓／揭露。完成 native check、實際畫面擷取與具體畫面審閱後，再進入章節渲染。
4. 以 `run --intent iteration` 迭代。華語章節重用需同時符合目前來源、runtime、實作、編碼輸出及 render 證據雜湊。QA 執行識別改變而媒體輸入相同時，可保留既有有效影片；目前的審閱 gate 仍先執行。
5. 母片重用核對章節、場景 PCM、timeline、profile、解碼器與所有成片證據。相同 PCM 合併輸入與輸出經雜湊核對後直接重用；圖片、host HTML 及素材內容相同時避免重寫。各工作區輸出為獨立檔案。
6. 完整解碼掃描有匹配成片與 runtime 的有效收據時，華語 QA 使用該掃描證據。收據缺失或不符則重新掃描。音訊 sample-for-sample、AAC 靜音、字幕／畫面與測驗檢查仍照常執行。
7. `--force` 繞過該階段重用。失敗或可處理中斷會清除本次成功快取資格與自有暫存；只有本引擎成功執行後才可建立重用收據。歷史交付收據不直接升格為新快取。
8. 交付時執行完整既有技術 gate、封裝、全檔還原驗證及規定的人工審閱。技術通過、人工接受、公開發布與學員完成分別記錄。

## compact-v1 封裝與還原

封裝含 `COMPACT_MANIFEST.json`、`RESTORE.py` 與 `objects/<sha256>`。每個精確 SHA-256 payload 只存一份；manifest 保留原始相對路徑、長度、雜湊及一般檔案權限。去重不改編碼、不重新合成聲音、不以語意相似判定相同。

交付輸出包含 ZIP、`ZIP名稱.sha256` 及相鄰 `RESTORE.py`。離線使用 Python 標準函式庫還原：

```bash
python3 RESTORE.py --archive PACKAGE.zip --destination NEW_DIRECTORY
```

目的地必須尚不存在，父目錄必須存在。工具直接從 ZIP 讀物件，在目的地同磁碟的私人暫存中寫出獨立檔案，核對所有 payload 的 CRC、SHA-256 與長度後才搬成正式目的地。它拒絕路徑穿越、符號連結、重複路徑、檔案／目錄衝突、缺少或多餘物件及特殊權限。驗證失敗或可處理中斷僅移除本次暫存；既有目的地保持原樣。進度走 stderr，完成結果走 JSON stdout。

封裝先核對所有輸入，再寫 partial ZIP、完整還原及驗證，最後發布正式檔。英文路線維持既有零次新推論／零次速度處理的音訊與 host 重建檢查，核對 PCM 與 HTML 身分。新英文 compact 封裝同時納入已驗證的 chapter host 與 combined PCM，讓標準函式庫一次還原可編輯檔案。既有英文 ZIP 轉存測試仍保留其原本的 exclusions；那類舊 payload 的衍生 host 與音訊快取，依包內 provenance 由固定環境的 `python -m ceh_video restore` 重建。runtime 環境依原 lockfile 安裝，未含在 ZIP。

容量預檢為 `unique payload bytes + restored payload bytes + reconstruction reserve + 128 MiB`。華語／實作的重建預留為零；英文另外計入兩份 baseline、processed、metadata 的快取重建及兩倍 host PCM 長度。檔案系統配置與其他程序仍需另留餘裕。預估值與實際量測分開記錄。驗證目錄成功後清除；工作版的增量快取保留。

## 保存與清理

| 分類 | 保存方式 |
| --- | --- |
| 講稿、來源、字幕、原始／處理後語音、配方、lockfile | 保存可追溯版本與精確雜湊 |
| 正式母片、章節交付品、ZIP、SHA、交付收據 | 保留目前候選與已接受正式版；依既定備份位置封存 |
| QA、人工審閱、失敗／成功執行證據 | 留在原擁有 repo／工作區；舊路徑作為歷史原文 |
| 正在迭代的章節片、PCM、AAC 與重用收據 | 保留；有效快取可省下後續重製 |
| 本次 partial／verify／restore 暫存 | 正常成功、例外及可處理中斷後清除 |
| 舊解壓或 staging 副本 | 僅列為候選；須通過下述全項核對 |

刪除採固定 allowlist。先核對保留 ZIP 與原收據的 SHA-256，再串流讀取 ZIP 每個 member 至 EOF，對照實體樹的完整檔案集合、大小與 SHA-256。確認檔案型態、inode、配置區塊、連結、設定／文件依賴、程序使用狀態與協調鎖；刪除前再核對。任一 unique／changed payload、使用依賴或不明狀態使整個目錄保留。

移除後核對正式輸出及收據的保護雜湊，記錄精確路徑、原 ZIP、刪除配置位元組與磁碟 free-space 差額。併行工作會影響 free-space 差額，因此以已移除 inode 配置量另行報告。保留原始來源、M05 無對應 ZIP 副本、測試／clean-C11 工作區及 M11 具名歷史 partial。

尚未指定的外接磁碟／NAS 與版本保留期限不自動推定。移轉時先驗證目的端雜湊與還原能力，再處理本機可移除副本。

## 驗證與版本紀錄

單元測試涵蓋格式、重用失效、輸出損壞、force、低空間、失敗與中斷。實際驗證另外記錄三條歷史封裝路線的完整還原，以及固定 runtime 的中文教學圖像＋測驗代表片段。至少三組 paired warm 比較，分開報告 host、render、master 與 QA；不將片段速度外推成整片效能。

| 版本 | 日期 | 變更 |
| --- | --- | --- |
| 1.0.0 | 2026-10-22 | 直接串流封裝、暫存生命週期、只讀容量盤點與保存規則 |
| 2.0.0 | 2026-10-22 | 精確位元組物件去重、離線還原、華語 verified reuse、具名依賴感知清理與實際比較 |

本版的完成狀態與量測數字以[執行紀錄](evidence/longform-round2-2026-10-22/README.md)為準；規範文字本身不構成影片驗收。

## Planning connection and publication scope — 2026-10-22

[Day record](../../../planning-everything-track/weeks/2026-W43/days/2026-10-22.md#longform-storage-2026-10-22) · [CEH project](../../../planning-everything-track/data/projects/2026-07-ceh-cehp-certification-training.md#longform-storage-2026-10-22) · [Coursework project](../../../planning-everything-track/data/projects/2026-09-cscm30018-teaching-assistant.md#longform-storage-2026-10-22).

The later publication request activates separate source, implementation, standards, evidence and Planning commits. Earlier “no Git publication” statements describe their execution snapshots. Heavy media and the non-Git coursework directory remain local. Next production activation belongs to a named release and its existing human acceptance gates.
