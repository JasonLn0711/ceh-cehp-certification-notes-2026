"""Artifact-bound agent review and persistent audio listening dispositions."""
from pathlib import Path
import html, re, time
from .common import digest, read, sha, write

DISPOSITIONS = {'pending_listening', 'confirmed_technical_defect', 'confirmed_listening_defect', 'reviewed_no_defect'}

def capture_manifest(project, chapter):
    folder = project.qa/(chapter+'-states')
    manifest=read(folder/'manifest.json')
    if manifest['capture_recipe']!=sha(Path(__file__).parent/'capture.mjs'):
        raise RuntimeError('Stale capture recipe: '+chapter)
    files=[folder/r['file'] for r in manifest['rows']]
    if len(set(files))!=len(files) or any(not f.is_file() or sha(f)!=r['sha256'] for f,r in zip(files,manifest['rows'])):
        raise RuntimeError('Stale capture image: '+chapter)
    if not files: raise RuntimeError('Capture teaching states before review: '+chapter)
    return {'source_sha256': project.chapter_inputs(chapter), 'captures': {f.name: sha(f) for f in files},
            'capture_recipe': sha(Path(__file__).parent/'capture.mjs'), 'renderer': project.profile['runtime']}

def record(project, chapter, findings, reviewer='agent'):
    if reviewer not in {'agent', 'human'}: raise ValueError('reviewer must be agent or human')
    if not findings.strip(): raise ValueError('Concrete inspected-frame findings required')
    row = {**capture_manifest(project, chapter), 'decision': 'pass', 'reviewer_type': reviewer,
           'findings': findings, 'recorded_at': time.time(), 'scope': 'Captured native visual states; full human watching/listening separate'}
    write(project.qa/(chapter+'-review.json'), row)
    return row

def require_review(project, chapter):
    row = read(project.qa/(chapter+'-review.json'))
    current = capture_manifest(project, chapter)
    if row['decision'] != 'pass' or any(row.get(k) != v for k,v in current.items()):
        raise RuntimeError('Stale or unresolved visual review: '+chapter)
    return row


def encoded_manifest(project):
    movie=project.output/project.profile['master_filename']
    audit=read(project.qa/'rendered-artifact-audit.json');late=read(project.qa/'late-diagram-samples.json')
    rows=[*audit['sampled_frames'],*late['samples']]
    return {'master_sha256':sha(movie),'captures':{r['file']:sha(project.output/'inspection_frames'/r['file']) for r in rows},'renderer':project.profile['runtime']}


def record_encoded(project,findings):
    if not findings.strip():raise ValueError('Concrete encoded-frame findings required')
    row={**encoded_manifest(project),'decision':'pass','reviewer_type':'agent','findings':findings,'scope':'Sampled encoded picture; full human listening/viewing separate'}
    write(project.qa/'encoded-review.json',row);return row


def require_encoded(project):
    row=read(project.qa/'encoded-review.json')
    if row['decision']!='pass' or any(row.get(k)!=v for k,v in encoded_manifest(project).items()):raise RuntimeError('Stale encoded visual review')
    return row

def audio_queue(project):
    if project.profile.get('schema_version') == 2:
        from .mandarin_delivery import audio_review
        return {k:v for k,v in audio_review(project,lambda row:None).items() if k!='items'}
    diagnostics = read(project.qa/'audio-review-diagnostics.json'); flags = {}
    for item in diagnostics['alignment_flags']: flags.setdefault(item['file'], []).append(item)
    policy = read(project.root/'pronunciation.json'); terms = set(policy['spell']) | set(policy['pronunciations'])
    decision_file = project.qa/'audio-review-decisions.json'
    prior = read(decision_file)['items'] if decision_file.exists() else {}
    items = []; total = 0; technical = []
    import numpy as np
    import soundfile as sf
    for scene in project.scenes:
        sid = scene['id']; a = project.audio(sid); spoken = [r for r in a['segments'] if r['kind']=='spoken']
        for i, segment in enumerate(spoken):
            total += 1; path = project.root/segment['path']; actual = sha(path)
            reasons = []; f = flags.get(f'{sid}-{segment["sentence"]:03}.json', [])
            if f: reasons.append('alignment')
            text = segment['canonical']; tokens = re.findall(r'\b[A-Za-z][A-Za-z0-9-]*\b', text)
            if set(tokens) & terms: reasons.append('technical_term')
            if re.search(r'\d|\b(?:one|two|three|four|five|six|seven|eight|nine|ten|hundred|thousand|million|percent|seconds?|bytes?|cores?)\b', text, re.I): reasons.append('quantity_or_unit')
            if re.search(r'\b(?:not|no|never|without|cannot|only|unknown|unvalidated)\b', text, re.I): reasons.append('claim_boundary')
            if sid in project.quiz_scenes(): reasons.append('quiz_content')
            pcm, sr = sf.read(path, dtype='int16', always_2d=True)
            defects = []
            if actual != segment['sha256']: defects.append('audio_hash_mismatch')
            if sr != 48000 or pcm.shape[1] != 2 or len(pcm) != segment['end_sample']-segment['start_sample']: defects.append('sample_contract_mismatch')
            if not np.any(pcm): defects.append('all_zero_spoken_clip')
            if np.max(np.abs(pcm.astype(np.int32))) >= 32767: defects.append('saturated_sample')
            if defects: technical.append({'scene':sid,'sentence':segment['sentence'],'defects':defects}); reasons.append('technical_defect')
            if not reasons: continue
            ident = digest({'scene':sid,'canonical':text,'audio':actual})
            old = prior.get(ident, {}); disposition = old.get('disposition','pending_listening')
            if defects: disposition = 'confirmed_technical_defect'
            row = {'id':ident,'scene':sid,'sentence':segment['sentence'],'canonical':text,'spoken':segment['spoken'],
                   'path':segment['path'],'audio_sha256':actual,'reasons':reasons,'alignment_flags':f,'technical_defects':defects,
                   'before':spoken[i-1]['canonical'] if i else '', 'after':spoken[i+1]['canonical'] if i+1<len(spoken) else '',
                   'disposition':disposition,'reviewer_type':old.get('reviewer_type','automated_technical' if defects else 'unassigned'),
                   'evidence':old.get('evidence','PCM/recipe diagnostics; listening judgment pending')}
            items.append(row)
    items.sort(key=lambda r: (-int(bool(r['technical_defects'])), -int('quiz_content' in r['reasons']), -int('alignment' in r['reasons']), r['scene'],r['sentence']))
    write(decision_file, {'items':{r['id']:{k:r[k] for k in ['disposition','reviewer_type','evidence']} for r in items}, 'human_acceptance':'pending'})
    out = project.qa/'audio-audition'; out.mkdir(exist_ok=True)
    sections = []
    for row in items:
        sections.append('<article><h2>'+html.escape(f'{row["scene"]} / {row["sentence"]:03} · {row["disposition"]}')+'</h2><p>'+html.escape(row['canonical'])+'</p><p>Spoken: '+html.escape(row['spoken'])+'</p><audio controls preload="none" src="../../project/'+html.escape(row['path'],quote=True)+'"></audio><details><summary>Context and review leads</summary><p>'+html.escape(row['before'])+'</p><p>'+html.escape(row['after'])+'</p><pre>'+html.escape(str(row['reasons'])+' '+str(row['alignment_flags']))+'</pre><code>'+row['id']+'</code></details></article>')
    (out/'index.html').write_text('<!doctype html><html lang="en-US"><meta charset="utf-8"><title>CEH prioritized audio review</title><style>body{font:20px/1.5 sans-serif;max-width:1050px;margin:40px auto;background:#F0EBE4;color:#292421}article{padding:20px 0;border-bottom:1px solid #B8B0A9}audio{width:100%}pre{white-space:pre-wrap}</style><h1>Prioritized audio review</h1><p>Automated findings locate review leads. Human pronunciation and naturalness acceptance remain pending.</p>'+''.join(sections))
    result = {'status':'technical_triage_complete' if not technical else 'technical_defects_found','spoken_clips_checked':total,
              'alignment_flags':len(diagnostics['alignment_flags']),'flagged_clips':len(flags),'queued_clips':len(items),
              'technical_defects':technical,'human_acceptance':'pending','items':items}
    write(out/'manifest.json', result); return {k:v for k,v in result.items() if k!='items'}

def audio_decision(project, ident, disposition, reviewer, evidence):
    if disposition not in DISPOSITIONS: raise ValueError('Invalid disposition')
    if reviewer not in {'human','automated_technical'}: raise ValueError('Listening decisions require reviewer_type=human')
    if disposition in {'confirmed_listening_defect','reviewed_no_defect'} and reviewer!='human': raise ValueError('Human listening evidence required')
    if not evidence.strip(): raise ValueError('Evidence required')
    d=read(project.qa/'audio-review-decisions.json')
    if ident not in d['items']: raise ValueError('Unknown audio review item')
    d['items'][ident]={'disposition':disposition,'reviewer_type':reviewer,'evidence':evidence};write(project.qa/'audio-review-decisions.json',d)
