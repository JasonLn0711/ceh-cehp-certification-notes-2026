CEH 有 20 個章節，請問網路上可以查到考古題，哪幾個章節的考題比重比較高嗎？或者考題於哪個章節的統計嗎？
可以，而且其實不需要依賴「考古題」去猜章節比重。EC-Council 有正式公布 CEH Exam Blueprint，這比網路流傳題庫可靠很多。

以目前可查到的 CEH Exam Blueprint v5.0 來看，CEH Knowledge Exam 是 125 題，而 20 個 Module 被歸成 9 個 Domain。官方甚至直接列出每個 Module 大約出幾題。([EC-Council Certification Lookup][1])

換成你課本的 20 個章節，大致是：

| Module | 章節                                | 官方約題數 | 約占 125 題 |
| ------ | --------------------------------- | ----: | -------: |
| M01    | Introduction to Ethical Hacking   |     7 |     5.6% |
| M02    | Footprinting and Reconnaissance   |     7 |     5.6% |
| M03    | Scanning Networks                 |     7 |     5.6% |
| M04    | Enumeration                       |     7 |     5.6% |
| M05    | Vulnerability Analysis            |     6 |     4.8% |
| M06    | System Hacking                    |     6 |     4.8% |
| M07    | Malware Threats                   |     7 |     5.6% |
| M08    | Sniffing                          |     6 |     4.8% |
| M09    | Social Engineering                |     6 |     4.8% |
| M10    | Denial-of-Service                 |     6 |     4.8% |
| M11    | Session Hijacking                 |     6 |     4.8% |
| M12    | Evading IDS, Firewalls, Honeypots |     6 |     4.8% |
| M13    | Hacking Web Servers               |     6 |     4.8% |
| M14    | Hacking Web Applications          |     6 |     4.8% |
| M15    | SQL Injection                     |     6 |     4.8% |
| M16    | Hacking Wireless Networks         |     6 |     4.8% |
| M17    | Hacking Mobile Platforms          |     6 |     4.8% |
| M18    | IoT and OT Hacking                |     6 |     4.8% |
| M19    | Cloud Computing                   |     6 |     4.8% |
| M20    | Cryptography                      |     6 |     4.8% |

這裡有一個很重要、也有點反直覺的結論：

**CEH v13 現在其實沒有某幾個單獨 Module「壓倒性地重要」。**

官方 v5 blueprint 把題數做得非常平均，大部分章節就是 6 題，M01–M04、M07 是 7 題左右。換句話說，如果有人跟你說「Web Application 佔 20–25%，所以只要狂讀 Web 就行」，那很可能混用了舊 blueprint、第三方統計，或者把整個 Domain 當成單一 Module。

真正差異比較明顯的是「Domain」。

官方 v5 的 Domain 比重約為：

1. Network and Perimeter Hacking：**24%，30 題**

   * M08 Sniffing
   * M09 Social Engineering
   * M10 DoS
   * M11 Session Hijacking
   * M12 Evading IDS/Firewall/Honeypots

2. Reconnaissance Techniques：**17%，21 題**

   * M02 Footprinting
   * M03 Scanning
   * M04 Enumeration

3. System Hacking Phases & Attack Techniques：**15%，19 題**

   * M05 Vulnerability Analysis
   * M06 System Hacking
   * M07 Malware

4. Web Application Hacking：**14%，18 題**

   * M13 Web Servers
   * M14 Web Applications
   * M15 SQL Injection

5. Mobile + IoT + OT：**10%，12 題**

   * M17 Mobile
   * M18 IoT/OT

6. M01 Introduction：**6%，7 題**

7. Wireless：**5%，6 題**

8. Cloud：**5%，6 題**

9. Cryptography：**5%，6 題**

官方 v5 blueprint 明確列出 Recon 為 21 題 / 17%；其中 M02、M03、M04 各 7 題。([EC-Council Certification Lookup][1]) System Hacking domain 則由 M05 約 6 題、M06 約 6 題、M07 約 7 題組成。([EC-Council Certification Lookup][1]) Network/Perimeter domain 約 30 題，其中 M08–M12 各約 6 題。([EC-Council Certification Lookup][1]) Web Application domain 約 18 題，M13、M14、M15 各約 6 題。([EC-Council Certification Lookup][1])

所以你可以把它理解成：

> **不是「哪一章特別多」，而是某些主題群加起來特別大。**

例如 M08 一章只有約 6 題，看起來不多。但 M08～M12 是同一個 Network & Perimeter domain，五章合計大約 **30 / 125 = 24%**。

同理：

> M02 + M03 + M04 ≈ 21 題
> M05 + M06 + M07 ≈ 19 題
> M08 + M09 + M10 + M11 + M12 ≈ 30 題
> M13 + M14 + M15 ≈ 18 題

光是 **M02～M15**，按照 blueprint 就大約：

$$
21 + 19 + 30 + 18 = 88
$$

也就是：

$$
\frac{88}{125}\approx70.4\%
$$

所以如果你的問題其實是：

> 「時間有限，我 CEH 應該先把哪裡讀熟？」

我會把複習優先順序設成：

**第一層：M02–M15**

尤其需要形成完整攻擊流程概念：

Recon → Scanning → Enumeration → Vulnerability Analysis → System Hacking → Malware → Sniffing → Social Engineering → DoS → Session Hijacking → Firewall/IDS evasion → Web Server → Web App → SQL Injection

這一大段本身就接近整張考卷 **70%**。

然後第二層才是：

**M17–M18：12 題**

最後再補：

**M01、M16、M19、M20：約 25 題。**

但有一點我要特別提醒你：這個「優先級」適合安排讀書時間，不代表低比重章節可以直接放棄。因為 CEH 125 題裡，每一個 Module 實際上仍有約 6–7 題，漏掉任何一章，都可能直接掉掉將近 5% 的總分。

至於你問的「網路考古題統計」，我也查到了大量第三方 CEH v13 practice banks，甚至有所謂 1,000+ 題的 dumps；但這些網站的章節分類、版本與真實性差異很大，有些甚至直接聲稱是 actual exam questions，因此我不建議拿它們當「真實考題分布」的證據。比較正規的免費練習網站也有，例如 CEHStudy 現在有 200 題、20 modules，每章各 10 題，但它是刻意平均配置，不能反推正式考試比重。([CEHStudy][2])

還有一個非常值得注意的版本差異。你如果 Google CEH 題數分布，會看到很多互相衝突的數字，原因是 **v4 → v5 blueprint 有明顯改動**。例如較舊 v4 的 Recon 曾經是 21%、Web Application 16%、Network/Perimeter 14%；現在 v5 則變成 Recon 17%、Web 14%、Network/Perimeter 24%。([EC-Council Certification Lookup][3])

因此，你現在準備 CEH v13，**不要用舊網頁看到的 21% Recon / 16% Web / 14% Network 那套配置當主要依據。**

EC-Council 目前也仍將 CEH 描述為 20 modules，Knowledge Exam 為 **125 道選擇題、4 小時**。([EC-Council][4])

如果你願意，我下一步可以直接替你做一個很實用的：

**「CEH v13 20章 × 官方題數 × 考古/模擬題常見程度 × 必背工具/port/command × 我建議投入時間」**

然後依你現在正在念的 **M05 Vulnerability Analysis** 開始，把 20 章排成「高、中、低複習優先度」，這會比單純看章節比重更適合你準備考試。

[1]: https://cert.eccouncil.org/wp-content/uploads/2024/04/CEH-Exam-Blueprint-v5.pdf?utm_source=chatgpt.com "<table id=\"e1\">"
[2]: https://cehstudy.com/?utm_source=chatgpt.com "CEH v13 Practice Questions & Flashcards | CEHStudy"
[3]: https://cert.eccouncil.org/wp-content/uploads/2024/02/CEH-Exam-Blueprint-v4.0.pdf?utm_source=chatgpt.com "CEH Exam Blueprint v4.0"
[4]: https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh-v13-north-america/?utm_source=chatgpt.com "Certified Ethical Hacker (CEH) | #1 Ethical Hacking Certification | EC-Council"
