"""Actual Mandarin audio/encoded checks and source-complete, secret-free packaging."""
from pathlib import Path
import json,subprocess,shutil,zipfile,hashlib,html,re,os
from .common import read,write,sha,digest

def audio_review(p,emit):
    import numpy as np,soundfile as sf
    from .mandarin_speech import valid_cache
    items=[];errors=[];holds=[];clips=0
    decisions=p.qa/'audio-review-decisions.json';prior=read(decisions)['items'] if decisions.exists() else {}
    for scene in p.scenes:
        sid=scene['id'];a=p.audio(sid);pcm,sr=sf.read(p.root/'assets/voice'/f'{sid}.wav',dtype='int16',always_2d=True)
        assert sr==48000 and pcm.shape==(a['samples'],2)
        for seg in a['segments']:
            data=pcm[seg['start_sample']:seg['end_sample']]
            if seg['kind']=='silence':
                assert len(data)==48000 and not np.any(data);holds.append({'scene':sid,'frames':len(data),'all_zero':True});continue
            f=p.root/seg['path'];baseline=p.root/seg['baseline_path'];source=read(f.with_suffix('.json'));clips+=1
            assert sha(f)==seg['sha256'] and valid_cache(p,seg['canonical'])
            assert source['speed_applications']==1 and source['atempo']==1.5 and source['baseline_rate']=='+0%'
            assert np.any(data) and np.max(np.abs(data.astype('int32')))<32767
            alignment=read(p.root/'data/forced-alignment'/f'{sid}-{seg["sentence"]:03}.json')
            assert alignment['audio_sha256']==seg['sha256'] and ''.join(w['text'] for w in alignment['words'])==seg['canonical']
            caps=[c for c in read(p.root/'data'/f'{sid}.captions.json') if c['source_sentence']==seg['sentence']]
            # Captions are checked after scene build; audio-only target retains explicit pending state.
            if caps:assert ''.join(c['text'] for c in caps)==seg['canonical']
            ident=digest({'scene':sid,'canonical':seg['canonical'],'audio':seg['sha256']});old=prior.get(ident,{})
            items.append({'id':ident,'scene':sid,'sentence':seg['sentence'],'canonical':seg['canonical'],'spoken':seg['spoken'],
              'path':seg['path'],'baseline_path':seg['baseline_path'],'audio_sha256':seg['sha256'],
              'disposition':old.get('disposition','pending_listening'),'reviewer_type':old.get('reviewer_type','unassigned'),'evidence':old.get('evidence','Provider/PCM verification; human listening pending'),
              'reasons':['Taiwan_Mandarin_pronunciation','technical_terms' if re.search('[A-Za-z]',seg['canonical']) else 'canonical_content'],
              'technical_status':'sample_hash_recipe_and_provider_boundaries_passed'})
    assert len(holds)==len(p.questions)
    folder=p.qa/'audio-audition';folder.mkdir(exist_ok=True)
    result={'total_clips':clips,'items':items,'technical_defects':errors,'human_listening':'pending','scope':'Signal, recipes, canonical text and provider metadata; no independent pronunciation acceptance'}
    write(folder/'manifest.json',result)
    write(decisions,{'items':{r['id']:{k:r[k] for k in ['disposition','reviewer_type','evidence']} for r in items},'human_acceptance':'pending'})
    rows=['<!doctype html><html lang="zh-TW"><meta charset="utf-8"><title>中文旁白聽辨</title><style>body{font:20px sans-serif;max-width:1100px;margin:auto;background:#F0EBE4;color:#292421}article{padding:24px;border-bottom:1px solid #B8B0A9}</style><h1>中文旁白聽辨</h1><p>全部項目待人工聽辨；技術檢查不代替發音與自然度驗收。</p>']
    for item in items:rows.append('<article><h2>'+item['id']+'</h2><p>'+html.escape(item['canonical'])+'</p><audio controls src="../../project/'+item['path']+'"></audio></article>')
    (folder/'index.html').write_text('\n'.join(rows))
    write(p.qa/'audio-clip-structure-audit.json',{'status':'passed','clips':clips,'scene_tracks':len(p.scenes),'quiz_holds':holds,'technical_defects':errors})
    emit({'phase':'mandarin_audio_technical_checks','clips':clips,'holds':len(holds),'human_listening':'pending'})
    return result

def checks(p,emit):
    import soundfile as sf,numpy as np
    from .runner import subprocess_stage
    m=read(p.root/'data/master-timing.json');movie=p.output/p.profile['master_filename'];probe=read(p.qa/'master-ffprobe.json')
    video=next(s for s in probe['streams'] if s['codec_type']=='video');assert int(video['nb_read_frames'])==m['frames']
    subprocess_stage(p,['ffmpeg','-v','error','-nostdin','-i',str(movie),'-f','null','-'],'master-full-decode',emit)
    reference,sr=sf.read(p.output/'master.reference.pcm.wav',dtype='int16',always_2d=True);assert sr==48000 and len(reference)==round(m['duration']*48000)
    cursor=0
    for scene in p.scenes:
        data,rate=sf.read(p.root/'assets/voice'/f'{scene["id"]}.wav',dtype='int16',always_2d=True)
        assert rate==48000 and np.array_equal(reference[cursor:cursor+len(data)],data);cursor+=len(data)
    assert cursor==len(reference)
    decoded=p.qa/'master.decoded.wav'
    subprocess.run(['ffmpeg','-v','error','-y','-nostdin','-i',str(movie),'-vn','-ar','48000','-ac','2','-c:a','pcm_s16le',str(decoded)],check=True)
    lossy,rate=sf.read(decoded,dtype='int16',always_2d=True);holds=[]
    for h in m['silences']:
        lo=h['start_sample'];hi=h['end_sample'];assert hi-lo==48000 and not np.any(reference[lo:hi])
        interior=lossy[lo+2400:hi-2400].astype('int32');boundary=lossy[lo:hi].astype('int32')
        assert np.max(np.abs(interior))<=16,'Unexpected decoded speech in quiz hold'
        holds.append({'scene':h['scene'],'reference_zero_frames':48000,'decoded_interior_peak':int(np.max(np.abs(interior))),'decoded_interval_peak':int(np.max(np.abs(boundary))),'scope':'AAC boundary residue separate from exact reference PCM'})
    continuity=[]
    for ch in m['chapters'][1:]:
        center=round(ch['start']*48000);lo=center-24000;hi=center+24000
        difference=(lossy[lo:hi].astype('float64')-reference[lo:hi].astype('float64'))
        continuity.append({'chapter':ch['id'],'reference_sample':center,'decoded_reference_rms_difference':float(np.sqrt(np.mean(difference*difference)))})
    write(p.qa/'audio-continuity-audit.json',{'status':'passed','reference_order':'all scene PCM tracks match master sample-for-sample','quiz_holds':holds,'chapter_boundaries':continuity,'scope':'Exact reference reconstruction and decoded AAC checks; human listening pending'})
    folder=p.output/'inspection_frames';folder.mkdir(exist_ok=True);times=[]
    for scene in m['scenes']:
        for phase,fraction in [('midpoint',.5),('late',.94)]:times.append((scene['scene'],phase,scene['start']+scene['duration']*fraction))
    for h in m['silences']:times.extend([(h['scene'],'quiz-hold',(h['start']+h['end'])/2),(h['scene'],'quiz-answer',h['end']+.6)])
    samples=[]
    for sid,phase,t in times:
        name=f'{sid}-{phase}.png';target=folder/name
        subprocess.run(['ffmpeg','-v','error','-nostdin','-y','-ss',f'{t:.9f}','-i',str(movie),'-frames:v','1',str(target)],check=True)
        samples.append({'scene':sid,'phase':phase,'time':t,'file':name,'sha256':sha(target)})
        if len(samples)%12==0:emit({'phase':'encoded_frame_capture','completed':len(samples),'total':len(times)})
    write(p.qa/'rendered-artifact-audit.json',{'status':'passed','master_sha256':sha(movie),'full_decode':'passed','frames':m['frames'],'sampled_frames':samples,'human_watching':'pending'})
    write(p.qa/'late-diagram-samples.json',{'status':'passed','samples':[],'scope':'All scene late states already included in rendered-artifact-audit.json'})
    contact(folder,samples,'encoded')

def contact(folder,rows,prefix):
    from PIL import Image,ImageDraw,ImageFont
    font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',22)
    for page in range(math_ceil(len(rows)/9)):
        subset=rows[page*9:(page+1)*9];im=Image.new('RGB',(1920,400*math_ceil(len(subset)/3)),(240,235,228));draw=ImageDraw.Draw(im)
        for i,row in enumerate(subset):
            x=i%3*640;y=i//3*400;draw.text((x+10,y+5),row['file'],font=font,fill=(41,36,33));picture=Image.open(folder/row['file']).convert('RGB');picture.thumbnail((640,360));im.paste(picture,(x,y+35))
        im.save(folder/f'{prefix}-contact-{page+1:02}.jpg',quality=94)

def math_ceil(x):return __import__('math').ceil(x)

def delivery(p,emit):
    from .review import require_encoded,require_review
    from .mandarin_build import deck
    require_encoded(p)
    for ch in p.chapters:require_review(p,ch)
    m=read(p.root/'data/master-timing.json');caps=read(p.root/'data/master-captions.json');audio=read(p.qa/'audio-clip-structure-audit.json');deck_result=deck(p)
    contract=read(p.root/'data/coverage-contract.json');coverage=read(p.root/'data/coverage.json')['targets']
    assert len(contract['groups'])==15 and all(target in coverage for targets in contract['groups'].values() for target in targets)
    assert all(any(sid in p.by_id and p.by_id[sid]['kind']!='quiz' for sid in coverage[target]) for targets in contract['groups'].values() for target in targets),'Required knowledge needs substantive teaching, not quiz-only coverage'
    with zipfile.ZipFile(deck_result['path']) as z:
        assert len([n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+.xml',n)])==46
        texts=''.join(z.read(n).decode() for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+.xml',n))
        assert not any(t in texts for t in ['科技犯罪偵查','警察','查扣','嫌疑人','被害人']) and '<a:t>' in texts
    report={'status':'rendered_automated_checks_passed','scenes':len(p.scenes),'chapters':len(p.chapters),'questions':len(p.questions),'canonical_characters':sum(len(s['narration_zh_TW']) for s in p.scenes),'duration_seconds':m['duration'],'frames':m['frames'],'subtitle_cues':len(caps),'speech_clips':audio['clips'],'deck':deck_result,'master_sha256':sha(p.output/p.profile['master_filename']),'native_review':'artifact_bound_agent_review','encoded_review':'artifact_bound_agent_review','human_watching_listening':'pending','public_release':'not_activated'}
    write(p.qa/'engine-delivery.json',report)
    (p.output/'engine-render-report.md').write_text(f'''# 小公司的數位日常：製片驗收\n\n實際主片：{m['duration']:.6f} 秒，{m['frames']:,} 影格；8章46幕、八題、{report['canonical_characters']:,} 個逐字稿字元、{len(caps)} 則字幕。\n\n台灣華語實際合成 {audio['clips']} 段，正常合成基準僅套用一次1.5倍旁白處理，畫面維持1倍。八次靜音各為48,000個全零立體聲PCM音訊框，AAC邊界另存檢查。\n\n原始角色、紙感色彩、中文字型與場景來源保留雜湊。原始試卷私存，交付內容為虛構公司與原創練習。完整解碼、字幕涵蓋、138次雙向跳轉比較、64項測驗邊界檢查與抽樣編碼畫面驗收，見qa。\n\n人工完整觀看與聽辨待完成；尚未公開發布。本片與教材產製不代表學員已作答、學會或取得評量成績。\n''')
    emit({'phase':'delivery_verified',**report})

def package(p,emit):
    from .review import require_encoded
    require_encoded(p);row=read(p.qa/'engine-delivery.json');assert row['master_sha256']==sha(p.output/p.profile['master_filename'])
    source=Path(__file__).parents[1];vendor=p.root/'vendor/ceh_video';vendor.mkdir(parents=True,exist_ok=True)
    shutil.copy2(source/'pyproject.toml',vendor/'pyproject.toml');shutil.copytree(source/'ceh_video',vendor/'ceh_video',dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__'))
    from .mandarin_package import payload_files
    files=payload_files(p)
    manifest={rel:sha(f) for f,rel in files};manifest_text=''.join(f'{h}  {rel}\n' for rel,h in sorted(manifest.items()))
    target=p.output/p.profile['editable_filename'];temp=target.with_suffix('.tmp.zip');prefix='Digital_Everyday_Masterclass_zh-TW_v1/'
    with zipfile.ZipFile(temp,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
        for i,(f,rel) in enumerate(files,1):
            archive.write(f,prefix+rel)
            if i%100==0:emit({'phase':'archive_payload','completed':i,'total':len(files)})
        archive.writestr(prefix+'FILES_SHA256.txt',manifest_text)
    temp.replace(target)
    verify=p.output/'archive-verification';verify.mkdir(exist_ok=True)
    with zipfile.ZipFile(target) as archive:
        assert archive.testzip() is None;archive.extractall(verify)
    extracted=verify/prefix
    for i,(rel,h) in enumerate(manifest.items(),1):
        assert sha(extracted/rel)==h
        if i%100==0:emit({'phase':'archive_extraction_hash','completed':i,'total':len(manifest)})
    receipt={'status':'crc_extraction_and_all_payload_hashes_passed','zip':str(target),'zip_sha256':sha(target),'bytes':target.stat().st_size,'entries':len(files)+1,'verified_payloads':len(files),'extracted_root':str(extracted),'private_assessment_included':False,'human_acceptance':'pending'}
    write(p.qa/'engine-packaging.json',receipt);emit(receipt)
