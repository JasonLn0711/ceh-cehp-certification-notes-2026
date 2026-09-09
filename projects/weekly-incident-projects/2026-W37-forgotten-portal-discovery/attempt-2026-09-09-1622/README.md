# M02 practical attempt — 2026-09-09

## Result and ownership

**One bounded TCP connect scan completed; seven original evidence files pass integrity verification.** The scan observed `127.0.0.1:8766/tcp` open while the supplied register contains only ports 8765 and 8767. This supports an inventory/register gap. `WP-2026-W37` is **attempted**, with metadata enumeration and full weekly acceptance still open.

FIRST PRINCIPLE: attention, finite authorized time and trustworthy evidence govern this record. Jason performed the learner actions; the supplied instructor guided and drafted documentation. This attempt owns source, outputs and analysis; Planning owns capacity, completion and next gate. Capturing instructor-drafted analysis demonstrates evidence preservation, while independent reasoning requires the learner's own response.

## Source and verification layers

- [Complete supplied conversation](practical-session.source.md), preserved verbatim as UTF-8, 40478 bytes; SHA-256 `4b9b6847f68b685e4b17a3a9a92c7f73184ff3149f3b1d97c93626afb2316c05`.
- The source contains commands, pasted terminal output, explanations, questions, prediction, window agreement and closeout. Formatting quirks remain intact.
- Local files were read during this capture. The [original manifest](SHA256SUMS.txt) was checked directly: **7/7 OK**. The original manifest, seven covered files and [learner verification receipt](hash-verification.txt) retain their original bytes.
- New source/summary files are later documentation additions **outside the original manifest**. `SHA256SUMS.txt`, `hash-verification.txt` and `mock-server.pid` are also outside its seven-file coverage. The original [coverage note](hash-coverage.md) explicitly explains the PID exclusion.
- No lab command was rerun during this capture. The saved transcript verifies a historical scan, rather than current reachability. Pasted shutdown/preflight output is source evidence, not a newly executed host-state check.

## Authorization and sequence

| Checkpoint | Evidence and interpretation |
| --- | --- |
| Earlier quiz 15:00–15:30; question-only extension through 16:00 | Separate [10/10 diagnostic](../../../../assessments/attempts/2026-09-09-m02-practice-diagnostic.md); source reported its closeout at 16:17 |
| Initial practical block 16:22–16:52; active 16:27–16:47 | Preserved in [roe.md](roe.md); earlier window expired |
| Resumption 18:18; user answered “okay” | Fresh dated amendment: learning 18:18–18:48; active testing 18:20–18:43; closeout reserved after 18:43 |
| Preflight | Pasted `ss` pipeline reported no matching listeners; no scan consumed |
| Mock startup | [mock-server.log](mock-server.log) reports three listeners; pasted shell job and [PID record](mock-server.pid) identify historical PID 722149 |
| Prediction | Jason predicted `8765 open, 8766 open, 8767 open` |
| Scan 18:32:28+08:00 | [scan-transcript.txt](scan-transcript.txt) records exactly `nmap -sT -Pn -n -p 8765-8767 127.0.0.1`, exit code 0 |
| 18:42:34 source time check | Instructor moved to closeout before 18:43; HTTP enumeration deferred |
| Shutdown | Pasted `kill -TERM`, shell termination message and later no-listener output support reported shutdown; precise shutdown time is not recorded |
| Documentation and hashes | Asset record, focused research, coverage note, manifest and seven OK verification lines preserved; exact final closeout time is unrecorded |

All windows use Asia/Taipei. The transcript timestamp falls within the amended active window. One scan is evidenced, against a ceiling of two for that day's exercise; **zero learner HTTP requests are reported**. An unused scan allowance does not extend an expired window. The two practical blocks are 30 minutes each as planned windows, not measured focus totals; retain the earlier quiz overrun separately and review remaining weekly capacity before assigning another block.

## Observation, labels and finding

| Port | Supplied register | Startup program report | Scan state / lookup label |
| --- | --- | --- | --- |
| 8765/tcp | public portal / Digital Services | public-portal | open / ultraseek-http |
| 8766/tcp | absent | legacy-reporting | open / amcs |
| 8767/tcp | observability / Platform Operations | observability | open / core-of-source |

The scan establishes bounded reachability during this attempt. Nmap documents `-sT` as OS `connect()` scanning; its service database maps port/protocol to names. Thus `amcs` is the displayed lookup label, while `legacy-reporting` is the mock's own runtime role report. Neither supplies independently verified organizational ownership. [Official connect scan documentation](https://nmap.org/book/man-port-scanning-techniques.html); [official service database documentation](https://nmap.org/book/nmap-services.html), both freshly opened during capture on 2026-09-09.

The [asset record](asset-record-8766.md) preserves the supported inventory-gap inference and its evidence references. Software identity/version, vulnerability, exploitability and accountable ownership remain separate validation questions. [Focused research](research-note.md) addresses the observed label discrepancy; [W37 research brief](../../../../research-briefs/2026-W37.md) routes that narrow live research and the remaining weekly research requirements.

## Plain-language command learning

| Syntax / tool | Purpose in the supplied session |
| --- | --- |
| `cat >>` and quoted heredoc | Append a literal dated amendment while preserving the original ROE |
| `sed -n '90,125p'` | Read the startup/argument logic before executing the program |
| `&&` / `||` | Choose the next command from success/nonzero exit status |
| `ss -ltn`, pipe and `grep -E` | Inspect local listening TCP sockets and filter the approved ports |
| `python3 -u`, `>`, `2>&1`, `&` | Start the mock with immediate stdout/stderr logging in the background |
| `$!` and PID file | Save the just-started background process identifier for this session |
| `script -q -c` | Preserve the scan's terminal output and command exit receipt |
| `-sT -Pn -n -p` | Connect scanning; skip host discovery and DNS; select exactly the approved ports |
| `kill -TERM`, `kill -0`, `while` | Request termination and wait for the saved process to disappear |
| `find`, `sort`, `tree` | Inspect artifact names and file layout before deciding hash coverage |
| `sha256sum`, `-c` | Record digests, then compare current bytes with the recorded values |
| `tee`, pipe, `tee -a` | Show stdout and save it; overwrite by default or append with `-a` |

Jason explicitly asked what `tee` means; the instructor explained screen-plus-file copying, pipe/stdin/stdout, overwrite and append before the learner continued. The first displayed hash command printed hashes without creating a manifest; the later redirected command saved it, and the check returned seven OK lines. Preserve this useful correction sequence as learning evidence.

## Precision notes for future teaching

These clarify the interpretation while preserving the exact supplied source:

- The `ss | grep || echo` message is conditional output, not independent proof that every preceding command succeeded. A failure of `ss` or a filtering error can also produce misleading reassurance. Future preflight should preserve/check command success and raw listener output before declaring a pass; no new preflight was executed here.
- The scan's `script` receipt contains exit code 0. A pipeline ending in `tee` alone does not expose every preceding exit code; here the actual seven OK lines and this capture's direct successful manifest check support integrity verification.
- The program's startup log reports listeners; the subsequent scan supplies the operator-side connectivity evidence. SIGTERM termination and pasted shell status support reported process shutdown, without a claim that the Python Ctrl-C cleanup handler executed.
- A historical PID should be treated as historical metadata. Future blocks identify their own process before acting; reuse of this saved PID is not an authorization or identity check.
- The source asked for an explanation of why `amcs` is not verified application identity, but Jason replied with a next-step question. Record that teach-back as **unanswered**, alongside the completed prediction and earlier 10/10 conceptual diagnostic. No later independent explanation or new retest result is invented.

## Closeout and next gate

Completed evidence: dated ROE amendment, supplied register, fixed-port startup report, one bounded scan, instructor-guided asset record, focused primary-source note, reported shutdown and seven-file integrity check. The revised daily quiz remains met; this practical slice adds actual learner execution.

Weekly state is `attempted`, not accepted. Next: choose a fresh dated block, confirm applicable scope and remaining capacity, restart the owned mock under that authorization, request only the agreed `/service-info` endpoint, and compare returned claims with this asset record. Preserve the original sealed packet and put new outputs in a new clearly dated continuation record. Complete the weekly map/decision and acceptance review afterward. M01's original refusal/delayed-retrieval requirements and official module assessments remain separate gates.

Connections: [weekly mission](../README.md), [project index](../../README.md), [readiness dashboard](../../../../assessment-governance/readiness_dashboard.md), [day record](../../../../../planning-everything-track/weeks/2026-W37/days/2026-09-09.md), [weekly plan](../../../../../planning-everything-track/weeks/2026-W37/weekly-plan.md).
