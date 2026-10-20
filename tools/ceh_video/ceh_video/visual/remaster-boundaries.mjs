/** Full-film visual boundary QA. Audio is deliberately omitted from temporary
 * hosts; original scene/audio hashes and integer timing remain bound to receipt.
 * Uses actual pinned HyperFrames nested hydration, never natural playback.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL, fileURLToPath} from 'node:url';
import {chromium} from '@playwright/test';
import {PNG} from 'pngjs';
import pixelmatch from 'pixelmatch';

const root = path.resolve(process.argv[2] || '.');
const out = path.resolve(root, '../qa/remaster-boundaries');
fs.mkdirSync(out, {recursive:true});
const hash = data => crypto.createHash('sha256').update(data).digest('hex');
const readJSON = file => JSON.parse(fs.readFileSync(file));
const sources = {};
function source(file) {
  const data = fs.readFileSync(file);
  sources[path.relative(root,file)] = hash(data);
  return data;
}
const profile = JSON.parse(source(path.join(root,'production.json')));
const scenes = JSON.parse(source(path.join(root,'data/scenes.json'))).scenes;
const compilerFile = path.join(root,'node_modules/hyperframes/dist/compiler-O5R3ZZDV.js');
const rows = [], errors = [], hosts = [];
let browser;
const report = {
  status:'failed', scope:'Visual-only nested scene boundaries; no audio decoding or continuity claim',
  sampleRate:48000, fps:30, audioFramesPerVideoFrame:1600,
  expectedBoundaries:57, expectedStates:171, rows, errors, hosts, sources,
  script_sha256:hash(fs.readFileSync(fileURLToPath(import.meta.url))),
  lock_sha256:hash(fs.readFileSync(new URL('./package-lock.json',import.meta.url))),
  geometryTolerance:'Pixel threshold 0.05; antialias pixels excluded; zero unexplained differences',
};
function stripAudio(html) {
  return html.replace(/<audio\b[^>]*>[\s\S]*?<\/audio\s*>/gi,'').replace(/<audio\b[^>]*\/\s*>/gi,'');
}
const metadata = new Map();
const sceneFrames = new Map();
const globalStarts = new Map();

async function makeHost(id, members, chapterSource) {
  const folder = path.join(out,'hosts',id);
  fs.mkdirSync(path.join(folder,'compositions'),{recursive:true});
  const assets = path.join(folder,'assets');
  if(!fs.existsSync(assets))fs.symlinkSync(path.join(root,'assets'),assets,'dir');
  const original = source(chapterSource).toString();
  const head = original.match(/<head\b[^>]*>([\s\S]*?)<\/head>/i)?.[1];
  if(!head)throw Error(`Missing source head: ${chapterSource}`);
  let frame = 0;
  const starts = new Map();
  const slots = members.map(s => {
    starts.set(s.id,frame);
    const duration = sceneFrames.get(s.id);
    fs.writeFileSync(path.join(folder,'compositions',s.id+'.html'),
      stripAudio(source(path.join(root,'compositions',s.id+'.html')).toString()));
    const slot = `<div class="clip" id="slot-${s.id}" data-composition-id="${s.id}" data-composition-src="compositions/${s.id}.html" data-start="${frame/30}" data-duration="${duration/30}" data-track-index="1" data-width="1920" data-height="1080" style="position:absolute;inset:0"></div>`;
    frame += duration;
    return slot;
  }).join('');
  const hostHTML = `<!doctype html><html lang="en-US"><head>${head}</head><body><div id="root" data-composition-id="${id}" data-width="1920" data-height="1080" data-duration="${frame/30}">${slots}</div><script>window.__timelines=window.__timelines||{};window.__timelines[${JSON.stringify(id)}]=gsap.timeline({paused:true});</script></body></html>`;
  fs.writeFileSync(path.join(folder,'index.html'),stripAudio(hostHTML));
  const {bundleToSingleHtml} = await import(pathToFileURL(compilerFile).href);
  const html = (await bundleToSingleHtml(folder)).replace('<head>',`<head><base href="${pathToFileURL(folder+'/').href}">`);
  if(/<audio\b/i.test(html))throw Error(`Audio element survived visual host transform: ${id}`);
  const file = path.join(folder,'bundle.html');
  fs.writeFileSync(file,html);
  const info = {id, scenes:members.map(s=>s.id), totalFrames:frame,
    chapterSource:path.relative(root,chapterSource),
    transform:'Original source head and scene templates; audio elements omitted; slots rebuilt from integer PCM frames',
    host_sha256:hash(hostHTML), bundle_sha256:hash(html)};
  hosts.push(info);
  return {id,file,starts,totalFrames:frame};
}

try {
  if(profile.runtime.hyperframes!=='0.8.174')throw Error('Revalidate pinned compiler adapter before changing HyperFrames');
  if(readJSON(path.join(root,'node_modules/hyperframes/package.json')).version!=='0.8.174')throw Error('Installed HyperFrames mismatch');
  report.compiler_sha256=hash(source(compilerFile));
  for(const file of ['assets/vendor/gsap.min.js','assets/fonts/LiberationSans-Regular.ttf',
    'assets/fonts/LiberationSans-Bold.ttf','assets/fonts/DejaVuSansMono.ttf'])source(path.join(root,file));
  report.runtimePackage_sha256=hash(source(path.join(root,'node_modules/hyperframes/package.json')));
  report.browserExecutable_sha256=hash(source(profile.runtime.browser));
  if(scenes.length!==58)throw Error(`Expected 58 scenes; found ${scenes.length}`);
  let globalFrame=0;
  for(const s of scenes) {
    const m=JSON.parse(source(path.join(root,'data',s.id+'.audio.json')));
    if(!Number.isSafeInteger(m.samples)||m.samples%1600||m.sample_rate!==48000||m.channels!==2)throw Error(`${s.id}: non-integral or unsupported audio clock`);
    if(Math.abs(m.duration-m.samples/48000)>1e-8)throw Error(`${s.id}: duration disagrees with PCM frames`);
    metadata.set(s.id,m);sceneFrames.set(s.id,m.samples/1600);globalStarts.set(s.id,globalFrame);globalFrame+=m.samples/1600;
    source(path.join(root,'assets/voice',s.id+'.wav'));
    source(path.join(root,'compositions',s.id+'.html'));
  }
  report.totalFrames=globalFrame;
  browser=await chromium.launch({executablePath:profile.runtime.browser,args:['--no-sandbox','--allow-file-access-from-files']});
  report.browser=browser.version();report.browserExecutable=profile.runtime.browser;
  const chapters=new Map();
  for(const s of scenes){if(!chapters.has(s.chapter_id))chapters.set(s.chapter_id,[]);chapters.get(s.chapter_id).push(s);}
  if(chapters.size!==11)throw Error(`Expected 11 chapters; found ${chapters.size}`);
  const chapterHosts=new Map();
  for(const [id,members]of chapters)chapterHosts.set(id,await makeHost('boundary-'+id,members,path.join(root,'chapters',id,'index.html')));
  const tasks=new Map();
  for(let i=1;i<scenes.length;i++){
    const left=scenes[i-1],right=scenes[i];
    const interchapter=left.chapter_id!==right.chapter_id;
    const host=interchapter?await makeHost(`boundary-${left.id}-${right.id}`,[left,right],path.join(root,'chapters',left.chapter_id,'index.html')):chapterHosts.get(left.chapter_id);
    if(!tasks.has(host))tasks.set(host,[]);
    tasks.get(host).push({left,right,interchapter});
  }
  for(const [host,boundaries]of tasks){
    const page=await browser.newPage({viewport:{width:1920,height:1080},deviceScaleFactor:1});
    page.on('pageerror',e=>errors.push({host:host.id,error:e.message}));
    await page.goto(pathToFileURL(host.file).href);
    await page.waitForFunction(()=>window.__renderReady,null,{timeout:60000});
    async function seek(frame){
      await page.evaluate(async frame=>{
        if(!window.__player?.renderSeek||!window.__hfWaitForSeekCompletion)throw Error('HyperFrames seek barrier unavailable');
        window.__player.renderSeek(frame/30,{exact:true});
        await window.__hfWaitForSeekCompletion();await document.fonts.ready;
      },frame);
    }
    async function heading(expected){
      const titles=await page.evaluate(()=>[...document.querySelectorAll('.heading')].filter(e=>{
        for(let p=e;p&&p!==document.body;p=p.parentElement){const s=getComputedStyle(p);if(s.display==='none'||s.visibility==='hidden'||+s.opacity===0)return false;}
        const r=e.getBoundingClientRect();return r.width>0&&r.height>0&&r.right>0&&r.bottom>0&&r.left<1920&&r.top<1080;
      }).map(e=>e.textContent.trim()));
      if(titles.length!==1||titles[0]!==expected.trim())throw Error(`Expected only visible heading ${JSON.stringify(expected)}; got ${JSON.stringify(titles)}`);
      return titles;
    }
    for(const {left,right,interchapter}of boundaries){
      const boundary=host.starts.get(right.id);
      for(const delta of [-1,0,1]){
        const frame=boundary+delta, expected=delta<0?left:right;
        const name=`${left.id}-${right.id}-${delta<0?'before':delta===0?'exact':'after'}`;
        const row={boundary:`${left.id}->${right.id}`,interchapter,host:host.id,offsetFrames:delta,
          localFrame:frame,globalFrame:globalStarts.get(right.id)+delta,
          audioFrame:(globalStarts.get(right.id)+delta)*1600,time:frame/30,expectedScene:expected.id,
          expectedHeading:expected.title,comparisons:[],pixels:0};
        rows.push(row);
        try{
          await seek(frame);row.headings=await heading(expected.title);
          const first=await page.screenshot();fs.writeFileSync(path.join(out,name+'.png'),first);
          row.screenshot=name+'.png';row.sha256=hash(first);
          const baseline=PNG.sync.read(first);
          for(const [mode,route]of [['forward',[0,frame]],['reverse',[host.totalFrames-1,frame]],['repeated',[frame,frame]]]){
            for(const destination of route)await seek(destination);
            await heading(expected.title);
            const second=PNG.sync.read(await page.screenshot());
            const diff=new PNG({width:baseline.width,height:baseline.height});
            const pixels=pixelmatch(baseline.data,second.data,diff.data,baseline.width,baseline.height,{threshold:.05,includeAA:false});
            row.comparisons.push({mode,pixels});row.pixels+=pixels;
            if(pixels)fs.writeFileSync(path.join(out,`${name}-${mode}-diff.png`),PNG.sync.write(diff));
          }
          row.status=row.pixels?'failed':'passed';
        }catch(error){row.status='failed';row.error=error.message;errors.push({state:name,error:error.message});}
      }
      console.log(JSON.stringify({stage:'remaster-boundary',boundary:`${left.id}->${right.id}`,completedStates:rows.length,totalStates:171}));
    }
    await page.close();
  }
  for(const [relative,expected]of Object.entries(sources))if(hash(fs.readFileSync(path.resolve(root,relative)))!==expected)throw Error(`Source changed while checking: ${relative}`);
  report.status=rows.length===171&&rows.every(r=>r.status==='passed')&&!errors.length?'passed':'failed';
}catch(error){errors.push({error:error.stack||error.message});}
finally{
  if(browser)await browser.close();
  fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(report,null,2));
  console.log(JSON.stringify({status:report.status,states:rows.length,expectedStates:171,errors:errors.length,report:path.join(out,'report.json')}));
  if(report.status!=='passed')process.exitCode=1;
}
