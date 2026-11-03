# M03-07 source and editorial review

Reviewed 2026-11-03 Asia/Taipei. Complete paired manuscripts and reference answers are preserved in notes/m03. No scan was executed and no learner answer or mastery claim is made.

## Route and question

Current remote concept-reading rule links core-route-2026-10-27.json. The row CEH26-M03-C07 / M03-07 is reading order 28, section 三/M03 row7, title「Nmap、掃描設定與結果判讀」, importance5/difficulty3, reason「能建立授權掃描、保存結果並解釋證據。」Original planned time 2026-11-05 08:00 is schedule metadata, not actual delivery. Legacy IDs are empty, new_scope/new_teaching. Prior M03 units receive brief connections, not full replay. Next M03-08 remains pending.

Main question: how do scope, settings and preserved output support a defensible scan conclusion? The lesson uses a building-inspection analogy, a read-only command illustration and a synthetic offline worksheet. It does not ask the reader to run network probes. Scope/stop conditions, output side effects and overwriting risks are explained. Port states remain observations, not intrusion evidence, as required by the M03 chapter supplement.

## Official sources actually read

All Nmap references are living official documentation, checked 2026-11-03. No actual installed version is assumed.

- https://nmap.org/book/man-target-specification.html — target notation expands or narrows target sets; authorization must be checked before choosing addresses/names.
- https://nmap.org/book/man-port-specification.html — -p lists/ranges, -p- selects1–65535, -F reduces covered common ports rather than preserving the same scope.
- https://nmap.org/book/man-port-scanning-techniques.html — -sT requests OS connection attempts, -sS is SYN probing, -sU covers UDP; no TCP-to-UDP inference.
- https://nmap.org/book/man-host-discovery.html — -sn discovery without port scanning; -Pn skips the usual discovery decision, not a liveness proof; local ARP considerations and -n reverse DNS behavior.
- https://nmap.org/book/man-misc-options.html — -A adds several features, not timing; --version prints installed version. Feature scope must be independently authorized.
- https://nmap.org/book/man-performance.html — timing/retry tradeoffs and response loss; template numbers are not safety/confidence grades.
- https://nmap.org/book/man-output.html — --reason, normal/XML output, -oA three file forms, deprecated grepable format and output overwrite risks.
- https://nmap.org/book/man-port-scanning-basics.html — states depend on observation position; filtered cannot be rewritten as closed or intrusion.

## Fidelity and review

Chinese and English have identical nine-section structure, command, two test ports8000/8001, localhost127.0.0.1, four questions and four stable reference-answer IDs. Synthetic records are labeled in each language. No version detection or OS evidence is invented. Reverse DNS suppression does not claim hostname input never resolves. Localhost explicitly refers to the current container/VM network environment; no external reachability is inferred. XML preference does not claim the normal output includes every runtime warning, which is why separate warnings/errors are retained.

The conceptual command is not an executed exercise. The actual exercise is three-step paper/text analysis with expected worksheet and no system cleanup. Scope planning is an original recommendation, not a purported legal rule or official fixed checklist.

Latest remote website AGENTS.md, article-standards, content-authoring, article-writing-template, diagram-design-system, publishing-security and perspectives/authoring were read before drafting. The new FIG-06/INT-01 M02-06 adoption is included: diagram layout must express sequence versus parallel relationships; no gratuitous simulator. Full source preservation, rule-ID acceptance, date/version, semantic HTML, answer-only disclosure and actual browser/deployment evidence remain separate. Unexecuted browser checks stay pending, not inferred from static tests.
