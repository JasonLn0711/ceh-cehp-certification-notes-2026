# Long-form production/storage round two — 2026-10-22

Canonical owner: CEH shared engine and validation; coursework retains lesson content and original acceptance. Large artifacts remain under `~/Videos/longform-round2-2026-10-22/`. Planning holds only status, capacity and locators. Standard: [v2.0.0](../../LONGFORM_STORAGE_STANDARD_v2.0.0.md); engine: `0.6.0`; timezone: `Asia/Taipei`.

## Completed archive verification

[Archive results](archive-results.json) record `LIVE_FULL_COMPLETED`, valid runtime and passed gates for three complete historical payload sets. Original ZIP SHA-256 values were verified before and after each conversion. Every restored payload was checked; all disposable extraction trees were removed.

| Same historical payload set | Original ZIP bytes | Compact ZIP bytes | Saved bytes | Restored payloads |
| --- | ---: | ---: | ---: | ---: |
| CEH M10 efficiency v1.2 | 1,818,201,690 | 1,762,746,770 | 55,454,920 | 6,722 |
| MATLAB concepts v3 | 1,662,799,212 | 1,120,162,276 | 542,636,936 | 2,374 |
| MATLAB practice v1 | 870,162,406 | 669,052,765 | 201,109,641 | 1,036 |

These compare complete unchanged historical payload sets. Compression/container overhead also contributes to the ZIP-size difference; duplicate logical bytes are separately recorded. Baseline and processed voice bytes remain distinct whenever their hashes differ. Compact experimental ZIPs are retained outside Git alongside their restore scripts and SHA files; the original releases remain unchanged.

The [current English route](english-route-result.json) additionally verified 7,831 payloads, reconstructed 781 audio clips with zero new inferences and zero tempo passes, and verified 12 host PCM hashes plus 12 normalized HTML identities. Its ZIP is 2,671,067,191 bytes. This new ready-to-edit package includes chapter hosts and combined PCM omitted by the old English format, so its payload scope is larger; its size is not an equivalent-payload compression comparison. This is the storage cost of the selected one-step restoration behavior.

The archive comparison records package-plus-full-restore wall time and a 0.5-second sampled allocation peak. Peaks include the validation harness's historical source extraction and English cache reconstruction, exclude directory blocks, and are sampled observations rather than exact peak bounds. The production writer itself uses direct source references and creates no source staging tree.

[English route attempt 1](english-route-attempt-1.json) was interrupted during harness setup because unrestricted `copytree` followed QA runtime links. The producer had not started. All files created by that attempt were removed; original sources were untouched. Attempt 2 used the curated package inventory and passed. Its validation-only QA and media copies were then removed. The first attempt's [trace](english-route-attempt-1.log) and [script](english_route_attempt_1.py) remain historical evidence; the corrected runner is [english_route_validation.py](english_route_validation.py).

## Verified old-copy cleanup

[Cleanup results](cleanup-result.json) record 40,839 complete ZIP/tree file comparisons across seven exact candidates. Two staging trees were removed, totaling **12,032,425,984 allocated bytes (11.206 GiB)**. All **8,694 protected file hashes** matched after removal. No official ZIP or unique source was removed.

| Workspace | Exact output directory | Outcome |
| --- | --- | --- |
| `CEH_M06_v1_1` | `project_source` | Preserved: delivery report dependency |
| `CEH_M07_v1_0` | `project_source` | Preserved: delivery report dependency |
| `CEH_M08_v1_0` | `project_source` | Preserved: delivery report dependency |
| `CEH_M09_v1_0` | `project_source` | Preserved: report and audio audition dependencies |
| `CEH_M10_v1_0` | `project_source` | Preserved: report and audio audition dependencies |
| `CEH_M10_optimization_v1` | `engine_project_source` | Removed after full verification |
| `CEH_M10_editorial_remaster_v1_1` | `engine_project_source` | Removed after full verification |

The filesystem free-space increase during this batch was **4.172 GiB**, affected by concurrent archive/native validation and unrelated activity. It is distinct from removed inode allocation. Recovery uses the retained ZIP and its original `engine_project_source/` prefix, recorded in each item. Restore into a new directory, verify the original archive SHA, and retain the original receipts as historical evidence.

The [producer-reference audit](producer-staging-references.txt) and [accessible-process audit](process-usage-audit.json) supplement exact-tree hashes, incoming-link inspection, lsof and exclusive producer locks. Unreadable/exited `/proc` entries and unrelated filesystem namespace warnings remain recorded visibility limits. M05 without a mapped ZIP, clean-C11/test workspaces and the named M11 historical partial were outside the allowlist.

## Native excerpt validation

[Native run evidence](media-results.json) records actual HyperFrames/NVENC execution for S01 and S05 from the existing Mandarin concepts lesson: 82.333 seconds, 2,470 frames, a teaching image and quiz hold/reveal. Voice bytes, output resolution, fps, encoder, browser and four render workers are fixed. No new TTS or full-film render is involved.

The comparison deliberately re-dispatches host/render/master/QA actions, representing an upstream QA-only invalidation. It is not a comparison against the baseline graph's ordinary unchanged-input no-op. Cold means no successful encoded reuse receipt, not an OS-cache flush. Other machine workloads remained active; measured times are observations for this excerpt, not isolated throughput estimates or full-film forecasts.

The [sampled encoded review](excerpt-encoded-review.json) covers seven encoded frames. The [contact sheet](excerpt-encoded-contact.jpg) shows the teaching image and neutral quiz hold followed by answer C. This is agent review of sampled states; full human listening/watching remains separate.

The native experiment finished with `LIVE_FULL_COMPLETED`, valid runtime and passed gates. Three warm pairs preserved both SHA-256 and modification time for the optimized chapter and master. All seven encoded PNG samples match the baseline exactly. The local-change case adds an HTML comment: it changed the source identity and triggered a real chapter encode; the resulting encoded bytes stayed identical, allowing the master to remain reused. No visual-content-change speed claim is made.

| Re-dispatched stage | Baseline median seconds (3 pairs) | Optimized median seconds (3 pairs) |
| --- | ---: | ---: |
| Host + timeline assembly | 0.448 | 0.397 |
| Chapter render / verified reuse | 188.804 | 1.042 |
| Master assembly / verified reuse | 11.398 | 1.175 |
| Audio and encoded-frame QA | 16.513 | 8.637 |

Times include Python process startup. Host work at this excerpt size is dominated by startup and hashing; no general host-speed improvement is inferred. Cold rendering took 196.336 s for baseline and 202.909 s for optimized. The main benefit is avoiding unnecessary re-encoding after re-dispatch, with current QA retained.

Preparation first failed because the isolated fixture omitted the `scripts` cue directory. The [first attempt](media-prepare-attempt-1.log) and [original preparation script](media_prepare_attempt_1.py) are retained. The cue directory was restored from the source workspace, native checks/captures were rerun, and the captured states were inspected. The [corrected preparation runner](media_prepare.py), [stage runner](media_stage.py) and [comparison runner](media_validation.py) preserve the procedure. Existing run directories and result files deliberately refuse an automatic rerun.

## Final validation and storage boundary

[Closeout](validation-closeout.json): **190 tests passed**, all 36 native stage-log hashes verified, final current chapter/master reuse identities and graph guards passed, original scene-audio hashes and the excluded M11 partial hash were preserved. All verification/extraction scratch directories are gone. Existing `force_align.py` ResourceWarnings are recorded in the passing test log.

[Final inventory check](final-compact-inventory-check.json) confirms that new English compact delivery includes 1,054 chapter-host payloads and 24 combined-audio files and reports its exclusions accurately. Later refinements to reconstruction capacity reserves, no-clobber publication/rollback, live graph runtime guards and missing-frame invalidation passed the final regression suite. The large ZIPs are validation snapshots, not newly published releases.

Retained experimental ZIPs, native excerpts, baseline engine snapshot and logs occupy **6.221 GiB** of allocated space, including directories. This retained verification evidence is separate from the **11.206 GiB** of old duplicates removed. The interrupted harness's large runtime copies were removed completely. Source media, production releases and the five dependency-bearing folders remain available.

The [engine change manifest](engine-changes.json) distinguishes this round's changes from the dirty workspace that already existed. No Git commit or publication was performed. Next production gate: create a named release with `compact-v1`, use its existing content/human acceptance requirements, and retain its package receipt. The five preserved old trees need a separate dependency migration or verified archival move before reconsidering removal.

[Documentation checks](documentation-validation.json) passed for 124 relative links and all JSON evidence. Planning knowledge validation passed for 181 metadata notes and 181 catalog entries; both repository diff checks passed.

## Planning connection and publication scope — 2026-10-22

[Day record](../../../../../planning-everything-track/weeks/2026-W43/days/2026-10-22.md#longform-storage-2026-10-22) · [CEH project](../../../../../planning-everything-track/data/projects/2026-07-ceh-cehp-certification-training.md#longform-storage-2026-10-22) · [Coursework project](../../../../../planning-everything-track/data/projects/2026-09-cscm30018-teaching-assistant.md#longform-storage-2026-10-22).

The later publication request activates separate source, implementation, standards, evidence and Planning commits. Earlier “no Git publication” statements describe their execution snapshots. Heavy media and the non-Git coursework directory remain local. Next production activation belongs to a named release and its existing human acceptance gates.

Publication checkout validation: [170 tests passed](publication-validation.json) after excluding unrelated M11/module and practice-video authoring changes. The earlier 190-test result belongs to the full working tree. Current package/reuse tests pass independently; the native measurements above retain their original implementation fingerprints.
