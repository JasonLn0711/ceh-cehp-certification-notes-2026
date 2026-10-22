# Production publication — October 22, 2026

## Ownership and evidence

Scarce resources are review time, rendering capacity, storage and traceable history. CEH owns source, engine code, production rules and validation; coursework owns its lessons and acceptance; local Videos workspaces retain heavy media. Planning owns status, capacity and next actions. This publication adds no study hours, learner completion, new rendering or media upload.

- [Publication request](../../source/2026-10-20-ceh-m11-video-production/source.md#publication-and-planning-request--2026-10-22) authorizes separate commits and remote main publication while preserving both histories.
- [M11 owner record](../../notes/m11-session-hijacking/video-production-2026-10-20.md) retains the delivered film and historical validation. Full human listening/viewing remains pending.
- [Director adoption](DIRECTOR_LED_ADOPTION.md) owns content/script and visual-design responsibilities; [workflow and templates](DIRECTOR_LED_WORKFLOW.md) are implemented documents. New camera runtime and creative approval automation remain proposed.
- [Storage v2](LONGFORM_STORAGE_STANDARD_v2.0.0.md) and [historical validation](evidence/longform-round2-2026-10-22/README.md) were already published through `29fc4a6`. Existing receipts retain their original code fingerprints and dates.
- [Planning day](../../../planning-everything-track/weeks/2026-W43/days/2026-10-22.md#ceh-production-publication-2026-10-22), [CEH locator](../../../planning-everything-track/data/projects/2026-07-ceh-cehp-certification-training.md#ceh-production-publication-2026-10-22) and [W43](../../../planning-everything-track/weeks/2026-W43/weekly-plan.md) connect the next action to existing capacity.

## Reconciliation and next gate

The CEH checkout fast-forwarded through eight remote commits. Overlapping indexes retain the remote concept-reading/storage entries and local M11/director entries. Existing local work was preserved in a named recovery stash. Planning integrated its three cached remote commits; current remote state cannot be verified because HTTPS authentication and SSH host-key verification failed.

Next production activation requires a named release and Jason's content/storyboard decisions. M11 human acceptance remains separate. The optional practice adapter is covered by regression tests; this publication makes no new live delivery claim for it. `btop/` remains outside publication.

## Validation

The full working-tree suite passed 190 tests before reconciliation. Publication checks are recorded below after checking the integrated tree. Historical no-commit/no-push statements describe their original task snapshots; this record owns the later publication state.

Integrated publication validation passed: 190 engine tests (`PYTHONPATH=tools/ceh_video /home/jnlngx10/Videos/CEH_M10_efficiency_v1_2/project/.venv/bin/python -m unittest discover -s tools/ceh_video/tests -p 'test_*.py'`), 181 Planning metadata notes/catalog entries (`python3 scripts/validate_knowledge.py`), and both `git diff --check` checks. The existing `force_align.py` unclosed-read ResourceWarnings remain. All 242 checked CEH Markdown path targets and 12 added Planning targets resolve. Thirteen older Planning links point to unavailable local files; those predate this change.

## Git result

Local commits: `540c232` source capture, `c9fcdba` module-owned scene validation, `b18a538` practical adapter, `4b93ad7` M11 source/evidence, and `2d30413` director documents/closeout. Planning commits: `d4654988` project locator and `580b1fa1` day/week records.

Status: committed locally; this publication is blocked. `git push origin HEAD:main` failed in both repositories with `fatal: could not read Username for 'https://github.com': No such device or address`. CEH SSH push and Planning SSH fetch failed with `Host key verification failed.` No force push, credential change or remote rewrite occurred. CEH's public fetch succeeded before integration; Planning's current remote state remains unverified.

Next gate: restore the existing GitHub authentication and SSH trust configuration through its owner, fetch `origin main`, inspect any new divergence, preserve both histories, rerun affected checks if integration changes files, and retry `git push origin HEAD:main`. Recovery stashes named `publication-reconcile-2026-10-22` remain in both repositories.
