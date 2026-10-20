"""Recorded integration QA, independent of screenshot baseline approval."""
import argparse
from pathlib import Path
import shutil
import time
from .common import Project, read
from .progress import Progress
from .run_record import RunRecord
from .runner import subprocess_stage

STAGES = {
    'boundaries': ('remaster-boundaries.mjs','remaster-boundaries/report.json'),
    'assets': ('remaster-assets.mjs','remaster-assets/report.json'),
    'quiz-negative': ('quiz-divider-negative.mjs','quiz-divider-negative/report.json'),
}

def run(p, selected, emit, kind='migration', parent=None):
    record=RunRecord(p,'qa:integration:'+selected,kind,parent);p.run_record=record
    def observed(row):record.event(row);emit(row)
    try:
        for name,(script,receipt) in STAGES.items():
            if selected!='all' and selected!=name:continue
            node='qa-'+name;began=time.monotonic();observed(dict(phase='node_start',node=node))
            try:
                subprocess_stage(p,['node',str(Path(__file__).parent/'visual'/script),str(p.root)],node,observed)
                assert read(p.qa/receipt)['status']=='passed',receipt
            except BaseException as exc:
                observed(dict(phase='failed',node=node,elapsed_seconds=time.monotonic()-began,error=str(exc)))
                raise
            observed(dict(phase='node_verified',node=node,elapsed_seconds=time.monotonic()-began))
        return record.finish('verified')
    except BaseException as exc:
        record.finish('interrupted' if isinstance(exc,KeyboardInterrupt) else 'failed',error=str(exc));raise
    finally:
        for f in p.qa.glob('qa-*.log*'):
            if f.stat().st_mtime>=record.wall_started:shutil.copy2(f,record.directory/f.name)
        del p.run_record

if __name__=='__main__':
    import json
    parser=argparse.ArgumentParser();parser.add_argument('project');parser.add_argument('--stage',choices=['all',*STAGES],default='all');parser.add_argument('--run-kind',choices=['migration','routine','retry'],default='migration');parser.add_argument('--parent-run');parser.add_argument('--plain',action='store_true')
    args=parser.parse_args()
    print(json.dumps(run(Project(args.project),args.stage,Progress(args.plain),args.run_kind,args.parent_run)))
