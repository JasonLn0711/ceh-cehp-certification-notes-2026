"""Original editable teaching diagrams; never labelled as MATLAB output."""
from html import escape

PAPER='#F0EBE4'; INK='#292421'; ACCENT='#C8755D'; SOFT='#F2D4B7'; RED='#B72D2D'
LABELS={
 'overview':'今天做三個案例','workflow':'先看完整流程','check':'結果要回到檔案核對',
 'folder':'先找對資料夾','upload':'整個資料夾一起上傳','filebundle':'把證據一起留好',
 'command':'在指令視窗執行','table':'一列是一筆設備資料','features':'提供模型判斷的資訊',
 'feature_scope':'先看清楚比較的範圍','split':'訓練與測試分開','disjoint':'確認兩組沒有重複',
 'standardize':'沿用訓練組的設定','logistic':'用訓練資料調整模型','threshold':'估計值再轉成類別',
 'confusion':'先讀類別，再看格子','recall':'需要檢查的，有找出來嗎',
 'prediction':'逐筆對照答案與預測','report':'把做法和結果說清楚','download':'下載同一輪的結果',
 'target':'先確認要量哪一塊','channels':'一個像素，三個通道','background':'背景也含有紅色數值',
 'red_threshold':'先看紅色數值','red_dominance':'再看紅色的相對差距','component':'保留上下左右相連的區域',
 'mask':'白色保留，黑色排除','target_mask':'回頭對照原圖的位置','error':'先保留完整錯誤訊息',
 'contour':'沿著目標描出邊界','area_boundary':'面積要數整塊區域','pixels':'每個小格子都是像素',
 'formula':'像素數 × 邊長的平方','scale':'尺度改變，要重新換算',
 'train_test':'圖庫先分成兩組','manifest':'清冊連到圖片與答案','vote':'三個鄰居，依標籤投票',
 'distance':'比較的是特徵距離','help':'問題說清楚，方便一起查',
 'area_frame':'分母：整張影像','circularity':'接近圓形的程度','conditions':'兩個條件同時成立',
}

def text(x,y,value,size=28,anchor='middle',color=INK):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{color}">{escape(str(value))}</text>'

def box(x,y,w,h,label='',fill='#FFFAF3',stroke=INK):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="3"/>'+ (text(x+w/2,y+h/2+10,label) if label else '')

def arrow(x1,y1,x2,y2):
    import math
    a=math.atan2(y2-y1,x2-x1)
    d=f'M{x1} {y1} L{x2} {y2} M{x2-14*math.cos(a-.5):.2f} {y2-14*math.sin(a-.5):.2f} L{x2} {y2} L{x2-14*math.cos(a+.5):.2f} {y2-14*math.sin(a+.5):.2f}'
    return f'<path class="draw" d="{d}" stroke="{RED}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'

def shape(kind,x,y,r=42,fill=SOFT):
    if kind=='circle':return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{INK}" stroke-width="3"/>'
    if kind=='square':return f'<rect x="{x-r}" y="{y-r}" width="{r*2}" height="{r*2}" fill="{fill}" stroke="{INK}" stroke-width="3"/>'
    return f'<polygon points="{x},{y-r} {x+r},{y+r} {x-r},{y+r}" fill="{fill}" stroke="{INK}" stroke-width="3"/>'

def diagram(kind,case_id=None):
    if kind not in LABELS:raise ValueError('Unknown teaching diagram: '+kind)
    parts=[]
    if kind in {'target','mask','contour','target_mask','background','area_boundary'}:
        mask=kind=='mask';parts.append(box(45,70,430,270,fill=INK if mask else '#F2EFE5'))
        polygon='130,120 355,112 390,245 312,285 148,255'
        parts.append(f'<polygon points="{polygon}" fill="{"#FFFAF3" if mask else "#CD7D73"}" stroke="{RED if kind in {"contour","area_boundary"} else "none"}" stroke-width="6"/>')
        if not mask:parts.append('<rect x="65" y="95" width="45" height="35" fill="#366E92"/>')
        if kind=='contour':parts.append(f'<path class="draw" d="M130 120 L355 112 L390 245 L312 285 L148 255 Z" stroke="{RED}" stroke-width="6" fill="none"/>')
        parts.append(arrow(440,45,355,112) if kind!='background' else arrow(440,45,440,95))
        parts.append(text(260,390,{'mask':'白色：目標區域','contour':'紅線：目標邊界','area_boundary':'區域與邊界，分開核對','background':'明亮背景也有 R 通道'}.get(kind,'依教材形狀重繪｜非執行結果'),25))
    elif kind in {'pixels','formula','scale'}:
        if kind=='formula':
            parts.extend([text(260,110,'區域像素數',38),text(260,175,'×',38),box(100,205,320,75,'每像素邊長²',SOFT),arrow(260,290,260,330),text(260,385,'面積（平方毫米）',32)])
        else:
            for row in range(5):
                for col in range(7):parts.append(f'<rect x="{78+52*col}" y="{75+52*row}" width="52" height="52" fill="{SOFT if 1<=col<=5 and 1<=row<=3 else "#FFFAF3"}" stroke="#8C8075" stroke-width="2"/>')
            parts.extend([arrow(440,55,365,105),text(260,385,'1 mm × 1 mm = 1 mm²',30)])
    elif kind in {'channels','red_threshold','red_dominance'}:
        labels=['紅 R','綠 G','藍 B']; colors=['#B72D2D','#547052','#366E92']; widths=[300,170,150]
        for i,(label,c,w) in enumerate(zip(labels,colors,widths)):
            parts.extend([text(85,110+i*95,label,28),f'<rect class="bar" x="150" y="{75+i*95}" width="{w}" height="48" rx="5" fill="{c}"/>'])
        caption={'channels':'通道概念示意','red_threshold':'R ≥ 170','red_dominance':'R − max(G, B) ≥ 55'}[kind]
        parts.append(text(260,395,caption,29));parts.append(arrow(475,35,400,80))
    elif kind=='component':
        for r in range(5):
            for c in range(7):
                keep=(1<=r<=3 and 2<=c<=4) or (r==0 and c==0)
                parts.append(f'<rect x="{80+c*50}" y="{75+r*50}" width="46" height="46" fill="{SOFT if keep else "#FFFAF3"}" stroke="{INK}" stroke-width="2"/>')
        parts.extend([arrow(390,40,305,150),text(260,390,'上下左右相連，選最大一塊',26)])
    elif kind=='conditions':
        parts.extend([box(50,60,420,90,'R ≥ 170',SOFT),text(260,215,'而且',34),box(30,265,460,90,'R − max(G, B) ≥ 55'),arrow(460,180,430,260)])
    elif kind=='circularity':
        parts.extend([shape('circle',260,190,110),text(260,355,'結合面積與邊界資訊',32),arrow(430,60,350,125)])
    elif kind in {'table','features','feature_scope','area_frame'}:
        if case_id=='case3':
            parts.append(shape('circle',260,175,95))
            if kind=='feature_scope':parts.append('<rect x="145" y="60" width="230" height="230" fill="none" stroke="#B72D2D" stroke-width="4"/>')
            else:parts.append('<rect x="70" y="40" width="380" height="270" fill="none" stroke="#B72D2D" stroke-width="4"/>')
            parts.extend([text(260,360,'圖形面積 ÷ 比較範圍',30),text(260,405,'看清楚分母是哪一塊',26)])
        else:
            labels=['ID','溫度','振動','電流','答案']
            for r in range(4):
                for c in range(5):parts.append(box(20+c*96,65+r*70,96,70,labels[c] if r==0 else ('•' if c in [1,2,3] else ('A' if c==0 else '0/1')),SOFT if c in [1,2,3] else '#FFFAF3'))
            parts.extend([arrow(270,25,270,65),text(260,400,'識別碼、特徵、答案，各有用途',25)])
    elif kind in {'split','train_test','disjoint','standardize'}:
        parts.extend([box(25,90,210,180,'訓練 Train',SOFT),box(285,90,210,180,'測試 Test')])
        if kind=='standardize':parts.extend([arrow(150,300,380,300),text(260,350,'同一組平均值與標準差',27)])
        elif kind=='disjoint':parts.extend([text(260,330,'確認交集為空',34),text(260,380,'路徑與內容分別檢查',26)])
        else:parts.extend([text(260,330,'先分開，再處理',34),text(260,380,'示意｜數量以輸出檔核對',25)])
    elif kind in {'vote','distance'}:
        parts.extend([shape('triangle',260,90,45),arrow(260,140,260,185)])
        for k,x in zip(['circle','circle','square'],[90,260,430]):parts.append(shape(k,x,255,45))
        parts.extend([text(260,355,'三個鄰居：兩票圓形',31),text(260,400,'投票示意｜非本輪模型預測',24)])
    elif kind in {'confusion','recall'}:
        parts.extend([text(300,55,'預測答案',28),text(65,220,'真實',26)])
        for r in range(2):
            for c in range(2):parts.append(box(135+c*150,85+r*120,150,120,'核對' if r==c else '判錯',SOFT if r==c else '#FFFAF3'))
        parts.extend([arrow(475,360,405,300),text(260,410,'格內數字來自實際輸出',27)])
    elif kind in {'prediction','manifest'}:
        parts.extend([box(50,65,420,75,'圖片路徑／設備識別碼',SOFT),arrow(260,150,260,195),box(45,210,205,95,'真實答案'),box(270,210,205,95,'模型預測'),text(260,375,'逐筆對照，再回到原資料',28)])
    elif kind in {'logistic','threshold'}:
        parts.extend([box(120,40,280,75,'感測特徵',SOFT),arrow(260,125,260,165),box(120,175,280,75,'模型估計'),arrow(260,260,260,300),box(90,310,340,75,'依 0.5 門檻分類')])
    elif kind in {'folder','upload','download','filebundle'}:
        parts.append('<path d="M55 110 L55 75 L205 75 L235 110 L465 110 L465 325 L55 325Z" fill="#F2D4B7" stroke="#292421" stroke-width="4"/>')
        for i,label in enumerate(['程式 .m','結果檔','操作說明']):parts.append(text(260,170+i*60,label,32))
        parts.append(arrow(420,35,420,105) if kind!='download' else arrow(420,330,420,385))
        parts.append(text(240,400,'保留資料夾與檔案的關係',25))
    elif kind=='command':
        parts.extend([box(45,100,430,160,fill=INK),text(85,165,'>>',38,'start',SOFT),text(145,165,'完整函式',36,'start','#FFFAF3'),text(260,225,'按 Enter 執行',30,color='#FFFAF3'),arrow(410,65,355,100),text(260,350,'示意｜不含提示符號',28)])
    elif kind in {'check','error','help'}:
        labels={'check':['檔案找得到','數字對得起來','結果說得清楚'],'error':['完整錯誤文字','目前位置與命令','預期與實際結果'],'help':['MATLAB 版本','執行命令與改動','回到 MATLAB 驗證']}[kind]
        for i,label in enumerate(labels):parts.append(box(50,60+i*105,420,80,label,SOFT if i==0 else '#FFFAF3'))
        parts.append(arrow(480,45,440,70))
    elif kind=='report':
        parts.append(box(90,35,340,355))
        for i,label in enumerate(['方法與資料','程式與設定','結果與限制']):parts.extend([text(260,115+i*95,label,32),f'<path d="M135 {140+i*95} L385 {140+i*95}" stroke="#8C8075" stroke-width="2"/>'])
        parts.append(arrow(465,40,415,90))
    else:
        labels=['資料','方法','結果'] if kind=='workflow' else ['感測資料','色塊面積','圖形分類']
        for i,label in enumerate(labels):parts.append(box(95,35+i*125,330,80,label,SOFT if i==0 else '#FFFAF3'))
        parts.extend([arrow(260,120,260,155),arrow(260,245,260,280)])
    return '<svg class="diagram" viewBox="0 0 520 430" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="'+escape(LABELS[kind])+'">'+''.join(parts)+'</svg>'
