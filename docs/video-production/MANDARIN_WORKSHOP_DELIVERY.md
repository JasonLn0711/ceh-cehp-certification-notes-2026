# Mandarin workshop delivery: timing, teaching images and GPU evidence

The shared Mandarin adapter supports the coursework-owned Island Workshop film without changing the legacy Digital Everyday timing defaults. The second film uses the versioned 1.3x voice policy, sample-based 0.45-second quiz holds, guarded quiet-tail trimming and a separate editable diagram profile.

Teaching panels preserve image aspect ratio above the mascot. Cue phrases resolve against provider word boundaries; image hashes participate in build invalidation, including the deck image payloads. Runtime seek checks and encoded-frame samples cover panel transitions. Hardware rendering requires an observed NVIDIA renderer and NVENC execution evidence; a software fallback fails verification. HTML layout, JavaScript, audio and file operations still use CPU.

Validation: 26 Mandarin unit tests pass. Actual v3 delivery: 8 GPU-rendered chapters, 53,577 decoded frames, 135 reviewed frame samples, 40-slide deck and 2,373 archive payload hashes verified. Human full viewing/listening remains pending; no MATLAB execution or YouTube publication is claimed.

Canonical content, source images, editable delivery and receipts remain in the [coursework handoff](../../../nycu-115-1-coursework/cscm30018/review-video-02/HANDOFF-2026-10-22.md). [Planning day note](../../../planning-everything-track/weeks/2026-W43/days/2026-10-22.md#video-handoff-2026-10-22) owns status, capacity and next action. Coursework currently has no Git repository; these sibling links are local workspace routes, not published source copies.

Run the focused checks with the project environment and `PYTHONPATH=tools/ceh_video python -m unittest discover -s tools/ceh_video/tests -p 'test_mandarin*.py'`.

## Storage maintenance — 2026-10-22

New releases follow [long-film storage standard v1.0.0](LONGFORM_STORAGE_STANDARD_v1.0.0.md), engine 0.5.5. Mandarin concept packaging now uses temporary extraction and atomic promotion; MATLAB practice packaging verifies each ZIP member by CRC/SHA without an extraction copy. This maintenance has bounded test evidence and preserves existing film receipts. Current coursework/publication status remains owned by the coursework records.

## Storage and verified reuse — 2026-10-22

New named releases use [long-form storage v2.0.0](LONGFORM_STORAGE_STANDARD_v2.0.0.md), engine 0.6.0. Select `package_format: compact-v1` for exact-byte deduplication and offline restoration. Current source, runtime, output and review hashes govern Mandarin chapter/master reuse; unchanged PCM and hosts avoid rewrites. Voice, timing, image, quiz and human acceptance requirements continue to follow the film's adopted version. Existing deliveries keep their original ZIPs and receipts.
