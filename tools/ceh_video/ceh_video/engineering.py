"""Bounded versioned English migration and engineering checks; no full-film publication."""
from pathlib import Path
import shutil, subprocess, sys
from .common import Project, read, write, sha, lock
from .audio_policy import CURRENT, V12, modern


def migrate(reference,workspace,emit=lambda row:None,policy_id='ceh-en-v1.2'):
    if policy_id not in (CURRENT['id'],V12['id']):raise ValueError('Unsupported migration policy')
    contract=V12 if policy_id==V12['id'] else CURRENT
    source=Project(Path(reference)/'project');dest=Path(workspace).resolve()
    if dest.exists():raise ValueError('Migration destination must be new: '+str(dest))
    if source.profile.get('module')!='M10':raise ValueError('This bounded migration supports M10 only')
    from .preflight import preflight
    # Validate without writing into the historical workspace.
    from .preflight import validate_profile
    validate_profile(source.profile)
    protected={rel:sha(source.root/rel) for rel in source.profile['locked_assets']}
    assert protected==source.profile['locked_assets']
    dest.mkdir(parents=True);root=dest/'project';root.mkdir()
    for name in ('assets','models','.venv','node_modules','scripts','data'):
        emit(dict(phase='migration_copy',item=name))
        if policy_id==V12['id'] and name in ('.venv','node_modules'):
            (root/name).symlink_to((source.root/name).resolve(),target_is_directory=True)
            continue
        def exclude(folder,names):
            return [n for n in names if n=='__pycache__' or
                    (policy_id==V12['id'] and Path(folder)==source.root/'assets' and n=='audio')]
        shutil.copytree(source.root/name,root/name,symlinks=(name=='node_modules'),ignore=exclude)
    for f in source.root.iterdir():
        if f.is_file():shutil.copy2(f,root/f.name)
    for name in ('design','docs','provenance'):
        if (source.root/name).is_dir():
            shutil.copytree(source.root/name,root/name,symlinks=False)
    for rel in protected:
        target=root/rel
        if not target.exists():target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source.root/rel,target)
    (root/'compositions').mkdir(exist_ok=True)
    for name in ('qa','output'):(dest/name).mkdir()
    profile=read(root/'production.json')
    version=contract['id'].removeprefix('ceh-en-')
    from . import __version__
    profile.update(engine_version=__version__,release='motion-'+version,audio_policy=contract['id'],
                   baseline_runtime=source.profile.get('baseline_runtime','historical-runtime-unrecorded'),
                   default_intent='iteration',
                   master_filename='CEH_M10_Denial_of_Service_en-US_'+version.replace('.','_')+'_1_4x_master.mp4',
                   editable_filename='CEH_M10_motion_'+version.replace('.','_')+'_EDITABLE.zip')
    profile['voice']['atempo']=1.4
    write(root/'production.json',profile)
    (root/'ACTIVE_PRODUCTION_POLICY.md').write_text(f'''# Active production policy {version}

production.json selects {contract['id']}. Narration uses approved af_heart/en-US baseline0.73 and exactly one spoken-only atempo1.4. At48kHz stereo: opening{contract['opening']}, sentence gap{contract['gap']}, ending{contract['ending']}, quiz{contract['quiz']} frames. Chapter pauses reference existing ending+next opening; no extra pause is inserted. Alignment padding is separate. Video/animation1x, music off,1920×1080/30fps. New content bottom<=993.6; no legacy subtitle exception applies. Fonts and locked artwork retain source hashes. Historical metadata is provenance, not current policy. This migration does not establish rendered-film acceptance.
''')
    p=Project(root)
    from .speech import import_baselines
    count=import_baselines(source,p)
    processed=0
    if source.profile['voice']==p.profile['voice']:
        from .speech import import_cache
        processed=import_cache(p)
    # Copied legacy derived outputs are never evidence for the new policy.
    for pattern in ('*.audio.json','*.captions.json','*.label-cues.json','master-timing.json','build-ledger.json'):
        for f in (root/'data').glob(pattern):f.unlink()
    if not processed:shutil.rmtree(root/'data/forced-alignment',ignore_errors=True)
    write(p.qa/'migration.json',dict(source=str(source.root),destination=str(root),baseline_clips=count,processed_clips=processed,
          protected_hashes=protected,source_profile_sha256=sha(source.root/'production.json'),
          runtime_reuse={name:str((root/name).resolve()) for name in ('.venv','node_modules') if (root/name).is_symlink()},
          exception_ids=[],status='implemented',historical_runtime='unknown; preserved explicitly'))
    update_workspace_docs(p)
    return dict(project=str(root),baseline_clips=count,status='migrated')


def verify_audio(p,reference_track=True):
    import numpy as np
    import soundfile as sf
    from .speech import recipe,valid_cache
    from .common import digest
    from .audio_policy import timing
    policy=timing(p.profile);assert policy['id'] in (CURRENT['id'],V12['id'])
    holds=[];rows=[];total=0
    p.output.mkdir(exist_ok=True)
    track=sf.SoundFile(p.output/'master.reference.pcm.wav','w',samplerate=48000,channels=2,subtype='PCM_16') if reference_track else None
    try:
        for scene in p.scenes:
            sid=scene['id'];a=p.audio(sid);data,rate=sf.read(p.root/'assets/voice'/f'{sid}.wav',dtype='int16',always_2d=True)
            assert rate==48000 and data.shape==(a['samples'],2) and a['samples']%1600==0
            assert a['timing_policy']==policy and a['atempo']==1.4
            cursor=0;counts={}
            for item in a['ledger']:
                start,end=item['start_sample'],item['end_sample'];assert type(start)==type(end)==int and start==cursor and end>start
                n=end-start;kind=item['kind'];counts[kind]=counts.get(kind,0)+1
                if kind!='spoken':assert not np.count_nonzero(data[start:end]),(sid,kind,'nonzero PCM')
                if kind in ('opening','gap','ending','quiz'):assert n==policy[kind],(sid,kind,n)
                elif kind=='frame_alignment':assert 0<n<1600
                else:assert kind=='spoken'
                cursor=end
            assert cursor==len(data) and counts['opening']==counts['ending']==1
            assert a['ledger'][0]['kind']=='opening'
            spoken=[s for s in a['segments'] if s['kind']=='spoken']
            from .speech import sentences
            expected_sequence=[(segment['kind'],text)
                for segment in scene['audio_segments']
                for text in (sentences(segment['text']) if segment['kind']=='spoken' else [None])]
            assert [(segment['kind'],segment.get('canonical')) for segment in a['segments']]==expected_sequence
            assert [(x['start_sample'],x['end_sample']) for x in a['ledger'] if x['kind']=='spoken']==[(x['start_sample'],x['end_sample']) for x in spoken]
            assert counts.get('quiz',0)==sum(x['kind']=='silence' for x in a['segments'])
            assert counts.get('gap',0)==max(0,len(spoken)-1-counts.get('quiz',0))
            for seg in spoken:
                meta=read((p.root/seg['path']).with_suffix('.json'))
                assert valid_cache(p,seg['canonical']) and meta['recipe_sha256']==digest(recipe(p,seg['canonical']))
                assert meta['atempo']==1.4 and meta['speed_applications']==1
                assert sha(p.root/seg['path'])==seg['sha256']
                clip,clip_rate=sf.read(p.root/seg['path'],dtype='int16',always_2d=True)
                assert clip_rate==48000
                assert np.array_equal(data[seg['start_sample']:seg['end_sample']],clip),(sid,seg['sentence'],'assembled spoken PCM differs')
            for seg in a['segments']:
                if seg['kind']!='silence':continue
                assert seg['end_sample']-seg['start_sample']==48000 and seg['start_sample']%1600==0
                before=[s for s in spoken if s['end_sample']<=seg['start_sample']]
                after=[s for s in spoken if s['start_sample']>=seg['end_sample']]
                assert before and after
                question=next(q for q in p.questions if q['scene_id']==sid)
                canonical=' '.join(s['canonical'] for s in before)
                if 'prompt' in question:assert question['prompt'] in canonical
                for choice in question['choices']:assert choice['text'] in canonical
                holds.append(dict(scene=sid,start_sample=total+seg['start_sample'],end_sample=total+seg['end_sample'],frames=48000,nonzero_samples=0))
            if track is not None:track.write(data)
            rows.append(dict(scene=sid,samples=len(data),ledger_counts=counts,sha256=sha(p.root/'assets/voice'/f'{sid}.wav')));total+=len(data)
    finally:
        if track is not None:track.close()
    assert len(holds)==8 and sum(x['frames'] for x in holds)==384000
    result=dict(status='passed',policy=policy,scenes=rows,silent_intervals=holds,total_samples=total,video_frames=total//1600,
                scope='Lossless PCM only; AAC and human listening are separate',aac_boundary_status='not_evaluated')
    if policy['id']=='ceh-en-v1.2':
        from .timing_ledger import chapter_boundaries
        result['chapter_boundaries']=chapter_boundaries(p)
    write(p.qa/('audio-policy-'+policy['id'].removeprefix('ceh-en-')+'.json'),result);return result


def run(p,stage,emit=lambda row:None):
    assert modern(p.profile)
    from .speech import synthesize
    with lock(p.state/'engineering.lock'):
        if stage=='audio':
            rows=[]
            for i,scene in enumerate(p.scenes):
                rows.append(synthesize(p,scene['id'],emit));emit(dict(phase='scene_audio',completed=i+1,total=len(p.scenes)))
            report=verify_audio(p);write(p.qa/'audio-rebuild.json',rows)
            return dict(status=report['status'],scenes=len(rows),samples=report['total_samples'])
        if stage=='render-representatives':return render_representatives(p,emit)
        if stage=='verify-audio':return verify_audio(p,reference_track=False)
        if stage=='aac-audit':
            from .aac_audit import audit
            return audit(p,emit)
        if stage in ('align','build'):
            module='force_align' if stage=='align' else 'build_film'
            from .runner import subprocess_stage
            subprocess_stage(p,[str(p.root/'.venv/bin/python'),'-m','ceh_video.worker',module],stage,emit)
            if stage=='build':
                subprocess_stage(p,[str(p.root/'.venv/bin/python'),'-m','ceh_video.worker','export_metadata'],'export_metadata',emit)
            return dict(status='executed',stage=stage)
        raise ValueError('Unknown engineering stage')


def update_workspace_docs(p):
    """Archive copied operator wording before applying the new workspace contract."""
    names=['ENGINE_EDITING.md','VOICE_AND_AUDIO.md','DESIGN.md','AGENT_PROMPT.md','BRIEF.md','RENDER_PLAN.md','README.md','EDITING.md','START_HERE_zh-TW.md']
    history=p.root/'historical-reference';history.mkdir(exist_ok=True)
    header=f'> Active workspace: {p.profile["release"]}, engine {p.profile["engine_version"]}. Follow ACTIVE_PRODUCTION_POLICY.md. Historical descriptions below are source context, not current policy or evidence that this new workspace has rendered a full master. No legacy subtitle exception applies here.\n\n'
    for name in names:
        file=p.root/name
        if not file.exists():continue
        original=history/name
        if not original.exists():shutil.copy2(file,original)
        text=original.read_text().replace('atempo=1.5','atempo=1.4').replace('1.5×','1.4×').replace('1.5x','1.4x').replace('y945–1028','y940–993.6')
        file.write_text(header+text)
    write(p.qa/'operator-doc-migration.json',dict(status='implemented',historical={name:sha(history/name) for name in names if (history/name).exists()},active={name:sha(p.root/name) for name in names if (p.root/name).exists()}))


def render_representatives(p,emit=lambda row:None):
    """Render only the two named narrated scenes after automated engineering gates."""
    import json
    from concurrent.futures import ThreadPoolExecutor
    from .visual_gate import require_visual
    selected=['S17','S23'];require_visual(p,selected)
    def render(sid):
        check=read(p.qa/f'{sid}-hyperframes-check.json')
        if not check['ok'] or check['browserSkipped']:raise RuntimeError('HyperFrames check required: '+sid)
        inputs={'composition':sha(p.root/'compositions'/f'{sid}.html'),'audio':sha(p.root/'assets/voice'/f'{sid}.wav')}
        target=p.output/f'{sid}-motion-v1.1.mp4';log=p.qa/f'{sid}-representative-render.log'
        emit(dict(phase='representative_render_start',scene=sid,log=str(log)))
        from .runner import subprocess_stage
        subprocess_stage(p,[str(p.root/'node_modules/.bin/hyperframes'),'render',str(p.root/'review'/sid),'--output',str(target),'--fps','30','--quality','delivery','--workers','1','--no-best-effort','--strict'],sid+'-representative-render',emit)
        probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(target)]))
        video=next(x for x in probe['streams'] if x['codec_type']=='video');audio=next(x for x in probe['streams'] if x['codec_type']=='audio')
        assert (video['width'],video['height'],video['r_frame_rate'],int(video['nb_frames']))==(1920,1080,'30/1',p.audio(sid)['samples']//1600)
        assert audio['codec_name']=='aac' and audio['sample_rate']=='48000' and audio['channels']==2
        assert inputs=={'composition':sha(p.root/'compositions'/f'{sid}.html'),'audio':sha(p.root/'assets/voice'/f'{sid}.wav')}
        result=dict(status='rendered_codec_verified',scene=sid,inputs=inputs,path=str(target),sha256=sha(target),probe=probe,human_listening='not_performed')
        write(p.qa/f'{sid}-representative-render.json',result);emit(dict(phase='representative_render_verified',scene=sid));return result
    with ThreadPoolExecutor(max_workers=2) as pool:rows=list(pool.map(render,selected))
    return dict(status='tested',scenes=selected,outputs=[r['path'] for r in rows],scope='Two narrated representative scenes; no full-master delivery')
