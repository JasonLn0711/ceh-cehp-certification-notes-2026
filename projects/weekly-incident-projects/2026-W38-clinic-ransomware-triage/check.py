#!/usr/bin/env python3
"""Instructor artifact check for W38 synthetic triage. No network or host changes."""
import argparse
import csv
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

FIELDS = ["asset", "verdict", "priority", "next_action", "evidence_ids"]
KEY = {
    "clinic-a": ("suspected_compromise", "1", "contain_in_plan", {"e02", "e03", "e04"}),
    "clinic-b": ("exposed_weakness", "2", "patch_in_plan", {"e05", "e06"}),
    "clinic-c": ("unverified_finding", "3", "verify_in_plan", {"e07", "e08"}),
}
ALLOWED = {"clinic-a": {"e01", "e02", "e03", "e04"}, "clinic-b": {"e05", "e06"}, "clinic-c": {"e07", "e08"}}


def check(path):
    with Path(path).open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != FIELDS:
            raise ValueError("Expected columns: " + ",".join(FIELDS))
        rows = list(reader)
    if len(rows) != 3 or {row.get("asset") for row in rows} != set(KEY):
        raise ValueError("Provide each of clinic-a, clinic-b and clinic-c exactly once")
    errors = []
    for row in rows:
        if set(row) != set(FIELDS) or any(value is None for value in row.values()):
            raise ValueError("Malformed CSV row")
        asset = row["asset"]
        verdict, priority, action, evidence = KEY[asset]
        if (row["verdict"], row["priority"], row["next_action"]) != (verdict, priority, action):
            errors.append(asset + ": review verdict, priority or proposed action")
        supplied = set(row["evidence_ids"].split(";"))
        if not evidence <= supplied or not supplied <= ALLOWED[asset]:
            errors.append(asset + ": review evidence coverage/provenance")
    return errors


def self_test():
    with TemporaryDirectory() as temp:
        path = Path(temp) / "decisions.csv"
        rows = [[asset, v, p, a, ";".join(sorted(e))] for asset, (v, p, a, e) in KEY.items()]
        def write(values):
            with path.open("w", newline="") as stream:
                writer = csv.writer(stream)
                writer.writerow(FIELDS)
                writer.writerows(values)
        write(rows)
        assert check(path) == []
        for column, bad in [(1, "unverified_finding"), (2, "3"), (3, "patch_in_plan"), (4, "e01"), (4, "e02;e03;e04;e08")]:
            changed = [row[:] for row in rows]
            changed[0][column] = bad
            write(changed)
            assert check(path), (column, bad)
        for bad in [rows[:2], [rows[0], rows[0], rows[2]], rows + [rows[0]], [rows[0][:-1], rows[1], rows[2]]]:
            write(bad)
            try:
                check(path)
            except ValueError:
                pass
            else:
                raise AssertionError("Malformed input accepted")
    print("author_self_test_passed; learner acceptance unchanged")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("worksheet", nargs="?", type=Path, help="Learner's saved CSV; never modified")
    parser.add_argument("--self-test", action="store_true", help="Author-only temporary-fixture check")
    args = parser.parse_args()
    if args.self_test:
        if args.worksheet:
            parser.error("Use --self-test without a worksheet")
        self_test()
        return 0
    if args.worksheet is None:
        parser.error("Supply a worksheet CSV or --self-test")
    try:
        errors = check(args.worksheet)
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        print("input_error: " + str(error), file=sys.stderr)
        return 2
    if errors:
        print("artifact_review_needed\n" + "\n".join(errors))
        return 1
    print("artifact_checks_passed; weekly research and learner/module acceptance still require review")
    return 0


if __name__ == "__main__":
    sys.exit(main())
