"""Sentence-content cache and sample-exact speech reconstruction."""
from pathlib import Path
import json, os, re, shutil, subprocess
from .common import digest, read, sha, write


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
    return {'canonical':text,'spoken':spoken(text,policy),'voice':p.profile['voice'],'models':p.profile['models'],
            'processing':{'sample_rate':48000,'channels':2,'subtype':'PCM_16','gain_peak_ceiling':.94,'ffmpeg':p.profile['runtime']['ffmpeg']}}


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
            assert meta['atempo']==1.5 and meta['speed_applications']==1 and meta['models_sha256']==p.profile['models']
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
        return r['recipe']==recipe(p,text) and all((d/name).exists() and sha(d/name)==r[key] for name,key in [('processed.wav','processed_sha256'),('baseline.wav','baseline_sha256'),('metadata.json','metadata_sha256')])
    except (OSError,ValueError,KeyError,TypeError):
        return False


def synthesize(p,sid,emit=lambda x:None):
    import numpy as np
    import soundfile as sf
    from kokoro_onnx import Kokoro
    scene=p.by_id[sid];policy=read(p.root/'pronunciation.json');model=None;timeline=[];chunks=[np.zeros((24000,2),dtype=np.int16)]
    cursor=24000;ordinal=0;generated=0;reused=0
    folder=p.root/'assets/voice'/sid;rawfolder=p.root/'assets/voice-baseline'/sid
    folder.mkdir(exist_ok=True,parents=True);rawfolder.mkdir(exist_ok=True,parents=True)
    for source_segment,segment in enumerate(scene['audio_segments']):
        if segment['kind']=='silence':
            timeline.append({'kind':'silence','source_segment':source_segment,'start_sample':cursor,'end_sample':cursor+48000,'seconds':1})
            chunks.append(np.zeros((48000,2),dtype=np.int16));cursor+=48000;continue
        parts=sentences(segment['text'])
        for i,text in enumerate(parts):
            cache=cache_entry(p,text);cache.mkdir(parents=True,exist_ok=True);r=recipe(p,text)
            if not valid_cache(p,text):
                if model is None:model=Kokoro(str(p.root/'models/kokoro-v1.0.onnx'),str(p.root/'models/voices-v1.0.bin'))
                samples,rate=model.create(r['spoken'],voice=r['voice']['name'],speed=r['voice']['baseline_speed'],lang=r['voice']['language'])
                assert rate==24000 and len(samples)
                gain=min(1.,.94/max(float(np.max(np.abs(samples))),1e-9))
                sf.write(cache/'baseline.tmp.wav',samples*gain,rate,subtype='PCM_16')
                subprocess.run(['ffmpeg','-v','error','-nostdin','-y','-i',str(cache/'baseline.tmp.wav'),'-af','atempo=1.5','-ar','48000','-ac','2','-c:a','pcm_s16le',str(cache/'processed.tmp.wav')],check=True)
                os.replace(cache/'baseline.tmp.wav',cache/'baseline.wav');os.replace(cache/'processed.tmp.wav',cache/'processed.wav')
                meta={'text':text,'spoken':r['spoken'],'voice':r['voice']['name'],'baseline_speed':.73,'atempo':1.5,'speed_applications':1,'models_sha256':r['models'],'baseline_seconds':len(samples)/rate,'recipe_sha256':digest(r)}
                write(cache/'metadata.json',meta)
                write(cache/'receipt.json',{'recipe':r,'processed_sha256':sha(cache/'processed.wav'),'baseline_sha256':sha(cache/'baseline.wav'),'metadata_sha256':sha(cache/'metadata.json'),'origin':'actual_local_inference','baseline_seconds':len(samples)/rate})
                generated+=1
            else:reused+=1
            wave=folder/f'{ordinal:03}.wav';raw=rawfolder/wave.name
            for a,b in [(cache/'processed.wav',wave),(cache/'baseline.wav',raw),(cache/'metadata.json',wave.with_suffix('.json'))]:
                temp=b.with_name(b.name+'.tmp');shutil.copy2(a,temp);os.replace(temp,b)
            data,rate=sf.read(wave,dtype='int16',always_2d=True);meta=read(cache/'metadata.json')
            assert rate==48000 and data.shape[1]==2 and np.any(data)
            timeline.append({'kind':'spoken','source_segment':source_segment,'sentence':ordinal,'canonical':text,'spoken':r['spoken'],'path':str(wave.relative_to(p.root)),'baseline_path':str(raw.relative_to(p.root)),'baseline_seconds':meta['baseline_seconds'],'speed_applications':1,'start_sample':cursor,'end_sample':cursor+len(data),'sha256':sha(wave)})
            chunks.append(data);cursor+=len(data);ordinal+=1
            if i<len(parts)-1:chunks.append(np.zeros((8640,2),dtype=np.int16));cursor+=8640
            emit({'phase':'speech_clip','scene':sid,'completed':ordinal,'generated':generated,'reused':reused})
    tail=144000;pad=(-(cursor+tail))%1600;chunks.append(np.zeros((tail+pad,2),dtype=np.int16));cursor+=tail+pad
    f=p.root/'assets/voice'/f'{sid}.wav';sf.write(str(f)+'.tmp.wav',np.concatenate(chunks),48000,subtype='PCM_16');os.replace(str(f)+'.tmp.wav',f)
    result={'scene':sid,'chapter':scene['chapter_id'],'voice':'af_heart','language':'en-us','baseline_speed':.73,'atempo':1.5,'sample_rate':48000,'channels':2,'samples':cursor,'duration':cursor/48000,'sentence_count':ordinal,'segments':timeline,'scope':'Generated post-speed audio; listening review separate'}
    write(p.root/'data'/f'{sid}.audio.json',result)
    write(p.qa/f'{sid}-speech-cache.json',{'generated':generated,'reused':reused,'scene':sid,'audio_sha256':sha(f)})
    return {'generated':generated,'reused':reused,'scene':sid}
