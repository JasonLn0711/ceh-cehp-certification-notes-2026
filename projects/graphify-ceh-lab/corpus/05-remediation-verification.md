# Remediation verification

## Remediation Plan

Remediation Plan specifies the proposed correction, responsible role, expected
result, and verification conditions. Remediation Plan requires Verification
Record. For this fictional case, collecting missing evidence comes before
selecting any correction.

## Verification Record and Comparable Retest

Verification Record captures what was checked and the observed result.
Comparable Retest preserves relevant observation conditions so the reviewer can
interpret a before/after comparison. Comparable Retest supports Verification
Record, which informs Closure Decision. Closure Decision remains pending here:
no real assessment, correction, or retest has taken place.

## Inference Review

Inference Review checks a graph relationship against the sentence that supports
it. EXTRACTED means the relationship was stated in the input; that input can
still be a synthetic example or an incorrect claim. INFERRED marks an added
interpretation. AMBIGUOUS marks uncertainty. Confidence tags describe extraction
confidence, not the probability that a system is secure.

## Sources

The verification-record structure is original teaching design informed by
[NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final)'s assessment and
mitigation scope. Confidence categories follow the
[pinned Graphify extraction specification](https://github.com/Graphify-Labs/graphify/blob/041771be72229bb2c8d8205b9cc6871c6be52b91/graphify/skills/codex/references/extraction-spec.md).
Sources checked 2026-10-14.

## Review Gate

Review Gate is an original synthetic workflow rule added to exercise semantic
updates. Verification Record feeds Review Gate. Review Gate requires a human
source check before Closure Decision. The gate remains pending in this example.
