/** Exhaustive caption/teaching-box bounds for all newly generated scenes. */
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import {chromium} from '@playwright/test';
import {validateGeometry} from './geometry.mjs';
const root=path.resolve(process.argv[2]),qa=path.resolve(root,'../qa/all-text-geometry');fs.mkdirSync(qa,{recursive:true});
const profile=JSON.parse(fs.readFileSync(path.join(root,'production.json'))),tokens=JSON.parse(fs.readFileSync(new URL('./tokens.v1.1.json',import.meta.url)));
const scenes=JSON.parse(fs.readFileSync(path.join(root,'data/scenes.json'))).scenes,rows=[];
const browser=await chromium.launch({executablePath:profile.runtime.browser,args:['--no-sandbox','--allow-file-access-from-files']});
try{const page=await browser.newPage({viewport:{width:1920,height:1080}});
for(const scene of scenes){
 const source=fs.readFileSync(path.join(root,'compositions',scene.id+'.html'),'utf8');
 const body=source.match(/<template>([\s\S]*)<\/template>/)[1].replaceAll('url(assets/',`url(file://${root}/assets/`);
 const file=path.join(qa,scene.id+'.html');fs.writeFileSync(file,`<html><head><script src="file://${root}/assets/vendor/gsap.min.js"></script><script>window.__timelines={}</script><style>html,body{margin:0;width:1920px;height:1080px}</style></head><body>${body}<script src="file://${root}/node_modules/hyperframes/dist/hyperframe-runtime.js"></script></body></html>`);
 await page.goto('file://'+file);await page.waitForFunction(()=>window.__renderReady);await page.evaluate(async()=>{await document.fonts.load('34px Editorial');await document.fonts.load('bold 54px Editorial');await document.fonts.ready;window.__player.renderSeek(0,{exact:true});await window.__hfWaitForSeekCompletion?.();});
 const objects=await page.evaluate(()=>[...document.querySelectorAll('.caption,.teaching,.chapter,.heading,.question,.option,.answer-mark,svg text')].map((e,i)=>{const b=e.getBoundingClientRect();return {id:e.id||e.className+i,box:{x:b.x,y:b.y,width:b.width,height:b.height},overflow:e instanceof HTMLElement&&e.scrollHeight>e.clientHeight+1};}));
 // Captions/teaching labels occupy mutually exclusive timed slots: each is checked individually here.
 // Simultaneous visibility and overlaps are checked by qa.mjs at real seek states.
 const errors=objects.flatMap(o=>validateGeometry([o],tokens).errors);
 rows.push({scene:scene.id,source_sha256:crypto.createHash('sha256').update(source).digest('hex'),objects:objects.length,maxBottom:Math.max(...objects.map(o=>o.box.y+o.box.height)),errors,exceptions:[]});
 console.error(JSON.stringify({phase:'all_text_geometry',scene:scene.id,errors:errors.length}));
}}finally{await browser.close();}
const result={geometrySha256:crypto.createHash('sha256').update(fs.readFileSync(new URL('./geometry.mjs',import.meta.url))).digest('hex'),validatorSha256:crypto.createHash('sha256').update(fs.readFileSync(new URL(import.meta.url))).digest('hex'),tokensSha256:crypto.createHash('sha256').update(fs.readFileSync(new URL('./tokens.v1.1.json',import.meta.url))).digest('hex'),status:rows.some(r=>r.errors.length)?'failed':'passed',scope:'Every caption, teaching label, heading and quiz HTML text box individually; simultaneous state/path coverage is separate',rows};
fs.writeFileSync(path.join(qa,'report.json'),JSON.stringify(result,null,2));console.log(JSON.stringify({status:result.status,scenes:rows.length}));if(result.status==='failed')process.exitCode=1;
