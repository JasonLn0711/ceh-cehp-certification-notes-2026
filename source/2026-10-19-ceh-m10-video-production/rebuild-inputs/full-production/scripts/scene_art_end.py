"""M10 connected case, response, recovery and capstone figures."""
from art_common import *

def bar(a, ident, x, y, width, height, value, maximum, i, color=ACCENT):
    background=a.add(rect(x,y,width,height,WHITE,4),ident+'-outline');a.show(background,at(a,0))
    fill=a.add(f'<rect x="{x+4}" y="{y+4}" width="{(width-8)*min(value/maximum,1)}" height="{height-8}" fill="{color}"/>',ident+'-fill')
    a.moves.append({'target':fill,'start':at(a,i),'duration':1.3,'from':{'scaleX':0,'svgOrigin':f'{x+4} {y+height/2}'},'props':{'scaleX':1,'ease':'power2.out'}})

def render(scene,audio):
    a=base(scene,audio);n=int(scene['id'][1:])
    if n==43:
        L(a,470,330,'Offered: 2,400 Mbps',0,34,30)
        bar(a,'offered',210,370,510,95,2400,2400,0)
        L(a,1090,330,'Accepted: 200 Mbps',1,34,30)
        bar(a,'accepted',835,370,510,95,200,2400,1,SOFT)
        C(a,210,535,'WAN limit 200 Mbps\nDiscarded 2,200 Mbps',1,w=510,h=135)
        C(a,835,535,'User checks: 20 / 100\nServer CPU: 25%',2,w=510,h=135)
        R(a,725,420,820,420,1)
        note(a,'Place upstream protection before the constrained access link')
    elif n==44:
        L(a,470,330,'6,000 unique attempts',0,34,31)
        L(a,1090,330,'Only 60 completed',2,34,31)
        R(a,700,385,875,385,2)
        for k in range(16):
            x=210+(k%8)*68;y=425+(k//8)*84
            g=a.add(rect(x,y,58,66,SOFT,4),'state-slot-'+str(k));a.show(g,at(a,1)+k*.055)
        L(a,480,650,'16 cells × 64 entries = 1,024',1,30,36)
        C(a,835,425,'Backlog 1,024 / 1,024',1,w=510,h=100)
        C(a,835,555,'Client success 5 / 100\nLink traffic 30 Mbps',2,w=510,h=120)
        note(a,'A control trial needs measured legitimate and unwanted outcomes')
    elif n==45:
        C(a,210,340,'Request\n60 IP bytes',0,w=430,h=135)
        C(a,940,340,'Response\n3,000 IP bytes',1,w=430,h=135,fill=SOFT)
        R(a,650,405,930,405,1,label='Paired exchange')
        L(a,790,545,'3,000 ÷ 60 = 50× at IP',2,38,40)
        L(a,790,625,'3,014 ÷ 74 ≈ 40.7× at Ethernet',2,30,49)
        note(a,'Source validation, reflector policy and victim protection have different owners')
    elif n==46:
        L(a,470,330,'Offered CPU work: 24 cores',1,32,32)
        bar(a,'work',210,380,510,95,24,24,1)
        L(a,1090,330,'CPU budget: 8 cores',1,32,32)
        bar(a,'budget',835,380,510,95,8,24,1,SOFT)
        C(a,210,545,'120 requests/sec × 0.2 sec\n= 24 core-seconds/sec',0,w=510,h=130)
        C(a,835,545,'Dependency: 32 / 32 busy\nQueue: 400 requests',2,w=510,h=130)
        note(a,'Toy demand accounting; proposed limits need a separate service test')
    elif n==47:
        flow(a,['Name user impact','Preserve aligned evidence','Select control owner','Record decision + rollback'],['school_building','evidence_slip','scope_sheet','report_file'])
        note(a,'Restore legitimate service while keeping observations and decisions traceable')
    elif n==48:
        C(a,210,340,'Legitimate user path\nLookup → connect → complete',0,w=550,h=135)
        C(a,835,340,'Resource path\nLink · state · work · dependency',1,w=550,h=135)
        R(a,760,410,825,410,1)
        C(a,210,565,'Repeat across an agreed window\nCheck false rejection',2,w=550,h=125,fill=SOFT)
        C(a,835,565,'Owner + monitoring + follow-up\nPreserve original evidence',3,w=550,h=125)
        note(a,'One quiet interval or one successful request does not establish stable recovery')
    elif n==49:
        C(a,210,335,'Allowed, minimized evidence',0,w=1180,h=80)
        R(a,800,425,800,470,1)
        C(a,210,480,'AI draft: claim → record → uncertainty',1,w=1180,h=95,fill=SOFT)
        C(a,210,615,'Human review + independent calculation + decision owner',2,w=1180,h=90)
        note(a,'Treat log text as untrusted data; keep change authority with the named owner')
    elif n==58:
        table(a,['Case','Resource / evidence','Control + acceptance'],[
            ['E01','Provider + WAN IP octets','Upstream + user continuity'],
            ['E02','Half-open state / completions','State control + legitimate flow'],
            ['E03','Paired packet layer / bytes','Owner-specific validation'],
            ['E04','Request work + dependency','Bounded work + service outcome'],
        ],row_h=74)
        note(a,'Submit your own evidence, resource explanation, control plan and acceptance check')
    else:raise ValueError(('No end-scene figure',scene['id']))
    return a
