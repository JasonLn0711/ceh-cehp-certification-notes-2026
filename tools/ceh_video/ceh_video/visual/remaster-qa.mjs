/** Full M10 coverage through actual HyperFrames seek; never writes golden baselines. */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {chromium} from '@playwright/test';
import {PNG} from 'pngjs';
import pixelmatch from 'pixelmatch';
import {validateGeometry} from './geometry.mjs';

function hashScope(ids){return crypto.createHash('sha256').update(ids.join(',')).digest('hex').slice(0,12);}
const project=path.resolve(process.argv[2]);
const here=path.dirname(fileURLToPath(import.meta.url));
const selected=process.env.CEH_QA_SCENES?.split(',');
const diagnostic=process.env.CEH_QA_SCENE,precheck=process.argv.includes('--precheck');
const attempt=process.env.CEH_QA_RUN_ID?'-'+process.env.CEH_QA_RUN_ID:'';
const out=path.resolve(project,precheck?'../qa/visual/precheck'+attempt:diagnostic?'../qa/visual/diagnostic-'+diagnostic+attempt:selected?'../qa/visual/scoped-'+hashScope(selected)+attempt:'../qa/visual/scenes');
const baseline=path.resolve((!precheck&&process.argv[3])||((selected||diagnostic)?path.resolve(project,'../qa/visual/scenes/golden'):path.join(out,'golden')));
const read=f=>JSON.parse(fs.readFileSync(f));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const fileHash=f=>hash(fs.readFileSync(f));
const profile=read(path.join(project,'production.json'));
const tokenFile=profile.token_manifest?path.join(project,profile.token_manifest):path.join(here,'tokens.v1.1.json');
const tokens=read(tokenFile);
const scenes=read(path.join(project,'data/scenes.json')).scenes;
const activeScenes=scenes.filter(s=>(!diagnostic||s.id===diagnostic)&&(!selected||selected.includes(s.id)));
if(selected&&(new Set(selected).size!==selected.length||selected.some(id=>!scenes.some(s=>s.id===id))))throw Error('Invalid or duplicate selected scene');
if(!activeScenes.length)throw Error('No matching scenes');
const questions=read(path.join(project,'data/questions.json')).questions;
const quizScenes=new Set(questions.map(q=>q.scene_id));
const rows=[],failures=[],sources={},audioSources={},layoutSources={},sceneSpecSources={},cueSources={},requiredStates={},allFrames=[],holdChecks=[],textLayouts=[];
fs.mkdirSync(out,{recursive:true});
const goldenManifest=!precheck&&fs.existsSync(path.join(baseline,'manifest.json'))?read(path.join(baseline,'manifest.json')):null;
const browser=await chromium.launch({executablePath:profile.runtime.browser,args:['--no-sandbox','--allow-file-access-from-files','--enable-unsafe-swiftshader']});
const environment={browser:browser.version(),viewport:[1920,1080],dpr:1,seed:0,hyperframes:profile.runtime.hyperframes,gsap:'3.14.2',playwright:'1.62.1',tokens:fileHash(tokenFile),lock:fileHash(path.join(here,'package-lock.json')),fontHashes:tokens.fontHashes};

async function seek(page,frame){
 await page.evaluate(async frame=>{
  if(!window.__player?.renderSeek||!window.__hfWaitForSeekCompletion)throw Error('Actual HyperFrames render/seek barrier required');
  window.__player.renderSeek(frame/30,{exact:true});
  await window.__hfWaitForSeekCompletion();await document.fonts.ready;
 },frame);
}
function diff(a,b,name){
 if(a.equals(b))return 0;
 const x=PNG.sync.read(a),y=PNG.sync.read(b);
 if(x.width!==y.width||x.height!==y.height)throw Error('Screenshot dimensions changed');
 const d=new PNG({width:x.width,height:x.height});
 const pixels=pixelmatch(x.data,y.data,d.data,x.width,x.height,{threshold:.05,includeAA:false});
 if(pixels)fs.writeFileSync(path.join(out,name+'.png'),PNG.sync.write(d));
 return pixels;
}
function framePlan(audio,cues){
 const length=audio.samples/1600;
 if(!Number.isInteger(length)||length<1)throw Error('Frame-aligned audio required');
 const clamp=n=>Math.max(0,Math.min(length-1,Math.round(n)));
 const frames=new Set([0,clamp(length*.15),clamp(length*.5),clamp(length*.85),length-1]);
 for(const cue of cues){if(!Number.isFinite(cue.start)||!Number.isFinite(cue.end)||cue.end<=cue.start)throw Error('Invalid narration label window');frames.add(clamp((cue.start+cue.end)*15));}
 for(const hold of audio.segments.filter(s=>s.kind==='silence')){
  const start=hold.start_sample/1600,end=hold.end_sample/1600;
  if(!Number.isInteger(start)||!Number.isInteger(end)||end-start!==30)throw Error('Quiz hold must contain exactly30 aligned video frames');
  for(const frame of [start-1,start,start+1,start+7,start+15,start+22,end-1,end,end+1])frames.add(clamp(frame));
 }
 return [...frames].sort((a,b)=>a-b);
}
async function geometry(page,includeHidden=false){
 return page.evaluate(({includeHidden,tokens})=>{
  const visible=e=>{for(let p=e;p&&p!==document.body;p=p.parentElement){const s=getComputedStyle(p);if(Number(s.opacity)===0||s.display==='none'||s.visibility==='hidden')return false;}return true;};
  const selector='.editorial-rule,.simulation-label,.chapter,.heading,.caption,.teaching,.question-title,.question,.option,.answer-mark,.quiz-clock,svg text';
  const els=[...document.querySelectorAll(selector)].filter(e=>includeHidden||visible(e));
  const objects=els.map((e,i)=>{
   const b=e.getBoundingClientRect(),style=getComputedStyle(e),node=e.closest('.remaster-node');
   const id=e.id||`${e.tagName}-${i}`;
   const result={id,selector:e.classList.contains('caption')?'.caption':e.tagName,text:e.textContent.trim(),box:{x:b.x,y:b.y,width:b.width,height:b.height},font:style.fontFamily,overflow:e instanceof HTMLElement&&(e.scrollWidth>e.clientWidth+1||e.scrollHeight>e.clientHeight+1)};
   if(node&&e!==node){
    const rect=node.querySelector('rect.card-frame')||node.querySelector('rect');
    if(e.matches('text[data-node-label]')){
     const inner={x:Number(e.dataset.innerX),y:Number(e.dataset.innerY),width:Number(e.dataset.innerWidth),height:Number(e.dataset.innerHeight)},local=e.getBBox();
     result.localBox={x:local.x,y:local.y,width:local.width,height:local.height};result.localInner=inner;
    }
    if(rect&&!result.localInner){const bounds=rect.getBoundingClientRect(),padding=Number(node.dataset.padding??rect.dataset.padding??0);result.parentBox={x:bounds.x+padding,y:bounds.y+padding,width:bounds.width-2*padding,height:bounds.height-2*padding};}
   }
   const family=style.fontFamily.split(',')[0].replace(/["']/g,'').trim();
   result.fontLoaded=document.fonts.check(`${style.fontSize} "${family}"`)&&[...document.fonts].some(f=>f.family.replace(/["']/g,'')===family&&f.status==='loaded');
   return result;
  }).filter(x=>x.text);
  const nodeBoxes=[...document.querySelectorAll('.remaster-node')].filter(visible).map((node,i)=>{const rect=node.querySelector('[data-component-bounds]')||node.querySelector('rect.card-frame');if(!rect)return null;const b=rect.getBoundingClientRect(),style=getComputedStyle(rect);return {id:node.id||'node-'+i,box:{x:b.x,y:b.y,width:b.width,height:b.height},...(rect.classList.contains('card-frame')?{radius:Number(rect.getAttribute('rx')||0),stroke:parseFloat(style.strokeWidth)}:{})};}).filter(Boolean);
  const overlaps=[];
  if(!includeHidden){for(let i=0;i<els.length;i++)for(let j=i+1;j<els.length;j++){
   const a=els[i],b=els[j];if(a.contains(b)||b.contains(a))continue;
   if(!(a.matches('.editorial-rule,.simulation-label,.caption,.teaching,.heading,.chapter,.question-title,.question,.option,.answer-mark,.quiz-clock')||b.matches('.editorial-rule,.simulation-label,.caption,.teaching,.heading,.chapter,.question-title,.question,.option,.answer-mark,.quiz-clock')))continue;
   const x=a.getBoundingClientRect(),y=b.getBoundingClientRect();
   if(Math.min(x.right,y.right)-Math.max(x.left,y.left)>.25&&Math.min(x.bottom,y.bottom)-Math.max(x.top,y.top)>.25)overlaps.push([a.id||a.tagName,b.id||b.tagName]);
  }}
  if(!includeHidden){for(const caption of objects.filter(o=>o.selector==='.caption'))for(const node of nodeBoxes){const a=caption.box,b=node.box;if(Math.min(a.x+a.width,b.x+b.width)-Math.max(a.x,b.x)>.25&&Math.min(a.y+a.height,b.y+b.height)-Math.max(a.y,b.y)>.25)overlaps.push([caption.id,node.id]);}}
  return {objects,nodeBoxes,overlaps,headings:[...document.querySelectorAll('.heading')].filter(visible).map(e=>e.textContent.trim())};
 },{includeHidden,tokens});
}
function checkGeometry(name,result){
 for(const node of result.nodeBoxes){const checked=validateGeometry([node],tokens,{generation:'new'});if(checked.errors.length)failures.push({name,kind:'node-geometry',errors:checked.errors});}
 for(const object of result.objects){
  // Each text object is checked independently; containment is not illegal overlap.
  const checked=validateGeometry([object],tokens,{generation:'new'});
  if(checked.errors.length)failures.push({name,kind:'geometry',errors:checked.errors});
  if(!object.fontLoaded)failures.push({name,kind:'font-not-loaded',id:object.id,font:object.font});
  if(object.localInner){const a=object.localBox,b=object.localInner;if(!Object.values(b).every(Number.isFinite)||a.x<b.x-.25||a.y<b.y-.25||a.x+a.width>b.x+b.width+.25||a.y+a.height>b.y+b.height+.25)failures.push({name,kind:'node-inner-text-overflow',id:object.id,box:a,parent:b});}
  if(object.parentBox){const a=object.box,b=object.parentBox;if(a.x<b.x-.25||a.y<b.y-.25||a.x+a.width>b.x+b.width+.25||a.y+a.height>b.y+b.height+.25)failures.push({name,kind:'node-text-overflow',id:object.id,box:a,parent:b});}
 }
 if(result.overlaps.length)failures.push({name,kind:'visible-overlap',pairs:result.overlaps});
}
async function quizCheck(page,sid,frame,hold){
 const state=await page.evaluate(()=>{
  const visible=e=>{for(let p=e;p&&p!==document.body;p=p.parentElement){const s=getComputedStyle(p);if(Number(s.opacity)===0||s.display==='none'||s.visibility==='hidden')return false;}return true;};
  return {answers:[...document.querySelectorAll('.answer-mark[id$="-answer"]')].filter(visible).map(e=>e.id),captions:[...document.querySelectorAll('.caption')].filter(visible).map(e=>e.id)};
 });
 const start=hold.start_sample/1600,end=hold.end_sample/1600;
 if(frame<end&&state.answers.length)failures.push({scene:sid,frame,kind:'premature-answer',state});
 if(frame>=end&&!state.answers.length)failures.push({scene:sid,frame,kind:'missing-answer',state});
 if(frame>=start&&frame<end&&(state.captions.length||state.answers.length))failures.push({scene:sid,frame,kind:'nonempty-quiz-hold',state});
 return state;
}
async function capture(page,scene,audio,frame){
 const name=`${scene.id}-f${String(frame).padStart(6,'0')}`,file=name+'.png';
 await seek(page,frame);
 const state=await geometry(page);checkGeometry(name,state);
 if(!state.headings.includes(scene.title))failures.push({name,kind:'missing-canonical-heading',expected:scene.title,actual:state.headings});
 const image=await page.screenshot({animations:'allow'});fs.writeFileSync(path.join(out,file),image);
 let goldenPixels=null;
 const reference=path.join(baseline,file);
 if(fs.existsSync(reference)){
  const row=goldenManifest?.rows?.find(r=>r.name===name&&r.file===file);
  if(!goldenManifest?.review||!row||row.sha256!==fileHash(reference))throw Error('Unreviewed/altered golden '+file);
  goldenPixels=diff(fs.readFileSync(reference),image,name+'-diff');
  if(goldenPixels)failures.push({name,kind:'golden',pixels:goldenPixels});
 }
 const comparisons={};
 const sequences={forward:[0,Math.floor(frame/2),frame],reverse:[Math.min(audio.samples/1600-1,frame+30),frame],repeated:[frame,frame]};
 for(const [kind,sequence]of Object.entries(sequences)){
  for(const destination of sequence)await seek(page,destination);
  comparisons[kind]=diff(image,await page.screenshot({animations:'allow'}),name+'-'+kind+'-diff');
  if(comparisons[kind])failures.push({name,kind:'seek-'+kind,pixels:comparisons[kind]});
 }
 const hold=audio.segments.find(s=>s.kind==='silence');if(hold)await quizCheck(page,scene.id,frame,hold);
 rows.push({name,scene:scene.id,frame,time:frame/30,file,sha256:hash(image),geometry:state.objects,exceptions:[],golden_pixels:goldenPixels,seek_pixels:Math.max(...Object.values(comparisons)),seek_comparisons:comparisons});
}

try{
 if(scenes.length!==58||quizScenes.size!==8)throw Error('Full M10 release requires58scenes and8quiz scenes');
 for(const scene of activeScenes){
  const sid=scene.id,sourceFile=path.join(project,'compositions',sid+'.html'),audioFile=path.join(project,'data',sid+'.audio.json'),cueFile=path.join(project,'data',sid+'.label-cues.json');
  const source=fs.readFileSync(sourceFile,'utf8'),audio=read(audioFile),cues=fs.existsSync(cueFile)?read(cueFile):[];
  sources[sid]=fileHash(sourceFile);audioSources[sid]=fileHash(audioFile);layoutSources[sid]=fileHash(path.join(project,'data',sid+'.layout.json'));sceneSpecSources[sid]=fileHash(path.join(project,'data',sid+'.scene-spec.json'));cueSources[sid]=fs.existsSync(cueFile)?fileHash(cueFile):null;
  const frames=framePlan(audio,cues);for(const frame of frames)requiredStates[`${sid}-f${String(frame).padStart(6,'0')}`]=frame;
  const match=source.match(/<template>([\s\S]*)<\/template>/);if(!match)throw Error('Missing scene template '+sid);
  const body=match[1].replaceAll('url(assets/',`url(${pathToFileURL(project+'/').href}assets/`);
  const file=path.join(out,sid+'.html');fs.writeFileSync(file,`<!doctype html><html><head><script src="${pathToFileURL(project+'/assets/vendor/gsap.min.js')}"></script><script>window.__timelines={}</script><style>html,body{margin:0;width:1920px;height:1080px}</style></head><body>${body}<script src="${pathToFileURL(project+'/node_modules/hyperframes/dist/hyperframe-runtime.js')}"></script></body></html>`);
  const page=await browser.newPage({viewport:{width:1920,height:1080},deviceScaleFactor:1}),errors=[];page.on('pageerror',error=>errors.push(error.message));
  try{
   await page.goto(pathToFileURL(file).href);await page.waitForFunction(()=>window.__renderReady===true,null,{timeout:30000});
   await page.evaluate(async()=>{await document.fonts.load('34px Editorial');await document.fonts.load('bold 54px Editorial');await document.fonts.load('30px Technical');await document.fonts.ready;});
   const contract=await page.evaluate(()=>({version:window.gsap?.version,timelines:Object.values(window.__timelines||{}).map(t=>({duration:t.totalDuration(),scale:t.timeScale(),repeat:t.repeat()}))}));
   if(contract.version!=='3.14.2'||!contract.timelines.length||contract.timelines.some(t=>!Number.isFinite(t.duration)||t.scale!==1||t.repeat!==0))throw Error('Finite1xGSAP contract failed '+sid);
   if(!quizScenes.has(sid)){
    const checked=await page.evaluate(sid=>{const api=window.__cehRemaster?.[sid];if(!api?.state||!api?.validateAllFrames||!api.layout||!api.spec)throw Error('Remaster geometry API missing '+sid);return {validation:api.validateAllFrames(),layout:api.layout};},sid);
    if(checked.validation.frames!==audio.samples/1600||checked.validation.errors.length)failures.push({scene:sid,kind:'all-frame-geometry',validation:checked.validation});
    allFrames.push({scene:sid,...checked.validation});
   }
   await seek(page,Math.floor(audio.samples/3200));
   const unique=await geometry(page,true);checkGeometry(sid+'-all-text',unique);textLayouts.push({scene:sid,objects:unique.objects});
   if(!precheck)for(const frame of frames)await capture(page,scene,audio,frame);
   if(!precheck)for(const hold of audio.segments.filter(s=>s.kind==='silence')){
    for(let frame=hold.start_sample/1600;frame<hold.end_sample/1600;frame++){await seek(page,frame);holdChecks.push({scene:sid,frame,...await quizCheck(page,sid,frame,hold)});}
   }
   if(errors.length)failures.push({scene:sid,kind:'runtime',errors});
  }finally{await page.close();}
  fs.writeFileSync(path.join(out,'failures.partial.json'),JSON.stringify(failures,null,2));
  console.error(JSON.stringify({phase:'remaster_visual_qa',scene:sid,scenes_completed:activeScenes.indexOf(scene)+1,total_scenes:activeScenes.length,captures:rows.length,failures:failures.length}));
 }
 for(const [rel,expected]of Object.entries(tokens.fontHashes))if(fileHash(path.join(project,rel))!==expected)failures.push({kind:'font-hash',file:rel});
 for(const [rel,expected]of Object.entries(profile.locked_assets))if(fileHash(path.join(project,rel))!==expected)failures.push({kind:'asset-hash',file:rel});
 if(goldenManifest&&JSON.stringify(goldenManifest.environment)!==JSON.stringify(environment))failures.push({kind:'golden-environment'});
 if(goldenManifest){
  const required=(selected||diagnostic)?Object.fromEntries(Object.entries(goldenManifest.requiredStates).filter(([name])=>activeScenes.some(s=>name.startsWith(s.id+'-')))):goldenManifest.requiredStates;
  if(JSON.stringify(required)!==JSON.stringify(requiredStates))failures.push({kind:'golden-required-states'});
 }
 if(!precheck&&(rows.length!==Object.keys(requiredStates).length||activeScenes.some(s=>!rows.some(r=>r.scene===s.id))))failures.push({kind:'incomplete-coverage'});
 if(!precheck&&holdChecks.length!==activeScenes.filter(s=>quizScenes.has(s.id)).length*30)failures.push({kind:'incomplete-quiz-frame-coverage',actual:holdChecks.length});
}catch(error){failures.push({kind:'fatal',message:error.stack||String(error)});}finally{await browser.close();}
const report={scope:selected?'selected':diagnostic?'diagnostic':'full',selectedScenes:selected||null,status:failures.length?'failed':precheck?'precheck_passed':rows.length&&rows.every(r=>r.golden_pixels===0)?'passed':'candidate_baseline_review_required',environment,qaScriptSha256:fileHash(fileURLToPath(import.meta.url)),geometrySha256:fileHash(path.join(here,'remaster-geometry.mjs')),textGeometrySha256:fileHash(path.join(here,'geometry.mjs')),runtimeSha256:fileHash(path.join(here,'remaster-runtime.js')),hyperframesRuntimeSha256:fileHash(path.join(project,'node_modules/hyperframes/dist/hyperframe-runtime.js')),gsapSha256:fileHash(path.join(project,'assets/vendor/gsap.min.js')),browserExecutableSha256:fileHash(profile.runtime.browser),sources,audioSources,layoutSources,sceneSpecSources,cueSources,requiredStates,allFrames,holdChecks,textLayouts,exceptions:[],rows,failures};
fs.writeFileSync(path.join(out,'manifest.json'),JSON.stringify(report,null,2));
console.log(JSON.stringify({status:report.status,captures:rows.length,failures:failures.length,report:path.join(out,'manifest.json')}));
if(failures.length)process.exitCode=1;
