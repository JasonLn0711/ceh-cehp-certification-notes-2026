// Scoped to one composition; tl is the registered paused GSAP timeline.
const sid=model.scene,root=document.getElementById(sid+'-connections').closest('[data-composition-id]');
const ns='http://www.w3.org/2000/svg',elements=new Map();
function make(tag,attrs,parent){const e=document.createElementNS(ns,tag);for(const [k,v]of Object.entries(attrs))e.setAttribute(k,v);parent.appendChild(e);return e;}
for(const edge of model.edges){
 const group=make('g',{},document.getElementById(sid+'-connections'));
 const line=make('path',{fill:'none',stroke:model.tokens.colors.terracotta,'stroke-width':4,'stroke-linecap':'round','stroke-linejoin':'round'},group);
 const head=make('path',{fill:'none',stroke:model.tokens.colors.terracotta,'stroke-width':4,'stroke-linecap':'round','stroke-linejoin':'round'},group);
 const packet=make('path',{d:'M-12 -8 H12 V8 H-12 Z M-12 -8 L0 2 L12 -8',fill:model.tokens.colors.apricot,stroke:model.tokens.colors.ink,'stroke-width':2},group);
 elements.set(edge.id,{group,line,head,packet});
}
const ease=gsap.parseEase(model.tokens.motion.ease),clamp=x=>Math.max(0,Math.min(1,x));
let routeKey=null,routeValues=null;
function state(t){
 const nodes=model.components.map(n=>{const u=ease(clamp((t-n.start)/model.tokens.motion.entrance));return {...n.box,id:n.id,opacity:u,start:n.start,dy:model.tokens.layout.entranceOffset*(1-u)};}).map(n=>({...n,y:n.y+n.dy}));
 const lookup=Object.fromEntries(nodes.map(n=>[n.id,n]));
 const key=nodes.map(n=>[n.x,n.y,n.width,n.height].join(',')).join(';');
 if(key!==routeKey){routeValues=routeSceneEdges(nodes,model.edges);routeKey=key;}
 const edges=model.edges.map((e,i)=>({...e,...routeValues[i],opacity:clamp((t-e.startTime)/model.tokens.motion.draw)}));
 return {nodes,edges};
}
function render(t){
 const frame=state(t);
 for(const n of frame.nodes){const e=document.getElementById(sid+'-'+n.id);e.setAttribute('transform',`translate(${n.x} ${n.y})`);e.style.opacity=n.opacity;
  const f=e.querySelector('[data-fill]');if(f)f.style.transform=`scaleX(${ease(clamp((t-n.start)/model.tokens.motion.draw))})`,f.style.transformBox='fill-box',f.style.transformOrigin='left';
 }
 for(const e of frame.edges){const el=elements.get(e.id);el.group.style.opacity=e.opacity;el.line.setAttribute('d',e.d);
  if(e.dashed){el.line.setAttribute('stroke-dasharray','10 10');el.packet.style.opacity=0;el.packet.setAttribute('transform',`translate(${e.start.x} ${e.start.y})`);}else{const length=e.points.slice(1).reduce((sum,p,i)=>sum+Math.hypot(p.x-e.points[i].x,p.y-e.points[i].y),0);el.line.setAttribute('stroke-dasharray',length);el.line.setAttribute('stroke-dashoffset',length*(1-e.opacity));}
  const end=pointAt(e.points,1);el.head.setAttribute('d',e.terminal==='blocked'?'M-12 -8 L-4 8 M-4 -8 L-12 8':'M-16 -10 L0 0 L-16 10');el.head.setAttribute('data-terminal',e.terminal||'arrow');el.head.setAttribute('transform',`translate(${end.x} ${end.y}) rotate(${end.angle})`);el.head.style.opacity=e.opacity===1?1:0;
  const progress=(t-e.startTime-model.tokens.motion.draw)/model.tokens.motion.packet;
  if(!e.dashed&&e.terminal!=='blocked'){const p=pointAt(e.points,clamp(progress));el.packet.style.opacity=progress>=0&&progress<1?1:0;el.packet.setAttribute('transform',`translate(${p.x} ${p.y}) rotate(${p.angle})`);}else{el.packet.style.opacity=0;el.packet.setAttribute('transform',`translate(${e.start.x} ${e.start.y})`);}
 }
 const note=document.getElementById(sid+'-note');if(note)note.style.opacity=ease(clamp((t-model.noteStart)/model.tokens.motion.entrance));
}
tl.to({time:0},{time:model.duration,duration:model.duration,ease:'none'},0);
tl.eventCallback('onUpdate',()=>render(tl.time()));
window.addEventListener('hf-seek',event=>event.detail.waitUntil(Promise.resolve().then(()=>render(tl.time()))));
window.__cehRemaster=window.__cehRemaster||{};
window.__cehRemaster[sid]={state,layout:model.components,spec:model.spec,validateAllFrames(){const errors=[];for(let frame=0;frame<model.frames;frame++){const s=state(frame/30),active=s.nodes.filter(n=>n.opacity>0);const e=validateState(active,s.edges.filter(e=>e.opacity>0),model.tokens);if(e.length){errors.push({frame,errors:e});if(errors.length>=20)break;}}return {frames:model.frames,errors};}};
render(0);
