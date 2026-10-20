"""Append-only attempt timing. Wall time and overlapping work are distinct."""
import datetime
import json
import threading
import time
import uuid
from pathlib import Path
from .common import write
from .progress import sanitize


def phase_summary(events):
    starts={e['node']:e['elapsed_seconds'] for e in events if e.get('phase')=='node_start'}
    queued={e['node']:e['elapsed_seconds'] for e in events if e.get('phase')=='node_queued'}
    ends={e['node']:e['elapsed_seconds'] for e in events if e.get('phase')=='node_verified'}
    render=sorted((end,node) for node,end in ends.items() if node.startswith('render:'))
    return {
        'queue_wait_seconds':{n:max(0,starts[n]-t) for n,t in queued.items() if n in starts},
        'render_window_seconds':render[-1][0]-min(starts[n] for _,n in render) if render else 0,
        'last_render_node':render[-1][1] if render else None,
        'single_job_tail_seconds':render[-1][0]-render[-2][0] if len(render)>1 else 0,
        'all_started_renders_verified':all(n in ends for n in starts if n.startswith('render:')),
        'note':'Render window/tail cover verified render completions only; failed work remains in stage totals. Wall time and overlapping summed work differ.',
    }


class RunRecord:
    def __init__(self, p, target, kind='routine', parent=None):
        if kind not in {'routine','migration','retry','delivery','benchmark'}:
            raise ValueError('Unknown run kind: '+kind)
        if kind=='retry' and not parent:
            raise ValueError('A retry requires its failed parent run ID')
        if parent and (Path(parent).name!=parent or not (p.qa/'runs'/parent/'summary.json').is_file()):
            raise ValueError('Parent run must identify a closed local attempt')
        self.id = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ-')+uuid.uuid4().hex[:8]
        self.directory = p.qa/'runs'/self.id
        self.directory.mkdir(parents=True, exist_ok=False)
        self.started = time.monotonic()
        self.wall_started = time.time()
        self.lock = threading.Lock()
        self.target, self.kind, self.parent = target, kind, parent
        self.seq = 0
        self.event({'phase': 'run_start', 'target': target, 'kind': kind, 'parent_run': parent})

    def event(self, value):
        with self.lock:
            self.seq += 1
            value = dict(value)
            if 'elapsed_seconds' in value:
                value['stage_elapsed_seconds'] = value.pop('elapsed_seconds')
            row = dict(value, run_id=self.id, sequence=self.seq,
                       utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                       elapsed_seconds=time.monotonic()-self.started)
            with (self.directory/'events.jsonl').open('a') as stream:
                stream.write(sanitize(json.dumps(row))+'\n')

    def finish(self, status, **fields):
        if (self.directory/'summary.json').exists():
            raise RuntimeError('Attempt already closed: '+self.id)
        events = [json.loads(line) for line in (self.directory/'events.jsonl').read_text().splitlines()]
        stages = [dict(node=e['node'], seconds=e['stage_elapsed_seconds'], status=e['phase'])
                  for e in events if e.get('phase') in {'node_verified','failed','interrupted','waiting_review'}
                  and 'stage_elapsed_seconds' in e and 'node' in e]
        result = dict(fields, run_id=self.id, status=status, target=self.target,
                      kind=self.kind, parent_run=self.parent,
                      stages=stages, summed_stage_work_seconds=sum(s['seconds'] for s in stages),
                      phase_summary=phase_summary(events),
                      wall_seconds=time.monotonic()-self.started,
                      evidence=str(self.directory))
        self.event({'phase': 'run_end', 'status': status})
        write(self.directory/'summary.json', result)
        return result
