"""Read-only historical ZIP inputs; real compact write + complete offline restore."""
from pathlib import Path
import hashlib,json,os,shutil,subprocess,sys,tempfile,threading,time,zipfile
from datetime import datetime,timezone
from ceh_video.common import sha,write
from ceh_video.compact_archive import write_compact
from ceh_video.progress import Progress
HERE=Path(__file__).resolve().parent
WORK=Path('/home/jnlngx10/Videos/longform-round2-2026-10-22')
BASE=Path('/home/jnlngx10/Videos')
CASES=[('english',BASE/'CEH_M10_efficiency_v1_2/output/CEH_M10_efficiency_v1_2_EDITABLE.zip','bdae800b242376b09ee4817270eaa7a3b611eda160e8a2491abb0d072934b825'),
 ('concepts',BASE/'Island_Workshop_MATLAB_Concepts_v3_images_gpu/output/Island_Workshop_MATLAB_Concepts_zh-TW_v3_images_gpu_FULL.zip','a8e73b30cb609de2bd4b7b0f2a91e3cea8a46042bea8f948fb39f71cd525a22c'),
 ('practice',BASE/'island-workshop-matlab-practice-v1/output/third-video-DELIVERY.zip','5e00d214288022e4af7e8c43735ca91bb8bf0bb84186dcd424b191b9b64cbc82')]

def allocated(root):
    total=0
    for folder,dirs,files in os.walk(root):
        for name in files:
            try:total+=(Path(folder)/name).stat().st_blocks*512
            except FileNotFoundError:pass
    return total

def english_check(root):
    base=root/'engine_project_source';env=os.environ.copy()
    env['CEH_VIDEO_PROJECT']=str(base/'project');env['PYTHONPATH']=str(base/'project/vendor')
    code='''import json
from ceh_video.common import Project,project_root,read,sha
from ceh_video.delivery import restore_packaged_audio_cache,verify_encoded_evidence,verify_golden_review_evidence
from ceh_video.packaging import restore_hosts,html_identity
p=Project(project_root())
r={'audio':restore_packaged_audio_cache(p),'hosts':restore_hosts(p),'pictures':verify_encoded_evidence(p.root.parent),'golden':verify_golden_review_evidence(p.root.parent)}
assert r['audio']['new_inferences']==r['audio']['tempo_passes']==0
pcm=read(p.root/'provenance/host-restore.json');html=read(p.root/'provenance/host-html-restore.json')
for name,h in pcm.items():assert sha(p.root/name)==h,name
for name,h in html.items():assert html_identity(p.root/name)==h,name
r['pcm_hashes_verified']=len(pcm);r['html_hashes_verified']=len(html)
print(json.dumps(r))'''
    return json.loads(subprocess.check_output([sys.executable,'-c',code],env=env,cwd=base,text=True))

def main():
    target=HERE/'archive-results.json'
    if target.exists():raise RuntimeError('Run evidence already exists')
    report={'study_id':'longform-storage-round2','experiment_id':'compact-real-restore-2026-10-22',
            'created_at':datetime.now(timezone.utc).isoformat(),'timezone':'Asia/Taipei',
            'execution_status':'running','runtime_validity':'fixed_python',
            'python':sys.version,'script_sha256':sha(__file__),'cases':[]}
    write(target,report)
    for ident,archive,expected in CASES:
        row={'id':ident,'source_archive':str(archive),'original_bytes':archive.stat().st_size,'status':'running'}
        report['cases'].append(row);write(target,report)
        assert sha(archive)==expected
        dest=WORK/('archive-'+ident);dest.mkdir()
        stop=threading.Event();peak=[0]
        def monitor():
            while not stop.wait(.5):peak[0]=max(peak[0],allocated(dest))
        thread=threading.Thread(target=monitor);thread.start()
        try:
            with tempfile.TemporaryDirectory(prefix='source-extraction-',dir=dest) as temp:
                started=time.monotonic()
                with zipfile.ZipFile(archive) as z:
                    for info in z.infolist():
                        if info.is_dir():continue
                        from ceh_video.compact_restore import safe_name
                        safe_name(info.filename)
                        if (info.external_attr>>16)&0o170000==0o120000:raise ValueError('Linked source')
                    z.extractall(temp)
                    entries=[(Path(temp)/i.filename,i.filename) for i in z.infolist() if not i.is_dir()]
                row['source_extraction_seconds']=time.monotonic()-started
                row['source_extraction_bytes']=sum(p.stat().st_size for p,_ in entries)
                reconstruction={}
                def verify(root):
                    if ident=='english':reconstruction.update(english_check(root))
                started=time.monotonic()
                result=write_compact(entries,dest/'compact.zip',Progress(plain=True),verify)
                row.update(compact=result,package_and_full_restore_seconds=time.monotonic()-started,
                           english_zero_inference_restore=reconstruction or 'not_applicable')
            assert sha(archive)==expected
            row.update(status='passed',original_sha256_preserved=expected,
                       saved_archive_bytes=row['original_bytes']-result['bytes'])
        except BaseException as e:
            row.update(status='failed',error=repr(e));raise
        finally:
            stop.set();thread.join();row['sampled_peak_allocated_bytes_including_source_extraction']=peak[0]
            row['peak_sampling_seconds']=.5;write(target,report)
    report.update(execution_status='LIVE_FULL_COMPLETED',runtime_validity='valid',gate_outcome='passed',
                  decision='compact format validated for exact historical payloads; original releases preserved')
    write(target,report)
    print(json.dumps(report))
if __name__=='__main__':main()
