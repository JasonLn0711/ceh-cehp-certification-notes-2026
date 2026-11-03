# M03-05｜Service Version & Banner Grabbing

## Scope and source

One composite unit from the adopted 161-unit route: service-response inference, banner collection, disguise, proxy ambiguity and version misidentification. The complete paired source manuscripts and reference answers are preserved under `notes/m03/`; actual learner questions, answers and understanding records remain separate and private.

The main question is: what evidence identifies the service and version behind an open entry point? The beginner lesson connects a shop-sign analogy to port-name lookup, Nmap service/version probes, the TCP NULL-probe boundary, softmatch, OS-fingerprinting distinction, reverse proxies and vendor backports. The practice is an offline synthetic-evidence exercise; no external target scanning is performed.

[Technical source review](m03-05-source-review.md) records primary documentation and observation/inference limits. The site owns canonical authoring, rendering and release gates. This notes mirror preserves paired public teaching without duplicating private learning status.

## Stable intended pages

- Chinese: https://learn.cs-kairos.com/courses/ceh/v13/m03/concepts/m03-05/
- English: https://learn.cs-kairos.com/en/courses/ceh/v13/m03/concepts/m03-05/

Initial content version: 1.0.0. Editorial revision date: 2026-11-03. First-publication date must match the actual release, rather than a build timestamp. Four reference answers are initially collapsed; body, tables and two relationship diagrams are directly visible. Reference answers are teaching material, not learner submissions.

## Acceptance boundary

Preparation, local static checks, PR validation, successful deployment and actual production readback are distinct evidence stages. Release provenance and observed browser checks will be appended only after execution. Unperformed 320/390/768/1280 CSS-pixel, 200%-text and no-JavaScript browser checks remain pending rather than inferred from static tests.

## Verified production receipt — 2026-11-03

- Website [PR 66](https://github.com/JasonLn0711/kairos-learning/pull/66) merged as `90d76183892a2076aa0ba224f5f55e87cf5a7e47`.
- Exact reviewed head: `cfdcac605982ea16b9f13164d667a533199c63a8`; [CI 41552258832](https://github.com/JasonLn0711/kairos-learning/actions/runs/41552258832) completed/success, including dependency audit high-severity gate, content, tests, type checks, boundary, release and preserved download checksums.
- Validated and merged tree: `01f5aef725ada63af6c155cdc8418b4f7edac6ca`; all 29 changed blobs matched the tested local files and other baseline blobs were preserved.
- [Pages 41552482484](https://github.com/JasonLn0711/kairos-learning/actions/runs/41552482484) completed/success at the exact merge SHA. The deploy-pages step completed at **2026-11-03 00:24:16 UTC / 08:24:16 Asia/Taipei**.
- Actual Cloud Browser readback at approximately 08:25–08:27 Asia/Taipei verified both stable URLs above, v1.0.0, original publication and revision dates 2026-11-03. Each page's 129 ordered expected text items matched the production DOM, including body, table cells, figure captions/nodes, questions and reference answers.
- Local final checks: 132 tests; type check 0 errors/warnings; 552 deployed text artifacts boundary; 272 HTML pages / 361 static assets; exact source order and SVG/ZIP output.

### Page-specific acceptance update

The two stable URLs above are denoted ZH and EN below. These are agent-operated browser observations, not an independent human accessibility certification. Earlier pending descriptions are retained as the preparation snapshot.

| Rules | Language / URL | Size / mode | Result | Evidence |
|---|---|---|---|---|
| WRITE-05–07 / HTML-01 | ZH, Chinese stable URL above | Actual production DOM | Pass within checked scope | 129/129 ordered text items; v1.0.0; both dates11/03; primary sources visible; no private identifiers |
| WRITE-05–07 / HTML-01 | EN, English stable URL above | Actual production DOM | Pass within checked scope | 129/129 ordered text items and matching version/date; bilingual links followed in both directions |
| HTML-02–04 / FIG-02 | ZH + EN, both stable URLs | 1180 CSS px | Pass within observed desktop scope | No page overflow; body16px/line-height28.8px; two direct semantic figures; three code blocks with light rgb(242,246,245), dark rgb(24,37,44), overflow-x:auto and tabindex0 |
| A11Y-02–03 | ZH + EN, both stable URLs | Desktop keyboard | Pass for tested controls | Four answers initially closed; first answer opens with Enter and closes with Space; Tab advances to second summary and Shift+Tab returns; visible3px blue focus outline |
| FIG-03 / release | ZH + EN assets | Production downloads | Pass | Four SVG downloads and bilingual ZIP byte hashes equal validated repository/build files |
| HTML-02–04 / FIG-02 / A11Y-01 | ZH + EN, both stable URLs | 320/390/768/1280 CSS px | Pending | No supported exact viewport-setting capability used;1180px observation is not substituted |
| HTML-02 / A11Y-02 | ZH + EN, both stable URLs | 200% text | Pending | No actual text-scaling browser check executed |
| HTML-01 / A11Y-03 | ZH + EN, both stable URLs | JavaScript disabled | Pending | Static HTML checks passed separately; actual no-JavaScript navigation not executed |
| A11Y-02 / HTML-04 | ZH + EN, both stable URLs | All navigation/download/code-scroll interactions | Partial | Answer keyboard and language links checked; exhaustive keyboard traversal/local-overflow scrolling remains pending |

The available Cloud Browser was used directly for the requested live page verification. Previously denied local Chromium or shell HTTP paths were not retried; no security control, DNS, permission or browser fingerprint was changed.

### Verified downloadable artifacts

| Artifact | SHA256 |
|---|---|
| m03-05-evidence-zh.svg | `6a8d7b044de81900b08ea0e8f8b8a9e293c85b66f43dda9a2f6477edba09bbfc` |
| m03-05-evidence-en.svg | `6d15e6da8930825068d49fd526459aee6f0e22703e9174624ce4a4be7a66dc47` |
| m03-05-proxy-zh.svg | `3c0d0e0a7b9d3b30ee8cf2719a3d1f314dbd591ea8e31ea26b6b816ecc40d874` |
| m03-05-proxy-en.svg | `70a65cfedacefa6e4c9c6c1b017554c18d2572a72a12017ce73d20d31f691d9c` |
| ceh-m03-05-bilingual-svg.zip | `ff5a46e48954352da9d060188ebb4a82cedd2d530a93ea7c7a468b6b0a04523b` |

The download navigation produced the browser's normal navigation-aborted signal when the ZIP transfer began; the completed download path and hash, not that navigation signal, establish the artifact result.

Reference-answer anchor: `#answer-port-label`. Website publication and answers do not establish learner submission or mastery. Next concept navigation is M03-06, explicitly pending; no M03-06 teaching page was published by this change.
