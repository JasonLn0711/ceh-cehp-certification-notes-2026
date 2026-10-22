"""Continue source-bound checks once the recorded alignment attempt completes.

This stops at candidate screenshots. Golden approval, native rendering and
delivery remain separate, artifact-bound actions.
"""
import argparse
import json
import os
import subprocess
import sys
import time
from ceh_video.common import Project, read
from ceh_video.run_record import RunRecord
from ceh_video.runner import checked_prepare_ready

parser = argparse.ArgumentParser()
parser.add_argument("--project", required=True)
parser.add_argument("--alignment-run", required=True)
parser.add_argument("--parent-run")
args = parser.parse_args()
p = Project(args.project)
upstream = p.qa / "runs" / args.alignment_run
if not upstream.is_dir():
    raise ValueError("Unknown alignment run")
record = RunRecord(p, "M11:source-and-candidate-validation",
                   "retry" if args.parent_run else "routine", args.parent_run)
try:
    while not (upstream / "summary.json").is_file():
        print(json.dumps({"phase": "waiting_alignment", "run": args.alignment_run}), flush=True)
        time.sleep(15)
    if read(upstream / "summary.json")["status"] != "completed":
        raise RuntimeError("Alignment did not complete; inspect upstream evidence")
    preparation = p.qa / "ready-preparation-process.json"
    while preparation.exists():
        state = read(preparation)
        if state["status"] == "completed":
            break
        if state["status"] != "running":
            raise RuntimeError("Ready-chapter preparation failed; inspect its attempt")
        os.kill(state["pid"], 0)
        print(json.dumps({"phase": "waiting_chapter_preparation", "run": state["run_id"]}), flush=True)
        time.sleep(5)
    while True:
        pending = [ch for ch in p.chapters if not checked_prepare_ready(p, ch)]
        if not pending:
            break
        print(json.dumps({"phase": "waiting_actual_chapter_review", "chapters": pending}), flush=True)
        time.sleep(5)
    commands = [
        ("verify-audio", ["engineering", "--stage", "verify-audio", "--run-kind", "routine"]),
        ("build", ["engineering", "--stage", "build", "--run-kind", "routine"]),
        ("preflight", ["preflight"]),
        ("representative-precheck", ["qa", "--scope", "representative", "--precheck"]),
        ("full-precheck", ["qa", "--scope", "full", "--precheck"]),
        ("candidate", ["qa", "--scope", "full"]),
    ]
    for name, command in commands:
        started = time.monotonic()
        record.event({"phase": "node_start", "node": name})
        log = record.directory / (name + ".log")
        print(json.dumps({"phase": "validation_start", "stage": name, "log": str(log)}), flush=True)
        with log.open("w") as stream:
            result = subprocess.run(
                [sys.executable, "-m", "ceh_video", "--project", str(p.root), "--plain", *command],
                env=p.environment(), stdout=stream, stderr=subprocess.STDOUT,
            )
        if result.returncode:
            raise RuntimeError(name + " failed; inspect " + str(log))
        record.event({"phase": "node_verified", "node": name,
                      "elapsed_seconds": time.monotonic() - started})
    record.finish("completed", next_gate="Inspect candidate screenshots before golden approval")
except BaseException as exc:
    record.finish("interrupted" if isinstance(exc, KeyboardInterrupt) else "failed", error=str(exc))
    raise
