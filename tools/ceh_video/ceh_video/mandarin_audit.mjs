// Native deterministic timeline, Chinese text geometry and eight exact quiz boundaries.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import assert from 'node:assert/strict';import {createRequire} from 'node:module';
const root=process.cwd(),require=createRequire(path.join(root,'package.json')),puppeteer=require('puppeteer-core');
const out=path.resolve('../qa/scene-seek');fs.mkdirSync(out,{recursive:true});const quizOut=path.resolve('../qa/quiz-runtime');fs.mkdirSync(quizOut,{recursive:true});
const profile=JSON.parse(fs.readFileSync('production.json'));const quizSamples=Math.round(profile.quiz_silence_seconds*48000);
const scenes=JSON.parse(fs.readFileSync('data/scenes.json')).scenes,questions=JSON.parse(fs.readFileSync('data/questions.json')).questions;
const browser=await puppeteer.launch({executablePath:process.env.HYPERFRAMES_BROWSER_PATH,headless:true,args:['--no-sandbox','--allow-file-access-from-files']});const rows=[],quizzes=[];
try{for(const scene of scenes){const sid=scene.id,a=JSON.parse(fs.readFileSync(`data/${sid}.audio.json`));const body=fs.readFileSync(`compositions/${sid}.html`,'utf8').match(/<template>([\s\S]*)<\/template>/)[1].replaceAll('url(assets/',`url(file://${root}/assets/`);const file=path.join(out,sid+'.html');fs.writeFileSync(file,`<html><head><script src="file://${root}/assets/vendor/gsap.min.js"></script><script>window.__timelines={}</script><style>html,body{margin:0;width:1920px;height:1080px}</style></head><body>${body}</body></html>`);
const page=await browser.newPage();await page.setViewport({width:1920,height:1080});const errors=[];page.on('pageerror',e=>errors.push(e.message));await page.goto('file://'+file);await page.evaluate(async()=>{await document.fonts.ready});
const info=await page.evaluate(sid=>({duration:window.__timelines[sid].duration(),paused:window.__timelines[sid].paused()}),sid);assert(info.paused&&Number.isFinite(info.duration)&&info.duration>0);assert.equal(errors.length,0,JSON.stringify(errors));
async function pose(t){await page.evaluate(({sid,t})=>{window.__timelines[sid].seek(t,false);},{sid,t});return await page.evaluate(()=>[...document.querySelectorAll('[id]')].filter(el=>el.id!=='root').map(el=>{const s=getComputedStyle(el),m=new DOMMatrix(s.transform==='none'?undefined:s.transform);return {id:el.id,opacity:s.opacity,transform:[m.a,m.b,m.c,m.d,m.e,m.f],fill:s.fill,dash:s.strokeDashoffset,bg:s.backgroundColor}}))}
if(scene.kind!=='quiz'){await pose(1.5);const later=JSON.parse(fs.readFileSync(`data/${sid}.geometry.json`)).filter(o=>o.phase>0&&o.kind!=='line').map(o=>o.id);const exposed=await page.evaluate(ids=>ids.filter(id=>Number(getComputedStyle(document.getElementById(id)).opacity)!==0),later);assert.equal(exposed.length,0,sid+' future teaching phase visible early: '+exposed.join(','));}
const times=[a.duration*.12,a.duration*.5,a.duration*.9],states=[];for(const t of times)states.push(await pose(t));for(const i of [1,0,2])assert.deepEqual(await pose(times[i]),states[i],sid+' repeated/reverse seek');
await pose(a.duration-.5);const geometry=await page.evaluate(()=>[...document.querySelectorAll('svg text,.heading,.teaching,.question,.option,.caption')].filter(e=>{const s=getComputedStyle(e);if(Number(s.opacity)===0)return false;const b=e.getBoundingClientRect();return b.width&&b.height&&(b.left<90||b.right>1830||b.top<60||b.bottom>1065)}).map(e=>({text:e.textContent,box:e.getBoundingClientRect().toJSON()})));assert.equal(geometry.length,0,sid+' unsafe text '+JSON.stringify(geometry));
const panelFile=`data/${sid}.panels.json`;
if(profile.teaching_panels&&fs.existsSync(panelFile)){
 const panels=JSON.parse(fs.readFileSync(panelFile)).states;
 for(const [i,state]of panels.entries()){
  const t=Math.min(state.end-.05,state.start+1);await pose(t);
  const proof=await page.evaluate(id=>{
   const nodes=[...document.querySelectorAll('.source-panel')].filter(e=>Number(getComputedStyle(e).opacity)>0);
   const el=document.getElementById(id),b=el.getBoundingClientRect(),img=el.querySelector('img');
   return {visible:nodes.map(n=>n.id),loaded:img.complete&&img.naturalWidth>0,box:[b.left,b.top,b.right,b.bottom],overflow:[...el.querySelectorAll('.source-title,.source-note')].some(n=>n.scrollHeight>n.clientHeight+2)};
  },`${sid}-source-${i}`);
  assert.deepEqual(proof.visible,[`${sid}-source-${i}`],sid+' picture cue mismatch');
  assert(proof.loaded&&!proof.overflow&&proof.box[0]>=1338&&proof.box[2]<=1792&&proof.box[3]<=642,sid+' picture safety');
  const stateA=await pose(t);await pose(Math.max(0,state.start-.1));assert.deepEqual(await pose(t),stateA,sid+' picture reverse seek');
 }
}
const q=questions.find(q=>q.scene_id===sid);if(q){const hold=a.segments.find(x=>x.kind==='silence'),start=hold.start_sample/48000,end=hold.end_sample/48000;assert.equal(hold.end_sample-hold.start_sample,quizSamples);
const cases=[{at:start-.02,clock:false,answer:false},{at:end+2,clock:false,answer:true},{at:start+.01,clock:true,answer:false},{at:(start+end)/2,clock:true,answer:false},{at:end-.01,clock:true,answer:false},{at:end+.01,clock:false,answer:true},{at:end,clock:false,answer:true},{at:(start+end)/2,clock:true,answer:false}];
for(const c of cases){await pose(c.at);const state=await page.evaluate(({sid,key})=>({clock:Number(getComputedStyle(document.getElementById(sid+'-clock')).opacity),answer:Number(getComputedStyle(document.getElementById(sid+'-answer')).opacity),background:getComputedStyle(document.getElementById(sid+'-'+key)).backgroundColor,captions:[...document.querySelectorAll('.caption')].filter(e=>Number(getComputedStyle(e).opacity)>0).map(e=>e.textContent)}),{sid,key:q.correct_letter});assert.equal(state.clock,c.clock?1:0);assert.equal(state.answer,c.answer?1:0);if(c.clock){assert.equal(state.background,'rgb(255, 250, 243)');assert.equal(state.captions.length,0)}quizzes.push({scene:sid,question:q.id,...c,state});}
await pose((start+end)/2);await page.screenshot({path:path.join(quizOut,q.id+'-pause.png')});await pose(end+2);await page.screenshot({path:path.join(quizOut,q.id+'-answer.png')});}
rows.push({scene:sid,comparisons:3,paused:true,timeline_duration:info.duration,measured_duration:a.duration,state_sha256:crypto.createHash('sha256').update(JSON.stringify(states)).digest('hex'),status:'passed'});await page.close();console.log(JSON.stringify({phase:'mandarin_native_runtime',completed:rows.length,total:scenes.length}));}}
finally{await browser.close()}
fs.writeFileSync(path.resolve('../qa/scene-seek-audit.json'),JSON.stringify({status:'passed',scenes:rows.length,comparisons:rows.length*3,rows},null,2));fs.writeFileSync(path.join(quizOut,'checks.json'),JSON.stringify({status:'passed',quiz_seconds:profile.quiz_silence_seconds,checks:quizzes.length,results:quizzes},null,2));
