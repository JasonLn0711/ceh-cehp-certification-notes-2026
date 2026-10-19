"""Editable geometry for the He-Ri office story, rendered as SVG and native PPTX shapes."""
import math
from .common import read

PAPER='#F0EBE4';INK='#292421';WHITE='#FFFAF3';ACCENT='#C8755D';SOFT='#F2D4B7';GRAY='#B8B0A9';GOLD='#E9B94D'

class Canvas:
    def __init__(self,sid):self.sid=sid;self.objects=[]
    def add(self,kind,phase=0,**data):
        ident=f'{self.sid}-obj-{len(self.objects):03}'
        self.objects.append(dict(id=ident,kind=kind,phase=phase,**data));return ident
    def box(self,x,y,w,h,phase=0,fill=WHITE,stroke=INK,rx=12):return self.add('rect',phase,x=x,y=y,w=w,h=h,fill=fill,stroke=stroke,rx=rx)
    def text(self,x,y,text,phase=0,size=36,w=500,bold=False,color=INK,anchor='middle'):
        return self.add('text',phase,x=x,y=y,text=text,size=size,w=w,bold=bold,color=color,anchor=anchor)
    def circle(self,x,y,r,phase=0,fill=WHITE,stroke=INK):return self.add('ellipse',phase,x=x-r,y=y-r,w=2*r,h=2*r,fill=fill,stroke=stroke)
    def line(self,x1,y1,x2,y2,phase=0,arrow=False,color=INK,dash=False,travel=False):
        return self.add('line',phase,x1=x1,y1=y1,x2=x2,y2=y2,arrow=arrow,color=color,dash=dash,travel=travel)
    def label(self,x,y,text,phase=0,w=380,fill=SOFT):
        self.box(x-w/2,y-35,w,76,phase,fill);self.text(x,y-3,text,phase,34,w-30,True)
    def device(self,x,y,label,phase=0,w=230):
        self.box(x-w/2,y-80,w,140,phase);self.box(x-w/2+18,y-62,w-36,98,phase,PAPER,GRAY,3)
        self.line(x-40,y+80,x+40,y+80,phase);self.line(x,y+60,x,y+80,phase)
        self.text(x,y+110,label,phase,32,w+80)
    def server(self,x,y,label,phase=0):
        self.box(x-85,y-105,170,210,phase)
        for i in range(3):self.box(x-65,y-85+i*57,130,42,phase,PAPER,GRAY,4);self.circle(x+43,y-64+i*57,5,phase,ACCENT)
        self.text(x,y+135,label,phase,32,330)
    def chip(self,x,y,label,phase=0):
        self.box(x-110,y-85,220,170,phase,SOFT)
        for i in range(6):
            dx=x-85+i*34;self.line(dx,y-105,dx,y-85,phase);self.line(dx,y+85,dx,y+105,phase)
        self.text(x,y-8,label,phase,44,200,True)
    def lock(self,x,y,phase=0):
        self.circle(x,y-30,48,phase,PAPER);self.box(x-70,y-30,140,110,phase,SOFT);self.circle(x,y+20,10,phase,INK)
    def memory(self,x,y,label,phase=0,filled=6):
        self.box(x-225,y-65,450,130,phase,SOFT)
        for i in range(8):
            self.box(x-205+i*51,y-43,38,70,phase,INK if i<filled else WHITE,INK,3)
            self.line(x-198+i*51,y+65,x-198+i*51,y+85,phase)
        self.text(x,y+115,label,phase,34,480)
    def document(self,x,y,label,phase=0):
        self.box(x-90,y-105,180,210,phase)
        for i in range(4):self.line(x-60,y-60+i*35,x+55,y-60+i*35,phase,color=GRAY)
        self.text(x,y+140,label,phase,32,340)

def build(scene):
    c=Canvas(scene['id']);k=scene['kind'];labels=scene['labels']
    if k=='office':
        c.box(180,290,1280,475,0,PAPER,GRAY);c.text(820,315,'禾日選物・辦公室',0,38,1000,True)
        c.device(415,510,'小晴｜客服',0);c.device(870,510,'小安｜帳務',1);c.server(1250,520,'訂單伺服器',2)
        c.line(545,520,740,520,1,True,ACCENT,travel=True);c.line(1000,520,1145,520,2,True,ACCENT,travel=True)
        c.text(820,720,'設備合作，完成同一天的工作',2,36,1100)
    elif k in {'inference','https_limit','ownership'}:
        c.device(410,490,'觀察到的畫面／紀錄',0,w=330)
        for i,(t,x) in enumerate(zip(labels,[850,850,850])):
            c.box(x-160,300+i*160,650,120,min(i,2),WHITE if i!=1 else SOFT)
            c.text(x+165,328+i*160,t,min(i,2),36,590,True)
        c.line(590,490,670,490,1,True,ACCENT,travel=True)
        c.text(420,730,'一項觀察，可能有不同解釋',2,32,510)
    elif k=='hdd':
        c.box(240,285,660,480,0,WHITE);c.circle(530,520,190,0,PAPER)
        for r in [55,95,135,175]:c.circle(530,520,r,0,fill='none',stroke=GRAY)
        c.circle(530,520,24,0,SOFT)
        arm=c.line(820,690,575,470,1,color=ACCENT);c.objects[-1]['motion']='needle'
        for i,l in enumerate(labels):c.label(1230,355+i*150,l,min(i,2),w=420)
        c.text(530,785,'HDD｜機械讀取',2,36,600,True)
    elif k=='ssd':
        c.box(250,310,730,420,0,SOFT)
        for row in range(2):
            for col in range(4):c.box(300+col*155,360+row*130,120,90,row,INK,INK,5)
        c.chip(1240,460,'控制器',1)
        c.line(990,470,1120,470,1,True,ACCENT,travel=True)
        c.label(1220,665,'無旋轉碟片／移動讀寫頭',2,w=530)
        c.text(620,780,'SSD｜快閃記憶體',2,38,730,True)
    elif k in {'deletion','overwrite','trim'}:
        c.document(390,450,'報價單.pdf',0)
        c.box(650,285,840,155,0,WHITE);c.text(1070,320,'檔案系統索引',0,38,760,True)
        c.text(1070,375,'檔名 → 資料所在位置',0,34,760)
        c.line(490,430,640,365,0,True,ACCENT,travel=True)
        c.text(1060,490,'儲存空間',1,34,750)
        for i in range(10):
            c.box(670+i*77,545,67,100,1,SOFT if i<6 else WHITE,INK,4)
            c.text(703+i*77,578,str(i+1),1,26,65)
        if k=='deletion':
            c.line(700,395,1430,395,1,color=ACCENT)
            c.label(1060,740,'索引變更 ≠ 內容必定逐位元清除',2,w=760)
        elif k=='overwrite':
            for i in [2,3,4]:c.box(670+i*77,545,67,100,2,ACCENT,INK,4)
            c.label(1060,740,'新資料可能覆寫原本的內容',2,w=700)
        else:
            c.chip(390,755,'控制器',2)
            c.line(1000,650,520,755,2,True,ACCENT,travel=True)
            c.label(1120,740,'TRIM 與垃圾回收影響恢復條件',2,w=680)
    elif k in {'file_states','state_comparison'}:
        for i,(x,l) in enumerate(zip([410,900,1390],labels)):
            c.document(x,465,l,i)
            c.label(x,735,['已保存內容','依條件判斷','目前工作狀態'][i],i,w=400)
        c.line(540,440,760,440,1,True,ACCENT);c.line(1030,440,1250,440,2,True,ACCENT)
    elif k=='cpu':
        c.document(350,490,'程式指令',0);c.chip(880,490,'CPU',1);c.label(1400,490,'運算結果',2,w=300)
        c.line(470,490,740,490,1,True,ACCENT,travel=True);c.line(1020,490,1220,490,2,True,ACCENT,travel=True)
        c.label(880,740,'執行指令，不是長期保存所有檔案',2,w=1050)
    elif k=='ram':
        c.memory(860,420,'RAM｜使用中的程式與資料',0,3)
        for i in range(4):
            c.box(470+i*220,640,185,100,1 if i<2 else 2,SOFT)
            c.text(562+i*220,675,['程式碼','訂單資料','搜尋結果','介面狀態'][i],1 if i<2 else 2,32,180)
            c.line(562+i*220,635,650+i*130,515,1 if i<2 else 2,True,ACCENT)
        c.label(860,280,'一般 RAM 需要供電維持內容',2,w=900)
    elif k=='os':
        c.label(860,340,'作業系統｜管理與協調資源',0,w=900)
        c.memory(460,590,'RAM',1,5);c.chip(1050,590,'CPU',1);c.document(1430,590,'SSD 檔案',2)
        for x in [460,1050,1430]:c.line(860,385,x,465,1 if x<1400 else 2,True,ACCENT)
    elif k=='dataflow':
        c.document(340,485,'SSD｜程式與訂單',0);c.memory(850,490,'RAM｜目前工作',1,5);c.chip(1410,490,'CPU',2)
        c.line(470,470,600,470,1,True,ACCENT,travel=True);c.line(1100,470,1270,470,2,True,ACCENT,travel=True)
        c.line(1280,695,470,695,2,True,ACCENT,travel=True);c.text(850,745,'修改成功保存後，再留到下一次使用',2,34,1300)
    elif k in {'performance','performance_compare'}:
        c.text(395,310,'工作管理員概念圖',0,40,550,True)
        for i,(label,value) in enumerate(zip(['CPU 負載','記憶體壓力','磁碟活動'],[.86,.94,.73])):
            y=410+i*135;c.text(350,y,label,min(i,2),36,320)
            c.box(570,y-20,780,65,min(i,2),WHITE,GRAY,4)
            bar=c.box(575,y-15,770*value,55,min(i,2),ACCENT if i!=1 else GOLD,INK,3)
            c.objects[-1]['motion']='bar'
        c.text(940,830,'示意負載，需對照當時執行的工作',2,34,1300)
    elif k=='osi':
        for i,l in enumerate(labels):
            y=285+(6-i)*73;c.box(350,y,1020,62,min(i//3,2),SOFT if i in [0,1,2,3,6] else WHITE)
            c.text(860,y+12,l,min(i//3,2),36,930,True)
        c.line(1450,765,1450,300,1,True,ACCENT,travel=True)
        c.text(1550,470,'低\n到\n高',2,36,100)
    elif k in {'physical','mac','ip','switch_router','network_path','lan'}:
        c.device(350,490,'客服電腦',0)
        if k=='physical':
            c.device(1330,490,'另一端設備',1);c.line(500,490,1180,490,1,color=ACCENT,travel=True)
            for i in range(14):c.line(560+i*35,570,577+i*35,530,2,color=INK)
            c.label(850,740,'第一層｜媒介與訊號',2,w=720)
        elif k=='mac':
            c.box(720,400,280,175,1,SOFT);c.text(860,450,'交換器',1,42,250,True)
            c.device(1380,490,'目的介面 MAC B',2)
            c.line(500,490,710,490,1,True,ACCENT,travel=True);c.line(1010,490,1230,490,2,True,ACCENT,travel=True)
            c.label(850,740,'MAC A → 交換器查表 → MAC B',2,w=1020)
        elif k=='switch_router':
            # Both devices are visible as distinct functional roles, not a router-only shorthand.
            c.box(620,410,230,160,0,SOFT);c.text(735,450,'交換器',0,38,220,True)
            c.box(1060,410,230,160,1,SOFT);c.text(1175,450,'路由器',1,38,220,True)
            c.server(1530,480,'另一個網路',2)
            c.line(490,490,610,490,0,True,ACCENT,travel=True)
            c.line(860,490,1050,490,1,True,ACCENT,travel=True)
            c.line(1300,490,1420,490,2,True,ACCENT,travel=True)
            c.text(735,640,'MAC／訊框',1,34,350);c.text(1175,640,'IP／封包',2,34,350)
            c.label(950,785,'第三層交換器也可能具備路由能力',2,w=1150)
        else:
            c.box(720,400,280,175,1,SOFT);c.text(860,440,'路由／閘道',1,38,260,True)
            c.server(1360,490,'另一個網路',2)
            c.line(500,490,710,490,1,True,ACCENT,travel=True);c.line(1010,490,1240,490,2,True,ACCENT,travel=True)
            c.label(860,740,{'ip':'目的 IP 與路由資訊','switch_router':'第二層轉送／第三層路由','network_path':'位址、路由、存取規則與服務','lan':'公司 LAN ↔ Internet'}[k],2,w=1050)
    elif k=='ports':
        c.device(350,490,'來源端點',0)
        c.box(820,285,630,490,1,WHITE);c.text(1135,315,'目的 IP：203.0.113.20',1,36,570,True)
        for i,t in enumerate(['TCP 443｜常見 HTTPS','TCP 80｜常見 HTTP','其他通訊端點']):
            c.label(1135,435+i*130,t,1 if i==0 else 2,w=530)
        c.line(510,490,800,435,1,True,ACCENT,travel=True)
        c.text(390,745,'連接埠協助區分通訊',2,34,480)
    elif k=='upper_layers':
        for i,l in enumerate(labels):
            c.box(300,300+(2-i)*160,1140,120,i,SOFT if i==2 else WHITE)
            c.text(870,335+(2-i)*160,l,i,40,1050,True)
        c.line(1510,745,1510,335,2,True,ACCENT)
    elif k in {'vlan','inter_vlan'}:
        c.box(195,340,590,420,0,SOFT);c.box(880,340,650,420,1,WHITE)
        c.text(490,365,'VLAN 10｜客服',0,38,540,True);c.text(1205,365,'VLAN 20｜管理與訂單',1,38,590,True)
        c.device(490,530,'客服電腦',0);c.device(1040,550,'管理電腦',1,w=170);c.server(1355,550,'訂單伺服器',1)
        if k=='inter_vlan':
            c.label(850,275,'第三層路由＋允許規則',2,w=650)
            c.line(600,465,700,310,2,True,ACCENT,travel=True);c.line(1020,310,1300,420,2,True,ACCENT,travel=True)
        else:c.label(850,820,'同一套實體網路，不同邏輯群組',2,w=1180)
    elif k=='nat':
        c.device(350,385,'小晴的電腦',0);c.device(350,680,'小安的電腦',1)
        c.box(680,325,490,420,1,SOFT);c.text(925,355,'NAT 對應',1,44,440,True)
        c.text(925,460,'內部來源 A ↔ 對外連線 A',1,30,450);c.text(925,580,'內部來源 B ↔ 對外連線 B',2,30,450)
        c.server(1440,500,'共用公網 IP',2)
        c.line(500,385,670,450,1,True,ACCENT,travel=True);c.line(500,680,670,600,2,True,ACCENT,travel=True);c.line(1180,500,1330,500,2,True,ACCENT,travel=True)
        c.text(935,810,'相同公網 IP ≠ 同一部電腦',2,40,1200,True)
    elif k in {'volatile','unlock','shutdown'}:
        if k=='unlock':
            c.document(430,470,'儲存的加密檔案',0);c.lock(920,480,1);c.device(1380,470,'目前已解鎖狀態',2)
            c.line(550,470,800,470,1,True,ACCENT);c.line(1030,470,1220,470,2,True,ACCENT)
            c.label(880,750,'檔案存在，與目前可開啟狀態不同',2,w=1200)
        elif k=='shutdown':
            c.device(380,490,'仍在運作的電腦',0)
            c.label(1080,370,'關機：工作狀態可能結束',1,w=760)
            c.label(1080,590,'操作：可能新增或修改資料',2,w=760)
            c.line(530,455,675,370,1,True,ACCENT);c.line(530,525,675,590,2,True,ACCENT)
            c.text(1000,800,'先理解目前狀態與處理目標',2,36,1100)
        else:
            for i,(x,l) in enumerate(zip([420,900,1380],labels)):
                c.device(x,440,l,i,w=310);c.memory(x,680,'使用中的狀態',i,4)
    elif k in {'address_txid','keys','hardware_wallet','wallet_summary'}:
        if k=='address_txid':
            c.document(450,460,'教學地址 A',0);c.document(1100,460,'示例交易 T01',1)
            c.label(450,740,'提供收款資訊',1,w=500);c.label(1100,740,'查找相應交易',2,w=500)
            c.text(850,280,'模擬字串，非實際收款或鏈上交易',2,34,1300)
        elif k=='keys':
            c.lock(400,480,0);c.label(400,720,'私鑰保護',0,w=400)
            c.document(910,480,'待授權的交易',1);c.label(1430,480,'有效簽章',2,w=320)
            c.line(520,480,780,480,1,True,ACCENT);c.line(1030,480,1230,480,2,True,ACCENT,travel=True)
            c.text(920,790,'地址／交易識別碼不等於秘密金鑰',2,36,1250)
        elif k=='hardware_wallet':
            c.device(350,480,'交易軟體',0);c.box(740,350,300,300,1,SOFT);c.lock(890,470,1)
            c.text(890,690,'金鑰留在裝置內',1,34,460,True);c.server(1390,480,'鏈上交易紀錄',2)
            c.line(505,450,720,450,1,True,ACCENT,travel=True);c.line(1060,450,1270,450,2,True,ACCENT,travel=True)
            c.text(1160,350,'簽署結果',2,32,250)
            c.text(860,815,'硬體錢包保護金鑰，不是把比特幣裝進設備',2,36,1400)
        else:
            for i,(x,y,l) in enumerate([(440,380,'地址｜收款資訊'),(1170,380,'交易識別碼｜查交易'),(440,680,'金鑰｜交易授權'),(1170,680,'裝置｜保護與簽署')]):
                c.label(x,y,l,min(i,2),w=620)
            c.line(440,425,440,630,2,False,GRAY,dash=True);c.line(1170,425,1170,630,2,False,GRAY,dash=True)
    elif k=='capstone':
        c.box(230,280,1240,535,0,WHITE)
        for i,t in enumerate(['觀察：目前確定知道什麼？','原理：設備與資料如何運作？','資訊限制：還缺什麼？','下一步：如何支持判斷？']):
            phase=min(i,2);c.box(285,325+i*110,45,45,phase,SOFT);c.text(370,325+i*110,t,phase,38,1000,anchor='start')
    elif k=='quiz':
        # Actual question geometry is compiled after measured audio is available.
        return []
    else:raise ValueError('Missing scene-specific art: '+k)
    return c.objects
