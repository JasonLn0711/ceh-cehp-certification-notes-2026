from ceh_video.common import project_root, Project
"""Original layered SVG rigs. All timing is driven by measured source sentences."""
from pathlib import Path
import html,json,re,textwrap
ROOT=project_root()
INK='#292421';PAPER='#F0EBE4';WHITE='#FFFAF3';ACCENT='#C8755D';SOFT='#F2D4B7';GRAY='#B8B0A9'
def esc(x):return html.escape(str(x))
def text(x,y,value,size=34,width=32,anchor='middle',color=INK):
 lines=textwrap.wrap(str(value),width=width,break_long_words=False,break_on_hyphens=False) or ['']
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" stroke="none">'+''.join(f'<tspan x="{x}" dy="{0 if i==0 else size*1.18}">{esc(line)}</tspan>' for i,line in enumerate(lines))+'</text>'
def inner(path):return re.sub(r'^.*?<svg[^>]*>|</svg>\s*$','',Path(path).read_text(),flags=re.S)
def rect(x,y,w,h,fill=WHITE,rx=8):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{INK}" stroke-width="4"/>'
def path(d,color=INK,dash=''):return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
class Art:
 def __init__(self,sid,audio):self.sid=sid;self.parts=[];self.moves=[];self.audio=audio;self.spoken=[s for s in audio['segments'] if s['kind']=='spoken'];self.count=0
 def at(self,phrase=None,index=0):
  if phrase:
   for s in self.spoken:
    if phrase.lower() in s['canonical'].lower():return s['start_sample']/48000
   raise ValueError((self.sid,'missing spoken anchor',phrase))
  return self.spoken[min(index,len(self.spoken)-1)]['start_sample']/48000
 def add(self,content,name=None):
  self.count+=1;ident=self.sid+'-'+(name or str(self.count));self.parts.append(f'<g id="{ident}">{content}</g>');return ident
 def move(self,target,start,duration=1,**props):self.moves.append({'target':target,'start':round(start,6),'duration':duration,'props':props})
 def show(self,target,at,dx=0,dy=0):
  self.moves.append({'target':target,'start':round(at,6),'duration':.8,'from':{'opacity':0,'x':dx,'y':dy},'props':{'opacity':1,'x':0,'y':0,'ease':'power2.out'}})
 def prop(self,kind,x,y,w=260,name=None,label=None):
  f=ROOT/'assets/props'/f'{kind}.svg';svg=f.read_text();vb=re.search(r'viewBox="([^"]+)"',svg).group(1).split();scale=w/float(vb[2]);content=f'<g transform="translate({x} {y}) scale({scale})">{inner(f)}</g>'
  if label:content+=text(x+w/2,y+float(vb[3])*scale+45,label,32,24)
  return self.add(content,name)
 def slip(self,x,y,label,w=340,h=96,name=None):return self.add(rect(x,y,w,h,WHITE,3)+path(f'M{x+15} {y+12} L{x+w-20} {y+8}',GRAY)+text(x+w/2,y+42,label,32,int(w/17)),name)
 def route(self,x1,y1,x2,y2,at,reverse=False,label=None,dashed=False):
  if reverse:x1,y1,x2,y2=x2,y2,x1,y1
  d=f'M{x1} {y1} C{(x1+x2)/2} {y1} {(x1+x2)/2} {y2} {x2} {y2}'
  ident=self.add(path(d,ACCENT,'10 10' if dashed else ''),'route'+str(self.count));self.moves.append({'target':ident,'start':at,'duration':1.3,'draw':True,'dashed':dashed})
  direction=1 if x2>=x1 else -1
  head=self.add(f'<path d="M{x2-direction*16} {y2-10} L{x2} {y2} L{x2-direction*16} {y2+10}" fill="none" stroke="{ACCENT}" stroke-width="4"/>','arrowhead'+str(self.count));self.show(head,at+1.2)
  # A single folded paper token follows the same cubic; tangent always agrees with direction.
  tok=self.add('<path d="M-23 -14 L23 -14 L23 14 L-23 14 Z M-23 -14 L0 3 L23 -14" fill="'+SOFT+'" stroke="'+INK+'" stroke-width="3"/>','packet'+str(self.count))
  self.parts[-1]=self.parts[-1].replace(f'id="{tok}"',f'id="{tok}" style="opacity:0"')
  if not dashed:self.moves.append({'target':tok,'start':at+1.3,'duration':2.4,'travel':[x1,y1,x2,y2]})
  else:self.move(tok,0,0,opacity=0)
  if label:
   lab=self.add(text((x1+x2)/2,(y1+y2)/2-38,label,30,30));self.show(lab,at)
  return ident
 def tally(self,x=1595,y=640,pose='point',at=0):
  parts=[]
  for part in ['legs','left_arm_'+pose,'right_arm_'+pose,'body','face_'+pose]:
   ident=self.add(f'<g transform="translate({x} {y}) scale(.6)">{inner(ROOT/"assets/mascot/parts"/(part+".svg"))}</g>','tally-'+part);parts.append(ident);self.show(ident,at,dy=20)
  # Arm pivot stays in the original rig coordinate system through a nested group.
  self.move(parts[2],at+1,.45,rotation=-12,svgOrigin=f'{x+185*.6} {y+128*.6}');self.move(parts[2],at+1.45,.5,rotation=0)
 def svg(self):return '<svg class="art" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" aria-label="'+self.sid+' layered teaching illustration">'+''.join(self.parts)+'</svg>'

# Canonical fixed atlas anchors. Position conveys geography, never unverified access rights.
ANCHORS={'ANALYST':(265,330),'STAFF':(265,500),'WINDOWS':(265,670),'DNS':(660,290),'DIR':(660,460),'SMB':(660,630),'NFS':(975,290),'LINUX':(975,460),'SMTP':(975,630),'NTP':(1280,290),'SWITCH':(1280,460),'PRINTER':(1280,630),'VOIP':(1590,290),'LEGACY':(1590,460),'EDGE':(1590,630),'REMOTE':(1590,785),'ISP':(1280,785)}
def atlas(a,waves=None):
 net=json.load(open(ROOT/'data/network_map.json'));ids={}
 for node in net['nodes']:
  x,y=ANCHORS[node['id']];label=node['name'];kind='school_laptop' if node['id'] in ['ANALYST','STAFF','WINDOWS','LINUX'] else 'managed_switch' if node['id']=='SWITCH' else 'network_printer' if node['id']=='PRINTER' else 'edge_router' if node['id'] in ['EDGE','ISP'] else 'school_building' if node['id']=='REMOTE' else 'office_server'
  # Compact icon is independent from its exact, legible name label.
  ident=a.prop(kind,x-43,y-60,86,label=None,name='node-'+node['id']);lab=a.add(text(x,y+35,label,30,23));ids[node['id']]=(ident,lab)
  time=(waves or {}).get(node['id'],a.at(index=0));a.show(ident,time,dy=18);a.show(lab,time)
 return ids
