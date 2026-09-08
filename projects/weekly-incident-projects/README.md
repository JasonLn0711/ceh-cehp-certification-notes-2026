# Weekly Historical-Incident Projects

## Purpose

Each active self-directed learning week owns one integrated side project. The
project uses a documented cybersecurity incident to give CEH, CEHP, CTF, and
AI-security practice an operational setting. The learner completes one bounded
mission, preserves evidence, and closes the week with an accepted, attempted,
or blocked result.

## Weekly Contract

- Project ID: `WP-YYYY-Www`.
- Core capacity: `2–4 h`; optional depth stays inside the same project.
- Red-capacity fallback: one `25 min` executable action with saved evidence.
- Evidence state: `planned`, `attempted`, `blocked`, or `accepted`.
- Source policy: one primary historical incident, checked against a first-party,
  government, regulator, standards-body, or similarly authoritative source.
- Teaching policy: historical facts, fictional mock elements, authorized
  learner actions, and learner observations remain separate.
- Prompt-first support: at activation, use the global
  `professor-learning-prompt` skill to prepare a copy-ready prompt for the
  user-named model, defaulting to `gpt-6-pro` for Jason. The professor explains
  the required definitions, procedure, cases and evidence boundary before the
  learner performs the first active action.
- Build cadence: map the full horizon; fully prepare only the current and next
  projects; refresh the topic-specific sources during the execution week.

An unfinished project keeps its original week and evidence state. The next week
opens its own project. A safety-critical prerequisite may enter the new
project's acceptance path when the new scenario can exercise it without adding
a second weekly project.

## Packet Interface

Every runnable project contains:

1. `README.md`: learner mission, prerequisites, incident facts, fictional mock
   design, ROE, first action, tasks, evidence, acceptance check, and fallback.
2. `instructor-key.md`: expected decisions and outputs, rubric, common errors,
   and safety refusals.
3. Only the fixtures or standard-library code needed to run the mock instance.

Learner evidence is created under an attempt-specific directory only when the
learner executes the project. Author-validation evidence remains separate and
does not advance learner state.

## 2026 Map

| Week | Project | Curriculum | Historical anchor | Core acceptance | Pack | Learner |
| --- | --- | --- | --- | --- | --- | --- |
| W36 | [Authorization Gate](2026-W36-authorization-gate/README.md) | M01 | [Anthropic cybersecurity-evaluation incidents](https://www.anthropic.com/research/investigating-incidents-cybersecurity-evals) | one permitted localhost request, two pre-execution refusals, verified evidence, and explanation | `runnable` | `planned` |
| W37 | [Forgotten Portal Discovery](2026-W37-forgotten-portal-discovery/README.md) | M02–M04, M01 safety repair if needed | [FTC Equifax settlement](https://www.ftc.gov/news-events/news/press-releases/2019/07/equifax-pay-575-million-part-settlement-ftc-cfpb-states-related-2017-data-breach) | find the omitted service and distinguish reconnaissance, scanning, and enumeration in an ownership-aware asset map | `runnable` | `planned` |
| W38 | Clinic Ransomware Triage | M05–M08 | [CISA WannaCry record](https://www.cisa.gov/news-events/ics-alerts/ics-alert-17-135-01i) | classify synthetic host, patch, log, and packet evidence and prioritize containment | `mapped` | `planned` |
| W39 | Helpdesk Identity Takeover | M09–M12 | [CISA CSRB Lapsus$ review](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf) | reconstruct a no-send identity/session path, revoke the toy session, and specify layered detection | `mapped` | `planned` |
| W40 | Legacy Customer Portal | M13–M16 | [ICO TalkTalk investigation](https://ico.org.uk/about-the-ico/media-centre/talktalk-cyber-attack-how-the-ico-investigation-unfolded/) | compare unsafe and parameterized local queries and pass the web regression check | `mapped` | `planned` |
| W41 | Water-Plant Safety Gateway | M17–M20 | [EPA Oldsmar incident context](https://www.epa.gov/system/files/documents/2021-07/_epaoig_notificationmemo_7-23-21_cybersecurity_0.pdf) | reject an unsafe synthetic setpoint, log a safe action, and map mobile/IoT/cloud/crypto boundaries | `mapped` | `planned` |
| W42 | Dependency Exposure Casebook | CEH M01–M20 | [CSRB Log4j report](https://www.cisa.gov/sites/default/files/2023-02/CSRB-Report-on-Log4j-PublicReport-July-11-2022-508-Compliant.pdf) | locate mock transitive exposure and close the course week with an exposure/remediation matrix | `mapped` | `planned` |
| W43 | Trusted Update Chain | CEH end-to-end | [GAO SolarWinds review](https://www.gao.gov/products/gao-22-104746) | detect a benign tampered update, report it, repair the trust check, and retest | `mapped` | `planned` |
| W44 | Content Validator Recovery | midterm continuity | [CrowdStrike incident review](https://www.crowdstrike.com/en-us/blog/falcon-content-update-preliminary-post-incident-report/) | reproduce and correct a validator false acceptance, then pass canary and rollback checks | `mapped` | `planned` |
| W45 | Managed File Transfer Release | CEH conversion | [Progress MOVEit response](https://www.progress.com/blogs/update-steps-we-are-taking-protect-moveit-customers) | make a local regression harness catch unsafe query and authorization behavior | `mapped` | `planned` |
| W46 | Smart-Building Practical | CEHP P1–P5 | [CISA Mirai alert](https://www.cisa.gov/news-events/ics-alerts/ics-alert-16-286-01) | complete five bounded discovery, enumeration, traffic, system, and web missions | `mapped` | `planned` |
| W47 | Pipeline Continuity Gate | CEHP course | [GAO Colonial Pipeline review](https://www.gao.gov/products/gao-21-105263) | make a synthetic containment/restart decision and connect course gaps to P1–P5 | `mapped` | `planned` |
| W48 | Agent Action Firewall | AI-agent security | [Anthropic mitigation update](https://www.anthropic.com/news/improving-alignment-security-efforts) | allow one in-scope action and block ambiguous or excluded actions before tool execution | `mapped` | `planned` |
| W49 | Token Validation Investigation | manual/agent comparison | [CSRB Exchange Online review](https://www.cisa.gov/resources-tools/resources/cyber-safety-review-board-releases-report-microsoft-online-exchange-incident-summer-2023) | compare manual and agent decisions on the same synthetic token fixtures | `mapped` | `planned` |
| W50 | Source-vs-Release Verifier | verifier correction | [Red Hat XZ record](https://access.redhat.com/security/cve/cve-2024-3094) | reproduce a missed source/archive mismatch, repair the verifier, and rerun | `mapped` | `planned` |
| W51 | Update Hunt Reproducibility | reproducibility | [CISA 3CX bulletin](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/351ed77) | reproduce an IOC verdict from frozen synthetic fixtures, hashes, and instructions | `mapped` | `planned` |
| W52 | Claims Clearinghouse Continuity | finals continuity | [HHS Change Healthcare guidance](https://www.hhs.gov/guidance/document/change-healthcare-cybersecurity-incident-cms-response-and-state-flexibilities) | process and reconcile one synthetic claim through a fallback path without duplication | `mapped` | `planned` |
| W53 | Library Recovery Handoff | year-end handoff | [British Library incident review](https://www.bl.uk/files/v5dwkion/production/99206a2d1e9f07b35712b78f7d75fbb09560c08d.pdf/british-library-cyber-incident-review-8-march-2024.pdf?dl=) | verify a minimum read-only restoration path and leave a reproducible 2027 handoff | `mapped` | `planned` |

The authoritative locators were checked on `2026-09-05`. This was a map-level
source check; each target week still requires its own fresh topic scan and
evidence classification before execution.

## Weekly Preparation Gate

During the preceding weekly review, build the next mapped packet and run its
author self-check. During the target week, record a fresh topic-driven web scan
in `../../research-briefs/YYYY-Www.md` before relying on current guidance.
Licensed course material may provide private learner evidence; reusable packets
contain original mock material and public authoritative sources.
