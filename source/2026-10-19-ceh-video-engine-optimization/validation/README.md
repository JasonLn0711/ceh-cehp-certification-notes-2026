# M10 engine validation layers

[Canonical rollout](../../../docs/video-production/M10_ENGINE_OPTIMIZATION.md) owns the decision, detailed plan and measured closeout. The maintained [engine guide](../../../tools/ceh_video/README.md) owns execution.

| Layer | Actual evidence |
| --- | --- |
| Regression | [35 tests](unit-tests.txt), including receipt corruption, non-M10 IDs/metadata, stale review, cancellation and archive scope |
| Model/cache fixtures | [Six scenarios and two real fixture TTS inferences](live-integration.json); [0.8.174 actual browser recheck](live-browser-upgrade.json) |
| Early failure | [Five actual preflight scenarios](live-preflight.json), including palette, anchor and quiz overflow before expensive work |
| Relocation | [Original locator unavailable](live-relocation.json); shipped PCM/alignment imports without new inference |
| Fresh dependencies | [Actual clean C11 prepare/capture/render](clean-C11-rebuild.json) |
| Preservation | [6,091 original payloads](baseline-preservation.json); [all 839 production WAVs unchanged](production-audio-preservation.json) |
| Audio review | [781 technical checks, 479 pending listening items](audio-triage-summary.json); [zero new ASR inferences](recognition-refresh.json) |
| Actual media | [Delivery](engine-delivery.json), [complete decode and silence](rendered-artifact-audit.json), [continuity](audio-continuity-audit.json), [encoded agent review](encoded-review.json) |
| Resume/reuse | [Nine chapter results retained](resume-evidence.json); [202 nodes reused, zero executed](unchanged-build.json) |
| Package | [CRC/extraction/5,705 payload hashes](engine-packaging.json); [production-only scope](engine-archive-scope.json) |

`Cxx-review.json` records current native source/capture hashes and the agent's actual inspection scope. Full captures and media remain local. The encoded review covers mandatory sampled frames; [two additional opening frames](encoded-opening-inspection.json) were inspected at native resolution. [Revalidation](encoded-picture-revalidation.json) binds the final unchanged pictures. [Bundled code hashes](engine-implementation.json) match the maintained engine.

Human listening, pronunciation accuracy, learner progress and public media release retain separate acceptance gates. The original fixed-runtime ASR result is imported/revalidated evidence; this rollout generates no new production speech or ASR inferences. The two real TTS inferences belong only to the isolated cache fixture.
