# M06 audio and subtitle review

Reviewed on 2026-10-18, Asia/Taipei. All 58 final scene WAVs have independent, unprompted local base.en recognition reports whose audio hashes match the actual files. Canonical text, rather than recognition output, drives the complete subtitles. This is machine-assisted speech/caption QA; it does not claim full human listening acceptance or a pronunciation-accuracy score.

## Speech identity, speed and coverage

The approved local Kokoro af_heart American English voice uses baseline speed 0.73 and exactly one atempo=1.5 pass on each of 697 spoken clips, then resampling to 48 kHz stereo. Canonical coverage is 8,969 words. Measured baseline speech is 4738.581333s; post-speed speech is 3162.745250s, yielding 170.149651 raw-clip WPM, including the model’s natural edge padding. A separate signal-duration estimate excludes only leading/trailing low-level windows (10ms RMS at −50dBFS, with 10ms guards), retaining internal pauses: 173.192412 WPM. Sensitivity at −60/−40dBFS gives 172.525006/174.042691 WPM. Every measured clip hash and threshold result is preserved in speech-rate-measurement.json. This calculation changes no audio samples; the single 1.5× operation remains the controlling speed invariant. Reading holds and quiz zero buffers are outside the speech transform. No BGM, paid voice service or external voice upload was used.

Known-text Whisper attention/DTW word alignment was run on the processed clips. There are 97 diagnostic flags: 53 zero-duration word alignments and 44 low-probability alignments. Short function words, acronyms, technical terms and numeral labels account for many of these flags. They indicate timing uncertainty; they are not established missing words. Phrase captions retain every canonical word and their intervals are validated separately. Inspect audio-review-diagnostics.json for every flagged word and recognition difference.

The minimum normalized character-similarity diagnostic across the 58 unprompted scene reports is 0.990086. This is neither WER nor an independently annotated accuracy measure. Common differences include number formatting, Northstar spacing, Maya/Meyer, spelling of spoken acronyms and option letters.

## Targeted ambiguity checks and one enunciation repair

A separate cached small.en model at pinned revision d1d751a5f8271d482d14ca55d9e2deeebbae577f was used without a canonical prompt on selected final clips. Its file hashes are recorded in speech-targeted-model.json; it is an optional diagnostic model, separate from the packaged base.en production aligner.

The first 14-clip check resolves the substantive recognition disagreements in S08 (“Imagine three”), S09 (“Knowing”), S14 (“prevent”), S30 (“Deleting”), S47 (“lead”), S48 (“installed”), S51 (“cite a source”) and S54's authentication-check sentence. S12's “A salt” is still transcribed as the homophone “assault” in one sentence, while the following sentence correctly recognizes “The salt is not a secret key.” S39's steganalysis is recognized with split or phonetic spelling. Some A/B option labels also remain inconsistently transcribed. These stay explicit listening-review priorities rather than being silently rewritten in captions.

The follow-up four-clip quiz/capstone check resolves S57's report wording and S58's negated claims. Both models initially merged S56's “What should the team conclude?” into “Watch”. A synthesis-only comma after “What” separates those consonants while preserving every canonical word, the same voice, baseline and single 1.5× transform. Only S56 sentence 13 changed; its other 20 spoken clips are hash-identical. The final processed clip is byte-identical to the correctly recognized candidate, and a fresh unprompted small.en check recognizes the exact question. The complete regenerated S56 base.en recognition also matches canonical text (similarity diagnostic 1.0). Source and caption wording stay unchanged. See speech-enunciation-correction.json and speech-final-prompt-recheck.json.

## Silence and final review scope

Each quiz hold is a dedicated 48,000-frame stereo zero buffer, untouched by tempo processing. The assembled reference PCM and final AAC windows have separate sample checks in the audio-structure and encoded-artifact reports. Final AAC is assessed as lossy compression; boundary residues are measured and disclosed, not called bit-exact decoded zero.

Full human end-to-end listening acceptance remains Jason's next gate. Prioritize S12, S39, the short A/B quiz labels and the listed alignment flags if timecoded corrections are requested. No learner answers, study minutes or practical acceptance are established by this production QA.
