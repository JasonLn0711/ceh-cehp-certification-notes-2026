"""Execute a resumable dependency plan and require artifact-bound reviews."""
from pathlib import Path
import concurrent.futures, json, os, signal, subprocess, sys, time,queue,threading
from .common import digest, lock, read, sha, write
from .graph import nodes, planning, receipt_path, commit_receipt, inspect_node, node_key


ACTIVE_CHILDREN={}
ACTIVE_LOCK=threading.Lock()
STOP_REQUESTED=threading.Event()

class RunCancelled(RuntimeError):pass

def cancel_children():
    with ACTIVE_LOCK:
        STOP_REQUESTED.set()
        for proc in list(ACTIVE_CHILDREN.values()):
            if proc.poll() is None:
                try:os.killpg(proc.pid,signal.SIGTERM)
                except ProcessLookupError:pass

class ReviewPending(RuntimeError):pass
class StageFailure(RuntimeError):
    def __init__(self,name,exit_code,log):
        self.exit_code=exit_code if exit_code>0 else 128-exit_code
        super().__init__(f'{name} exited {exit_code}; inspect {log}')


def subprocess_stage(p,command,name,emit):
    log=p.qa/(name.replace(':','--')+'.log');log.parent.mkdir(exist_ok=True,parents=True)
    emit({'phase':'child_start','node':name,'command':command[:4],'log':str(log)})
    with log.open('a') as target:
        with ACTIVE_LOCK:
            if STOP_REQUESTED.is_set():raise RunCancelled('Run cancelled before child dispatch: '+name)
            proc=subprocess.Popen(command,cwd=p.root,env=p.environment(),stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,start_new_session=True)
            ACTIVE_CHILDREN[proc.pid]=proc
        from .progress import sanitize
        messages=queue.Queue()
        def drain():
            try:
                for line in proc.stdout:messages.put(line)
            finally:messages.put(None)
        reader=threading.Thread(target=drain,daemon=True);reader.start();last_output=None;began=time.monotonic();last_heartbeat=began
        child=p.state/'children'/(name.replace(':','--')+'.json')
        write(child,{'status':'running','pid':proc.pid,'heartbeat_at':time.time(),'last_actual_output_at':None,'activity':'quiet_child_progress_unknown'})
        try:
            while True:
                try:line=messages.get(timeout=1)
                except queue.Empty:line=''
                if line is None:break
                if line:
                    line=sanitize(line);target.write(line);target.flush();last_output=time.time()
                    if line.lstrip().startswith('{'):
                        try:emit({'node':name,'child':json.loads(line)})
                        except json.JSONDecodeError:pass
                if time.monotonic()-last_heartbeat>=15:
                    last_heartbeat=time.monotonic();write(child,{'status':'running','pid':proc.pid,'heartbeat_at':time.time(),'last_actual_output_at':last_output,'activity':'child_output_observed' if last_output else 'quiet_child_progress_unknown'})
                    emit({'phase':'child_alive_progress_unknown','node':name,'last_actual_output_at':last_output,'log':str(log)})
            code=proc.wait()
        except BaseException:
            try:os.killpg(proc.pid,signal.SIGTERM)
            except ProcessLookupError:pass
            try:proc.wait(timeout=15)
            except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);proc.wait()
            write(child,{'status':'interrupted','pid':proc.pid,'cleanup':'child_process_group_terminated'});raise
        finally:
            with ACTIVE_LOCK:ACTIVE_CHILDREN.pop(proc.pid,None)
    with ACTIVE_LOCK:ACTIVE_CHILDREN.pop(proc.pid,None)
    write(child,{'status':'completed' if code==0 else 'failed','pid':proc.pid,'exit_code':code,'last_actual_output_at':last_output})
    if code:raise StageFailure(name,code,log)


def worker(p,name,args,emit):
    subprocess_stage(p,[str(p.root/'.venv/bin/python'),'-m','ceh_video.worker',name,*args],name+('-'+'-'.join(args) if args else ''),emit)


def seed_audio(p):
    """Import only hash-verified original audio/alignment; visual review is never inferred."""
    marker=p.state/'audio-import.json'
    if marker.exists():return
    imported=read(p.qa/'reference-import.json')
    identities=p.qa/'reference-audio-identities.json'
    if not identities.exists():
        reference=Path(imported['reference'])
        write(identities,{'scenes':{s['id']:sha(reference/'project/assets/voice'/f'{s["id"]}.wav') for s in p.scenes},'voice':p.profile['voice'],'models':p.profile['models']})
    frozen=read(identities)
    assert frozen['voice']==p.profile['voice'] and frozen['models']==p.profile['models']
    from .speech import import_cache,spoken
    policy=read(p.root/'pronunciation.json')
    for s in p.scenes:
        sid=s['id'];a=p.audio(sid)
        assert sha(p.root/'assets/voice'/f'{sid}.wav')==frozen['scenes'][sid]
        assert ' '.join(x['canonical'] for x in a['segments'] if x['kind']=='spoken')==' '.join(s['narration_en_US'].split())
        for seg in a['segments']:
            if seg['kind']!='spoken':continue
            assert seg['spoken']==spoken(seg['canonical'],policy)
            assert sha(p.root/seg['path'])==seg['sha256']
            f=p.root/'data/forced-alignment'/f'{sid}-{seg["sentence"]:03}.json';alignment=read(f)
            assert alignment['audio_sha256']==seg['sha256'] and alignment['canonical']==seg['canonical']
    import_cache(p)
    graph=nodes(p)
    for sid in p.by_id:
        for name in ['speech:'+sid,'align:'+sid]:
            row=planning(p,name)[-1];commit_receipt(p,graph[name],row['key'],'verified_reference_import')
    write(marker,{'status':'verified_reference_audio_and_alignment_imported','scenes':len(p.scenes),'source':imported['reference_manifest_sha256']})


def action(p,node,emit,force=False):
    if p.profile.get('schema_version') == 2:
        from .mandarin import action as mandarin_action
        return mandarin_action(p,node,emit,force)
    name=node.name
    if name.startswith('speech:'):
        from .speech import synthesize
        synthesize(p,name.split(':')[1],emit);return 'executed'
    if name.startswith('prepare:'):
        ch=name.split(':')[1]
        fingerprint=p.qa/f'{ch}-checked-fingerprint.json';check=p.qa/f'{ch}-check.json'
        if not (fingerprint.exists() and check.exists() and read(fingerprint)['sha256']==p.chapter_inputs(ch) and read(check)['ok'] and not read(check)['browserSkipped']):worker(p,'chapter',['prepare',ch],emit)
        subprocess_stage(p,['node',str(Path(__file__).parent/'capture.mjs'),ch],name+'-captures',emit)
        worker(p,'contact_sheet',[str(p.qa/(ch+'-states'))],emit)
        return 'executed'
    if name.startswith('render:'):
        from .review import require_review
        ch=name.split(':')[1]
        try:require_review(p,ch)
        except (FileNotFoundError,RuntimeError) as exc:raise ReviewPending(str(exc))
        old=read(p.qa/'reference-import.json')['chapters'][ch];video=p.output/'chapters'/f'{ch}.mp4'
        if not force and p.chapter_inputs(ch)==old['input_sha256'] and video.exists() and sha(video)==old['mp4_sha256']:
            # The new compiler/check/capture/review have run; encoded bytes are the verified identical inputs' artifact.
            previous=read(p.qa/f'{ch}-render.json');previous.update(source_sha256=p.chapter_inputs(ch),origin='verified_reference_render_reused')
            write(p.qa/f'{ch}-render.json',previous);return 'verified_reference_render_reused'
        worker(p,'chapter',['render',ch],emit);return 'executed'
    if name=='root':
        worker(p,'assemble_project',[],emit);worker(p,'export_metadata',[],emit)
        m=read(p.root/'data/master-timing.json');times=[s['start']+s['duration']/2 for s in m['scenes']]+[(s['start']+s['end'])/2 for s in m['silences']]
        check=p.qa/'master-project-check.json'
        command=[str(p.root/'node_modules/.bin/hyperframes'),'check',str(p.root),'--at',','.join(f'{t:.6f}' for t in times),'--json']
        with check.open('w') as f:
            subprocess.run(command,cwd=p.root,env=p.environment(),stdout=f,check=True)
        result=read(check);assert result['ok'] and not result['browserSkipped']
        for layer in ['lint','runtime','layout','contrast']:assert result[layer]['errorCount']==0 and result[layer]['warningCount']==0
        for script in ['audit_quiz.mjs','audit_scene_seek.mjs']:subprocess_stage(p,['node',str(p.root/'scripts'/script)],name+'-'+script,emit)
        return 'executed'
    if name=='audio-review':
        from .review import audio_queue
        for script in ['recognition_audit','audit_audio_clips','review_audio','measure_speech','asr_receipt']:worker(p,script,[],emit)
        r=audio_queue(p);assert not r['technical_defects'],r
        return 'executed'
    if name=='checks':
        for script in ['audit_rendered','audit_audio_continuity','capture_late_diagrams']:worker(p,script,[],emit)
        return 'executed'
    if name=='delivery':
        from .delivery import validate
        validate(p);return 'executed'
    if name=='package':
        from .delivery import package
        package(p,emit);return 'executed'
    worker(p,node.action[0],node.action[1:],emit);return 'executed'


def review_batch(p,rows,emit):
    """Catch stale current reviews before launching any expensive chapter jobs."""
    if any(r['node'].startswith('prepare:') and r['action']=='run' for r in rows):return
    from .review import require_review
    for row in rows:
        if not row['node'].startswith('render:'):continue
        ch=row['node'].split(':')[1]
        try:require_review(p,ch)
        except (FileNotFoundError,RuntimeError) as exc:
            record={'status':'waiting_review','chapter':ch,'error':str(exc)}
            write(p.state/'review-gate.json',record);emit(record);raise ReviewPending(str(exc))


def run(p,target,forced,emit):
    from .preflight import preflight
    began=time.monotonic();p.state.mkdir(exist_ok=True);completed=[];reused=[]
    with lock(p.state/'run.lock'):
        STOP_REQUESTED.clear()
        preflight(p)
        if p.profile.get('schema_version') == 1:seed_audio(p)
        rows=planning(p,target);force_set=set(forced)
        unknown=force_set-set(nodes(p))
        if unknown:raise ValueError('Unknown forced nodes '+str(unknown))
        review_batch(p,rows,emit)
        def execute(name):
            if STOP_REQUESTED.is_set():raise RunCancelled('Run cancelled before node dispatch: '+name)
            node=nodes(p)[name];current=inspect_node(p,node)
            if current['action']=='reuse' and name not in force_set:
                reused.append(name);emit({'phase':'cache_reused','node':name});return
            process=p.state/'processes'/(name.replace(':','--')+'.json')
            record={'node':name,'status':'running','pid':os.getpid(),'started':time.time(),'key':current['key']};write(process,record)
            try:
                with lock(p.state/'locks'/(name.replace(':','--')+'.lock')):origin=action(p,node,emit,name in force_set)
                node=nodes(p)[name];commit_receipt(p,node,node_key(p,node),origin)
                record.update(status='verified',origin=origin);completed.append(name)
            except BaseException as exc:
                record.update(status='waiting_review' if isinstance(exc,ReviewPending) else 'interrupted' if isinstance(exc,KeyboardInterrupt) else 'failed',error=str(exc));write(process,record)
                emit({'phase':record['status'],'node':name,'error':str(exc),'receipt':str(process)});raise
            write(process,record);emit({'phase':'node_verified','node':name,'completed':len(completed),'reused':len(reused),'total_nodes':len(rows)})
        pool=concurrent.futures.ThreadPoolExecutor(max_workers=p.profile['runtime']['max_chapter_renders']);futures=[]
        try:
            for row in rows:
                name=row['node'];node=nodes(p)[name]
                if any(d in force_set for d in node.dependencies):force_set.add(name)
                for future in futures:
                    if future.done():future.result()
                if name=='master':
                    for future in futures:future.result()
                if name.startswith('render:'):futures.append(pool.submit(execute,name))
                else:execute(name)
            for future in futures:future.result()
        except BaseException:
            for future in futures:future.cancel()
            cancel_children()
            pool.shutdown(wait=True,cancel_futures=True)
            raise
        else:pool.shutdown(wait=True)
        result={'status':'verified','target':target,'executed':completed,'reused':reused,'elapsed_seconds':time.monotonic()-began,'human_listening':'pending'}
        write(p.qa/('run-'+target.replace(':','--')+'.json'),result);return result
