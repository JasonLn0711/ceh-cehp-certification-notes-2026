// Real seeked browser captures at narration-linked teaching states, with paint stabilization.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';
import {createRequire} from 'node:module';
const root=process.cwd(),require=createRequire(path.join(root,'package.json')),puppeteer=require('puppeteer-core');
const chapter=process.argv[2],out=path.resolve('../qa',chapter+'-states');fs.mkdirSync(out,{recursive:true});
const scenes=JSON.parse(fs.readFileSync('data/scenes.json')).scenes.filter(s=>s.chapter_id===chapter);
const questions=JSON.parse(fs.readFileSync('data/questions.json')).questions,cues={};
for(const name of fs.readdirSync('scripts').filter(x=>/^cues_.*\.json$/.test(x)))Object.assign(cues,JSON.parse(fs.readFileSync('scripts/'+name)));
const browser=await puppeteer.launch({executablePath:process.env.HYPERFRAMES_BROWSER_PATH,headless:true,args:['--no-sandbox','--allow-file-access-from-files']});
const rows=[];
try{for(const scene of scenes){
 const sid=scene.id,a=JSON.parse(fs.readFileSync(`data/${sid}.audio.json`)),times=new Map();
 const add=(label,t)=>times.set(Math.round(t*30)/30,label);
 add('midpoint',a.duration/2);add('complete',a.duration-4);
 if(questions.some(q=>q.scene_id===sid)){
  for(const hold of a.segments.filter(x=>x.kind==='silence')){add('hold', (hold.start_sample+hold.end_sample)/96000);add('answer',hold.end_sample/48000+.45);}
 }else{
  for(const [i,phrase]of (cues[sid]||[]).entries()){
   const segment=a.segments.find(x=>x.kind==='spoken'&&x.canonical.toLowerCase().includes(phrase.toLowerCase()));
   if(!segment)throw Error(sid+' missing teaching anchor '+phrase);
   add('teaching-'+(i+1),Math.min(a.duration-2,segment.end_sample/48000+.85));
  }
 }
 const page=await browser.newPage();await page.setViewport({width:1920,height:1080});
 let body=fs.readFileSync(`compositions/${sid}.html`,'utf8').match(/<template>([\s\S]*)<\/template>/)[1].replaceAll('url(assets/',`url(file://${root}/assets/`);
 const file=path.join(out,sid+'.html');fs.writeFileSync(file,`<html><head><script src="file://${root}/assets/vendor/gsap.min.js"></script><script>window.__timelines={}</script><style>html,body{margin:0;width:1920px;height:1080px}</style></head><body>${body}</body></html>`);
 await page.goto('file://'+file);await page.evaluate(async()=>{await document.fonts.ready});
 for(const [t,label]of [...times].sort((a,b)=>a[0]-b[0])){
  await page.evaluate(({sid,t})=>{window.__timelines[sid].seek(t,false)},{sid,t});
  await page.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
  const errors=await page.evaluate(()=>[...document.querySelectorAll('.question,.option,.caption,.heading')].filter(e=>{const s=getComputedStyle(e),b=e.getBoundingClientRect();return Number(s.opacity)>0&&b.width&&b.height&&(b.right>1922||b.bottom>1082||b.left< -2||b.top< -2||e.scrollHeight>e.clientHeight+2&&e.clientHeight>0&&s.overflow==='hidden')}).map(e=>e.id||e.className));
  if(errors.length)throw Error(sid+' text geometry '+errors.join(','));
  const name=`${sid}-${label}-${t.toFixed(3)}.png`,target=path.join(out,name);await page.screenshot({path:target});
  rows.push({scene:sid,phase:label,time:t,file:name,sha256:crypto.createHash('sha256').update(fs.readFileSync(target)).digest('hex')});
 }
 await page.close();console.log(JSON.stringify({phase:'teaching_state_capture',scene:sid,captured:rows.length}));
}}finally{await browser.close()}
fs.writeFileSync(path.join(out,'manifest.json'),JSON.stringify({status:'captured_review_pending',chapter,capture_recipe:crypto.createHash('sha256').update(fs.readFileSync(new URL(import.meta.url))).digest('hex'),rows},null,2));
