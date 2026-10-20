from ceh_video.audio_policy import modern
"""Sentence-content cache and sample-exact speech reconstruction."""
from pathlib import Path
import json, os, re, shutil, subprocess
from .common import digest, read, sha, write
from .audio_policy import timing


def spoken(text, policy):
    spell=set(policy['spell']); pronunciations=policy['pronunciations']
    def token(m):
        word=m.group(0)
        return ' '.join('A,' if c=='A' else c for c in word) if word in spell else pronunciations.get(word,word)
    return re.sub(r'\b[A-Za-z][A-Za-z0-9-]*\b',token,text)


def sentences(text):
    out=[];prefix=''
    for part in re.split(r'(?<=[.!?])\s+(?=[A-Z“\"])',text):
        if re.fullmatch('[A-D][.]',part):prefix=part+' ';continue
        out.append(prefix+part);prefix=''
    if prefix:out.append(prefix.strip())
    assert ' '.join(out)==' '.join(text.split())
    return out


def recipe(p,text):
    policy=read(p.root/'pronunciation.json')
    result={'canonical':text,'spoken':spoken(text,policy),'voice':p.profile['voice'],'models':p.profile['models'],
            'processing':{'sample_rate':48000,'channels':2,'subtype':'PCM_16','gain_peak_ceiling':.94,'ffmpeg':p.profile['runtime']['ffmpeg']}}
    if modern(p.profile):
        result['baseline_recipe']=baseline_recipe(p,text)
        result['processing'].update(atempo=timing(p.profile)['atempo'],speed_applications=1)
    return result


def cache_entry(p,text):return p.state/'speech-cache'/digest(recipe(p,text))


def import_cache(p):
    count=0
    for s in p.scenes:
        for seg in p.audio(s['id'])['segments']:
            if seg['kind']!='spoken':continue
            f=p.root/seg['path'];raw=p.root/seg['baseline_path'];meta=read(f.with_suffix('.json'));r=recipe(p,seg['canonical'])
            assert sha(f)==seg['sha256']
            assert meta['text']==seg['canonical'] and meta['spoken']==r['spoken']
            assert meta['voice']==r['voice']['name'] and meta['baseline_speed']==r['voice']['baseline_speed']
            assert meta['atempo']==timing(p.profile)['atempo'] and meta['speed_applications']==1 and meta['models_sha256']==p.profile['models']
            d=cache_entry(p,seg['canonical']);d.mkdir(parents=True,exist_ok=True)
            shutil.copy2(f,d/'processed.wav');shutil.copy2(raw,d/'baseline.wav');shutil.copy2(f.with_suffix('.json'),d/'metadata.json')
            write(d/'receipt.json',{'recipe':r,'processed_sha256':sha(f),'baseline_sha256':sha(raw),'metadata_sha256':sha(d/'metadata.json'),'origin':'verified_legacy_recipe','baseline_seconds':meta['baseline_seconds']})
            count+=1
    return count


def valid_cache(p,text):
    d=cache_entry(p,text);f=d/'receipt.json'
    if not f.exists():return False
    try:
        r=read(f)
        if modern(p.profile) and (not valid_baseline(p,text) or sha(baseline_entry(p,text)/'baseline.wav')!=r['baseline_sha256']):return False
        return r['recipe']==recipe(p,text) and all((d/name).exists() and sha(d/name)==r[key] for name,key in [('processed.wav','processed_sha256'),('baseline.wav','baseline_sha256'),('metadata.json','metadata_sha256')])
    except (OSError,ValueError,KeyError,TypeError):
        return False


def synthesize(p,sid,emit=lambda x:None):
    import numpy as np
    import soundfile as sf
    scene=p.by_id[sid];policy=read(p.root/'pronunciation.json');model=None;timeline=[];chunks=[]
    contract=timing(p.profile);ledger=[];cursor=0;ordinal=0;generated=0;reused=0;reprocessed=0
    def silence(kind, frames):
        nonlocal cursor
        if frames:
            ledger.append(dict(kind=kind,start_sample=cursor,end_sample=cursor+frames))
            chunks.append(np.zeros((frames,2),dtype=np.int16));cursor+=frames
    silence('opening',contract['opening'])
    folder=p.root/'assets/voice'/sid;rawfolder=p.root/'assets/voice-baseline'/sid
    folder.mkdir(exist_ok=True,parents=True);rawfolder.mkdir(exist_ok=True,parents=True)
    for source_segment,segment in enumerate(scene['audio_segments']):
        if segment['kind']=='silence':
            if contract['id']!='ceh-en-v1.0':silence('frame_alignment',(-cursor)%1600)
            timeline.append({'kind':'silence','source_segment':source_segment,'start_sample':cursor,'end_sample':cursor+contract['quiz'],'seconds':1})
            silence('quiz',contract['quiz']);continue
        parts=sentences(segment['text'])
        for i,text in enumerate(parts):
            cache=cache_entry(p,text);cache.mkdir(parents=True,exist_ok=True);r=recipe(p,text)
            if not valid_cache(p,text):
                baseline=baseline_entry(p,text)
                if not valid_baseline(p,text):
                    if modern(p.profile) and p.profile.get('baseline_runtime')=='historical-runtime-unrecorded':
                        raise RuntimeError('Baseline missing or invalid; declare the actual synthesis runtime in a new profile before fresh inference')
                    from kokoro_onnx import Kokoro
                    if model is None:model=Kokoro(str(p.root/'models/kokoro-v1.0.onnx'),str(p.root/'models/voices-v1.0.bin'))
                    samples,rate=model.create(r['spoken'],voice=r['voice']['name'],speed=r['voice']['baseline_speed'],lang=r['voice']['language'])
                    assert rate==24000 and len(samples)
                    gain=min(1.,.94/max(float(np.max(np.abs(samples))),1e-9))
                    baseline.mkdir(parents=True,exist_ok=True)
                    sf.write(baseline/'baseline.wav',samples*gain,rate,subtype='PCM_16')
                    write(baseline/'receipt.json',dict(recipe=baseline_recipe(p,text),sha256=sha(baseline/'baseline.wav'),origin='actual_local_inference',gain=gain))
                    generated+=1
                else:reprocessed+=1
                shutil.copy2(baseline/'baseline.wav',cache/'baseline.wav')
                info=sf.info(cache/'baseline.wav')
                subprocess.run(['ffmpeg','-v','error','-nostdin','-y','-i',str(cache/'baseline.wav'),'-af',f"atempo={contract['atempo']}",'-ar','48000','-ac','2','-c:a','pcm_s16le',str(cache/'processed.tmp.wav')],check=True)
                os.replace(cache/'processed.tmp.wav',cache/'processed.wav')
                meta={'text':text,'spoken':r['spoken'],'voice':r['voice']['name'],'language':r['voice']['language'],'baseline_speed':r['voice']['baseline_speed'],'atempo':contract['atempo'],'speed_applications':1,'models_sha256':r['models'],'baseline_seconds':info.frames/info.samplerate,'recipe_sha256':digest(r),'baseline_provenance':read(baseline/'receipt.json'),'processing':r['processing']}
                write(cache/'metadata.json',meta)
                write(cache/'receipt.json',{'recipe':r,'processed_sha256':sha(cache/'processed.wav'),'baseline_sha256':sha(cache/'baseline.wav'),'metadata_sha256':sha(cache/'metadata.json'),'origin':'baseline_processed_once','baseline_seconds':info.frames/info.samplerate})
            else:reused+=1
            wave=folder/f'{ordinal:03}.wav';raw=rawfolder/wave.name
            for a,b in [(cache/'processed.wav',wave),(cache/'baseline.wav',raw),(cache/'metadata.json',wave.with_suffix('.json'))]:
                temp=b.with_name(b.name+'.tmp');shutil.copy2(a,temp);os.replace(temp,b)
            data,rate=sf.read(wave,dtype='int16',always_2d=True);meta=read(cache/'metadata.json')
            assert rate==48000 and data.shape[1]==2 and np.any(data)
            timeline.append({'kind':'spoken','source_segment':source_segment,'sentence':ordinal,'canonical':text,'spoken':r['spoken'],'path':str(wave.relative_to(p.root)),'baseline_path':str(raw.relative_to(p.root)),'baseline_seconds':meta['baseline_seconds'],'speed_applications':1,'start_sample':cursor,'end_sample':cursor+len(data),'sha256':sha(wave)})
            ledger.append(dict(kind='spoken',start_sample=cursor,end_sample=cursor+len(data),sentence=ordinal))
            chunks.append(data);cursor+=len(data);ordinal+=1
            next_spoken=i<len(parts)-1 or (contract['id']!='ceh-en-v1.0' and source_segment+1<len(scene['audio_segments']) and scene['audio_segments'][source_segment+1]['kind']=='spoken')
            if next_spoken:silence('gap',contract['gap'])
            emit({'phase':'speech_clip','scene':sid,'completed':ordinal,'generated':generated,'reused':reused})
    silence('ending',contract['ending']);silence('frame_alignment',(-cursor)%1600)
    f=p.root/'assets/voice'/f'{sid}.wav';sf.write(str(f)+'.tmp.wav',np.concatenate(chunks),48000,subtype='PCM_16');os.replace(str(f)+'.tmp.wav',f)
    result={'scene':sid,'chapter':scene['chapter_id'],'voice':'af_heart','language':'en-us','baseline_speed':.73,'atempo':contract['atempo'],'timing_policy':contract,'ledger':ledger,'sample_rate':48000,'channels':2,'samples':cursor,'duration':cursor/48000,'sentence_count':ordinal,'segments':timeline,'scope':'Generated post-speed audio; listening review separate'}
    write(p.root/'data'/f'{sid}.audio.json',result)
    write(p.qa/f'{sid}-speech-cache.json',{'generated':generated,'reprocessed':reprocessed,'reused':reused,'scene':sid,'audio_sha256':sha(f)})
    return {'generated':generated,'reprocessed':reprocessed,'reused':reused,'scene':sid}


def baseline_recipe(p,text):
    voice=p.profile['voice']
    return dict(canonical=text,spoken=spoken(text,read(p.root/'pronunciation.json')),
                voice={k:voice[k] for k in ('name','language','baseline_speed')},models=p.profile['models'],
                synthesis_runtime=p.profile.get('baseline_runtime','historical-runtime-unrecorded'),
                format=dict(sample_rate=24000,channels=1,subtype='PCM_16',gain_peak_ceiling=.94))


def baseline_entry(p,text):
    return p.state/'baseline-cache'/digest(baseline_recipe(p,text))


def valid_baseline(p,text):
    folder=baseline_entry(p,text)
    try:
        receipt=read(folder/'receipt.json')
        return receipt['recipe']==baseline_recipe(p,text) and receipt['sha256']==sha(folder/'baseline.wav')
    except (OSError,ValueError,KeyError,TypeError):return False


def import_baselines(source,destination):
    """Only hash-verified raw PCM enters the baseline cache; processed bytes never do."""
    import soundfile as sf
    count=0
    for scene in source.scenes:
        for seg in source.audio(scene['id'])['segments']:
            if seg['kind']!='spoken':continue
            text=seg['canonical'];meta=read((source.root/seg['path']).with_suffix('.json'))
            assert valid_cache(source,text), 'Unverified source cache: '+text
            receipt=read(cache_entry(source,text)/'receipt.json')
            raw=source.root/seg['baseline_path'];info=sf.info(raw)
            assert sha(raw)==receipt['baseline_sha256']
            assert (info.samplerate,info.channels,info.subtype)==(24000,1,'PCM_16')
            assert meta['spoken']==baseline_recipe(destination,text)['spoken']
            assert meta['voice']==destination.profile['voice']['name'] and meta['baseline_speed']==destination.profile['voice']['baseline_speed']
            assert meta['models_sha256']==destination.profile['models']
            folder=baseline_entry(destination,text);folder.mkdir(parents=True,exist_ok=True)
            shutil.copy2(raw,folder/'baseline.wav')
            write(folder/'receipt.json',dict(recipe=baseline_recipe(destination,text),sha256=sha(raw),origin='verified_legacy_baseline',source=str(raw),source_receipt_sha256=sha(cache_entry(source,text)/'receipt.json'),source_metadata_sha256=sha((source.root/seg['path']).with_suffix('.json'))))
            count+=1
    return count
