# v1.2 implementation addendum

v1.2 changes only in-scene sentence gaps to14400 frames. Ten chapter intervals reference existing ending24000+opening14400; alignment padding remains separate. Eight quiz holds remain48000 each. Spoken clips and clip-relative alignment are reused by identity; all absolute offsets are rebuilt.

Status: implemented changes under validation; see [v1.2 standard](PRODUCTION_STANDARD_v1.2.md) and [execution evidence](M10_EFFICIENCY_IMPLEMENTATION.md). Historical evidence below applies only to its named release.

# Audio timing policy v1.1

## Full-remaster audio custody

The full-remaster workspace reuses the earlier validated 1.4× raw/processed cache and matching alignment identities. New-workspace verification is **tested**: the sample audit passes, and the actual 117-node audio-review execution reused all 781 clips and 58 alignments with zero new Kokoro inference. Its audio metadata hashes are identical to the verified 1.4× baseline. Continuous-master AAC measurement is now complete after actual encoding. All 212,363,200 reference stereo frames were compared; 64 decoded tail-padding frames are separately disclosed. All eight hold reports include nonzero sample counts, peak and RMS. Peak hold residue reaches 0.8431297 PCM16 units; this is measured lossy residue, not zero-valued PCM.

Keep 212,363,200 stereo frames and 132,727 video frames (73:44.233). A visual edit changes scene receipts only. If a cache recipe or raw hash fails, stop and diagnose its provenance instead of accepting old 1.5× processed media. Active voice-calibration metadata must be generated from `ceh-en-v1.1`; the original calibration record remains in the historical source package.

The eight earlier scene-level AAC residue measurements are historical evidence. The remaster separately decoded its completed master MP4 and reported residue at all eight holds in `qa/master-aac-boundaries.json`. Exact zero PCM and AAC boundary measurements remain separate acceptance records. Human listening dispositions remain pending until actual listening.

### Current technical review and listening boundary

`qa/asr-availability-minimum.json` records one actual fixed-runtime clip inference as `LIVE_MINIMUM_COMPLETED` in `availability_validation` mode. Its transcript is `qa/recognition/availability-S01-001.json`. Full-film transcription was not executed; ASR accuracy and timing remain `not_evaluated`. `qa/audio-technical-triage.json` checks all 781 clips with zero technical defects. Forced alignment contributes 161 flags across 142 clips, and the context-linked audition queue contains 478 pending listening items. These flags are review leads, not confirmed speech errors. `qa/audio-review-diagnostics.json` and `qa/audio-audition/manifest.json` retain the scope and identities. Human listening acceptance remains pending.


Actual master checkpoint: `CEH_M10_Denial_of_Service_en-US_Editorial_Remaster_v1_1_1_4x_1s_master.mp4` is 1920×1080 at 30 FPS, 132,727 frames / 73:44.233. SHA-256: `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`. `qa/run-checks.json` is verified; full decoding found zero black intervals, and all 212,363,200 reference audio frames passed continuity comparison. All 165 encoded sample pictures passed artifact-bound agent review: `qa/encoded-review-coverage.json` binds the three inspection receipts and `qa/encoded-review.json` records the actual CLI review against the current master and all 165 hashes. ZIP extraction verification passed. Human viewing/listening remains pending.

### Earlier engineering-run policy and evidence

The completed tests described below belong to `CEH_M10_motion_v1_1`, engine 0.3.0. The executable policy is retained by engine 0.4.0.

Status: **implemented / tested** for all 58 M10 scene PCM tracks. The executable authority is `tools/ceh_video/ceh_video/audio_policy.py:4–19`; profile selection is explicit. Mandarin cannot enter this policy.

At 48,000 Hz, opening=14,400, sentence gap=9,600, ending=24,000 and quiz=48,000 stereo audio frames. Eight quiz intervals total 384,000 frames. A video frame is 1,600 audio frames. `speech.py:70–121` records contiguous integer-frame entries for opening, spoken, gap, quiz, ending and frame alignment. Padding before a quiz and after the ending is independently recorded, always 0–1,599 frames. No sentence gap is inserted across a quiz hold.

The approved Kokoro baseline remains af_heart / en-US / synthesis speed 0.73. Baseline PCM is 24 kHz mono PCM16; the postprocessed reference is 48 kHz stereo PCM16. FFmpeg receives baseline PCM and exactly one `atempo=1.4` filter. There is no video speed filter, no silence speed filter and no WPM-driven adjustment.

## Cache and provenance

`baseline_recipe()` includes canonical/resolved text, voice, language, baseline speed, model hashes, runtime provenance, gain policy and PCM format. Historical synthesis runtime is explicitly `historical-runtime-unrecorded`; the currently installed runtime is not misrepresented as historical provenance. An imported baseline requires the old cache receipt, raw hash, approved metadata and raw format to agree. The import records source receipt and metadata hashes.

The processed recipe separately includes baseline identity, target atempo, application count, output format and FFmpeg identity. A 1.5× processed cache entry cannot satisfy a 1.4× recipe. Model inference is lazy and occurs only when an eligible raw baseline is unavailable. All 781 references were imported and processed from baseline without new inference in this execution.

`speech` graph keys include policy and implementation identities. `seed_audio()` explicitly refuses to certify historical audio/alignment as current v1.1 output. Old node receipts and alignment files are excluded from migration. Downstream alignment uses the new processed hashes, and captions, narration anchors, chapter timing and quiz reveal points must be regenerated.

## Executable acceptance

```bash
PYTHONPATH=tools/ceh_video "$CEH_PY" -m unittest discover -s tools/ceh_video/tests -v
PYTHONPATH=tools/ceh_video "$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain engineering --stage audio
PYTHONPATH=tools/ceh_video "$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain engineering --stage verify-audio
```

Set `CEH_PROJECT` and `CEH_PY` using [migration commands](MIGRATION_AND_ROLLBACK.md). `test_audio_policy.py` includes real FFmpeg tone fixtures, eight exact holds, invalid speed/application rejection, legacy cache isolation and corruption of one sample. `engineering.verify_audio()` validates the real integer ledger, zero-valued named buffers, hashes, options before each hold, and 30 FPS alignment. Evidence: `qa/audio-policy-v1.1.json`, `qa/audio-rebuild.json`, `output/master.reference.pcm.wav` in the new workspace.

Measured total: **212,363,200 stereo frames / 132,727 video frames / 4,424.233333… seconds**. This is the lossless reference duration, not a claim that a full master MP4 was rendered. Caption/alignment and visual acceptance are separate gates.

AAC is lossy. Its decoded boundary report must be stored separately with encoder settings, decoded frame count, nonzero sample counts and peak residuals around each hold. Zero-valued PCM does not establish zero-valued AAC boundaries. The eight quiz scenes were independently AAC-encoded and decoded: each hold contains residual nonzero samples, with peak magnitude 1 PCM16 unit. The separate `qa/aac-boundary-report.json` records 1,266–2,972 nonzero channel samples per hold. Full-master AAC measurement remains **proposed** until that output is encoded.

Final local delivery: the master is 207,412,180 bytes, SHA-256 `d61b48ae4f2044c30dd9aa646026e90383eae593494d29ec21d11fe1e6d974e9`; `CEH_M10_editorial_remaster_v1_1_EDITABLE.zip` is 3,707,042,054 bytes, SHA-256 `4f5d3e5a2a82672466cd0830fc02a16a39a14d571810aef13f1bca9976b7264e`. `qa/engine-packaging.json` verifies ZIP CRC, extraction, 8,369 files and 8,368 payload hashes, including 165 encoded pictures and the cited golden-review receipts. `qa/engine-extracted-reconstruction.json` confirms 781 restored clips with zero inference and zero tempo passes. `qa/encoded-review-revalidation.json` confirms the same master and all 165 reviewed picture hashes after the conservative check rerun.

Project documents inside the ZIP retain their honest packaging-time checkpoint. These final repository records and the external receipts establish completed archive acceptance; the frozen project, staging tree and ZIP were not rewritten. Human listening remains pending for 478 items; the one-clip ASR run establishes minimum availability only, with full-film accuracy/timing `not_evaluated`.
