# M04-09 SNMP 列舉｜初版發布

[公開教學來源](../source/2026-10-26-one-concept/M04-09-teaching.md) · [中文頁](https://learn.cs-kairos.com/courses/ceh/v13/m04/concepts/m04-09/) · [英文頁](https://learn.cs-kairos.com/en/courses/ceh/v13/m04/concepts/m04-09/)

內容版本 v1.0.0、revision 1：六節完整教學、一題尚待回答的小檢核。涵蓋 Manager／Agent／MIB／OID、GET／GETNEXT／WALK／SET、連接埠、安全層級及讀取與修改的證據界線。沒有執行 SNMP 查詢或修改設備。下一核心 M04-10 LDAP。

原文技術句子與順序保留；標題、摘要與語意清單依網站格式呈現。公開版僅排除最後一句的私人交付／理解狀態，保留「用一兩句回答就好。」；精確完整交付原文存於私人來源庫。新增 GET 要求／權限檢查／回應圖明標「網頁補充」，不把讀到名稱當成寫入或登入證據。HTML/CSS 響應式重排與固定布局 SVG 分開；中文 SVG 1853 bytes、英文 1880 bytes。正文、圖解直接呈現，沒有新增收合控制或虛構學員 Q&A。

## 發布與驗證

[PR #29](https://github.com/JasonLn0711/kairos-learning/pull/29) 先以 draft 建立，品質檢查後合併。實作 `64aa302565f38ce2df5112bb0783a488304d816f`；正式部署 `805995b1fb054e12f43771cbc0b258ddab60736b`。[品質 CI](https://github.com/JasonLn0711/kairos-learning/actions/runs/40247733594)、[Pages](https://github.com/JasonLn0711/kairos-learning/actions/runs/40247831605) 均成功。

內容驗證、三個測試檔、Svelte 型別檢查（零錯誤／警告）、建置、發布邊界與 208 頁 release 驗證通過。每語言 44 個來源／圖解片段核對。GX10 Brave 正式雙語正文與本機全文一致；320／390／1280 實際寬度無溢出，錨點完整，鍵盤導航可用。兩個正式 SVG DOM 與本機相同。

主要來源：[Net-SNMP](https://www.net-snmp.org/tutorial/tutorial-5/commands/snmpgetnext.html)、[RFC3416](https://www.rfc-editor.org/rfc/rfc3416.html)、[RFC3417](https://www.rfc-editor.org/rfc/rfc3417.html)、[RFC3418](https://www.rfc-editor.org/rfc/rfc3418.html)、[RFC3415](https://www.rfc-editor.org/rfc/rfc3415.html)。RFC3411 直接擷取遇限流，保留原文引用並以相關 RFC 核對。

限制：未重試先前待批准的瀏覽器原生存檔，不宣稱原生下載或正式 HTTP 位元組比對完成；未進行完整螢幕閱讀器認證。
