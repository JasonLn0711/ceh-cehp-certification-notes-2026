CEH｜M04-04 SMB 列舉
10/24 午間：一次學一個核心概念

先記住一句：SMB 的共享名稱是檔案分享入口；看得到入口、能列出內容、能讀檔、能修改，要分開確認。

1. SMB 是什麼？

SMB（Server Message Block）是網路檔案分享協定，讓電腦存取另一台伺服器上的檔案。Windows 常用它；Linux 的 Samba 與許多 NAS 也能提供 SMB 服務。

例如合成路徑 \\fileserver\Training\readme.txt：
- fileserver 是伺服器名稱。
- Training 是共享名稱，也就是管理者開放的分享入口。
- readme.txt 是入口下的檔案。

SMB 列舉就是查詢共享名稱、類型與註解；在允許的條件下，也能查看共享內的目錄與檔案資訊。
[Microsoft SMB 概覽](https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview)

2. 從連線到讀檔，經過哪些確認？

先分成四件事：
- 找到服務：直接透過 TCP 傳輸的 SMB 常用 445 埠。埠有回應是入口線索，再由協定回應確認服務。
- 協商通訊方式：雙方協商支援的 SMB 版本與能力。
- 確認使用身分：建立工作階段，依設定完成身分驗證。
- 檢查操作權限：連到指定共享，再依每次請求判斷能否列目錄、讀檔或修改。

「誰在操作」與「允許做什麼」是兩個問題。匿名、Guest 與具名帳號也不是同一種身分，紀錄時要分清楚。
[SMB over TCP](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/direct-hosting-of-smb-over-tcpip)

3. 工具查到的資訊，要怎麼讀？

Windows 可透過相關管理介面查共享；Samba 的 smbclient 則能查詢共享、連線及操作檔案。

例如 smbclient 的 -L 用來查伺服器提供的服務；連進某個共享後，列目錄與下載是另外的操作。取得哪些資訊，仍取決於查詢方式、身分與伺服器設定。
[Samba 官方手冊](https://www.samba.org/samba/docs/current/man-html/smbclient.1.html)

Microsoft 的 NetShareEnum 也能查共享資訊：Level 0 回傳名稱，Level 1 再包含類型與註解。這些層級描述「查哪些欄位」，不代表匿名一定能查詢。
[NetShareEnum](https://learn.microsoft.com/en-us/windows/win32/api/lmshare/nf-lmshare-netshareenum)

4. 用一個合成案例串起來

以下是假想的授權實驗室紀錄，沒有執行真實查詢。使用同一個測試帳號 labuser，目標與操作已事先約定：
- 查共享清單：取得 Training 與 Finance 名稱。
- 列出 Training 目錄：看見 readme.txt。
- 讀取 Training\readme.txt：成功取得合成測試內容。
- 讀取約定的 Finance\test.txt：收到 ACCESS_DENIED。
- 修改、上傳與刪除：本次未測試。

可以這樣記：labuser 查到了兩個共享名稱，並讀取 Training 的指定測試檔。Finance\test.txt 的這次讀取請求遭拒；原因與其他操作權限另行查核。

單一檔案的拒絕回應，只能先描述這次請求，不能直接推論整個共享都不能讀，或所有人都沒有權限。

5. 共享權限與檔案權限，怎麼一起看？

在使用 NTFS 的 Windows 檔案伺服器上，透過網路存取檔案時，要一起檢查：
- 共享權限：分享入口允許哪些網路存取。
- NTFS 權限：檔案系統對特定資料夾或檔案的存取規則。

例如共享入口允許讀取，但指定檔案的有效權限未允許該帳號讀取，這次讀檔仍會受限。群組成員、繼承與拒絕規則也要一起核對。

ACCESS_DENIED 的原因也可能涉及身分驗證或 SMB 安全政策。先確認失敗發生在哪一步，再查完整回應、身分與日誌。
[Microsoft 存取拒絕排查](https://learn.microsoft.com/en-us/troubleshoot/windows-client/networking/access-denied-access-smb-file-share)

ABE（Access-Based Enumeration，依存取權限列舉）可依權限調整共享內檔案與資料夾的顯示。它處理可見性；實際讀寫仍由存取控制判定。
[共享內的列舉設定](https://learn.microsoft.com/en-us/powershell/module/smbshare/set-smbshare?view=windowsserver2025-ps)

6. 防護與證據怎麼做？

限制哪些網路與身分需要使用 SMB，依工作需求設定共享及檔案權限，維護受支援版本與更新，並定期查核異常登入和檔案操作。

傳輸保護也要分清楚：
- SMB Signing（簽署）：協助驗證訊息完整性，偵測傳輸途中遭竄改。
- SMB Encryption（加密）：保護傳輸內容的機密性。

實際是否使用、是否強制，取決於版本、協商結果與有效政策。使用加密連線後，檔案存取仍要通過權限檢查。
[SMB 簽署](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-signing-overview)｜[SMB 加密與安全](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-security)

證據記下時間、目標、身分、共享與完整路徑、操作、協定／保護條件及原始回應。練習只使用授權環境與合成檔案。

小檢核：
你能列出 Finance 共享名稱，但讀取其中約定的 test.txt 時收到 ACCESS_DENIED。請用兩三句話說明：目前確認了什麼？接下來要核對哪些條件，才能說清楚拒絕原因與修改權限？
