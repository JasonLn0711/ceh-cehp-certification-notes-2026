"""Prepare completed chapters while other chapters synthesize; no review inference."""
import argparse
import json
import os
import time
from ceh_video.common import Project, read, write
from ceh_video.graph import nodes
from ceh_video.runner import action
from ceh_video.run_record import RunRecord

parser = argparse.ArgumentParser()
parser.add_argument("--project", required=True)
args = parser.parse_args()
p = Project(args.project)
record = RunRecord(p, "M11:ready-chapter-preparation", "routine")
p.run_record = record
pending = set(p.chapters)
state_file = p.qa / "ready-preparation-process.json"
write(state_file, dict(status="running", pid=os.getpid(), run_id=record.id))

def emit(row):
    record.event(row)
    print(json.dumps(row), flush=True)

try:
    while pending:
        log = p.qa / "alignment-build-attempt3.log"
        compiled = {json.loads(line)["scene"] for line in log.read_text().splitlines()
                    if line.startswith('{"scene":')}
        ready = [ch for ch in pending
                 if {s["id"] for s in p.chapter_scenes(ch)} <= compiled]
        if not ready:
            # Alignment failure is recorded separately; preserve it as the next gate.
            source = read(p.qa / "narration-process.json")
            if source["status"] == "failed":
                raise RuntimeError("Narration failed; inspect its recorded attempt")
            time.sleep(5)
            continue
        for ch in sorted(ready, key=lambda c: -sum(p.audio(s["id"])["samples"]
                                                  for s in p.chapter_scenes(c))):
            started = time.monotonic()
            emit({"phase": "node_start", "node": "prepare:" + ch})
            origin = action(p, nodes(p)["prepare:" + ch], emit)
            emit({"phase": "node_verified", "node": "prepare:" + ch,
                  "elapsed_seconds": time.monotonic() - started, "origin": origin})
            pending.remove(ch)
            emit({"phase": "chapter_prepared", "chapter": ch,
                  "completed": len(p.chapters) - len(pending), "total": len(p.chapters),
                  "next_gate": "Inspect captured states and record source-bound review"})
    record.finish("completed", chapters=len(p.chapters), human_acceptance="pending")
    write(state_file, dict(status="completed", pid=os.getpid(), run_id=record.id))
except BaseException as exc:
    record.finish("interrupted" if isinstance(exc, KeyboardInterrupt) else "failed", error=str(exc))
    write(state_file, dict(status="failed", pid=os.getpid(), run_id=record.id, error=str(exc)))
    raise
