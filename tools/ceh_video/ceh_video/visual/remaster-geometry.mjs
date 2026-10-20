/** Absolute-time orthogonal routing. No DOM, clocks, mutable caches or randomness. */
// Diagram-route variant: bounded gutters exclude title, note, subtitle and asset rail.
const RG_SAFE = {left: 144.4, top: 304, right: 1470, bottom: 744};
const RG_PORT_FRACTIONS = [.5,.25,.75];
const RG_LANE_CLEARANCE = 12; // Packet half-height8 + line half-width2 + 2px separation.
const RG_EPS = 1e-7;
const RG_CLEARANCE = 12; // 10px arrow half-width plus stroke clearance.
const RG_STUB = 20;
const rgEq = (a,b) => Math.abs(a-b) < RG_EPS;
const rgPointEq = (a,b) => rgEq(a.x,b.x) && rgEq(a.y,b.y);
const rgExpand = (b,n) => ({x:b.x-n,y:b.y-n,width:b.width+2*n,height:b.height+2*n});
const rgInside = (p,b) => p.x>b.x+RG_EPS && p.x<b.x+b.width-RG_EPS && p.y>b.y+RG_EPS && p.y<b.y+b.height-RG_EPS;
const rgSafe = p => p.x>=RG_SAFE.left && p.x<=RG_SAFE.right && p.y>=RG_SAFE.top && p.y<=RG_SAFE.bottom;
function rgCross(a,b,r) {
  if(rgEq(a.y,b.y)) return a.y>r.y+RG_EPS && a.y<r.y+r.height-RG_EPS && Math.max(a.x,b.x)>r.x+RG_EPS && Math.min(a.x,b.x)<r.x+r.width-RG_EPS;
  if(rgEq(a.x,b.x)) return a.x>r.x+RG_EPS && a.x<r.x+r.width-RG_EPS && Math.max(a.y,b.y)>r.y+RG_EPS && Math.min(a.y,b.y)<r.y+r.height-RG_EPS;
  return true; // A non-orthogonal segment is not a supported route.
}
function rgClear(points,obstacles) {
  return points.every(rgSafe) && points.slice(1).every((p,i)=>!obstacles.some(b=>rgCross(points[i],p,b)));
}
function rgSimplify(points) {
  const out=[];
  for(const p of points) {
    if(out.length && rgPointEq(out.at(-1),p)) continue;
    while(out.length>1 && ((rgEq(out.at(-2).x,out.at(-1).x)&&rgEq(out.at(-1).x,p.x)) || (rgEq(out.at(-2).y,out.at(-1).y)&&rgEq(out.at(-1).y,p.y))) && (out.at(-1).x-out.at(-2).x)*(p.x-out.at(-1).x)+(out.at(-1).y-out.at(-2).y)*(p.y-out.at(-1).y)>0) out.pop();
    out.push({...p});
  }
  return out;
}
function rgBacktracks(points) {
  return points.slice(2).some((c,i)=>{const a=points[i],b=points[i+1];return (rgEq(a.x,b.x)&&rgEq(b.x,c.x)||rgEq(a.y,b.y)&&rgEq(b.y,c.y))&&((b.x-a.x)*(c.x-b.x)+(b.y-a.y)*(c.y-b.y))<0;});
}
function rgNormal(a,b,side,incoming=false) {
  const normals={right:[1,0],left:[-1,0],bottom:[0,1],top:[0,-1]},n=normals[side];
  if(!n)return false;
  const dx=b.x-a.x,dy=b.y-a.y,sign=incoming?-1:1;
  return Math.abs(dx*n[1]-dy*n[0])<RG_EPS&&(dx*n[0]+dy*n[1])*sign>RG_EPS;
}
function rgLength(points) { return points.slice(1).reduce((s,p,i)=>s+Math.abs(p.x-points[i].x)+Math.abs(p.y-points[i].y),0); }
function rgPorts(b, fractions=[.5], requested=null, other=null) {
  // Facing cards can approach by the entrance offset. Their two normal stubs
  // share that measured gap rather than crossing each other and doubling back.
  const stub=side=>{
    if(!other)return RG_STUB;
    const gaps={right:other.x-(b.x+b.width),left:b.x-(other.x+other.width),
      bottom:other.y-(b.y+b.height),top:b.y-(other.y+other.height)};
    return gaps[side]>0?Math.min(RG_STUB,gaps[side]/2):RG_STUB;
  };
  const ports=[];
  for(const f of fractions) {
    if(!Number.isFinite(f)||f<=0||f>=1)throw Error('Port fraction must lie strictly inside component side');
    ports.push(
      ['right',{x:b.x+b.width,y:b.y+b.height*f},{x:b.x+b.width+stub('right'),y:b.y+b.height*f},f],
      ['left',{x:b.x,y:b.y+b.height*f},{x:b.x-stub('left'),y:b.y+b.height*f},f],
      ['bottom',{x:b.x+b.width*f,y:b.y+b.height},{x:b.x+b.width*f,y:b.y+b.height+stub('bottom')},f],
      ['top',{x:b.x+b.width*f,y:b.y},{x:b.x+b.width*f,y:b.y-stub('top')},f]);
  }
  return requested?ports.filter(p=>p[0]===requested.side&&rgEq(p[3],requested.fraction)):ports;
}
function rgReserved(routes) {
  return routes.flatMap(r=>[
    ...r.points.slice(1).map((p,i)=>{const a=r.points[i];return {x:Math.min(a.x,p.x)-RG_LANE_CLEARANCE,y:Math.min(a.y,p.y)-RG_LANE_CLEARANCE,width:Math.abs(a.x-p.x)+2*RG_LANE_CLEARANCE,height:Math.abs(a.y-p.y)+2*RG_LANE_CLEARANCE};}),
    {x:r.end.x-12,y:r.end.y-12,width:24,height:24}
  ]);
}

function rgCandidates(a,b,obstacles) {
  const candidates=[[a,b],[a,{x:b.x,y:a.y},b],[a,{x:a.x,y:b.y},b]];
  const xs=[(a.x+b.x)/2,RG_SAFE.left,RG_SAFE.right];
  const ys=[(a.y+b.y)/2,RG_SAFE.top,RG_SAFE.bottom];
  for(const r of obstacles) {xs.push(r.x,r.x+r.width);ys.push(r.y,r.y+r.height);}
  for(const x of xs) candidates.push([a,{x,y:a.y},{x,y:b.y},b]);
  for(const y of ys) candidates.push([a,{x:a.x,y},{x:b.x,y},b]);
  return candidates;
}
// Rectilinear visibility grid fallback. Endpoint and obstacle edges form a finite
// routing graph; Dijkstra's distance is deterministic with stable index ties.
function rgGraph(a,b,obstacles) {
  const xs=[a.x,b.x,RG_SAFE.left,RG_SAFE.right], ys=[a.y,b.y,RG_SAFE.top,RG_SAFE.bottom];
  for(const r of obstacles) {xs.push(r.x,r.x+r.width);ys.push(r.y,r.y+r.height);}
  const unique = v=>[...new Set(v)].sort((a,b)=>a-b);
  const xx=unique(xs).filter(x=>x>=RG_SAFE.left&&x<=RG_SAFE.right), yy=unique(ys).filter(y=>y>=RG_SAFE.top&&y<=RG_SAFE.bottom);
  const nodes=[], by=new Map();
  for(let j=0;j<yy.length;j++) for(let i=0;i<xx.length;i++) {
    const p={x:xx[i],y:yy[j]}; if(obstacles.some(r=>rgInside(p,r))) continue;
    by.set(`${i},${j}`,nodes.length);nodes.push({p,i,j});
  }
  const start=nodes.findIndex(n=>rgPointEq(n.p,a)), end=nodes.findIndex(n=>rgPointEq(n.p,b));
  if(start<0||end<0) return null;
  const dist=Array(nodes.length).fill(Infinity), prev=Array(nodes.length).fill(-1), done=new Set();dist[start]=0;
  while(true) {
    let u=-1; for(let i=0;i<nodes.length;i++) if(!done.has(i)&&(u<0||dist[i]<dist[u])) u=i;
    if(u<0||!Number.isFinite(dist[u])) return null;
    if(u===end) break; done.add(u);
    const n=nodes[u];
    for(const [di,dj] of [[1,0],[-1,0],[0,1],[0,-1]]) {
      const v=by.get(`${n.i+di},${n.j+dj}`); if(v===undefined||done.has(v)||!rgClear([n.p,nodes[v].p],obstacles)) continue;
      const cost=dist[u]+rgLength([n.p,nodes[v].p]);if(cost<dist[v]) {dist[v]=cost;prev[v]=u;}
    }
  }
  const result=[];for(let v=end;v!==-1;v=prev[v]) result.unshift(nodes[v].p);return result;
}

export function route(fromBox,toBox,obstacleBoxes=[],{fromId=fromBox.id,toId=toBox.id,routingVariant=null,reservedRoutes=[],fromPort=null,toPort=null}={}) {
  for(const b of [fromBox,toBox,...obstacleBoxes]) if(![b.x,b.y,b.width,b.height].every(Number.isFinite)||b.width<=0||b.height<=0) throw new Error('Invalid routing box');
  if(fromBox===toBox || (fromId!==undefined&&fromId===toId)) throw new Error('Self connections require an explicit component variant');
  const obstacles=obstacleBoxes.filter(b=>b!==fromBox&&b!==toBox&&!(fromId!==undefined&&b.id===fromId)&&!(toId!==undefined&&b.id===toId)).map(b=>rgExpand(b,RG_CLEARANCE));
  // Endpoint interiors also block middle segments; only the final port touches them.
  const reserved=rgReserved(reservedRoutes);
  const blockers=[...obstacles,fromBox,toBox,...reserved];
  // The port-to-stub links alone may enter the endpoint clearance envelope.
  // Every middle segment must stay clear of both expanded endpoint boxes.
  const middleBlockers=[...obstacles,rgExpand(fromBox,RG_CLEARANCE),rgExpand(toBox,RG_CLEARANCE),...reserved];
  if(routingVariant!==null&&routingVariant!=='independent-ports')throw Error('Unknown routing variant');
  const fractions=routingVariant==='independent-ports'?RG_PORT_FRACTIONS:[.5];
  const pairs=[];
  for(const f of rgPorts(fromBox,fromPort?[fromPort.fraction]:fractions,fromPort,toBox)) for(const t of rgPorts(toBox,toPort?[toPort.fraction]:fractions,toPort,fromBox)) {
    if(!rgClear([f[1],f[2]],blockers)||!rgClear([t[2],t[1]],blockers)) continue;
    pairs.push({f,t,lower:rgLength([f[1],f[2],t[2],t[1]])});
  }
  pairs.sort((a,b)=>a.lower-b.lower);
  let best=null,score=Infinity;
  function consider(p,f,t) {
    if(!p||!rgClear(p,middleBlockers)) return;
    const points=rgSimplify([f[1],...p,t[1]]);
    if(points.length<2||rgBacktracks(points)||!rgNormal(points[0],points[1],f[0])||!rgNormal(points.at(-2),points.at(-1),t[0],true)||!rgClear(points,blockers)) return;
    const cost=rgLength(points)+(points.length-2)*8;
    if(cost<score) {score=cost;best={points,start:{...f[1]},end:{...t[1]},fromSide:f[0],toSide:t[0],fromFraction:f[3],toFraction:t[3]};}
  }
  for(const {f,t,lower} of pairs) {
    if(lower>score) continue;
    for(const p of rgCandidates(f[2],t[2],middleBlockers)) consider(p,f,t);
  }
  if(!best) for(const {f,t} of pairs) consider(rgGraph(f[2],t[2],middleBlockers),f,t);
  if(!best) throw new Error(`No safe orthogonal route: ${fromId??'from'} → ${toId??'to'}`);
  best.d=best.points.map((p,i)=>`${i?'L':'M'}${p.x} ${p.y}`).join(' ');
  return best;
}

export function routeSceneEdges(nodes,edges) {
  const lookup=Object.fromEntries(nodes.map(n=>[n.id,n])),routed=[];
  for(const e of edges){
    const r=route(lookup[e.from],lookup[e.to],nodes,{...e,fromId:e.from,toId:e.to,
      reservedRoutes:e.routingVariant==='independent-ports'?routed:[]});
    routed.push({...e,...r});
  }
  return routed;
}
function rgCollinearOverlap(a,b,c,d) {
  if(rgEq(a.y,b.y)&&rgEq(c.y,d.y)&&rgEq(a.y,c.y))return Math.min(Math.max(a.x,b.x),Math.max(c.x,d.x))-Math.max(Math.min(a.x,b.x),Math.min(c.x,d.x))>RG_EPS;
  if(rgEq(a.x,b.x)&&rgEq(c.x,d.x)&&rgEq(a.x,c.x))return Math.min(Math.max(a.y,b.y),Math.max(c.y,d.y))-Math.max(Math.min(a.y,b.y),Math.min(c.y,d.y))>RG_EPS;
  return false;
}

function rgTransverseCross(a,b,c,d) {
  if(rgEq(a.y,b.y)&&rgEq(c.x,d.x))return c.x>Math.min(a.x,b.x)+RG_EPS&&c.x<Math.max(a.x,b.x)-RG_EPS&&a.y>Math.min(c.y,d.y)+RG_EPS&&a.y<Math.max(c.y,d.y)-RG_EPS;
  if(rgEq(a.x,b.x)&&rgEq(c.y,d.y))return rgTransverseCross(c,d,a,b);
  return false;
}

export function pointAt(points,p) {
  if(!points.length||!Number.isFinite(p)) throw new Error('Invalid path position');
  if(points.length===1) return {...points[0],angle:0};
  const lengths=points.slice(1).map((q,i)=>Math.hypot(q.x-points[i].x,q.y-points[i].y));
  let distance=Math.max(0,Math.min(1,p))*lengths.reduce((a,b)=>a+b,0);
  for(let i=0;i<lengths.length;i++) {
    if(distance<=lengths[i]||i===lengths.length-1) {
      const a=points[i],b=points[i+1],f=lengths[i]?distance/lengths[i]:0;
      return {x:a.x+(b.x-a.x)*f,y:a.y+(b.y-a.y)*f,angle:Math.atan2(b.y-a.y,b.x-a.x)*180/Math.PI};
    }
    distance-=lengths[i];
  }
}

export function validateState(nodes,edges,tokens={}) {
  const errors=[], width=tokens.canvas?.width??1920,height=tokens.canvas?.height??1080;
  const sx=width*(tokens.safeArea?.horizontal??.07),sy=height*(tokens.safeArea?.vertical??.08);
  const byId=new Map(nodes.map(n=>[n.id,n]));
  for(const n of nodes) {
    if(![n.x,n.y,n.width,n.height].every(Number.isFinite)||n.width<=0||n.height<=0) {errors.push(`invalid-box:${n.id}`);continue;}
    if(n.x<sx-RG_EPS||n.y<sy-RG_EPS||n.x+n.width>width-sx+RG_EPS||n.y+n.height>height-sy+RG_EPS) errors.push(`safe-area:${n.id}`);
  }
  for(let i=0;i<nodes.length;i++) for(let j=i+1;j<nodes.length;j++) {
    const a=nodes[i],b=nodes[j];if(a.x<b.x+b.width-RG_EPS&&a.x+a.width>b.x+RG_EPS&&a.y<b.y+b.height-RG_EPS&&a.y+a.height>b.y+RG_EPS) errors.push(`overlap:${a.id}:${b.id}`);
  }
  for(const e of edges) {
    const a=byId.get(e.from),b=byId.get(e.to),r=e.route??e;
    if(!a||!b||!r.points?.length) {errors.push(`missing-route:${e.from}:${e.to}`);continue;}
    const port=(box,side,fraction)=>rgPorts(box,[fraction??.5]).find(p=>p[0]===side)?.[1];
    const start=port(a,r.fromSide,r.fromFraction),end=port(b,r.toSide,r.toFraction);
    if(!start||!end||!rgPointEq(start,r.points[0])||!rgPointEq(end,r.points.at(-1))) errors.push(`port:${e.from}:${e.to}`);
    if(r.points.length<2||!rgNormal(r.points[0],r.points[1],r.fromSide)||!rgNormal(r.points.at(-2),r.points.at(-1),r.toSide,true))errors.push(`port-normal:${e.from}:${e.to}`);
    if(rgBacktracks(r.points))errors.push(`route-backtracking:${e.from}:${e.to}`);
    const middle=r.points.slice(1,-1),endpointEnvelopes=[rgExpand(a,RG_CLEARANCE),rgExpand(b,RG_CLEARANCE)];
    if(middle.some(p=>endpointEnvelopes.some(box=>rgInside(p,box)))||!rgClear(middle,endpointEnvelopes))errors.push(`route-endpoint-clearance:${e.from}:${e.to}`);
    if(!r.points.every(rgSafe)) errors.push(`route-safe-area:${e.from}:${e.to}`);
    const obs=nodes.filter(n=>n.id!==e.from&&n.id!==e.to).map(n=>rgExpand(n,RG_CLEARANCE));
    if(!rgClear(r.points,[...obs,a,b])) errors.push(`route-crossing:${e.from}:${e.to}`);
  }
  for(let i=0;i<edges.length;i++)for(let j=i+1;j<edges.length;j++){
    const a=edges[i].route??edges[i],b=edges[j].route??edges[j];
    if(!a.points?.length||!b.points?.length)continue;
    if([a.points[0],a.points.at(-1)].some(p=>[b.points[0],b.points.at(-1)].some(q=>rgPointEq(p,q))))errors.push(`shared-edge-port:${edges[i].from}:${edges[i].to}:${edges[j].from}:${edges[j].to}`);
    if(a.points.slice(1).some((p,k)=>b.points.slice(1).some((q,l)=>rgCollinearOverlap(a.points[k],p,b.points[l],q))))errors.push(`shared-edge-lane:${edges[i].from}:${edges[i].to}:${edges[j].from}:${edges[j].to}`);
    if(a.points.slice(1).some((p,k)=>b.points.slice(1).some((q,l)=>rgTransverseCross(a.points[k],p,b.points[l],q))))errors.push(`edge-crossing:${edges[i].from}:${edges[i].to}:${edges[j].from}:${edges[j].to}`);
  }
  return errors;
}
