# M09-06｜獨立驗證與反釣魚控制

2026-10-30；Module 09：Social Engineering。現行[教學路線](../study-plan/core-route-2026-10-27.md#ceh26-m09-c06)的 **Independent Verification & Anti-Phishing Controls** 單元；161 是教學設計數量，不是官方固定考點數。

## 核心與完整教材範圍

**從既有可信來源查證身分、特定要求與授權，再以互補控制保護行動。信任、驗證、授權與整體防護各有角色。**

以虛構 Northstar 教材中心收到廠商名單移轉要求為主線，連結獨立查證、可信通訊錄、具體目的地與用途核准、郵件網域驗證、抗釣魚身分驗證、最小權限、通報與證據範圍。案例為匿名合成，教學只做概念推理，不操作第三方目標或收集真實驗證材料。

教材採完整初學者繁中與配對英文：結論、定義、用途條件、連貫機制、完整例子、防護及證據、小檢核。3 項圖形推理參考解答與正文分開，網站整合時預設收合；正文、表格與圖直接呈現。參考答案是教材，不是實際學員 Q&A。

## 四組雙語原生 SVG

1. **信任來源與執行邊界**：將未核實說法、獨立可信查核與受保護行動分開；虛線框是查核區，箭頭是通過查核後的流程，不是封包路徑。
2. **回撥查核**：既有可信聯絡資訊的回撥、特定要求詢問與回覆；箭頭代表通訊方向，拒絕／不明與核實成功是替代結果。
3. **互補控制位置**：郵件來源、訊息與端點、人的工作流程、登入驗證、影響與應變；使用分層卡片而非連續箭頭，避免表達成每封信必經的固定管線。
4. **觀察與推論界線**：DMARC 通過、MFA 登入成功、未觀測到告警各有證明範圍；下一步分別核實要求授權、交易／工作階段、偵測涵蓋率及紀錄。

8 份 SVG 含 `viewBox`、獨立識別碼、`title`／`desc`，按欄位寬度等比例縮放；共用網站元件的顯示寬度為 100%、高度自動，無固定顯示尺寸或最小寬度。XML 與無腳本／外部引用檢查已通過；Inkscape 渲染與雙語目視核對已完成。這些是原生圖形核驗，不代替正式網站瀏覽器或手機實測。

## 技術核對與校訂

- SPF 檢查傳送層寄件網域的來源主機授權，與可見 From 身分分開。
- DKIM 簽章驗證與受簽內容完整性，與內容誠實性、加密分開。
- DMARC 通過需要符合對齊條件的 SPF **或** DKIM 通過；任意網域的 SPF 通過不足。相似網域或遭接管的真信箱仍可能通過驗證。
- WebAuthn／FIDO2 抗釣魚驗證保護登入機制，與登入後資料分享或付款授權分開；復原、端點與工作階段仍有各自防護需求。
- **QA 校訂：**「未觀測到告警」只支持目前看不到告警，還須查告警產生、收集、傳遞、規則與涵蓋率；不直接推論偵測條件沒有觸發。中英正文及圖4已一致修正。
- 獨立管道仍須維護；回撥不是絕對保證。緊急工作沿既有核准流程進行；處置依實際點擊、輸入、執行、傳送情況區分。

## 第一手來源

- [FTC：How To Recognize and Avoid Phishing Scams](https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams) — 使用既知真實聯絡管道，與可疑訊息提供的資訊分開。
- [NCSC：Phishing attacks: defending your organisation](https://www.ncsc.gov.uk/guidance/phishing) — 組織多層防護，涵蓋技術、流程及通報。
- [NCSC：Email security and anti-spoofing](https://www.ncsc.gov.uk/collection/email-security-and-anti-spoofing) — SPF、DKIM、DMARC 的角色與防冒充範圍。
- [IETF RFC 9989：Domain-based Message Authentication, Reporting, and Conformance (DMARC)](https://www.rfc-editor.org/rfc/rfc9989.html) — 郵件驗證與對齊機制；2026 年 5 月版本，取代 RFC 7489。
- [NIST SP 800-63B-4 §3.2.5：Phishing Resistance](https://pages.nist.gov/800-63-4/sp800-63b.html#phishres) — 抗釣魚驗證機制及 verifier-name binding。

## 關聯與發布狀態

[閱讀規則](../study-plan/concept-reading-2026-10-22.md) · [前課 M09-05](m09-05-publication.md) · [教學橋接](public-teaching-bridge-2026-10-23.md#m09-06-2026-10-30) · [M09 章後補充](../study-plan/core-route-2026-10-27-supplements.md#m09)。本課收束 M09 信任不能取代驗證的核心，連結 M01 的授權、縱深防禦與事件應變；下一個路線單元是 [M02-01：Passive vs. Active Reconnaissance](../study-plan/core-route-2026-10-27.md#ceh26-m02-c01)。

目標頁：[繁中](https://learn.cs-kairos.com/courses/ceh/v13/m09/concepts/m09-06/) · [English](https://learn.cs-kairos.com/en/courses/ceh/v13/m09/concepts/m09-06/)。**[草稿 PR #53](https://github.com/JasonLn0711/kairos-learning/pull/53) 已建立，head `16e62084278e2ecf715c3f938e06088d8dbf060c`；[CI 40978442982](https://github.com/JasonLn0711/kairos-learning/actions/runs/40978442982) 已 completed／success，核對同一 head，未轉為可審查、未合併、未部署。目標連結不是已上線宣告。** 本機 47 項測試、Svelte 0 錯誤／0 警告、內容驗證、發布邊界及雙語完整靜態輸出核驗通過；已測 tree `80a2a16f983645bf34992a782678ab779c5a1d01` 與遠端 PR tree 一致。M02 八個單元只加入待教目錄，未新增教材，以維持 M09-06 後正確導向 M02-01。私人聊天識別、交付回執、個人筆記與理解狀態不置於公開紀錄。


## 2026-10-30｜M09-06 v1.0.0 發布核驗

已依批准將 [PR #53](https://github.com/JasonLn0711/kairos-learning/pull/53) 轉為可審查並合併。合併前再次核實 head `16e62084278e2ecf715c3f938e06088d8dbf060c` 與 [CI 40978442982](https://github.com/JasonLn0711/kairos-learning/actions/runs/40978442982) 的 completed／success 一致；merge SHA 為 `8d7fe8fc44a1f2814a7422c444649607a9199609`。

[Pages 40981473221](https://github.com/JasonLn0711/kairos-learning/actions/runs/40981473221) 已 completed／success，精確對應上述 merge SHA；部署步驟於 00:44:18 UTC（台灣 08:44:18）成功，工作流程於 00:44:21 UTC 更新為成功。main tree `80a2a16f983645bf34992a782678ab779c5a1d01` 與已核驗的 PR／本機 tree 完全相同。

- [繁中教材](https://learn.cs-kairos.com/courses/ceh/v13/m09/concepts/m09-06/) · [英文教材](https://learn.cs-kairos.com/en/courses/ceh/v13/m09/concepts/m09-06/)
- 中英各 4 張原生 SVG 與 3 項預設收合參考解答；正文及表格直接呈現，圖形依欄寬等比例縮放。
- 47 項測試、Svelte 0 錯誤／0 警告、內容、發布邊界、靜態 release 及既有下載 checksum 均通過；audit high gate 通過，既有 5 項 low 提醒未以強制升級消除。
- **正式網站正文與下載內容讀回、瀏覽器／手機呈現及鍵盤互動仍未核驗。** 既有受限路徑未重試或繞過；Pages 部署成功不等於這些驗收已完成。

上方草稿與未部署敘述保留為歷史快照；本節為最新發布狀態。後續仍接 M02-01，M02 的八個目錄項目不代表已交付教材。公開參考解答不代表實際學員作答或理解。
