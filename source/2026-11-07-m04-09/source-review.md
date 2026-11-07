# M04-09 來源與編輯審查

查核日期：2026-11-07，Asia/Taipei。版本候選 v1.0.0。主要問題是：不同協定的回應證明什麼，後續需要哪些防護與驗證證據。

## 公開採用與完整性

公開繁中稿只將聊天回覆邀請及理解狀態句改為中性自評：先選答案並說明理由，再展開參考解答；閱讀不代表理解。其餘原稿順序與文字保留。私人交付識別、個人學習進度、筆記及原始聊天紀錄不進公開 repo。

獨立文字審閱確認九節、七類主題、五筆合成觀察、一題 A–D 選項及 16 個相鄰來源連結完整。中英文數字、來源 URL 順序、條件與結論一致。唯一答案為 D；答案是編輯提供，不是學員回答或實際 Q&A。四稿 SHA-256 校驗通過。

## 來源與主張

以下皆為協定規格或官方資料。2026-11-07 以網頁工具查核，沒有進行真實掃描、登入或設定變更。

- [RFC 5905](https://www.rfc-editor.org/rfc/rfc5905.html)：NTP、UDP 123 及 stratum 階層；不把階層當成安全或實測精準度分數。
- [RFC 8633](https://www.rfc-editor.org/rfc/rfc8633.html)：NTP 控制查詢及反射／放大風險，限制不必要管理暴露。
- [RFC 7296](https://www.rfc-editor.org/rfc/rfc7296.html)：IKEv2、500／4500、初始協商與 IKE_AUTH 的身分驗證界線。
- [RFC 4301](https://www.rfc-editor.org/rfc/rfc4301.html)：IPsec 與安全關聯；ESP／AH 的 IP 協定編號不當成 TCP／UDP 埠號。
- [RFC 3261](https://www.rfc-editor.org/rfc/rfc3261.html)、[RFC 3550](https://www.rfc-editor.org/rfc/rfc3550.html)、[RFC 3711](https://www.rfc-editor.org/rfc/rfc3711.html)：SIP 訊令、RTP 媒體及 SRTP 保護分別判讀；SIP TLS 不保證媒體加密。
- [RFC 4861](https://www.rfc-editor.org/rfc/rfc4861.html)、[RFC 4890](https://www.rfc-editor.org/rfc/rfc4890.html)：IPv6 鄰居／路由器探索與必要 ICMPv6；快取不等於完整資產。
- [RFC 4271](https://www.rfc-editor.org/rfc/rfc4271.html)、[RouteViews](https://api.routeviews.org/docs/)：BGP 路由及觀測點的可見範圍，公開資料不代表管理存取權。
- [RFC 5398](https://www.rfc-editor.org/rfc/rfc5398.html)：64496 為文件示例 ASN；203.0.113.0/24 只作文件範例，不聲稱實際公告。
- [RFC 6811](https://www.rfc-editor.org/rfc/rfc6811.html)、[RFC 7454](https://www.rfc-editor.org/rfc/rfc7454.html)：路由來源驗證及運作防護；不把來源驗證當成整條 AS_PATH 的認證。
- [RFC 854](https://www.rfc-editor.org/rfc/rfc854.html)、[RFC 1350](https://www.rfc-editor.org/rfc/rfc1350.html)：Telnet 與 TFTP；TFTP 初始 UDP 69、後續 TID 及沒有帳號驗證不等於任意讀寫。

## 文字審閱與工程範圍

WRITE-01–04、WRITE-05、WRITE-08 已按本次全文進行文字、來源、雙語及顯示名稱審閱。初次術語補足英文、中文及用途；合成資料與實測分開。原稿未加入圖片或互動，不強制配圖。

網站生成使用既有 sourceBody 契約，兩語各 59 個區塊、九節及一個原生收合答案。這些資料結構與 HTML／A11Y、四種尺寸、200% 文字、鍵盤、無 JavaScript 及正式讀回，均由網站本次實測另行留證；文字審閱不代替工程驗收。

網站維護入口為 [m04_09_content.py](https://github.com/JasonLn0711/kairos-learning/blob/main/scripts/m04_09_content.py)；合併前這是目標連結。依既有發布閘門驗證後再公開，保留 M04-10 待發布及舊課歷史。
