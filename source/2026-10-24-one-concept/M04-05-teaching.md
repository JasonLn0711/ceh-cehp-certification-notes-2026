CEH｜M04-05 NetBIOS 列舉
10/24 晚間：一次學一個核心概念

先記住一句：NetBIOS 名稱表提供電腦名稱與服務用途的線索；共享內容和檔案權限，要另外查核。

1. NetBIOS 是什麼？

想像公司裡有一份內部分機表，記著各部門的名稱與用途。找到「財務部」之後，進門、閱讀文件仍各有規則。

NetBIOS（Network Basic Input/Output System）原本是一套讓區域網路程式使用名稱、交換資料的介面。把這些功能放到 TCP/IP 網路上運作，稱為 NetBIOS over TCP/IP，常簡稱 NBT 或 NetBT。

NetBIOS 列舉就是查詢這類名稱與狀態資訊，協助盤點舊系統、辨識服務線索，以及檢查資訊開放的範圍。
[NetBIOS 運作概念](https://www.rfc-editor.org/rfc/rfc1001)

2. 137、138、139，分別做什麼？

- 名稱服務：137 埠。處理名稱註冊與查詢，常見 UDP，也有 TCP。
- 資料報服務：UDP 138。傳送不必先建立工作階段的訊息。
- 工作階段服務：TCP 139。建立連線，供程式持續交換資料；傳統 SMB 可透過它運作。

接回上一課：直接透過 TCP 的 SMB 使用 445，可以不依賴 NetBIOS。因此，NetBIOS 查詢沒有回應時，SMB 是否可用仍要另外確認。
[Microsoft：NetBIOS 與直接 SMB 傳輸](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/direct-hosting-of-smb-over-tcpip)

3. 名稱是怎麼找到的？

NetBIOS 名稱解析，就是把名稱對應到網路位址。依設定，電腦可能透過區域網路廣播，或向集中管理名稱的伺服器查詢；Windows 的 WINS 就是這類名稱服務。

它與 DNS 使用不同的名稱系統。兩邊顯示的電腦名稱可能相似，查詢方式與紀錄仍要分開確認。

Windows 的名稱顯示還常帶有十六進位尾碼，例如 <00> 或 <20>，表示該名稱的用途。判讀時要一起看：
- 名稱：例如 LAB-FS。
- 尾碼：例如 <20>。
- 類型：例如 UNIQUE 或 GROUP。

UNIQUE 表示唯一名稱，GROUP 表示群組名稱。這裡的群組是 NetBIOS 名稱類型，與檔案權限群組要分開理解。
[Microsoft 名稱與尾碼說明](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-nbte/6dbf0972-bb15-4f29-afeb-baaae98416ed)

4. 用一個合成案例讀名稱表

以下是假想的授權實驗室資料，這裡沒有執行真實查詢。

Windows 的 nbtstat 可以查看 NetBIOS 名稱表。在已取得許可的練習環境，可於命令提示字元輸入：

nbtstat /A 192.0.2.10

/A 是依 IP 查遠端名稱表；小寫 /a 是依遠端名稱查詢，參數大小寫有差別。192.0.2.10 是文件示範位址，實作時替換成約定的實驗主機。
[nbtstat 官方說明](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nbtstat)｜[文件示範位址](https://www.rfc-editor.org/rfc/rfc5737)

假設回應有以下三筆：
- LAB-FS <00> UNIQUE：電腦名稱線索，對應工作站服務使用的名稱。
- LAB-FS <20> UNIQUE：伺服器服務註冊的名稱，可作為檔案分享服務的查核線索。
- LABGROUP <00> GROUP：機器群組名稱線索；實際工作群組或網域設定，再與管理端資料核對。
[Microsoft 尾碼定義](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-brws/0c773bdd-78e2-4d8b-8b3d-b7506849847b)

目前取得的是名稱與用途線索。共享名稱、登入條件、指定檔案的讀寫結果，接著沿用 SMB 那一課的方法，依授權範圍分別確認。

另外，nbtstat /n 看本機名稱表，/c 看本機名稱快取；這兩者與當次遠端查詢回應，應分開記錄。

5. 查不到，或查到了，要怎麼記？

查詢逾時時，先記「這次查詢在等待期間未收到回覆」。可能原因包括服務未啟用、防火牆阻擋、網路路徑或目標狀態，再用其他證據定位。

取得上述名稱表時，可以寫：
在約定的網路位置，向指定實驗主機查詢 NetBIOS 名稱表，取得 LAB-FS 的 <00>、<20> 與 LABGROUP 的群組名稱紀錄。共享與檔案操作留待另行驗證。

保存時間、來源網路位置、目標、工具與參數、完整回應。名稱表可以和資產清冊、服務設定交叉核對；產品版本、漏洞與實際存取權限，各自需要對應證據。

6. 防護從實際用途出發

先確認哪些舊設備或應用還依賴 NetBIOS，再安排調整：
- 仍有需要的系統：限制可連線的網路與來源。
- 已無依賴的系統：經相容性測試後停用 NetBIOS over TCP/IP。
- 邊界防火牆：讓名稱服務與檔案分享只對預期範圍開放。
- 異常查詢：搭配資產設定與日誌查核。

停用 NetBIOS 後，直接透過 TCP 445 的 SMB 仍可能運作；它的網路存取、身分驗證、共享與檔案權限，繼續各自管理。

小檢核：
你查到 LAB-FS <20> UNIQUE，同事說：「這表示我們已經可以讀取它的共享檔案。」

請用兩三句話說明：目前取得了什麼線索？接下來需要哪些查核，才能確認指定檔案的讀取權限？
