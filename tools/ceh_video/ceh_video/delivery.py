"""Validate actual outputs and close a self-contained, extracted/hash-checked archive."""
from pathlib import Path
import csv, json, math, re, shutil, tempfile, zipfile
from .common import read, sha, write
from .review import require_review,require_encoded


def export_qa(path):
    """Ship production evidence; keep unrelated Git/Planning custody notes local."""
    return path.suffix in {'.json','.jsonl','.md'} and bool(re.match(
        r'^(?:C\d+-(?:check|checked-fingerprint|render|timing|review)|audio-|asr-|recognition-|reference-|live-|clean-|production-|resume-|baseline-|late-|encoded-|quiz-|scene-seek-|rendered-|master-|engine-|run-|preflight\.|document-links\.)',path.name))


def validate(p):
    import numpy as np
    import soundfile as sf
    source=(p.root/p.profile['source_package']).resolve();source_hashes=0
    for line in (source/'FILES_SHA256.txt').read_text().splitlines():
        if not line or line.startswith('#'):continue
        h,name=line.split(None,1);assert sha(source/name.lstrip('* '))==h;source_hashes+=1
    assert read(source/'scenes.json')==read(p.root/'data/scenes.json'),'Release canonical content changed; use a separate authored release'
    clips=0;words=0;holds=[];duration=0;captions=[]
    for s in p.scenes:
        sid=s['id'];a=p.audio(sid);pcm,sr=sf.read(p.root/'assets/voice'/f'{sid}.wav',dtype='int16',always_2d=True)
        assert sr==48000 and pcm.shape==(a['samples'],2) and len(pcm)%1600==0
        text=' '.join(r['canonical'] for r in a['segments'] if r['kind']=='spoken')
        assert text==' '.join(s['narration_en_US'].split());words+=len(text.split())
        caps=read(p.root/'data'/f'{sid}.captions.json');assert ' '.join(c['text'] for c in caps)==text
        for row in a['segments']:
            if row['kind']=='spoken':
                f=p.root/row['path'];meta=read(f.with_suffix('.json'));assert sha(f)==row['sha256']
                assert meta['baseline_speed']==.73 and meta['atempo']==1.5 and meta['speed_applications']==1
                alignment=read(p.root/'data/forced-alignment'/f'{sid}-{row["sentence"]:03}.json');assert alignment['audio_sha256']==row['sha256'];clips+=1
            else:
                zero=pcm[row['start_sample']:row['end_sample']];assert zero.shape==(48000,2) and not np.any(zero)
                for c in caps:assert c['end']<=row['start_sample']/48000+1e-5 or c['start']>=row['end_sample']/48000-1e-5
                holds.append(sid)
        for c in caps:
            assert 0<=c['start']<c['end']<=a['duration'];captions.append({**c,'start':c['start']+duration,'end':c['end']+duration})
        duration+=a['duration']
    assert words==p.profile['expected']['canonical_words'] and len(holds)==len(p.questions)
    assert all(a['end']<=b['start']+.001 for a,b in zip(captions,captions[1:]))
    for ch in p.chapters:
        require_review(p,ch);check=read(p.qa/f'{ch}-check.json');r=read(p.qa/f'{ch}-render.json')
        assert check['ok'] and not check['browserSkipped'];assert r['status']=='rendered_codec_verified'
        assert r['source_sha256']==p.chapter_inputs(ch) and sha(p.output/'chapters'/f'{ch}.mp4')==r['output_sha256']
    require_encoded(p)
    probe=read(p.qa/'master-ffprobe.json');v=next(s for s in probe['streams'] if s['codec_type']=='video');a=next(s for s in probe['streams'] if s['codec_type']=='audio')
    assert (v['codec_name'],v['width'],v['height'],v['r_frame_rate'],a['codec_name'],a['sample_rate'],a['channels'])==('h264',1920,1080,'30/1','aac','48000',2)
    assert int(v['nb_read_frames'])==round(duration*30) and len(probe['chapters'])==len(p.chapters)
    artifact=read(p.qa/'rendered-artifact-audit.json');assert artifact['decoded_entire_master'] and artifact['black_intervals']==0
    assert read(p.qa/'audio-continuity-audit.json')['status']=='passed'
    quiz=read(p.qa/'quiz-runtime/checks.json');assert quiz['status']=='passed' and quiz['checks']==8*len(p.questions)
    seek=read(p.qa/'scene-seek-audit.json');assert seek['status']=='passed' and seek['comparisons']==3*len(p.scenes)
    result={'status':'automated_delivery_checks_passed','module':p.profile['module'],'engine_version':p.profile['engine_version'],'runtime':p.profile['runtime'],'source_hashes':source_hashes,'canonical_words':words,'clips':clips,'scenes':len(p.scenes),'chapters':len(p.chapters),'captions':len(captions),'duration':duration,'frames':round(duration*30),'zero_pcm_holds':len(holds),'pcm_frames_per_hold':48000,'master_sha256':sha(p.output/p.profile['master_filename']),'encoded_samples':len(artifact['sampled_frames'])+read(p.qa/'late-diagram-samples.json')['count'],'human_listening':'pending','pronunciation_accuracy':'not_evaluated','public_media_release':'not_activated'}
    write(p.qa/'engine-delivery.json',result)
    (p.output/'engine-render-report.md').write_text(f'''# {p.profile['title']} — optimized production engine

Actual complete film: {duration:.6f} seconds, {round(duration*30):,} frames, {len(p.scenes)} scenes, {len(p.chapters)} chapters, {words:,} canonical words and {len(captions):,} subtitle cues. Engine {p.profile['engine_version']}; HyperFrames {p.profile['runtime']['hyperframes']}.

The approved editorial, voice and silence policies remain intact. All {clips} speech clips have verified recipes. Each of {len(holds)} quiz holds contains exactly 48,000 stereo zero PCM frames. Decoded lossy AAC residue is recorded separately. Full decode, scene seeks, quiz boundaries, chapter/master fingerprints, artifact-bound sampled visual review and PCM/AAC continuity passed.

Source package and M10 v1.0 remain immutable. New implementation, runtime and output identities have separate receipts. Human pronunciation, naturalness and full-film listening acceptance remain pending; the prioritized queue records unresolved review leads. Independent ASR receipts establish availability; accuracy and latency remain not_evaluated.

Start with project/ENGINE_EDITING.md in the editable archive. Production profile, pronunciation policy, bundled engine, models, fonts, native diagrams and regeneration inputs are included. Environments, node_modules and caches are excluded. Final media are adjacent to the ZIP. See qa/engine-delivery.json, reference-import.json, native chapter review receipts, encoded-review.json and integration evidence for the exercised layers.

Master SHA-256: {result['master_sha256']}.
''')
    return result


def package(p,emit):
    d=read(p.qa/'engine-delivery.json');assert d['status']=='automated_delivery_checks_passed';require_encoded(p)
    archive=p.output/p.profile['editable_filename'];staging=p.output/'engine_project_source'
    if staging.exists():raise RuntimeError('Reconcile existing closed package before replacing '+str(staging))
    def ignore(folder,names):return [n for n in names if n in {'.venv','node_modules','.production','.hyperframes','.waveform-cache','__pycache__','review','.git'} or n.endswith('.tmp')]
    staging.mkdir();shutil.copytree(p.root,staging/'project',ignore=ignore);shutil.copytree(p.root.parent/'inputs',staging/'inputs');(staging/'qa').mkdir()
    for f in p.qa.iterdir():
        if f.is_file() and export_qa(f):shutil.copy2(f,staging/'qa'/f.name)
    shutil.copytree(p.qa/'audio-audition',staging/'qa/audio-audition')
    shutil.copytree(p.qa/'recognition',staging/'qa/recognition')
    for ch in p.chapters:shutil.copytree(p.qa/(ch+'-states'),staging/'qa'/(ch+'-states'),ignore=shutil.ignore_patterns('*.html'))
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
    receipt={'status':'crc_extraction_hashes_verified','files':len(files),'payload_hashes':len(manifest),'bytes':archive.stat().st_size,'sha256':sha(archive),'archive':archive.name,'human_listening':'pending'}
    write(p.qa/'engine-packaging.json',receipt);return receipt
