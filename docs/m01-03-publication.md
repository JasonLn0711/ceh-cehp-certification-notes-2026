# CEH M01-03｜道德駭客、合法授權與交戰規則 — v1.0.0

**狀態：2026-10-27 已完成網站部署與正式雙語文字／圖檔讀回。**

[教學正文](../source/2026-10-27-one-concept/M01-03-teaching.md) · [既有 M01 基礎講義](../notes/2026-09-20-ceh-week-01/m01-foundations.md#authorization) · [新路線](../study-plan/core-route-2026-10-27.md) · [穩定概念索引](../study-plan/core-concept-index-2026-10-27.md)

## 結論與範圍

本課為新路線第 **3** 單元，穩定 ID `M01-03`，完整範圍為 **Ethical Hacking、Authorization、Rules of Engagement（ROE）**。承接 M01-01 的保護目標與 M01-02 的風險判讀，說明資安測試必須具備適當授權、具體範圍與執行邊界；技術上做得到，不代表已取得許可。

- 中文正式頁：<https://learn.cs-kairos.com/courses/ceh/v13/m01/concepts/m01-03/>
- 英文正式頁：<https://learn.cs-kairos.com/en/courses/ceh/v13/m01/concepts/m01-03/>
- 正式頁已經標準 HTTPS 讀回；下方記錄本次精確證據及未完成的瀏覽器驗證。
- 本課沒有操作第三方目標，也不以一份通用 ROE 取代實際法律、契約或第三方授權審查。

## 呈現與學習邊界

沿用[現行 CEH 呈現規範](public-teaching-bridge-2026-10-23.md#ceh-answer-presentation-2026-10-27)：正文與圖表直接呈現；程式碼／命令／輸出採淺底深字；理解測驗提供預設收合的白話繁中參考解答，英文頁保持語意一致。參考答案與實際學員 Q&A 分開。

教材準備、對話交付、網站發布、本人作答與理解確認是不同證據。此公開紀錄不保存私人交付識別碼、原始私人筆記或個人理解狀態，也不預填任何學習完成。沿用既有路線，不另建平行 M01 閱讀路線，不變更原 M04 ID 或歷史。

## 發布與核驗

- [網站 PR #37](https://github.com/JasonLn0711/kairos-learning/pull/37)，實作 `d012f7189448b4585cb068293ead4574fc8899b3`；已合併 main `9683624b927f5b59843cb8cadac2008e206c04ed`。
- [品質 CI 40494048402](https://github.com/JasonLn0711/kairos-learning/actions/runs/40494048402) 全步驟成功；[Pages 40494181903](https://github.com/JasonLn0711/kairos-learning/actions/runs/40494181903) 成功。
- 本地內容檢查、24 單元測試、Svelte 0 errors/warnings、draft/future 發布邊界、乾淨建置與 220 HTML release check 通過。已發布概念從 14 增至 15，測試確認 M01-03 有正文而 M01-04 仍未發布。
- 2026-10-27 正式雙語各 37 個 source blocks 的文字、表格、圖解與答案逐一讀回，無缺漏；每頁 1 個參考答案預設收合，沒有預設展開的 details。
- 兩份圖檔透過正式 HTTPS 下載，與來源 bytes 相同：中文 2,178 bytes、英文 2,250 bytes，均小於 100,000 bytes。流程為可重排 HTML；SVG 為獨立固定布局下載。
- 沿用既有 CEH 淺色程式碼樣式；本課不要求執行命令、掃描或存取真實系統。
- **未完成：** 雲端 Chromium sandbox 無法啟動，因此實際手機／桌面視覺、鍵盤互動未測；沒有使用未授權的使用者電腦，沒有拿前次課程結果冒充本次通過。

已先在私人對話交付完整教學，再執行上述發布；公開文件不放私人訊息 ID 或個人理解紀錄。Planning 日／週同步另列權限待處理，未重試先前受阻操作。

## 來源與呈現校訂

NIST SP 800-115 第 6～8 章與附錄 B（2026-10-27 查核）支援規劃、ROE、協調、資料處理與報告範圍；不是個別系統授權書，也不是本地法規適用的法律意見。課內七項清單屬教學整理；Northstar、帳號與 `.test` 目標皆為合成紙上例。AI／工具不代替授權，NDA 不等於任意測試許可，跨主機連結不自動擴張範圍。

網站保留完整七節語意，以三個表格整理聊天室條列；另附一個四步響應式流程與固定版 SVG 下載。只有參考解答收合，圖解正文直接呈現。M01-01／02 舊內容與本輪既有 ID、網址未變；M01-04 僅為下一預排單元，未建立已交付狀態。
