#!/usr/bin/env python3
"""Validate the current original question bank and its local practical fixtures.

Run from any directory: python3 assessments/practice-bank/check.py
This is a material-integrity check, not a learner or psychometric assessment.
"""
import collections
import csv
import importlib.util
from pathlib import Path
import re
import sys
sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DOMAIN = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 7, 7, 8, 9]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sections(text, prefix="CEH26-"):
    pattern = r"^### (" + re.escape(prefix) + r"[^\s]+)(?:[^\n]*)\n([\s\S]*?)(?=^### |\Z)"
    return re.findall(pattern, text, re.M)


def validate():
    with (ROOT / "assessment-governance/item_bank.csv").open() as handle:
        rows = list(csv.DictReader(handle))
    registry = {}
    for row in rows:
        if row["item_id"].startswith("CEH26-"):
            ident = (row["item_id"], row["version"])
            require(ident not in registry, f"Duplicate registry entry {ident}")
            registry[ident] = row
    ids, stems = set(), set()
    domain_counts = {}
    for form in [*(f"m{m:02d}" for m in range(1, 21)), "mock-a", "mock-b"]:
        question_text = (HERE / f"{form}.md").read_text()
        key_text = (HERE / f"{form}-key.md").read_text()
        version = re.search(r"original practice v([\d.]+)", question_text)
        require(version is not None, f"Missing form version: {form}")
        version = version[1]
        items, keys = sections(question_text), sections(key_text)
        expected = 125 if form.startswith("mock") else 30
        require(len(items) == len(keys) == expected, f"Wrong item/key count: {form}")
        require([x[0] for x in items] == [x[0] for x in keys], f"Key order/IDs differ: {form}")
        require("**Answer:" not in question_text and "Technical references:" not in question_text, f"Key content leaked into {form}")
        counts = collections.Counter()
        position_sequence = []
        for n, ((iid, body), (_, key)) in enumerate(zip(items, keys), 1):
            require(iid == f"CEH26-{form.upper()}-Q{n:03d}", f"Unexpected ID/order: {iid}")
            require(iid not in ids, f"Duplicate item ID: {iid}")
            ids.add(iid)
            stem = body.strip().split("\n\n", 1)[0]
            normalized = re.sub(r"\W+", " ", stem.lower()).strip()
            require(normalized not in stems, f"Duplicate stem: {iid}")
            stems.add(normalized)
            options = re.findall(r"^([A-D])\. (.+)$", body, re.M)
            require([x[0] for x in options] == list("ABCD"), f"Four options missing: {iid}")
            require(len({x[1] for x in options}) == 4, f"Duplicate choices: {iid}")
            answer = re.search(r"\*\*Answer: ([A-D]) — (.+)\*\*", key)
            require(answer is not None, f"Answer missing: {iid}")
            require(dict(options)[answer[1]] == answer[2], f"Answer label mismatch: {iid}")
            explanation_letters = re.findall(r"^- \*\*([A-D]) —", key, re.M)
            require(set(explanation_letters) == set("ABCD") - {answer[1]}, f"Distractor explanations incomplete: {iid}")
            position_sequence.append(answer[1])
            row = registry.get((iid, version))
            require(row is not None and row["correct_answer"] == answer[1], f"Registry/key mismatch: {iid}")
            module = int(row["module"][1:])
            require(1 <= module <= 20, f"Invalid module: {iid}")
            require(row["rationale"] in key, f"Registry explanation missing from key: {iid}")
            require(f"CEH v5 domain {DOMAIN[module-1]}" in key, f"Domain mismatch: {iid}")
            if not form.startswith("mock"):
                require(module == int(form[1:]), f"Wrong module in practice form: {iid}")
            require("https://" in key and "Technical references:" in key, f"No technical source route: {iid}")
            counts[DOMAIN[module-1]] += 1
        for start in range(0, len(position_sequence), 10):
            batch = collections.Counter(position_sequence[start:start+10])
            require(max(batch.get(c, 0) for c in "ABCD") - min(batch.get(c, 0) for c in "ABCD") <= 1, f"Unbalanced option positions: {form} batch {start//10+1}")
        require(not re.search(r"(.)\1\1\1", "".join(position_sequence)), f"Long answer-position run: {form}")
        if form.startswith("mock"):
            require([counts[d] for d in range(1, 10)] == [7, 21, 19, 30, 18, 6, 12, 6, 6], f"Wrong mock weighting: {form}")
            domain_counts[form] = dict(counts)
    require(len(ids) == 850, "Expected 850 distinct MCQs")
    practical = sections((HERE / "practical.md").read_text(), "CEHP26-")
    practical_keys = sections((HERE / "practical-key.md").read_text(), "CEHP26-")
    expected_ids = [f"CEHP26-P{p}-T{t:02d}" for p in range(1, 6) for t in range(1, 6)]
    require([x[0] for x in practical] == [x[0] for x in practical_keys] == expected_ids, "Expected 25 matched practical tasks/keys")
    spec = importlib.util.spec_from_file_location("cehp_local_lab", HERE / "lab.py")
    lab = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lab)
    lab.self_test()
    print("PASS: 600 practice + 250 distinct mock MCQs; matched keys/registry; 25 practical tasks; both blueprint allocations; five local fixture checks. No learner result recorded.")
    return domain_counts


if __name__ == "__main__":
    try:
        validate()
    except (ValueError, AssertionError, OSError) as exc:
        raise SystemExit(f"FAIL: {exc}")
