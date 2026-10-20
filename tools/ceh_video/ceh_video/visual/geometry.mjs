/** Pure geometry in composition coordinates. No clock or DOM mutation. */
export const EPSILON = 0.25;
export function safeBounds(tokens) {
  const {width,height}=tokens.canvas, {horizontal,vertical}=tokens.safeArea;
  return {left:width*horizontal,top:height*vertical,right:width*(1-horizontal),bottom:height*(1-vertical)};
}
export function port(box,side) {
  if(side==='left')return {x:box.x,y:box.y+box.height/2};
  if(side==='right')return {x:box.x+box.width,y:box.y+box.height/2};
  if(side==='top')return {x:box.x+box.width/2,y:box.y};
  if(side==='bottom')return {x:box.x+box.width/2,y:box.y+box.height};
  throw Error('Unknown port '+side);
}
export function connector(a,b) {
  const start=port(a,'right'),end=port(b,'left'),middle=(start.x+end.x)/2;
  return {start,end,d:`M${start.x},${start.y} C${middle},${start.y} ${middle},${end.y} ${end.x},${end.y}`};
}
export function exceptionFor(registry, context, object, rule) {
  if(!object.exceptionId)return null;
  const entry=registry.exceptions.find(e=>e.id===object.exceptionId);
  if(!entry || context.generation!=='frozen-legacy' || context.release!==entry.release ||
    context.sourceProfileSha256!==entry.sourceProfileSha256 || !entry.sceneHashes?.[context.scene] || context.sourceSceneSha256!==entry.sceneHashes?.[context.scene] || !entry.scenes.includes(context.scene) ||
    !entry.selectors.includes(object.selector) || !entry.rules.includes(rule))throw Error('Out-of-scope exception '+object.exceptionId);
  return entry;
}
export function validateGeometry(objects,tokens,context={},registry={exceptions:[]}) {
  const errors=[],exceptions=[],safe=safeBounds(tokens);
  for(const o of objects){
    if(o.exceptionId){exceptionFor(registry,context,o,'bottom-safe-area');exceptions.push({id:o.exceptionId,scene:context.scene,selector:o.selector});}
    const b=o.box;
    if(![b.x,b.y,b.width,b.height].every(Number.isFinite)||b.width<=0||b.height<=0){errors.push(`${o.id}:invalid-bounds`);continue;}
    if(b.x<safe.left-EPSILON||b.y<safe.top-EPSILON||b.x+b.width>safe.right+EPSILON)errors.push(`${o.id}:safe-area`);
    if(b.y+b.height>safe.bottom+EPSILON&&!exceptionFor(registry,context,o,'bottom-safe-area'))errors.push(`${o.id}:bottom-safe-area`);
    if(o.overflow)errors.push(`${o.id}:text-overflow`);
    if(o.radius!==undefined && !Object.values(tokens.radius).includes(o.radius))errors.push(`${o.id}:radius`);
    if(o.stroke!==undefined && !Object.values(tokens.stroke).includes(o.stroke))errors.push(`${o.id}:stroke`);
    if(o.originalAspect!==undefined && Math.abs(b.width/b.height/o.originalAspect-1)>0.001)errors.push(`${o.id}:aspect`);
    if(o.endpoint && Math.hypot(o.endpoint.x-o.target.x,o.endpoint.y-o.target.y)>EPSILON)errors.push(`${o.id}:anchor`);
  }
  for(let i=0;i<objects.length;i++)for(let j=i+1;j<objects.length;j++){
    const a=objects[i],b=objects[j];if(a.parent===b.id||b.parent===a.id||a.layer==='decoration'||b.layer==='decoration')continue;
    const x=Math.min(a.box.x+a.box.width,b.box.x+b.box.width)-Math.max(a.box.x,b.box.x);
    const y=Math.min(a.box.y+a.box.height,b.box.y+b.box.height)-Math.max(a.box.y,b.box.y);
    if(x>EPSILON&&y>EPSILON)errors.push(`${a.id}/${b.id}:overlap`);
    const distance=Math.hypot(Math.max(0,-x),Math.max(0,-y));
    if(distance<Math.max(a.minSpacing||0,b.minSpacing||0)-EPSILON)errors.push(`${a.id}/${b.id}:spacing`);
  }
  return {errors,exceptions};
}
