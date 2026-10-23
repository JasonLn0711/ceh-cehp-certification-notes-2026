# M06 系統入侵原理｜逐概念閱讀路線

依[現行閱讀規則](../../study-plan/concept-reading-2026-10-22.md)與[三章總規劃](../../study-plan/m05-m07-concept-plan-2026-10-23.md)，本章 17 核心、4 選讀，沿用附件順序。全部狀態為**已規劃**，尚未交付本路線教材。每次一概念、一例子、一個小檢核；本人回答與 Q&A 另記。

2026-10-23 查核：[CEH AI 官方課程](https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/)列 23 個 Key Topics；[Blueprint v5.0](https://cert.eccouncil.org/wp-content/uploads/2024/04/CEH-Exam-Blueprint-v5.pdf)第 3 頁有 10 個大分類、6 題；6/125＝4.8%。本章核心數是教學拆分，與上述數字各自獨立。

## 核心目錄

- [M06-01 System Hacking Concepts 系統入侵原理](#m06-01)
- [M06-02 Authentication, Authorization & Privileges 身分驗證與權限模型](#m06-02)
- [M06-03 Online Password Attacks 線上密碼攻擊](#m06-03)
- [M06-04 Password Hashing & Offline Cracking 密碼儲存與離線破解](#m06-04)
- [M06-05 Gaining Access 取得系統存取權](#m06-05)
- [M06-06 Vulnerability Exploitation & Metasploit 漏洞利用與框架](#m06-06)
- [M06-07 Executing Applications 應用程式與程序執行](#m06-07)
- [M06-08 Windows Privilege Escalation Windows 權限提升](#m06-08)
- [M06-09 Linux Privilege Escalation Linux 權限提升](#m06-09)
- [M06-10 Active Directory Security AD 列舉與權限關係](#m06-10)
- [M06-11 Windows/Linux Post Exploitation 存取後活動分析](#m06-11)
- [M06-12 Maintaining Access 維持存取](#m06-12)
- [M06-13 Establishing Persistence 建立持續性機制](#m06-13)
- [M06-14 Hiding Files & Steganography 檔案隱藏與資訊隱寫](#m06-14)
- [M06-15 Covering Tracks & Clearing Logs 痕跡處理與日誌](#m06-15)
- [M06-16 Buffer Overflow & Memory Safety 緩衝區溢位](#m06-16)
- [M06-17 System Hacking Countermeasures 防禦與驗證](#m06-17)

<a id="m06-01"></a>
### M06-01｜System Hacking Concepts 系統入侵原理

- 狀態：已規劃；教材、作答、Q&A與理解確認各自待證據。
- 為何必學：建立全章流程，理解取得存取權、提權、執行與維持存取之間的關係。
- 先修：M05-14（概念銜接，不宣稱已學會）。
- 學習成果：區分存取、執行、提權與持續性。
- 具體示例方向：合成工作階段狀態圖。
- 防護／證據：依各階段證據判定能力。
- 小檢核：登入成功能確認什麼？

<a id="m06-02"></a>
### M06-02｜Authentication, Authorization & Privileges 身分驗證與權限模型

- 狀態：已規劃；教材、作答、Q&A與理解確認各自待證據。
- 為何必學：所有帳號攻擊、權限提升與程序執行的共同基礎；必須理解使用者、群組、權限與安全邊界。
- 先修：M06-01（概念銜接，不宣稱已學會）。
- 學習成果：區分身分、程序安全脈絡與授權。
- 具體示例方向：一般帳號與服務帳號比較。
- 防護／證據：最小權限與存取檢查。
- 小檢核：同帳號不同程序脈絡可能差在哪？

<a id="m06-03"></a>
### M06-03｜Online Password Attacks 線上密碼攻擊

- 狀態：已規劃；教材、作答、Q&A與理解確認各自待證據。
- 為何必學：辨識 Brute Force、Dictionary Attack、Password Spraying 與 Credential Stuffing，理解偵測和防護。
- 先修：M06-02（概念銜接，不宣稱已學會）。
- 學習成果：辨識四類線上密碼嘗試。
- 具體示例方向：合成登入事件分布。
- 防護／證據：MFA、速率限制與帳號監控。
- 小檢核：噴灑與撞庫的資料來源有何差異？

<a id="m06-04"></a>
### M06-04｜Password Hashing & Offline Cracking 密碼儲存與離線破解

- 狀態：已規劃；教材、作答、Q&A與理解確認各自待證據。
- 為何必學：理解 Hash、Salt、KDF、SAM、`/etc/shadow`、NTLM 等基礎，避免把 Hash 與加密混為一談。
- 先修：M06-02（概念銜接，不宣稱已學會）。
- 學習成果：說明Hash、Salt、KDF與離線驗證。
- 具體示例方向：合成密碼儲存示意，不用真憑證。
- 防護／證據：安全KDF與憑證保管。
- 小檢核：雜湊為何不是解密還原？

<a id="m06-05"></a>
### M06-05｜Gaining Access 取得系統存取權

- 狀態：已規劃；教材、作答、Q&A與理解確認各自待證據。
- 為何必學：區分透過有效憑證、錯誤設定與漏洞取得存取權，以及各種存取層級。
- 先修：M06-02,M06-04（概念銜接，不宣稱已學會）。
- 學習成果：分辨憑證、配置與漏洞造成的存取。
- 具體示例方向：三張匿名存取事件卡。
- 防護／證據：驗證狀態與可操作資源分別記錄。
- 小檢核：取得帳號存取還有哪些限制？

<a id="m06-06"></a>
### M06-06｜Vulnerability Exploitation & Metasploit 漏洞利用與框架

- 狀態：已規劃；教材、作答、Q&A與理解確認各自待證據。
- 為何必學：銜接 M05，理解 Exploit、Payload、Session 與漏洞成立條件，不把掃描結果當成利用成功。
- 先修：M05-11,M06-05（概念銜接，不宣稱已學會）。
- 學習成果：區分Exploit、Payload與Session。
- 具體示例方向：預製模擬框架報告。
- 防護／證據：查成立條件與操作證據。
- 小檢核：掃描Finding與成功Session差在哪？

<a id="m06-07"></a>
### M06-07｜Executing Applications 應用程式與程序執行

- 狀態：已規劃；教材、作答、Q&A與理解確認各自待證據。
- 為何必學：了解 Process、Thread、Shell、父子程序及執行身分，區分程式執行成功與取得高權限。
- 先修：M06-02,M06-05（概念銜接，不宣稱已學會）。
- 學習成果：解釋程序、執行緒、Shell與父子關係。
- 具體示例方向：良性程式程序樹。
- 防護／證據：記PID、身分與啟動來源。
- 小檢核：程式執行成功表示哪些權限？

<a id="m06-08"></a>
### M06-08｜Windows Privilege Escalation Windows 權限提升

- 狀態：已規劃；教材、作答、Q&A與理解確認各自待證據。
- 為何必學：理解 Access Token、SID、ACL、UAC、服務帳號及 SYSTEM 權限，是 Windows 安全的核心。
- 先修：M06-02,M06-07（概念銜接，不宣稱已學會）。
- 學習成果：閱讀Token、SID、ACL與UAC邊界。
- 具體示例方向：合成Windows權限表。
- 防護／證據：檢查服務帳號與授權變更。
- 小檢核：本機管理員與網域管理員差在哪？

<a id="m06-09"></a>
### M06-09｜Linux Privilege Escalation Linux 權限提升

- 狀態：已規劃；教材、作答、Q&A與理解確認各自待證據。
- 為何必學：理解 UID/GID、sudo、SUID/SGID、Capabilities 與檔案權限，建立 Linux 權限管理能力。
- 先修：M06-02,M06-07（概念銜接，不宣稱已學會）。
- 學習成果：閱讀UID/GID、sudo與Capabilities。
- 具體示例方向：合成Linux權限清單。
- 防護／證據：最小權限與檔案設定稽核。
- 小檢核：SUID與sudo應分別查哪些條件？

<a id="m06-10"></a>
### M06-10｜Active Directory Security AD 列舉與權限關係

- 狀態：已規劃；教材、作答、Q&A與理解確認各自待證據。
- 為何必學：理解網域帳號、群組、服務身分、Kerberos 及權限委派，銜接企業內網安全。
- 先修：M04-10,M06-02,M06-08（概念銜接，不宣稱已學會）。
- 學習成果：說明網域群組、Kerberos與委派。
- 具體示例方向：虛構AD權限關係圖。
- 防護／證據：查服務身分與委派證據。
- 小檢核：群組成員如何影響可用資源？

<a id="m06-11"></a>
### M06-11｜Windows/Linux Post Exploitation 存取後活動分析

- 狀態：已規劃；教材、作答、Q&A與理解確認各自待證據。
- 為何必學：學會判斷一個已取得存取權的工作階段，實際上能讀取、修改或操作哪些資源。
- 先修：M06-05,M06-08,M06-09（概念銜接，不宣稱已學會）。
- 學習成果：限定工作階段實際可用能力。
- 具體示例方向：同Session不同資源存取表。
- 防護／證據：逐操作保存回應，不推定全權。
- 小檢核：一個讀取成功可推論多大範圍？

<a id="m06-12"></a>
### M06-12｜Maintaining Access 維持存取

- 狀態：已規劃；教材、作答、Q&A與理解確認各自待證據。
- 為何必學：理解既有 Session、遠端連線與有效憑證可能如何支持持續操作，並認識其限制。
- 先修：M06-11（概念銜接，不宣稱已學會）。
- 學習成果：區分延續Session與後續恢復能力。
- 具體示例方向：合成連線中斷時間軸。
- 防護／證據：憑證有效期與連線紀錄。
- 小檢核：連線保持和持續性機制差在哪？

<a id="m06-13"></a>
### M06-13｜Establishing Persistence 建立持續性機制

- 狀態：已規劃；教材、作答、Q&A與理解確認各自待證據。
- 為何必學：理解重新開機或連線中斷後如何仍可能恢復執行，以及 Startup、Scheduled Tasks、Services 等機制的風險。
- 先修：M06-07,M06-12（概念銜接，不宣稱已學會）。
- 學習成果：說明自動啟動條件與執行身分。
- 具體示例方向：預製排程任務與服務設定。
- 防護／證據：比對基線、變更及管理許可。
- 小檢核：合法排程何時值得調查？

<a id="m06-14"></a>
### M06-14｜Hiding Files & Steganography 檔案隱藏與資訊隱寫

- 狀態：已規劃；教材、作答、Q&A與理解確認各自待證據。
- 為何必學：區分 Hidden File、NTFS Alternate Data Streams、Steganography 與加密，理解不同隱匿方式。
- 先修：M06-07（概念銜接，不宣稱已學會）。
- 學習成果：區分隱藏、ADS、隱寫與加密。
- 具體示例方向：良性檔案屬性與示意圖。
- 防護／證據：檔案盤點、雜湊與格式檢查。
- 小檢核：隱藏檔案與加密保護哪一層？

<a id="m06-15"></a>
### M06-15｜Covering Tracks & Clearing Logs 痕跡處理與日誌

- 狀態：已規劃；教材、作答、Q&A與理解確認各自待證據。
- 為何必學：認識攻擊活動留下的事件、日誌與檔案跡證，理解日誌遭竄改或清除的風險及偵測方法。
- 先修：M06-07,M06-14（概念銜接，不宣稱已學會）。
- 學習成果：理解日誌清除與其他跡證。
- 具體示例方向：預製1102事件與遠端日誌。
- 防護／證據：集中保管、完整性與調查，不清真日誌。
- 小檢核：本機日誌清除後還有哪些證據？

<a id="m06-16"></a>
### M06-16｜Buffer Overflow & Memory Safety 緩衝區溢位

- 狀態：已規劃；教材、作答、Q&A與理解確認各自待證據。
- 為何必學：理解記憶體、Stack、Heap、越界寫入與程式控制流程，是深入理解漏洞利用技術的基礎。
- 先修：M06-07（概念銜接，不宣稱已學會）。
- 學習成果：解釋Stack/Heap越界與控制流程。
- 具體示例方向：紙上記憶體界線圖。
- 防護／證據：ASLR、DEP/NX與Canary各司其職。
- 小檢核：越界寫入與成功利用之間缺什麼？

<a id="m06-17"></a>
### M06-17｜System Hacking Countermeasures 防禦與驗證

- 狀態：已規劃；教材、作答、Q&A與理解確認各自待證據。
- 為何必學：將前面各項技術對應到最小權限、MFA、更新、EDR、日誌保護與事件調查。
- 先修：M06-08,M06-09,M06-13,M06-15,M06-16（概念銜接，不宣稱已學會）。
- 學習成果：把身分、修補與監控整合驗證。
- 具體示例方向：合成系統防護檢查表。
- 防護／證據：MFA、最小權限、EDR及複驗。
- 小檢核：如何證明一項防護真的生效？

## 選讀延伸（不自動插入核心交付佇列）

| ID | 主題 | 為何選讀／第一輪方向 | 狀態 |
| --- | --- | --- | --- |
| M06-E01 | Pass-the-Hash / Pass-the-Ticket | 理解為什麼某些驗證材料即使不是明文密碼，也可能被濫用來驗證身分。 | 已規劃・選讀 |
| M06-E02 | Keylogger、Spyware、Rootkit | 區分鍵盤輸入擷取、間諜活動與深層隱匿技術；掌握偵測觀念。 | 已規劃・選讀 |
| M06-E03 | Steganalysis & Detection Tools | 理解隱寫分析、影像或音訊異常，以及為何不存在通用且完全可靠的偵測方法。 | 已規劃・選讀 |
| M06-E04 | AI-Powered Vulnerability Exploitation | 理解 AI 如何輔助技術分析及腳本審查，並辨識錯誤生成、越權與不可信輸出的問題。 | 已規劃・選讀 |

選讀依本人指定再安排；附件中較強的「不能跳過」措辭保留在私人原文，本路線採核心優先與選讀分離。測驗題是教材，不是本人作答或實際Q&A。所有示例採合成資料、良性程式或預製紀錄，實作另確認隔離環境與授權。

[主規劃](../../study-plan/m05-m07-concept-plan-2026-10-23.md) · [M04前章](../m04-enumeration/reading-route.md) · [公開章節索引](https://learn.cs-kairos.com/courses/ceh/v13/m06/#one-concept)
