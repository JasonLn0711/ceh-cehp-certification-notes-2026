# CEH M01-01 detailed CIA lesson — v1.1.0

The existing [Chinese concept page](https://learn.cs-kairos.com/courses/ceh/v13/m01/concepts/m01-01/) and [English page](https://learn.cs-kairos.com/en/courses/ceh/v13/m01/concepts/m01-01/) retain their stable identity. The authorized replacement expands the original summary into nine sections, an Ubuntu hash experiment, two practice questions and three responsive diagrams. Previous bodies remain in Git history. [Public teaching text](../source/2026-10-27-one-concept/M01-01-detailed-teaching.md) · [Stable concept index](../study-plan/core-concept-index-2026-10-27.md).

## Source and editorial verification

The supplied text was read in full: 13,971 bytes; SHA-256 `cf06ababfddc14120ec6c090996c3f8bfdbc0c8c6f5ed77ae978ff9f29b3cc29`.

188 of 191 normalized source blocks remain unchanged. Three ASCII schematics are represented by text-based responsive diagrams and equivalent SVG downloads. All eight code/output blocks remain verbatim; all nine sections and both questions remain in order. Markdown emphasis, heading levels and citation tracking parameters are normalized. Four separately labelled supplements clarify ransomware's integrity impact, signature trust prerequisites, safe file overwrite/one-character change and the absence of automatic grading. No learner answers are fabricated.

The change is MINOR (1.0.0 → 1.1.0): substantial additional explanation and practice within the existing CIA concept, without changing its identity or advancing the route. [Exact normalization manifest](https://github.com/JasonLn0711/kairos-learning/blob/main/docs/releases/2026-10-27-m01-01-detailed-normalization.json).

## Publication evidence

Website [PR #35](https://github.com/JasonLn0711/kairos-learning/pull/35), initially draft; implementation `711e8f8c3733721d8298b98ccf7ece52ab78c3bf`; merge `3e88f85a71c149057e013f9a19aa3f3901e8c5e9`.

- [Quality CI](https://github.com/JasonLn0711/kairos-learning/actions/runs/40469434718): success.
- [Pages deployment](https://github.com/JasonLn0711/kairos-learning/actions/runs/40469550372): success.
- Bilingual content validation, all three tests, Svelte check (zero errors/warnings), publication boundary, release links/anchors and disclosure validation passed.
- Local source-to-HTML check: 277 Chinese text/code/table items found, none missing.
- GX10 Brave: both languages checked at 320/390/1280 px, three figures, eight code blocks, zero teaching disclosures and no document overflow. Keyboard anchor and download-link focus checked.
- Production v1.1.0 read back in both languages on GX10 Brave, including all nine headings, three figures, eight code/output blocks and paired language links. All six viewport combinations checked after refresh; a cached Chinese v1.0.0 navigation required reload before the new version appeared. Remote Git blob hashes match all eight changed files. Direct HTTP SVG verification returned 403 for the first asset, so public asset HTTP retrieval is not marked passed. Local SVG rendering and remote byte/hash checks passed.
- SVG byte sizes (Chinese/English): hash 1957/2026; failover 1515/1524; framework 2296/2312. All below 100 KB. Webpage diagrams reflow; standalone SVGs scale with a fixed viewBox.
- Browser native save/download was not retried because the earlier operation remains approval-pending. Asset availability verification is separate from saving a file.

A small isolated temporary-file experiment confirmed the documented `85` → `95` modification changes the SHA-256 digest. This validation is editor execution evidence, not learner practical completion.

## Primary sources

- [NIST information security](https://csrc.nist.gov/glossary/term/information_security)
- [NIST NCCoE data integrity](https://www.nccoe.nist.gov/publication/1800-26/VolA/index.html)
- [NIST digital signature](https://csrc.nist.gov/glossary/term/digital_signature)

Private delivery identifiers, raw learning notes and understanding states are excluded from this public record. Planning synchronization remains separate from website publication.
