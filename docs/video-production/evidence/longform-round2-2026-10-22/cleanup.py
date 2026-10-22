"""Authorized seven-target audit; remove only exact, unused ZIP-backed copies."""
from pathlib import Path
import importlib.util
import json
import os
import hashlib
import zipfile
import time
import shutil
import fcntl
import sys
from datetime import datetime,timezone

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('prior',HERE.parent/'longform-cleanup-2026-10-22/cleanup.py')
prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
BASE=prior.BASE
TARGETS=[('CEH_M06_v1_1','project_source'),('CEH_M07_v1_0','project_source'),
 ('CEH_M08_v1_0','project_source'),('CEH_M09_v1_0','project_source'),('CEH_M10_v1_0','project_source'),
 ('CEH_M10_optimization_v1','engine_project_source'),('CEH_M10_editorial_remaster_v1_1','engine_project_source')]

def dependencies(target):
    refs=[];links=[]
    # Check actual consumer documents/settings outside the proposed tree. Scripts that
    # generate staging are recorded separately by the accompanying source audit.
    roots=[BASE,Path('/home/jnlngx10/phd-research/repos/nycu-115-1-coursework')]
    for root in roots:
        for folder,dirs,files in os.walk(root,followlinks=False):
            dirs[:]=[d for d in dirs if d not in {'.git','.venv','node_modules','vendor','.production','project_source','engine_project_source','archive-verification','longform-round2-2026-10-22'}]
            for name in dirs+files:
                p=Path(folder)/name
                if p.is_symlink():
                    resolved=p.resolve()
                    if resolved==target or target in resolved.parents:links.append(str(p))
            for name in files:
                p=Path(folder)/name
                if p.suffix not in {'.md','.html','.json','.sh','.py','.js'} or p.is_symlink() or p.stat().st_size>4*1024*1024:continue
                text=p.read_text(errors='replace')
                # A relative link needs to be adjacent to this workspace; absolute
                # consumers can live anywhere in the scanned roots.
                if str(target) in text or (target.parent in p.parents and target.name+'/' in text):
                    refs.append(str(p))
    return {'consumer_references':refs,'incoming_links':links}

def protected(ws,target):
    result={}
    for root in [ws/'output',ws/'qa']:
        for folder,dirs,files in os.walk(root):
            dirs[:]=[d for d in dirs if Path(folder)/d!=target]
            for name in files:
                p=Path(folder)/name
                if not p.is_symlink():result[str(p)]=prior.sha(p)
    return result

def main():
    report_path=HERE/'cleanup-result.json'
    if report_path.exists():raise RuntimeError('Evidence exists; no automatic batch retry')
    report={'created_at':datetime.now(timezone.utc).isoformat(),'timezone':'Asia/Taipei',
            'script_sha256':prior.sha(__file__),'status':'running','items':[],
            'disk_before':shutil.disk_usage(BASE)._asdict()}
    prior.write(report_path,report)
    for name,folder in TARGETS:
        ws=BASE/name;target=ws/'output'/folder
        row={'workspace':name,'target':str(target),'status':'checking'}
        report['items'].append(row);prior.write(report_path,report)
        handle=None
        try:
            rp=ws/'qa'/('engine-packaging.json' if folder=='engine_project_source' else 'packaging-receipt.json')
            r=json.loads(rp.read_text());archive=ws/'output'/r.get('archive',r.get('zip',''))
            if archive.parent!=ws/'output' or archive.is_symlink():raise ValueError('Unexpected ZIP')
            if prior.sha(archive)!=r['sha256']:raise ValueError('ZIP hash differs from original receipt')
            files,allocated=prior.physical_tree(target)
            with zipfile.ZipFile(archive) as z:
                names=z.namelist()
                members=[i for i in z.infolist() if not i.is_dir()]
                if len(names)!=len(set(names)):raise ValueError('Duplicate ZIP entries')
                prefix=folder+'/'
                if any(not i.filename.startswith(prefix) for i in members):raise ValueError('Unexpected ZIP prefix')
                if {i.filename[len(prefix):] for i in members}!=set(files):raise ValueError('ZIP/tree file set differs')
                for i,info in enumerate(members,1):
                    rel=info.filename[len(prefix):]
                    with z.open(info) as f:h=hashlib.file_digest(f,'sha256').hexdigest()
                    if files[rel]['sha256']!=h or files[rel]['size']!=info.file_size:raise ValueError('Unique or changed payload: '+rel)
                    if i%1000==0:prior.event('cleanup_member_verification',workspace=name,completed=i,total=len(members))
            row.update(archive=str(archive),archive_sha256=r['sha256'],verified_files=len(files),
                       logical_bytes=sum(v['size'] for v in files.values()),allocated_bytes=allocated,
                       dependencies=dependencies(target))
            if any(row['dependencies'].values()):
                row.update(status='skipped_dependency',reason='Existing consumer references or incoming links; whole tree preserved')
                continue
            lock=ws/'project/.production/run.lock'
            if not lock.exists():
                row.update(status='skipped_lock_unavailable',reason='Legacy producer has no coordinating run lock')
                continue
            handle=lock.open('r');fcntl.flock(handle,fcntl.LOCK_EX|fcntl.LOCK_NB)
            row['usage_check']=prior.idle(target)
            keep=protected(ws,target);row['protected_sha256']=keep
            # Recheck exact full content after dependency audit and lock acquisition.
            current,_=prior.physical_tree(target)
            if current!=files:raise ValueError('Target changed during audit')
            if prior.sha(archive)!=r['sha256']:raise ValueError('Recovery ZIP changed during audit')
            prior.idle(target)
            row['status']='verified_removal_started';prior.write(report_path,report)
            shutil.rmtree(target)
            if protected(ws,target)!=keep:raise RuntimeError('Protected outputs changed')
            row['status']='removed_and_protected_hashes_verified'
        except Exception as e:
            row.update(status='skipped_or_stopped',error=str(e))
        finally:
            if handle:handle.close()
            prior.write(report_path,report)
            prior.event('cleanup_target_result',workspace=name,status=row['status'])
    report['disk_after']=shutil.disk_usage(BASE)._asdict()
    report['observed_free_bytes_increase']=report['disk_after']['free']-report['disk_before']['free']
    report['removed_allocated_bytes']=sum(r.get('allocated_bytes',0) for r in report['items'] if r['status']=='removed_and_protected_hashes_verified')
    report['status']='completed';prior.write(report_path,report)
    print(json.dumps({'status':report['status'],'removed_allocated_bytes':report['removed_allocated_bytes']}))

if __name__=='__main__':main()
