# M04-02 DNS 補充教材：v2 校訂紀錄

2026-10-23。這是既有 DNS 核心的深化修訂；原交付教學保留於 [原文](../source/2026-10-23-one-concept/M04-02-teaching.md)，公開完整校訂內容見 [v2 中英文](../source/2026-10-23-one-concept/M04-02-supplement-v2.md)。[中文原頁](https://learn.cs-kairos.com/courses/ceh/v13/m04/concepts/m04-02/)與[英文原頁](https://learn.cs-kairos.com/en/courses/ceh/v13/m04/concepts/m04-02/)沿用穩定 ID。下一個核心仍為 M04-03 FTP。

## 原文、採用與差異

提供的詳細教材包含十一節、四題選擇題及一題情境題。私人原文完整保存；公開版清除 Mermaid CSS、來源顯示殘片、favicon／+1、複製按鈕與無功能送出文字。教學中的自問自答與測驗歸教材，Q&A 等實際問題與討論後補。

| 原教材 | v2 整合位置與決定 |
| --- | --- |
| 一、DNS 第一原理 | story：名稱、IP、分散式查詢與聯絡簿情境。 |
| 二、解析流程 | roles：新增原生 HTML 流程圖；區分公開根／TLD 流程與自建 .test 區域。 |
| 三、八種記錄 | records：補 IPv6、CNAME 與 HTTP redirect、MX、SOA、委派、PTR 與 CDN。 |
| 四、列舉目的 | roles／records：已知名稱、資產清單及授權來源；單筆查詢的範圍。 |
| 五、操作 | practice：工具確認、指定 DNS、合成完整判讀範例、欄位拆解、各類查詢及 Windows 替代工具。 |
| 六、失敗判讀 | responses：NOERROR／referral／NODATA、SERVFAIL、Timeout、TTL、Split-Horizon。 |
| 七、AXFR | defense：一個區域的管理功能、TCP、存取控制與 TSIG。 |
| 八、安全概念 | defense／security：Cache Snooping、DNSSEC／DoH／DoT／HTTPS 與 NSEC 選讀。 |
| 九、系統階段 | layers：名稱→連線→TLS→HTTP→存取控制，附 curl HEAD 條件與證據欄位。 |
| 十、優先順序 | priorities：P0/P1/P2 是教學安排；25–35分鐘只作彈性閱讀估計，容量上限保留。 |
| 十一、測驗 | check：原四題答案 B/C/B/C，逐選項解析；原情境題保留為 Q5，附展開參考解析。 |

## 技術校訂與來源

- 全部操作改用已設定的授權實驗 DNS 與 `.test`、文件 IP；不向公開解析器或真實網站實測。保留名稱依 [RFC 2606](https://datatracker.ietf.org/doc/html/rfc2606)、IPv4 依 [RFC 5737](https://www.rfc-editor.org/rfc/rfc5737)、IPv6 依 [RFC 3849](https://www.rfc-editor.org/rfc/rfc3849)。原文通用 Ubuntu 安裝兩行改為依系統與管理政策安裝，教材不執行套件變更。
- TTL 是回應記錄的快取存活時間；快取回覆通常為剩餘值，權威回覆通常為設定值。原文把所有 TTL 都說成剩餘值，已限定條件。[RFC 1034](https://www.rfc-editor.org/rfc/rfc1034)／[RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035)。
- NOERROR 空 Answer 要看 Authority、別名鏈及查詢對象，不能直接等同 NODATA；referral 要繼續查詢。[RFC 2308](https://datatracker.ietf.org/doc/html/rfc2308)。
- [RFC 9824](https://www.rfc-editor.org/info/rfc9824/) 已定義 Compact Denial 與 NXNAME：不存在名稱可呈現 NODATA-like NOERROR。因此一般 NODATA 的「名稱存在」解釋加上適用前提，Q2 明示排除進階例外；選讀保存完整證明判讀方向。
- AXFR 複製一個區域，已委派子區域資料獨立管理；存取控制與驗證分開確認。[RFC 5936](https://datatracker.ietf.org/doc/html/rfc5936)。
- DNSSEC 是來源驗證／完整性，DoH／DoT 是傳輸保護；端點仍處理查詢。NSEC 揭露程度依簽署方式，避免宣稱所有簽署區域可完整列出。[RFC 4033](https://www.rfc-editor.org/rfc/rfc4033)、[4034](https://datatracker.ietf.org/doc/html/rfc4034)、[7858](https://datatracker.ietf.org/doc/html/rfc7858)、[8484](https://datatracker.ietf.org/doc/html/rfc8484)。
- dig 完整輸出優先；`+noall +answer` 只適合已確認資料的精簡檢視。[ISC dig](https://bind9.readthedocs.io/en/stable/manpages.html#dig-dns-lookup-utility)。Windows 語法依 [Microsoft Resolve-DnsName](https://learn.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname)。
- curl 不繼承 dig 的指定伺服器；示例要求本機解析及信任憑證完成，HEAD 結果只對該請求成立。[curl 官方手冊](https://curl.se/docs/manpage.html)。

查核日為2026-10-23。來源引用已換成可回查的一手文件。工具查閱、合成輸出與實際學員操作分開；本次沒有執行 DNS／AXFR 探測，也沒有學員作答。

## 版本與呈現

網站資料正本 `kairos-learning/content/concepts/m04-02.json` revision 2；沿用既有 ConceptBlocks／ConceptChecks，增加兩張原生流程圖，保留原四步判讀圖。圖解呈現查詢分工與排查順序，不建立虛構量測數據、學習完成率或新圖表套件。進階內容折疊，手機長指令使用原有可捲動區塊。公開教材不帶私人交付 ID 或原始資料檔。

網站建置、雙語內容、測驗解析、手機桌機與正式發布證據由網站 release note 及私人 publication receipt 接續保存。學員理解與網站發布各自驗證。
