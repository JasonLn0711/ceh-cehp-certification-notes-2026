CEH｜M04-07 Unix/Linux 使用者列舉
10/25 午間：一次學一個核心概念

先記住一句：帳號與群組資料告訴我們系統如何辨識身分；能否登入、讀檔或執行管理操作，要各自確認。

1. 使用者列舉在做什麼？

想像公司的員工名冊：你查到某人的名字、員工編號與部門，接著還要看門禁規則，才知道他能進哪些房間。

Unix/Linux 使用者列舉，就是在授權範圍內查詢帳號、使用者編號、群組與相關設定，協助盤點身分及檢查資訊揭露。

帳號也可能供服務程式使用，不一定對應一位真人。本課以已獲准使用的 Linux 練習主機為例；不同 Unix 系統的工具與欄位可能有差異，這項概念也沒有單一固定的網路埠。

2. 先認識帳號、UID 與 GID

• 使用者名稱：人容易辨識的帳號名稱，例如 labuser。
• UID（User ID）：系統辨識使用者的數字編號。
• GID（Group ID）：系統辨識群組的數字編號。
• 主要群組與附加群組：帳號有主要群組，也可能加入其他群組，供權限規則使用。

查到群組成員資格，是判讀權限的線索；實際操作還要對照資源設定，以及執行該操作的程式當時使用的身分。
[Linux 身分與群組](https://man7.org/linux/man-pages/man7/credentials.7.html)

3. 帳號資料存在哪裡？

Linux 的 /etc/passwd 常保存本機帳號資料。每列有七個以冒號分隔的欄位：

名稱:密碼欄位:UID:主要GID:說明:家目錄:登入程式

例如以下合成資料：

labuser:x:1001:1001:Training User:/home/labuser:/bin/bash

這列提供 labuser 的身分編號、主要群組編號、說明、家目錄與登入程式設定。1001 是本例編號，不是所有系統的固定值。

常見的 x 表示密碼資訊另外存放於 shadow 資料中，不是密碼本身。/etc/shadow 包含敏感的密碼及期限資訊，應限制讀取；本課不需要取得或公開它。

/etc/passwd 通常可供一般使用者讀取，讓工具對照名稱與編號；是否有風險，要看透露哪些資訊及其使用情境。
[帳號欄位](https://man7.org/linux/man-pages/man5/passwd.5.html)｜[shadow 說明](https://man7.org/linux/man-pages/man5/shadow.5.html)

4. 用一個合成案例串起來

以下是假想的授權 Linux 實驗室資料，沒有執行真實查詢。管理者已指定測試帳號 labuser 與可查核的檔案。

在主機終端機輸入：

getent passwd labuser

假設取得剛才那列帳號資料。getent 會依系統設定查詢帳號來源；來源可能是本機檔案，也可能包含集中式目錄服務。因此，它與只查看 /etc/passwd 的範圍可能不同。

再查看指定帳號的身分與群組：

id labuser

假設回覆：

uid=1001(labuser) gid=1001(labuser) groups=1001(labuser),3000(project)

這次查詢顯示 labuser 的 UID、主要 GID，以及列出的群組成員資格。

接著在約定條件下，使用測試工作階段讀取 /srv/training/report.txt，卻收到 Permission denied。

可以記成：查到 labuser 的帳號資料與 project 群組資格；指定工作階段對 report.txt 的這次讀取遭拒。接著核對工作階段身分、路徑與權限設定。

有一個實用差別：id labuser 查指定帳號的資訊；不加帳號的 id 顯示目前執行環境的使用者與群組資訊。帳號資料剛更新時，既有工作階段不一定已套用新的群組。
[getent 手冊](https://man7.org/linux/man-pages/man1/getent.1.html)｜[GNU id 手冊](https://man7.org/linux/man-pages/man1/id.1.html)

5. 查詢與權限怎麼一起判讀？

讀取檔案時，除了檔案本身的讀取權限，也要檢查路徑上資料夾的搜尋／通過權限；ACL（存取控制清單）等額外規則也可能影響結果。單看 project 這個群組名稱，還不足以替某個檔案下結論。

帳號資料中的登入程式是設定線索；實際登入還涉及驗證方式、帳號狀態與服務政策。管理操作則另看適用的授權規則。

若查不到某帳號，先保存查詢方式、回覆與當時的資料來源設定。有些來源支援指定帳號查詢，卻不支援完整名單列舉；快取、連線及來源設定也需要查核。
[路徑與權限](https://man7.org/linux/man-pages/man7/path_resolution.7.html)｜[ACL](https://man7.org/linux/man-pages/man5/acl.5.html)｜[帳號來源設定 NSS](https://man7.org/linux/man-pages/man5/nsswitch.conf.5.html)

6. 防護與證據怎麼做？

定期盤點仍需要的使用者與服務帳號，依工作需求配置群組及資源權限；保護 shadow 等敏感資料，讓目錄查詢與登入服務只提供必要資訊，並保留適當的驗證與權限變更紀錄。

證據至少記下時間、主機、查詢身分、指令、帳號來源條件與完整回應。涉及讀檔時，再記工作階段身分、完整路徑、操作及結果；公開教材使用合成名稱，不放真實帳號清單或敏感資料。

小檢核：
id labuser 顯示它屬於 project 群組，但測試工作階段讀取 /srv/training/report.txt 時收到 Permission denied。請用兩三句話說明：目前確認了什麼？接下來應核對哪些身分與權限條件？
