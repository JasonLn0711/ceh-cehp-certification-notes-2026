CEH｜M04-10 LDAP 列舉
10/26 午間：一次學一個核心概念

先記住一句：LDAP 查到的是「這個身分，在這些搜尋條件下看得到的目錄資料」，不等於能修改物件或取得管理權限。

1. LDAP 是什麼？
LDAP（Lightweight Directory Access Protocol，輕量型目錄存取協定）讓程式查詢與操作目錄服務。

目錄像公司的組織通訊錄，依階層整理使用者、群組與資源。它可以用資料庫儲存，但「目錄服務」「底層資料庫」與「LDAP 協定」不是同一件事。Active Directory Domain Services（AD DS）是支援 LDAP 的目錄服務，不是 LDAP 的另一個名字。

LDAP 不只支援讀取，也支援修改；本課只談授權範圍內的唯讀列舉。[OpenLDAP 概覽](https://www.openldap.org/doc/admin26/intro.html)

2. 什麼時候用？
在已授權的帳號盤點、故障排除或安全檢查中，用來確認哪些帳號、群組與組織資訊可見。事前要確認目標、使用帳號、可查範圍及資料保存方式，不是能連上就能任意蒐集。

3. 看懂目錄與搜尋條件
- Entry（項目）：目錄中的一個物件，例如一位使用者。
- Attribute（屬性）：物件的欄位，例如 cn（常用名稱）、mail（電子郵件）。
- DN（辨別名稱）：項目在目錄中的完整名稱，例如 cn=Mei,ou=People,dc=example,dc=test。ou 是組織單位，dc 是網域名稱的組成部分。
- Base DN：搜尋從哪個項目開始，像先指定要查哪個部門。
- Scope（範圍）：base 只查起點；one 只查直接下一層；sub 查起點及其所有下層。
- Filter（篩選條件）：哪些項目符合要求，例如 (cn=Mei)。
- 回傳屬性：找到之後，要取回哪些欄位，不必把所有資料都拿走。

因此，找到某個名稱，不代表已查完整個組織。結果還會受存取權限、數量及時間等限制。[RFC 4511 搜尋規格](https://www.rfc-editor.org/rfc/rfc4511.html#section-4.5)

4. Bind、查詢權限與加密要分開
Bind 用來建立連線的身分／授權狀態，不是「一成功就有全部讀寫權限」。

匿名 Bind 成功，不代表匿名能列出人員；具名帳號認證成功，也不代表可以修改使用者或群組。實際可做什麼，要看存取控制。[RFC 4513](https://www.rfc-editor.org/rfc/rfc4513.html#section-4)

常見的 TCP 389 可以用 StartTLS，在既有 LDAP 連線中啟用 TLS；TCP 636 的 LDAPS 則先建立 TLS，再交換 LDAP 訊息。

所以不能把「389」直接當成未加密，也不能只看到「636」就認定安全。要確認 TLS 確實成功、憑證與伺服器身分驗證正確；使用帳號密碼的 simple bind 不應在缺乏適當保護的連線上傳送。[Microsoft LDAP over TLS 說明](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/enable-ldap-over-ssl-3rd-certification-authority)

5. 一個純合成、唯讀例子
假設你獲准用唯讀帳號查詢實驗室通訊錄：

搜尋起點：ou=People,dc=example,dc=test
範圍：one，只查 People 的直接下一層
條件：(cn=Mei)
要求欄位：cn、mail

假設回傳：
名稱 Mei，電子郵件 mei@example.test。

這只能證明：在這次身分、範圍與條件下，伺服器回傳了這個項目的指定資料。不能因此說已查完所有帳號、能讀密碼，或擁有網域管理權。

即使讀到群組成員關係，也還要確認特定資源的授權規則，不能直接當成實際有效權限。這是紙上例子，沒有連線查詢任何設備。

6. 防護與證據判讀
防護重點是限制不必要的匿名讀取、採最小權限、保護連線與認證資訊，並依需要限制查詢來源及範圍。

紀錄查詢時間、實際身分、Base DN、Scope、Filter、要求欄位、完成狀態與筆數；不要保存密碼或不必要的個資。

要證明匿名資料暴露，應指出「匿名身分實際讀到了哪些資料」，不能只寫 Bind 成功。回傳零筆也不等於資料不存在，可能是範圍、條件、權限或查詢限制的影響。

小檢核：
匿名搜尋回傳零筆結果，為什麼不能直接寫「這個目錄沒有使用者」？請說出兩個還需要確認的因素。

一兩句即可。
