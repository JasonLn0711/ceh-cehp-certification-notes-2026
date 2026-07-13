# CEH / CEHP Daily Closed-Loop Plan

> Schedule scope change (`2026-07-13`): UCOM / UUU confirmed CEH 台北 `2048`
> for `2026-10-12` to `2026-10-16` and CEHP 台北 `26416` for `2026-11-19`
> to `2026-11-20`. The July-to-August sequence remains an optional early
> learning sprint; its August class-logistics labels no longer define the live
> attendance dates. Current gates live in `assessment-governance-system.md`.

## Operating Principle

Use a low-friction daily loop. Each day has:

- one primary task
- one visible output
- one record update

The system is successful when assessment results change the next learning action
without turning the governance process into the main workload.

## Canonical Detailed Calendar

Use the captured detailed calendar plan as the execution source:

`daily-closed-loop-calendar-plan.md`

Source copy:

`../source/2026-07-01-daily-closed-loop-assessment-calendar/ceh_cehp_assessment_calendar_plan_2026-07-01_to_2026-08-02.md`

## Default Calendar Blocks

- Weekdays: `20:30-22:00`
- Saturday: `09:30-12:00`
- Sunday: `15:00-17:00`

When a conflict appears, shift the time block and keep the task order.

## Daily Schedule

The table below is the compact operating mirror. The detailed source includes
the ten-layer mapping (`L1` to `L10`), exact default time blocks, and readiness
gate wording.

| Date | Calendar title | Task | Output |
| --- | --- | --- | --- |
| `2026-07-01` | 制度啟動與 baseline pretest | Establish the folder/system fields, complete the closed-book baseline, and mark confidence `1-4`. | baseline raw score, unknown list, attempt log entry |
| `2026-07-02` | Baseline scoring 與弱點圖 | Score baseline, map items to 20 modules, identify top five weak modules. | weak-module map v0, readiness rule v0 |
| `2026-07-03` | 題庫資料模型與 traceability v0 | Establish item bank, competency map, and traceability schema; add metadata for baseline items. | item bank v0, traceability matrix v0 |
| `2026-07-04` | M01 Ethical Hacking | Preview authorization, scope, stop condition, reporting path; finish M01 mini-posttest. | M01 status, critical safety check |
| `2026-07-05` | M02 Reconnaissance | Preview passive vs active discovery and authorization boundaries. | M02 posttest, recon evidence/control map |
| `2026-07-06` | M03 Scanning Networks | Preview host/port/service/vulnerability discovery with toy outputs. | M03 posttest, scan-output checklist |
| `2026-07-07` | M04 Enumeration | Preview users, shares, banners, service details, and scanning/enumeration distinction. | M04 posttest, one-page comparison note |
| `2026-07-08` | Gate 1: M01-M04 修補 | Retest missed items, specify parallel form B, update weak modules. | Gate 1 dashboard |
| `2026-07-09` | M05 Vulnerability Analysis | Preview severity, exploitability, impact, exposure, context, and false positives. | M05 posttest, risk/context/remediation note |
| `2026-07-10` | M06 System Hacking 概念化 | Preview credential, privilege, persistence, cleanup, and least privilege at concept level. | M06 posttest, lawful lesson list |
| `2026-07-11` | M07 Malware Threats | Preview malware types, delivery, persistence, controls, and evidence. | M07 posttest, malware evidence/control map |
| `2026-07-12` | M08 Sniffers + 週檢討 | Preview packet, flow, protocol, anomaly, and evidence; complete weekly meta-evaluation. | M08 posttest, weekly review |
| `2026-07-13` | Gate 2: M05-M08 修補 | Repair missed items, apply short-answer rubric `0 / 0.5 / 1`, update traceability. | rubric v1, Gate 2 dashboard |
| `2026-07-14` | M09 Social Engineering | Preview phishing, verification path, MFA, reporting flow, and human controls. | M09 posttest, control note |
| `2026-07-15` | M10 Denial-of-Service | Preview availability, resilience, rate limiting, monitoring, and escalation. | M10 posttest, availability map |
| `2026-07-16` | M11 Session Hijacking | Preview token/session risk, cookie flags, expiration, TLS, server-side validation. | M11 posttest, session risk/control note |
| `2026-07-17` | M12 Evasion / IDS / Firewall | Preview detection limits, layered controls, logging, and false negatives. | M12 posttest, defense-in-depth note |
| `2026-07-18` | Gate 3: M09-M12 情境題校準 | Retest missed items, write one evidence-based scenario per module, check high-confidence wrong items. | 4 scenario items, Gate 3 dashboard |
| `2026-07-19` | M13 Hacking Webservers | Preview patching, configuration, least privilege, logging, and default exposure. | M13 posttest, webserver hardening checklist |
| `2026-07-20` | M14 Web Application | Preview auth, input validation, access control, error handling, and logging. | M14 posttest, web-app risk map |
| `2026-07-21` | M15 SQL Injection 安全概念 | Preview untrusted input, parameterized query, controls, and log evidence. | M15 posttest, SQLi control note |
| `2026-07-22` | M16 Wireless Network | Preview WPA2/WPA3, guest separation, rogue AP, enterprise auth, and weak protocols. | M16 posttest, wireless control note |
| `2026-07-23` | Gate 4: M13-M16 修補 | Retest missed items, add 8 web/wireless form B items, update module status. | Gate 4 dashboard |
| `2026-07-24` | M17 Mobile Platforms | Preview device, app, network, storage, and identity risk. | M17 posttest, mobile attack-surface note |
| `2026-07-25` | M18 IoT / OT | Preview physical safety, firmware, segmentation, patching constraints, downtime risk. | M18 posttest, IT vs IoT/OT table |
| `2026-07-26` | M19 Cloud Computing | Preview shared responsibility, IAM, storage permissions, logging, and network rules. | M19 posttest, cloud responsibility checklist |
| `2026-07-27` | M20 Cryptography | Preview encryption vs hashing, integrity, key management, TLS, and common misuse. | M20 posttest, crypto misuse/control note |
| `2026-07-28` | 20 模組總整理 | Write 2-3 sentences per module: core risk, evidence type, main control. | 20-module class-readiness map v1 |
| `2026-07-29` | 正式 Pre-August Form B 建置 | Build 50 or 40 item form B, keep up to 8 anchors, add metadata and rubric links. | pre-August form B v1 |
| `2026-07-30` | Pre-August Readiness Test | Complete form B closed-book, score it, record confidence and safety errors. | form B score, final repair queue |
| `2026-07-31` | 修補封版與上課 notebook | Repair weakest five form B items/modules and create CEH class notebook template. | class notebook template v1 |
| `2026-08-01` | Final Gate: CEH readiness dry run | Explain 20 modules in 2-3 sentences, rehearse evidence interpretation, list class questions. | final gate result, class question list |
| `2026-08-02` | Light Review + Logistics Lock | Light review: authorization, 20-module map, top weak topics, transportation, equipment, login, sleep. | CEH Day 1 packet |

## Daily Closeout Template

Use `../assessment-governance/daily_closeout_template.md`.

## 2026-08-02 Minimum Standard

- Baseline is scored.
- All 20 modules have status.
- At least 16 modules are `pass` or `review`.
- Legal/authorization, network basics, web basics, cloud shared responsibility,
  and cryptography are at least `review`.
- Each `activation_needed` module has one concrete remediation action.
