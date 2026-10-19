import puppeteer from 'puppeteer-core';
import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
const root=process.cwd(),out=path.resolve(root,'../qa/quiz-runtime');
fs.mkdirSync(out,{recursive:true});
const seconds=JSON.parse(fs.readFileSync('data/production-overrides.json')).quiz_silence_seconds;
const browser=await puppeteer.launch({executablePath:process.env.HYPERFRAMES_BROWSER_PATH||'/home/jnlngx10/.cache/ms-playwright/chromium_headless_shell-1234/chrome-linux/headless_shell',headless:true,args:['--no-sandbox','--allow-file-access-from-files']});
const results=[];
try {
 const page=await browser.newPage();await page.setViewport({width:1920,height:1080});
 const questions=JSON.parse(fs.readFileSync('data/questions.json')).questions;
 for(let n=54;n<=57;n++) {
  const sid=`S${n}`,html=fs.readFileSync(`compositions/${sid}.html`,'utf8');
  assert(html.includes(`${seconds} second each`));assert(!html.includes('12 seconds each'));
  const body=html.match(/<template>([\s\S]*)<\/template>/)[1].replaceAll('url(assets/',`url(file://${root}/assets/`);
  const file=path.join(out,sid+'.html');
  fs.writeFileSync(file,`<html><head><script src="file://${root}/assets/vendor/gsap.min.js"></script><script>window.__timelines={}</script><style>html,body{width:1920px;height:1080px}</style></head><body>${body}</body></html>`);
  await page.goto('file://'+file);await page.evaluate(async()=>{await document.fonts.ready;});
  const audio=JSON.parse(fs.readFileSync(`data/${sid}.audio.json`));
  for(const [i,p] of audio.segments.filter(s=>s.kind==='silence').entries()) {
   const q=questions.filter(q=>q.scene_id===sid)[i],start=p.start_sample/48000,end=p.end_sample/48000;
   assert(Math.abs(end-start-seconds)<1e-6);
   const midpoint=(start+end)/2;
   const cases=[{at:start-.02,clock:false,answer:false},{at:end+2,clock:false,answer:true},{at:start+.01,clock:true,answer:false},{at:midpoint,clock:true,answer:false},{at:end-.01,clock:true,answer:false},{at:end+.01,clock:false,answer:true},{at:end,clock:false,answer:true},{at:midpoint,clock:true,answer:false}];
   for(const c of cases) {
    await page.evaluate(({sid,at})=>{window.__timelines[sid].seek(at,false);},{sid,at:c.at});
    const state=await page.evaluate(({sid,q})=>{
     const id=sid+'-'+q.id,clock=document.getElementById(id+'-clock'),answer=document.getElementById(id+'-answer');
     return {clockOpacity:Number(getComputedStyle(clock).opacity),clock:clock.textContent,answerOpacity:Number(getComputedStyle(answer).opacity),correctBackground:getComputedStyle(document.getElementById(id+'-'+q.correct_letter)).backgroundColor};
    },{sid,q});
    const diagnostic=JSON.stringify({sid,question:q.id,...c,state});assert.equal(state.clockOpacity,c.clock?1:0,diagnostic);assert.equal(state.answerOpacity,c.answer?1:0,diagnostic);
    if(c.clock) {assert.equal(state.clock,String(Math.max(1,Math.ceil(end-c.at-1e-6))));assert.equal(state.correctBackground,'rgb(255, 250, 243)');}
    results.push({scene:sid,question:q.id,...c,state});
   }
   await page.screenshot({path:path.join(out,q.id+'-pause.png')});
   await page.evaluate(({sid,at})=>{window.__timelines[sid].seek(at,false);},{sid,at:end+2});
   await page.screenshot({path:path.join(out,q.id+'-answer.png')});
  }
 }
} finally {await browser.close();}
fs.writeFileSync(path.join(out,'checks.json'),JSON.stringify({source:'actual compiled compositions and final measured audio metadata',quiz_seconds:seconds,checks:results.length,status:'passed',results},null,2));
console.log(JSON.stringify({quizRuntimeChecks:results.length,quizSeconds:seconds,status:'passed'}));
