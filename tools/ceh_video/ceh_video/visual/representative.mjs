// Bounded S23 geometry prototype; the original 58-scene artwork stays separately compiled.
import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';
const project=path.resolve(process.argv[2]),here=path.dirname(fileURLToPath(import.meta.url));
const out=path.join(project,'engineering');fs.mkdirSync(out,{recursive:true});
for(const name of ['geometry.mjs','tokens.v1.1.json'])fs.copyFileSync(path.join(here,name),path.join(out,name));
fs.copyFileSync(path.join(here,'node_modules/pixi.js/dist/pixi.min.js'),path.join(out,'pixi.min.js'));
fs.copyFileSync(path.join(here,'node_modules/gsap/dist/PixiPlugin.min.js'),path.join(out,'PixiPlugin.min.js'));
const tokens=JSON.parse(fs.readFileSync(path.join(here,'tokens.v1.1.json')));
for(const backend of ['svg','pixi']){
const id=`S23-engineering-${backend}`;
const html=`<!doctype html><html lang="en-US"><head><meta charset="utf-8"><style>
@font-face{font-family:Editorial;src:url(../assets/fonts/LiberationSans-Regular.ttf)}
@font-face{font-family:Editorial;src:url(../assets/fonts/LiberationSans-Bold.ttf);font-weight:700}
html,body{margin:0;width:1920px;height:1080px;background:${tokens.colors.paper};color:${tokens.colors.ink};font-family:Editorial}
#root{position:relative;width:1920px;height:1080px}h1{position:absolute;left:155px;top:125px;margin:0;font-size:54px}
.chapter{position:absolute;left:155px;top:87px;font-size:27px}.card{position:absolute;width:350px;height:160px;border:4px solid ${tokens.colors.ink};border-radius:8px;background:${tokens.colors.paper_white};box-sizing:border-box;display:flex;align-items:center;justify-content:center;font-size:36px}
.chapter,h1,.card,.note,.caption{z-index:2}#diagram{position:absolute;inset:0;width:1920px;height:1080px}.caption{position:absolute;left:230px;top:940px;width:1460px;font-size:34px;line-height:1.15;text-align:center}.note{position:absolute;left:230px;top:850px;width:1460px;font-size:36px;text-align:center}
</style><script src="../assets/vendor/gsap.min.js"></script>${backend==='pixi'?'<script src="pixi.min.js"></script><script src="PixiPlugin.min.js"></script>':''}</head><body>
<div id="root" data-composition-id="${id}" data-width="1920" data-height="1080" data-duration="6">
<div class="chapter">C05 · Reflection and amplification · Engineering fixture</div><h1>Follow the reflected reply</h1>
<svg id="diagram" viewBox="0 0 1920 1080"><defs><marker id="arrow" markerWidth="16" markerHeight="20" refX="16" refY="10" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L16 10 L0 20" fill="none" stroke="${tokens.colors.ink}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></marker><clipPath id="flow-mask"><rect x="155" y="272" width="1610" height="550"/></clipPath></defs><path id="connection" fill="none" stroke="${tokens.colors.ink}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow)"/><g clip-path="url(#flow-mask)"><rect id="packet" width="23" height="14" rx="4" fill="${tokens.colors.terracotta}"/></g></svg>
<div id="sender" class="card">Sender</div><div id="reflector" class="card">Reflector</div><div class="note">Claimed source → Victim</div><div class="caption">All arrows here represent stored, simulated packets.</div></div>
<script type="module">
import {connector} from './geometry.mjs';
window.__hf=window.__hf||{};window.__hf.buildReady=window.__hf.buildReady||{};
window.__hf.buildReady[${JSON.stringify(id)}]=(async()=>{
await document.fonts.load('36px Editorial');await document.fonts.ready;
const backend=${JSON.stringify(backend)},line=document.querySelector('#connection'),packet=document.querySelector('#packet');let app,sprite;
if(backend==='pixi'){
 app=new PIXI.Application();await app.init({width:1920,height:1080,backgroundAlpha:0,autoStart:false,sharedTicker:false,preference:'webgl',antialias:true,resolution:1});app.stop();app.ticker.stop();PIXI.Ticker.shared.stop();PIXI.Ticker.system.stop();
 app.canvas.style.cssText='position:absolute;inset:0;pointer-events:none;z-index:1';document.querySelector('#root').appendChild(app.canvas);packet.style.display='none';
 sprite=new PIXI.Graphics().roundRect(0,0,23,14,4).fill(${JSON.stringify(tokens.colors.terracotta)});app.stage.addChild(sprite);
 const mask=new PIXI.Graphics().rect(155,272,1610,550).fill(0xffffff);app.stage.addChild(mask);sprite.mask=mask;
 gsap.registerPlugin(PixiPlugin);PixiPlugin.registerPIXI(PIXI);
 const probe=gsap.timeline({paused:true}).to(sprite,{pixi:{x:100},duration:1,ease:'none'});probe.seek(.5);window.__pixiPluginProbe=sprite.x;probe.kill();
}
const state={time:0};
function frame(t){
 const u=Math.min(1,Math.max(0,t/2.4));const a={x:230+80*u,y:380,width:350,height:160},b={x:1200,y:420-40*u,width:350,height:160};
 for(const [id,box]of [['sender',a],['reflector',b]]){const e=document.getElementById(id);e.style.left=box.x+'px';e.style.top=box.y+'px';}
 const c=connector(a,b);line.setAttribute('d',c.d);const p=Math.min(1,Math.max(0,(t-.8)/2.4)),q=1-p,m=(c.start.x+c.end.x)/2;const point={x:q*q*q*c.start.x+3*q*q*p*m+3*q*p*p*m+p*p*p*c.end.x,y:q*q*q*c.start.y+3*q*q*p*c.start.y+3*q*p*p*c.end.y+p*p*p*c.end.y};
 if(app){sprite.position.set(point.x-11.5,point.y-7);app.render();}else{packet.setAttribute('x',point.x-11.5);packet.setAttribute('y',point.y-7);}
 window.__geometry={a,b,connection:c,time:t};
}
const tl=gsap.timeline({paused:true}).to(state,{time:6,duration:6,ease:'none',onUpdate:()=>frame(state.time)});
window.__timelines=window.__timelines||{};window.__timelines[${JSON.stringify(id)}]=tl;
window.addEventListener('hf-seek',event=>{const work=Promise.resolve().then(()=>frame(event.detail.time));event.detail.waitUntil(work);});
window.__fixtureFrame=frame;frame(0);window.__fixtureReady=true;
})();
</script><script src="../node_modules/hyperframes/dist/hyperframe-runtime.js"></script></body></html>`;
fs.writeFileSync(path.join(out,`${backend}.html`),html);
const standalone=path.join(project,'engineering-'+backend);fs.mkdirSync(standalone,{recursive:true});
fs.cpSync(path.join(project,'assets/fonts'),path.join(standalone,'assets/fonts'),{recursive:true});fs.cpSync(path.join(project,'assets/vendor'),path.join(standalone,'assets/vendor'),{recursive:true});
for(const name of ['geometry.mjs','pixi.min.js','PixiPlugin.min.js'])fs.copyFileSync(path.join(out,name),path.join(standalone,name));
fs.writeFileSync(path.join(standalone,'index.html'),html.replaceAll('../assets/','assets/').replace('<script src="../node_modules/hyperframes/dist/hyperframe-runtime.js"></script>','')); 
}
console.log(JSON.stringify({status:'implemented',output:out,scope:'Six-second S23 geometry fixture; not a replacement for narration-length S23'}));
