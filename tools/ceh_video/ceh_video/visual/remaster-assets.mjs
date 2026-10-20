/** Verify locked vector identity, uniform transforms and actual DOM bounds. */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL,fileURLToPath} from 'node:url';
import {chromium} from '@playwright/test';
const root=path.resolve(process.argv[2]),out=path.resolve(root,'../qa/remaster-assets');
const read=f=>JSON.parse(fs.readFileSync(f)),hash=f=>crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');
const profile=read(path.join(root,'production.json')),tokens=read(path.join(root,profile.token_manifest));
const runtimeHashes={runtimeSha256:hash(new URL('./remaster-runtime.js',import.meta.url)),hyperframesRuntimeSha256:hash(path.join(root,'node_modules/hyperframes/dist/hyperframe-runtime.js')),gsapSha256:hash(path.join(root,'assets/vendor/gsap.min.js')),browserExecutableSha256:hash(profile.runtime.browser)};
const report={...runtimeHashes,status:'failed',scriptSha256:hash(fileURLToPath(import.meta.url)),tokensSha256:hash(path.join(root,profile.token_manifest)),sources:{},assets:{},rows:[],errors:[]};
fs.mkdirSync(out,{recursive:true});
const browser=await chromium.launch({executablePath:profile.runtime.browser,args:['--no-sandbox','--allow-file-access-from-files']});
try {
 for(const scene of read(path.join(root,'data/scenes.json')).scenes){
  const sid=scene.id,source=path.join(root,'compositions',sid+'.html'),layout=read(path.join(root,'data',sid+'.layout.json'));
  report.sources[sid]=hash(source);
  if(layout.template==='quiz')continue;
  for(const r of layout.rails)for(const a of [{asset:r.asset,sha256:r.sha256},...(r.parts||[])]){report.assets[a.asset]=hash(path.join(root,a.asset));if(report.assets[a.asset]!==a.sha256)throw Error('Asset identity changed: '+a.asset);}
  for(const n of layout.components)if(n.asset){const f='assets/props/'+n.asset+'.svg';report.assets[f]=hash(path.join(root,f));if(report.assets[f]!==n.assetSha256)throw Error('Device identity changed: '+f);}
  const body=fs.readFileSync(source,'utf8').match(/<template>([\s\S]*)<\/template>/)[1].replaceAll('url(assets/',`url(${pathToFileURL(root+'/')}assets/`);
  const html=path.join(out,sid+'.html');fs.writeFileSync(html,`<!doctype html><html><head><script src="${pathToFileURL(root+'/assets/vendor/gsap.min.js')}"></script><script>window.__timelines={}</script><style>html,body{margin:0;width:1920px;height:1080px}</style></head><body>${body}<script src="${pathToFileURL(root+'/node_modules/hyperframes/dist/hyperframe-runtime.js')}"></script></body></html>`);
  const page=await browser.newPage({viewport:{width:1920,height:1080},deviceScaleFactor:1});
  try{
   await page.goto(pathToFileURL(html).href);await page.waitForFunction(()=>window.__renderReady===true);
   const times=[...new Set(layout.components.flatMap(n=>[n.start,n.start+.4,n.start+.8,n.start+1.225,n.start+1.95]))];
   for(const t of times){
    await page.evaluate(async t=>{window.__player.renderSeek(t,{exact:true});await window.__hfWaitForSeekCompletion();await document.fonts.ready;},t);
    const state=await page.evaluate(({tokens,rails})=>{
     const safe={x:1920*tokens.safeArea.horizontal,y:1080*tokens.safeArea.vertical,right:1920*(1-tokens.safeArea.horizontal),bottom:1080*(1-tokens.safeArea.vertical)},errors=[];
     const assets=[...document.querySelectorAll('.locked-asset')].map(e=>{
      const b=e.getBoundingClientRect(),m=e.getCTM(),id=e.dataset.asset;
      const sx=Math.hypot(m.a,m.b),sy=Math.hypot(m.c,m.d),dot=m.a*m.c+m.b*m.d;
      if(Math.abs(sx-sy)>1e-6||Math.abs(dot)>1e-6)errors.push('nonuniform-or-skew:'+id);
      if(b.x<safe.x-.25||b.y<safe.y-.25||b.right>safe.right+.25||b.bottom>safe.bottom+.25)errors.push('asset-safe-area:'+id);
      const rail=rails.find(r=>r.id===id);
      if(rail&&(b.x<rail.x-.25||b.y<rail.y-.25||b.right>rail.x+rail.width+.25||b.bottom>rail.y+rail.height+.25))errors.push('asset-rail-overflow:'+id);
      return {id,box:{x:b.x,y:b.y,width:b.width,height:b.height},scaleX:sx,scaleY:sy,dot};
     });
     return {assets,errors};
    },{tokens,rails:layout.rails});
    report.rows.push({scene:sid,time:t,...state});if(state.errors.length)report.errors.push({scene:sid,time:t,errors:state.errors});
   }
  }finally{await page.close();}
  console.error(JSON.stringify({phase:'asset_geometry',scene:sid,errors:report.errors.length}));
 }
 report.status=report.errors.length?'failed':'passed';
}catch(e){report.errors.push({fatal:String(e.stack||e)});}finally{await browser.close();}
fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(report,null,2));
console.log(JSON.stringify({status:report.status,states:report.rows.length,errors:report.errors.length}));
if(report.status!=='passed')process.exitCode=1;
