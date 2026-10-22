# Verified extraction-copy cleanup — 2026-10-22

Batch `longform-cleanup-2026-10-22`, policy `longform-storage-v1.0.0`. Status: **completed**. Executed on 2026-10-22 (Asia/Taipei), following the user-approved first-batch plan and explicit “Implement the plan.” instruction.

Only the four exact `output/archive-verification/` directories below were removed. All 9,845 payloads and four manifests matched their retained ZIPs; each ZIP matched its original receipt. The 564 protected output/evidence file hashes matched after cleanup. Original receipts were preserved.

| Workspace under `~/Videos/` | Payloads | Removed allocated bytes, including directories | Result |
| --- | ---: | ---: | --- |
| `Digital_Everyday_Masterclass_v1` | 3,010 | 2,713,825,280 | Removed; protected outputs verified |
| `Island_Workshop_MATLAB_Concepts_v1` | 2,257 | 2,711,347,200 | Removed; protected outputs verified |
| `Island_Workshop_MATLAB_Concepts_v2_1p3` | 2,205 | 2,898,231,296 | Removed; protected outputs verified |
| `Island_Workshop_MATLAB_Concepts_v3_images_gpu` | 2,373 | 2,976,772,096 | Removed; protected outputs verified |

Removed inode allocation: **11,300,175,872 bytes (10.52411 GiB)**. Observed filesystem free-space increase: **11,294,670,848 bytes (10.51898 GiB)**. These figures differ because filesystem activity continued during measurement.

## Verification and preservation

- Acquired the existing exclusive engine run locks and checked the exact targets with `lsof`; no target open handles were observed. `lsof` reported visibility limits for unrelated tracefs/Docker namespaces; those warnings remain in the receipts. No elevated privileges or permission changes were used for cleanup.
- Scanned incoming symlinks across Videos and coursework, excluding `.git`, `.venv` and `node_modules`; none pointed to the targets. Every target entry was checked for symlinks, mount changes, shared inodes, extra files and hash differences.
- Saved preflight evidence before removal; repeated verification immediately before each removal. The one-off runner accepts no arbitrary target paths.
- Preserved project source, adopted voice assets, all formal ZIP/MP4/subtitle/deck outputs and QA outside the four extraction trees. The CEH M11 partial archive in `qa/authoring-history/report-locator-correction/` retained its exact SHA-256; CEH test workspaces were excluded.
- Existing `extracted_root` fields remain historical locations, not assertions that copies still exist. To restore one copy, verify its retained ZIP against the preflight hash, extract into that workspace’s `output/archive-verification/`, and verify `FILES_SHA256.txt`. No TTS or rendering is required.

## Evidence

- [Preflight manifest](preflight.json): exact targets, recovery ZIPs, original receipt locations, all candidate file identities and protected hashes.
- [Execution receipt](result.json): per-target completion, usage-check warnings, protected verification and before/after disk measurements.
- [One-off runner](cleanup.py): default preflight; `--apply` revalidates the approved manifest. The completed batch refuses a second apply.
- [Source authorization](../../../../source/2026-10-22-longform-storage-policy/source.md).

No film was rendered or repackaged. No Git commit or push was performed.
