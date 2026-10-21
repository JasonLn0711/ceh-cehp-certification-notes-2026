"""Original editable workshop teaching figures; all numbers are illustrative."""
from .mandarin_art import Canvas,PAPER,INK,WHITE,ACCENT,SOFT,GRAY

def build(scene):
    c=Canvas(scene['id']);kind=scene['kind'];labels=(scene.get('labels',[])+['','',''])[:3]
    chapter=int(scene['chapter_id'][1:]);sid=int(scene['id'][1:])
    if kind=='quiz':return []
    code=scene.get('code',[])
    if sid==3:
        c.document(395,455,'GPT／Claude：說明與草稿',0)
        c.device(865,455,'MATLAB：依實際資料執行',1,w=300)
        c.document(1335,455,'人：核對結果與證據',2)
        c.line(520,450,680,450,1,True,ACCENT,travel=True)
        c.line(1040,450,1210,450,2,True,ACCENT,travel=True)
        c.label(865,760,'保留程式、輸入與本次輸出，逐步檢查',2,w=1250)
    elif sid==11:
        c.label(430,330,'全部資料',0,w=430)
        c.line(430,375,430,480,0,True,ACCENT)
        c.label(430,540,'80% 訓練資料',0,w=500)
        c.line(700,335,1230,335,1,True,ACCENT)
        c.label(1230,410,'20% 測試資料',1,w=500)
        c.label(430,740,'建立模型與縮放參數',1,w=540)
        c.line(430,590,430,690,1,True,ACCENT)
        c.line(730,740,1230,740,2,True,ACCENT)
        c.line(1230,455,1230,690,2,True,ACCENT)
        c.label(1230,740,'最後評估',2,w=420)
    elif sid==37:
        pairs=[('量測面積','像素數 × 每格面積'),('填滿比例','圖形面積 ÷ 外接矩形'),('面積比例','圖形面積 ÷ 整張影像'),('測試準確率','判對筆數 ÷ 測試總筆數')]
        for i,(name,value) in enumerate(pairs):
            y=300+i*120;c.box(200,y,1250,105,min(i,2),WHITE,GRAY)
            c.text(420,y+28,name,min(i,2),34,400,True)
            c.text(1020,y+28,value,min(i,2),34,780)
    elif sid==34:
        c.document(405,420,'img001.png',0);c.document(1110,420,'img999.png',0)
        c.label(405,650,'相同解碼像素',1,w=500);c.label(1110,650,'相同解碼像素',1,w=500)
        c.line(680,650,840,650,1,True,ACCENT)
        c.text(800,780,'改名仍會重複；近似圖另需檢查',2,36,1250,True)
    elif sid==14:
        c.text(700,280,'示意：全部預測正常',0,36,1050,True)
        for i,t in enumerate(['預測正常 0','預測需檢查 1']):c.text(800+i*420,360,t,0,32,400,True)
        for r,t in enumerate(['真實正常 0','真實需檢查 1']):
            c.text(380,470+r*130,t,r,32,400,True)
            for k,val in enumerate([8,0] if r==0 else [2,0]):
                c.box(610+k*420,440+r*130,400,110,r,SOFT if r==k else WHITE,GRAY)
                c.text(810+k*420,465+r*130,str(val),r,43,350,True)
        c.text(850,770,'準確率 8/10 = 80%    正類召回率 0/2 = 0%',2,34,1350,True)
    elif code:
        c.box(185,290,1320,355,0,WHITE,INK)
        c.text(225,312,'MATLAB｜關鍵片段',0,30,1200,True,anchor='start')
        c.line(220,365,1470,365,0,color=GRAY)
        for i,line in enumerate(code[:4]):
            c.text(225,390+i*53,line,min(i,2),29,1240,anchor='start');c.objects[-1]['technical']=True
        for i,label in enumerate(labels):
            c.label(410+i*450,745,label,min(i,2),w=420)
    elif sid==26:
        rows=[['路徑','正確類別'],['train/img001.png','circle'],['train/img002.png','square'],['test/img109.png','triangle']]
        for r,row in enumerate(rows):
            for k,val in enumerate(row):
                w=780 if k==0 else 470;x=200 if k==0 else 980
                c.box(x,310+r*100,w,100,min(r,2),SOFT if r==0 else WHITE,GRAY,1)
                c.text(x+w/2,340+r*100,val,min(r,2),33,w-40,r==0)
        c.text(825,760,'路徑找檔案；標籤留作訓練或評估',2,35,1250,True)
    elif sid==32:
        for i,(x,label) in enumerate([(390,'圓形'),(800,'圓形'),(1210,'方形')]):
            if i<2:c.circle(x,440,90,min(i,1),SOFT)
            else:c.box(x-90,350,180,180,1,ACCENT)
            c.text(x,565,label,min(i,1),36,300,True)
        c.label(800,740,'三位鄰居投票：圓形獲得兩票',1,w=1120)
    elif kind=='island_pixels' or chapter in [4,5]:
        # Same filled object and contour expose region/edge distinction.
        cells={(r,k) for r in range(2,7) for k in range(2,7)}
        for r in range(9):
            for k in range(10):
                inside=(r,k) in cells
                edge=inside and any((r+dr,k+dk) not in cells for dr,dk in [(1,0),(-1,0),(0,1),(0,-1)])
                c.box(220+k*45,325+r*45,44,44,0,(WHITE if inside else INK) if sid==18 else (SOFT if inside else WHITE),GRAY,0)
                if edge and sid!=18:c.box(220+k*45,325+r*45,44,44,1,ACCENT,INK,0)
        c.text(445,755,'白色位置為真；黑色為假' if sid==18 else '區域填滿／輪廓描邊',2,32,550,True)
        for i,label in enumerate(labels):c.label(1120,365+i*170,label,i,w=690)
        c.line(700,520,755,520,1,True,ACCENT)
    elif kind=='island_table' or chapter==2:
        rows=scene.get('rows') or [['樣本','溫度','振動','電流','標籤'],['DEV01','68','3.1','7.8','0'],['DEV02','79','5.2','9.4','1'],['DEV03','65','2.4','7.1','0']]
        for r,row in enumerate(rows[:4]):
            for k,val in enumerate(row[:5]):
                c.box(195+k*250,315+r*95,250,95,min(r,2),SOFT if r==0 else WHITE,GRAY,1)
                c.text(320+k*250,341+r*95,str(val),min(r,2),31,235,r==0)
        for i,label in enumerate(labels):c.text(400+i*460,765,label,i,31,430,True)
    elif chapter==3 and kind!='island_flow':
        c.text(490,280,'示意：100筆分成兩部分',0,36,650,True)
        for i in range(10):
            c.box(220+i*100,370,80,110,0 if i<8 else 1,SOFT if i<8 else ACCENT)
            c.text(260+i*100,402,'10',0 if i<8 else 1,32,75)
        c.text(610,510,'80筆：訓練',0,36,650,True);c.text(1120,510,'20筆：測試',1,36,400,True)
        for i,label in enumerate(labels):c.label(420+i*460,720,label,i,w=430)
    elif chapter in [6,7] and kind!='island_flow':
        c.box(210,290,710,460,0,WHITE,GRAY)
        c.line(285,680,835,680,0,True);c.line(285,680,285,340,0,True)
        c.text(600,705,'縮放後的特徵（示意）',0,28,600)
        for i,(x,y) in enumerate([(400,540),(470,490),(440,600),(690,405),(735,470),(775,380)]):
            if i<3:c.circle(x,y,20,0,SOFT)
            else:c.box(x-18,y-18,36,36,1,ACCENT,INK,1)
        c.circle(500,550,15,2,INK)
        for x,y in [(400,540),(470,490),(440,600)]:c.line(500,550,x,y,2,color=ACCENT,dash=True)
        for i,label in enumerate(labels):c.label(1240,365+i*165,label,i,w=530)
    elif kind=='island_flow':
        for i,label in enumerate(labels):
            x=415+i*460;c.document(x,460,label,i)
            if i<2:c.line(x+115,455,x+325,455,i+1,True,ACCENT,travel=True)
        c.box(250,720,1260,85,2,SOFT,GRAY)
        c.text(880,740,'先看輸入，再看處理，最後核對輸出',2,34,1200,True)
    else:
        # Workbench: distinct physical materials, not a repeated dashboard.
        c.line(210,665,1520,665,0,color=INK)
        for i,label in enumerate(labels):
            x=410+i*460
            if i==0:
                c.document(x,450,label,i)
            elif i==1:
                c.box(x-115,345,230,230,i,WHITE)
                for r in range(4):
                    for k in range(4):c.box(x-85+k*44,375+r*44,38,38,i,SOFT if r+k>2 else WHITE,GRAY,0)
                c.text(x,600,label,i,32,410)
            else:
                c.circle(x-42,430,52,i,SOFT);c.box(x+20,470,85,85,i,ACCENT)
                c.text(x,600,label,i,32,410)
        c.text(865,745,'小島創作所｜開放日前的工作桌',2,35,1250,True)
    return c.objects
