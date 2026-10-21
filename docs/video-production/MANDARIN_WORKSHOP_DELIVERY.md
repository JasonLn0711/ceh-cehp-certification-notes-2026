# Mandarin workshop delivery: timing, teaching images and GPU evidence

The shared Mandarin adapter supports the coursework-owned Island Workshop film without changing the legacy Digital Everyday timing defaults. The second film uses the versioned 1.3x voice policy, sample-based 0.45-second quiz holds, guarded quiet-tail trimming and a separate editable diagram profile.

Teaching panels preserve image aspect ratio above the mascot. Cue phrases resolve against provider word boundaries; image hashes participate in build invalidation, including the deck image payloads. Runtime seek checks and encoded-frame samples cover panel transitions. Hardware rendering requires an observed NVIDIA renderer and NVENC execution evidence; a software fallback fails verification. HTML layout, JavaScript, audio and file operations still use CPU.

Validation: 26 Mandarin unit tests pass. Actual v3 delivery: 8 GPU-rendered chapters, 53,577 decoded frames, 135 reviewed frame samples, 40-slide deck and 2,373 archive payload hashes verified. Human full viewing/listening remains pending; no MATLAB execution or YouTube publication is claimed.

Canonical content, source images, editable delivery and receipts remain in the [coursework handoff](../../../nycu-115-1-coursework/cscm30018/review-video-02/HANDOFF-2026-10-22.md). [Planning day note](../../../planning-everything-track/weeks/2026-W43/days/2026-10-22.md#video-handoff-2026-10-22) owns status, capacity and next action. Coursework currently has no Git repository; these sibling links are local workspace routes, not published source copies.

Run the focused checks with the project environment and `PYTHONPATH=tools/ceh_video python -m unittest discover -s tools/ceh_video/tests -p 'test_mandarin*.py'`.
