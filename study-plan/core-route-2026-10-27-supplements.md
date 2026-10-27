# 章後補充考點檢查清單

[161 單元路線](core-route-2026-10-27.md) · [來源](../source/2026-10-27-core-route/README.md)

以下保留附件各章表後原文，僅解碼 HTML entity；是待覆蓋清單，不新增單元數、不代表已讀或已懂。於該章單元適當位置串接，尤其 M04 其他服務、M06 工具／證據、M08 VLAN/STP 與 M20 量子／Blockchain 延伸。

## M01

- [ ] 在 [M01 第一單元](core-route-2026-10-27.md#ceh26-m01-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：Risk（風險）不等於 Vulnerability（弱點）。**

有弱點不代表已經遭入侵，也不代表所有弱點的處置優先級相同。還需要考慮受影響資產、威脅、暴露程度與既有控制措施。

第一輪另外要認識 CIA、Information Assurance、NIST、ISO/IEC、PCI DSS 等框架或規範的角色，以及 CEH v13 納入的 AI 輔助資安工作。它們不能彼此視為等價的認證或合規制度。

## M02

- [ ] 在 [M02 第一單元](core-route-2026-10-27.md#ceh26-m02-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：Passive Reconnaissance 與 Active Reconnaissance 的區別。**

使用搜尋引擎查詢公開資訊，和直接對目標主機發送探測封包，是不同類型的活動，也可能涉及不同的授權條件。

## M03

- [ ] 在 [M03 第一單元](core-route-2026-10-27.md#ceh26-m03-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：Port State 是觀測結果，不是入侵結果。**

例如 `445/tcp open` 不能單獨證明 SMB 共享可讀取、身分驗證可繞過，或主機已有漏洞。

## M04

- [ ] 在 [M04 第一單元](core-route-2026-10-27.md#ceh26-m04-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：看得到資源，不等於具有操作資源的權限。**

例如 SMB 能列出共享名稱，不代表目前身分能讀取、修改或刪除其中的檔案。

官方 M04 還包括 Telnet、TFTP、DNS 相關技術及多種網路服務；這些可以先達到協定辨識與安全風險判讀程度，再視工作需要深入。[cert.eccouncil.org](https://cert.eccouncil.org/wp-content/uploads/2024/04/CEH-Exam-Blueprint-v5.pdf)[eccouncil.org](https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/)

## M05

- [ ] 在 [M05 第一單元](core-route-2026-10-27.md#ceh26-m05-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：Vulnerability Finding ≠ Confirmed Exploitability。**

掃描器判定某版本可能受影響，仍需要確認實際版本、修補狀態、設定與漏洞成立條件。

CVSS、KEV、EPSS 是實務優先排序的補充；它們並不是官方 M05 藍圖獨立列出的三個考試項目。

## M06

- [ ] 在 [M06 第一單元](core-route-2026-10-27.md#ceh26-m06-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：Privilege Escalation 的核心是突破既有的授權邊界。**

本機 Administrator、Linux root 與 Active Directory Domain Admin 不可視為同一個權限層級。

官方另外涵蓋 Metasploit、Keylogger、Rootkit、Spyware、Steganography、Steganalysis、執行工具與日誌清除技術。第一輪要理解其機制與防禦證據，但不需要在一般系統上實際部署惡意工具。

## M07

- [ ] 在 [M07 第一單元](core-route-2026-10-27.md#ceh26-m07-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：File、Process、Memory 與 Network Evidence 是不同類型的證據。**

檔案存在不代表正在執行；程序正在執行不代表它是惡意的；TCP 已建立連線也不能單獨證明存在 C2。

官方還納入 AI-based Malware 與 AI 輔助惡意程式分析，可在熟悉基本證據模型後作為研究延伸。[eccouncil.org](https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/)

## M08

- [ ] 在 [M08 第一單元](core-route-2026-10-27.md#ceh26-m08-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：封包是否可被看見、是否可被修改、內容是否可讀取，是三個不同問題。**

即使攻擊者改變了區域網路封包路徑，正確配置的 TLS 仍可保護大部分應用程式內容與完整性。

官方課程還包含 VLAN Hopping、STP Attack、Promiscuous Detection。第一輪至少應能解釋其前提、主要風險與交換器防護機制。[cert.eccouncil.org](https://cert.eccouncil.org/wp-content/uploads/2024/04/CEH-Exam-Blueprint-v5.pdf)[eccouncil.org](https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/)

## M09

- [ ] 在 [M09 第一單元](core-route-2026-10-27.md#ceh26-m09-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：信任不能取代驗證。** 即使訊息看起來來自主管，也必須透過獨立且可信的管道確認要求及授權。

進階補充是 AI Deepfake、AI 生成釣魚內容及社群平台冒充，但應回到身分與授權驗證的基本原理。

## M10

- [ ] 在 [M10 第一單元](core-route-2026-10-27.md#ceh26-m10-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：DoS 的本質是有限資源遭到耗盡。**

不一定要塞滿網路頻寬。若某 API 的每個請求都需要非常昂貴的資料庫查詢，即使流量不高，也可能耗盡應用程式資源。

## M11

- [ ] 在 [M11 第一單元](core-route-2026-10-27.md#ceh26-m11-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：Session Token 是具有存取能力的驗證材料。**

所以只保護使用者密碼還不夠；工作階段本身也需要安全傳輸、保管與撤銷機制。

## M12

- [ ] 在 [M12 第一單元](core-route-2026-10-27.md#ceh26-m12-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：Detection Gap（偵測落差）。**

沒有收到告警，並不代表沒有發生攻擊。還必須檢查感測器位置、日誌覆蓋率、偵測規則、資料保留及加密流量的可見範圍。

官方還要求認識 IDS／Firewall／NAC 規避方法、工具類別，以及 Honeypot 辨識。學習時應以解析差異、監測限制和修補策略為核心。[cert.eccouncil.org](https://cert.eccouncil.org/wp-content/uploads/2024/04/CEH-Exam-Blueprint-v5.pdf)

## M13

- [ ] 在 [M13 第一單元](core-route-2026-10-27.md#ceh26-m13-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：Reverse Proxy 與 Backend 是不同的安全邊界。**

例如使用 Cloudflare、Nginx、FastAPI 的系統，需要分別理解邊緣服務、反向代理及後端 API 的授權與安全設定。

## M14

- [ ] 在 [M14 第一單元](core-route-2026-10-27.md#ceh26-m14-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：Authentication ≠ Authorization。**

即使使用者 A 已成功登入，也不代表他可以讀取使用者 B 的資料。API 必須在伺服器端檢查身分與每項受保護資源、操作之間的授權關係。

另外，官方 CEH v13 課程頁仍包含 OWASP Top 10:2021；截至 2026 年 10 月，[OWASP Top 10:2025](https://top10.owasp.org/2025/) 已是最新正式版本。工程學習應補充新版本，但考試仍需核對當時教材。[eccouncil.org](https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/)[owasp.org](https://owasp.org/projects/top-ten)

## M15

- [ ] 在 [M15 第一單元](core-route-2026-10-27.md#ceh26-m15-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：Code 與 Data 必須分離。**

使用參數化查詢，可避免將輸入值直接串接成 SQL 語法。這比單純過濾特殊字元更可靠。

OWASP 的 Web Security Testing Guide 將身分、驗證、授權、Session、輸入、業務邏輯與客戶端測試分成不同範圍，也能用來建立 M13–M15 的完整練習。[wstg.owasp.org](https://wstg.owasp.org/stable/4-Web_Application_Security_Testing/)

## M16

- [ ] 在 [M16 第一單元](core-route-2026-10-27.md#ceh26-m16-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：Wireless Authentication 與 Application Authorization 是不同層級。**

例如設備已通過 Wi-Fi 或 BLE 配對，不代表它就有權存取應用程式中的所有資料。

官方課程著重 Wi-Fi 安全、無線分析及攻擊工具；Bluetooth 也是官方考試藍圖明列的範圍。[cert.eccouncil.org](https://cert.eccouncil.org/wp-content/uploads/2024/04/CEH-Exam-Blueprint-v5.pdf)

## M17

- [ ] 在 [M17 第一單元](core-route-2026-10-27.md#ceh26-m17-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：OS Permission ≠ API Authorization。**

手機 App 被允許使用相機，不代表後端 API 就應允許該 App 上傳或讀取所有使用者的影像。裝置與伺服器都需要各自建立授權規則。

OWASP Mobile Top 10:2024 已發布正式版本，官方 CEH v13 亦將其納入課程主題。[owasp.org](https://owasp.org/projects/mobile-top-10)[eccouncil.org](https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/)

## M18

- [ ] 在 [M18 第一單元](core-route-2026-10-27.md#ceh26-m18-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：Cyber-Physical Risk（數位與實體風險的連結）。**

OT 與一般 IT 系統最大的差異之一，是不當的網路操作可能影響設備、物理程序或人身安全。因此不能直接把一般網路掃描方法套用到營運中的工控環境。

NIST SP 800-82 Rev.3 特別重視 OT 的 Performance、Reliability、Safety。2026 年 9 月已公布 Rev.4 初步公開草案，但目前正式版本仍是 Rev.3。[csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/82/r3/final)

## M19

- [ ] 在 [M19 第一單元](core-route-2026-10-27.md#ceh26-m19-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：Shared Responsibility Model（共同責任模型）。**

使用雲端平台不表示對方會自動替你保護所有設定、應用程式與資料。例如，儲存權限及 API 授權仍然需要由相關責任方正確規劃和維護。

另外需要理解 Container 並非完整虛擬機，容器與 Host Kernel 的安全邊界也不同於獨立 VM。

## M20

- [ ] 在 [M20 第一單元](core-route-2026-10-27.md#ceh26-m20-c01)開始、章末檢查以下補充覆蓋。

**最重要的小概念：Encryption、Hashing、Digital Signature、Authentication 是不同機制，不能混用。**

例如，TLS 不只是使用 AES 加密資料，也涉及身分驗證與安全金鑰建立。只有加密而沒有正確驗證通訊對象，仍可能產生安全問題。

官方 CEH v13 課程另涵蓋 Blockchain、Quantum Cryptography 與密碼分析工具。後量子密碼學則可額外認識 NIST 於 2024 年發布的 FIPS 203、204、205，這些是現代延伸知識，不應誤認為 CEH Blueprint 獨立配置了相關題數。[eccouncil.org](https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/)[csrc.nist.gov](https://csrc.nist.gov/News/2024/postquantum-cryptography-fips-approved)
