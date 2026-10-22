# Initial adopted video production baseline

Adopted 2026-10-20 by the user for current video production. This is the initial **series baseline**, not a reset of historical standard versions. The active English timing contract is [v1.2](PRODUCTION_STANDARD_v1.2.md), with the verified reuse behavior introduced in engine 0.5.3. M11 Session Hijacking is the first new module produced under this adoption; engine 0.5.4 adds module-owned diagrams and inventory-sized validation while preserving the timing/reuse contracts. Its local film and editable archive passed automated and agent visual validation; human full viewing/listening remains separate.

## Identity and content

Keep the M04 Editorial Masterclass v3 hand-drawn editorial style, warm paper palette, approved Liberation Sans / DejaVu Sans Mono fonts, original Tally rig and Northstar Learning Center. Use semantic SVG icons, topology, sequences, packets, timelines, comparisons and evidence figures alongside cards. HTML/CSS/SVG + finite paused seekable GSAP is the default; optional GPU frameworks require measured benefit. New module copy, examples, chapter count and scene count belong to that module's source manifest. M10's 58 scenes and 11 chapters are historical content choices, not universal requirements. Eight original narrated quiz questions remain the English Masterclass contract.

## Executable timing

Select `audio_policy: ceh-en-v1.2`. Preserve Kokoro af_heart/en-US synthesis speed 0.73; apply exactly one `atempo=1.4` to baseline spoken PCM. At 48 kHz stereo, opening = 14,400 frames; sentence gap = 14,400; ending = 24,000; quiz hold = 48,000. Chapter boundary = existing ending + next opening = 38,400 frames (0.8 seconds), with alignment padding separately accounted. Read every question and A–D before its hold, then reveal/read the answer. Eight holds total exactly 384,000 zero PCM frames. Keep picture/animation 1×, music off, 1920×1080 at 30 FPS. Preserve lossless PCM; report AAC residue separately. Other languages retain independent profiles.

## Geometry and evidence

All new/redesigned scenes stay inside x=134.4..1785.6, y=86.4..993.6. Typography measurement, connector anchors, aspect ratios, subtitle clearance and deterministic seeks are release gates. `LEGACY-M10-SUBTITLE-001` applies only to frozen M10 optimization-v1 S01–S58. M11 inherits **zero exceptions**. Goldens require actual inspection and a source-bound review, never automatic acceptance after failure.

## Efficient execution

Use a new workspace; retain historical deliveries. Copy only canonical source/assets/models once, reuse pinned installed runtime locally, and exclude old combined audio, render outputs and QA receipts. Run representative geometry first; only then run full QA. Schedule ready chapters longest-first, independently of presentation order. Reuse speech, encoded chapters, master and QA only when their actual inputs, outputs, runtime identities and current gates match. Preserve explicit force behavior and invalidation on missing/changed evidence. Packaging changes affect packaging checks; changed media affects media checks. Produce one verified final editable archive after content acceptance.

Every attempt records its own run ID, first-authoring / routine / retry / delivery purpose, stage wall time, queue time and final render tail. First-run production and warm reuse are reported separately. The one-hour production goal remains unproven. Full human viewing/listening remains distinct from automated and agent visual acceptance.

[Engine](../../tools/ceh_video/README.md) · [Geometry](LAYOUT_AND_GEOMETRY_RULES.md) · [QA](VISUAL_QA_STANDARD.md) · [Maintenance evidence](M10_HIGH_IMPACT_FIXES.md) · [M11 production](../../notes/m11-session-hijacking/video-production-2026-10-20.md)

## Director-led authoring — adopted October 21

The [director-led workflow](DIRECTOR_LED_WORKFLOW.md) adds user-owned content and narration, assistant-proposed visuals/camera direction, and one whole-film review with explicit scene-level decisions. [Templates and prompts](DIRECTOR_PROMPTS.md) precede expensive production. This is an authoring-policy addition; v1.2 timing and engine versions remain unchanged. Templates and a proposed M11 S06 example are delivered as documents; automatic compilation, new camera support and runtime creative-approval enforcement remain proposed. Existing M11 delivery evidence and human acceptance status are preserved. [Decision and validation](DIRECTOR_LED_ADOPTION.md).
