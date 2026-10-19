# CEH video production standard v1.0

Adopted 2026-10-18, Asia/Taipei. Jason approved the M04 Editorial Masterclass v3.0 visual system as the initial CEH series standard. The latest timing decision is **1.5× American English narration only and exactly 1.000 second of true silence after each of eight quiz questions**. This document reconciles the earlier 12-second wording with the later explicit correction. Historical M04–M06 source records remain intact.

## Purpose and design ownership

Produce complete, connected English teaching that explains principles, mechanisms, procedures, cases, defenses, and evidence limits. Use simple American English for narration, visible instructional text, questions, choices, and captions. A complete module has no arbitrary runtime ceiling. The current masterclass package structure is 11 chapters and 58 scenes, including eight graded multiple-choice questions and an integrated capstone. Module content must be written for its own subject.

Preserve the approved warm paper hand-drawn editorial design, original Tally notebook character, Northstar Learning Center campus, device identities, colors, and layered assets. Reuse original artwork rather than recreating the mascot. Carry provenance and integrity hashes for the locked assets. Build mechanisms with editable text, objects, and meaningful relationships; use narration-timed animation to explain them. Static source boards establish design intent, while final animated scenes require actual runtime evidence.

Output is 1920×1080 at 30 fps, with the original safe areas and palette in `STYLE_TOKENS.json`. Keep captions clear of diagrams. Preserve native SVG text/geometry and editable presentation text/shapes. Typography must remain readable at normal playback size. Use approved locally installed or licensed fonts and record fallbacks and licenses.

## Voice, speed, and time

The approved local M06 voice baseline is Kokoro `af_heart`, en-US, synthesis speed `0.73`. Apply exactly one FFmpeg `atempo=1.5` operation to each spoken clip. This is the adopted implementation of 1.5× narration relative to the approved baseline. Keep video, animations, reading holds, and silent buffers at rate 1.0. Do not accelerate the full film or apply the speech speed twice.

The inherited 115–130 baseline WPM and 172.5–195 effective WPM ranges are editorial estimates. A final delivery reports actual spoken word count and measured audio duration. If reporting a signal-based WPM estimate, state the threshold, window, guards, and treatment of internal pauses separately from raw clip WPM. Do not reuse another module's measurements or alter the approved speed merely to force a target WPM.

Generate the complete canonical script, including every question, option, answer, and explanation. Synthesis-only pronunciation or punctuation interventions must preserve the canonical meaning and have an explicit record. Keep original clips, processed clips, and source fingerprints distinguishable. Background music is off by default.

## Eight quiz holds

For each question, narrate the full stem and A–D choices before the hold. Insert exactly **48,000 stereo audio frames of zero-valued PCM at 48 kHz**, lasting **1.000 second**. Eight questions therefore contribute exactly **8.000 seconds** of authored quiz silence. Reveal and narrate the answer after the hold. Reading or animation holds must not be inserted inside this measured quiz interval. Learners can pause playback for more thinking time.

Maintain a question-to-scene mapping and a sample-accurate timeline. Validate both forward and backward seeking at the question, hold, and answer boundaries. Distinguish reference zero PCM from a decoded lossy deliverable. H.264 video with AAC audio remains the approved final MP4 profile; report any measured AAC boundary residue separately instead of claiming bit-exact decoded zero. Preserve a lossless reference mix when producing the final film.

## Source package and full-film workflow

A production source package contains the complete script, chapters/scenes/questions/visual-scene JSON, all scene boards, an editable visual deck, original shared assets, motion references, fictional or authorized evidence, student work and separate instructor answers, official references, build instructions, and rerunnable integrity checks. Give all counts and word totals from actual files. Preserve the M06 JSON interfaces when extending them.

Use Codex and HyperFrames for the full production workflow. The executable agent prompt requires the complete module, narration, aligned captions, chapter outputs, and final MP4, without a short-pilot approval gate. Internal technical checks can precede full rendering when they resolve an actual implementation risk; they do not impose a new user approval checkpoint.

Author finite, seek-safe motion with local frozen assets. Derive final scene duration from actual speech, explanatory motion, and reading needs. Captions align to the processed speech at its final rate, exclude silent quiz intervals, and cover all spoken content. Chapter/scene boundaries, audio coverage, and source/output fingerprints must be reviewable.

## Evidence and acceptance layers

| Layer | Required evidence | Claim supported |
| --- | --- | --- |
| Adopted specification | Preserved request and this standard | Current production decision |
| Source ready | Complete content, editable assets, schema/mapping, silence, runtime examples, manifest and ZIP checks | Reviewable production package |
| Runtime ready | All actual scene compositions and measured speech/caption timeline pass checks | Full-film render inputs prepared |
| Rendered | Actual chapter/master artifacts, codec/frame/duration checks, complete decode, encoded visual/audio audit | Film rendered with stated automated checks |
| Human accepted | Recorded viewing/listening review and resolved findings | Human acceptance of the reviewed artifact |
| Publicly released | Explicit release action and verified destination URL | Media publication |

Keep these layers distinct. A prompt or source ZIP does not establish generated narration, synchronized subtitles, rendered animation, learner practice, human acceptance, or public release. Report real blockers with the affected stage and next check. Preserve prior evidence when correcting an artifact.

## Scope and stewardship

Use lawful authorized training, toy examples, or clearly labeled fictional evidence. Every invented observation carries `SIMULATED OUTPUT`. Prepared material does not add learner answers, practical acceptance, attendance, Blog completion, or study minutes. The CEH repo owns detailed source decisions and compact evidence. Local `~/Videos/` workspaces own large production assets. Planning owns thin locators, status, capacity, and the next gate.

## Adoption history

| Decision | Current interpretation |
| --- | --- |
| M04 v3 editorial inheritance | Original design, Tally, Northstar, and output settings retained |
| Initial narration change | American English speech alone becomes 1.5× |
| Later explicit silence correction | Every previous 12-second quiz hold becomes exactly 1.000 second |
| M06 implementation accepted for reuse | Local `af_heart` / 0.73 baseline, one `atempo=1.5`, AAC with measured residue disclosure |
| M07 requested delivery | Complete production source ZIP; actual speech, captions, and MP4 remain the next production layer |
| M08 applicability — 2026-10-18 | Same v1.0 standard; newly authored Sniffing source package with synthetic offline PCAPs. Full narration, aligned captions and MP4 are the next production layer. |
| M09 applicability — 2026-10-19 | Same v1.0 standard; newly authored Social Engineering lesson, consent-based no-send cases and complete source plus full-film production explicitly activated. Actual production and human acceptance retain separate receipts. |
| M10 applicability — 2026-10-19 | Same v1.0 standard; newly authored Denial-of-Service lesson, four offline resource/evidence cases and complete source plus full-film production activated. Preserve 1.5× narration only and eight exact 1.000-second PCM holds; actual render and human acceptance require their own evidence. |

## Implementation connection — October 19

The [shared engine rollout](M10_ENGINE_OPTIMIZATION.md) uses M10 as the reference project for audio triage, declared-input reuse, resumable processes and current visual review. Its engine version is separate from this v1.0 editorial contract. Module migrations require their own runtime and artifact evidence; this connection does not alter released M04–M09 packages.
