# M04-08 NFS 列舉｜初版發布

[完整教學原文](../source/2026-10-25-one-concept/M04-08-teaching.md)保存實際交付文字；[中文頁](https://learn.cs-kairos.com/courses/ceh/v13/m04/concepts/m04-08/)與[英文頁](https://learn.cs-kairos.com/en/courses/ceh/v13/m04/concepts/m04-08/)維持一概念一頁。

初版內容版本 **v1.0.0**、內部 revision 1；六節涵蓋 export/mount、showmount 與 NFSv4 的觀察界線、UID/GID、root_squash、共享與檔案權限、合成案例、防護及一題小檢核。既有概念版本保持原值。原文標題由頁面標題呈現，結論置於摘要，晚間標籤置於文章開頭；其他正文與順序完整保留，連結、清單及指令改為語意格式。

網頁另有明示的合成證據對照圖；HTML/CSS 會重排，獨立 SVG 採固定布局。[中文 SVG](https://learn.cs-kairos.com/images/ceh/m04-08-evidence-zh.svg) 1,515 bytes，[英文 SVG](https://learn.cs-kairos.com/images/ceh/m04-08-evidence-en.svg) 1,540 bytes。三個觀察並列，不代表自動授權的步驟。依使用者最新偏好，正文與圖解直接呈現；實際 Q&A 尚無內容，不新增收合控制。

原始教學含一題待回答小檢核；發布不代表理解或完成實驗。下一核心為 M04-09 SNMP。沒有執行 NFS 查詢、掛載或權限變更。

## 來源與驗證

2026-10-25 核對 [nfs-utils showmount](https://man7.org/linux/man-pages/man8/showmount.8.html)、[exports](https://man7.org/linux/man-pages/man5/exports.5.html) 與 [RFC 7530](https://www.rfc-editor.org/rfc/rfc7530.html#section-3.1)。showmount 依賴 MNT 服務，NFSv4-only 服務可能不公開該介面；root_squash 與密碼學保護分開說明。

[PR #28](https://github.com/JasonLn0711/kairos-learning/pull/28) 先建立 draft，品質驗證後合併。實作 `8631adad19428a9bb5b69452f3facb0e3ed56770`，部署合併 `d0bdba5491e547f12329eb74aad67028b85516be`。[品質 CI](https://github.com/JasonLn0711/kairos-learning/actions/runs/40187641384) 與 [Pages](https://github.com/JasonLn0711/kairos-learning/actions/runs/40187729237) 均成功。

本機內容、單元測試、型別、發布邊界、建置與 206 頁驗證通過。GX10 Brave 正式頁雙語 320／390／1280 無橫向溢出、缺失錨點或非 Q&A 收合；鍵盤導覽可用。正式正文與本機渲染全文一致；每語言 55 個來源／圖解片段核對。正式 SVG DOM 與本機一致。

限制：命令列 urllib 抓取正式頁及 SVG 回覆 HTTP 403，沒有重試，所以不宣稱正式 HTTP 原始位元組比對成功。瀏覽器正常讀回完成；先前待批准的原生存檔未重試，亦未進行完整螢幕閱讀器認證。
