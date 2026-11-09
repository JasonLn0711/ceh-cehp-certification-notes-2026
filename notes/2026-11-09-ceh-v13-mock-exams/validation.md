# Validation receipt — November 9, 2026

Status: **validated for source custody, note coverage and connection integrity**. [Machine-readable receipt](validation.json) records the measured checks and their scope. [Collection index](README.md) · [Source receipt](../../source/2026-11-09-ceh-v13-mock-exams/README.md) · [Question audit](quality-audit.md) · [Connection map](connections.md).

## Source and coverage evidence

| Requirement | Observed result |
| --- | --- |
| Preserve the supplied archive members | Original ZIP and all five extracted attachments match their recorded SHA-256; extracted bytes equal the corresponding ZIP member bytes |
| Cover all four files | Bank 1–542, Mock 01 1–125, Mock 02 1–125 excluding 110, Mock 03 1–125; 916 numbered entries total |
| Preserve additional source content | One complete BYOD question embedded inside Bank Q517 has its own record with the malformed original label; source numbering stays unchanged |
| Explain every entry | 917 unique IDs, retained stems/printed keys, source lines/headings/pages, concepts, substantive study explanations and direct question-note anchors |
| Connect course modules | Twenty guides include all 917 item links exactly once by editorial primary module and link to their corresponding existing practice form |
| Preserve answer-key semantics | Printed keys agree with the source; all 125 Mock 03 bold markings agree with its derived index; Mock 02 Q110 remains absent with its original placeholder |
| Preserve key/content defects | 102 held entries appear individually in the audit; 139 qualifications remain in the register and detailed notes; 676 additional study explanations carry no independent key-certification claim |
| Trace repetition | 114 normalized-stem duplicate groups, 114 extra entries and 803 distinct normalized stem strings; raw keys remain available for each pair |
| Preserve the image | Original PNG bytes retained, relative source link intact and image visually inspected; the identity/device/least-privilege content is connected to M01 |
| Connect existing records | Twelve CEH entry points and five thin Planning records link the source, notes, project, day and relevant weekly plans |

The focused verification independently reads the ZIP, source headings and keys, CSV register, detailed notes, module tables, duplicate register and link targets. It verifies every register destination and source line, rather than treating file counts alone as coverage.

## Repository checks

- `python3 assessments/practice-bank/check.py` in the CEH repo: **passed**. It verifies the existing 600 core items, 250 authored mock items, keys/registry, 25 practical tasks, allocation and five local fixtures. It does not certify the imported source keys.
- `python3 scripts/validate_knowledge.py` in Planning: **passed**, 186 metadata notes and 186 catalog entries.
- `python3 scripts/validate_repository.py` in Planning: **passed**, 44 grandfathered warnings and zero new warnings. Existing warning paths concern earlier repository content.
- `git diff --check` in both repos: **passed**. New generated Markdown/CSV/JSON were also checked for trailing whitespace. Supplied source bytes retain their original formatting.
- Focused source/coverage/link verification: **passed**. The machine-readable receipt gives the final local-link count and file scope.

## Learner evidence and ownership

Six pre-existing progress/assessment files remain byte-identical, including the private concept-progress metadata and existing attempt/form/readiness/coverage records. The next undelivered concept remains **CEH26-M05-C04**. Existing question forms and learner IDs retain their own versions. The practice-bank check's local fixtures are material validation, not learner execution.

The archive and technical detail stay in CEH. Planning mirrors the locator, source-preparation outcome, unchanged capacity boundary and next gate. No personal minutes, first answers, understanding, concept delivery, new quota, accepted practical work or official readiness is inferred. At the initial validation, changes were local. The [November 9 integration and publication receipt](../../docs/2026-11-09-first-principle-closeout.md) records subsequent commits, remote-history preservation and fresh checks.

## What this evidence establishes

The supplied material is preserved, comprehensively annotated and connected. Selected primary checks support the specific corrections in the audit. Underlying PDFs, official exam-item authenticity, independent correctness of every supplied key and any future public redistribution retain their stated boundaries. Future formal use of a held item requires a specific repair/review; those conditions do not create new scheduled work.
