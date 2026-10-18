# CODEX / HYPERFRAMES: BUILD THE COMPLETE CEH M06 AMERICAN ENGLISH MOVIE

You are the film production engineer, scene animator, voice director, teaching editor, source-integrity reviewer and cybersecurity fact-checker. **Produce the entire complete movie**, not just another outline, not a 1-2 minute user-facing pilot, not a slide-based recording, and do not claim to have rendered a movie unless the MP4 exists and was checked.

## 0. Required reading order

1. `PRODUCTION_STANDARD_v1.1.md`, `STYLE_INHERITANCE.md`, `STYLE_TOKENS.json`, `VISUAL_STYLE_MASTER.md`, `reference/*`: these preserve all M04 v3 production settings and unchanged M05 narration speed, with **only the new 1-second quiz silence override**.
2. `VIDEO_BRIEF_en-US.md`, `COURSE_STRUCTURE.md`, `COVERAGE_MATRIX.md`, `CONCEPT_CONNECTIONS.md`, `GLOSSARY_en-US.md` for accurate M06 teaching content.
3. `chapters.json`, `scenes.json` (authoritative full **8,969-word** speech), `questions.json`, `SCRIPT_en-US.md` (mirror of `audio_segments`), `case/*`, `lab_mock/*`.
4. `VOICE_AND_AUDIO.md`, `production/audio_speed_1_5x.sh`, `production/build_quiz_audio.py`, `production/quiz_hold_contract.json`.
5. `visual_scenes.json`, `EDITORIAL_STORYBOARD_58_SCENES.md`, `CHAPTER_VISUAL_CONTINUITY.md`, `ANIMATION_LAYER_CONTRACT.md`, `VISUAL_QA_CHECKLIST.md`.
6. `assets/mascot/*` (do not redraw Tally), `assets/props/*`, `keyframes/S01.svg` to `S58.svg`, `previews/`, `slides/` editable 18-slide lookbook, `examples/seek_safe_motion`.
7. `RENDER_PLAN.md`, `QA_CHECKLIST.md`, `tooling/validate_pack.py`, `SOURCES.md`.

## 1. Strict invariant M04 editorial art and film setup

Keep original 1920x1080, 16:9, 30 fps, H.264 video/AAC audio, a single clear US-English instructor voice, English labels, en-US subtitles, Northstar campus, Tally non-speaking mascot, warm paper/ink/terracotta, muted paper grain, hand-drawn outlines, original stroke weight, safe margins, native editable diagrams with seek-safe animations. Do not produce flat PowerPoint slideshow footage; the native PPTX is a visual style reference.

## 2. Exact two timing defaults

**Narration 1.5× relative to M04 voice** (already approved for M05) is retained. Choose EITHER verified native TTS rate 1.5 OR standard TTS then exactly one `atempo=1.5` on spoken segments. NEVER apply both; never accelerate the whole video. Measure post-speed audible WPM and reject unintelligible pronunciation.

**New change: silence exactly 1.000 second per quiz question**, replacing 12.000. There are 8 questions, grouped in S54–S57, two per scene. Read every question and A/B/C/D options completely. Insert true digital silence with *all* other audio muted for precisely 1 second; keep the question card and 1-second countdown visible. Only then reveal and narrate correct answer and explanation. Sum = **8.000 seconds true silence**. Other silent reading holds are possible elsewhere but must not be confused with or overwrite quiz contract.

## 3. Course is already authored; DO NOT summarize it away

All 58 scenes contain substantive beginner-friendly paragraphs explaining concept, how it works, flow, a single connected Northstar practical example, evidence limits, implications and defenses. Read **all** `scenes.json.audio_segments` verbatim, including the quiz question/answers and capstone. The English `on_screen_copy` are short intentional labels, NOT substitutes for spoken lessons. Follow unique M06 M05-to-M06 progression. Never accidentally insert M05 original CVE/EPSS questions or M04 enumeration lecture.

## 4. Mandatory safe pedagogical boundaries

The source's Northstar records are fully invented and offline. All simulated terminal/log events must retain the readable `SIMULATED OUTPUT` label. Demonstrations may show READ-ONLY checking concepts and print supplied fixtures. No real target scans, credential spraying, intrusion/exploit chaining, real local credential dumping, keylogger/spyware installation, rootkit development, persistence setup, covert-channel implementation or log deletion. The official CEH curriculum contains these categories, but teaching mechanisms and detecting/protecting them is sufficient for this visual beginner masterclass. If you show any tools, do so as a conceptual interface, not an attack instruction.

## 5. Full production workflow, no user-facing pilot gate

A. Check real installed HyperFrames skill & current CLI workflow (e.g. `/hyperframes` and `/general-video` if installed) and version; verify Node/FFmpeg and local production credentials. Do not assume CLI flags from older releases. Do not purchase paid TTS or acquire external rights without user permission.
B. Make complete 58-scene layered editable HyperFrames project. Follow 1:1 `visual_scenes.json` visual concepts, stable network positions, named rig layers, deterministic seek-safe motion. No static slide parade and no automatic generated text baked into illustrations.
C. Render/synthesize ALL American English speech and 8 true 1-second quiz quiet segments under `VOICE_AND_AUDIO.md`. Establish measured per-clip durations, correct audio alignment, on-screen wording and caption timing.
D. Render/inspect every chapter with internal QA; internal previews are permitted, but DO NOT require user approval of a two-minute pilot before full production.
E. Assemble all 11 chapter MP4s, one continuous full MP4, captions SRT/VTT, licensed asset logs, source project, track ledger, rendered-media manifests, and actual ffprobe QA. Resolve factual, spelling, scene-cut and audio-level errors before calling the film complete.

## 6. Acceptance / no false completion

58 full scenes, 11 full chapters, 8 MCQs, 8 *1.000 second* digital-silent audio gaps after choices, plain American English everywhere in finished footage, 1.5× spoken narration ONCE, stable M04 v3 aesthetic and Tally, meaningful motion, safe claims, readable simulated-output labels, faithful captions, 1920x1080/30fps H.264/AAC complete MP4. If any cloud service, TTS licensing, quota or runtime tool blocks actual export, do ALL independent work and report the exact blocker; do not fabricate an MP4 or a completed voice track.
