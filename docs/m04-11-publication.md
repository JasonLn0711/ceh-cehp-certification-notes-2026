# M04-11 RPC 列舉｜初版發布

[公開教學來源](../source/2026-10-26-one-concept/M04-11-teaching.md) · [中文頁](https://learn.cs-kairos.com/courses/ceh/v13/m04/concepts/m04-11/) · [英文頁](https://learn.cs-kairos.com/en/courses/ceh/v13/m04/concepts/m04-11/)

內容版本 v1.0.0、revision 1：五節完整教學、一題尚待回答的小檢核。涵蓋 RPC 呼叫、介面／端點、ONC RPC 與 Microsoft RPC、映射與權限的證據界線。沒有執行 RPC 查詢或修改設備。下一核心 M04-12 列舉防護。

原文技術句子與順序保留；標題、摘要與語意清單依網站格式呈現。公開版僅排除最後一句的私人交付／理解狀態，保留「用一兩句回答即可。」；精確完整交付原文存於私人來源庫。新增四種獨立證據對照圖明標「網頁補充」，分別判讀登記、連線、驗證及操作授權。HTML/CSS 響應式重排與固定布局 SVG 分開；中文 SVG 1843 bytes、英文 1872 bytes。正文、圖解直接呈現，沒有新增收合控制或虛構學員 Q&A。

## 發布與驗證

[PR #31](https://github.com/JasonLn0711/kairos-learning/pull/31) 先以 draft 建立，品質檢查後合併。實作 `bf571663edc4be1332cb701632838a620fa8f367`；正式部署 `cdf2ea94db32da8967d0dabb482b0e73719c380f`。[品質 CI](https://github.com/JasonLn0711/kairos-learning/actions/runs/40312626086)、[Pages](https://github.com/JasonLn0711/kairos-learning/actions/runs/40312777924) 均成功。

內容驗證、三個測試檔、Svelte 型別檢查（零錯誤／警告）、建置、發布邊界與 212 頁 release 驗證通過。每語言 51 個來源／圖解片段核對。GX10 Brave 正式雙語正文與本機全文一致；320／390／1280 實際寬度無溢出，錨點完整，鍵盤導航可用。兩個正式 SVG DOM 與本機相同。

主要來源：[RFC5531](https://www.rfc-editor.org/rfc/rfc5531.html)、[RFC1833](https://www.rfc-editor.org/rfc/rfc1833.html)、[Microsoft 服務與連接埠](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements)；本次均成功讀取。

限制：未重試先前待批准的瀏覽器原生存檔，不宣稱原生下載或正式 HTTP 位元組比對完成；未進行完整螢幕閱讀器認證。
