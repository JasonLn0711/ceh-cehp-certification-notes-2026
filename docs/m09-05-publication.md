# M09-05｜內部威脅與身分竊用

2026-10-29；Module 09：Social Engineering。現行 [161 單元路線](../study-plan/core-route-2026-10-27.md)第 12 個教學設計單元；數量不是官方固定考點數。

## 核心與教材範圍

**有權限不代表可以任意使用；帳號活動不等於已確認本人操作；個資外洩不等於已證實身分竊用。**

以虛構 Northstar 教材中心串聯內部威脅、惡意／非蓄意行為、外部人員冒用內部帳號、身分竊用、驗證憑證竊取與帳號接管。身分查核、登入驗證、資源與用途授權分開；正確資料及熟悉聲音、影像不替代可信查核。所有案例為匿名合成，不操作第三方目標。

- 圖1：人、帳號、身分的概念關聯，非必然攻擊順序。
- 圖2：合法查閱與用途／分享權限邊界；實線為授權存取示意，虛線為可能越界，外部帳號冒用另列。
- 圖3：資料暴露、既有帳號接管與冒名申辦；點線不表示後果必然發生。
- 圖4：保留證據、驗證情境、區分已知／推論／待查，必要時先控風險；箭頭是處理流程，非攻擊流量。

正文採初學者白話繁中，配對英文；4 組雙語原生 SVG 採 viewBox、等比例欄寬縮放，無固定顯示寬度／最小寬度。正文與圖直接顯示，僅 3 項參考解答預設收合。編輯參考解答不冒充實際學員 Q&A，也不表示理解已驗證。

## 防護與證據

最小權限、職務分離、權限生命週期、MFA 與復原入口、稽核與資料外洩防護共同降低風險；不存在單項保證。MFA 不會單獨阻止真正員工濫用原有權限。大量下載只是需要查核的事件線索，須核對業務授權、操作結果、裝置與傳送紀錄；帳號或 IP 單獨不證明人與意圖。調查遵守授權、資料最小化與隱私界線，不公開指責尚未查明的個人。

## 第一手來源

- [CMU SEI：Insider Threat](https://insights.sei.cmu.edu/insider-threat/)
- [CMU SEI：Unintentional Insider Threat and Social Engineering](https://sei.cmu.edu/blog/unintentional-insider-threat-and-social-engineering/)
- [FTC：What To Know About Identity Theft](https://consumer.ftc.gov/articles/what-know-about-identity-theft)
- [NIST SP 800-63A-4：Identity Proofing](https://pages.nist.gov/800-63-4/sp800-63a.html)
- [NIST：Least Privilege](https://csrc.nist.gov/glossary/term/least_privilege) · [Separation of Duty](https://csrc.nist.gov/glossary/term/separation_of_duty)
- [NIST SP 800-53 Rev.5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

## 關聯與發布界線

[閱讀規則](../study-plan/concept-reading-2026-10-22.md) · [前課 M09-04](m09-04-publication.md) · [教學橋接](public-teaching-bridge-2026-10-23.md#m09-05-2026-10-29) · [章後補充](../study-plan/core-route-2026-10-27-supplements.md#m09)。連結 M01 的 CIA、風險、授權與縱深防禦；下一單元 M09-06 為 Independent Verification & Anti-Phishing Controls。

目標頁：[繁中](https://learn.cs-kairos.com/courses/ceh/v13/m09/concepts/m09-05/) · [English](https://learn.cs-kairos.com/en/courses/ceh/v13/m09/concepts/m09-05/)。**目前為教材準備／網站整合階段，非已上線宣告。** 精確 PR、CI、合併、部署與正式讀回須分層核實；原生 SVG 320／680 px 渲染不是瀏覽器／手機互動驗證。私人聊天識別、交付回執、個人作答與理解狀態不放公開 repo。


<a id="m09-05-publication-1-0-0-2026-10-29"></a>
## 2026-10-29｜M09-05 v1.0.0 已部署；正式頁讀回待核

**[PR #52](https://github.com/JasonLn0711/kairos-learning/pull/52) 已合併，merge SHA `ab8161538a4442863ae22da898f6e7f4df35ec03`。[Pages 40867362334](https://github.com/JasonLn0711/kairos-learning/actions/runs/40867362334) 為 completed／success，完成時間 11:43:04 UTC（台灣 19:43:04）；對應的精確 merge SHA 已讀回核對。** 發布流程亦核實 deploy-pages 步驟成功。

- [繁中教材](https://learn.cs-kairos.com/courses/ceh/v13/m09/concepts/m09-05/) · [英文教材](https://learn.cs-kairos.com/en/courses/ceh/v13/m09/concepts/m09-05/)
- 中英各 66 個內容區塊、4 張原生 inline SVG、3 段預設收合參考解答；正文與圖形直接呈現，使用 responsive 共用元件按欄寬等比例縮放。
- 精確 head `21876227dca19cce7ac1322071753264d6da68be` 的 [CI 40864414266](https://github.com/JasonLn0711/kairos-learning/actions/runs/40864414266) 通過；整合流程核實正式 main tree `53f9d2a20c05f8eaecda095dfb06f6142dc214e5` 與已測試 tree 相同。
- 44 項測試與完整靜態 release 檢查通過。教材來源、雙語文字與安全 SVG 序列化分離，原生圖形渲染不代替瀏覽器實測。
- **正式網站正文、下載、瀏覽器／手機與鍵盤操作尚未讀回核驗；受限路徑未重試。** 部署成功不宣稱所有互動與呈現驗收完成。

上方準備／未發布敘述保留為歷史快照；本節為最新發布進度。穩定 ID 與單元順序不變，編輯參考答案不視為實際學員作答或理解證據。
