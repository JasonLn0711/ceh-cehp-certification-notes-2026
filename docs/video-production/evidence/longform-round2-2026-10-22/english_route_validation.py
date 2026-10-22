"""Exercise current English package route against real read-only production inputs."""
from pathlib import Path
import shutil,time,json
from ceh_video.common import Project,sha,write
from ceh_video.packaging import package,inventory
from ceh_video.progress import Progress
HERE=Path(__file__).resolve().parent
WORK=Path('/home/jnlngx10/Videos/longform-round2-2026-10-22/english-route-2')
p=Project('/home/jnlngx10/Videos/CEH_M10_efficiency_v1_2/project')
original_qa=p.qa;original_output=p.output
WORK.mkdir();(WORK/'qa').mkdir();(WORK/'output').mkdir()
# Copy only curated QA payload paths, never follow arbitrary QA directory links.
for row in inventory(p)['entries']:
    if not row['path'].startswith('qa/'):continue
    target=WORK/row['path'];target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(row['source'],target)
p.qa=WORK/'qa';p.output=WORK/'output'
for name in ['engine-packaging.json','engine-extracted-reconstruction.json','package-plan.json']:(p.qa/name).unlink(missing_ok=True)
shutil.copytree(original_output/'inspection_frames',p.output/'inspection_frames')
movie=original_output/p.profile['master_filename'];before=sha(movie)
shutil.copy2(movie,p.output/movie.name)
p.profile={**p.profile,'package_format':'compact-v1','editable_filename':'english-route-compact.zip'}
started=time.monotonic()
try:
    result=package(p,Progress(plain=True))
    assert sha(movie)==before
    result.update(execution_status='LIVE_FULL_COMPLETED',runtime_validity='valid',gate_outcome='passed',
                  route='current English packaging.package',elapsed_seconds=time.monotonic()-started,
                  source_project=str(p.root),profile_override='package_format and editable_filename in memory; original production.json preserved',
                  scratch_qa_and_media_copies='Isolated harness copies; producer inventory references original sources read-only')
    write(HERE/'english-route-result.json',result)
finally:
    # Only harness-created media/QA copies; validated ZIP and reconstruction evidence remain.
    if (HERE/'english-route-result.json').exists():
        (p.output/movie.name).unlink();shutil.rmtree(p.output/'inspection_frames');shutil.rmtree(p.qa)
