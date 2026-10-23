# M04-01 revision 2：教學校訂與覆蓋

保留穩定ID M04-01與原公開網址，深化同一概念。第一版完整原文繼續保存在source/2026-10-23-one-concept/M04-01-teaching.md，原始詳細資料由既定私人來源保管。網站正式教材正本為kairos-learning/content/concepts/m04-01.json。

| 原資料範圍 | 公開呈現與校訂 |
| --- | --- |
| 流程位置與辦公大樓類比 | 第一節，保留偵察／掃描／列舉關係與流程可重疊 |
| Port／Service／Protocol／Resource、445、SMB、NetShareEnum | 第二節表格與合成案例；Port定義包含IP與傳輸協定；API 0/1細節折疊，群組資格與匿名可查分開 |
| Authentication／Authorization、Share／NTFS、ABE | 第三節，權限圖以完成驗證為假設；ABE僅控制共享內檔案／資料夾顯示；拒絕原因依回應與日誌定位 |
| nmap／smbclient、證據矩陣 | 第四節，分開共享名稱、ls、get；改互動輸入密碼；文件IP換授權主機；全新本機目錄保存合成檔 |
| 風險、T1135／T1087、5140／5145 | 第五節，政策與敏感度支撐風險判斷；先確認稽核，5140不是逐檔完整讀取紀錄，5145失敗針對共享層 |
| 跨協定地圖、後續學習 | 第六節，保留SMB／NetBIOS、LDAP／AD、DNS、SNMP、NFS、SMTP並補RPC；12核心是教學安排；下一課DNS，AD為延伸 |
| 三題與解析 | 第七節測驗；保留原三題、答案B/C/B及逐選項可展開教材解析；實際Q&A維持待補 |

公開版移除favicon、image、+1、utm追蹤及沒有功能的提交文字，使用表格、程式碼與進階細節折疊減少閱讀負擔。原始細節沒有當成本人回答、實測結果或理解確認；本輪未執行掃描。

## 技術來源與審核

主對話提供的獨立技術審核已納入，並核對官方來源：

- [Nmap埠狀態](https://nmap.org/book/man-port-scanning-basics.html)、[服務辨識](https://nmap.org/book/man-version-detection.html)
- [NetShareEnum](https://learn.microsoft.com/en-us/windows/win32/api/lmshare/nf-lmshare-netshareenum)、[SMB拒絕排查](https://learn.microsoft.com/en-us/troubleshoot/windows-client/networking/access-denied-access-smb-file-share)
- [SMB ABE](https://learn.microsoft.com/en-us/powershell/module/smbshare/set-smbshare?view=windowsserver2025-ps)
- [Samba手冊](https://www.samba.org/samba/docs/current/man-html/smbclient.1.html)：-c隱含-N；get複製到本機。
- [5140](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-5140)、[5145](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-5145)
- [T1135](https://attack.mitre.org/techniques/T1135/)、[T1087](https://attack.mitre.org/techniques/T1087/)、[RFC5737](https://www.rfc-editor.org/rfc/rfc5737)
- 官方範圍沿用既有[CEH Blueprint v5.0](https://cert.eccouncil.org/wp-content/uploads/2024/04/CEH-Exam-Blueprint-v5.pdf)，不因審核參考含舊版v4連結而降版。
