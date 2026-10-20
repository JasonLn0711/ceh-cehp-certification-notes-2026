// Real nested HyperFrames composition boundary replay, independent of natural playback.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import {chromium} from '@playwright/test';import {PNG} from 'pngjs';import pixelmatch from 'pixelmatch';
const root=path.resolve(process.argv[2]),out=path.resolve(root,'../qa/cross-scene-seek');fs.mkdirSync(out,{recursive:true});
const profile=JSON.parse(fs.readFileSync(path.join(root,'production.json'))),scenes=JSON.parse(fs.readFileSync(path.join(root,'data/scenes.json'))).scenes.filter(s=>s.chapter_id==='C04');
let cursor=0,boundary;for(const scene of scenes){cursor+=JSON.parse(fs.readFileSync(path.join(root,'data',scene.id+'.audio.json'))).duration;if(scene.id==='S17')boundary=cursor;}
if(!boundary)throw Error('Missing S17 boundary');
const folder=path.join(root,'chapters/C04'),source=fs.readFileSync(path.join(folder,'index.html'),'utf8');
if(profile.runtime.hyperframes!=='0.8.174')throw Error('Revalidate pinned compiler adapter before changing HyperFrames');
const {bundleToSingleHtml}=await import('file://'+path.join(root,'node_modules/hyperframes/dist/compiler-O5R3ZZDV.js'));
const html=(await bundleToSingleHtml(folder)).replace('<head>',`<head><base href="file://${folder}/">`);
const file=path.join(out,'C04.html');fs.writeFileSync(file,html);
const browser=await chromium.launch({executablePath:profile.runtime.browser,args:['--no-sandbox','--allow-file-access-from-files']});const rows=[],errors=[];
try{const page=await browser.newPage({viewport:{width:1920,height:1080},deviceScaleFactor:1});page.on('pageerror',e=>errors.push(e.message));await page.goto('file://'+file);await page.waitForFunction(()=>window.__renderReady,null,{timeout:60000});
async function seek(t){await page.evaluate(async t=>{window.__player.renderSeek(t,{exact:true});await window.__hfWaitForSeekCompletion?.();await document.fonts.ready;},t);}
for(const [i,t]of [boundary-1/30,boundary,boundary+1/30].entries()){
 await seek(t);const headings=await page.evaluate(()=>[...document.querySelectorAll('.heading')].filter(e=>{for(let p=e;p&&p!==document.body;p=p.parentElement){const s=getComputedStyle(p);if(s.display==='none'||s.visibility==='hidden'||+s.opacity===0)return false;}return e.getBoundingClientRect().width>0;}).map(e=>e.textContent));
 const expected=scenes.find(s=>s.id===(t<boundary?'S17':'S18')).title;if(!headings.includes(expected))throw Error('Missing visible boundary scene '+expected+'; got '+headings);
 const first=await page.screenshot();fs.writeFileSync(path.join(out,`${i}.png`),first);
 for(const destination of [cursor-1/30,0,t,t])await seek(destination);
 const second=await page.screenshot(),a=PNG.sync.read(first),b=PNG.sync.read(second),d=new PNG({width:a.width,height:a.height});const changed=pixelmatch(a.data,b.data,d.data,a.width,a.height,{threshold:.05,includeAA:false});if(changed)fs.writeFileSync(path.join(out,`${i}-diff.png`),PNG.sync.write(d));
 rows.push({time:t,headings,pixels:changed,sha256:crypto.createHash('sha256').update(first).digest('hex')});
}
}finally{await browser.close();}
const result={status:rows.some(r=>r.pixels)||errors.length?'failed':'passed',chapter:'C04',boundary:'S17 → S18',boundaryTime:boundary,rows,errors,source_sha256:crypto.createHash('sha256').update(source).digest('hex')};fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(result,null,2));console.log(JSON.stringify(result));if(result.status!=='passed')process.exitCode=1;
