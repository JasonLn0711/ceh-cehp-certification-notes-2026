# CEH M05 production — supplied messages

Captured on 2026-10-18, Asia/Taipei, from the current Codex conversation.
The sections below preserve the supplied wording. The implementation and
validation are recorded separately in the [production record](../../notes/m05-vulnerability-analysis/video-production-2026-10-18.md).

## Original production brief

```text
## CEH 影片製作通則 v1.0

已將 CEH M04 Editorial Masterclass v3.0 定為後續 CEH 教學影片的初版通則。唯一變更是 American English 旁白語速改為原設定的 1.5 倍，不將整部影片直接加速。

其餘沿用 M04 v3.0 的設定：溫暖紙感手繪動畫、原創 Tally 角色、Northstar 共用案例、簡單美式英文、完整長篇教學、1920×1080／30fps、逐幕 SVG、可編輯簡報、HyperFrames／Codex 製作流程，以及案例、測驗與品質驗收。每題原本的 12 秒靜音思考時間也維持不變。

## CEH M05 English Masterclass：Vulnerability Analysis

M05 的課程內容已重新編寫，不是將 M04 腳本直接替換名稱。

完整章節

# 11

分鏡場景

# 58

英文旁白字數

# 8,279

| 章節      | 教學內容                                                |
| ------- | --------------------------------------------------- |
| C01–C02 | 從 Enumeration 到 Vulnerability Analysis、學校網路、授權範圍及證據 |
| C03–C04 | Vulnerability／Threat／Risk、CVE、CWE、CPE、NVD           |
| C05–C06 | 弱點評估方法、掃描器原理、常見工具與實際操作流程                            |
| C07–C08 | CVSS、EPSS、KEV、風險排序、誤報及弱點驗證                          |
| C09–C10 | Northstar 四項弱點案例、修補、重新驗證與 AI 輔助                     |
| C11     | 八題分級選擇題與綜合實務作業                                      |

全片以同一所 Northstar Learning Center 為共同情境。從發現可能的弱點、判斷掃描結果是否可靠，到決定修補順序與驗證方法，都使用相互連貫的例子。

以 1.5 倍旁白語速估算，約 47 分鐘的語音與測驗靜音時間，正式影片還需要加上動畫解說與閱讀停留時間，因此不設定片長上限。

## 下載 CEH M05 完整影片製作包

CEH M05 English Editorial Masterclass v1.0

ZIP · 2.8 MB · 224 個檔案

858 項來源與結構檢查通過，0 項失敗

&#x20;下載完整 CEH M05 ZIP 製作包

重要檔案預覽

18 頁可編輯視覺展示稿

沿用 M04 v3.0 的原始版型、角色與色彩

PPTX

視覺設計預覽

18 頁展示稿縮圖及 58 幕動畫構圖

查看

完整英文旁白逐字稿

8,279 字，包含詳細原理、流程及案例

Markdown

統一製片通則 v1.0

M04 v3.0 完整繼承，語速唯一改為 1.5×

Markdown

Codex／HyperFrames 製作指令

完整長片製作、配音、字幕與驗收流程

Markdown

ZIP 另外包括 58 張可編輯 SVG、原始 Tally 角色與分層素材、四組可拖曳時間軸的動畫程式範例、虛構弱點評估證據、學生作業與教師解答、官方參考來源，以及可重新執行的完整性驗證程式。

驗收結果： 我確認了 M04 原始視覺設定與角色素材的一致性、英文腳本完整性、各章節及場景對應、八次 12 秒靜音設定、SVG 有效性、PowerPoint 可編輯結構及 ZIP 解壓縮與雜湊完整性。

目前完成的是整套可供 Codex 正式製片的來源包，不是已渲染的 MP4。實際 1.5× 美式英文配音、同步字幕及完整影片仍需在 HyperFrames 執行。製作指令已要求直接完成全片，不以短片試作作為前置關卡。

下一步： 解壓縮 ZIP，在 Codex 開啟專案資料夾，請它完整閱讀並執行 `AGENT_PROMPT.md`。
The reference: `CEH_M05_English_Masterclass_HandDrawn_Editorial_v1_FULL.zip`
```

## Implementation request

```text
Implement the plan.
```

## Subsequent M05 timing correction

```text
請修改 M05 的影片的每段 12 秒靜音，全部改為 1 秒。其他不變。（並檢視需優化的地方）
```

Followed by:

```text
Implement the plan.
```

## Documentation and Git request

```text
Using FIRST PRINCIPLE, and please take notes on my day note in the `planning-everything-track` repo, and update the relevant docs, files, and contents for it.
Please update all the commits separately on git, and push this branch to the remote main branch of the github repo. (If there were conflict among commits, i would like to keep both local commits and remote commits.)
And build strong connection with all other relevant files, docs, and contents.
```
