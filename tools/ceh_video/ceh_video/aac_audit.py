"""Measure lossy quiz boundaries separately from lossless PCM acceptance."""
import subprocess
import numpy as np
import soundfile as sf
from .common import write,sha


def audit(p,emit=lambda row:None):
    folder=p.qa/'aac-boundaries';folder.mkdir(exist_ok=True)
    rows=[]
    for sid in sorted(p.quiz_scenes()):
        source=p.root/'assets/voice'/f'{sid}.wav';encoded=folder/f'{sid}.m4a';decoded=folder/f'{sid}.decoded.wav'
        subprocess.run(['ffmpeg','-v','error','-nostdin','-y','-i',str(source),'-c:a','aac','-b:a','192k',str(encoded)],check=True)
        subprocess.run(['ffmpeg','-v','error','-nostdin','-y','-i',str(encoded),'-c:a','pcm_s16le',str(decoded)],check=True)
        pcm,rate=sf.read(decoded,dtype='int16',always_2d=True);assert rate==48000 and pcm.shape[1]==2
        for hold in p.audio(sid)['segments']:
            if hold['kind']!='silence':continue
            zero=pcm[hold['start_sample']:hold['end_sample']]
            rows.append(dict(scene=sid,start_sample=hold['start_sample'],end_sample=hold['end_sample'],decoded_frames=len(pcm),hold_frames=len(zero),nonzero_channel_samples=int(np.count_nonzero(zero)),peak_pcm=int(np.abs(zero.astype(np.int32)).max()),source_sha256=sha(source),encoded_sha256=sha(encoded),decoded_sha256=sha(decoded)))
        emit(dict(phase='aac_boundary',scene=sid,completed=len(rows),total=8))
    result=dict(status='measured',scope='Eight independently encoded AAC quiz scenes, not a full-master MP4 boundary result',encoder='FFmpeg AAC 192k, M4A edit-list-aware decode',ffmpeg=p.profile['runtime']['ffmpeg'],rows=rows)
    write(p.qa/'aac-boundary-report.json',result);return result
