# Audio and caption review

All 58 final scene WAV hashes match independent unprompted base.en recognition and known-text forced alignment. Full canonical caption coverage is verified separately; ASR output never substitutes for the approved script. Scene waveforms have no clipped peaks, and eight inserted PCM holds contain exactly 1 second of zero-valued samples.

Reviewed the complete difference list in audio-review-diagnostics.json. Most differences are number formatting, proper-name spacing, acronym spelling, or the deliberate SIM→“simulated finding” pronunciation expansion. A focused 12-clip, unprompted small.en beam5 recheck supports the intended “mistake,” “safe next check,” “a known exploited issue,” “database,” “permitting,” “mature,” “overreacting” and “applicability” readings where base.en differed.

Residual diagnostic uncertainty remains: S47 sentence3 is recognized as “tracks” in place of “checks” by both models; S40 sentence6 varies between the correct “If a line” and “Zifa line”; S19 sentence10 varies around the brief “It is” transition. These are pronunciation/recognition review points, not proven source omissions. The canonical text remains intact in input and displayed captions. No end-to-end human listening or pronunciation-accuracy score is claimed.

The 100 retained forced-alignment flags mark low-probability or zero-duration word estimates, often acronym or short-function-word boundaries. Captions display complete phrases with valid nonoverlapping intervals; flags remain available for fine human timing review. Automated structural checks do not establish human listening acceptance.

Evidence: audio-review-diagnostics.json; speech-targeted-recheck.json; speech-small-targeted-recheck.json; recognition/S01.json throughS58.json; project/data/forced-alignment/*.json; audio-structure-audit.json. The small.en diagnostic model was downloaded for focused QA and is not part of the production voice or packaged runtime models.
