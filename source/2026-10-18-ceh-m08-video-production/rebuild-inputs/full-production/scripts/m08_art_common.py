"""M08 semantic teaching layers. Canonical narration anchors drive every diagram beat."""
from editorial import *
import math
CUES=json.load(open(ROOT/'scripts/cues_m08.json'))

def at(a,i):return a.at(CUES[a.sid][i])
def C(a,x,y,label,i=0,w=355,h=106,name=None):
 g=a.slip(x,y,label,w,h,name);a.show(g,at(a,i),dy=14);return g

def L(a,x,y,label,i=0,size=32,width=30,name=None):
 g=a.add(text(x,y,label,size,width),name);a.show(g,at(a,i));return g

def P(a,kind,x,y,w=200,i=0,name=None,label=None):
 g=a.prop(kind,x,y,w,name,label);a.show(g,at(a,i),dy=16);return g

def R(a,x1,y1,x2,y2,i=0,dashed=False,label=None):
 n=len(a.parts);g=a.route(x1,y1,x2,y2,at(a,i),dashed=dashed,label=label)
 if x1==x2:
  d=1 if y2>=y1 else -1;a.parts[n+1]=re.sub(r'<path d="[^"]+"',f'<path d="M{x2-10} {y2-d*16} L{x2} {y2} L{x2+10} {y2-d*16}"',a.parts[n+1],count=1)
 return g

def note(a,label,i=3,y=735):return C(a,330,y,label,i,w=1010,h=98,name='evidence-limit')
def stamp(a):
 g=a.add(text(795,278,'SIMULATED OUTPUT',24,60),'simulation-stamp');a.show(g,0)

def base(scene,audio):
 a=Art(scene['id'],audio)
 if True:
  P(a,'school_building',1510,280,170,0,'campus-anchor');L(a,1595,463,'Northstar',0,28,17)
  a.tally(1510,570,at=a.at())
 stamp(a);return a

def pipeline(a,items,props=None,question=None):
 for i,label in enumerate(items):
  x=200+i*315
  if props:P(a,props[i],x+35,335,205,i,'mechanism-'+str(i))
  C(a,x,570 if props else 395,label,i,w=270,h=130)
  if i:R(a,x-36,480 if props else 460,x+8,480 if props else 460,i,True)
 if question:note(a,question)

def compare(a,left,right,props=None,limit=None):
 for i,(x,(head,body)) in enumerate([(210,left),(845,right)]):
  L(a,x+260,335,head,i,36,25)
  if props:P(a,props[i],x+145,370,225,i)
  C(a,x,605 if props else 395,body,i,w=525,h=115 if props else 200)
 if limit:note(a,limit)

def four(a,items,props=None,limit=None):
 for i,label in enumerate(items):
  x=210+(i%2)*620;y=330+(i//2)*225
  if props:P(a,props[i],x,y,145,i);C(a,x+165,y+35,label,i,w=375,h=120)
  else:C(a,x,y,label,i,w=540,h=155)
 if limit:note(a,limit)


def table(a,headers,rows,x=210,y=330,width=1180,row_h=92,i=0,name='table',row_times=None):
    cols=len(headers);cw=width/cols
    for col,label in enumerate(headers):
        g=a.add(rect(x+col*cw,y,cw,row_h,SOFT,0)+text(x+(col+.5)*cw,y+40,label,30,int(cw/17)),name+'-head-'+str(col));a.show(g,at(a,i))
    for r,row in enumerate(rows):
        for col,label in enumerate(row):
            yy=y+(r+1)*row_h
            g=a.add(rect(x+col*cw,yy,cw,row_h,WHITE,0)+text(x+(col+.5)*cw,yy+38,label,30,int(cw/17)),name+'-'+str(r)+'-'+str(col));a.show(g,row_times[r] if row_times else at(a,min(i+r+1,3)))

def block(a,x,y,label,i=0,w=330,h=125,fill=WHITE,name=None):
    g=a.add(rect(x,y,w,h,fill,3)+text(x+w/2,y+43,label,32,max(12,int(w/17))),name);a.show(g,at(a,i),dy=12);return g

def nodes(a,labels,addresses=None,i=0):
    for j,label in enumerate(labels):
        x=210+j*410
        P(a,'school_laptop' if j==0 else 'managed_switch' if j==1 else 'office_server',x+60,350,180,min(j,3),'device-'+str(j))
        C(a,x,565,label,min(j,3),340,100)
        if addresses:L(a,x+170,710,addresses[j],min(j,3),28,25)
        if j:R(a,x-50,440,x+40,440,min(j,3),False)
