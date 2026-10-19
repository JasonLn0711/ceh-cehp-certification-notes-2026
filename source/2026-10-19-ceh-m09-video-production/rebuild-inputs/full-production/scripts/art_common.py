"""M09 native teaching geometry. Approved palette/rig; exact narration anchors."""
from editorial import *
CUES=json.load(open(ROOT/'scripts/cues_m09.json'))
def at(a,i):return a.at(CUES[a.sid][i])
def L(a,x,y,label,i=0,size=32,width=30,name=None):
 g=a.add(text(x,y,label,size,width),name);a.show(g,at(a,i));return g
def C(a,x,y,label,i=0,w=355,h=120,fill=WHITE,name=None,size=32):
 g=a.add(rect(x,y,w,h,fill,4)+text(x+w/2,y+42,label,size,max(12,int(w/(size*.53)))),name);a.show(g,at(a,i),dy=12);return g
def P(a,kind,x,y,w=190,i=0,name=None):
 g=a.prop(kind,x,y,w,name);a.show(g,a.at() if i==0 else at(a,i),dy=14);return g
def R(a,x1,y1,x2,y2,i=0,label=None,dashed=False):
 n=len(a.parts);g=a.route(x1,y1,x2,y2,at(a,i),dashed=dashed,label=label)
 if x1==x2:
  d=1 if y2>=y1 else -1
  a.parts[n+1]=re.sub(r'<path d="[^"]+"',f'<path d="M{x2-10} {y2-d*16} L{x2} {y2} L{x2+10} {y2-d*16}"',a.parts[n+1],count=1)
 return g
def note(a,label,i=3,y=742):
 x=210;w=1180;h=88
 border=a.add(path(f'M{x} {y+3} L{x+w} {y} L{x+w+2} {y+h} L{x-2} {y+h+2} Z',INK),'note-border')
 a.moves.append({'target':border,'start':at(a,i),'duration':.8,'draw':True})
 marker=a.add(f'<rect x="{x+16}" y="{y+15}" width="{w-32}" height="55" fill="{SOFT}"/>','note-marker')
 a.moves.append({'target':marker,'start':at(a,i),'duration':.65,'from':{'scaleX':0,'svgOrigin':f'{x+16} {y+42}'},'props':{'scaleX':1,'ease':'power2.out'}})
 t=a.add(text(x+w/2,y+35,label,29,73),'note-text');a.show(t,at(a,i)+.2)
 return border
def base(scene,audio):
 a=Art(scene['id'],audio)
 for j in range(8):a.add(path(f'M66 {125+j*90} l18 {2 if j%2 else -2}',GRAY),'paper-edge-'+str(j))
 g=a.prop('school_building',1510,280,170,'campus-anchor');a.show(g,a.at(),dy=12)
 g=a.add(text(1595,463,'Northstar',28,17),'campus-name');a.show(g,a.at())
 a.tally(1510,570,at=a.at())
 g=a.add(text(800,278,'SIMULATED OUTPUT',24,60),'simulation-stamp');a.show(g,0)
 return a
def flow(a,labels,props=None,limit=None):
 for i,label in enumerate(labels):
  x=210+i*305
  if props:P(a,props[i],x+42,345,175,i,'mechanism-'+str(i))
  C(a,x,565 if props else 415,label,i,w=265,h=130,fill=SOFT if i==0 else WHITE)
  if i:R(a,x-39,520 if props else 480,x-7,520 if props else 480,i,dashed=False)
 if limit:note(a,limit)
def compare(a,left,right,limit=None,props=None):
 for i,(x,pair) in enumerate([(210,left),(835,right)]):
  head,body=pair;L(a,x+275,335,head,i,35,27)
  if props:P(a,props[i],x+165,365,195,i)
  C(a,x,590 if props else 385,body,i,w=550,h=125 if props else 265,fill=SOFT if i==0 else WHITE)
 if limit:note(a,limit)
def four(a,labels,props=None,limit=None):
 for i,label in enumerate(labels):
  x=210+(i%2)*625;y=330+(i//2)*215
  if props:P(a,props[i],x,y,130,i);C(a,x+150,y+28,label,i,w=395,h=145)
  else:C(a,x,y,label,i,w=550,h=160,fill=SOFT if i==0 else WHITE)
 if limit:note(a,limit)
def layers(a,labels,limit=None):
 for i,label in enumerate(labels):C(a,210+i*35,330+i*96,label,i,w=1180-i*70,h=78,fill=SOFT if i==0 else WHITE)
 if limit:note(a,limit)
def table(a,headers,rows,x=210,y=330,w=1180,row_h=87,start=0):
 cw=w/len(headers)
 for j,label in enumerate(headers):
  g=a.add(rect(x+j*cw,y,cw,row_h,SOFT,0)+text(x+(j+.5)*cw,y+35,label,29,max(10,int(cw/16))),f'head-{j}');a.show(g,a.at())
 for i,row in enumerate(rows):
  for j,label in enumerate(row):
   yy=y+(i+1)*row_h;g=a.add(rect(x+j*cw,yy,cw,row_h,WHITE,0)+text(x+(j+.5)*cw,yy+34,label,28,max(10,int(cw/15.5))),f'cell-{i}-{j}');a.show(g,at(a,min(start+i+1,3)))
def person(a,x,y,label,i=0):
 body=f'<circle cx="{x}" cy="{y+27}" r="27" fill="{SOFT}" stroke="{INK}" stroke-width="4"/>'+path(f'M{x} {y+55} V{y+145} M{x-42} {y+100} L{x} {y+70} L{x+42} {y+100} M{x} {y+145} L{x-38} {y+200} M{x} {y+145} L{x+38} {y+200}')
 g=a.add(body,'person-'+str(a.count));a.show(g,at(a,i),dx=-16);L(a,x,y+245,label,i,30,25)
def phone(a,x,y,label,i=0):
 body=rect(x,y,170,260,WHITE,20)+path(f'M{x+50} {y+22} H{x+120}')+f'<circle cx="{x+85}" cy="{y+237}" r="7" fill="{INK}"/>'+text(x+85,y+100,label,28,10)
 g=a.add(body,'phone-'+str(a.count));a.show(g,at(a,i),dy=18);return g
def door(a,x,y,i=0):
 body=rect(x,y,230,310,SOFT,2)+rect(x+18,y+18,192,292,WHITE,1)+f'<circle cx="{x+175}" cy="{y+164}" r="7" fill="{INK}"/>'+rect(x-65,y+110,45,70,WHITE,3)
 g=a.add(body,'office-door');a.show(g,at(a,i));return g
def decision(a,title,left,right,limit=None):
 C(a,605,330,title,0,w=390,h=105,fill=SOFT)
 C(a,210,555,left,1,w=510,h=135)
 C(a,875,555,right,2,w=510,h=135)
 R(a,800,438,465,545,1)
 R(a,800,438,1130,545,2,dashed=True)
 L(a,465,492,'Check normal path',1,28,24)
 L(a,1130,492,'Check alternate path',2,28,24)
 if limit:note(a,limit)
