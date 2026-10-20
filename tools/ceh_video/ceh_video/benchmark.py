"""Isolated fixed-workload benchmark. Never changes production configuration."""
import concurrent.futures
import json
import os
from pathlib import Path
import re
import statistics
import shutil
import subprocess
import sys
import time
from .common import Project, sha, write
from .run_record import RunRecord

WORKLOADS = [('topology','S23',0),('resource','S44',23),('quiz','S50',0)]
CONFIGS = [(1,4),(2,2),(2,4)]


def host(p, out, label, sid, start, source):
    folder=out/label
    (folder/'compositions').mkdir(parents=True,exist_ok=True)
    (folder/'assets').symlink_to(p.root/'assets',target_is_directory=True)
    original=source.read_text()
    wrapper=f'''<script>(function(){{const original=window.__timelines.{sid};const clock={{time:0}};function sample(){{original.pause().seek({start}+clock.time,false);}}const benchmark=gsap.timeline({{paused:true}});benchmark.to(clock,{{time:30,duration:30,ease:'none',onUpdate:sample}},0);window.__timelines.{sid}=benchmark;sample();}})();</script>'''
    child=re.sub(r'(<div id="root"[^>]*data-duration=")[^"]+',r'\g<1>30',original).replace('</template>',wrapper+'</template>')
    (folder/'compositions'/f'{sid}.html').write_text(child)
    review=(p.root/'review'/sid/'index.html').read_text()
    head=re.search(r'<head>([\s\S]*?)</head>',review).group(1)
    (folder/'index.html').write_text(f'''<!doctype html><html><head>{head}</head><body><div id="root" data-composition-id="benchmark" data-width="1920" data-height="1080" data-duration="30"><div class="clip" data-composition-id="{sid}" data-composition-src="compositions/{sid}.html" data-start="0" data-duration="30" data-width="1920" data-height="1080" data-track-index="1" style="position:absolute;inset:0"></div></div><script>window.__timelines=window.__timelines||{{}};window.__timelines.benchmark=gsap.timeline({{paused:true}});</script></body></html>''')
    return folder


def run(p, variant, source_dir, configs=CONFIGS):
    record=RunRecord(p,'benchmark:'+variant,'benchmark')
    out=record.directory
    for file in (Path(__file__),Path(__file__).with_name('run_record.py')):
        shutil.copy2(file,out/file.name)
    print(json.dumps(dict(phase='benchmark_start',run_id=record.id,variant=variant,configurations=configs,trials=3,workloads=len(WORKLOADS),evidence=str(out))),file=sys.stderr,flush=True)
    sources={sid:sha(source_dir/(sid+'.html')) for _,sid,_ in WORKLOADS}
    hosts={label:host(p,out,label,sid,start,source_dir/(sid+'.html')) for label,sid,start in WORKLOADS}
    rows=[]
    def render(label, workers, trial, jobs):
        name=f'{variant}-{jobs}x{workers}-trial{trial}-{label}'
        video=out/(name+'.mp4');log=out/(name+'.log')
        cmd=[str(p.root/'node_modules/.bin/hyperframes'),'render',str(hosts[label]),'--output',str(video),'--fps','30','--quality','delivery','--workers',str(workers),'--no-best-effort','--strict']
        began=time.monotonic();load=os.getloadavg()
        with log.open('w') as stream:
            result=subprocess.run(['/usr/bin/time','-v',*cmd],cwd=p.root,env=p.environment(),stdout=stream,stderr=subprocess.STDOUT)
        row=dict(label=label,wall_seconds=time.monotonic()-began,exit_code=result.returncode,load_before=load,load_after=os.getloadavg(),command=cmd)
        if result.returncode:raise RuntimeError(str(log))
        probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-of','json',str(video)]))
        v=next(s for s in probe['streams'] if s['codec_type']=='video')
        assert (v['width'],v['height'],v['r_frame_rate'],int(v['nb_frames']))==(1920,1080,'30/1',900)
        subprocess.run(['ffmpeg','-v','error','-i',str(video),'-f','null','-'],check=True,stdout=subprocess.DEVNULL)
        frames={}
        for frame in (0,450,899):
            target=out/(name+f'-{frame}.png')
            subprocess.run(['ffmpeg','-v','error','-y','-i',str(video),'-vf',f'select=eq(n\\,{frame})','-frames:v','1',str(target)],check=True)
            frames[str(frame)]=sha(target)
        row.update(decoded_frames=frames,video_sha256=sha(video),probe=probe)
        log_text=log.read_text()
        probes=re.findall(r'browserGpuMode probe → (hardware|software) \(WebGL renderer vendor="([^"]*)" renderer="([^"]*)"\)',log_text)
        expected=p.profile['runtime']['expected_gpu_renderer']
        assert probes and all(mode=='hardware' and renderer==expected for mode,vendor,renderer in probes), 'GPU probe mismatch: '+str(log)
        assert 'UNVERIFIED' not in log_text, 'Unverified GPU: '+str(log)
        row['gpu_probes']=probes
        match=re.search(r'Maximum resident set size \(kbytes\): (\d+)',log_text)
        row['max_rss_kb']=int(match.group(1)) if match else None
        record.event(dict(phase='workload_complete',name=name,wall_seconds=row['wall_seconds']))
        print(json.dumps(dict(phase='workload_complete',name=name,wall_seconds=row['wall_seconds'],run_id=record.id)),file=sys.stderr,flush=True)
        return row
    try:
        for trial in range(1,4):
            # Rotate configuration order to reduce systematic warmup/order bias.
            order=configs[(trial-1)%len(configs):]+configs[:(trial-1)%len(configs)]
            for jobs,workers in order:
                began=time.monotonic()
                with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as pool:
                    results=list(pool.map(lambda w:render(w[0],workers,trial,jobs),WORKLOADS))
                rows.append(dict(trial=trial,jobs=jobs,workers=workers,batch_wall_seconds=time.monotonic()-began,workloads=results))
                print(json.dumps(dict(phase='benchmark_batch_complete',completed=len(rows),total=3*len(configs),trial=trial,jobs=jobs,workers=workers)),file=sys.stderr,flush=True)
                write(out/'benchmark.json',dict(status='running',variant=variant,sources=sources,runtime=p.profile['runtime'],rows=rows))
        refs={w['label']:w['decoded_frames'] for w in rows[0]['workloads']}
        assert sources=={sid:sha(source_dir/(sid+'.html')) for _,sid,_ in WORKLOADS}, 'Benchmark sources changed'
        equal=all(w['decoded_frames']==refs[w['label']] for row in rows for w in row['workloads'])
        assert equal,'Decoded pictures differ across trials/configurations; inspect retained frames'
        medians=[dict(jobs=j,workers=w,seconds=statistics.median(r['batch_wall_seconds'] for r in rows if (r['jobs'],r['workers'])==(j,w))) for j,w in configs]
        best=min(x['seconds'] for x in medians)
        choice=min((x for x in medians if x['seconds']<=best*1.05),key=lambda x:(x['jobs']*x['workers'],x['seconds']))
        report=dict(status='passed',variant=variant,sources=sources,runtime=p.profile['runtime'],rows=rows,medians=medians,recommendation=choice,decoded_frames_equal=equal,scope='Three visual-only 30-second excerpts; full film baseline not run; batch wall includes validation')
        write(out/'benchmark.json',report);record.finish('verified',report=str(out/'benchmark.json'))
        return report
    except BaseException as exc:
        record.finish('failed',error=str(exc));raise

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('project');parser.add_argument('variant');parser.add_argument('sources');parser.add_argument('--jobs',type=int);parser.add_argument('--workers',type=int)
    args=parser.parse_args()
    configs=[(args.jobs,args.workers)] if args.jobs and args.workers else CONFIGS
    print(json.dumps(run(Project(args.project),args.variant,Path(args.sources),configs)))
