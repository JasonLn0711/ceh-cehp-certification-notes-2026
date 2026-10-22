from ceh_video.audio_policy import modern
"""Validate actual outputs and close a self-contained, extracted/hash-checked archive."""
from pathlib import Path
import csv, json, math, re, shutil, tempfile, zipfile
from .common import read, sha, write
from .review import require_review,require_encoded


def export_qa(path):
    """Ship production evidence; keep unrelated Git/Planning custody notes local."""
    return path.suffix in {'.json','.jsonl','.md'} and bool(re.match(
        r'^(?:C\d+-(?:check|checked-fingerprint|render|timing|review)|audio-|asr-|recognition-|reference-|live-|clean-|production-|resume-|baseline-|benchmark-|late-|encoded-|quiz-|scene-seek-|rendered-|master-|engine-|run-|historical-|alignment-|migration[-.]|remaster-|visual-|all-text-|cross-scene-|local-ci|preflight\.|document-links\.)',path.name))


def validate_source_content(profile,source,current,source_questions,current_questions):
    """Permit release-envelope updates only for the explicit remaster profile."""
    if profile.get('design_profile')=='m10-editorial-remaster-v1.1':
        allowed={'version','status','actual_final_mp4_rendered','playback_rate','narration_speed_multiplier','voice','delivery_effective_wpm_range'}
        assert {k:v for k,v in source.items() if k not in allowed}=={k:v for k,v in current.items() if k not in allowed},'Canonical scene payload or protected metadata changed'
        assert source_questions['questions']==current_questions['questions'],'Canonical questions changed'
        assert current.get('narration_speed_multiplier')==1.4
        assert current.get('voice',{}).get('baseline_speed')==.73
        assert current.get('voice',{}).get('postprocess')=='exactly one atempo=1.4 on spoken clips'
    else:
        assert source==current,'Release canonical content changed; use a separate authored release'
        assert source_questions==current_questions,'Release canonical questions changed'


def bundle_engine(target):
    """Bundle the running maintained engine, never a stale project's vendor tree."""
    source=Path(__file__).resolve().parent
    if target.exists():shutil.rmtree(target)
    shutil.copytree(source,target,ignore=shutil.ignore_patterns('__pycache__','*.pyc','node_modules'))
    return {str(f.relative_to(target)):sha(f) for f in sorted(target.rglob('*')) if f.is_file()}


def audio_restore_manifest(p):
    """Portable provenance references source media, not operational cache directories."""
    from .speech import valid_cache,baseline_entry,cache_entry
    items=[]
    for scene in p.scenes:
        for seg in p.audio(scene['id'])['segments']:
            if seg['kind']!='spoken':continue
            assert valid_cache(p,seg['canonical'])
            items.append({'canonical':seg['canonical'],'processed':seg['path'],'baseline':seg['baseline_path'],
                'metadata':str(Path(seg['path']).with_suffix('.json')),
                'baseline_receipt':read(baseline_entry(p,seg['canonical'])/'receipt.json'),
                'processed_receipt':read(cache_entry(p,seg['canonical'])/'receipt.json')})
    return {'schema_version':1,'scope':'Verified raw/processed media provenance for explicit local cache reconstruction','items':items}


def restore_packaged_audio_cache(p):
    """Explicit restoration from archived verified media; performs no synthesis/tempo pass."""
    from .speech import baseline_entry,cache_entry,baseline_recipe,recipe,valid_cache
    record=read(p.root/'provenance/audio-restore.json')
    for item in record['items']:
        text=item['canonical'];raw=p.root/item['baseline'];processed=p.root/item['processed'];metadata=p.root/item['metadata']
        base=item['baseline_receipt'];receipt=item['processed_receipt']
        assert base['recipe']==baseline_recipe(p,text) and receipt['recipe']==recipe(p,text)
        assert sha(raw)==base['sha256']==receipt['baseline_sha256']
        assert sha(processed)==receipt['processed_sha256'] and sha(metadata)==receipt['metadata_sha256']
        b=baseline_entry(p,text);b.mkdir(parents=True,exist_ok=True);shutil.copy2(raw,b/'baseline.wav');write(b/'receipt.json',base)
        c=cache_entry(p,text);c.mkdir(parents=True,exist_ok=True)
        for source,name in [(raw,'baseline.wav'),(processed,'processed.wav'),(metadata,'metadata.json')]:shutil.copy2(source,c/name)
        write(c/'receipt.json',receipt);assert valid_cache(p,text)
    return {'status':'verified_media_cache_restored','clips':len(record['items']),'new_inferences':0,'tempo_passes':0}


from .audio_review import require_minimum_asr, remaster_audio_review


def validate(p):
    from .visual_gate import require_visual
    require_visual(p,list(p.by_id))
    if p.profile.get('audio_policy')=='ceh-en-v1.2':
        from .root_check import require_current
        require_current(p)
    import numpy as np
    import soundfile as sf
    source=(p.root/p.profile['source_package']).resolve();source_hashes=0
    for line in (source/'FILES_SHA256.txt').read_text().splitlines():
        if not line or line.startswith('#'):continue
        h,name=line.split(None,1);assert sha(source/name.lstrip('* '))==h;source_hashes+=1
    validate_source_content(p.profile,read(source/'scenes.json'),read(p.root/'data/scenes.json'),read(source/'questions.json'),read(p.root/'data/questions.json'))
    if modern(p.profile):
        from .engineering import verify_audio
        verify_audio(p,False)
    if p.profile.get('design_profile')=='m10-editorial-remaster-v1.1':remaster_audio_review(p)
    clips=0;words=0;holds=[];duration=0;total_samples=0;captions=[]
    for s in p.scenes:
        sid=s['id'];a=p.audio(sid);pcm,sr=sf.read(p.root/'assets/voice'/f'{sid}.wav',dtype='int16',always_2d=True)
        assert sr==48000 and pcm.shape==(a['samples'],2) and len(pcm)%1600==0
        text=' '.join(r['canonical'] for r in a['segments'] if r['kind']=='spoken')
        assert text==' '.join(s['narration_en_US'].split());words+=len(text.split())
        caps=read(p.root/'data'/f'{sid}.captions.json');assert ' '.join(c['text'] for c in caps)==text
        for row in a['segments']:
            if row['kind']=='spoken':
                f=p.root/row['path'];meta=read(f.with_suffix('.json'));assert sha(f)==row['sha256']
                assert meta['baseline_speed']==.73 and meta['atempo']==p.profile['voice']['atempo'] and meta['speed_applications']==1
                alignment=read(p.root/'data/forced-alignment'/f'{sid}-{row["sentence"]:03}.json');assert alignment['audio_sha256']==row['sha256'];clips+=1
            else:
                zero=pcm[row['start_sample']:row['end_sample']];assert zero.shape==(48000,2) and not np.any(zero)
                for c in caps:assert c['end']<=row['start_sample']/48000+1e-5 or c['start']>=row['end_sample']/48000-1e-5
                holds.append(sid)
        for c in caps:
            assert 0<=c['start']<c['end']<=a['duration'];captions.append({**c,'start':c['start']+duration,'end':c['end']+duration})
        total_samples+=a['samples'];duration=total_samples/48000
    assert words==p.profile['expected']['canonical_words'] and len(holds)==len(p.questions)
    assert all(a['end']<=b['start']+.001 for a,b in zip(captions,captions[1:]))
    for ch in p.chapters:
        require_review(p,ch);check=read(p.qa/f'{ch}-check.json');r=read(p.qa/f'{ch}-render.json')
        assert check['ok'] and not check['browserSkipped'];assert r['status']=='rendered_codec_verified'
        assert r['source_sha256']==p.chapter_inputs(ch) and sha(p.output/'chapters'/f'{ch}.mp4')==r['output_sha256']
        if p.profile.get('design_profile')=='m10-editorial-remaster-v1.1':
            gpu=r['gpu'];assert gpu['requested_mode']==gpu['observed_mode']=='hardware' and gpu['renderer']==p.profile['runtime']['expected_gpu_renderer']
            assert gpu['stdout_sha256']==sha(p.qa/f'{ch}-render.log') and gpu['stderr_sha256']==sha(p.qa/f'{ch}-render.log.stderr')
    require_encoded(p)
    probe=read(p.qa/'master-ffprobe.json');v=next(s for s in probe['streams'] if s['codec_type']=='video');a=next(s for s in probe['streams'] if s['codec_type']=='audio')
    assert (v['codec_name'],v['width'],v['height'],v['r_frame_rate'],a['codec_name'],a['sample_rate'],a['channels'])==('h264',1920,1080,'30/1','aac','48000',2)
    assert int(v['nb_read_frames'])==total_samples//1600 and len(probe['chapters'])==len(p.chapters)
    artifact=read(p.qa/'rendered-artifact-audit.json')
    if probe.get('ceh_frame_count_evidence') or artifact.get('full_decode_receipt'):
        from .media_scan import require_scan
        scan=require_scan(p.output/p.profile['master_filename'],total_samples//1600,p.qa)
        assert probe['ceh_frame_count_evidence']=={'method':'ffmpeg_full_decode_progress','receipt':'master-full-decode.json','master_sha256':scan['master_sha256']}
        assert artifact['frames']==scan['decoded_frames'] and artifact['master_sha256']==scan['master_sha256']
        from .master_audio_cache import audio_key
        cached=read(p.qa/'master-audio-cache.json')
        assert cached['master_sha256']==scan['master_sha256']
        assert cached['key']==audio_key(p.output/'master.reference.pcm.wav',total_samples,p.profile)
    artifact=read(p.qa/'rendered-artifact-audit.json');assert artifact['decoded_entire_master'] and artifact['black_intervals']==0
    continuity=read(p.qa/'audio-continuity-audit.json');assert continuity['status']=='passed'
    if p.profile.get('design_profile')=='m10-editorial-remaster-v1.1':
        master_hash=sha(p.output/p.profile['master_filename'])
        assert continuity['master_sha256']==master_hash and continuity['reference_sha256']==sha(p.output/'master.reference.pcm.wav')
        residue=read(p.qa/'master-aac-boundaries.json')
        assert residue['status']=='measured' and residue['master_sha256']==master_hash
        assert len(residue['holds'])==8 and all(x['frames']==48000 for x in residue['holds'])
    if p.profile.get('design_profile')!='m10-editorial-remaster-v1.1':
        quiz=read(p.qa/'quiz-runtime/checks.json');assert quiz['status']=='passed' and quiz['checks']==8*len(p.questions)
        seek=read(p.qa/'scene-seek-audit.json');assert seek['status']=='passed' and seek['comparisons']==3*len(p.scenes)
    # Remaster scene/quiz/all-frame/boundary coverage was verified by require_visual above.
    result={'status':'automated_delivery_checks_passed','module':p.profile['module'],'engine_version':p.profile['engine_version'],'runtime':p.profile['runtime'],'source_hashes':source_hashes,'canonical_words':words,'clips':clips,'scenes':len(p.scenes),'chapters':len(p.chapters),'captions':len(captions),'duration':duration,'frames':total_samples//1600,'zero_pcm_holds':len(holds),'pcm_frames_per_hold':48000,'master_sha256':sha(p.output/p.profile['master_filename']),'encoded_samples':len(artifact['sampled_frames'])+read(p.qa/'late-diagram-samples.json')['count'],'human_listening':'pending','pronunciation_accuracy':'not_evaluated','public_media_release':'not_activated'}
    minimum=p.qa/'asr-availability-minimum.json'
    result['asr_availability']=read(minimum).get('execution_status') if minimum.is_file() else 'not_evaluated'
    asr_note='A single real inference establishes minimum ASR availability; full-film transcription, accuracy and latency remain not_evaluated.' if result['asr_availability']=='LIVE_MINIMUM_COMPLETED' else 'Independent ASR availability, accuracy and latency remain not_evaluated for this release.'
    write(p.qa/'engine-delivery.json',result)
    (p.output/'engine-render-report.md').write_text(f'''# {p.profile['title']} — optimized production engine

Actual complete film: {duration:.6f} seconds, {total_samples//1600:,} frames, {len(p.scenes)} scenes, {len(p.chapters)} chapters, {words:,} canonical words and {len(captions):,} subtitle cues. Engine {p.profile['engine_version']}; HyperFrames {p.profile['runtime']['hyperframes']}.

The approved editorial, voice and silence policies remain intact. All {clips} speech clips have verified recipes. Each of {len(holds)} quiz holds contains exactly 48,000 stereo zero PCM frames. Decoded lossy AAC residue is recorded separately. Full decode, scene seeks, quiz boundaries, chapter/master fingerprints, artifact-bound sampled visual review and PCM/AAC continuity passed.

Source package and historical releases remain immutable. New implementation, runtime and output identities have separate receipts. Human pronunciation, naturalness and full-film listening acceptance remain pending; the prioritized queue records unresolved review leads. {asr_note}

Start with project/ENGINE_EDITING.md in the editable archive. Production profile, pronunciation policy, bundled engine, models, fonts, native diagrams and regeneration inputs are included. Environments, node_modules and runtime caches are excluded; verified speech PCM is included for restoration. Final media are adjacent to the ZIP. See qa/engine-delivery.json, qa/visual/golden-approval.json, native chapter review receipts, qa/encoded-review.json and integration evidence for the exercised layers. Historical reference-import receipts apply only to workspaces created by reference import.

Master SHA-256: {result['master_sha256']}.
''')
    return result


def bundle_encoded_evidence(p,staging):
    """Carry the actual reviewed encoded frames with their existing review hashes."""
    review=read(p.qa/'encoded-review.json')
    audit=read(p.qa/'rendered-artifact-audit.json');late=read(p.qa/'late-diagram-samples.json')
    names=[r['file'] for r in [*audit['sampled_frames'],*late['samples']]]
    expected=len(p.scenes)+3*len(p.chapters)+3*len(p.questions)+len(p.scenes)-len(p.questions)
    assert len(names)==len(set(names))==expected,'Incomplete encoded picture inventory'
    assert set(names)==set(review['captures']),'Encoded review/capture inventory mismatch'
    folder=staging/'output/inspection_frames';folder.mkdir(parents=True,exist_ok=True)
    for name in names:
        assert Path(name).name==name and name.endswith('.png'),'Invalid encoded capture path'
        source=p.output/'inspection_frames'/name
        assert sha(source)==review['captures'][name],'Stale encoded capture: '+name
        shutil.copy2(source,folder/name)
    for source in sorted((p.output/'inspection_frames').glob('*contact*.jpg')):shutil.copy2(source,folder/source.name)
    record={'scope':'Exact encoded pictures bound to the current encoded review; full movie is delivered adjacent to the archive','master_sha256':review['master_sha256'],'captures':review['captures'],'required_frames':expected}
    write(staging/'qa/encoded-frame-manifest.json',record)
    return record


def verify_encoded_evidence(base):
    """Validate extracted images against both inventory and artifact-bound review."""
    manifest=read(base/'qa/encoded-frame-manifest.json');review=read(base/'qa/encoded-review.json')
    audit=read(base/'qa/rendered-artifact-audit.json');late=read(base/'qa/late-diagram-samples.json')
    names=[r['file'] for r in [*audit['sampled_frames'],*late['samples']]]
    assert len(names)==len(set(names))==manifest['required_frames']
    assert set(names)==set(manifest['captures'])==set(review['captures'])
    assert manifest['master_sha256']==review['master_sha256'] and manifest['captures']==review['captures']
    for name,expected in manifest['captures'].items():
        assert Path(name).name==name
        assert sha(base/'output/inspection_frames'/name)==expected,'Extracted encoded capture changed: '+name
    return {'status':'extracted_encoded_frames_hash_verified','frames':len(names),'master_sha256':manifest['master_sha256']}



def verify_golden_review_evidence(base):
    """Verify the candidate and review receipts cited by the shipped approval."""
    qa=Path(base)/'qa'
    approval=read(qa/'visual/golden-approval.json')
    assert approval.get('decision')=='approved_initial_golden','Missing golden approval decision'
    candidate=qa/'visual/candidate-final-manifest.json'
    assert sha(candidate)==approval.get('candidate_sha256'),'Golden candidate manifest changed'
    receipts=approval.get('review_receipts',{})
    required={'early-candidate-review-final-freeze/review.json',
              'visual/agent-review-late-port-normal-final/candidate-review.json'}
    profile=Path(base)/'project/production.json'
    if profile.is_file() and read(profile).get('audio_policy')=='ceh-en-v1.2':
        required={'visual/agent-review-v1.2.json'}
    assert required<=set(receipts),'Incomplete golden review receipt inventory'
    for name,expected in receipts.items():
        rel=Path(name)
        assert not rel.is_absolute() and '..' not in rel.parts,'Invalid golden review receipt path'
        assert sha(qa/rel)==expected,'Golden review receipt changed: '+name
    if required=={'visual/agent-review-v1.2.json'}:
        review=read(qa/'visual/agent-review-v1.2.json')
        assert review.get('status')=='agent_visual_review_completed'
        assert review.get('candidate_sha256')==sha(candidate)
        manifest=read(candidate)
        assert set(review.get('scenes',[]))==set(manifest['sources'])
        assert set(review.get('approved_states',[]))=={r['name'] for r in manifest['rows']}
        inspected=set(review.get('visually_inspected_states',[]))
        assert inspected and inspected<=set(review['approved_states'])
        assert all(any(name.startswith(sid+'-') for name in inspected) for sid in manifest['sources'])
        assert review.get('contact_sheets') and review.get('findings')
        for name,expected in review['contact_sheets'].items():
            rel=Path(name);assert not rel.is_absolute() and '..' not in rel.parts
            assert sha(qa/rel)==expected,'Review contact sheet changed'
    return {'status':'golden_candidate_and_review_hashes_verified',
            'approval_sha256':sha(qa/'visual/golden-approval.json'),
            'candidate_sha256':sha(candidate),'review_receipts':receipts}



def copy_remaster_qa(source, target, ignore):
    """Ship evidence, excluding reproducible boundary hosts with linked media trees."""
    source=Path(source)
    def evidence_ignore(folder,names):
        omitted=list(ignore(folder,names))
        if source.name=='remaster-boundaries' and Path(folder)==source and 'hosts' in names:
            omitted.append('hosts')
        return omitted
    shutil.copytree(source,target,ignore=evidence_ignore)


def package(p,emit):
    d=read(p.qa/'engine-delivery.json');assert d['status']=='automated_delivery_checks_passed';require_encoded(p)
    archive=p.output/p.profile['editable_filename'];staging=p.output/'engine_project_source'
    if staging.exists():raise RuntimeError('Reconcile existing closed package before replacing '+str(staging))
    def ignore(folder,names):return [n for n in names if n in {'.venv','node_modules','.production','.hyperframes','.waveform-cache','__pycache__','review','.git'} or n.endswith('.tmp')]
    staging.mkdir();shutil.copytree(p.root,staging/'project',ignore=ignore);shutil.copytree(p.root.parent/'inputs',staging/'inputs');(staging/'qa').mkdir()
    for f in p.qa.iterdir():
        if f.is_file() and export_qa(f):shutil.copy2(f,staging/'qa'/f.name)
    if p.profile.get('design_profile')=='m10-editorial-remaster-v1.1':
        for ch in p.chapters:
            for suffix in ('-render.log','-render.log.stderr'):shutil.copy2(p.qa/(ch+suffix),staging/'qa'/(ch+suffix))
    engine_manifest=bundle_engine(staging/'project/vendor/ceh_video')
    engine_spec=Path(__file__).resolve().parent.parent/'pyproject.toml'
    if engine_spec.is_file():shutil.copy2(engine_spec,staging/'project/vendor/pyproject.toml')
    write(staging/'qa/bundled-engine.json',{'engine_version':p.profile['engine_version'],'files':engine_manifest})
    if p.profile.get('design_profile')=='m10-editorial-remaster-v1.1':
        for name in ['visual','remaster-boundaries','remaster-assets','quiz-divider-negative','early-candidate-review-final-freeze']:
            src=p.qa/name
            if not src.is_dir():raise RuntimeError('Missing full-remaster QA directory: '+name)
            copy_remaster_qa(src,staging/'qa'/name,ignore)
        for name in ['all-text-geometry','cross-scene-seek','quiz-runtime']:
            if (p.qa/name).is_dir():shutil.copytree(p.qa/name,staging/'qa'/name,ignore=ignore)
        for f in p.qa.glob('*.json'):
            if export_qa(f) or f.name in {'audio-policy-v1.1.json','historical-preservation.json','alignment-summary.json','migration.json'}:shutil.copy2(f,staging/'qa'/f.name)
        write(staging/'qa/archive-exclusions.json',{'excluded':['qa/remaster-boundaries/hosts/'],'reason':'Reproducible HyperFrames boundary host projects link to the project media tree. The boundary harness regenerates them; report.json and all captured evidence remain included.','regenerator':'project/vendor/ceh_video/visual/remaster-boundaries.mjs'})
        write(staging/'project/provenance/audio-restore.json',audio_restore_manifest(p))
        write(staging/'qa/raw-media-hashes.json',{str(f.relative_to(p.root)):sha(f) for f in sorted((p.root/'assets').rglob('*')) if f.is_file()})
    shutil.copytree(p.qa/'audio-audition',staging/'qa/audio-audition')
    if (p.qa/'recognition').is_dir():shutil.copytree(p.qa/'recognition',staging/'qa/recognition')
    elif p.profile.get('design_profile')!='m10-editorial-remaster-v1.1':raise RuntimeError('Missing recognition evidence')
    for ch in p.chapters:shutil.copytree(p.qa/(ch+'-states'),staging/'qa'/(ch+'-states'),ignore=shutil.ignore_patterns('*.html'))
    bundle_encoded_evidence(p,staging)
    files=[f for f in sorted(staging.rglob('*')) if f.is_file()];manifest={str(f.relative_to(staging)):sha(f) for f in files}
    write(staging/'FILES_SHA256.json',manifest)
    files=[f for f in sorted(staging.rglob('*')) if f.is_file()]
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=1,allowZip64=True) as z:
        for i,f in enumerate(files,1):
            z.write(f,'engine_project_source/'+str(f.relative_to(staging)))
            if i%500==0 or i==len(files):emit({'phase':'package_entries','completed':i,'total':len(files)})
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        with tempfile.TemporaryDirectory(dir=p.qa,prefix='verify-package-') as temp:
            z.extractall(temp);base=Path(temp)/'engine_project_source'
            for name,h in manifest.items():assert sha(base/name)==h,name
            picture_receipt=verify_encoded_evidence(base)
            golden_receipt=None
            if p.profile.get('design_profile')=='m10-editorial-remaster-v1.1':
                golden_receipt=verify_golden_review_evidence(base)
                import os,subprocess,sys
                env=os.environ.copy();env['PYTHONPATH']=str(base/'project/vendor');env['CEH_VIDEO_PROJECT']=str(base/'project')
                code='from ceh_video.common import Project, project_root; from ceh_video.delivery import restore_packaged_audio_cache; import json; print(json.dumps(restore_packaged_audio_cache(Project(project_root()))))'
                restored=json.loads(subprocess.check_output([sys.executable,'-c',code],cwd=base,env=env,text=True))
                assert restored['clips']==781 and restored['new_inferences']==restored['tempo_passes']==0
                write(p.qa/'engine-extracted-reconstruction.json',restored)
    receipt={'status':'crc_extraction_hashes_verified','files':len(files),'payload_hashes':len(manifest),'bytes':archive.stat().st_size,'sha256':sha(archive),'archive':archive.name,'encoded_picture_evidence':picture_receipt,'golden_review_evidence':golden_receipt,'human_listening':'pending'}
    write(p.qa/'engine-packaging.json',receipt);return receipt
