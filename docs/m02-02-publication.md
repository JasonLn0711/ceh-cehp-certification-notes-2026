# M02-02 public teaching and publication evidence

Bilingual OSINT Sources and Source Validation teaching, reference answers, and four bilingual figures are available under [notes/m02](../notes/m02/). This unit follows M02-01 in the [161-unit route](../study-plan/core-route-2026-10-27.md).

## Website integration, 2026-10-30

- [PR #55](https://github.com/JasonLn0711/kairos-learning/pull/55) in the existing learning-site repository.
- Tested and remote head: `b92dbd0a5705636b54509c8d4e466b7228d3038e`; tree `8864c7a1eeb774313ee0ccca81c741df810cb936` matches the locally tested tree.
- [CI run 41046793957](https://github.com/JasonLn0711/kairos-learning/actions/runs/41046793957) succeeded at 2026-10-30 19:16:20 Asia/Taipei for that head.
- 56 tests passed; Svelte check reported zero errors and warnings. Release checks covered 244 HTML pages, 496 public text files, full bilingual text order, four inline diagrams per language, four collapsed reference answers, search text, SVG/ZIP bytes, and preserved existing download checksums.
- Eight original SVG files were rendered with Inkscape and visually inspected. Maximum diagram text is capped at inherited body size; narrower columns shrink proportionally.
- Browser-level mobile inspection remains unverified: local Chromium could not start because the environment prohibited its socket operation. Formal-site content readback is also not asserted; an existing restricted access route was not retried.
- After specific approval, PR #55 was marked ready for review and merged on 2026-10-30. Merge commit: `036123cd1464c5bc92c9516fd9a4e8341dfdfe0e`. Its tree is `8864c7a1eeb774313ee0ccca81c741df810cb936`, identical to the tested tree.
- [GitHub Pages run 41057351394](https://github.com/JasonLn0711/kairos-learning/actions/runs/41057351394) completed successfully at 2026-10-30 20:43:30 Asia/Taipei for that exact merge commit, including release verification and the deploy-pages step. This establishes successful Pages deployment, not independent live-page visual verification.
- Published route: https://learn.cs-kairos.com/courses/ceh/v13/m02/concepts/m02-02/ ; English route: https://learn.cs-kairos.com/en/courses/ceh/v13/m02/concepts/m02-02/ . Live HTTP/content and browser-mobile readback remain unverified under the access limitations above.

Teaching examples are synthetic; no third-party probing is performed. Private learning records and original conversations are not included.
