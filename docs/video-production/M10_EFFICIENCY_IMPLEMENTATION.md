# M10 v1.2 execution and acceptance

## Ownership and sequence

Canonical code/docs: this CEH repository. Raw execution/media: `/home/jnlngx10/Videos/CEH_M10_efficiency_v1_2`. Scarce resources: operator attention and native render time. Planning receives no duplicate raw record. Historical workspaces are preserved; pre-change engine/docs and dirty-state inventory are retained in the new QA directory.

1. Preserve exact request, choices,16 findings and source hashes.
2. Implement independent run timing, longest-first ready-chapter dispatch, archive-only dependencies and manifest-first packaging.
3. Reconstruct all58 scenes with14400-frame sentence gaps; reuse781 processed clips and relative word alignment. Check ten chapter boundaries and eight holds.
4. Render semantic figures for eleven named scenes, then run scoped geometry/candidate review before full QA.
5. Compare fixed30-second topology/resource/quiz workloads at1×4,2×2,2×4 workers, three interleaved trials. Capture source/runtime/environment identity and competing-load limits. Runtime optimization comparisons use the same configuration and pictures.
6. Freeze source and run all required golden/seek/boundary/asset/native QA. Review actual candidate artifacts; no automatic golden promotion.
7. Render one complete new release, inspect encoded samples, measure PCM/AAC, package once and restore without inference.

## Dependency acceptance

| Change | Required invalidation | Preserved |
|---|---|---|
| Packaging implementation | archive plan/write/extraction | speech, alignment, render, audio review, decode |
| One semantic scene spec/cue | scene, owning chapter, master checks | unrelated chapters and spoken PCM |
| Shared renderer/geometry | all consuming visual scenes | speech and clip alignment |
| Pause policy | scene PCM and all offsets/cues | baseline/processed clips and relative alignment |
| One spoken sentence | its clip and downstream consumers | unrelated clip identities |
| QA implementation | its evidence and dependent acceptance | unchanged encoded bytes |

## Tests and evidence

Run Python unit contracts and Node geometry tests. Negative fixtures cover unknown policies, nonzero PCM silence, duplicate chapter pauses, expired asset identity, wrong anchors, out-of-scope legacy exception, stale review, archive symlinks, package-only invalidation and interrupted runs. Valid traces must distinguish real progress from a quiet live child. Tests retain failure evidence.

The full release requires the computed new-time inventory; historical counts558/171/905 are reference coverage, not hardcoded current counts. New geometry, subtitles, fonts and standalone icon identity must pass actual-browser assertions. Full video decode, frame totals,8 quiz boundaries, all-frame audio continuity and165 encoded picture reviews retain independent evidence.

## Status and rollback

Source preserved and decisions adopted. Implementation and the paired excerpt benchmark are tested. Complete new master validation is tested below; archive acceptance is tested in the final local-delivery addendum. No50% or one-hour claim is established by this document. Revert by selecting the prior complete workspace/profile/runtime; keep new attempts and do not merge caches across voice/processing identities. No automatic old-module rerender, remote publishing or destructive cleanup.

## Validation checkpoint and stop/defer list

The first real v1.2 PCM pass verified all 58 scenes: 215,795,200 stereo audio frames (134,872 video frames, 74:55.733333). All 781 clips reused approved processed PCM; new inference and tempo passes were both zero. The initial 93 Python tests and 16 Node geometry tests passed. Later added regression cases require a new suite result. The full 58-scene browser geometry precheck passed.

Representative capture attempt `20261020T081923Z-e0b69ac2` remains failed: 134 screenshots had no individual geometry/seek findings, but two final coverage checks mistakenly applied full-film counts to a selected subset. The harness now derives selected counts explicitly; formal full-release coverage remains independently enforced by `visual_gate.py`. The representative retry passed all 134 captures; the failed attempt and evidence-custody limitation remain recorded. Visual review found an orphaned document corner in S49; the standalone variant now uses approved evidence, AI and review props and omits that card decoration. See `qa/visual-iteration-review-v1.2.json`.

Keep these activities deferred: full-film historical A/B rerender, all-module migration, new voice/model inference, additional ASR accuracy experiments, PixiJS rewrite, online Figma runtime dependency, new font identity, autonomous golden promotion and public publication. They are outside this approved release. Full human listening remains a separate acceptance record. A failed source-bound check blocks the corresponding deliverable; it does not trigger unrelated model generation or archive recreation.

## Stage accounting and attribution

Each `qa/runs/RUN_ID` preserves kind (`migration`, `routine`, `retry`, `delivery`, `benchmark`), parent attempt, UTC events, monotonic elapsed time, node stage durations and a summary. Queue waits are measured from dispatch eligibility to node start. Render wall spans first render start to last render finish; single-job tail is the difference between the last two render completions. Summed stage work can exceed elapsed time because work overlaps. Cache hits report reuse rather than a fabricated stage speedup. Source graph inputs are rechecked at run completion; unexpected changes fail the attempt and require replanning affected nodes.

Closed attempt summaries/events and small logs accompany the editable archive. The active/final packaging attempt remains external, preventing a self-referential archive key. Diagnostic videos, benchmark host trees and local runtime environments are retained in the workspace but excluded from the release archive. The package verifies all twelve restored combined PCM tracks against source hashes as well as the 781 clip cache entries; it performs zero inference and zero tempo operations.

## Pre-render validation checkpoint

- Python: 98 tests passed (6.128 seconds); Node: 16 geometry tests passed.
- Full candidate: 558 captures, zero geometry/seek failures; agent reviewed 124 selected states across all 58 scenes and explicitly approved the initial baseline. Independent golden regression is running at this checkpoint.
- Cross-scene boundary QA: 171 states passed. Asset QA: 905 states passed. All eight injected quiz-divider violations were detected and clean sources restored.
- Thirty-six real excerpt renders completed. Median batch walls: 1×4 204.728431 seconds; 2×2 168.923442; 2×4 144.938315. Adopt 2×4 (14.2% below 2×2 on these three fixed excerpts only). The runtime optimization candidate measured 146.941533 seconds and was rejected; baseline runtime remains active.
- Read-only archive inventory at this checkpoint: 5,817 files, 2,630,789,533 bytes. Final QA artifacts will change this inventory. No heavy staging copy or final archive has occurred.
- Full-film render, encoded review, AAC boundary measurement and archive extraction/restoration are pending. These documents describe a checkpoint; external final run receipts establish completed delivery.


## v1.2 full-composition visual/audio partition

The production index and all 58 compositions remain unchanged. `root_check.py` creates a temporary visual QA host by removing audio elements only, retaining the original head, visual markup, slots, global offsets and GSAP timelines. Native HyperFrames checks every scene midpoint and all eight quiz-hold midpoints (66 times), including contrast, with strict zero warnings. The receipt binds every original/transformed source, runtime, configuration and implementation hash. Delivery rejects changed sources, missing samples, skipped browser checks or disabled contrast. Temporary hosts are excluded from the archive; source-transform and native receipts are included.

This extends the existing visual-only boundary-check approach; it does not claim full-host browser audio playback acceptance. The unchanged production host passed a separate real single-point check in 329.424 seconds. The original all-66-time check hit the native deadline. The visual-only all-66-time diagnostic passed in 98.327 seconds, with 59 contrast objects checked. These are diagnostic observations with different scopes, not a controlled speedup percentage. PCM sample validation, eight exact holds, full encoded-media decode and AAC continuity remain independent mandatory gates. The two earlier SIGTERM origins remain unknown; the traced deadline attempt received no SIGTERM.

## Full-film validation checkpoint — 2026-10-20

`implemented / tested`: run `20261020T100536Z-58bb3af5` verified all eleven newly rendered chapters, the assembled master and encoded checks. Wall time **6995.166090 seconds (1:56:35.166)**; 186 upstream nodes reused. Eleven renders overlap: render window **4982.271554 seconds**, summed render work is reported separately in the run stages. Master assembly plus actual frame counting took **1178.167320 seconds**; full encoded/audio checks **720.574466 seconds**; audio review **27.005647 seconds**. Queue and source-graph overhead remain visible in wall time. Final single-job tail **95.027198 seconds**, last chapter C08; C11 completed third. Historical wall7631.377713 / render6338.707376 / tail1936.212783 seconds yield observed reductions8.34% /21.40% /95.09%. These are different releases, duration and preparation scope, not a controlled whole-film A/B. The50% and one-hour goals remain **not achieved**.

The complete movie is1920×1080/30fps,134872 actual decoded frames,4495.733333 seconds,11 embedded chapters;48kHz stereo AAC. Entire-master decode passed, black intervals0; all215795200 PCM reference frames compared, minimum chapter correlation0.999922 and minimum signal-to-codec-error ratio38.026dB. Eight reference holds remain exactly48000 zero-valued stereo frames. Decoded AAC maximum hold peak0.000028022012; codec tail512 frames, separately disclosed.

All165 encoded pictures were agent-reviewed using20 contact sheets, with S49 and Q03 hold additionally viewed at full resolution. Eight hold samples have no early answer/caption; S49 standalone evidence/AI/review sequence has no detached decoration; S58 complete table shows E01–E04. No sampled clipping/subtitle collision found. This is sampled agent review; full human watching/listening remains pending. Full golden558 states, pixel/seek differences0; boundary171, asset905, native328 states all passed. Final current code:101 Python tests and16 Node geometry tests passed. Root integration strict66 times passed; source inputs remained unchanged through the full run.

Evidence: `qa/production-phase-accounting-v1.2.json`, `production-source-index-v1.2.json`, `runs/20261020T100536Z-58bb3af5/summary.json`, `master-ffprobe.json`, `audio-continuity-audit.json`, `master-aac-boundaries.json`, `encoded-review.json`, `encoded-agent-review-evidence-v1.2.json`, `local-ci-python-v1.2.log`, `local-ci-node-v1.2.log`. First-upgrade QA incorrectly labelled routine in two original attempts is explicitly reclassified only in the reporting view; immutable source labels remain preserved. Uninstrumented coding/review time and the first interruption's exact wall time remain unknown. Sum of overlapping attempts is not total wall time.

At this bundled documentation checkpoint, the complete movie and sampled review are tested; **final ZIP restoration remains pending**. External `qa/final-delivery-closeout-v1.2.json` records the eventual package result without circularly rebuilding the archive. No Git publication/public upload occurred.

## Final local delivery — verified 2026-10-20

This addendum supersedes the pending-package checkpoint. One complete new MP4 and one editable ZIP passed local acceptance; no archive rebuild or full-media rerun was required. Delivery validation run `20261020T120516Z-2af91640` executed only delivery (80.455046 seconds). Release run `20261020T120703Z-7f0be21d` executed only package, reused201 nodes, wall240.591311 seconds; package stage185.818452 seconds.

Archive:6,722 members,6,721 payload hashes,1,818,201,690 bytes; source inventory2,733,577,276 bytes. Heavy pre-package staging0 bytes. Necessary verification extraction2,737,446,685 bytes is separately accounted. CRC during extraction, all payload hashes,165 reviewed encoded pictures and golden-review provenance passed. Restore reconstructed781 clips,12 combined PCM tracks and12 host HTML identities with zero inference and zero tempo operations. Environments remain pinned separately installed dependencies.

- MP4 SHA-256: `a6022560e6cd77f432461157882826b0e89c3500d8645374085740cdc8e3e281`
- ZIP SHA-256: `bdae800b242376b09ee4817270eaa7a3b611eda160e8a2491abb0d072934b825`
- External final receipt: `/home/jnlngx10/Videos/CEH_M10_efficiency_v1_2/qa/final-delivery-closeout-v1.2.json`

The archive intentionally retains its pre-packaging documentation checkpoint; the external receipt and this canonical addendum close acceptance without circular repackaging. Human full viewing/listening remains pending. Performance targets50% and one hour remain not achieved. No Git commit/push or public upload was performed.

| Deliverable | State | Evidence/remaining boundary |
| --- | --- | --- |
| Current-system/performance audit and preserved request | implemented / tested | source hashes,16 historical findings plus new failures/results; unknowns disclosed |
| Production standard v1.1 history and adopted v1.2 | implemented / tested | v1.2 complete movie; historical releases unchanged |
| Audio timing policy and cache/ledger implementation | implemented / tested |58 scenes,781 unchanged clips,eight exact PCM holds |
| Motion tokens,components,layout/geometry | implemented / tested |11 semantic variants,558 golden states,no new exception |
| Rendering architecture and worker choice | implemented / tested |HTML/SVG+GSAP,36 measured excerpt outputs; PixiJS expansion deferred |
| Visual QA and deterministic seeks | implemented / tested |558 states,171 boundaries,905 assets,328 native,165 encoded pictures |
| Migration and rollback | implemented / tested in stated scope |fresh migration fixture tested; actual ZIP reconstruction passed; historical-media hashes preserved |
| Full editable release | implemented / tested |one ZIP,CRC/hash/cache/PCM/HTML restoration passed |
| Additional capture/AAC/decode optimization | proposed |cost subdivision and paired same-quality tests required before changing defaults |
| Human full-film listening/viewing | pending |requires real human acceptance; no substituted claim |
| Historical SIGTERM attribution | blocked on missing attribution evidence |origin unknown; full run signal trace clean |

## Engine 0.5.1 targeted maintenance

[Two targeted fixes and evidence](M10_HIGH_IMPACT_FIXES.md) follow the completed 0.5.0 release: continuous AAC cache for unchanged PCM and one combined full decode. The closed v1.2 release is preserved. Capture-parameter candidates were slower and rejected; no new chapter-render default or whole-film speed claim is made. Source changes and maintenance validation are separate from the completed release evidence above.
