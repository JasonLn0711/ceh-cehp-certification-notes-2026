#!/usr/bin/env python3
"""Check the CEH sample graph without third-party Python dependencies."""

import argparse
from collections import Counter, deque
import json
from pathlib import Path
import re
import sys
import time


def check(graph_path, corpus):
    data = json.loads(graph_path.read_text(encoding="utf-8"))
    errors = []
    nodes = data.get("nodes", [])
    edges = data.get("links", data.get("edges", []))
    if not isinstance(nodes, list) or not isinstance(edges, list):
        return ["nodes and links must be arrays"], 0, 0
    if not nodes or not edges:
        errors.append("graph must contain nodes and relationships")
    if not data.get("directed"):
        errors.append("this lab expects a directed graph")
    if not data.get("graph", {}).get("schema_version"):
        errors.append("graph schema_version is missing")
    if not data.get("graph", {}).get("graphify_version"):
        errors.append("graph graphify_version is missing")
    ids = [n.get("id") for n in nodes]
    if len(set(ids)) != len(ids):
        errors.append("duplicate node IDs")
    id_set = set(ids)
    covered = set()
    for kind, items in (("node", nodes), ("edge", edges)):
        for i, item in enumerate(items):
            source = item.get("source_file")
            if not source:
                errors.append(f"{kind} {i}: missing source_file")
                continue
            path = (corpus / source).resolve()
            if not path.is_relative_to(corpus) or not path.is_file():
                errors.append(f"{kind} {i}: source does not resolve inside corpus: {source}")
                continue
            if kind == "node":
                covered.add(path)
            location = item.get("source_location")
            if not location:
                errors.append(f"{kind} {i}: missing source_location")
            elif not re.fullmatch(r"L\d+(?:[-–]L?\d+)?", str(location)):
                # Section names are directly checkable against Markdown headings.
                section = str(location).lstrip("# ")
                headings = [line.lstrip("# ").strip() for line in path.read_text(encoding="utf-8").splitlines() if line.startswith("#")]
                if section not in headings:
                    errors.append(f"{kind} {i}: section not found: {location}")
            else:
                last_line = int(re.findall(r"\d+", str(location))[-1])
                if not 1 <= last_line <= len(path.read_text(encoding="utf-8").splitlines()):
                    errors.append(f"{kind} {i}: line location out of range")
    for i, edge in enumerate(edges):
        if edge.get("source") not in id_set or edge.get("target") not in id_set:
            errors.append(f"edge {i}: dangling endpoint")
        tag, score = edge.get("confidence"), edge.get("confidence_score")
        valid = ((tag == "EXTRACTED" and score == 1.0)
                 or (tag == "INFERRED" and score in (0.95, 0.85, 0.75, 0.65, 0.55))
                 or (tag == "AMBIGUOUS" and isinstance(score, (int, float)) and 0.1 <= score <= 0.3))
        if not valid:
            errors.append(f"edge {i}: invalid confidence tag/score")
    missing = set(corpus.glob("*.md")) - covered
    if missing:
        errors.append("notes without nodes: " + ", ".join(sorted(p.name for p in missing)))
    labels = Counter(n.get("label") for n in nodes)
    for label in ("Port Observation", "Service Identification", "Vulnerability Assessment", "Remediation Plan", "Verification Record"):
        if labels[label] != 1:
            errors.append(f"expected one canonical {label!r} node; found {labels[label]}")
    by_label = {n.get("label"): n.get("id") for n in nodes}
    start, end = by_label.get("Port Observation"), by_label.get("Verification Record")
    queue, visited = deque([start] if start else []), set()
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        queue.extend(e.get("target") for e in edges if e.get("source") == current)
    if not end or end not in visited:
        errors.append("no directed path from Port Observation to Verification Record")
    return errors, len(nodes), len(edges)


def main():
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graph", type=Path, default=root / "graphify-out/graph.json")
    parser.add_argument("--corpus", type=Path, default=root / "corpus")
    args = parser.parse_args()
    started = time.monotonic()
    print(f"Checking {args.graph}", file=sys.stderr)
    try:
        errors, nodes, edges = check(args.graph, args.corpus.resolve())
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        print(f"FAIL: {exc}. Build with the README's Codex prompt or inspect the input JSON.", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {nodes} nodes, {edges} edges; sources, tags, coverage and path checked ({time.monotonic() - started:.2f}s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
