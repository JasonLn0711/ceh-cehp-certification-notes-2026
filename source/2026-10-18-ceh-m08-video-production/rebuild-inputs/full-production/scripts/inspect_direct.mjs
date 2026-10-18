// Independent native-scene seek inspection; supplements CLI chapter snapshots.
import fs from 'node:fs';import path from 'node:path';import puppeteer from 'puppeteer-core';
const root=process.cwd(),chapter=process.argv[2],out=path.resolve('../qa',chapter+'-direct');fs.mkdirSync(out,{recursive:true});
const scenes=JSON.parse(fs.readFileSync('data/scenes.json')).scenes.filter(s=>s.chapter_id===chapter);
const browser=await puppeteer.launch({executablePath:process.env.HYPERFRAMES_BROWSER_PATH||'/home/jnlngx10/.cache/ms-playwright/chromium_headless_shell-1234/chrome-linux/headless_shell',headless:true,args:['--no-sandbox','--allow-file-access-from-files']});
const rows=[];
try{
for(const s of scenes){const page=await browser.newPage();await page.setViewport({width:1920,height:1080});const sid=s.id,a=JSON.parse(fs.readFileSync(`data/${sid}.audio.json`)),body=fs.readFileSync(`compositions/${sid}.html`,'utf8').match(/<template>([\s\S]*)<\/template>/)[1].replaceAll('url(assets/',`url(file://${root}/assets/`);
const file=path.join(out,sid+'.html');fs.writeFileSync(file,`<html><head><script src="file://${root}/assets/vendor/gsap.min.js"></script><script>window.__timelines={}</script><style>html,body{margin:0;width:1920px;height:1080px}</style></head><body>${body}</body></html>`);await page.goto('file://'+file);await page.evaluate(async()=>{await document.fonts.ready});
for(const [phase,t] of [['middle',a.duration/2],['reason',a.duration-4]]){await page.evaluate(({sid,t})=>{window.__timelines[sid].seek(t,false)},{sid,t});await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))));const state=await page.evaluate(sid=>Array.from(document.querySelectorAll(`[id^="${sid}-"]`)).filter(e=>/tally|stamp|campus/.test(e.id)).map(e=>({id:e.id,opacity:getComputedStyle(e).opacity})),sid);await page.screenshot({path:path.join(out,`${sid}-${phase}.png`)});rows.push({scene:sid,phase,time:t,state});}
await page.close();console.log(JSON.stringify({scene:sid,phase:'native_seek_frames_captured'}));}
}finally{await browser.close()}
fs.writeFileSync(path.join(out,'receipt.json'),JSON.stringify({scope:'Direct native GSAP scene capture; actual encoded output is a separate gate',rows},null,2));
