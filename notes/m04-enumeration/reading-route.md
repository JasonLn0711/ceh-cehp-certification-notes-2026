# M04 Enumeration｜一次一個重要概念

依[2026-10-22 採用規則](../../study-plan/concept-reading-2026-10-22.md)，每列是一個完整閱讀任務；可跨次接續，不另拆獨立子任務。先讀12個核心，再接M05；7個辨識／風險主題保留選讀。防護貫穿每一項，第12項再整合。[原文與決策](../../source/2026-10-22-concept-reading/README.md)保留順序依據。

官方 [Blueprint v5.0 第2頁](https://cert.eccouncil.org/wp-content/uploads/2024/04/CEH-Exam-Blueprint-v5.pdf)列 Enumeration 七題；十九項及12＋7深度是教學安排，不是官方題數分配。既有[M04–M06課程索引](../2026-10-04-ceh-week-02/README.md)與[題庫](../../assessments/practice-bank/m04.md)供有需要時查閱，不增加本次作業。

## 閱讀目錄

| ID | 重要概念 | 理解目標 | 第一輪深度 | 教材整理 |
| --- | --- | --- | --- | --- |
| M04-01 | Enumeration Concepts／列舉原理 | 區分偵察、掃描、列舉與存取權限 | 核心：用途、條件、證據與防護 | [教學原文](../../source/2026-10-23-one-concept/M04-01-teaching.md) |
| M04-02 | DNS Enumeration／DNS 列舉 | 常見記錄、查詢結果、AXFR、Cache Snooping 與 DNSSEC 的界線 | 核心：用途、條件、證據與防護 | [教學原文](../../source/2026-10-23-one-concept/M04-02-teaching.md) |
| M04-03 | FTP Enumeration／FTP 列舉 | 服務回應、匿名登入與檔案權限各自能證明什麼 | 核心：用途、條件、證據與防護 | [教學原文](../../source/2026-10-24-one-concept/M04-03-teaching.md) |
| M04-04 | SMB Enumeration／SMB 列舉 | 共享、驗證、授權與 TCP 445 的判讀界線 | 核心：用途、條件、證據與防護 | [教學原文](../../source/2026-10-24-one-concept/M04-04-teaching.md) |
| M04-05 | NetBIOS Enumeration／NetBIOS 列舉 | 名稱資訊、137–139 與現代 SMB 的關係 | 核心：用途、條件、證據與防護 | [教學原文](../../source/2026-10-24-one-concept/M04-05-teaching.md) |
| M04-06 | SMTP Enumeration／SMTP 列舉 | 郵件服務回應與帳號資訊揭露的條件 | 核心：用途、條件、證據與防護 | [教學原文](../../source/2026-10-25-one-concept/M04-06-teaching.md) |
| M04-07 | Unix/Linux User Enumeration／Unix/Linux 使用者列舉 | 使用者、群組、UID/GID 與權限 | 核心：用途、條件、證據與防護 | [教學原文](../../source/2026-10-25-one-concept/M04-07-teaching.md) |
| M04-08 | NFS Enumeration／NFS 列舉 | Export、掛載、身分對應與共享權限 | 核心：用途、條件、證據與防護 | [教學原文](../../source/2026-10-25-one-concept/M04-08-teaching.md) |
| M04-09 | SNMP Enumeration／SNMP 列舉 | MIB、OID、Community String、版本與驗證／加密設定 | 核心：用途、條件、證據與防護 | [教學原文](../../source/2026-10-26-one-concept/M04-09-teaching.md) |
| M04-10 | LDAP Enumeration／LDAP 列舉 | 目錄、DN、物件、屬性、群組與查詢權限 | 核心：用途、條件、證據與防護 | [教學原文](../../source/2026-10-26-one-concept/M04-10-teaching.md) |
| M04-11 | RPC Enumeration／RPC 列舉 | 遠端程序呼叫、介面與端點，辨識 Windows RPC 與 ONC RPC 的不同 | 核心：用途、條件、證據與防護 | [教學原文](../../source/2026-10-26-one-concept/M04-11-teaching.md) |
| M04-12 | Enumeration Countermeasures／列舉防護 | 由觀察證據連到風險、防護與驗證 | 核心：用途、條件、證據與防護 | 待整理 |
| M04-13 | Telnet Enumeration／Telnet 列舉 | TCP 23、明文遠端登入及與 SSH 的差異 | 辨識、解釋與風險判斷 | 待整理 |
| M04-14 | TFTP Enumeration／TFTP 列舉 | UDP 69、簡單檔案傳輸與缺少內建登入驗證的風險 | 辨識、解釋與風險判斷 | 待整理 |
| M04-15 | NTP Enumeration／NTP 列舉 | UDP 123、時間同步、版本與對等資訊揭露條件 | 辨識、解釋與風險判斷 | 待整理 |
| M04-16 | IPv6 Enumeration／IPv6 列舉 | IPv6 位址、ICMPv6、Neighbor Discovery 與主機發現 | 辨識、解釋與風險判斷 | 待整理 |
| M04-17 | VoIP Enumeration／VoIP 列舉 | SIP、分機、帳號與服務資訊 | 辨識、解釋與風險判斷 | 待整理 |
| M04-18 | IPsec Enumeration／IPsec 列舉 | IKE、VPN 協商、UDP 500/4500 與設定資訊 | 辨識、解釋與風險判斷 | 待整理 |
| M04-19 | BGP Enumeration／BGP 列舉 | TCP 179、AS、路由宣告、Peer 與資訊揭露風險 | 辨識、解釋與風險判斷 | 待整理 |

本表是公開教材目錄；個人交付、筆記與理解狀態在私人紀錄分開追蹤。AI 輔助列舉是選讀延伸，不列為第20個必做任務，也不推定有固定考題。

<a id="learning-record"></a>
## 交付與學習紀錄邊界

本公開 repo 保留完整教學與匿名整理內容。五項個人狀態及實際回答請在確認私人的紀錄中追蹤，依[現行規則](../../study-plan/concept-reading-2026-10-22.md#每日核心概念與公開頁--2026-10-23-採用)更新。既有歷史證據保留於 Git，不從教材存在推定個人學會。

[M04-01 教學原文](../../source/2026-10-23-one-concept/M04-01-teaching.md) · [公開概念頁](https://learn.cs-kairos.com/courses/ceh/v13/m04/concepts/m04-01/)。教材交付與理解確認各自前進；本人指定補強優先。

## M04-01 深化教材（版本歷史）

以下為各次修訂當時的紀錄；「下一概念」描述當時位置，現行交付順序以私人進度正本為準。

[同一概念頁](https://learn.cs-kairos.com/courses/ceh/v13/m04/concepts/m04-01/)在 revision 2 深化為七節教學，提供合成SMB案例、授權實驗步驟、證據矩陣與三題測驗。教材解析與實際Q&A分開；Q&A等收到實際討論後整理。原第一版教學來源保留，下一概念仍M04-02 DNS，AD為相關延伸。[技術校訂與覆蓋對照](../../docs/m04-01-revision-2-review.md)。

M04-01 v3 改為具體故事、短句與原生圖解；[改寫說明](../../docs/m04-01-revision-3-review.md)。沿用相同公開網址、七節與三題，屬同概念深化。

M04-02 DNS：[公開概念頁](https://learn.cs-kairos.com/courses/ceh/v13/m04/concepts/m04-02/) · [送出原文與網頁補充邊界](../../docs/m04-02-publication.md)。一題小檢核，Q&A待提供；下一核心為FTP。

十二核心之後接[M05路線](../m05-vulnerability-analysis/reading-route.md)，再接M06與M07；[47核心總規劃](../../study-plan/m05-m07-concept-plan-2026-10-23.md)。

DNS 補充：[M04-02 v2 校訂教材](../../source/2026-10-23-one-concept/M04-02-supplement-v2.md)與[來源差異](../../docs/m04-02-revision-2-review.md)，沿用原 ID；教學與測驗分開呈現，Q&A 待補。

[M04-03 FTP 概念頁](https://learn.cs-kairos.com/courses/ceh/v13/m04/concepts/m04-03/)與[發布紀錄](../../docs/m04-03-publication.md)：完整教學、一題待回答小檢核；下一核心為 M04-04 SMB。

[M04-04 SMB頁](https://learn.cs-kairos.com/courses/ceh/v13/m04/concepts/m04-04/) · [發布紀錄](../../docs/m04-04-publication.md)。完整教學與一題待回答小檢核，下一核心為M04-05 NetBIOS。

[M04-05 NetBIOS頁](https://learn.cs-kairos.com/courses/ceh/v13/m04/concepts/m04-05/) · [發布與來源說明](../../docs/m04-05-publication.md)。一題待回答小檢核，下一核心為M04-06 SMTP。

[M04-06 SMTP頁](https://learn.cs-kairos.com/courses/ceh/v13/m04/concepts/m04-06/) · [發布與來源說明](../../docs/m04-06-publication.md)。一題待回答小檢核，下一核心為M04-07 Unix/Linux使用者列舉。

M04-01 [v4繁中七節改寫](../../docs/m04-01-revision-4-review.md)保留既有版型與三題，僅此繁中頁程式碼改淺色；交付序列不變。

2026-10-25：M04-01 v6 主正文保留；現已收到並整理[兩份實際 SMB／Kafka 問答](../../docs/m04-01-qa-2026-10-25.md)，獨立收合、原文與校訂分區。兩題為教材測驗，尚無本人作答；其他概念的 Q&A 狀態各自保留。

[M04-07 Unix/Linux 使用者列舉](https://learn.cs-kairos.com/courses/ceh/v13/m04/concepts/m04-07/) · [原文與網頁補充邊界](../../docs/m04-07-publication.md)。一題待回答小檢核；下一核心為 M04-08 NFS。

[M04-08 NFS 頁](https://learn.cs-kairos.com/courses/ceh/v13/m04/concepts/m04-08/) · [來源與發布驗證](../../docs/m04-08-publication.md)。初版 v1.0.0，原文六節與一題小檢核；下一核心為 M04-09 SNMP。

[M04-09 SNMP 正式頁](https://learn.cs-kairos.com/courses/ceh/v13/m04/concepts/m04-09/) · [來源與發布驗證](../../docs/m04-09-publication.md)，初版 v1.0.0；下一核心 M04-10 LDAP。

[M04-10 LDAP 正式頁](https://learn.cs-kairos.com/courses/ceh/v13/m04/concepts/m04-10/) · [來源與發布驗證](../../docs/m04-10-publication.md)，初版 v1.0.0；下一核心 M04-11 RPC。
