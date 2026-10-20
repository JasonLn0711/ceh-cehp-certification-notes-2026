from ceh_video.audio_policy import modern
"""Fail-closed render guard for new English scenes; no inherited exceptions."""
from pathlib import Path
from .common import read,sha


def require_visual(p,scene_ids):
    if p.profile.get('design_profile')=='m10-editorial-remaster-v1.1':
        return require_remaster_visual(p,scene_ids)
    if not modern(p.profile):return
    manifest=p.qa/'visual/scenes/manifest.json'
    if not manifest.exists():raise RuntimeError('New scenes require geometry and reviewed screenshot regression: '+str(manifest))
    report=read(manifest)
    if report['status']!='passed' or report['failures'] or report['exceptions']:
        raise RuntimeError('New-scene visual gate failed; legacy exceptions cannot be inherited')
    visual=Path(__file__).parent/'visual'
    if report.get('geometrySha256')!=sha(visual/'geometry.mjs'):raise RuntimeError('Stale geometry implementation evidence')
    if report.get('qaScriptSha256')!=sha(visual/'qa.mjs') or report.get('environment',{}).get('tokens')!=sha(visual/'tokens.v1.1.json'):
        raise RuntimeError('Stale visual harness or token evidence')
    if report.get('environment',{}).get('lock')!=sha(visual/'package-lock.json'):raise RuntimeError('Dependency lock changed since visual QA')
    runtime=p.profile.get('runtime',{}).get('hyperframes')
    if runtime and (report['environment'].get('hyperframes')!=runtime or read(p.root/'node_modules/hyperframes/package.json')['version']!=runtime):raise RuntimeError('HyperFrames dependency mismatch')
    for rel,expected in p.profile.get('locked_assets',{}).items():
        if sha(p.root/rel)!=expected:raise RuntimeError('Protected asset changed: '+rel)
    bounds_file=p.qa/'all-text-geometry/report.json'
    if not bounds_file.exists():raise RuntimeError('Missing exhaustive text geometry evidence')
    bounds=read(bounds_file)
    if bounds.get('geometrySha256')!=sha(visual/'geometry.mjs'):raise RuntimeError('Stale bounds geometry implementation')
    if bounds.get('validatorSha256')!=sha(visual/'all-text-geometry.mjs') or bounds.get('tokensSha256')!=sha(visual/'tokens.v1.1.json'):raise RuntimeError('Stale bounds validator evidence')
    if bounds['status']!='passed':raise RuntimeError('Text geometry failed')
    for sid in scene_ids:
        matching=[r for r in bounds['rows'] if r['scene']==sid and not r['errors'] and not r['exceptions'] and r['source_sha256']==sha(p.root/'compositions'/f'{sid}.html')]
        if not matching:raise RuntimeError('Missing or stale exhaustive text bounds: '+sid)
        if report.get('audioSources',{}).get(sid)!=sha(p.root/'data'/f'{sid}.audio.json'):
            raise RuntimeError('Missing or stale audio timing evidence: '+sid)
        if report.get('sources',{}).get(sid)!=sha(p.root/'compositions'/f'{sid}.html'):
            raise RuntimeError('Missing or stale visual evidence: '+sid)
        if not any(row['name'].startswith(sid+'-') and row['golden_pixels']==0 and row['seek_pixels']==0 for row in report['rows']):
            raise RuntimeError('Missing screenshot and seek evidence: '+sid)


def required_frames(audio,cues):
    """Independently reproduce the QA capture contract (JS Math.round semantics)."""
    import math
    samples=audio['samples']
    if not isinstance(samples,int) or samples<=0 or samples%1600:
        raise RuntimeError('Non-integral video frame duration')
    length=samples//1600
    def clamp(n):return max(0,min(length-1,math.floor(n+.5)))
    frames={0,clamp(length*.15),clamp(length*.5),clamp(length*.85),length-1}
    for cue in cues:
        if not all(math.isfinite(cue[k]) for k in ('start','end')) or cue['end']<=cue['start']:
            raise RuntimeError('Invalid label cue window')
        frames.add(clamp((cue['start']+cue['end'])*15))
    for hold in (r for r in audio['segments'] if r['kind']=='silence'):
        start,end=hold['start_sample'],hold['end_sample']
        if start%1600 or end%1600 or end-start!=48000:raise RuntimeError('Invalid quiz frame interval')
        start//=1600;end//=1600
        frames.update(clamp(n) for n in (start-1,start,start+1,start+7,start+15,start+22,end-1,end,end+1))
    return sorted(frames)


def _checked_rows(report,expected):
    if report.get('status')!='passed' or report.get('failures')!=[] or report.get('exceptions')!=[]:
        raise RuntimeError('Remaster visual gate failed; exceptions cannot be inherited')
    if report.get('requiredStates')!=expected:raise RuntimeError('Incomplete required-state coverage')
    rows=report.get('rows',[])
    if len(rows)!=len(expected) or {r.get('name') for r in rows}!=set(expected):
        raise RuntimeError('Missing or duplicate screenshot states')
    for row in rows:
        if row.get('frame')!=expected[row['name']] or row.get('golden_pixels')!=0 or row.get('seek_pixels')!=0 or row.get('exceptions')!=[]:
            raise RuntimeError('Unverified screenshot state: '+row['name'])
        if row.get('seek_comparisons')!={'forward':0,'reverse':0,'repeated':0}:
            raise RuntimeError('Incomplete deterministic seek evidence: '+row['name'])
    return rows


def _hash_matches(path,expected,label):
    if not path.is_file() or expected!=sha(path):raise RuntimeError('Missing or stale '+label+': '+str(path))


def require_remaster_visual(p,scene_ids):
    visual=Path(__file__).parent/'visual'
    folder=p.qa/'visual/scenes';report=read(folder/'manifest.json')
    token_path=p.root/p.profile['token_manifest'];tokens=read(token_path)
    for field,path in {
        'qaScriptSha256':visual/'remaster-qa.mjs',
        'geometrySha256':visual/'remaster-geometry.mjs',
        'textGeometrySha256':visual/'geometry.mjs',
        'runtimeSha256':visual/'remaster-runtime.js',
        'hyperframesRuntimeSha256':p.root/'node_modules/hyperframes/dist/hyperframe-runtime.js',
        'gsapSha256':p.root/'assets/vendor/gsap.min.js',
        'browserExecutableSha256':Path(p.profile['runtime']['browser']),
    }.items():_hash_matches(path,report.get(field),field)
    environment=report.get('environment',{})
    _hash_matches(token_path,environment.get('tokens'),'design tokens')
    _hash_matches(visual/'package-lock.json',environment.get('lock'),'QA dependency lock')
    runtime=p.profile['runtime']['hyperframes']
    if environment.get('hyperframes')!=runtime or read(p.root/'node_modules/hyperframes/package.json')['version']!=runtime:
        raise RuntimeError('HyperFrames version mismatch')
    if environment.get('viewport')!=[1920,1080] or environment.get('dpr')!=1 or environment.get('seed')!=0 or environment.get('gsap')!='3.14.2' or environment.get('playwright')!='1.62.1':
        raise RuntimeError('Unpinned visual environment')
    if environment.get('fontHashes')!=tokens['fontHashes']:raise RuntimeError('Font manifest mismatch')
    for rel,expected in {**p.profile.get('locked_assets',{}),**tokens['fontHashes']}.items():
        _hash_matches(p.root/rel,expected,'protected asset')
    ids={s['id'] for s in p.scenes};quiz={q['scene_id'] for q in p.questions}
    if len(ids)!=58 or len(quiz)!=8 or not set(scene_ids)<=ids:raise RuntimeError('Invalid M10 scene inventory')
    expected={};holds=set();frame_counts={}
    for sid in sorted(ids):
        audio_file=p.root/'data'/f'{sid}.audio.json';audio=read(audio_file)
        cue_file=p.root/'data'/f'{sid}.label-cues.json';cues=read(cue_file) if cue_file.exists() else []
        for field,path in [('sources',p.root/'compositions'/f'{sid}.html'),('audioSources',audio_file)]:
            _hash_matches(path,report.get(field,{}).get(sid),field)
        if cue_file.exists():_hash_matches(cue_file,report.get('cueSources',{}).get(sid),'label cues')
        elif report.get('cueSources',{}).get(sid) is not None:raise RuntimeError('Unexpected label cues: '+sid)
        _hash_matches(p.root/'data'/f'{sid}.layout.json',report.get('layoutSources',{}).get(sid),'scene layout')
        _hash_matches(p.root/'data'/f'{sid}.scene-spec.json',report.get('sceneSpecSources',{}).get(sid),'scene specification')
        frame_counts[sid]=audio['samples']//1600
        for frame in required_frames(audio,cues):expected[f'{sid}-f{frame:06}']=frame
        silences=[r for r in audio['segments'] if r['kind']=='silence']
        if len(silences)!=(1 if sid in quiz else 0):raise RuntimeError('Unexpected quiz hold count: '+sid)
        for hold in silences:holds.update((sid,f) for f in range(hold['start_sample']//1600,hold['end_sample']//1600))
    rows=_checked_rows(report,expected)
    audited=report.get('allFrames',[])
    if len(audited)!=50 or {r.get('scene') for r in audited}!=ids-quiz or any(r.get('errors')!=[] or r.get('frames')!=frame_counts[r['scene']] for r in audited):
        raise RuntimeError('Incomplete all-frame geometry coverage')
    checked=report.get('holdChecks',[])
    if len(checked)!=240 or len(holds)!=240 or {(r.get('scene'),r.get('frame')) for r in checked}!=holds or any(r.get('answers')!=[] or r.get('captions')!=[] for r in checked):
        raise RuntimeError('Incomplete or nonempty quiz-hold evidence')
    text=report.get('textLayouts',[])
    if len(text)!=58 or {r.get('scene') for r in text}!=ids or any(not r.get('objects') for r in text):
        raise RuntimeError('Incomplete text-layout evidence')
    golden=folder/'golden';baseline=read(golden/'manifest.json')
    if not baseline.get('review') or baseline.get('environment')!=environment or baseline.get('requiredStates')!=expected:
        raise RuntimeError('Missing reviewed matching golden baseline')
    golden_rows=baseline.get('rows',[])
    if len(golden_rows)!=len(rows):raise RuntimeError('Incomplete golden baseline')
    indexed={r['name']:r for r in golden_rows}
    if set(indexed)!=set(expected):raise RuntimeError('Golden state inventory mismatch')
    for row in rows:
        reference=indexed[row['name']]
        filename=row['name']+'.png'
        if row.get('file')!=filename or reference.get('file')!=filename:raise RuntimeError('Invalid screenshot artifact path')
        _hash_matches(folder/filename,row.get('sha256'),'captured screenshot')
        _hash_matches(golden/filename,reference.get('sha256'),'reviewed screenshot')
    if p.profile.get('audio_policy')=='ceh-en-v1.2':
        from .delivery import verify_golden_review_evidence
        verify_golden_review_evidence(p.root.parent)
    boundary_folder=p.qa/'remaster-boundaries';boundary=read(boundary_folder/'report.json')
    if boundary.get('status')!='passed' or boundary.get('errors')!=[]:raise RuntimeError('Nested boundary QA failed')
    _hash_matches(visual/'remaster-boundaries.mjs',boundary.get('script_sha256'),'boundary harness')
    _hash_matches(visual/'package-lock.json',boundary.get('lock_sha256'),'boundary dependency lock')
    ordered=[s['id'] for s in p.scenes]
    expected_boundaries={(f'{a}->{b}',d) for a,b in zip(ordered,ordered[1:]) for d in (-1,0,1)}
    states=boundary.get('rows',[])
    if len(states)!=171 or {(r.get('boundary'),r.get('offsetFrames')) for r in states}!=expected_boundaries:
        raise RuntimeError('Incomplete 171-state boundary evidence')
    for row in states:
        if row.get('status')!='passed' or row.get('pixels')!=0 or len(row.get('comparisons',[]))!=3 or {c.get('mode') for c in row['comparisons']}!={'forward','reverse','repeated'} or any(c.get('pixels')!=0 for c in row['comparisons']):
            raise RuntimeError('Unverified boundary seek')
        if Path(row.get('screenshot','')).name!=row.get('screenshot'):raise RuntimeError('Invalid boundary screenshot path')
        _hash_matches(boundary_folder/row['screenshot'],row.get('sha256'),'boundary screenshot')
    if not boundary.get('sources'):raise RuntimeError('Missing boundary source identities')
    for rel,expected_hash in boundary['sources'].items():_hash_matches((p.root/rel).resolve(),expected_hash,'boundary source')

    assets=read(p.qa/'remaster-assets/report.json')
    if assets.get('status')!='passed' or assets.get('errors')!=[]:raise RuntimeError('Asset geometry QA failed')
    for field,path in {'scriptSha256':visual/'remaster-assets.mjs','tokensSha256':token_path,
            'runtimeSha256':visual/'remaster-runtime.js',
            'hyperframesRuntimeSha256':p.root/'node_modules/hyperframes/dist/hyperframe-runtime.js',
            'gsapSha256':p.root/'assets/vendor/gsap.min.js',
            'browserExecutableSha256':Path(p.profile['runtime']['browser'])}.items():_hash_matches(path,assets.get(field),'asset '+field)
    if set(assets.get('sources',{}))!=ids:raise RuntimeError('Incomplete asset source coverage')
    for sid,expected_hash in assets['sources'].items():_hash_matches(p.root/'compositions'/f'{sid}.html',expected_hash,'asset scene')
    asset_rows=assets.get('rows',[])
    if {r.get('scene') for r in asset_rows}!=ids-quiz or any(r.get('errors')!=[] or not r.get('assets') for r in asset_rows):raise RuntimeError('Incomplete or failed 50-scene asset geometry')
    if not assets.get('assets'):raise RuntimeError('Missing locked asset identities')
    for rel,expected_hash in assets['assets'].items():_hash_matches(p.root/rel,expected_hash,'asset identity')
