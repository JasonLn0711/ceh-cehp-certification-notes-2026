# 講義二完整筆記：M01 管理安全、M02 偵察、M03 掃描

[中文總覽、來源與逐節覆蓋](README.md) · [講義一](part-01.md) · [概念連結](connections.md)

整理日期：2026-09-21，Asia/Taipei。來源為 Jason 本次貼入的第二份中文講義；三十節及收斂案例均保留筆記。內容屬教學整理，非錄音逐字還原。假想例子與講義補充不代表真實事故或已執行實驗。H2-01 至 H2-35 的完整網址見[來源表](sources.md)。

<a id="h2-01"></a>
## 1. Cyber Kill Chain、ATT&CK 與 Diamond Model

三模型的工作不同：**Kill Chain 看推進階段；ATT&CK 看目標與方法；Diamond Model 看事件要素關係**。它們可互補，不彼此替代。

Cyber Kill Chain 七階段：reconnaissance（偵察）→ weaponization（準備工具／內容）→ delivery（交付）→ exploitation（利用）→ installation（安裝／建立後續活動條件）→ command and control（C2 指令／資訊交換）→ actions on objectives（竊取、改動、干擾等最終目標）。七階段是講義補充，錄音由 USB 例子中段開始。普通 USB 插入、程式執行、安裝成功、建立遠控各有條件，不能省略。防守問題是在哪個階段能觀察或攔阻。

ATT&CK 將 tactic（目的）、technique（方法）、procedure（具體實作）分開；例如 initial access／phishing／某次訊息及交付序列。行為可重複、交錯或省略，不必由矩陣左走到右。使用流程：觀察 → 對應技術 → 找支持紀錄 → 驗證控制。標上編號尚未證明能偵測。

Diamond Model 用 adversary、capability、infrastructure、victim 描述入侵。公司電腦連可疑網域時，可能已知部分設施與受影響端點、但對手未知；某國 IP 不足以確定國籍或歸因。

來源：H2-01、02；[既有模型與 USB 查核](../m01-foundations.md#intrusion-models)、[講義一 TTP](part-01.md#h1-06)。

<a id="h2-02"></a>
## 2. Information Assurance 與持續調整

IA 是用措施與證據支持資訊安全的可信程度；講義引 NIST 定義涉及可用性、完整性、機密性、身分驗證及不可否認性，錄音四項不是唯一完整定義。「僅人資能讀薪資」需接到身分、權限、離職撤權與實際測試。

Security control 可以是技術、流程或人員安排，不只設備。課堂 `Protect → Detect → Respond → Predict` 是保護、偵測、應變、再依資訊預估風險的組織方式，不是所有框架的固定順序。限制權限 → 看異常下載 → 處理受影響帳號 → 調整規則是教學例子；predict 保留不確定性。

來源：H2-03；[縱深控制英文筆記](../m01-foundations.md#layered-controls)。

<a id="h2-03"></a>
## 3. Defense in Depth：互補控制與共同失效

由政策／SOP、實體安全、邊界網路、內網、主機、應用到資料逐層檢查。政策說責任與允許行為，SOP 說核准、陪同、設備帶出如何執行。實體保護處理接觸／磁碟攜出；DMZ 是互通受控區域，公開網站不應自由存取薪資系統；進公司 Wi-Fi 後仍要區隔。通過前一層不取消後面的授權。

Mantrap 是雙門受控通道概念，實際設計還要顧及人身安全與疏散。層數多不等於強：若全部控制依賴同一失竊管理帳號，可能共同失效。應問各控制是否保護不同界線，並具備獨立有效的檢查。接到[既有縱深筆記](../m01-foundations.md#layered-controls)與下一節。

<a id="h2-04"></a>
## 4. SID、ACL、NTFS 與離線磁碟

NTFS 保存檔案及其安全資訊。SID 識別 Windows 使用者／群組等安全主體，同名 Alex 不等於同一 SID。ACL 是控制項目集合；DACL 中的 ACE 表達對主體的允許或拒絕。Access token 帶有效身分、群組等安全資訊。讀檔時，由作業系統依安全情境、要求及 DACL 判斷。

**SID 名稱不能解析 ≠ DACL 消失 ≠ 所有人取得權限**。磁碟搬到另一台機器後，真正的另一道界線是：控制離線讀取環境者可能不走原 OS 權限檢查。適當靜態資料加密，在必要金鑰未同時取得的前提下提供內容保護。檔案權限處理受管理環境內存取；加密處理離開原環境的資料保護，兩者互補。

來源：H2-04–06；[英文 SID 查核](../m01-foundations.md#windows-permissions)、[Windows 課程講義](../../../../nycu_114-2_network_security_practices/handouts/windows-access-control.md)。

<a id="h2-05"></a>
## 5. Risk 與變更管理

Risk 同時看 likelihood 與 impact／consequence；不是「已知不修」，也不只發生機率。高頻小不便與罕見全部資料損失應比較後果；缺資料時寫清假設及不確定性，避免虛構精準乘積。

課堂循環：**Identify 資產／事件／後果 → Assess 可能性／影響／未知 → Treat → Track → Review**。處理方式有降低（修補／限縮）、避免（停止不必要活動）、接受（由有權者理解剩餘風險並設定追蹤／重評）、轉移或分攤部分後果（契約／保險）；保險不修漏洞，也不移走全部責任。

延到週五更新，需先確認適用性、不修補暴露、更新服務風險、測試與復原、核准變更、執行及驗證。這是 change management 的取捨。舊機暫不能更新仍可限縮存取或安排替換，不必把選項縮成立即全修／完全放棄。

來源：H2-07；[風險詳解](../m01-foundations.md#risk)與[弱點到傷害](../../m05-vulnerability-analysis/lesson-01-weakness-to-harm.md)。

<a id="h2-06"></a>
## 6. CTI、SOC、CVE 與情報生命週期

CTI 將資訊分析成特定角色可採取的決策。某公司受害是消息；其進入方式、我方相似系統、可用紀錄、應交誰處理才構成有用問題。

| 類別 | 決策用途 |
| --- | --- |
| Strategic 策略型 | 較長期資源配置，例如供應鏈風險 |
| Tactical 戰術型 | TTP 與偵測／防護調整 |
| Operational 作業型 | 具體攻擊活動、目標、活動情境 |
| Technical 技術型 | 網域、檔案雜湊、弱點資訊等技術線索 |

分類會重疊，不限定某職稱只能看一類。SOC 是協調監控、分析、應變的功能，可內部、外包或混合；其他角色仍負責各自安全工作。CVE 識別公開已知弱點，不證明一台主機被入侵，也不直接給出組織完整風險。

生命週期：定義問題 → 蒐集 → 整理分析 → 傳遞給決策者 → 回饋更新。SOC 需將公告連到受影響資產／管理者，不只是轉寄；舊事件可辨識重複與變化，不因大家聽過就失去價值。[既有情報筆記](../m01-foundations.md#threat-intelligence)。

<a id="h2-07"></a>
## 7. Threat Modeling：資料流與信任邊界

安全目標 → 理解應用 → 拆解元件／資料流／權限 → 識別威脅 → 識別弱點。以報帳為例：員工只能讀自己資料，主管僅核准負責範圍；瀏覽器輸入、應用處理、資料庫保存與主管核准各有界線。

Decompose 不只是找報告收件同事，而是理解系統如何運作。Trust boundary 是安全假設或權限條件改變處；使用者欄位進伺服器時不能直接相信員工編號。這與[成績授權案例](part-01.md#h1-09)、[AI 外部資料指示](part-01.md#h1-10)同樣在問「來源能聲稱什麼，系統可相信到哪裡」。來源：H2-08；[既有建模／應變筆記](../m01-foundations.md#incident-response)。

<a id="h2-08"></a>
## 8. Incident Management 與升級／揭露

Event 是系統活動，alert 是值得注意的偵測訊號，security incident 需依安全影響與程序研判；每個警報不是已確認入侵。Artifact 包括日誌、郵件、檔案、畫面、時間與錯誤訊息，稱為跡證仍需確認可信度。

通報 → 判斷嚴重性／範圍 → 保留必要證據 → 限制持續影響 → 調查處理 → 恢復 → 檢討。這是教學流程；vulnerability handling、artifact handling、announcement、alert、handling、response、disclosure 不是僵硬線性順序。正在外流時不必等根因全查完才控制，但全面斷電也要考慮證據及營運。NIST SP 800-61 Rev.3 將應變放在 CSF 2.0 風險管理脈絡，本次已做選定來源核對。

Escalation 在此指向有能力／決策權者升級通報，說明已知、未知及所需支援，不是 privilege escalation。主管品質不能以性別或年資推定。主管機關通報、通知受影響者、對外公告是不同工作；講義以 GDPR 主管機關 72 小時原則及適用例外說明，不能一律等待修復。法律適用與時限的實際判斷需另核對具體主體與事件，本次不建立個案義務。

來源：H2-09、10；[應變詳解](../m01-foundations.md#incident-response)與[來源核對界線](sources.md#live-checks)。

<a id="h2-09"></a>
## 9. 監督式、非監督式與偵測錯誤

Supervised learning 使用帶目標標記的訓練例子，目標可為類別或數值。垃圾／正常郵件只是分類例子。流程：準備資料／標記 → 訓練 → 用未參與訓練資料評估 → 預測 → 追蹤錯誤。Unsupervised learning 在沒有該種目標標記下找結構，如依連線相似性分群，再交人分析。

是否有標記不保證準確；標記可能錯、資料可能偏、未來環境可能不同。False positive 把正常判異常；false negative 漏掉真異常。AI 方法名稱不代替成效評估。來源：H2-11；[既有 ML 筆記](../m01-foundations.md#machine-learning)與[跨課程連結](connections.md#trust)。

<a id="h2-10"></a>
## 10. 法律、標準與認證的用途

以下保留講義的學習分類及其更正，不是新作的各地法律適用意見。法律在適用條件下形成義務；標準可能因法律、合約或承諾而必須遵守；認證是在特定範圍內證明符合性。「尚未登記／未被查到」不免除適用義務。

| 名稱 | 講義保留的核心 | 應避免的擴張 |
| --- | --- | --- |
| PCI DSS | 支付卡帳戶資料及相關安全環境，涉及儲存／處理／傳輸者與可影響環境者 | 不限發卡銀行；付款外包仍需釐清責任；單純折扣會員卡非自動適用 |
| ISO/IEC 27001 | ISMS 包含範圍、風險、責任、執行、評估與持續改善 | 文件範本不等於落實；ISO 不直接替組織認證；員工稽核員訓練不等於公司認證 |
| NIST | 多種標準、框架與指引 | 不是美國版 ISO 認證，也非美國只用 NIST、其他國家只用 ISO |
| HIPAA | 美國定義中的 covered entities／business associates 及相關健康資訊義務 | 不涵蓋全球所有醫院；不能只用名稱判斷臺灣醫療同意個案 |
| SOX／SEC 保存規則 | 講義七年例子限於特定 audit／review 紀錄，可含相關電子通訊 | 不等於所有公司每封 email 或全部稅務資料都存七年 |
| DMCA | 技術保護措施規避、線上服務等著作權議題 | 不是首次承認非紙本創作有著作權 |
| GDPR | 2016 通過，主要規定自 2018-05-25 適用；個資權利受範圍與例外約束 | 刪除權不等於所有資訊全球消失；搜尋移除、平台刪除、源站刪除不同 |
| DPA 2018／UK GDPR／DUAA 2025 | 英國相關但不同法制部分，DUAA 修正既有架構 | 不是將 GDPR 換名稱；實際施行條款與日期須逐項確認 |

查詢順序是**國家／時間／主體／資料／義務／例外**。來源：H2-12–21；[既有法規查核](../m01-foundations.md#law-and-standards)。

<a id="h2-11"></a>
## 11. Footprinting、Reconnaissance 與主動／被動

足跡蒐集和偵察在教材有重疊，均將組織、人員、網路、系統資訊整理成可驗證認識。流程：目的／範圍 → 允許來源 → 來源／時間 → 觀察與推論 → 下一個驗證問題。

CCNA 職缺支持該工作需要相關知識，不能證明全公司設備品牌；也可能為客戶招人。Email `alex` 不證明內部 AD 同名，更沒有固定猜中百分比。

Passive reconnaissance 使用既存第三方資料而不向目標新增探測；active 產生目標互動，無須成功 TCP 連線。透過第三方工具或代理新增探測仍是互動。這與[passive attack](part-01.md#h1-07)的「是否改變觀察對象」是不同分類軸。[英文蒐集界線](../m02-reconnaissance.md#collection-boundary)。

<a id="h2-12"></a>
## 12. 搜尋工具觀察面的差別

| 工具／來源 | 可觀察什麼 | 限制 |
| --- | --- | --- |
| `site:example.org filetype:pdf` | 搜尋引擎索引中的特定站點 PDF；是搜尋式，不是 shell 命令 | 索引非網站完整現況，可用於己方公開資訊盤點 |
| GHDB | 第三方整理的搜尋範例 | 非 Google 產品；發現私人資料不自動授權取得 |
| Shodan | 網際網路服務／設備資訊，觀察面不同於一般網頁搜尋 | 收錄不等於當前有漏洞，無登入畫面不等於公開使用許可 |
| DNSDumpster | 網域紀錄／關係線索 | 非全公司完整 DNS 資料庫，非封包路由圖 |
| Wayback Machine | 歷史擷取快照 | 擷取時間不等於修改時間；頁尾公司名稱改變不足以證明併購法律關係或動機 |

[英文搜尋筆記](../m02-reconnaissance.md#search-tools)與[DNS／歷史](../m02-reconnaissance.md#dns-and-history)保留對應查核。

<a id="h2-13"></a>
## 13. Competitive Intelligence 與 OSINT

競爭情報可分析公開產品、職缺、專利；公開資料分析和竊取營業秘密不同。專利公開不保證產品即將上市，照片打光不足以判斷專訪付費與金額。

TheHarvester 的 `-d`、`-b`、`-l` 在講義分別涉及目標、資料來源、結果限制；支援來源与參數依安裝版本文件核對，不能由 ASR 猜操作。OSINT 的 open source 指公開資訊來源，並非工具必須開源。OSINT Framework 是資源目錄，連結未必免費或開源。Maltego、Recon-ng、FOCA 是依語境判讀，沒有完整版本／操作，不能補寫成完成的實驗。[既有競爭情報筆記](../m02-reconnaissance.md#competitive-intelligence)。

<a id="h2-14"></a>
## 14. Dark Web、Tor、Bitcoin

Dark web 在此指需特定網路或軟體存取的服務；搜尋不到的資料不全屬暗網。Tor Browser 使用 Tor 網路；relay 和一般商用 VPN 伺服器概念不同。一般網站可能看到 Tor 出口位址，onion services 則有不同連線安排。來源 IP 改變只證明觀察位址改變，不證明所有活動無法關聯。

Bitcoin 是另一個支付／帳本議題；公開交易史不等於地址背後身分直接可知，去中心化也不等於不可追蹤。未識別的資料販售個案不作實證，更不能推全體交易用途比例。來源：H2-22、23；[英文 Tor／Bitcoin](../m02-reconnaissance.md#tor-and-bitcoin)。

<a id="h2-15"></a>
## 15. WHOIS、RDAP、DNS 與地理線索

WHOIS 是傳統註冊查詢；RDAP（Registration Data Access Protocol）提供標準化註冊資料查詢。講義引 ICANN 自 2025-01-28 以 RDAP 為 gTLD 註冊資料正式來源；這不表示所有 ccTLD 同日停 WHOIS。註冊狀態、註冊商、公開日期不是所有伺服器設定或私人聯絡資料。

| 紀錄 | 用途 |
| --- | --- |
| A | IPv4 位址 |
| MX | 郵件交換伺服器資訊 |
| NS | 區域名稱伺服器資訊 |
| CNAME | 名稱別名 |
| TXT | 文字，常供設定／驗證用途 |
| PTR | 反向名稱查詢常用紀錄 |

正向查詢從名稱找位址等資料；反向依獨立管理的 PTR 查名稱，不是數學反函數。正向成功不保證反向同名，PTR 不驗證使用者／設備所有權。IP geolocation、供應者所在地、實際使用者地點分開看。來源：H2-24、25；[DNS 與註冊詳解](../m02-reconnaissance.md#dns-and-history)。

<a id="h2-16"></a>
## 16. Traceroute、TTL、CDN

Traceroute（Windows `tracert`）以不同 TTL 的探測與回覆推測部分中繼路徑；各平台探測方式可不同。IP TTL 經路由轉送遞減，避免無限存活；某跳沉默可能只是未回覆，未證明沒有設備或路徑斷掉。

Linux 常見初始 64、Windows 常見 128 是線索，TTL 可設定且不專屬 OS。收到 58 加去程六跳得到 64 的算術，需有回程同樣六跳的前提；路徑可能不對稱，不能直接證明後端 Linux。DNS TTL 是快取有效時間，與 IP TTL 是不同欄位。

CDN 是分布式內容傳遞架構，不只是高速海纜。觀察 IP、回應、OS 特徵可能是邊緣節點，不能推出來源業務系統；雲端／CDN 也不保證免於 DoS。來源：H2-25；[路徑與 TTL 詳解](../m02-reconnaissance.md#paths-and-ttl)。

<a id="h2-17"></a>
## 17. Email Headers 與來源證據

SMTP 處理節點會加入 `Received` 等資訊。分析應保存原始郵件 → 檢查標頭 → 辨識可信節點 → 對照時間與伺服器紀錄 → 做有限路徑判斷。郵件閘道、垃圾檢查、歸檔與郵件服務可能存在，但順序非所有公司一致。

不是每個內部流程都出現在標頭，較早欄位也可能不可信，因此不能由一封信畫出完整公司網路。Message-ID 是識別資訊，不是數位簽章或真實身分證明。來源：H2-26；[郵件詳解](../m02-reconnaissance.md#email-and-human-factors)與[簽章證據](part-01.md#h1-04)。

<a id="h2-18"></a>
## 18. 社交工程與資訊暴露對策

接觸 → 信任／壓力 → 偏離程序 → 提供資訊或行動。假 IT 來電是辨識流程弱點的教學，不是取得對同事測試的許可。需要獨立可信的確認渠道，以及敏感操作前停下確認的機制。

Eavesdropping 是取得不該聽到的資訊；shoulder surfing 是窺視輸入／畫面；dumpster diving 從廢棄文件或媒體蒐集；impersonation 冒稱角色。它們可重疊，也不全是同種欺騙。外觀、地理題答錯、單句反應不足以判斷機器人或犯罪者。

Directory listing 顯示目錄檔名，可為正常公開索引或意外暴露；關閉列表不禁止直接讀檔。公開目錄中的備份應保護內容權限，而非只藏檔名。禁止社群連線不刪除既有公開資料；平台可取得某些站外活動，不等於內建瀏覽器每次必偷所有密碼。[既有反制問題](../m02-reconnaissance.md#email-and-human-factors)。

<a id="h2-19"></a>
## 19. RDP、VM、Terminal、Shell、root

第二段列四台 VM：**Parrot、Windows Server 2019、Windows Server 2022、Windows 11**。缺白板與帳密手冊，仍不推測 IP、角色或登入資訊。RDP 是遠端桌面互動協定，`mstsc` 是 Windows 連線程式；VM 是虛擬電腦，兩者不相同。

Terminal 提供文字輸入輸出介面，shell 解讀命令；root 是 Linux 高權限帳號，sudo 依政策以指定身分執行；`whoami` 顯示有效使用者，不提升權限。本機 root 不提供任意網路測試許可。[虛擬化詳解](../course-overview.md#virtualization)、[命令參考](../m03-network-scanning.md#command-reference)。

<a id="h2-20"></a>
## 20. Host、Port、Service、Socket

掃描語境的 host 泛指目標設備，正式架構仍可區分終端主機與路由器。Service 是功能軟體；port 是傳輸層端點編號，TCP 與 UDP 各有編號空間。TCP 21 常用 FTP 控制、80 常用 HTTP，慣例不是產品識別證據。

`/etc/services` 與 Windows 對應檔案是服務名稱／編號對照，不是封包分派中心。應用建立 socket、綁定位址／port，OS 依協定及連線資訊分派資料；改名稱表不會讓正在跑的網站自動換監聽 port。[傳輸與 socket 詳解](../m03-network-scanning.md#transport)。

<a id="h2-21"></a>
## 21. Packet、Header、Payload、MTU

表頭是該層處理資訊，payload 是該層承載內容；IP payload 可含 TCP header 和資料。來源／目的 IP 在 IP 表頭，來源／目的 port 在 TCP 表頭。

Packetization 是安排傳送單位；TCP segmentation 是把位元組串流安排成區段；IP fragmentation 是在適用條件下把 IP 封包分片並重組。MTU 是特定鏈路條件的最大傳輸單元，不直接等於應用資料量。假設 IP MTU 1,500、IPv4 header 20、TCP header 20 bytes，無額外選項：**1,500 − 20 − 20 = 1,460 bytes TCP 資料**。不是所有網路都固定如此。

分塊還涉及共享資源、跨鏈路與重傳效率，不只早期線路品質。[表頭與連線詳解](../m03-network-scanning.md#tcp-state)。

<a id="h2-22"></a>
## 22. TCP、UDP 與可靠性的層次

TCP 提供有序、具可靠機制的位元組串流，以序號、確認、重傳處理問題；網路失效仍可能傳輸失敗，TCP 也不提供加密。**TCP ACK 是傳輸確認，不是應用驗證、磁碟寫入或資料庫提交完成**。

UDP 傳資料報，本身沒有 TCP 的連線、順序、可靠傳輸機制；應用仍能自建確認／重傳。檔案常重完整順序，即時互動可能更重時效。UDP 非永遠更快；協定可否配置取決於應用支援，管理者不能將只懂 TCP 的程式單方切 UDP 就期待互通。來源：H2-27；[傳輸詳解](../m03-network-scanning.md#transport)。

<a id="h2-23"></a>
## 23. TCP Flags、三向交握、FIN

| Flag | 語意 | 更正 |
| --- | --- | --- |
| SYN | 同步序號，常見於建立連線 | 不是一般操作許可 |
| ACK | 確認號碼欄位有效 | 不要求每包分別回一包 |
| FIN | 此方向沒有更多資料 | 是方向性結束，不是雙方同時無資料 |
| RST | 重設、拒絕或中止相關連線 | 非唯一正常收尾方式 |
| PSH | 與交付資料給接收應用行為有關 | 非所有緩衝區立刻全清 |
| URG | urgent pointer 有意義 | 非整包享最高處理優先權 |

這是六個傳統旗標，不是完整控制位元清單。講義例子：甲 SYN seq=100 → 乙 SYN seq=500、ACK=101 → 甲 ACK=501。雙方各有序號空間，SYN 占序號；之後 ACK 對應預期下一位元組位置，不是第幾包。數字屬教學，非還原白板。

TCP 兩方向可分別結束；FIN／ACK 可合併或重傳，所以常見四包關閉圖不是永恆定律。來源：H2-27；[交握圖](../m03-network-scanning.md#handshake-model)。

<a id="h2-24"></a>
## 24. Host Discovery：ARP 與 ICMP

ARP 在本地 IPv4 鏈路問 IP 對應的鏈路層位址。MAC 不是跨 Internet 不可改的身分證。ARP 回覆證明相應位址解析行為，不是電源儀器；代理回覆、虛擬化都影響實體與應用健康推論。

ICMP 提供控制與錯誤訊息；ping 常用 Echo Request／Reply。無回覆可能因過濾、路徑、設定或狀態。Nmap 對本地乙太網目標可能以 ARP 發現，即使指定其他 `-P*`；命令列寫 ICMP 不保證結果就是 Echo 回覆造成。判讀需工具實際行為、權限、網路位置。來源：H2-28；本次[選定官方機制核對](sources.md#live-checks)及[主機發現詳解](../m03-network-scanning.md#discovery)。

<a id="h2-25"></a>
## 25. Port States、Connect Scan、SYN Scan

Open 支持有接受相關通訊的端點；closed 表示可回應但沒有該接受狀態；filtered 表示過濾等因素使工具無法區分 open／closed。它們屬特定時間、位置與方法的結果。這是本課三個重點狀態；其他 Nmap 組合狀態仍依官方規則。

`-sT` 使用 OS connect 功能，開放端點通常完成交握後收尾；只代表可建立 TCP，非所有應用功能正常。`-sS` 不完成一般完整連線，稱 half-open；典型 SYN+ACK 支持 open、RST 支持 closed，沉默／ICMP 錯誤需按掃描規則判讀。半開放仍可能被封包監測、網路設備、IDS 發現；無完整應用連線紀錄不等於無痕。掃描範圍／順序依預設和選項，不是固定從 1 到全部 ports。

來源：H2-29、30；[主機／port 判讀](../m03-network-scanning.md#discovery)。

<a id="h2-26"></a>
## 26. Banner、Version、OS、NSE

Banner 是服務回傳的歡迎／識別資料，可能省略、修改或偽裝。`-sV` 用服務探測／回應模式增加協定或產品線索，不只印 port 名稱表；**`-v` 只是詳細輸出，`-sV` 才是版本辨識**。

`-O` 比對 TCP/IP 堆疊特徵，不一定讀「我是 Windows」字串。可能某 Windows 家族不等於確認精確版本與更新。NSE 是腳本引擎；`smb-os-discovery` 透過 SMB 可取得資訊，依服務與權限而異；`.nse` 為副檔名，`/usr/share/nmap/scripts` 是常見 Linux 路徑，不跨平台保證。腳本應查實際行為／影響與授權，名稱像查詢不等於無副作用。

來源：H2-31、32；[服務與 OS 詳解](../m03-network-scanning.md#identification)。

<a id="h2-27"></a>
## 27. 七個命令的問題與證據界線

以下保留講義的文件化範例；`<LAB_IP>` 是占位符，需另有實際授權目標。這是讀命令的筆記，本次未執行。

| 範例 | 問什麼 | 不能直接宣稱 |
| --- | --- | --- |
| `nmap -sn -PR <LAB_IP>` | 本地 IPv4 ARP 發現，不做一般 port scan | 實體完整開機／應用正常 |
| `nmap -sn -PE <LAB_IP>` | 要求 Echo 發現，留意實際 ARP 行為 | 每項 up 都由 ICMP 證明 |
| `nmap -sT <LAB_IP>` | OS connect 的 TCP 端點狀態 | 業務功能全正常 |
| `nmap -sS <LAB_IP>` | SYN 回應所支持狀態 | 不可偵測／無紀錄 |
| `nmap -p 21 -sV <LAB_IP>` | port 21 服務／版本探測 | 弱點可利用 |
| `nmap -O <LAB_IP>` | OS 指紋比對 | 精確安裝／修補狀態 |
| `nmap --script smb-os-discovery <LAB_IP>` | 指定 SMB 腳本可取得資訊 | 所有欄位必出／任意腳本皆無影響 |

每次先辨別主機、port、服務、OS 哪一層問題，再對照結果。來源：H2-28–32；既有[13 個完整命令參考](../m03-network-scanning.md#command-reference)保留其他命令與查核。

<a id="h2-28"></a>
## 28. 分片、路由、偽冒、檢查碼

| 概念 | 原理與防守問題 | 查核更正 |
| --- | --- | --- |
| Fragmentation | 中間設備與接收端若重組／理解不同，可能形成檢查落差及成本 | 分片有正常用途，非全部無例外丟棄 |
| Source routing | 來源提供部分路由資訊，需辨別機制與政策必要性 | 不與所有一般路由混稱 |
| Source-port manipulation | 不嚴謹規則可能錯信來源 port | 外傳到目的 port 80 是另一種出站政策問題；允許 80／443 不保證正常業務 |
| Decoy | 多個聲稱來源增加判斷混淆 | 不代表擁有那些 IP 或必能騙過設備 |
| IP spoofing | 聲稱來源與實際發送不同；如甲寄乙卻填丙為回覆位址 | 回覆可能到丙，不能自然取得雙向資料；可用來理解 reflection |
| MAC spoofing | 部分設備可改使用的鏈路層位址 | 非所有設備相同，也非跨 Internet 隱身 |
| Packet builder | 軟體可建構指定欄位／內容；課堂例 Colasoft | 可建構不等於任意場域可發送 |
| Checksum | 檢查協定規定範圍內的某些錯誤 | 非簽章；能改內容者可能重算。故意錯碼不保證穿過防火牆 |

此處是概念與防守判讀，沒有增加規避操作。來源：H2-33；[既有規避與防禦詳解](../m03-network-scanning.md#evasion-and-defense)。

<a id="h2-29"></a>
## 29. Proxy、VPN、No-logs

Proxy 代一方進行部分通訊，支援能力依種類／配置；VPN 是另一種網路連接與通訊保護機制，不只是大型 web proxy。目標看見的來源可改變，但互動仍存在，不能因此稱被動偵察。

No-logs 是需要界定紀錄種類、期間、系統及驗證方式的聲稱。多層 VPN、境外位址與 no-logs 都不能保證絕對無法關聯或調查必然失敗。公司受控代理可管理外部目的地，也說明信任只是移到另一處。[既有身分／規避邊界](../m03-network-scanning.md#evasion-and-defense)。

<a id="h2-30"></a>
## 30. 防禦措施的精確保護範圍

ICMP 還負責控制與錯誤回報；限制 Echo 與全面丟 ICMP 不同，後者可能影響正常功能。IDS 提供偵測／警報，IPS 在部署／規則條件下可阻止；有警報未必阻止，無警報未必沒問題。

Apache `ServerSignature Off` 控制伺服器產生頁面的署名；`ServerTokens` 控制 HTTP `Server` header 揭露程度，精簡仍可能留產品名稱。隱藏版本不修版本、權限、設定弱點。本次官方設定核對見[來源表](sources.md#live-checks)。

TTL 或 IPv4 ID 差異可能來自正常路徑／設定；IP ID 不保證全機逐包遞增，因此差異不單獨證明 spoofing。Source-address validation 問來源是否應從該網路位置出現。加密保護特定內容與邊界，配適當驗證／完整性機制可支持其他目標，但不自動修受感染端點、不濾除所有偽造封包、不防有限頻寬耗盡；「解決 80% 網路問題」無證據。

來源：H2-34、35；[英文反制詳解](../m03-network-scanning.md#countermeasures)。

<a id="worked-example"></a>
## 收斂：一份有邊界的掃描判讀

**以下全為講義教學情境，本次沒有操作 VM。** ARP 回覆、ICMP Echo 沉默、TCP 21 open、服務辨識符合某 FTP 產品，可以同時成立。

| 觀察 | 支持結論 | 保留未知 |
| --- | --- | --- |
| ARP 回覆 | 本地鏈路有相應解析回應 | 是否代理回應、實體狀態、應用健康 |
| ICMP 無回覆 | 此次未取得 Echo 回覆 | 過濾、路徑、設定、狀態等原因 |
| TCP 21 open | 當時該觀察點可接觸該 TCP 端點 | 實際應用、業務健康、授權 |
| FTP 產品匹配 | 回應與工具模式相符 | 精確版本、修補、漏洞適用與利用 |

下一步依原目標選：資產核對、不必要服務處理或特定弱點適用性；工具還有選項不是擴張範圍理由。掃描判讀紀錄至少包含目的、授權、來源位置／時間、工具版本／權限、探測、原始觀察、可支持結論、未知與下一步。讀者應能解釋工具問了什麼、系統回答什麼、結論如何受到證據限制。

這條鏈與[原英文判讀矩陣](../m03-network-scanning.md#interpretation-chain)及[既有 W37 服務資料證據](../../../projects/weekly-incident-projects/2026-W37-forgotten-portal-discovery/continuation-2026-09-09-1948/metadata-comparison.md)相連；歷史實作保留自己的時間與範圍，不作本次掃描結果。

## 完整英文對照

[英文 M01 後半](../plain-english/m01-foundations.md#p2-01)對應 §1–10；[英文 M02](../plain-english/m02-reconnaissance.md#p2-11)對應 §11–19；[英文 M03](../plain-english/m03-network-scanning.md#p2-20)對應 §20–30 及收斂案例。詳細[追溯表](../plain-english/coverage.md)包含所有子節。
