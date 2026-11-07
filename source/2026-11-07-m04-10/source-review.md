# M04-10 來源與逐小節採用查核

查核日期：2026-11-07（Asia/Taipei）。主要問題：如何證明列舉防護同時保留必要服務，限制不應取得的資料與操作，並用對應證據支持結論。

編輯與技術查核依 Kairos Learning 當日 main 的 AGENTS.md、article-standards.md、content-authoring.md、perspectives/authoring.md 及 publishing-security.md。適用 WRITE-01–11、HTML-01–04、A11Y-01–03；圖解依 FIG 規範按教學需要選用，不為滿足圖數而創作測量值。完整正文與中英一致性分開檢查，測試不代表學員已理解。

## 逐節採用

| 原稿章／小節 | 公開正文 | 保留內容與編輯處理 |
| --- | --- | --- |
| 導言 | 導言 | 管理者角度、先定政策再驗收；整合複習不表示前課已學會。 |
| 一、保護什麼 | 1 | 正常查詢用途、資訊／身分／操作三問；Finance 名稱可見與內容可讀分開。 |
| 二、四個關卡 | 2 | 網路可達、身分驗證、授權、傳輸保護；櫃檯比喻及非固定執行順序限制。 |
| 三、入口與來源 | 3 | 盤點、最少功能、網路分段；網路 ACL 與服務權限分層；正反案例、維護與還原、修補驗證及 banner／埠號限制。 |
| 四、最小權限 | 4 | 所需資料／操作、有效群組與繼承、reader 不等於唯讀、匿名與已登入超額權限。 |
| 五、通訊保護 | 5 | 加密、完整性、簽章用途；SMB 傳輸與儲存分開；LDAP simple bind／TLS 及伺服器身分。 |
| 六／DNS | 6 DNS | AXFR 授權與正常查詢／同步各自驗證；拒絕區域傳送不令公開記錄成為秘密。 |
| 六／FTP、SMTP | 6 FTP and SMTP | 匿名必要性、列／讀／寫分開；VRFY／EXPN 與其他郵件資訊線索的限制。 |
| 六／SMB、NFS、NetBIOS、RPC | 6 SMB and NFS, NetBIOS and RPC | 來源／身分／檔案操作；NFSv4.1 版本範圍；名稱與功能授權分開；停用前相依檢查。 |
| 六／SNMP | 6 SNMP | USM authPriv 與 VACM read／write view 分開，v3 不等於全部權限正確。 |
| 六／LDAP、AD | 6 LDAP and Active Directory | 搜尋範圍／屬性／身分、OpenLDAP 規則順序；不同實作預設不互套。 |
| 六／其他服務 | 6 Other services | NTP 校時與管理查詢分開；VPN／語音／IPv6／路由沿政策及證據問題查核。 |
| 七、日誌告警 | 7 | 日誌／告警／阻擋差別、欄位與保存、正常基線、低風險事件驗證、空白日誌及資料最小化。 |
| 八、驗收方法 | 8 | 政策、觀察、交叉證據、結論缺口；允許與拒絕、逾時原因待證、讀取授權不包含寫入。 |
| 九、合成案例 | 9 | 訪客對應拒絕紀錄、lookup-demo 正常欄位與 TLS、privateNote=training-only 超額讀取、修正與重測。 |
| 十、單題檢核 | 10 | 訪客與核准監控都逾時／失敗，缺日誌；修正結論並提出待補證據。三個紙上步驟、預期判讀及無環境變更均保留。 |
| 收尾 | 收尾 | 原創非官方題、參考解答與實際學習分開；下一主題 M05-01；查核日期。公開版不承諾已收到學員回答。 |

格式編輯將 Markdown 粗體章節轉成語意標題；英文自然表達相同條件、來源、案例及限制。兩項技術 review 建議已寫回繁中原稿：網路 ACL 與服務權限分開說明；FTP 操作及 NFSv4.1 ACL 補上直接 RFC 依據。完整英文另做逐節核對。沒有為精簡刪掉協定小節、推理或案例。

## 官方依據與主張範圍

以下來源均於查核日實讀；引用支撐機制，不將合成案例冒稱實測。NIST SP 800-171 的原適用範圍是非聯邦系統 CUI 保護，本課只引用防護概念，不推論讀者具有該合規義務。

- [NIST SP 800-171 Rev. 3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/800-171r3/NIST.SP.800-171r3.html)：03.04.06 最少功能；03.03.02–03.03.03 稽核內容及分析。
- [NIST least privilege](https://csrc.nist.gov/glossary/term/least_privilege)：完成指定工作所需的最低權限。
- [NIST SP 800-40 Rev. 4](https://csrc.nist.gov/pubs/sp/800/40/r4/final)：修補識別、優先排序、取得、安裝與驗證。
- [Microsoft SMB traffic](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic)：依網路邊界限制 SMB；例外需配合現況。
- [Microsoft access control](https://learn.microsoft.com/en-us/windows/security/identity-protection/access-control/access-control)：身分、資源、群組與有效權限。
- [Microsoft SMB security](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-security)：簽章與加密功能，不等同磁碟加密。
- [RFC 4513 §5.1.3](https://www.rfc-editor.org/rfc/rfc4513.html#section-5.1.3)：LDAP name/password simple bind 所需機密性保護。
- [RFC 5936 §5](https://www.rfc-editor.org/rfc/rfc5936.html#section-5)：AXFR 授權。
- [RFC 959 §4.1.3](https://www.rfc-editor.org/rfc/rfc959.html#section-4.1.3)：FTP 檔案服務的不同命令與操作。
- [RFC 5321 §7.3](https://www.rfc-editor.org/rfc/rfc5321.html#section-7.3)：VRFY／EXPN 揭露與限制的範圍。
- [RFC 8881 §6](https://www.rfc-editor.org/rfc/rfc8881.html#section-6)：NFSv4.1 檔案存取控制屬性，不能推廣到所有 NFS 版本。
- [RFC 3414 §1.3](https://www.rfc-editor.org/rfc/rfc3414.html#section-1.3)：USM 安全服務；本課未建議使用其中歷史密碼演算法。
- [RFC 3415 §2.5](https://www.rfc-editor.org/rfc/rfc3415.html#section-2.5)：VACM 可讀／可寫檢視範圍。
- [OpenLDAP 2.6 Access Control](https://www.openldap.org/doc/admin26/access-control.html)：項目、屬性、要求者與規則順序；沒有規則不等於一律拒絕，不套用到 AD 預設。
- [RFC 8633 §3.4](https://www.rfc-editor.org/rfc/rfc8633.html#section-3.4)：NTP 控制面查詢限制，與核准校時分別驗證。

初次內容 review 通過，未發現阻擋性技術問題。網站呈現、四寬度、200% 文字、鍵盤、無 JavaScript 及正式頁是否通過，依本次網站回執逐項記錄；本文來源查核不代替那些驗收。
