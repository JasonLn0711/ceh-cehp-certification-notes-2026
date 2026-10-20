import {test} from 'node:test';
import assert from 'node:assert/strict';
import {route,routeSceneEdges,pointAt,validateState} from './remaster-geometry.mjs';
const box=(id,x,y,width=160,height=100)=>({id,x,y,width,height});
test('ports follow a translated card and repeated routing is identical',()=>{
  const a=box('a',155,304),b=box('b',800,320);
  for(const offset of [0,16,8,0]) {
    const moved={...a,y:a.y+offset},r=route(moved,b,[moved,b]);
    assert.deepEqual(r,route(moved,b,[moved,b]));
    assert.deepEqual(validateState([moved,b],[{from:'a',to:'b',route:r}]),[]);
    assert.ok(r.points.length>=2);
  }
});
test('an intervening card forces an obstacle-free orthogonal detour',()=>{
  const nodes=[box('a',155,400),box('b',1000,400),box('block',500,370,250,160)];
  const r=route(nodes[0],nodes[1],nodes);
  assert.ok(r.points.length>=4);
  assert.deepEqual(validateState(nodes,[{from:'a',to:'b',...r}]),[]);
  assert.equal(pointAt(r.points,0).x,r.start.x);
  assert.equal(pointAt(r.points,1).y,r.end.y);
});
test('reverse packet travel evaluates directly and clamps progress',()=>{
  const points=[{x:500,y:400},{x:300,y:400},{x:300,y:500}];
  assert.deepEqual(pointAt(points,.5),{x:350,y:400,angle:180});
  assert.deepEqual(pointAt(points,-1),{x:500,y:400,angle:180});
  assert.deepEqual(pointAt(points,2),{x:300,y:500,angle:90});
});
test('a complete blocked corridor fails instead of intersecting its obstacle',()=>{
  const a=box('a',155,400),b=box('b',1000,400),wall=box('wall',500,86.4,200,907.2);
  assert.throws(()=>route(a,b,[a,b,wall]),/No safe orthogonal route/);
});
test('validation detects port displacement, overlap and unsafe content',()=>{
  const a=box('a',155,400),b=box('b',1000,400),r=route(a,b);
  r.points[0].x+=1;
  assert.ok(validateState([a,b],[{from:'a',to:'b',...r}]).some(e=>e.startsWith('port:')));
  assert.ok(validateState([a,{...b,x:200}],[]).some(e=>e.startsWith('overlap:')));
  assert.ok(validateState([{...a,y:80}],[]).some(e=>e.startsWith('safe-area:')));
});

test('independent ports prevent a return path from merging with incoming traffic',()=>{
  const nodes=[box('app',155,304,620,188),box('pool',815,304,620,188),box('limit',155,532,620,188),box('queue',815,532,620,188)];
  const edges=[{from:'app',to:'pool'},{from:'queue',to:'pool'},{from:'limit',to:'app'}].map(e=>({...e,routingVariant:'independent-ports'}));
  for(const offset of [0,8,16]){
    const moved=nodes.map(n=>({...n,y:n.y+offset}));const routes=routeSceneEdges(moved,edges);
    assert.deepEqual(validateState(moved,routes),[]);
    assert.ok(routes.flatMap(e=>e.points).every(p=>p.x>=144.4&&p.x<=1470&&p.y>=304&&p.y<=744));
    assert.deepEqual(routes,routeSceneEdges(moved,edges));
  }
});
test('shared target port and collinear line overlap are hard failures',()=>{
  const nodes=[box('a',155,304),box('b',800,304),box('c',155,532)];
  const first=route(nodes[0],nodes[1],nodes);const duplicate={...first,from:'a',to:'b'};
  const errors=validateState(nodes,[{...first,from:'a',to:'b'},duplicate]);
  assert.ok(errors.some(e=>e.startsWith('shared-edge-port:')));
  assert.ok(errors.some(e=>e.startsWith('shared-edge-lane:')));
});
test('blocked boundary route keeps its own terminal and independent ports',()=>{
  const nodes=[box('boundary',595,304,400,188),box('others',1035,304,400,188),box('outside',1035,532,400,188)];
  const edges=[{from:'boundary',to:'others',routingVariant:'independent-ports'},
    {from:'outside',to:'boundary',routingVariant:'independent-ports',terminal:'blocked',dashed:true}];
  const routes=routeSceneEdges(nodes,edges);
  assert.equal(routes[1].terminal,'blocked');
  assert.deepEqual(validateState(nodes,routes),[]);
  assert.notDeepEqual(routes[0].start,routes[1].end);
});

test('S27 origin to allowed prefix leaves right port normally without border hugging',()=>{
  const origin=box('origin',155,304,400,188),allowed=box('allowed',595,532,400,188);
  const options={routingVariant:'independent-ports',fromPort:{side:'right',fraction:.75},toPort:{side:'left',fraction:.25}};
  const r=route(origin,allowed,[origin,allowed],options);
  assert.deepEqual(r.points,[{x:555,y:445},{x:575,y:445},{x:575,y:579},{x:595,y:579}]);
  assert.deepEqual(validateState([origin,allowed],[{from:'origin',to:'allowed',...r}]),[]);
  const bad={...r,points:[{x:555,y:445},{x:555,y:579},{x:595,y:579}]};
  assert.ok(validateState([origin,allowed],[{from:'origin',to:'allowed',...bad}]).some(e=>e.startsWith('port-normal:')));
  const near={...r,points:[{x:555,y:445},{x:556,y:445},{x:556,y:579},{x:595,y:579}]};
  assert.ok(validateState([origin,allowed],[{from:'origin',to:'allowed',...near}]).some(e=>e.startsWith('route-endpoint-clearance:')));
});
test('mixed entrance positions preserve outward and inward port normals',()=>{
  for(const fromDy of [0,8,16])for(const toDy of [0,8,16]){
    const a=box('a',155,304+fromDy,400,188),b=box('b',595,532+toDy,400,188);
    const r=route(a,b,[a,b],{routingVariant:'independent-ports',fromPort:{side:'right',fraction:.75},toPort:{side:'left',fraction:.25}});
    assert.equal(r.points[1].y,r.points[0].y);assert.ok(r.points[1].x>r.points[0].x);
    assert.equal(r.points.at(-2).y,r.points.at(-1).y);assert.ok(r.points.at(-1).x>r.points.at(-2).x);
    assert.deepEqual(validateState([a,b],[{from:'a',to:'b',...r}]),[]);
  }
});
test('shortened facing gap uses disjoint normal stubs and rejects reversals',()=>{
  const a=box('a',595,320,400,188),b=box('b',595,532,400,188);
  const r=route(b,a,[a,b],{fromPort:{side:'top',fraction:.5},toPort:{side:'bottom',fraction:.5}});
  assert.deepEqual(r.points,[{x:795,y:532},{x:795,y:508}]);
  assert.deepEqual(validateState([a,b],[{from:'b',to:'a',...r}]),[]);
  const loop={...r,points:[{x:795,y:532},{x:795,y:512},{x:795,y:528},{x:795,y:508}]};
  assert.ok(validateState([a,b],[{from:'b',to:'a',...loop}]).some(e=>e.startsWith('route-backtracking:')));
});
