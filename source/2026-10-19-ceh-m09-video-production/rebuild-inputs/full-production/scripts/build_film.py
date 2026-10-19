#!/usr/bin/env python3
"""Compile editable scene compositions from locked copy and measured audio samples."""
from editorial import *
from scene_art import build
from production_settings import quiz_seconds,quiz_label

import argparse,csv,os,shutil
import soundfile as sf
CSS='''@font-face{font-family:Technical;src:url(assets/fonts/DejaVuSansMono.ttf)}@font-face{font-family:Editorial;src:url(assets/fonts/LiberationSans-Regular.ttf)}@font-face{font-family:Editorial;src:url(assets/fonts/LiberationSans-Bold.ttf);font-weight:700}.chapter,.heading,.teaching,.caption,.question,.choices,.answer-mark,.quiz-clock,.question-title{font-family:Editorial,Arial,sans-serif}*{box-sizing:border-box}body{margin:0;background:#F0EBE4}#root{position:relative;width:100%;height:100%;overflow:hidden;font-family:Editorial,Arial,sans-serif;color:#292421;background:#F0EBE4}.art{position:absolute;inset:0;width:1920px;height:1080px;font-family:Editorial,Arial,sans-serif}.chapter{position:absolute;left:155px;top:85px;font-size:27px;letter-spacing:1px}.heading{position:absolute;left:155px;top:125px;width:1600px;font-size:54px;font-weight:700;line-height:1.08;margin:0}.teaching{position:absolute;left:200px;top:850px;width:1520px;text-align:center;font-size:38px;font-weight:700;line-height:1.15}.caption{position:absolute;left:230px;top:945px;width:1460px;text-align:center;font-size:34px;white-space:normal;line-height:1.15;background:#F0EBE4;padding:4px 16px}.question-title{position:absolute;left:240px;top:220px;width:1380px;font-size:30px;font-weight:700}.question{position:absolute;left:240px;top:285px;width:1330px;font-size:43px;line-height:1.18}.choices{position:absolute;left:260px;top:420px;width:1370px;display:flex;flex-direction:column;gap:22px}.option{font-size:35px;line-height:1.15;padding:15px 24px;border-bottom:2px solid #B8B0A9;background:#FFFAF3}.quiz-clock{position:absolute;left:1620px;top:300px;width:120px;height:120px;border:4px solid #292421;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:44px;background:#F2D4B7}.answer-mark{position:absolute;left:260px;top:840px;width:1370px;font-size:34px;text-align:center;font-weight:700}'''
CSS+='''.question-title{left:230px;top:225px;width:1320px;color:#292421}.question{left:230px;width:1320px;font-weight:700;line-height:1.15}.choices{left:230px;width:1320px;gap:12px}.option{font-size:34px;line-height:1.15;padding:12px 20px;border-bottom:2px solid #B8B0A9}.quiz-clock{left:1600px;top:295px}.answer-mark{left:230px;top:850px;width:1320px;font-size:34px}.teaching{font-size:36px;max-height:86px}.chapter{color:#292421}'''
def script(moves,sid,duration):
 travel=[]
 for m in moves:
  if 'travel' not in m:continue
  x1,y1,x2,y2=m['travel'];poses=[]
  for i in range(21):
   p=i/20;q=1-p;c=(x1+x2)/2;poses.append({'x':q*q*q*x1+3*q*q*p*c+3*q*p*p*c+p*p*p*x2,'y':q*q*q*y1+3*q*q*p*y1+3*q*p*p*y2+p*p*p*y2,'duration':m['duration']/20 if i else 0,'ease':'none'})
  target=json.dumps('#'+m['target']);travel.extend([f'tl.set({target},{{x:{x1},y:{y1}}},0);',f'tl.set({target},{{opacity:1}},{m["start"]});',f'tl.to({target},{{keyframes:{json.dumps(poses)},ease:"none"}},{m["start"]});',f'tl.set({target},{{opacity:0}},{m["start"]+m["duration"]});'])
 return '''const tl=gsap.timeline({paused:true});
const moves='''+json.dumps(moves)+''';
for(const m of moves){const el=document.getElementById(m.target);if(!el)throw Error('Missing layer '+m.target);
if(m.draw){tl.set(el,{opacity:0},0);tl.set(el,{opacity:1},m.start);for(const p of el.querySelectorAll('path')){if(m.dashed){tl.set(p,{strokeDasharray:'10 10',strokeDashoffset:0},0);tl.fromTo(p,{opacity:0},{opacity:1,duration:m.duration,ease:'none'},m.start);}else{const length=p.getTotalLength();tl.fromTo(p,{strokeDasharray:length,strokeDashoffset:length},{strokeDashoffset:0,duration:m.duration,ease:'none'},m.start);}}}
else if(m.travel){}
else if(m.from){tl.set(el,m.from,0);tl.fromTo(el,m.from,{...m.props,duration:m.duration,immediateRender:false},m.start);}
else tl.to(el,{...m.props,duration:m.duration},m.start);
}
'''+''.join(travel)+'''
const clocks=Array.from(document.querySelectorAll('[data-quiz-scene="'''+sid+'''"]'));
if(clocks.length){const clockState={time:0};tl.fromTo(clockState,{time:0},{time:'''+str(duration)+''',duration:'''+str(duration)+''',ease:'none',onUpdate:()=>{for(const el of clocks){const start=Number(el.dataset.pauseStart),end=Number(el.dataset.pauseEnd),t=clockState.time;el.style.opacity=(t>=start-1e-6&&t<end-1e-6)?'1':'0';el.textContent=String(Math.max(0,Math.ceil(end-t-1e-6)));}}},0);}
window.__timelines['''+json.dumps(sid)+''']=tl;'''
def visibility(moves,target,start,end):
 moves.append({'target':target,'start':0,'duration':0,'props':{'opacity':0}})
 moves.append({'target':target,'start':start,'duration':0,'props':{'opacity':1}})
 moves.append({'target':target,'start':end,'duration':0,'props':{'opacity':0}})
def captions(sid,audio):
 result=[]
 for row in audio['segments']:
  if row['kind']!='spoken':continue
  f=ROOT/'data/forced-alignment'/f'{sid}-{row["sentence"]:03}.json'
  if not f.exists():return []
  aligned=json.load(open(f));assert aligned['audio_sha256']==row['sha256'];words=aligned['words'];chunk=[];chunks=[]
  for word in words:
   if chunk and len(' '.join(w['text'] for w in chunk+[word]))>70:chunks.append(chunk);chunk=[]
   chunk.append(word)
  if chunk:chunks.append(chunk)
  if len(chunks)>1 and len(chunks[-1])<4 and len(chunks[-2])>6:
   shift=4-len(chunks[-1]);chunks[-1]=chunks[-2][-shift:]+chunks[-1];chunks[-2]=chunks[-2][:-shift]
  for chunk in chunks:
   result.append({'text':' '.join(w['text'] for w in chunk),'start':row['start_sample']/48000+chunk[0]['start'],'end':row['start_sample']/48000+max(w['end'] for w in chunk)})
 return result

def quiz(scene,audio):
 from PIL import ImageFont
 sid=scene['id'];moves=[];parts=[];qs=[q for q in json.load(open(ROOT/'data/questions.json'))['questions'] if q['scene_id']==sid];silences=[s for s in audio['segments'] if s['kind']=='silence'];starts=[];layouts=[]
 def lines(text,size,width,bold=False):
  f=ImageFont.truetype(str(ROOT/'assets/fonts'/('LiberationSans-Bold.ttf' if bold else 'LiberationSans-Regular.ttf')),size);count=1;line=''
  for word in text.split():
   trial=(line+' '+word).strip()
   if f.getlength(trial)>width-10 and line:count+=1;line=word
   else:line=trial
  return count
 for q in qs:
  matches=[s for s in audio['segments'] if s['kind']=='spoken' and re.search(r'\bquestion\s+0*'+str(int(q['id'][1:]))+r'[.:]',s['canonical'].lower()) is not None]
  assert len(matches)==1,(sid,q['id']);starts.append(matches[0]['start_sample']/48000)
 for i,(q,pause) in enumerate(zip(qs,silences)):
  start=starts[i];end=audio['duration'] if i==len(qs)-1 else starts[i+1];answer=pause['end_sample']/48000;key=sid+'-'+q['id']
  prompt_top=272;prompt_size=40;prompt_height=lines(q['id']+'. '+q['prompt'],prompt_size,1320,True)*46;choice_top=prompt_top+prompt_height+24;heights=[lines(c['letter']+'. '+c['text'],34,1270)*39.1+26 for c in q['choices']];choice_end=choice_top+sum(heights)+12*3
  assert choice_end<830,(sid,q['id'],'Quiz requires more room',choice_end)
  content=f'<div class="quiz-page" id="{key}" style="opacity:0"><div class="question-title">{q["id"]} · {esc(q["level"].upper())} · 1 second each</div><div class="question" style="top:{prompt_top}px;font-size:{prompt_size}px">{q["id"]}. {esc(q["prompt"])}</div><div class="choices" style="top:{choice_top}px">'+''.join(f'<div class="option" id="{key}-{c["letter"]}">{c["letter"]}. {esc(c["text"])}</div>' for c in q['choices'])+'</div></div>';parts.append(content);visibility(moves,key,start,end)
  moves.append({'target':key+'-'+q['correct_letter'],'start':answer,'duration':.35,'props':{'backgroundColor':SOFT,'borderColor':INK}})
  ident=key+'-clock';parts.append(f'<div class="quiz-clock" id="{ident}" data-quiz-scene="{sid}" data-pause-start="{pause["start_sample"]/48000}" data-pause-end="{answer}" style="opacity:0">1</div>')
  ident=key+'-guide';parts.append(f'<div class="answer-mark" id="{ident}" style="opacity:0">Pause the video if you need more time</div>');visibility(moves,ident,start,answer)
  ident=key+'-answer';parts.append(f'<div class="answer-mark" id="{ident}" style="opacity:0">Correct answer: {q["correct_letter"]}</div>');visibility(moves,ident,answer,end)
  layouts.append({'question':q['id'],'prompt_height':prompt_height,'choice_top':choice_top,'choice_end':choice_end,'answer_start':answer,'canonical_explanation_in':'narration and synchronized captions; correct option highlighted'})
 a=Art(sid,audio);a.tally(1565,625,'think',0)
 stamp=a.add(text(1665,835,'SIMULATED OUTPUT',20,18),'quiz-simulation-stamp');a.show(stamp,0)
 parts.append(a.svg());moves.extend(a.moves)
 (ROOT/'data'/f'{sid}.quiz-layout.json').write_text(json.dumps(layouts,indent=2))
 return ''.join(parts),moves

def host(scenes,name):
 duration=sum(a['duration'] for s,a in scenes);start=0;slots=[]
 for s,a in scenes:
  sid=s['id'];d=a['duration'];slots.append(f'<div class="clip" id="slot-{sid}" data-composition-id="{sid}" data-composition-src="compositions/{sid}.html" data-start="{start:.9f}" data-duration="{d:.9f}" data-track-index="1" data-width="1920" data-height="1080" style="position:absolute;inset:0"></div>');start+=d
 if len(scenes)==1:audio_path='assets/voice/'+scenes[0][0]['id']+'.wav'
 else:
  audio_path='assets/audio/'+name+'.wav';audio_file=ROOT/audio_path;recipe=[(s['id'],(ROOT/'assets/voice'/f'{s["id"]}.wav').stat().st_mtime_ns) for s,a in scenes];cache=audio_file.with_suffix('.json')
  if not audio_file.exists() or not cache.exists() or json.load(open(cache))!=[list(x) for x in recipe]:
   with sf.SoundFile(str(audio_file)+'.tmp.wav','w',samplerate=48000,channels=2,subtype='PCM_16') as dest:
    for scene,metadata in scenes:
     pcm,sr=sf.read(ROOT/'assets/voice'/f'{scene["id"]}.wav',dtype='int16');assert sr==48000;dest.write(pcm)
   os.replace(str(audio_file)+'.tmp.wav',audio_file);cache.write_text(json.dumps(recipe))
 slots.append(f'<audio class="clip" id="narration-{name}" src="{audio_path}" data-start="0" data-duration="{duration:.9f}" data-track-index="10"></audio>')
 return f'<!doctype html><html lang="en-US"><head><meta charset="utf-8"><script src="assets/vendor/gsap.min.js"></script><style>{CSS}</style></head><body><div id="root" data-composition-id="{name}" data-width="1920" data-height="1080" data-duration="{duration:.9f}">'+''.join(slots)+f'</div><script>window.__timelines=window.__timelines||{{}};window.__timelines["{name}"]=gsap.timeline({{paused:true}});</script></body></html>'

def write_host(folder,content):
 target=ROOT/folder;target.mkdir(parents=True,exist_ok=True)
 (target/'index.html').write_text(content)
 (target/'hyperframes.json').write_text((ROOT/'hyperframes.json').read_text())
 for name in ['assets','compositions']:
  link=target/name
  if link.is_symlink():link.unlink()
  link.mkdir(exist_ok=True)
 if not (target/'assets/vendor').exists():
  for name in ['vendor','fonts','props','mascot']:
   shutil.copytree(ROOT/'assets'/name,target/'assets'/name,copy_function=os.link,dirs_exist_ok=True)
 (target/'assets/voice').mkdir(exist_ok=True)
 for sid in re.findall(r'data-composition-src="compositions/(S[0-9]+).html"',content):
  shutil.copyfile(ROOT/'compositions'/f'{sid}.html',target/'compositions'/f'{sid}.html')
  shutil.copyfile(ROOT/'compositions'/f'{sid}.motion.json',target/'compositions'/f'{sid}.motion.json')
  wave=target/'assets/voice'/f'{sid}.wav'
  source_wave=ROOT/'assets/voice'/f'{sid}.wav'
  if wave.exists() and not os.path.samefile(source_wave,wave):wave.unlink()
  if not wave.exists():os.link(source_wave,wave)

 for audio_path in re.findall(r'src="(assets/audio/[^"]+\.wav)"',content):
  wave=target/audio_path;wave.parent.mkdir(exist_ok=True);source_wave=ROOT/audio_path
  if wave.exists() and not os.path.samefile(source_wave,wave):wave.unlink()
  if not wave.exists():os.link(source_wave,wave)

def main():
 for folder in ['compositions','assets/audio','review','chapters']:(ROOT/folder).mkdir(parents=True,exist_ok=True)
 parser=argparse.ArgumentParser();parser.add_argument('--scene');parser.add_argument('--chapter');parser.add_argument('--scenes');args=parser.parse_args();allscenes=json.load(open(ROOT/'data/scenes.json'))['scenes'];ready=[];ledger=[]
 selected=set(args.scenes.split(',')) if args.scenes else None
 prior={row['scene']:row for row in json.load(open(ROOT/'data/build-ledger.json'))} if selected else {}
 for scene in allscenes:
  if args.chapter and scene['chapter_id']!=args.chapter:continue
  sid=scene['id'];af=ROOT/'data'/f'{sid}.audio.json'
  if not af.exists() or (args.scene and sid!=args.scene):continue
  audio=json.load(open(af));d=audio['duration'];n=int(sid[1:]);moves=[]
  if selected is not None and sid not in selected:
   ready.append((scene,audio));ledger.append(prior[sid]);continue
  if 54<=n<=57:art,moves=quiz(scene,audio)
  else:
   a=build(scene,audio);art=a.svg();moves=a.moves
   # Every approved label is retained and exposed at a measured sentence boundary.
   labels=scene['on_screen_copy'];sentences=a.spoken
   cue_map={}
   for cf in (ROOT/'scripts').glob('cues_*.json'):cue_map.update(json.load(open(cf)))
   if sid in cue_map:
    assert len(cue_map[sid])==len(labels),(sid,'cue count')
    indices=[next(j for j,row in enumerate(sentences) if phrase.lower() in row['canonical'].lower()) for phrase in cue_map[sid]]
   else:raise ValueError((sid,'Missing M09 narration-anchored label cue map'))
   cues=[(ix,i,label) for i,(ix,label) in enumerate(zip(indices,labels))]
   cues.sort(key=lambda x:(x[0],x[1]))
   bindings=[]
   for j,(ix,i,label) in enumerate(cues):
    start=sentences[ix]['start_sample']/48000
    # Same-sentence terms share one readable label group rather than overlap.
    next_indices=[c[0] for c in cues[j+1:] if c[0]>ix]
    end=sentences[next_indices[0]]['start_sample']/48000 if next_indices else d
    peers=[c for c in cues if c[0]==ix]
    if peers[0][1]!=i:continue
    value=' · '.join(c[2] for c in peers)
    ident=sid+'-teaching'+str(i);art+=f'<div class="teaching" id="{ident}">{esc(value)}</div>';visibility(moves,ident,start,end)
    bindings.append({'labels':[c[2] for c in peers],'sentence':ix,'canonical_anchor':sentences[ix]['canonical'],'rendered_label':value,'start':start,'end':end})
   (ROOT/'data'/f'{sid}.label-cues.json').write_text(json.dumps(bindings,indent=2))
  caps=captions(sid,audio)
  assert caps,(sid,'final forced alignment incomplete')
  for i,cap in enumerate(caps):
   ident=sid+'-caption'+str(i);art+=f'<div class="caption" id="{ident}">{esc(cap["text"])}</div>';visibility(moves,ident,cap['start'],cap['end'])
  markup=f'<div class="chapter">{scene["chapter_id"]} · {esc(scene["chapter_title"])}</div><h1 class="heading">{esc(scene["title"])}</h1>'+art
  out=f'<!doctype html><html lang="en-US"><body><template><style>{CSS}</style><div id="root" data-composition-id="{sid}" data-width="1920" data-height="1080" data-duration="{d:.9f}">{markup}</div><script>{script(moves,sid,d)}</script></template></body></html>'
  (ROOT/'compositions'/f'{sid}.html').write_text(out);(ROOT/'compositions'/f'{sid}.motion.json').write_text(json.dumps({'scene':sid,'duration':d,'assertions':[{'kind':'staysInFrame','selector':'.heading'},{'kind':'staysInFrame','selector':'.caption'}],'source':'measured audio samples','moves':moves,'status':'authored; visual QA pending'},indent=2));(ROOT/'data'/f'{sid}.captions.json').write_text(json.dumps(caps,indent=2))
  ready.append((scene,audio));ledger.append({'scene':sid,'duration':d,'movements':len(moves),'captions':len(caps),'status':'authored_pending_runtime_QA'})
  write_host('review/'+sid,host([(scene,audio)],'review-'+sid))
 if args.scene:
  print(json.dumps({'scenes_authored':len(ready),'scope':'one scene and its review project; global assembly unchanged'}));return
 (ROOT/'index.html').write_text(host(ready,'master'));(ROOT/'data/build-ledger.json').write_text(json.dumps(ledger,indent=2))
 for chapter in sorted(set(s['chapter_id'] for s,a in ready if selected is None or s['id'] in selected)):write_host('chapters/'+chapter,host([(s,a) for s,a in ready if s['chapter_id']==chapter],chapter))
 print(json.dumps({'scenes_authored':len(ready),'all_required':58,'duration':sum(a['duration'] for s,a in ready),'status':'not_rendered'}))
if __name__=='__main__':main()
