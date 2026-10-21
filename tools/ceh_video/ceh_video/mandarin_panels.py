"""Source-bound picture panels with provider-word-timed editorial annotations."""
import base64, html, math, mimetypes, re
from .common import read, sha, write

def specification(p, sid):
    if not p.profile.get('teaching_panels'): return []
    return read(p.root/p.profile['teaching_panels']).get(sid, [])

def assets(p):
    return {r['id']:r for r in read(p.root/'data/teaching-assets.json')}

def cue_time(p, sid, audio, phrase):
    for seg in audio['segments']:
        if seg['kind']!='spoken' or phrase not in seg['canonical']: continue
        target=seg['canonical'].index(phrase); offset=0
        for word in read(p.root/'data/forced-alignment'/f'{sid}-{seg["sentence"]:03}.json')['words']:
            offset+=len(word['text'])
            if offset>target:return seg['start_sample']/48000+word['start']
    raise ValueError(f'{sid}: panel cue absent from aligned narration: {phrase}')

def layout_objects(objects):
    """Reserve x=1340..1790 above the existing mascot; preserve all main objects."""
    result=[]
    for original in objects:
        o=dict(original)
        for k in ('x','x1','x2'):
            if k in o:o[k]=145+(o[k]-145)*.82
        for k in ('y','y1','y2'):
            if k in o:o[k]=270+(o[k]-270)*.82
        for k in ('w','h','size','rx'):
            if k in o:o[k]*=.82
        result.append(o)
    return result

def resolved(p,sid,audio):
    inventory=assets(p);rows=[]
    for spec in specification(p,sid):
        asset=inventory[spec['asset']];f=p.root/asset['file']
        if sha(f)!=asset['sha256']:raise ValueError('Teaching image changed: '+str(f))
        rows.append({**spec,'start':cue_time(p,sid,audio,spec['cue']),'file':asset['file'],'sha256':asset['sha256'],'source_type':asset['type']})
    rows.sort(key=lambda r:r['start'])
    for i,r in enumerate(rows):r['end']=rows[i+1]['start'] if i+1<len(rows) else audio['duration']
    return rows

def image_box(path):
    if path.suffix=='.svg':
        w,h=map(float,re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"',path.read_text()).groups())
    else:
        from PIL import Image
        with Image.open(path) as im:w,h=im.size
    scale=min(410/w,250/h);w*=scale;h*=scale
    return 20+(410-w)/2,55+(250-h)/2,w,h

def markup(p,sid,audio):
    rows=resolved(p,sid,audio);parts=[];motion=[]
    for i,r in enumerate(rows):
        ident=f'{sid}-source-{i}';f=p.root/r['file'];mime=mimetypes.guess_type(str(f))[0]
        data='data:'+mime+';base64,'+base64.b64encode(f.read_bytes()).decode()
        ix,iy,iw,ih=image_box(f)
        x,y=r['point'];x=ix+iw*x;y=iy+ih*y
        # A short draw-on pointer approaches the named region without covering it.
        ax=max(25,min(425,x+75));ay=max(65,y-55);angle=math.atan2(y-ay,x-ax)
        path=f'M{ax} {ay} L{x} {y} M{x-16*math.cos(angle+.5)} {y-16*math.sin(angle+.5)} L{x} {y} L{x-16*math.cos(angle-.5)} {y-16*math.sin(angle-.5)}'
        box=''
        if r.get('box'):
            bx,by,bw,bh=r['box'];box=f'<rect x="{ix+iw*bx}" y="{iy+ih*by}" width="{iw*bw}" height="{ih*bh}" rx="4" fill="none" stroke="#C62828" stroke-width="4"/>'
        # Image uses a fixed contained box. Annotation coordinates are in that box;
        # all diagram assets are framed to it by the SVG viewBox, not cropped.
        parts.append(f'<div id="{ident}" class="source-panel" data-source-sha="{r["sha256"]}" data-source-kind="{r["source_type"]}" style="opacity:0"><div class="source-title">{html.escape(r["title"])}</div><img id="{ident}-image" src="{data}" alt="{html.escape(r["title"])}"/><svg class="source-annotations" viewBox="0 0 450 380"><g id="{ident}-box">{box}</g><g id="{ident}-arrow"><path d="{path}" fill="none" stroke="white" stroke-width="9" stroke-linecap="round"/><path d="{path}" fill="none" stroke="#C62828" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></g></svg><div class="source-note">{html.escape(r["caption"])}</div></div>')
        t=r['start'];end=r['end'];draw=min(.7,max(.15,(end-t)/4))
        motion.append(f'gsap.set("#{ident}",{{opacity:0}});tl.set("#{ident}",{{opacity:1}},{t});tl.set("#{ident}",{{opacity:0}},{end});')
        motion.append(f'gsap.set("#{ident}-box",{{opacity:0}});tl.to("#{ident}-box",{{opacity:1,duration:{draw},ease:"sine.out"}},{t});')
        # Existing registry arrow helper is reused for both halo and red stroke.
        motion.append(f'document.querySelectorAll("#{ident}-arrow path").forEach(path=>{{const length=path.getTotalLength();gsap.set(path,{{strokeDasharray:length,strokeDashoffset:length}});tl.to(path,{{strokeDashoffset:0,duration:{draw},ease:"power2.inOut"}},{t});}});')
    write(p.root/'data'/f'{sid}.panels.json',{'scene':sid,'panel_box':[1340,260,450,380],'mascot_top':650,'states':rows})
    return ''.join(parts),'\n'.join(motion)

CSS='''.source-panel{position:absolute;left:1340px;top:260px;width:450px;height:380px;background:#FFFAF3;border:2px solid #B8B0A9;border-radius:12px;overflow:hidden}.source-title{position:absolute;left:18px;top:10px;width:414px;font-size:28px;font-weight:700;line-height:1.25}.source-panel img{position:absolute;left:20px;top:55px;width:410px;height:250px;object-fit:contain}.source-annotations{position:absolute;inset:0;width:450px;height:380px;pointer-events:none}.source-note{position:absolute;left:18px;top:316px;width:414px;font-size:21px;line-height:1.3;color:#292421}'''
