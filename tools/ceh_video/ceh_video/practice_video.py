"""Opt-in practical tutorial adapter. Existing Mandarin films do not import it.

One source timeline owns captions, ordered diagrams and per-case step progress.
Drafts visibly reserve missing recordings. Delivery requires real Online receipts.
"""
from pathlib import Path
import hashlib,html,json,math
from .practice_art import diagram,LABELS,PAPER,INK,ACCENT,SOFT

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def text_hash(text): return hashlib.sha256(text.encode()).hexdigest()
def esc(value): return html.escape(str(value))

def validate_lesson(lesson):
    if lesson.get('schema_version')!=1:raise ValueError('Unsupported practice schema')
    ids=set();cases={}
    if len(lesson['chapters'])!=5:raise ValueError('Five chapters required')
    for ch in lesson['chapters']:
        for s in ch['steps']:
            if s['id'] in ids:raise ValueError('Duplicate scene')
            ids.add(s['id'])
            if s['case_id']:cases.setdefault(s['case_id'],[]).append(s['step'])
            for b in s['beats']:
                if b['id'] in ids:raise ValueError('Duplicate paragraph')
                ids.add(b['id'])
                if b['cue']['paragraph_id']!=b['id']:raise ValueError('Cue belongs to a different paragraph')
                if not b['text'] or b['panel']['kind'] not in LABELS:raise ValueError('Missing text or unknown panel')
    if set(cases)!={'case1','case2','case3'} or any(v!=list(range(1,9)) for v in cases.values()):raise ValueError('Each case requires ordered steps 1..8')
    return True

def cue_time(text,words,phrase):
    if text.count(phrase)!=1:raise ValueError('Cue absent or ambiguous: '+phrase)
    char=text.index(phrase)
    for w in words:
        if w['char_start']<=char<w['char_end']:return w['start']
    raise ValueError('Cue has no real provider boundary: '+phrase)

def captions(words,start):
    rows=[];group=[]
    for w in words:
        if group and len(''.join(x['text'] for x in group))+len(w['text'])>36:
            rows.append({'start':start+group[0]['start'],'end':start+group[-1]['end'],'text':''.join(x['text'] for x in group)});group=[]
        group.append(w)
        if w['text'].rstrip().endswith(('。','？','！','；')):
            rows.append({'start':start+group[0]['start'],'end':start+group[-1]['end'],'text':''.join(x['text'] for x in group)});group=[]
    if group:rows.append({'start':start+group[0]['start'],'end':start+group[-1]['end'],'text':''.join(x['text'] for x in group)})
    return rows

def timeline(lesson,voice,project=None,selected=None):
    validate_lesson(lesson);offset=0;scenes=[];all_captions=[];chapter_rows=[]
    for ch in lesson['chapters']:
        ch_start=offset
        for s in ch['steps']:
            if selected and s['id'] not in selected:continue
            row={**s,'start':offset,'beats':[]};local=.15
            for b in s['beats']:
                v=voice.get(b['id'])
                if not v or v['text_sha256']!=text_hash(b['text']):raise ValueError('Missing or stale voice: '+b['id'])
                if project and sha(project/v['file'])!=v['sha256']:raise ValueError('Changed voice audio: '+b['id'])
                if v['duration']<=0 or v['speed_applications']!=1:raise ValueError('Invalid audio contract')
                if ''.join(w['text'] for w in v['words'])!=b['text']:raise ValueError('Word coverage mismatch')
                br={**b,'start':local,'duration':v['duration'],'voice':v}
                states=[{'start':local,'kind':b['panel']['kind']}]
                for state in b['panel'].get('states',[]):
                    at=local+cue_time(b['text'],v['words'],state['cue_phrase'])
                    if at<=states[-1]['start']:raise ValueError('Panel states must preserve authored order')
                    if state['kind'] not in LABELS:raise ValueError('Unknown ordered panel')
                    states.append({'start':at,'kind':state['kind']})
                br['panels']=states;row['beats'].append(br)
                all_captions.extend(captions(v['words'],offset+local));local+=v['duration']+.15
            row['duration']=math.ceil((local+s['read_hold_seconds']+.45)*30)/30
            for i,b in enumerate(row['beats']):
                b['end']=row['beats'][i+1]['start'] if i+1<len(row['beats']) else row['duration']
                for j,state in enumerate(b['panels']):state['end']=b['panels'][j+1]['start'] if j+1<len(b['panels']) else b['end']
            scenes.append(row);offset+=row['duration']
        if offset>ch_start:chapter_rows.append({'id':ch['id'],'title':ch['title'],'start':ch_start,'duration':offset-ch_start})
    return {'duration':offset,'fps':30,'frames':round(offset*30),'scenes':scenes,'chapters':chapter_rows,'captions':all_captions,'timing_source':'actual_provider_word_boundaries'}

def progress_at(t,schedule):
    """A pure function for seeks; eight equal teaching stages, not time percent."""
    if not schedule['scenes']:raise ValueError('No scenes')
    t=max(0,min(t,schedule['duration']))
    row=next((s for s in schedule['scenes'] if s['start']<=t<s['start']+s['duration']),schedule['scenes'][-1])
    if not row['case_id']:return {'case_id':None,'step':None,'fraction':None}
    f=max(0,min(1,(t-row['start'])/row['duration']))
    return {'case_id':row['case_id'],'step':row['step'],'fraction':(row['step']-1+f)/8}

def inside(project,relative):
    if not relative or Path(relative).is_absolute():raise ValueError('Assets must be project-relative')
    path=(project/relative).resolve()
    if not path.is_relative_to(project.resolve()):raise ValueError('Asset escapes project')
    return path

def delivery_gate(lesson,schedule,project,captures,execution):
    problems=[]
    if schedule['duration']>1800:problems.append('Film exceeds 30 minutes')
    if execution.get('environment')!='MATLAB Online' or execution.get('status')!='passed':problems.append('MATLAB Online execution not verified')
    if not execution.get('version') or not execution.get('run_id'):problems.append('Missing runtime identity')
    checks=execution.get('checks',{})
    if any(checks.get(k) is not True for k in ['case1','case2','case3','run_matlab_tests']):problems.append('Missing case/test checks')
    evidence=execution.get('artifacts',[])
    if not evidence:problems.append('No execution evidence artifacts')
    for asset in evidence:
        try:
            if sha(inside(project,asset['file']))!=asset['sha256']:raise ValueError('hash')
        except (OSError,KeyError,ValueError):problems.append('Invalid execution artifact')
    for s in schedule['scenes']:
        if not s['capture_id']:continue
        for bi,b in enumerate(s['beats']):
            if s['case_id'] and s['step']==1 and bi==0:continue
            m=captures.get(b['id'])
            if not m:problems.append('Missing Online capture: '+b['id']);continue
            try:
                if m.get('environment')!='MATLAB Online' or m.get('run_id')!=execution.get('run_id'):raise ValueError('capture run mismatch')
                if m.get('kind') not in {'image','video'}:raise ValueError('unknown capture kind')
                if sha(inside(project,m['file']))!=m['sha256']:raise ValueError('capture hash')
                if m['kind']=='video' and m.get('duration',0)-m.get('source_start',0)<b['end']-b['start']:raise ValueError('Video is shorter than its slot; supply a source-bound held still')
            except (OSError,KeyError,ValueError) as exc:problems.append('Invalid capture '+b['id']+': '+str(exc))
    return {'passed':not problems,'problems':problems,'scope':'Runtime and capture prerequisites; human audiovisual acceptance remains separate'}

CSS='''@font-face{font-family:EditorialTC;src:url(assets/fonts/NotoSansTC-Regular.otf)}@font-face{font-family:EditorialTC;src:url(assets/fonts/NotoSansTC-Bold.otf);font-weight:700}@font-face{font-family:Technical;src:url(assets/fonts/DejaVuSansMono.ttf)}*{box-sizing:border-box}html,body{margin:0}#root{position:relative;width:100%;height:100%;overflow:hidden;background:#F0EBE4;color:#292421;font-family:EditorialTC,sans-serif}.pv-frame{position:absolute;inset:0}.pv-chapter{position:absolute;left:72px;top:42px;font-size:27px}.pv-title{position:absolute;left:72px;top:88px;font-size:56px;font-weight:700;margin:0;line-height:1.2}.pv-badge{position:absolute;right:72px;top:45px;font-size:25px;border:2px solid #B72D2D;color:#B72D2D;padding:8px 18px}.pv-track{position:absolute;left:72px;top:168px;width:1160px;height:66px;display:flex;gap:10px}.pv-cell{position:relative;flex:1;background:#E0D7CD;border:2px solid #9B8D7E;border-radius:6px;overflow:hidden}.pv-fill{position:absolute;inset:0;background:#C8755D;transform-origin:0% 50%}.pv-number{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:27px;font-weight:700}.pv-current{border:4px solid #292421}.pv-main{position:absolute;left:72px;top:260px;width:1160px;height:630px;border:3px solid #9B8D7E;border-radius:15px;background:#FFFAF3;overflow:hidden}.pv-main img,.pv-main video{width:100%;height:100%;object-fit:contain}.pv-slot{position:absolute;inset:0}.pv-placeholder{position:absolute;inset:0;padding:66px;display:flex;flex-direction:column;justify-content:center;gap:28px}.pv-placeholder .tag{font-size:26px;color:#B72D2D}.pv-placeholder .action{font-size:48px;font-weight:700}.pv-placeholder .note{font-size:30px;line-height:1.6;max-width:950px}.pv-command{font:26px Technical,monospace;white-space:pre-wrap;overflow-wrap:anywhere;padding:20px;background:#F0EBE4;border-radius:10px}.pv-panel{position:absolute;left:1272px;top:260px;width:576px;height:500px;border:3px solid #9B8D7E;border-radius:15px;background:#FFFAF3;overflow:hidden}.pv-panel-title{position:absolute;left:24px;top:18px;width:520px;font-size:30px;font-weight:700;line-height:1.3}.pv-panel .diagram{position:absolute;left:25px;top:67px;width:520px;height:390px;font-family:EditorialTC,sans-serif}.pv-source{position:absolute;left:25px;bottom:12px;font-size:22px;color:#594E43}.pv-caption{position:absolute;left:130px;top:941px;width:1660px;max-height:110px;text-align:center;font-size:40px;line-height:1.3;background:#F0EBE4;padding:4px 16px}.pv-mascot{position:absolute;left:1620px;top:773px;width:160px;height:138px}.pv-guidance{position:absolute;left:1278px;top:795px;width:310px;font-size:27px;line-height:1.55}.pv-flow{display:grid;grid-template-columns:1fr 1fr;gap:18px;padding:32px}.pv-flow-item{font-size:29px;padding:16px;border:2px solid #9B8D7E;border-radius:8px;background:#F0EBE4;line-height:1.35}.pv-reference{position:absolute;left:72px;top:907px;font-size:22px;color:#594E43}'''

def mascot():
    return '<svg class="pv-mascot" viewBox="0 0 180 160"><path d="M38 55 Q80 0 117 55 L115 80 L38 80Z" fill="#292421"/><circle cx="77" cy="62" r="31" fill="#F2D4B7" stroke="#292421" stroke-width="3"/><path d="M43 106 Q77 88 111 106 L120 155 L35 155Z" fill="#C8755D" stroke="#292421" stroke-width="3"/><path d="M45 115 L15 90 M110 115 L146 75" fill="none" stroke="#292421" stroke-width="4" stroke-linecap="round"/><circle cx="66" cy="60" r="3" fill="#292421"/><circle cx="88" cy="60" r="3" fill="#292421"/><path d="M67 77 Q77 84 89 76" fill="none" stroke="#292421" stroke-width="3"/></svg>'

def command(s):
    return {'case1':'s1 = case1_sensor_classifier_matlab;','case2':'s2 = case2_image_measure_matlab;','case3':'s3 = case3_shape_classifier_matlab;'}.get(s['case_id'],'')

def scene_html(s,ch,captures,draft):
    sid=s['id'];duration=s['duration'];parts=[];js=[]
    parts.extend([f'<div class="pv-chapter">{esc(ch["title"])}</div>',f'<h1 class="pv-title">{esc((str(s["step"])+" / 8　") if s["step"] else "")}{esc(s["label"])}</h1>'])
    if draft:parts.append('<div class="pv-badge">製作預覽｜非實錄成品</div>')
    if s['case_id']:
        cells=[]
        for i in range(1,9):
            ident=f'{sid}-fill-{i}';cells.append(f'<div class="pv-cell {"pv-current" if i==s["step"] else ""}"><div id="{ident}" class="pv-fill"></div><span class="pv-number">{i}</span></div>')
            if i==s['step']:js.append(f'tl.fromTo("#{ident}",{{scaleX:0}},{{scaleX:1,duration:{duration},ease:"none"}},0);')
            else:js.append(f'gsap.set("#{ident}",{{scaleX:{1 if i<s["step"] else 0}}});')
        parts.append('<div class="pv-track">'+''.join(cells)+'</div>')
    for bi,b in enumerate(s['beats']):
        ident=b['id'];main=''
        if s['case_id'] and s['step']==1 and bi==0:
            main='<div class="pv-flow">'+''.join(f'<div class="pv-flow-item">{i+1}　{esc(step["label"])}</div>' for i,step in enumerate(ch['steps']))+'</div>'
        elif ident in captures:
            m=captures[ident]
            if m['kind']=='image':
                if m.get('crop'):
                    crop=m['crop'];x,y,w,h=[float(crop[k]) for k in ['x','y','width','height']]
                    iw,ih=[float(m['source_dimensions'][k]) for k in ['width','height']]
                    if min(x,y)<0 or min(w,h)<=0 or x+w>iw or y+h>ih:raise ValueError('Invalid source crop')
                    main=f'<svg width="100%" height="100%" viewBox="0 0 {w} {h}" style="overflow:hidden"><defs><clipPath id="{ident}-crop"><rect width="{w}" height="{h}"/></clipPath></defs><g clip-path="url(#{ident}-crop)"><image href="{esc(m["file"])}" x="{-x}" y="{-y}" width="{iw}" height="{ih}"/></g></svg>'
                else:main=f'<img src="{esc(m["file"])}" alt="{esc(s["label"])}的實際 MATLAB Online 畫面"/>'
            else:main=f'<video class="clip" id="{ident}-recording" src="{esc(m["file"])}" data-start="{b["start"]}" data-duration="{b["end"]-b["start"]}" data-media-start="{m.get("source_start",0)}" data-track-index="2" muted></video>'
        elif s['capture_id']:
            code=('<div class="pv-command">'+esc(command(s))+'</div>') if s['step']==1 else ''
            main=f'<div class="pv-placeholder"><div class="tag">操作畫面待錄製</div><div class="action">{esc(s["label"])}</div>{code}<div class="note">此區預留真實 MATLAB Online 操作。</div><div class="note">右側是教學示意；實際結果待本輪執行。</div></div>'
        else:
            main=f'<div class="pv-placeholder"><div class="tag">跟著做，也保留核對的方法</div><div class="action">{esc(s["label"])}</div><div class="note">{esc(ch["title"])}</div><div class="note">資料 → 操作 → 檢查 → 保存</div></div>'
        parts.append(f'<div class="pv-main" id="{ident}-main">{main}</div>')
        js.append(f'gsap.set("#{ident}-main",{{opacity:0}});tl.set("#{ident}-main",{{opacity:1}},{b["start"]});tl.set("#{ident}-main",{{opacity:0}},{b["end"]});')
        for j,state in enumerate(b['panels']):
            pid=f'{ident}-panel-{j}';kind=state['kind'];at=state['start'];end=state['end']
            parts.append(f'<div class="pv-panel" id="{pid}"><div class="pv-panel-title">{esc(LABELS[kind])}</div>{diagram(kind,s["case_id"])}<div class="pv-source">教學示意｜實測結果看左側操作畫面</div></div>')
            js.append(f'gsap.set("#{pid}",{{opacity:0}});tl.set("#{pid}",{{opacity:1}},{at});tl.set("#{pid}",{{opacity:0}},{end});tl.fromTo("#{pid} .diagram",{{scale:.96,y:8}},{{scale:1,y:0,duration:.45,ease:"power3.out",immediateRender:false}},{at});')
            js.append(f'document.querySelectorAll("#{pid} .draw").forEach(el=>{{const len=el.getTotalLength();gsap.set(el,{{strokeDasharray:len,strokeDashoffset:len}});tl.to(el,{{strokeDashoffset:0,duration:Math.min(.7,{end-at}),ease:"power2.out"}},{at});}});')
            js.append(f'document.querySelectorAll("#{pid} .bar").forEach((el,i)=>{{tl.fromTo(el,{{scaleX:0,transformOrigin:"0% 50%"}},{{scaleX:1,duration:.5,ease:"power2.out",immediateRender:false}},{at}+.15*i);}});')
    parts.extend([mascot(),'<div class="pv-guidance"><div>左邊看操作</div><div>右邊看這一步的意思</div></div>', '<div class="pv-reference">教材 v1.7｜合成案例練習｜程式與結果分開核對</div>'])
    return f'<template><style>{CSS}</style><div id="root" data-composition-id="{sid}" data-width="1920" data-height="1080" data-duration="{duration}"><div class="pv-frame">'+''.join(parts)+'</div></div><script>const tl=gsap.timeline({paused:true});'+''.join(js)+f'window.__timelines["{sid}"]=tl;</script></template>'

def stamp(t,separator=','):
    ms=round(t*1000);h,ms=divmod(ms,3600000);m,ms=divmod(ms,60000);s,ms=divmod(ms,1000)
    return f'{h:02}:{m:02}:{s:02}{separator}{ms:03}'

def build(project,lesson,voice,captures=None,execution=None,draft=True,selected=None):
    captures=captures or {};execution=execution or {};schedule=timeline(lesson,voice,project,selected)
    gate=delivery_gate(lesson,schedule,project,captures,execution)
    if not draft and not gate['passed']:raise ValueError('Delivery blocked: '+'; '.join(gate['problems']))
    project.mkdir(exist_ok=True,parents=True);(project/'compositions').mkdir(exist_ok=True);(project/'data').mkdir(exist_ok=True)
    chapters={c['id']:c for c in lesson['chapters']};slots=[]
    for s in schedule['scenes']:
        (project/'compositions'/f'{s["id"]}.html').write_text(scene_html(s,chapters[s['chapter_id']],captures,draft))
        (project/'compositions'/f'{s["id"]}.motion.json').write_text(json.dumps({'scene':s['id'],'duration':s['duration'],'rules':s['motion_rules'],'entry':{'from_rest':True},'exit':{'still_moving':False},'panels':[p for b in s['beats'] for p in b['panels']]},ensure_ascii=False,indent=2))
        slots.append(f'<div class="clip" id="slot-{s["id"]}" data-composition-id="{s["id"]}" data-composition-src="compositions/{s["id"]}.html" data-start="{s["start"]}" data-duration="{s["duration"]}" data-track-index="1" data-width="1920" data-height="1080" style="position:absolute;inset:0"></div>')
        for b in s['beats']:slots.append(f'<audio class="clip" id="voice-{b["id"]}" src="{esc(b["voice"]["file"])}" data-start="{s["start"]+b["start"]}" data-duration="{b["duration"]}" data-track-index="10"></audio>')
    for s in schedule['scenes']:
        capid=s['id']+'-captions';items=[]
        for i,c in enumerate(schedule['captions']):
            if s['start']<=c['start']<s['start']+s['duration']:
                items.append(f'<div class="clip pv-caption" id="caption-{i}" data-start="{c["start"]-s["start"]}" data-duration="{c["end"]-c["start"]}" data-track-index="20">{esc(c["text"])}</div>')
        capcss=CSS.replace('background:#F0EBE4;color:#292421;font-family:EditorialTC,sans-serif','background:transparent;color:#292421;font-family:EditorialTC,sans-serif')
        (project/'compositions'/f'{capid}.html').write_text(f'<template><style>{capcss}</style><div id="root" data-composition-id="{capid}" data-width="1920" data-height="1080" data-duration="{s["duration"]}">'+''.join(items)+f'</div><script>window.__timelines["{capid}"]=gsap.timeline({{paused:true}});</script></template>')
        slots.append(f'<div class="clip" id="slot-{capid}" data-composition-id="{capid}" data-composition-src="compositions/{capid}.html" data-start="{s["start"]}" data-duration="{s["duration"]}" data-track-index="20" data-width="1920" data-height="1080" style="position:absolute;inset:0"></div>')
    page=f'<!doctype html><html lang="zh-TW"><head><meta charset="utf-8"><script src="assets/vendor/gsap.min.js"></script><style>{CSS}</style></head><body><div id="root" data-composition-id="practice-master" data-width="1920" data-height="1080" data-duration="{schedule["duration"]}">'+''.join(slots)+'</div><script>window.__timelines["practice-master"]=gsap.timeline({paused:true});</script></body></html>'
    (project/'index.html').write_text(page)
    (project/'data/timeline.json').write_text(json.dumps(schedule,ensure_ascii=False,indent=2)+'\n')
    (project/'data/delivery-gate.json').write_text(json.dumps(gate,ensure_ascii=False,indent=2)+'\n')
    srt=[];vtt=['WEBVTT\n']
    for i,c in enumerate(schedule['captions'],1):
        srt.append(f'{i}\n{stamp(c["start"])} --> {stamp(c["end"])}\n{c["text"]}\n')
        vtt.append(f'{stamp(c["start"],".")} --> {stamp(c["end"],".")}\n{c["text"]}\n')
    (project/'data/captions.zh-TW.srt').write_text('\n'.join(srt));(project/'data/captions.zh-TW.vtt').write_text('\n'.join(vtt))
    return {'duration':schedule['duration'],'scenes':len(schedule['scenes']),'captions':len(schedule['captions']),'draft':draft,'delivery_ready':gate['passed']}
