# CEH M09-03｜語音釣魚、簡訊釣魚與身分冒充

2026-10-29 教材準備與公開編修紀錄。穩定 ID：CEH M09-03；內部 key：CEH26-M09-C03；[現行路線](../study-plan/core-route-2026-10-27.md#ceh26-m09-c03)第 10 個教學設計單元。161 為教學設計數量，不是官方固定概念數。

## 完整教材與公開呈現

完整繁中與英文稿以初學者為對象，從 Northstar 合成簡訊／來電情境，連到 Vishing、Smishing、Impersonation 的管道／手法區別；承接 M09-02 的目標分類，解釋來電顯示、語音複製、身分驗證與授權、一次性驗證碼及 MFA 邊界、獨立查證、縱深防禦與證據判讀。

教材採生活例子、定義／用途／條件、必要子概念、防護、合成證據矩陣、無連線桌上練習及一個情境小檢核。詳細網頁稿有 12 節與 5 張比較表；正文與表格直接閱讀，三段參考解答對應同一情境，預設收合且與實際 Q&A 分開。中英內容語意一致。範例只做紙上判斷，不發送訊息、不撥號、不提供操作真實目標的指令。

網站 canonical 內容由 [kairos-learning](https://github.com/JasonLn0711/kairos-learning) 持有；本 repo 保留路線、教學與來源橋接。目標網址：
- 繁中：`https://learn.cs-kairos.com/courses/ceh/v13/m09/concepts/m09-03/`
- 英文：`https://learn.cs-kairos.com/en/courses/ceh/v13/m09/concepts/m09-03/`

**本紀錄建立時：完整雙語教材與參考解答已備妥；正式網站發布、內容讀回與手機呈現尚待獨立核驗。目標網址不是上線證據。** 後續版本以實際 CI／部署與正式頁驗證更新，不將教材呈現修訂算成新增單元。

## 官方來源與技術界線

2026-10-29 已讀原始官方資料：

- [加拿大資安中心：Vishing／ITSAP.00.102](https://www.cyber.gc.ca/en/what-voice-phishing-vishing-itsap00102)，頁面更新 2026-07-21：語音社交工程、可信身分冒充、來電獨立查證。
- [加拿大資安中心：Smishing／ITSAP.00.103](https://www.cyber.gc.ca/en/guidance/smishing-protect-yourself-sms-attacks-itsap00103)，頁面更新 2026-04-24：SMS 釣魚、來源與對話串外觀、可信入口。
- [加拿大資安中心：Social engineering](https://www.cyber.gc.ca/en/guidance/social-engineering-itsap00166)：身分冒充與跨情境信任問題。
- [FTC：How to avoid a scam](https://consumer.ftc.gov/articles/how-avoid-scam)：來電識別可被操弄；查證來源獨立於可疑要求。
- [FTC：AI voice cloning](https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes)：熟悉的聲音不足以建立可信身分。
- [NIST SP 800-63B-4 §3.2.5](https://pages.nist.gov/800-63-4/sp800-63b.html#phishres)：手動 OTP 輸出沒有綁定特定驗證工作階段，不屬抗釣魚驗證。
- [NIST：Phishing resistance](https://www.nist.gov/blogs/cybersecurity-insights/phishing-resistance-protecting-keys-your-kingdom)：多管道釣魚與驗證防護的作用範圍；現行規範以最終 SP 800-63B-4 為準，不引用舊草案作現行要求。

管道、冒充身分、目標及要求為不同觀察角度；本課四問法與證據矩陣是教學整理，不宣稱官方固定攻擊階段。接觸、資訊暴露、驗證成功、未授權活動與資料外洩各自需要證據。

## 路線與關聯

[閱讀規則](../study-plan/concept-reading-2026-10-22.md) · [M09 索引](../study-plan/core-concept-index-2026-10-27.md) · [前課 M09-02](m09-02-publication.md) · [公開教學橋接](public-teaching-bridge-2026-10-23.md#m09-03-2026-10-29)。後續單元為 M09-04 Pretexting／Baiting／Tailgating；M09-06 再深入獨立驗證與防釣魚控制。

私人聊天識別、原始交付與個人作答／理解狀態沿用已確認私人的 Planning 正本，本公開文件只保存教學與發布邊界。既有教材、穩定 ID、M04 歷史與容量規則保持。


<a id="m09-03-publication-1-1-0-2026-10-29"></a>
## 2026-10-29 最新主稿 v1.1.0｜部署成功，正式頁驗證待補

**[PR #48](https://github.com/JasonLn0711/kairos-learning/pull/48) 已合併；[Pages 40840001516](https://github.com/JasonLn0711/kairos-learning/actions/runs/40840001516) 為 completed／success，對應 merge SHA `a7ffb6b846e5a9e82c87058832cea63a776100ff`。** 合併與部署的精確 SHA 已由 GitHub 讀回核對。

本次以最新提供的完整主稿為主要內容，公開內容版 **v1.1.0／revision 2**。遠端該版 [concept JSON](https://github.com/JasonLn0711/kairos-learning/blob/a7ffb6b846e5a9e82c87058832cea63a776100ff/content/concepts/m09-03.json) 讀回確認：繁中、英文各 **143 個內容區塊、3 張表格、7 組圖解、4 段預設收合參考解答**；14 份簡潔設計的中英文 SVG 配對呈現。實際 Q&A 欄位維持獨立，編輯參考解答不作為學員問答。

- [繁中教材](https://learn.cs-kairos.com/courses/ceh/v13/m09/concepts/m09-03/) · [英文教材](https://learn.cs-kairos.com/en/courses/ceh/v13/m09/concepts/m09-03/)
- [雙語 SVG 圖檔包](https://learn.cs-kairos.com/downloads/ceh-m09-03-bilingual-svg.zip)：此為建置內容的正式目標連結，正式下載內容尚未讀回核實。
- CI 的內容驗證、測試、型別檢查、發布邊界、release 驗證、既有下載 checksum 及 deploy-pages 步驟均為 success。這些是工程證據，不取代瀏覽器實際操作。
- **正式 HTML 正文、正式下載、手機版與鍵盤操作仍未完成核驗。** 受限制的讀取路徑未重試；本紀錄不將「部署成功」改寫成「正式內容與互動全部驗收通過」。

上方 12 節／5 表／3 解答與待部署描述保留為較早準備快照；本節為現行公開版本。這是 M09-03 同單元主稿修訂，既有教學來源、穩定 ID 與後續 M09-04 路線維持，不新增單元。
