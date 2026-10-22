請重新規劃我們的 CEH 閱讀規劃，以下方這個版本為主，以後一次我們就讀一個重要概念，把任務變小，比較容易一個接一個實踐：
"""
# CEH M04｜官方考試範圍、必學概念與最佳學習順序

結論：我建議將 M04 拆成 19 個基礎知識單元，其中 12 個列為核心必學，另外 7 個達到能辨識、解釋與判斷風險的程度即可。

學習順序不應完全依照官方教材排列，而應考量三個因素：實務重要性、理解難度，以及概念之間的先修關係。

## 一、先確認 EC-Council 官方考試範圍

我查核了 EC-Council 官方發布的 [CEH Exam Blueprint v5.0](https://cert.eccouncil.org/wp-content/uploads/2024/04/CEH-Exam-Blueprint-v5.pdf?utm_source=chatgpt.com)，以及目前公開的 CEH 課程綱要。

官方考試藍圖

# v5.0

Enumeration 題數

# 7 題

知識考試總題數

# 125 題

官方藍圖將 Enumeration 歸在 Domain 2：Reconnaissance Techniques。該 Domain 包括 M02、M03 與 M04，合計占 17%。

來源：EC-Council Exam Blueprint v5.0，第 2 頁；CEH 官方考試介紹。

[image](https://www.google.com/s2/favicons?domain=https://cert.eccouncil.org\&sz=32)

cert.eccouncil.org

+1



這裡需要修正上一則回答：先前提到的 6 題是舊版 v4.0 藍圖。目前查到的較新官方 v5.0 藍圖列為 7 題，約占整份 125 題考試的 5.6%。但這不代表每個技術各有固定題數，也不能據此推算各技術的出題機率。

官方考試藍圖列出 8 組大範圍；我將當中合併的協定拆開，得到 19 個便於學習的單元。另一方面，官方課程頁面列出 16 個 Key Topics，另外包含 AI 輔助列舉及 DNS 技術細節。這兩份文件用途不同，不應將 16 或 19 誤認成官方規定的考題數量。

[image](https://www.google.com/s2/favicons?domain=https://cert.eccouncil.org\&sz=32)

cert.eccouncil.org

+1



## 二、我如何判定哪些概念「必學」？

我的排序不是猜測哪個協定最常出題，而是採用以下決策模型。

學習優先級評估模型（我的教學判斷，非官方權重）

資安實務與後續課程的重要性

40%

能否支援 AD 安全、滲透測試、系統防禦及 M05/M06

官方課程與實驗的直接涵蓋程度

30%

是否明列於考試藍圖，以及官方實作項目

先修依賴與概念可遷移性

20%

是否能幫助理解其他多個技術

學習成本與短期成果

10%

是否能快速建立正確觀念並完成練習

一個重要的判準是：官方 M04 實作練習明確涵蓋 NetBIOS、SNMP、LDAP、NFS、DNS、SMTP、RPC、SMB、FTP。 這九項自然應列為核心。再加上列舉原理、Unix/Linux User Enumeration，以及防禦措施，就得到我建議的 12 個必學單元。

[image](https://www.google.com/s2/favicons?domain=https://www.eccouncil.org\&sz=32)

EC-Council



重要性高，不代表一定要最先學。例如 LDAP 對企業資安極為重要，但必須先理解帳號、群組、目錄結構和基本網路協定。因此我會把它排在基礎協定之後。

## 三、12 個核心必學概念：依建議學習順序排列

難度 1＝初學者容易理解；5＝需要較完整的網路、作業系統或身分管理基礎。重要性是相對實務價值，不是官方出題機率。

| 順序 | 重要概念                        | 重要性 | 難度  | 為什麼必學？                                                           |
| -- | --------------------------- | --- | --- | ---------------------------------------------------------------- |
| 1  | Enumeration Concepts 列舉原理   | 5/5 | 1/5 | 整章共同基礎。必須區分 Reconnaissance、Scanning、Enumeration，以及列舉與真正取得存取權的差異。 |
| 2  | DNS Enumeration DNS 列舉      | 5/5 | 2/5 | DNS 是網路核心服務。能透過 DNS 記錄理解主機、名稱服務、郵件與部分網路配置資訊。                     |
| 3  | FTP Enumeration             | 4/5 | 1/5 | 原理簡單，適合第一個服務列舉實驗；可理解匿名存取、伺服器回應及檔案權限。                             |
| 4  | SMB Enumeration             | 5/5 | 3/5 | Windows 網路常見的檔案共享與存取機制。共享名稱、帳號權限及存取控制都涉及重要安全問題。                  |
| 5  | NetBIOS Enumeration         | 4/5 | 2/5 | 幫助理解 Windows 傳統名稱解析及舊式 SMB 傳輸，並辨識歷史系統中的資訊揭露問題。                   |
| 6  | SMTP Enumeration            | 4/5 | 2/5 | 認識郵件伺服器如何處理收件者及相關查詢，以及帳號資訊可能洩漏的條件。                               |
| 7  | Unix/Linux User Enumeration | 4/5 | 2/5 | 理解 Linux 使用者、群組、UID/GID、帳號權限，是後續 Linux 安全與權限提升的重要基礎。             |
| 8  | NFS Enumeration             | 4/5 | 3/5 | 理解 Unix/Linux 網路檔案共享、Export、掛載與權限設定，與 SMB 形成跨平台對照。               |
| 9  | SNMP Enumeration            | 5/5 | 3/5 | 網路交換器、路由器與監控設備常涉及 SNMP；錯誤的管理設定可能揭露系統與網路資訊。                       |
| 10 | LDAP Enumeration            | 5/5 | 4/5 | 理解 Active Directory 目錄、使用者、群組、組織單位及存取控制，是企業身分安全的關鍵。              |
| 11 | RPC Enumeration             | 4/5 | 4/5 | 了解 Windows 遠端程序呼叫、服務介面與端點，有助於理解企業內網服務間如何互相運作。                    |
| 12 | Enumeration Countermeasures | 5/5 | 3/5 | 必須能將取得的資訊轉換成資安風險判斷，並提出權限限制、強化設定與偵測方法。                            |

這個順序有三個刻意安排：

第一，先學看得見結果的服務。 DNS 和 FTP 能讓初學者較快理解「一個服務如何回傳資訊」。

第二，將關聯性高的系統放在一起。 SMB 與 NetBIOS 連續學；Linux 帳號與 NFS 連續學；LDAP 與 RPC 放在後段，建立對企業系統的理解。

第三，防禦貫穿全程。 雖然第 12 項才做完整的防禦整合，但前面每一個協定都會同步討論對應防護措施。

### 核心單元中特別值得學深的四個

[Attacking Common Services Course | HTB Academy](https://images.openai.com/static-rsc-4/82z1mvoT91NdW17dM4fABRqE-i0bdSE796mjn4qVPhrpJ3Q80TECBYETVxYDWBcQSF9-yqDiCL20iBW9Z5i4nluwLqLCcdpJ9AWaujURts6XEsbVV6O2AKjvOink7myBQ0WVHFOUmlk4GcsN2drqRyt0NZDCIYKVWeq7g7tFl98?purpose=inline)

SMB + NetBIOS：Windows 網路基礎

學習重點包括 TCP 445、傳統 NetBIOS 137–139、共享資源、驗證與授權。現代 SMB 可以直接使用 TCP 445，不必依賴 NetBIOS。這個區別對判讀掃描結果很重要。

[image](https://www.google.com/s2/favicons?domain=https://learn.microsoft.com\&sz=32)

Microsoft Learn



[Active Directory (AD) est un service d'annuaire développé par Microsoft pour les réseaux de domaines Windows.  Il est utilisé pour gérer et organiser les ordinateurs, les utilisateurs et les… | Zied Zekri | 18 commentaires](https://images.openai.com/static-rsc-4/oLXfvTXlPCoI1qVhpwcaKMkJ8RO8cgohhwHsvEPvaYNADII-4TsVwkIORhE0bOp8TF95VY0WBEMeB7I0EGSgmrLZCg9onqaDXU-tlNpWgy2hJlzx_0O_cvzgZJGwkmRhXv6PiQKYRESuOYHgng2ddvFBinlRHTl__4NPH8-mK0s?purpose=inline)

LDAP：企業身分與目錄的核心

需要理解 Directory、Distinguished Name（DN）、Object、Attribute、Group Membership，以及 LDAP 查詢結果如何受到帳號權限限制。這些知識將銜接 AD 安全與 M06。

[Enterprise Network Rack Components: Router, Firewall, Switch, Patch Panel, Servers, UPS, PDU | Ayoub Elkhattabi posted on the topic | LinkedIn](https://images.openai.com/static-rsc-4/9b7B1_KTaRac8fgMPtRLNXK_jpifKBrDPljYlXKawUjBVbbA7I9k6Axg6Gdr6DUsLDChoxWz_X9bqwkH9iQJY9GoKandBI4ZSy3h--vuU6fsaQvpMPqOtu2XnSMe91lQjBSCC9uhAlgpQGg3sA1q4WKNuzElFPqvd7qZE4ltO74?purpose=inline)

SNMP：網路設備管理與資訊揭露

必學 MIB、OID、Community String，以及 SNMPv1/v2c 與 v3 的安全差異。尤其要知道 SNMPv3 也必須正確設定驗證與加密，不能認為使用 v3 就自動安全。

[image](https://www.google.com/s2/favicons?domain=https://www.cisco.com\&sz=32)

Cisco



[A Beginners Guide to DNS Resolution](https://images.openai.com/static-rsc-4/BKo9rjXj1A_C5Mam0YMJcjU47Cb617Cqg6RjuwXZh6UgX9YYr2tnWMb06PiMKg2pEcaOm5yAbz_uoCV2wEsJjdIT_8KO9JJ9xyP9ZiRpEqOl1_XIPWvc4YSr--0Oe3bnMjsAO8aBzVsRWT2oUfeHC7peDa_1nEsyThhKb7VPU0k?purpose=inline)

DNS：最容易延伸至其他資安領域

除了 A、AAAA、MX、NS、PTR、TXT 記錄，還要理解 Zone Transfer（AXFR）、DNS Cache Snooping 與 DNSSEC Zone Walking。注意 DNSSEC 用來驗證 DNS 資料完整性，不負責隱藏 DNS 資料。

[image](https://www.google.com/s2/favicons?domain=https://www.isc.org\&sz=32)

ISC



## 四、另外 7 個官方範圍：掌握辨識與風險判斷即可

這七項仍在官方考試藍圖中，不建議完全跳過。只是相較前面 12 項，在第一輪學習時不需要每項都做深度實驗。

| 順序 | 概念                 | 難度  | 第一輪至少要懂                                              |
| -- | ------------------ | --- | ---------------------------------------------------- |
| 13 | Telnet Enumeration | 1/5 | TCP 23、明文遠端登入、服務資訊揭露與 SSH 的差異                        |
| 14 | TFTP Enumeration   | 1/5 | UDP 69、簡單檔案傳輸、缺乏內建登入驗證的設計及其風險                        |
| 15 | NTP Enumeration    | 2/5 | UDP 123、時間同步服務、版本與對等資訊可能揭露的情況                        |
| 16 | IPv6 Enumeration   | 3/5 | IPv6 位址、ICMPv6、Neighbor Discovery，以及與 IPv4 不同的主機發現方式 |
| 17 | VoIP Enumeration   | 3/5 | SIP、分機資訊、VoIP 系統與其帳號及服務資訊                            |
| 18 | IPsec Enumeration  | 4/5 | IKE、VPN 協商、UDP 500/4500、可能揭露的 VPN 設定資訊               |
| 19 | BGP Enumeration    | 5/5 | TCP 179、AS、路由宣告、BGP Peer 及路由基礎概念                     |

這裡要強調：難度 5/5 的 BGP 不代表它對網路安全不重要，而是深入理解它需要較完整的路由協定知識。就 M04 第一輪備考而言，優先學習 BGP 的角色、主要名詞和資訊揭露風險，比深入研究其完整路由機制更有效率。

至於官方課程另外提到的 Enumeration using AI，我建議當成第 20 個實作延伸：利用 AI 協助解讀與分類列舉結果、整理風險，並要求它提供能人工驗證的依據。它出現在官方課程與實驗列表，但沒有在 v5.0 考試藍圖中獨立列為一個考點，因此不應假設它有固定題數。

[image](https://www.google.com/s2/favicons?domain=https://www.eccouncil.org\&sz=32)

EC-Council



## 五、我設計的六堂 M04 學習路線

這個安排的核心是：先學協定與主機，再學資源和身分，最後把結果轉成安全風險與防護決策。

建議學習路線

核心約 10–12 小時，依實驗熟練度調整

1

列舉的原理與容易理解的服務

1.5 小時

Enumeration、DNS、FTP

能從開放服務與實際回應，區分服務存在、資訊揭露、授權存取三種不同事實

2

Windows 與電子郵件服務

2 小時

SMB、NetBIOS、SMTP

了解共享資源、Windows 傳統網路資訊與郵件帳號列舉

3

Linux 帳號與檔案共享

1.5 小時

Unix/Linux Users、NFS

能解釋帳號、群組、檔案權限，以及匯出共享設定

4

網路設備管理

1.5 小時

SNMP、MIB、OID、SNMPv3

知道為什麼管理服務可能揭露系統配置，以及如何降低風險

5

企業目錄與遠端服務

2.5 小時

LDAP、Active Directory、RPC

能閱讀目錄結構、理解群組及服務介面，區分身分驗證與授權

6

其他技術、防禦與整合測驗

2–3 小時

Telnet、TFTP、NTP、IPv6、VoIP、IPsec、BGP、Countermeasures

完成其餘官方範圍，並整理一份包含證據、風險與改善措施的練習報告

這六堂採取「先完成核心概念，再廣泛覆蓋其餘考點」的策略。課堂時間為教學估計，並非官方規定時數。

## 六、如何確認真的學會 M04？

學習這一章，不應只要求背出協定和 Port Number。

每一個必學主題都要通過以下五項檢核：

自我檢核進度

0/5

解釋協定的正常用途與運作原理

辨識常用連接埠、服務及列舉工具

解釋能取得哪些資訊，以及必須具備什麼存取條件

區分資訊揭露、配置弱點、實際可利用的漏洞

提出至少一項具體防護措施及其驗證方法

例如：掃描結果顯示 TCP 445 開啟，你只能先判斷某項服務在該埠接受連線；還不能推論自己已經能讀取共享資料夾，更不能直接認定該主機存在漏洞。後續必須依據協定回應、身分驗證及實際授權情形判斷。

因此，M04 真正需要建立的是「從網路服務辨識資源、身分、設定與權限，再根據證據判定資安風險」的能力。

## 七、課前理解測驗

先測試兩題，確認 M03 與 M04 的銜接觀念。答案先不揭露。

Q1. 某 Windows 主機開放 TCP 445。以下哪個敘述最正確？

A. 代表攻擊者已能讀取所有共享資料夾

B. 代表主機一定存在 SMB 漏洞

C. 代表可能有 SMB 服務，仍需進一步確認可取得的資訊與存取權限

D. 代表主機一定啟用了 NetBIOS

Q2. 在企業網路中，你想知道網域有哪些使用者與群組。以下哪一項最直接相關？

A. NTP

B. LDAP

C. TFTP

D. BGP

提交答案並查看解析

我的建議是先依這個順序完成前兩堂課，建立 Enumeration、DNS、FTP、SMB、NetBIOS、SMTP 的操作與概念基礎，再進入 Linux、SNMP 與 Active Directory。這比直接記憶大量工具名稱更能形成可長期運用的資工與資安知識。
"""