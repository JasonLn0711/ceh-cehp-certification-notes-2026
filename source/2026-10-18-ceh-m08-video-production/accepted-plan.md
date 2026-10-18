# Accepted M08 implementation plan

The following is the substantive plan approved by “Implement the plan.”

## 交付與通則

沿用已採納的 CEH video production standard v1.0，補上 M08 適用紀錄，維持同一份通則。

依已確認的範圍，交付完整影片製作來源 ZIP。保留 M04 v3 紙感手繪設計、原創 Tally、Northstar、1920×1080／30fps，以及僅旁白 1.5× 的設定。實際配音、同步字幕與 MP4 屬後續製片階段。

## 課程內容

以 EC-Council M08 Sniffing 官方範圍為骨幹，重新編寫完整美式英文教學。

| 章節 | 場景 | 教學內容 |
|---|---|---|
| C01 | S01–04 | 模組銜接、Northstar 任務、授權與證據 |
| C02 | S05–09 | Ethernet、MAC／IP、交換器轉送與封包可見性 |
| C03 | S10–16 | 端點／SPAN／TAP、擷取與顯示篩選、離線分析流程 |
| C04 | S17–21 | 明文協定、HTTP、TLS／VPN、可見資訊與推論界線 |
| C05 | S22–26 | ARP spoofing／poisoning、MITM、證據與防護 |
| C06 | S27–32 | MAC spoofing／flooding、DHCP、starvation 與防護 |
| C07 | S33–38 | VLAN hopping、STP attacks、DNS poisoning 與對策 |
| C08 | S39–43 | Sniffer detection、工具限制、誤判與交叉驗證 |
| C09 | S44–48 | Northstar 四項相連案例與綜合判斷 |
| C10 | S49–53 | 防護、重新驗證、事件紀錄與 AI 輔助分析 |
| C11 | S54–58 | 八題分級選擇題、解析與綜合實作業 |

四項案例涵蓋觀測位置限制、ARP binding 變化、DHCP 異常與 DNS 回應差異。沿用既有裝置及 IP；新增網路角色以 M08 擴充資料記錄。

## 製作與驗收

- 以 M07 來源包為結構範本，重寫 M08 腳本、圖解、案例及八題原創測驗；保留既有 JSON 介面與獨立題目 namespace。
- 交付 58 張可編輯 SVG、18 頁可編輯 PPTX、完整英文逐字稿、學生作業、獨立教師解答、概念連結與來源對照。
- 提供四組可拖曳動畫範例：封包可見性、ARP 對應、DHCP／DNS 判讀、測驗靜音。
- 加入可重現的離線合成 PCAP、產生器及分析步驟。明確標示合成資料與觀測位置；使用現有 tcpdump -r 實測解析及 capture filters。Wireshark display filters 依官方文件核對，驗證紀錄區分實測與文件審查。
- 每題完整題幹及 A–D 選項後，設定 1.000 秒真靜音：48 kHz、48,000 個 stereo PCM frames，全零；答案於靜音結束後揭示。
- 驗證章節／場景／測驗對應、鎖定素材雜湊、文字溢出、字幕安全區、SVG、簡報編輯結構、動畫正反向 seek，以及 ZIP 解壓與逐檔雜湊。
- AGENT_PROMPT.md 要求後續直接完成全片，沿用 af_heart／0.73 基準及一次 atempo=1.5，不設短片批准關卡。來源包狀態標為 source_ready，實際字數、檔數與檢查結果由 M08 檔案重新統計。

輸出位置：
/home/jnlngx10/Videos/CEH_M08_v1_0/output/CEH_M08_English_Masterclass_HandDrawn_Editorial_v1_FULL.zip

## 紀錄與 Git

CEH repo 保存請求原文、M08 製作紀錄、來源與精簡 QA；大型素材留在 Videos。更新影片索引與 M08／P3 課程連結，並接回既有課堂紀錄，保留各自的證據狀態。

Planning 的 10 月 18 日日誌、W42 週計畫及 CEH 專案定位只記錄交付位置、狀態、驗證與下一步，保護既有學習容量；準備教材不增加學習完成紀錄。

依既有 Git 授權，按通則承接、M08 來源與 QA、文件連結、Planning 紀錄分開提交。發布前檢查並保留其他修改及遠端提交，執行相關 validators、連結檢查與 git diff --check，再推送 origin HEAD:main 並確認同步。
