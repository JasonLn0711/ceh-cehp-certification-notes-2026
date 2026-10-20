# Full M10 editorial remaster — execution evidence

Canonical implementation: `tools/ceh_video/ceh_video/`, engine 0.4.0. Local production workspace: `/home/jnlngx10/Videos/CEH_M10_editorial_remaster_v1_1`. Raw media, image manifests, logs and receipts live under that workspace; this directory holds the compact evidence index. Original releases remain in their existing workspaces.

## Execution plan and acceptance

1. Audit the maintained engine and source package; retain historical v1.0 evidence and approved asset identities.
2. Apply the English v1.1 sample contract, reuse verified baseline PCM, and verify all 781 clips, 58 scenes, eight holds, alignments and timeline outputs.
3. Compile all 58 source-bound scenes with approved fonts/palette, measured text, explicit device identities, constrained cards and absolute-time connectors. Enforce the bottom safe-area boundary at y=993.6.
4. Check native chapter states, every frame of the 50 non-quiz diagram models, every quiz-hold frame, all required screenshot/seek states, asset transforms and all 57 scene boundaries. Review candidates before creating read-only goldens and rerun regression.
5. Render all eleven chapters with the measured worker configuration and verified GPU identity. Assemble the full continuous-PCM/AAC master, decode it completely, measure all AAC hold boundaries, and inspect encoded samples.
6. Package the editable source, engine, local assets, models and provenance; extract the ZIP and verify payload hashes and restoration of all 781 cached clips. Record output identities. Human listening and public release retain separate status.

No failed baseline is automatically promoted. No new scene inherits the historical subtitle exception. Each render/check/package receipt binds its declared inputs and outputs.

## Verified at the current checkpoint

| Layer | Status | Actual evidence |
|---|---|---|
| Python regression | tested | 86 tests passed, including cache isolation, integer timing, geometry gates, GPU probe rejection and packaged-cache restoration |
| JavaScript geometry | tested | 16 tests passed across the original and remaster geometry suites |
| Audio reconstruction | tested | Actual 117-node audio-review execution; zero synthesized clips; audio metadata unchanged from verified 1.4× input |
| Sample contract | tested | 212,363,200 stereo frames; eight holds of 48,000 zero PCM frames, separate alignment padding |
| Protected assets | tested | 905 sampled states; locked hashes, uniform scaling and safe-area checks passed |
| Historical preservation | tested | 46 checks passed, including the original approved master and editable archive |
| Render-worker selection | tested | Eight real ten-second outputs; two paired trials; identical output hashes and full decoding |
| Native chapter review | tested | Eleven chapters, 328 native captures, zero check warnings/errors; agent review explicitly rebound after runtime pinning |
| Full-scene geometry precheck | tested | Final strict endpoint-normal routing: 58 scenes, 2,143 text boxes and 110,721 diagram frames; zero failures |
| Quiz decoration negative control | tested | All eight quizzes reject the injected historical divider; 16 screenshots; production sources unchanged |
| Complete golden regression | tested | 558/558 current-source states pass after artifact-bound candidate approval; strict visual gate passes all 58 scenes, zero exceptions |
| Scene-boundary QA | tested | Final 171/171 states across 57 boundaries pass with unchanged source hashes; direct/forward/reverse/repeated comparisons agree |
| Full master | rendered, tested | `qa/run-checks.json` verified; 132,727 frames, 1920×1080, 30 FPS, 73:44.233; full decode with zero black intervals |
| Continuous PCM/AAC integrity | tested | All 212,363,200 reference frames compared; min SNR 38.091 dB, min correlation 0.99992328; 64 AAC tail frames and all eight hold residues disclosed |
| Complete encoded sample review | tested | All 165 frames pass; three inspection receipts and coverage are bound by `qa/encoded-review-coverage.json`, with actual CLI review in `qa/encoded-review.json` |
| Editable archive | implemented, tested | 3,707,042,054 bytes; CRC/extraction verified, 8,368 payload hashes, 781 clips restored without inference or processing |

The native HyperFrames probe identifies NVIDIA GB10. The Playwright QA probe identifies SwiftShader. Their image/renderer evidence is kept separate. Two concurrent jobs with two workers each improved measured excerpt throughput by 28.24–37.55% against one worker per job on the final frozen source; that result does not establish full-film scaling or a PixiJS advantage.

## Exceptions and review limits

`LEGACY-M10-SUBTITLE-001` covers only the frozen optimization-v1 subtitle reservation in S01–S58, bound to its profile and individual composition hashes. New remaster S01–S58 use zero exceptions. Fonts, narration timing, source text and asset identity have no exceptions.

Human listening remains pending for 478 prioritized items, including 161 alignment flags across 142 clips. The real one-clip ASR availability run has status `LIVE_MINIMUM_COMPLETED`; full-film recognition accuracy and pronunciation accuracy are `not_evaluated`. Agent image review does not establish human full-film acceptance. Remote CI activation, Figma round-trip validation and a no-WebGL Pixi fallback remain outside the exercised local production path.

## Failures retained and corrected

- The first packaging attempt expanded temporary boundary-host media symlinks into approximately 78 GB of generated staging. The owned packaging process was interrupted; `qa/package-attempt-001-expanded-hosts.*` preserves its inventory/log. Generated staging was removed only after confirming its files had link count one. Packaging now excludes only `qa/remaster-boundaries/hosts/`, which the boundary harness regenerates. A bounded copy retained the report and all 171 screenshot hashes in 10,614,019 bytes. The regression test checks real and dangling symlink exclusion, preserved evidence and the narrow directory scope. This corrects archive construction without changing rendering sources or waiving a QA gate.

The retry completed through the ordinary package CLI after conservatively rerunning affected audio/check receipts. `qa/encoded-review-source-rendered-artifact-audit.json` preserves the audit hash cited by the existing picture-review receipts; all 165 regenerated picture hashes and the master remained unchanged in `qa/encoded-review-revalidation.json`. ZIP retry, CRC, extraction and cache reconstruction passed.

- HyperFrames exposed DOM measurement work during timeline updates and hidden packet bounds at the origin. Pure geometry and anchored hidden packets corrected both.
- Browser text ink exceeded the initial font-measurement estimate. An 8 px measurement reserve corrected wrapping while preserving the approved font sizes and strict 0.25 px bounds tolerance.
- The TCP sequence exposed a mismatched node identifier and delayed connector cue. Source-bound timings now reveal SYN, SYN+ACK, ACK and established state in order.
- Device assets previously relied on inferred identity. Explicit original asset paths and provenance now fail closed when missing.
- A diagram badge overlapped quiz content. It is confined to the 50 diagram scenes; quiz wording and timing are unchanged.
- The asset validator caught missing provenance on restored S47 illustrations. Metadata and original hashes now pass.
- Boundary validation detected an authorized S47 source change during a run. The failed attempt remains recorded; only a fresh frozen-source run can satisfy delivery.

- Candidate image review found shared arrow ports that could merge distinct traffic paths. Fixed side/fraction ports, independent route corridors and blocked-terminal corrections now pass the final 58-scene precheck and geometry tests. The explicit variant scope is S05, S06, S10, S12, S14, S23, S26, S27, S31, S32 and S36. Superseded candidates remain preserved; full golden regression now passes; complete encoding now passes; editable ZIP verification passed.

- Full-size S27 review exposed a right-side port whose route initially followed the card border. The current pass was interrupted and preserved; perpendicular endpoint direction, endpoint clearance and reversal rejection were added and independently tested. Fresh full-frame validation passes; the superseded attempt remains preserved.

Actual master checkpoint: `CEH_M10_Denial_of_Service_en-US_Editorial_Remaster_v1_1_1_4x_1s_master.mp4` is 1920×1080 at 30 FPS, 132,727 frames / 73:44.233. SHA-256: `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`. `qa/run-checks.json` is verified; full decoding found zero black intervals, and all 212,363,200 reference audio frames passed continuity comparison. All 165 encoded sample pictures passed artifact-bound agent review: `qa/encoded-review-coverage.json` binds the three inspection receipts and `qa/encoded-review.json` records the actual CLI review against the current master and all 165 hashes. ZIP extraction verification passed. Human viewing/listening remains pending.

Final local delivery: the master is 207,412,180 bytes, SHA-256 `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`; `CEH_M10_editorial_remaster_v1_1_EDITABLE.zip` is 3,707,042,054 bytes, SHA-256 `4f5d3e5a2a82672466cd0830fc02a16a39a14d571810aef13f1bca9976b7264e`. `qa/engine-packaging.json` verifies ZIP CRC, extraction, 8,369 files and 8,368 payload hashes, including 165 encoded pictures and the cited golden-review receipts. `qa/engine-extracted-reconstruction.json` confirms 781 restored clips with zero inference and zero tempo passes. `qa/encoded-review-revalidation.json` confirms the same master and all 165 reviewed picture hashes after the conservative check rerun.

Project documents inside the ZIP retain their honest packaging-time checkpoint. These final repository records and the external receipts establish completed archive acceptance; the frozen project, staging tree and ZIP were not rewritten. Human listening remains pending for 478 items; the one-clip ASR run establishes minimum availability only, with full-film accuracy/timing `not_evaluated`.
