/** Real HyperFrames seek, geometry and screenshot regression. Baselines are read-only. */
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';
import {chromium} from '@playwright/test';import {PNG} from 'pngjs';import pixelmatch from 'pixelmatch';
import {validateGeometry} from './geometry.mjs';
const project=path.resolve(process.argv[2]),mode=process.argv[3]||'fixtures';
const here=path.dirname(new URL(import.meta.url).pathname),tokens=JSON.parse(fs.readFileSync(path.join(here,'tokens.v1.1.json')));
const qaScriptSha256=crypto.createHash('sha256').update(fs.readFileSync(new URL(import.meta.url))).digest('hex');
const profile=JSON.parse(fs.readFileSync(path.join(project,'production.json'))),out=path.resolve(project,'../qa/visual',mode);
const baseline=path.resolve(process.argv[4]||path.join(out,'golden'));fs.mkdirSync(out,{recursive:true});
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');const rows=[],failures=[],sources={},audioSources={};
const browser=await chromium.launch({executablePath:profile.runtime.browser,args:['--no-sandbox','--allow-file-access-from-files','--enable-unsafe-swiftshader']});
const environment={browser:browser.version(),viewport:[1920,1080],dpr:1,seed:0,hyperframes:profile.runtime.hyperframes,gsap:'3.14.2',playwright:'1.62.1',tokens:hash(fs.readFileSync(path.join(here,'tokens.v1.1.json'))),lock:hash(fs.readFileSync(path.join(here,'package-lock.json')))};
async function seek(page,t){await page.evaluate(async t=>{if(!window.__player?.renderSeek)throw Error('Actual HyperFrames runtime required');window.__player.renderSeek(t,{exact:true});await window.__hfWaitForSeekCompletion?.();await document.fonts.ready;},t);}
function diff(a,b,file){const x=PNG.sync.read(a),y=PNG.sync.read(b);if(x.width!==y.width||x.height!==y.height)throw Error('Image dimensions changed');const d=new PNG({width:x.width,height:x.height});const count=pixelmatch(x.data,y.data,d.data,x.width,x.height,{threshold:.05,includeAA:false});if(count)fs.writeFileSync(file,PNG.sync.write(d));return count;}
async function capture(page,name,t){
 await seek(page,t);const image=await page.screenshot({animations:'allow'}),file=name+'.png';fs.writeFileSync(path.join(out,file),image);
 const geometry=await page.evaluate(()=>{
  const visible=e=>{for(let p=e;p&&p!==document.body;p=p.parentElement){const s=getComputedStyle(p);if(+s.opacity===0||s.display==='none'||s.visibility==='hidden')return false;}return true;};
  const selector='.chapter,.heading,h1,.caption,.teaching,.question-title,.question,.option,.answer-mark,.quiz-clock,.card,.note';
  return [...document.querySelectorAll(selector)].filter(visible).map((e,i)=>{const b=e.getBoundingClientRect(),s=getComputedStyle(e);return {id:e.id||e.className||'text'+i,selector:e.classList.contains('caption')?'.caption':e.tagName,box:{x:b.x,y:b.y,width:b.width,height:b.height},overflow:e.scrollHeight>e.clientHeight+1&&s.overflow==='hidden',font:s.fontFamily,...(e.classList.contains('card')?{radius:parseFloat(s.borderRadius),stroke:parseFloat(s.borderWidth)}:{})};});
 });
 if(mode==='fixtures'){
  const anchorError=await page.evaluate(()=>{const line=document.querySelector('#connection'),a=document.querySelector('#sender').getBoundingClientRect(),b=document.querySelector('#reflector').getBoundingClientRect(),start=line.getPointAtLength(0),end=line.getPointAtLength(line.getTotalLength());return Math.max(Math.hypot(start.x-a.right,start.y-a.y-a.height/2),Math.hypot(end.x-b.left,end.y-b.y-b.height/2));});
  if(anchorError>.25)failures.push({name,kind:'anchor',error:anchorError});
 }
 const result=validateGeometry(geometry,tokens,{generation:'new'});if(result.errors.length)failures.push({name,kind:'geometry',errors:result.errors});
 const reference=path.join(baseline,file);let difference=null;
 if(fs.existsSync(reference)){const m=JSON.parse(fs.readFileSync(path.join(baseline,'manifest.json'))),row=m.rows.find(r=>r.file===file);if(!m.review||!row||row.sha256!==hash(fs.readFileSync(reference)))throw Error('Unreviewed or altered golden '+file);difference=diff(fs.readFileSync(reference),image,path.join(out,name+'-diff.png'));if(difference)failures.push({name,kind:'golden',pixels:difference});}
 const sequence=[0,t/2,t,Math.min(t+1,+(await page.locator('[data-composition-id]').first().getAttribute('data-duration'))),0,t,t];
 for(const destination of sequence)await seek(page,destination);
 const repeat=await page.screenshot({animations:'allow'});const seekDifference=diff(image,repeat,path.join(out,name+'-seek-diff.png'));if(seekDifference)failures.push({name,kind:'seek',pixels:seekDifference});
 rows.push({name,time:t,file,sha256:hash(image),geometry,exceptions:result.exceptions,golden_pixels:difference,seek_pixels:seekDifference});
}
try{
 const targets=mode==='fixtures'?['svg','pixi']:(process.env.CEH_QA_SCENES?.split(',')||['S17','S23','S50','S51','S52','S53','S54','S55','S56','S57']);
 for(const target of targets){
  const page=await browser.newPage({viewport:{width:1920,height:1080},deviceScaleFactor:1});const errors=[];page.on('pageerror',e=>errors.push(e.message));
  let file,times;
  if(mode==='fixtures'){file=path.join(project,'engineering',target+'.html');sources[target]=hash(fs.readFileSync(file));times=[0,1.2,2.4,5.966666666666667];}
  else{
   const source=fs.readFileSync(path.join(project,'compositions',target+'.html'),'utf8');
   sources[target]=hash(Buffer.from(source));audioSources[target]=hash(fs.readFileSync(path.join(project,'data',target+'.audio.json')));
   const body=source.match(/<template>([\s\S]*)<\/template>/)[1].replaceAll('url(assets/',`url(file://${project}/assets/`);
   file=path.join(out,target+'.html');fs.writeFileSync(file,`<!doctype html><html><head><script src="file://${project}/assets/vendor/gsap.min.js"></script><script>window.__timelines={}</script><style>html,body{margin:0;width:1920px;height:1080px}</style></head><body>${body}<script src="file://${project}/node_modules/hyperframes/dist/hyperframe-runtime.js"></script></body></html>`);
   const audio=JSON.parse(fs.readFileSync(path.join(project,'data',target+'.audio.json')));times=[0,audio.duration/2,audio.duration-1/30];
   for(const h of audio.segments.filter(x=>x.kind==='silence'))times.push(h.start_sample/48000-1/30,h.start_sample/48000,(h.start_sample+h.end_sample)/96000,h.end_sample/48000-1/30,h.end_sample/48000,h.end_sample/48000+1/30);
  }
  await page.goto('file://'+file);await page.waitForFunction(()=>window.__renderReady===true,null,{timeout:30000});await page.evaluate(()=>document.fonts.load('34px Editorial'));
  const timelineContract=await page.evaluate(()=>({version:window.gsap?.version,timelines:Object.values(window.__timelines||{}).map(t=>({duration:t.totalDuration(),scale:t.timeScale(),repeat:t.repeat()}))}));
  if(timelineContract.version!=='3.14.2'||!timelineContract.timelines.length||timelineContract.timelines.some(t=>!Number.isFinite(t.duration)||t.scale!==1||t.repeat!==0))throw Error('Finite 1x GSAP contract failed');
  if(mode==='fixtures'&&target==='pixi'){globalThis.webglInfo=await page.evaluate(()=>{const gl=document.querySelector('canvas').getContext('webgl2');if(!gl)return 'webgl2-unavailable';const ext=gl.getExtension('WEBGL_debug_renderer_info');return ext?gl.getParameter(ext.UNMASKED_RENDERER_WEBGL):gl.getParameter(gl.RENDERER);});const probe=await page.evaluate(()=>window.__pixiPluginProbe);if(probe!==50)throw Error('PixiPlugin probe failed');}
  for(const [i,t]of times.entries()){
   await capture(page,target+'-'+i,t);
   if(mode!=='fixtures'&&target>='S50'){
    const a=JSON.parse(fs.readFileSync(path.join(project,'data',target+'.audio.json'))),hold=a.segments.find(s=>s.kind==='silence');
    const answerOpacity=await page.locator('.answer-mark[id$="-answer"]').evaluate(e=>Number(getComputedStyle(e).opacity));
    if(t>=hold.end_sample/48000&&t<a.duration&&answerOpacity!==1)failures.push({name:target,time:t,kind:'missing-answer-at-reveal',answerOpacity});
    if(t<hold.end_sample/48000&&answerOpacity!==0)failures.push({name:target,time:t,kind:'premature-answer',answerOpacity});
    if(t>=hold.start_sample/48000&&t<hold.end_sample/48000){
     const bad=await page.evaluate(()=>[...document.querySelectorAll('.caption,.answer-mark[id$="-answer"]')].filter(e=>Number(getComputedStyle(e).opacity)>0).map(e=>e.id));if(bad.length)failures.push({name:target,time:t,kind:'early-answer-or-caption',elements:bad});
    }
   }
  }
  if(mode==='fixtures'){
   const timings=[];for(let i=0;i<30;i++){const start=performance.now();await seek(page,i/5);timings.push(performance.now()-start);}
   rows.filter(r=>r.name.startsWith(target+'-')).forEach(r=>r.seekTimingMs=timings);
   await seek(page,2.4);const clean=await page.screenshot();await page.locator('#sender').evaluate(e=>e.style.transform='translateX(1px)');const shifted=await page.screenshot();const pixels=diff(clean,shifted,path.join(out,target+'-one-pixel-negative.png'));if(pixels===0)failures.push({name:target,kind:'negative-control-undetected'});
  }
  // Font identity is checked by file hash as well as browser face readiness.
  if(!await page.evaluate(()=>document.fonts.check('34px Editorial')&&[...document.fonts].some(f=>f.family==='Editorial'&&f.status==='loaded')))failures.push({name:target,kind:'font'});
  if(errors.length)failures.push({name:target,kind:'runtime',errors});
  console.error(JSON.stringify({phase:'visual_qa',scene:target,captures:rows.length,failures:failures.length}));await page.close();
 }
 for(const [rel,expected]of Object.entries(tokens.fontHashes))if(hash(fs.readFileSync(path.join(project,rel)))!==expected)failures.push({kind:'font-hash',file:rel});
 for(const [rel,expected]of Object.entries(profile.locked_assets))if(hash(fs.readFileSync(path.join(project,rel)))!==expected)failures.push({kind:'asset-hash',file:rel});
 const goldenManifest=path.join(baseline,'manifest.json');
 if(fs.existsSync(goldenManifest)&&JSON.stringify(JSON.parse(fs.readFileSync(goldenManifest)).environment)!==JSON.stringify(environment))failures.push({kind:'golden-environment'});
}finally{await browser.close();}
const report={status:failures.length?'failed':rows.every(r=>r.golden_pixels===0)?'passed':'candidate_baseline_review_required',environment,qaScriptSha256,geometrySha256:hash(fs.readFileSync(new URL('./geometry.mjs',import.meta.url))),webgl:globalThis.webglInfo||null,sources,audioSources,exceptions:[],rows,failures};
fs.writeFileSync(path.join(out,'manifest.json'),JSON.stringify(report,null,2));console.log(JSON.stringify({status:report.status,captures:rows.length,failures:failures.length,report:path.join(out,'manifest.json')}));if(failures.length)process.exitCode=1;
