"""Taiwan Mandarin provider audio and real boundary metadata; no inferred word timing."""
from pathlib import Path
import asyncio, json, re, shutil, subprocess, unicodedata
from .common import digest, read, sha, write
from .mandarin_policy import timing, tail_samples

TICKS = 10_000_000

def normalize(text):
    return ''.join(c.lower() for c in unicodedata.normalize('NFKC',text) if c.isalnum())

def spoken(text, policy):
    # ASCII token edges deliberately work next to Han characters.
    spell=set(policy.get('spell',[])); words=policy.get('pronunciations',{})
    def expand(m):
        token=m.group(0)
        return ' '.join(token) if token in spell else words.get(token,token)
    return re.sub(r'(?<![A-Za-z0-9])[A-Za-z][A-Za-z0-9-]*(?![A-Za-z0-9])',expand,text)

def recipe(p,text):
    result = {'canonical':text,'spoken':spoken(text,read(p.root/'pronunciation.json')),
      'voice':p.profile['voice'],'processing':{'atempo':p.profile['voice']['atempo'],'speed_applications':1,
      'sample_rate':48000,'channels':2,'subtype':'PCM_16','ffmpeg':p.profile['runtime']['ffmpeg']}}
    if p.profile.get('quiet_tail'):result['processing']['quiet_tail']=p.profile['quiet_tail']
    return result

def cache_entry(p,text):return p.state/'speech-cache'/digest(recipe(p,text))

def valid_cache(p,text):
    folder=cache_entry(p,text)
    try:
        receipt=read(folder/'receipt.json')
        return receipt['recipe']==recipe(p,text) and all((folder/f).is_file() and sha(folder/f)==h for f,h in receipt['outputs'].items())
    except (OSError,ValueError,KeyError,TypeError):return False

def align_events(canonical,events,processed_seconds,rate=1.5):
    positions=[]; stream=''
    for index,char in enumerate(canonical):
        value=normalize(char)
        positions.extend([index]*len(value));stream+=value
    actual=''.join(normalize(e['text']) for e in events)
    if actual!=stream:raise ValueError('Provider boundary text does not cover canonical text: '+repr((actual,stream)))
    rows=[];cursor=0;prior=0
    for event in events:
        token=normalize(event['text'])
        if not token:continue
        end=cursor+len(token);lo=positions[cursor];hi=positions[end-1]+1
        start=event['offset']/TICKS/rate;stop=(event['offset']+event['duration'])/TICKS/rate
        assert start>=prior-.001 and stop>start and stop<=processed_seconds+.08,(start,stop,processed_seconds)
        rows.append({'text':canonical[lo:hi],'char_start':lo,'char_end':hi,'start':start,
          'end':min(stop,processed_seconds),'source':'provider_word_boundary'})
        prior=start;cursor=end
    assert rows and cursor==len(stream)
    # Carry punctuation/spacing with its real adjacent provider token, never divide a token.
    for i,row in enumerate(rows):
        lo=0 if i==0 else row['char_start'];hi=rows[i+1]['char_start'] if i+1<len(rows) else len(canonical)
        row['text']=canonical[lo:hi];row['char_start']=lo;row['char_end']=hi
    assert ''.join(w['text'] for w in rows)==canonical
    return rows

async def generate(p,text,folder):
    import edge_tts, soundfile as sf, numpy as np
    r=recipe(p,text);folder.mkdir(parents=True,exist_ok=True);events=[]
    request={'text':r['spoken'],'voice':r['voice']['name'],'rate':r['voice']['baseline_rate'],'boundary':'WordBoundary'}
    write(folder/'request.json',request)
    with (folder/'provider.tmp.mp3').open('wb') as output:
        async for item in edge_tts.Communicate(**request).stream():
            if item['type']=='audio':output.write(item['data'])
            elif item['type']=='WordBoundary':events.append(item)
    assert events and (folder/'provider.tmp.mp3').stat().st_size>0
    (folder/'provider.tmp.mp3').replace(folder/'provider.mp3')
    subprocess.run(['ffmpeg','-v','error','-nostdin','-y','-i',str(folder/'provider.mp3'),'-ar','48000','-ac','2','-c:a','pcm_s16le',str(folder/'baseline.wav')],check=True)
    process_baseline(p,text,folder,events,origin='actual_online_tts',provider_version=edge_tts.__version__)

def quiet_tail_window(data,sample_rate,events,config):
    """Trim only quiet source tail beyond both provider speech and signal plus guard."""
    import numpy as np
    assert sample_rate==48000 and data.ndim==2 and data.shape[1]==2 and events
    end=len(data)
    if config:
        assert config=={'threshold_pcm16':32,'retain_seconds':.18}
        peak=np.max(np.abs(data.astype('int32')),axis=1)
        active=np.flatnonzero(peak>config['threshold_pcm16']);assert len(active)
        provider_end=max((e['offset']+e['duration'])/TICKS for e in events)
        guard=round(config['retain_seconds']*sample_rate)
        end=min(len(data),max(round(provider_end*sample_rate)+guard,int(active[-1])+1+guard))
        assert end/sample_rate>=provider_end
        assert not len(peak[end:]) or int(np.max(peak[end:]))<=config['threshold_pcm16']
    return end

def process_baseline(p,text,folder,events,origin='verified_baseline_reprocessed',provider_version='7.3.1'):
    import soundfile as sf, numpy as np
    r=recipe(p,text);speed=p.profile['voice']['atempo']
    baseline_data,sr=sf.read(folder/'baseline.wav',dtype='int16',always_2d=True)
    end=quiet_tail_window(baseline_data,sr,events,p.profile.get('quiet_tail'))
    chain=(f'atrim=end_sample={end},asetpts=PTS-STARTPTS,' if end<len(baseline_data) else '')+f'atempo={speed}'
    subprocess.run(['ffmpeg','-v','error','-nostdin','-y','-i',str(folder/'baseline.wav'),'-af',chain,'-ar','48000','-ac','2','-c:a','pcm_s16le',str(folder/'processed.wav')],check=True)
    data,rate=sf.read(folder/'processed.wav',dtype='int16',always_2d=True)
    assert rate==48000 and data.shape[1]==2 and np.any(data) and np.max(np.abs(data.astype('int32')))<32767
    words=align_events(text,events,len(data)/rate,speed)
    alignment_recipe=f'edge-provider-word-boundaries-atempo-{speed}-v1'
    write(folder/'boundaries.json',{'events':events,'words':words,'recipe':alignment_recipe,'scope':'Provider timing and text coverage, not independent ASR or human listening'})
    baseline=sf.info(folder/'baseline.wav')
    meta={'text':text,'spoken':r['spoken'],'voice':r['voice']['name'],'baseline_rate':'+0%',
      'baseline_speed':1.0,'atempo':speed,'speed_applications':1,'baseline_seconds':baseline.duration,
      'processed_seconds':len(data)/rate,'samples':len(data),'recipe_sha256':digest(r)}
    if p.profile.get('quiet_tail'):
        removed=baseline_data[end:].astype('int32')
        meta['source_window']={'start_sample':0,'end_sample':end,'baseline_samples':len(baseline_data),'sample_rate':sr,
          'removed_tail_seconds':(len(baseline_data)-end)/sr,'removed_tail_peak':int(np.max(np.abs(removed))) if len(removed) else 0,
          'provider_last_end_seconds':max((e['offset']+e['duration'])/TICKS for e in events),'guard_seconds':.18,'filter':chain}
    write(folder/'metadata.json',meta)
    names=['provider.mp3','baseline.wav','processed.wav','metadata.json','boundaries.json','request.json']
    write(folder/'receipt.json',{'recipe':r,'outputs':{n:sha(folder/n) for n in names},'origin':origin,'provider_version':provider_version})

def synthesize(p,sid,emit=lambda x:None):
    import soundfile as sf, numpy as np
    scene=p.by_id[sid];policy=timing(p.profile);opening=policy['opening_samples'];chunks=[np.zeros((opening,2),dtype='int16')];cursor=opening;rows=[];ordinal=0;reused=0;generated=0
    out=p.root/'assets/voice'/sid;raw=p.root/'assets/voice-baseline'/sid
    for d in [out,raw,p.root/'data/forced-alignment']:d.mkdir(parents=True,exist_ok=True)
    for segment_index,segment in enumerate(scene['audio_segments']):
        if segment['kind']=='silence':
            hold=policy['quiz_samples'];silence=np.zeros((hold,2),dtype='int16');chunks.append(silence)
            rows.append({'kind':'silence','start_sample':cursor,'end_sample':cursor+hold,'seconds':hold/48000});cursor+=hold;continue
        text=segment['text'];folder=cache_entry(p,text)
        if not valid_cache(p,text):asyncio.run(generate(p,text,folder));generated+=1
        else:reused+=1
        wave=out/f'{ordinal:03}.wav';baseline=raw/f'{ordinal:03}.wav'
        for src,dest in [(folder/'processed.wav',wave),(folder/'baseline.wav',baseline),(folder/'metadata.json',wave.with_suffix('.json'))]:shutil.copy2(src,dest)
        pcm,rate=sf.read(wave,dtype='int16',always_2d=True);assert rate==48000
        meta=read(folder/'metadata.json');r=recipe(p,text);boundaries=read(folder/'boundaries.json')
        row={'kind':'spoken','source_segment':segment_index,'sentence':ordinal,'canonical':text,'spoken':r['spoken'],
          'path':str(wave.relative_to(p.root)),'baseline_path':str(baseline.relative_to(p.root)),
          'baseline_seconds':meta['baseline_seconds'],'speed_applications':1,'start_sample':cursor,'end_sample':cursor+len(pcm),'sha256':sha(wave)}
        rows.append(row);chunks.append(pcm);cursor+=len(pcm)
        write(p.root/'data/forced-alignment'/f'{sid}-{ordinal:03}.json',{'scene':sid,'sentence':ordinal,
          'canonical':text,'spoken':r['spoken'],'audio_sha256':sha(wave),'recipe':boundaries['recipe'],
          'duration':len(pcm)/rate,'words':boundaries['words'],'review_flags':[],'status':'provider_aligned_not_listen_reviewed'})
        ordinal+=1
        if segment_index+1<len(scene['audio_segments']) and scene['audio_segments'][segment_index+1]['kind']=='spoken':
            gap=policy['sentence_gap_samples'];chunks.append(np.zeros((gap,2),dtype='int16'));cursor+=gap
        emit({'phase':'mandarin_tts_clip','scene':sid,'completed':ordinal,'generated':generated,'reused':reused})
    tail=tail_samples(p,scene);pad=(-(cursor+tail))%1600;chunks.append(np.zeros((tail+pad,2),dtype='int16'));cursor+=tail+pad
    dest=p.root/'assets/voice'/f'{sid}.wav';sf.write(str(dest)+'.tmp.wav',np.concatenate(chunks),48000,subtype='PCM_16');Path(str(dest)+'.tmp.wav').replace(dest)
    write(p.root/'data'/f'{sid}.audio.json',{'scene':sid,'chapter':scene['chapter_id'],'voice':p.profile['voice']['name'],
      'language':'zh-TW','baseline_speed':1.0,'atempo':p.profile['voice']['atempo'],'sample_rate':48000,'channels':2,'samples':cursor,
      'duration':cursor/48000,'timing_policy':policy,'tail_samples':tail,'frame_padding_samples':pad,'sentence_count':ordinal,'segments':rows,'scope':'Actual generated narration; human listening pending'})
    write(p.qa/f'{sid}-speech-cache.json',{'scene':sid,'generated':generated,'reused':reused,'audio_sha256':sha(dest)})
    return {'scene':sid,'generated':generated,'reused':reused}
