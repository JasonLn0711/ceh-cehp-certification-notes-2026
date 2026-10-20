"""Audio diagnostics are independent of archive construction."""
from .common import read, write, sha

def require_minimum_asr(p):
    """One actual fixed-runtime inference proves availability only."""
    receipt=read(p.qa/'asr-availability-minimum.json');transcript=read(p.qa/'recognition/availability-S01-001.json')
    assert receipt['mode']=='availability_validation' and receipt['execution_status']=='LIVE_MINIMUM_COMPLETED'
    assert receipt['runtime_validity']=='valid_target_runtime' and receipt['new_inferences']==1
    assert receipt['accuracy']==receipt['latency']=='not_evaluated' and receipt['full_film_transcription']=='not_executed'
    assert receipt['transcript_sha256']==sha(p.qa/'recognition/availability-S01-001.json')
    assert receipt['input_sha256']==transcript['audio_sha256']==sha(p.root/transcript['input'])
    assert transcript['recognized'].strip() and transcript['segments']
    assert all(r['end']>r['start']>=0 and r['text'].strip() for r in transcript['segments'])
    assert receipt['runtime']['model']=='base.en' and receipt['runtime']['device']=='cpu' and receipt['runtime']['compute_type']=='int8'
    assert receipt['runtime']['canonical_prompt'] is False and receipt['runtime']['vad_filter'] is False
    assert receipt['models']=={f.name:sha(f) for f in sorted((p.root/'models/faster-whisper-base.en').iterdir()) if f.is_file()}
    return receipt


def remaster_audio_review(p):
    from .review import audio_queue
    require_minimum_asr(p)
    flags=[];sources={}
    for f in sorted((p.root/'data/forced-alignment').glob('*.json')):
        d=read(f);sources[f.name]=sha(f)
        for flag in d['review_flags']:flags.append({'file':f.name,'canonical':d['canonical'],'word_text':d['words'][flag['word']]['text'],**flag})
    write(p.qa/'audio-review-diagnostics.json',{'status':'alignment_diagnostics_only','scope':'Forced-alignment review leads; independent one-clip availability has a separate receipt','alignment_flags':flags,'alignment_sources':sources,'human_listening':'pending'})
    result=audio_queue(p);assert not result['technical_defects'],result
    write(p.qa/'audio-technical-triage.json',result)
    return result

