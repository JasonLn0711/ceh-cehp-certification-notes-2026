/** Actual-browser regression for a decorative divider crossing a quiz title.
 * Runs unchanged production QA functions against disposable copied hosts only.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL,fileURLToPath} from 'node:url';
import {chromium} from '@playwright/test';
import {validateGeometry} from './geometry.mjs';
const root=path.resolve(process.argv[2]);
const out=path.resolve(root,'../qa/quiz-divider-negative');fs.mkdirSync(out,{recursive:true});
const read=f=>JSON.parse(fs.readFileSync(f));const hash=b=>crypto.createHash('sha256').update(b).digest('hex');const sha=f=>hash(fs.readFileSync(f));
const here=path.dirname(fileURLToPath(import.meta.url));const profile=read(path.join(root,'production.json'));const tokens=read(path.join(root,profile.token_manifest));
const harness=path.join(here,'remaster-qa.mjs'),code=fs.readFileSync(harness,'utf8');
const start=code.indexOf('async function geometry('),end=code.indexOf('async function quizCheck(',start);
if(start<0||end<0)throw Error('Production geometry function extraction contract changed');
const extracted=code.slice(start,end),failures=[];
const {geometry,checkGeometry}=new Function('tokens','failures','validateGeometry',extracted+'\nreturn {geometry,checkGeometry};')(tokens,failures,validateGeometry);
const rows=[],errors=[],sources={};let browser;
const report={status:'failed',scope:'Eight actual copied quiz compositions; unchanged production geometry/checkGeometry functions; injected divider exists only in disposable browser DOM. No golden promotion or production mutation.',harnessSha256:sha(harness),extractedFunctionsSha256:hash(extracted),scriptSha256:sha(fileURLToPath(import.meta.url)),tokensSha256:sha(path.join(root,profile.token_manifest)),geometrySha256:sha(path.join(here,'geometry.mjs')),hyperframesRuntimeSha256:sha(path.join(root,'node_modules/hyperframes/dist/hyperframe-runtime.js')),gsapSha256:sha(path.join(root,'assets/vendor/gsap.min.js')),browserExecutableSha256:sha(profile.runtime.browser),sources,rows,errors};
try{
 browser=await chromium.launch({executablePath:profile.runtime.browser,args:['--no-sandbox','--allow-file-access-from-files','--enable-unsafe-swiftshader']});
 report.browser=browser.version();
 for(const question of read(path.join(root,'data/questions.json')).questions){
  const sid=question.scene_id,source=path.join(root,'compositions',sid+'.html');sources[sid]=sha(source);
  const original=fs.readFileSync(source,'utf8'),match=original.match(/<template>([\s\S]*)<\/template>/);if(!match)throw Error('Missing template '+sid);
  const body=match[1].replaceAll('url(assets/',`url(${pathToFileURL(root+'/')}assets/`);
  const host=path.join(out,sid+'.html');fs.writeFileSync(host,`<!doctype html><html><head><script src="${pathToFileURL(root+'/assets/vendor/gsap.min.js')}"></script><script>window.__timelines={}</script><style>html,body{margin:0;width:1920px;height:1080px}</style></head><body>${body}<script src="${pathToFileURL(root+'/node_modules/hyperframes/dist/hyperframe-runtime.js')}"></script></body></html>`);
  const page=await browser.newPage({viewport:{width:1920,height:1080},deviceScaleFactor:1});
  try{
   await page.goto(pathToFileURL(host).href);await page.waitForFunction(()=>window.__renderReady===true);
   const a=read(path.join(root,'data',sid+'.audio.json')),hold=a.segments.find(r=>r.kind==='silence'),frame=hold.start_sample/1600+15;
   await page.evaluate(async frame=>{await document.fonts.load('34px Editorial');await document.fonts.load('bold 54px Editorial');window.__player.renderSeek(frame/30,{exact:true});await window.__hfWaitForSeekCompletion();await document.fonts.ready;},frame);
   const before=failures.length;const clean=await geometry(page);checkGeometry(sid+'-clean',clean);const cleanFailures=failures.slice(before);
   const cleanImage=await page.screenshot();fs.writeFileSync(path.join(out,sid+'-clean.png'),cleanImage);
   if(cleanFailures.length)throw Error(sid+' current quiz failed: '+JSON.stringify(cleanFailures));
   if(await page.locator('.editorial-rule').count())throw Error(sid+' unexpectedly retains production divider');
   await page.evaluate(()=>{const line=document.createElement('div');line.id='negative-editorial-rule';line.className='editorial-rule';Object.assign(line.style,{position:'absolute',left:'155px',top:'248px',width:'1610px',borderTop:'2px solid #B8B0A9',opacity:'1',display:'block',visibility:'visible'});document.body.appendChild(line);});
   const bad=await geometry(page),mark=failures.length;checkGeometry(sid+'-injected',bad);const injectedFailures=failures.slice(mark);
   const detected=injectedFailures.some(r=>r.kind==='visible-overlap'&&r.pairs.some(pair=>pair.includes('negative-editorial-rule')));
   if(!detected)throw Error(sid+' injected divider overlap escaped current production checker');
   const badImage=await page.screenshot();fs.writeFileSync(path.join(out,sid+'-injected.png'),badImage);
   await page.locator('#negative-editorial-rule').evaluate(e=>e.remove());const restoreStart=failures.length;checkGeometry(sid+'-restored',await geometry(page));if(failures.length!==restoreStart)throw Error(sid+' cleanup did not restore clean geometry');
   if(sha(source)!==sources[sid])throw Error('Production source changed during isolated test: '+sid);
   rows.push({scene:sid,frame,cleanFailures,injectedFailures,negativeControlDetected:true,restoredClean:true,productionSourceUnchanged:true,cleanImage:{file:sid+'-clean.png',sha256:hash(cleanImage)},injectedImage:{file:sid+'-injected.png',sha256:hash(badImage)}});
   console.error(JSON.stringify({phase:'quiz_divider_negative',scene:sid,status:'passed'}));
  }finally{await page.close();}
 }
 if(rows.length!==8)throw Error('Eight quiz regressions required');
 report.status='passed';
}catch(error){errors.push(String(error.stack||error));}finally{await browser?.close();}
fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(report,null,2));console.log(JSON.stringify({status:report.status,scenes:rows.length,report:path.join(out,'report.json')}));if(report.status!=='passed')process.exitCode=1;
