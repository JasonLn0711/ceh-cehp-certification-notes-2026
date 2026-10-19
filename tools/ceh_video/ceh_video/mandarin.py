"""Locale-v2 production adapter; stages use the shared cache/process/review engine."""
from pathlib import Path
import json,os,subprocess,sys,time
from .common import read,write,sha

def validate_profile(d):
    assert d.get('schema_version')==2
    assert d.get('content')=={'locale':'zh-TW','narration_key':'narration_zh_TW'},'Explicit Mandarin content contract required'
    assert d.get('voice')=={'provider':'edge-tts','provider_version':'7.3.1','name':'zh-TW-HsiaoChenNeural','language':'zh-TW','baseline_rate':'+0%','atempo':1.5,'speed_applications':1},'Mandarin voice or single-speed contract changed'
    assert d['output']=={'width':1920,'height':1080,'fps':30,'sample_rate':48000,'channels':2,'video_rate':1.0,'bgm':False}
    assert d['quiz_silence_seconds']==1
    assert d['alignment']['backend']=='provider_word_boundaries'
    assert d['runtime']['max_chapter_renders']==2 and d['runtime']['render_workers']==4

def preflight(p,diagrams=True):
    validate_profile(p.profile);errors=[]
    def check(ok,why):
        if not ok:errors.append(why)
    exp=p.profile['expected'];ids=[s['id'] for s in p.scenes]
    check(len(ids)==len(set(ids))==exp['scenes'],'unique scene coverage')
    check(len(p.chapters)==exp['chapters'] and len(p.questions)==exp['questions'],'chapter/question counts')
    check(sum(len(s['narration_zh_TW']) for s in p.scenes)==exp['canonical_characters'],'canonical character coverage')
    banned=['科技犯罪偵查','警察','查扣','嫌疑人','被害人','詐騙機房']
    for s in p.scenes:
        copy=s['title']+s['takeaway']+s['narration_zh_TW']+''.join(s['labels'])
        check(not any(term in copy for term in banned),s['id']+': viewer-facing scope')
        check(''.join(x['text'] for x in s['audio_segments'] if x['kind']=='spoken')==s['narration_zh_TW'],s['id']+': complete canonical audio segments')
        holds=sum(x['kind']=='silence' for x in s['audio_segments']);check(holds==sum(q['scene_id']==s['id'] for q in p.questions),s['id']+': hold mapping')
        if diagrams:
            from .mandarin_art import build
            objects=build(s);check(bool(objects) or s['kind']=='quiz',s['id']+': actual diagram geometry')
    for q in p.questions:
        check(q['scene_id'] in ids and [c['letter'] for c in q['choices']]==list('ABCD') and q['correct_letter'] in 'ABCD',q['id']+': choices/key')
    for rel,h in p.profile['locked_assets'].items():check((p.root/rel).is_file() and sha(p.root/rel)==h,'locked asset '+rel)
    for rel in p.profile['fonts'].values():check((p.root/rel).is_file(),'local font '+rel)
    check((p.root/'assets/vendor/hw-arrow-helpers.js').is_file(),'local registry helper')
    check(read(p.root/'node_modules/hyperframes/package.json')['version']==p.profile['runtime']['hyperframes'],'renderer pin')
    coverage=read(p.root/'data/coverage.json');check(coverage['source_subquestion_groups']==15 and bool(coverage['targets']),'assessment coverage map')
    row={'status':'passed' if not errors else 'failed','errors':errors,'scenes':len(ids),'chapters':len(p.chapters),'questions':len(p.questions),'scope':'Source, profile, locked assets and real diagram geometry; actual media separate'}
    write(p.qa/'preflight.json',row)
    if errors:raise RuntimeError('Mandarin preflight failed: '+'; '.join(errors))
    return row

def hf_check(p,folder,times,name,emit):
    from .runner import subprocess_stage
    target=p.qa/name
    script='import subprocess,sys;f=open(sys.argv[1],"w");r=subprocess.run(sys.argv[2:],stdout=f);f.close();raise SystemExit(r.returncode)'
    command=[str(p.root/'.venv/bin/python'),'-c',script,str(target),str(p.root/'node_modules/.bin/hyperframes'),'check',str(folder),'--at',','.join(f'{t:.6f}' for t in sorted(set(times))),'--json']
    subprocess_stage(p,command,name.replace('.json',''),emit)
    r=read(target);assert r['ok'] and not r['browserSkipped'],str(target)
    return r

def action(p,node,emit,force=False):
    from .runner import subprocess_stage,worker
    from .mandarin_build import build_scene,host,assemble
    name=node.name
    if name.startswith('speech:'):
        from .mandarin_speech import synthesize
        synthesize(p,name.split(':')[1],emit)
    elif name.startswith('align:'):
        sid=name.split(':')[1]
        for row in p.audio(sid)['segments']:
            if row['kind']=='spoken':
                a=read(p.root/'data/forced-alignment'/f'{sid}-{row["sentence"]:03}.json')
                assert a['audio_sha256']==row['sha256'] and ''.join(w['text'] for w in a['words'])==row['canonical']
    elif name.startswith('scene:'):build_scene(p,name.split(':')[1])
    elif name.startswith('prepare:'):
        ch=name.split(':')[1];scenes=p.chapter_scenes(ch);folder=p.root/'chapters'/ch;duration=host(p,scenes,ch,folder);offset=0;times=[]
        for s in scenes:
            a=p.audio(s['id']);times.extend(offset+a['duration']*t for t in [.12,.5,.9])
            for r in a['segments']:
                if r['kind']=='silence':times.extend([offset+(r['start_sample']+r['end_sample'])/96000,offset+r['end_sample']/48000+.4])
            offset+=a['duration']
        write(p.qa/f'{ch}-timing.json',{'duration':duration,'frames':round(duration*30),'scenes':[s['id'] for s in scenes]})
        hf_check(p,folder,times,ch+'-check.json',emit)
        subprocess_stage(p,['node',str(Path(__file__).parent/'capture.mjs'),ch],name+'-captures',emit)
        worker(p,'contact_sheet',[str(p.qa/(ch+'-states'))],emit)
        write(p.qa/f'{ch}-checked-fingerprint.json',{'sha256':p.chapter_inputs(ch),'status':'checked_visual_review_pending'})
    elif name.startswith('render:'):
        from .review import require_review
        ch=name.split(':')[1];require_review(p,ch);before=p.chapter_inputs(ch)
        assert read(p.qa/f'{ch}-checked-fingerprint.json')['sha256']==before
        target=p.output/'chapters'/f'{ch}.mp4';target.parent.mkdir(exist_ok=True);started=time.monotonic()
        command=[str(p.root/'node_modules/.bin/hyperframes'),'render',str(p.root/'chapters'/ch),'--output',str(target),'--fps','30','--quality','delivery','--workers','4','--no-best-effort','--strict']
        subprocess_stage(p,command,'render-'+ch,emit)
        probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(target)]))
        video=next(x for x in probe['streams'] if x['codec_type']=='video');audio=next(x for x in probe['streams'] if x['codec_type']=='audio');expected=read(p.qa/f'{ch}-timing.json')
        assert (video['codec_name'],video['width'],video['height'],video['r_frame_rate'],audio['codec_name'])==('h264',1920,1080,'30/1','aac')
        assert abs(float(video['duration'])-expected['duration'])<.001 and before==p.chapter_inputs(ch)
        write(p.qa/f'{ch}-render.json',{'status':'rendered_codec_verified','source_sha256':before,'output_sha256':sha(target),'elapsed_seconds':time.monotonic()-started,'probe':probe})
    elif name=='root':
        info=assemble(p);m=read(p.root/'data/master-timing.json');times=[s['start']+s['duration']/2 for s in m['scenes']]+[(h['start']+h['end'])/2 for h in m['silences']]
        hf_check(p,p.root,times,'master-project-check.json',emit)
        subprocess_stage(p,['node',str(Path(__file__).parent/'mandarin_audit.mjs')],'mandarin-runtime-audit',emit)
        emit({'phase':'master_runtime_verified',**info})
    elif name=='master':worker(p,'assemble_master',[],emit)
    elif name in ['audio-review','checks','delivery','package']:
        from . import mandarin_delivery
        getattr(mandarin_delivery,name.replace('-','_'))(p,emit)
    else:raise ValueError(name)
    return 'actual_execution'
