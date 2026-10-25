# M04-07 Unix/Linux 使用者列舉

[完整交付教材](../source/2026-10-25-one-concept/M04-07-teaching.md)保存原文；[中文概念頁](https://learn.cs-kairos.com/courses/ceh/v13/m04/concepts/m04-07/)與[英文概念頁](https://learn.cs-kairos.com/en/courses/ceh/v13/m04/concepts/m04-07/)沿用穩定 ID。

教學涵蓋帳號、UID/GID、主要／附加群組、passwd/shadow 資料界線、NSS/getent、指定帳號與目前工作階段身分，以及路徑／ACL 與當次操作的證據判讀。範例為合成，沒有執行帳號查詢或檔案操作。

網頁保留完整原文順序，另外明列一張「帳號查詢／工作階段／指定讀取」平行證據卡。依[響應式圖解規格](https://github.com/JasonLn0711/kairos-learning/blob/main/docs/content-authoring.md#responsive-teaching-diagrams--adopted-october-25)採原生 HTML/CSS，提供[中文 SVG](https://learn.cs-kairos.com/images/ceh/m04-07-evidence-zh.svg)（1,537 bytes）與[英文 SVG](https://learn.cs-kairos.com/images/ceh/m04-07-evidence-en.svg)（1,636 bytes）。比較卡表達不同證據範圍，不是權限階梯或量測圖表。

一題小檢核待本人回答；Q&A 保持待補，教材交付不等於理解。下一核心依[既有路線](../notes/m04-enumeration/reading-route.md)為 M04-08 NFS。M04-01 已發布的實際 Q&A 保留。

## 來源查核

2026-10-25 已閱讀原始專案手冊：[Linux credentials](https://man7.org/linux/man-pages/man7/credentials.7.html)、[passwd](https://man7.org/linux/man-pages/man5/passwd.5.html)、[shadow](https://man7.org/linux/man-pages/man5/shadow.5.html)、[getent](https://man7.org/linux/man-pages/man1/getent.1.html)、[GNU id](https://man7.org/linux/man-pages/man1/id.1.html)、[NSS](https://man7.org/linux/man-pages/man5/nsswitch.conf.5.html)、[path resolution](https://man7.org/linux/man-pages/man7/path_resolution.7.html)、[ACL](https://man7.org/linux/man-pages/man5/acl.5.html)。GNU 網站 id HTML 抓取逾時，改讀 man7 託管的 GNU coreutils 原始手冊頁；未引用未讀到的版本細節。
