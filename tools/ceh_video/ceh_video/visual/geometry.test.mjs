import {test} from 'node:test';import assert from 'node:assert/strict';
import {safeBounds,port,connector,validateGeometry} from './geometry.mjs';
const tokens={canvas:{width:1920,height:1080},safeArea:{horizontal:.07,vertical:.08},radius:{card:8},stroke:{props:4}};
const object={id:'caption',selector:'.caption',box:{x:230,y:940,width:1460,height:50}};
const registry={exceptions:[{id:'LEGACY-M10-SUBTITLE-001',release:'optimization-v1',sourceProfileSha256:'verified',sceneHashes:{S23:'frozen-scene'},scenes:['S23'],selectors:['.caption'],rules:['bottom-safe-area']}]};
test('new caption bottom limited to 993.6',()=>{assert.equal(safeBounds(tokens).bottom,993.6);assert.deepEqual(validateGeometry([object],tokens).errors,[]);assert.ok(validateGeometry([{...object,box:{...object.box,height:55}}],tokens).errors.length)});
test('exceptions require exact frozen source, scene and selector',()=>{const bad={...object,exceptionId:'LEGACY-M10-SUBTITLE-001',box:{...object.box,height:88}};const context={generation:'frozen-legacy',release:'optimization-v1',sourceProfileSha256:'verified',sourceSceneSha256:'frozen-scene',scene:'S23'};assert.equal(validateGeometry([bad],tokens,context,registry).exceptions.length,1);for(const c of [{...context,generation:'new'},{...context,scene:'S24'},{...context,sourceProfileSha256:'changed'},{...context,sourceSceneSha256:'redesigned'}])assert.throws(()=>validateGeometry([bad],tokens,c,registry));assert.throws(()=>validateGeometry([{...bad,exceptionId:'unknown'}],tokens,context,registry));});
test('one pixel arrow error fails; transformed anchors recompute',()=>{const a={x:200,y:200,width:300,height:200},b={x:900,y:220,width:300,height:200};assert.deepEqual(connector(a,b).start,port(a,'right'));assert.equal(connector({...a,x:230},b).start.x,530);assert.ok(validateGeometry([{...object,endpoint:{x:1,y:0},target:{x:0,y:0}}],tokens).errors.includes('caption:anchor'));});
test('overlap, overflow, aspect, radius and stroke fail independently',()=>{const a={...object,radius:7,stroke:3,overflow:true,originalAspect:1};const errors=validateGeometry([a,{...object,id:'other'}],tokens).errors;for(const suffix of ['radius','stroke','text-overflow','aspect'])assert.ok(errors.includes(`caption:${suffix}`));assert.ok(errors.includes('caption/other:overlap'));});
import {component,grid,measureText} from './components.mjs';
test('grid, vector identity and intrinsic measurement reject invalid inputs',()=>{
 const t={...tokens,spacing:{medium:16}};assert.throws(()=>component('CharacterRig','tally',{x:0,y:0,width:27,height:30},t));
 assert.equal(component('CharacterRig','tally',{x:0,y:0,width:27,height:30},t,{assetSha256:'locked',viewBox:[0,0,270,300]}).originalAspect,.9);
 const cells=grid([{},{}],{x:200,y:300,width:800,height:200},{columns:2,gap:32});assert.equal(cells[1].box.x,616);
 const ctx={measureText:s=>({width:s.length*10})};assert.deepEqual(measureText('one two three',ctx,{font:'36px Editorial',maxWidth:70,lineHeight:42}).lines,['one two','three']);
 assert.throws(()=>measureText('overflow',ctx,{font:'36px Editorial',maxWidth:20,lineHeight:42}));
});
