"""Resume three existing-model CPU workers; shared sentence keys stay in one lane."""
import argparse,json,os,subprocess,sys,time
from pathlib import Path
from ceh_video.common import Project,read,write
from ceh_video.speech import synthesize,sentences,valid_cache
from ceh_video.run_record import RunRecord
from ceh_video.engineering import verify_audio

def groups(p,workers=3):
    parent={s['id']:s['id'] for s in p.scenes}
    def find(a):
        while parent[a]!=a:a=parent[a]
        return a
    texts={s['id']:{t for seg in s['audio_segments'] if seg['kind']=='spoken' for t in sentences(seg['text'])} for s in p.scenes}
    owners={}
    for sid,values in texts.items():
        for text in values:
            if text in owners:parent[find(sid)]=find(owners[text])
            else:owners[text]=sid
    groups={}
    for sid in parent:groups.setdefault(find(sid),[]).append(sid)
    lanes=[[] for _ in range(workers)];loads=[0]*workers
    for ids in sorted(groups.values(),key=lambda ids:-sum(len(t.split()) for sid in ids for t in texts[sid] if not valid_cache(p,t))):
        lane=min(range(workers),key=lambda i:loads[i]);lanes[lane]+=ids;loads[lane]+=sum(len(t.split()) for sid in ids for t in texts[sid] if not valid_cache(p,t))
    sets=[set().union(*(texts[sid] for sid in lane)) for lane in lanes]
    assert all(not sets[a]&sets[b] for a in range(workers) for b in range(a+1,workers))
    assert sorted(sid for lane in lanes for sid in lane)==sorted(parent)
    return lanes

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--project',required=True);parser.add_argument('--lane');parser.add_argument('--parent-run');args=parser.parse_args();p=Project(args.project)
    if args.lane is not None:
        ids=args.lane.split(',');r=RunRecord(p,'M11:narration-lane','routine')
        try:
            for sid in ids:
                start=time.monotonic();r.event(dict(phase='node_start',node='speech:'+sid))
                synthesize(p,sid,lambda e:print(json.dumps(e),flush=True))
                r.event(dict(phase='node_verified',node='speech:'+sid,elapsed_seconds=time.monotonic()-start));print(json.dumps(dict(scene=sid,status='audio_ready')),flush=True)
            r.finish('completed',scenes=ids)
        except BaseException as e:r.finish('interrupted' if isinstance(e,KeyboardInterrupt) else 'failed',error=str(e));raise
        return
    r=RunRecord(p,'M11:three-worker-narration','retry',args.parent_run);lanes=groups(p);write(p.qa/'narration-lanes.json',dict(lanes=lanes,shared_sentence_keys='assigned to one lane; no concurrent cache writes',voice=p.profile['voice']))
    children=[];streams=[];write(p.qa/'narration-process.json',dict(pid=os.getpid(),status='running',run_id=r.id))
    try:
        for i,ids in enumerate(lanes):
            f=(p.qa/f'narration-lane-{i+1}.log').open('w');streams.append(f)
            child=subprocess.Popen([sys.executable,__file__,'--project',str(p.root),'--lane',','.join(ids)],env=p.environment(),stdout=f,stderr=subprocess.STDOUT,start_new_session=True);children.append(child);r.event(dict(phase='worker_dispatched',lane=i+1,pid=child.pid,scenes=ids))
        last=time.monotonic()
        while any(c.poll() is None for c in children):
            if any(c.poll() not in (None,0) for c in children):raise RuntimeError('Narration lane failed; inspect lane logs')
            if time.monotonic()-last>15:
                print(json.dumps(dict(phase='workers_active',running=sum(c.poll() is None for c in children),logs=[f.name for f in streams])),flush=True);last=time.monotonic()
            time.sleep(1)
        assert all(c.returncode==0 for c in children)
        result=verify_audio(p);write(p.qa/'narration-process.json',dict(pid=os.getpid(),status='completed',run_id=r.id,exit_code=0));r.finish('completed',samples=result['total_samples'],scenes=len(p.scenes));print(json.dumps(dict(status='passed',scenes=len(p.scenes),samples=result['total_samples'])),flush=True)
    except BaseException as e:
        import signal
        for c in children:
            if c.poll() is None:os.killpg(c.pid,signal.SIGTERM)
        for c in children:c.wait()
        write(p.qa/'narration-process.json',dict(pid=os.getpid(),status='failed',run_id=r.id,error=str(e)));r.finish('failed',error=str(e));raise
    finally:
        for f in streams:f.close()
if __name__=='__main__':main()
