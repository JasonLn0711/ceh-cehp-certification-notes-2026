"""Compile the complete M10 editorial remaster from source-bound scene specs.

Layout coordinates derive from versioned regions, measured font metrics and grids.
The immutable content, PCM and alignment contracts remain independently owned.
"""
from pathlib import Path
import html, json, math, re, copy
from .common import read, write, sha
from .remaster_early import SCENES as EARLY
from .remaster_late import SCENES as LATE

PROFILE = 'm10-editorial-remaster-v1.1'
SEMANTIC_SCENES = {'S01','S07','S17','S23','S27','S33','S40','S44','S47','S48','S49'}
SPECS = {**EARLY, **LATE}


def wrap(text, font, width):
    lines=[]
    for paragraph in str(text).split('\n'):
        line=''
        for word in paragraph.split():
            if font.getlength(word)>width:raise ValueError('Unbreakable text exceeds component: '+word)
            trial=(line+' '+word).strip()
            if line and font.getlength(trial)>width:lines.append(line);line=word
            else:line=trial
        if line:lines.append(line)
    return lines or ['']


def cue_times(p, scene, audio):
    cues={}
    for f in sorted((p.root/'scripts').glob('cues_*.json')):cues.update(read(f))
    phrases=cues[scene['id']]; spoken=[r for r in audio['segments'] if r['kind']=='spoken']
    result=[]
    for phrase in phrases:
        matches=[r for r in spoken if phrase.lower() in r['canonical'].lower()]
        if not matches:raise ValueError((scene['id'],'missing narration anchor',phrase))
        result.append(matches[0]['start_sample']/48000)
    return result


def text_svg(text, box, font, size, *, bold=False, center=True, label=False, guard=0):
    lines=wrap(text,font,box['width']-guard);height=len(lines)*size*1.15
    if height>box['height']+.25:raise ValueError(('Text overflow',text,box,height))
    x=box['x']+box['width']/2 if center else box['x'];y=box['y']+(box['height']-height)/2+size*.88
    attrs=' data-node-label="1" data-inner-x="{x}" data-inner-y="{y}" data-inner-width="{width}" data-inner-height="{height}"'.format(**box) if label else ''
    return '<text'+attrs+f' x="{x}" y="{y}" font-family="Editorial" font-size="{size}" font-weight="{700 if bold else 400}" text-anchor="{"middle" if center else "start"}">'+''.join(f'<tspan x="{x}" dy="{0 if i==0 else size*1.15}">{html.escape(line)}</tspan>' for i,line in enumerate(lines))+'</text>', dict(lines=lines,width=max(font.getlength(s) for s in lines),height=height,box=box,fontSize=size)


def inner_svg(file):
    value=file.read_text();match=re.search(r'viewBox="([^"]+)"',value)
    if not match:raise ValueError('Asset viewBox required: '+str(file))
    view=list(map(float,match.group(1).split()))
    return re.sub(r'^.*?<svg[^>]*>|</svg>\s*$','',value,flags=re.S),view



def layout_boxes(template, nodes, region, gap, maximum_height):
    """Versioned semantic arrangements; all positions derive from body constraints."""
    count=len(nodes)
    columns=2 if count<=4 else 3
    if count==3:columns=3
    if count==1:columns=1
    rows=math.ceil(count/columns)
    width=(region['width']-(columns-1)*gap)/columns
    height=min(maximum_height,(region['height']-(rows-1)*gap)/rows)
    top=region['y']+(region['height']-(height*rows+(rows-1)*gap))/2
    positions=list(range(count))
    # Process sequences read across the top, then back along the lower row.
    # Evidence/comparison figures retain aligned columns for paired inspection.
    if template in ('flow','sequence','timeline') and rows==2:
        positions=list(range(columns))+list(range(columns*2-1,columns-1,-1))[:count-columns]
    if template=='reflection':
        ports={'sender':0,'service':1,'claimed-return-address':2,'victim':3}
        positions=[ports[n['id']] for n in nodes]
    return [dict(x=region['x']+(i%columns)*(width+gap),y=top+(i//columns)*(height+gap),width=width,height=height) for i in positions]


def device_asset(node):
    """Illustration identity is authored and source-bound, never label-inferred."""
    if node.get('asset') and node.get('assetProvenance'):return node['asset']
    if node.get('asset') or node['kind']=='device':
        raise ValueError('DeviceIcon requires explicit asset identity and provenance: '+node['id'])
    return None


def scene_art(p,scene,audio,tokens,fonts):
    sid=scene['id'];spec=copy.deepcopy(SPECS[sid]);cues=cue_times(p,scene,audio)
    semantic=p.profile.get('visual_variant')=='semantic-v1.2' and sid in SEMANTIC_SCENES
    if semantic and sid=='S01':
        for n in spec['nodes']:
            if n['id']=='student':n.update(asset='authorized_student',assetProvenance='Original art_common.person used by S01; design/asset-provenance-v1.2.json')
    if semantic and sid=='S49':
        figures={'allowed':'evidence_slip','draft':'ai_sorter','review':'retake_check'}
        for n in spec['nodes']:
            n.update(asset=figures[n['id']],assetProvenance='Explicit semantic-v1.2 S49 variant; preserved approved props, design/asset-registry-v1.2.json')
    spec['presentation']='semantic-figure' if semantic else 'editorial-card'
    colors=tokens['colors'];ink=colors['ink'];paper=colors['paper_white'];accent=colors['terracotta'];soft=colors['apricot'];pad=tokens['layout']['objectPadding']
    region=tokens['layout']['body'];gap=tokens['layout']['gridGap'];nodes=spec.get('nodes',[]);components=[];parts=[];measurements=[]
    if spec['template']=='matrix':
        headers=spec['headers'];rows=spec['rows'];count=len(headers)
        fractions=([.12,.44,.44] if sid=='S58' else [1/count]*count)
        widths=[(region['width']-(count-1)*8)*f for f in fractions]
        height=(region['height']-len(rows)*8)/(len(rows)+1)
        for ri,row in enumerate([headers,*rows]):
            x=region['x']
            for ci,value in enumerate(row):
                node=dict(id=f'cell-{ri}-{ci}',label=value,kind='card',cue=min(max(ri-1,0),len(cues)-1))
                b=dict(x=x,y=region['y']+ri*(height+8),width=widths[ci],height=height)
                components.append(dict(**node,box=b,start=0 if ri==0 else cues[node['cue']],tableHeader=ri==0));x+=widths[ci]+8
    else:
        boxes=layout_boxes(spec['template'],nodes,region,gap,tokens['components']['semanticFigure']['maxHeight'] if semantic else tokens['layout']['cardMaxHeight'])
        for node,b in zip(nodes,boxes):
            start=cues[node['cue']]
            if sid=='S17' and node['id']=='pending':
                matches=[r for r in audio['segments'] if r['kind']=='spoken' and 'The server responds'.lower() in r['canonical'].lower()]
                if matches:start=matches[0]['start_sample']/48000
            components.append(dict(**node,box=b,start=start))
    for node in components:
        b=node['box'];w=b['width'];h=b['height'];kind=node['kind'];ident=sid+'-'+node['id'];body=[]
        if semantic:
            body.append(f'<rect data-component-bounds="1" x="0" y="0" width="{w}" height="{h}" fill="none" stroke="none"/>')
            node['presentation']='standalone'
        else:
            body.append(f'<rect class="card-frame" data-component-bounds="1" x="0" y="0" width="{w}" height="{h}" rx="8" fill="{soft if node.get("tableHeader") else paper}" stroke="{ink}" stroke-width="4"/>')
        # Component variants reserve their own measured label and resource geometry.
        bottom=50 if kind in ('bar','queue') else 0
        text_box=dict(x=pad,y=pad,width=w-2*pad,height=h-2*pad-bottom)
        asset=device_asset(node)
        if asset:
            file=p.root/'assets/props'/f'{asset}.svg'
            if str(file.relative_to(p.root)) not in p.profile['locked_assets']:raise ValueError('Unapproved device asset: '+asset)
            content,vb=inner_svg(file)
            icon=tokens['components']['deviceInline']['iconSize'];icon_gap=tokens['components']['deviceInline']['gap']
            candidate=dict(x=pad+icon+icon_gap,y=pad,width=w-2*pad-icon-icon_gap,height=h-2*pad-bottom)
            lines=wrap(node['label'],fonts['body'],candidate['width'])
            if semantic:
                label_lines=wrap(node['label'],fonts['body'],w-2*pad-tokens['typography']['measurementGuard'])
                label_height=len(label_lines)*30*1.15
                icon=min(w-2*pad,h-2*pad-bottom-label_height-tokens['components']['semanticFigure']['labelGap'])
                if icon<=0:raise ValueError(('Standalone icon does not fit',sid,node['id']))
                candidate=dict(x=pad,y=pad+icon+tokens['components']['semanticFigure']['labelGap'],width=w-2*pad,height=label_height+1)
                ix=(w-icon)/2;iy=pad;variant='standalone-semantic-figure'
            elif len(lines)*30*1.15>candidate['height']:
                # An explicit compact stacked variant retains the same font size.
                icon=tokens['components']['deviceStackedCompact']['iconSize']
                candidate=dict(x=pad,y=pad+icon+8,width=w-2*pad,height=h-2*pad-bottom-icon-8)
                wrap_lines=wrap(node['label'],fonts['body'],candidate['width'])
                if len(wrap_lines)*30*1.15>candidate['height']:
                    raise ValueError(('DeviceIcon label does not fit',sid,node['id'],node['label']))
                ix=(w-icon)/2;iy=pad;variant='device-stacked-compact'
            else:ix=pad;iy=(h-icon)/2;variant='device-inline'
            scale=min(icon/vb[2],icon/vb[3]);ix+=(icon-vb[2]*scale)/2;iy+=(icon-vb[3]*scale)/2
            body.append(f'<g class="locked-asset device-icon" data-asset="{asset}" transform="translate({ix} {iy}) scale({scale}) translate({-vb[0]} {-vb[1]})">{content}</g>')
            node['asset']=asset;node['assetSha256']=sha(file);node['componentVariant']=variant
            text_box=candidate
        bold=kind=='metric' or node.get('tableHeader',False)
        value,measurement=text_svg(node['label'],text_box,fonts['bold'] if bold else fonts['body'],30,bold=bold,label=True,guard=tokens['typography']['measurementGuard'])
        measurements.append(dict(id=ident,**measurement));body.append(value)
        if kind=='bar':
            fraction=max(0,min(1,node['value']/node['maximum']));bar_height=tokens['components']['resourceBar']['height'];by=h-pad-bar_height
            body.append(f'<rect x="{pad}" y="{by}" width="{w-2*pad}" height="{bar_height}" rx="4" fill="{colors["paper_shadow"]}"/><rect data-fill="1" x="{pad}" y="{by}" width="{(w-2*pad)*fraction}" height="{bar_height}" rx="4" fill="{accent}"/>')
        elif kind=='queue':
            cells=node.get('cells',8);cw=(w-2*pad-(cells-1)*4)/cells
            filled=math.ceil(cells*min(1,node['value']/node['maximum']))
            for k in range(cells):body.append(f'<rect data-cell="{k}" data-filled="{int(k<filled)}" x="{pad+k*(cw+4)}" y="{h-pad-24}" width="{cw}" height="24" rx="4" fill="{soft if k<filled else paper}" stroke="{ink}" stroke-width="2"/>')
        elif kind=='document' and not semantic:
            # Paper corner is structural geometry, outside the text rectangle.
            body.append(f'<path d="M{w-12} 0 L{w-12} 12 L{w} 12" fill="none" stroke="{ink}" stroke-width="2"/>')
        parts.append(f'<g id="{ident}" class="remaster-node" data-padding="16" data-node-id="{node["id"]}" transform="translate({b["x"]} {b["y"]})">'+''.join(body)+'</g>')
    edges=[];by_id={n['id']:n for n in components}
    for i,edge in enumerate(spec.get('edges',[])):
        e=dict(edge,id=f'{sid}-edge-{i}');e['startTime']=max(by_id[e['from']]['start'],by_id[e['to']]['start'],cues[e.get('cue',0)]);edges.append(e)
    # Rails retain the original artwork verbatim, with uniform scaling only.
    rails=[];rig_moves=[]
    file=p.root/'assets/props/school_building.svg';x=1535;y=330;w=180
    content,vb=inner_svg(file);scale=w/vb[2];h=vb[3]*scale
    parts.append(f'<g class="locked-asset" data-asset="campus" transform="translate({x} {y}) scale({scale})">{content}</g>')
    rails.append(dict(id='campus',x=x,y=y,width=w,height=h,sha256=sha(file),asset=str(file.relative_to(p.root)),originalAspect=vb[2]/vb[3]))
    # Preserve original isolated parts, layer order, .6 scale, shoulder pivot,
    # -12-degree gesture and .45/.5-second return from editorial.Art.tally.
    rig=[];rig_sources=[];x=1545;y=590;pose='point';at=cues[0]
    for part in ['legs','left_arm_'+pose,'right_arm_'+pose,'body','face_'+pose]:
        file=p.root/'assets/mascot/parts'/(part+'.svg');content,vb=inner_svg(file);ident=sid+'-tally-'+part
        rig.append(f'<g id="{ident}"><g transform="translate({x} {y}) scale(.6)">{content}</g></g>')
        rig_sources.append(dict(asset=str(file.relative_to(p.root)),sha256=sha(file)))
        rig_moves.append(dict(target=ident,start=at,duration=.8,**{'from':dict(opacity=0,x=0,y=20)},props=dict(opacity=1,x=0,y=0,ease='power2.out')))
    arm=sid+'-tally-right_arm_'+pose
    rig_moves.extend([dict(target=arm,start=at+1,duration=.45,props=dict(rotation=-12,svgOrigin=f'{x+185*.6} {y+128*.6}')),
                      dict(target=arm,start=at+1.45,duration=.5,props=dict(rotation=0))])
    parts.append('<g class="locked-asset" data-asset="tally">'+''.join(rig)+'</g>')
    file=p.root/'assets/mascot/rig_anchors.json'
    rails.append(dict(id='tally',x=1530,y=575,width=210,height=220,asset=str(file.relative_to(p.root)),sha256=sha(file),parts=rig_sources,originalAspect=.9,rigScale=.6,pose=pose))
    label,_=text_svg('Northstar',dict(x=1490,y=510,width=275,height=40),fonts['body'],30,guard=tokens['typography']['measurementGuard']);parts.append(label)
    note=spec.get('note','')
    if note:
        text,m=text_svg(note,tokens['layout']['note'],fonts['note'],28,guard=tokens['typography']['measurementGuard']);parts.append(f'<g id="{sid}-note" class="remaster-note">'+text+'</g>');measurements.append(dict(id=sid+'-note',**m))
    content=f'<svg class="art remaster-art" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" aria-label="{sid} editorial mechanism"><g id="{sid}-connections"></g>'+''.join(parts)+'</svg>'
    model=dict(scene=sid,duration=audio['samples']/48000,frames=audio['samples']//1600,components=components,edges=edges,rails=rails,tokens=tokens,noteStart=max(cues),spec=spec,rigMoves=rig_moves)
    write(p.root/'data'/f'{sid}.scene-spec.json',dict(scene=sid,**spec,audio_sha256=sha(p.root/'data'/f'{sid}.audio.json')))
    write(p.root/'data'/f'{sid}.layout.json',dict(scene=sid,components=components,rails=rails,textMeasurements=measurements,tokens_sha256=sha(p.root/p.profile['token_manifest']),exceptions=[]))
    return content,model


def compile_project(p,args,legacy):
    from PIL import ImageFont
    tokens=read(p.root/p.profile['token_manifest']);fonts={key:ImageFont.truetype(str(p.root/'assets/fonts/LiberationSans-Regular.ttf'),size) for key,size in [('body',30),('note',28)]}
    fonts['bold']=ImageFont.truetype(str(p.root/'assets/fonts/LiberationSans-Bold.ttf'),30)
    code=Path(__file__).parent/'visual';geometry=(code/'remaster-geometry.mjs').read_text();geometry=re.sub(r'\bexport\s+','',geometry)
    runtime=(code/'remaster-runtime.js').read_text();ready=[];ledger=[]
    selected=set(args.scenes.split(',')) if args.scenes else None
    for scene in p.scenes:
        sid=scene['id']
        if args.scene and sid!=args.scene or args.chapter and scene['chapter_id']!=args.chapter or selected and sid not in selected:continue
        audio=p.audio(sid);duration=audio['samples']/48000;moves=[]
        if sid in p.quiz_scenes():
            art,moves=legacy['quiz'](scene,audio);model=None
            write(p.root/'data'/f'{sid}.scene-spec.json',dict(scene=sid,template='quiz',source_sha256=sha(p.root/'data/questions.json')))
            write(p.root/'data'/f'{sid}.layout.json',dict(scene=sid,template='quiz',measured=read(p.root/'data'/f'{sid}.quiz-layout.json'),tokens_sha256=sha(p.root/p.profile['token_manifest']),exceptions=[]))
        else:
            art,model=scene_art(p,scene,audio,tokens,fonts);times=cue_times(p,scene,audio);grouped={}
            for i,label in enumerate(scene['on_screen_copy']):grouped.setdefault(times[i],[]).append(label)
            bindings=[];starts=sorted(grouped)
            for i,start in enumerate(starts):
                end=starts[i+1] if i+1<len(starts) else duration;value=' · '.join(grouped[start]);ident=f'{sid}-teaching{i}'
                art+=f'<div class="teaching" id="{ident}">{html.escape(value)}</div>';legacy['visibility'](moves,ident,start,end)
                bindings.append(dict(labels=grouped[start],rendered_label=value,start=start,end=end))
            write(p.root/'data'/f'{sid}.label-cues.json',bindings)
        caps=legacy['captions'](sid,audio)
        for i,cap in enumerate(caps):
            ident=f'{sid}-caption{i}';art+=f'<div class="caption" id="{ident}">{html.escape(cap["text"])}</div>';legacy['visibility'](moves,ident,cap['start'],cap['end'])
        simulation='' if sid in p.quiz_scenes() else '<div class="simulation-label">SIMULATED OUTPUT</div>'
        divider='' if sid in p.quiz_scenes() else '<div class="editorial-rule"></div>'
        markup=f'<div class="chapter">{html.escape(scene["chapter_id"]+" · "+scene["chapter_title"])}</div><h1 class="heading">{html.escape(scene["title"])}</h1>'+divider+simulation+art
        if model:moves.extend(model['rigMoves'])
        script=legacy['script'](moves,sid,duration)
        if model:script+='\n'+geometry+'\nconst model='+json.dumps(model)+';\n'+runtime
        # Layout measurement is complete before runtime capture. DOM checks verify it.
        script+='\nwindow.__hf=window.__hf||{};window.__hf.buildReady=window.__hf.buildReady||{};window.__hf.buildReady['+json.dumps(sid)+']=(async()=>{await document.fonts.load("34px Editorial");await document.fonts.load("700 54px Editorial");await document.fonts.ready;for(const e of document.querySelectorAll(".teaching")){e.style.top=Math.min(850,940-16-e.getBoundingClientRect().height)+"px";}})();'
        out=f'<!doctype html><html lang="en-US"><body><template><style>{legacy["active_css"]()}</style><div id="root" data-composition-id="{sid}" data-width="1920" data-height="1080" data-duration="{duration:.9f}">{markup}</div><script>(function(){{{script}}})();</script></template></body></html>'
        (p.root/'compositions'/f'{sid}.html').write_text(out)
        write(p.root/'compositions'/f'{sid}.motion.json',dict(scene=sid,duration=duration,frames=audio['samples']//1600,moves=moves,design_profile=PROFILE,assertions=[{'kind':'staysInFrame','selector':'.heading'},{'kind':'staysInFrame','selector':'.caption'}],source='integer narration audio-frame anchors'))
        write(p.root/'data'/f'{sid}.captions.json',caps);ready.append((scene,audio));ledger.append(dict(scene=sid,duration=duration,captions=len(caps),status='authored_pending_QA'))
        legacy['write_host']('review/'+sid,legacy['host']([(scene,audio)],'review-'+sid))
        print(json.dumps(dict(phase='remaster_scene_authored',scene=sid)),flush=True)
    if args.scene or selected:return
    (p.root/'index.html').write_text(legacy['host'](ready,'master'));write(p.root/'data/build-ledger.json',ledger)
    for chapter in sorted(set(s['chapter_id'] for s,a in ready)):
        legacy['write_host']('chapters/'+chapter,legacy['host']([(s,a) for s,a in ready if s['chapter_id']==chapter],chapter))
