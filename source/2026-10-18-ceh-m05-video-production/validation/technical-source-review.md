# M05 technical source review

Review date: 2026-10-18, Asia/Taipei. Scope: all 58 `scenes.json` narratives, the corresponding `SCRIPT_en-US.md`, `SOURCES.md`, `case/NORTHSTAR_FINDINGS.json`, all `lab_mock` files and the instructor key. This review evaluates teaching claims and evidence boundaries. It does not establish learner performance, a real vulnerability assessment, or rendered-video quality.

## Result

The checked core definitions and mechanisms are supported by primary sources. No demonstrable material factual error requires replacing the locked narration. Preserve the original text. The production must retain the conditional and hypothetical language described below; the mock packet supports no completed repair or live retest.

## Checked claims

| Scenes | Claim and assessment | Primary source checked |
|---|---|---|
| S01–S14, S39–S50 | Assessment separates observations, applicability, possible consequences and evidence of an incident. Patch management includes identifying, prioritizing, installing and verifying changes. The six teaching stages are an instructional synthesis, not an attributed mandatory standard. | [NIST SP 800-40 Rev. 4](https://csrc.nist.gov/pubs/sp/800/40/r4/final) |
| S15–S18, S53–S54 | CVE identifies a specific publicly known vulnerability; CWE describes weakness types; CPE structures product identification. An identifier alone does not determine local applicability. | [CVE records](https://www.cve.org/Resources/Media/Archives/OldWebsite/cve/identifiers/index.html), [MITRE CWE FAQ](https://cwe.mitre.org/about/faq), [NIST CPE naming specification](https://www.nist.gov/publications/common-platform-enumeration-naming-specification-version-23) |
| S18 | NVD enriches records with severity and affected-product information when available. The explicit allowance for missing or delayed enrichment is appropriate. | [NVD CVE FAQ](https://nvd.nist.gov/general/FAQ-Sections/CVE-FAQs); official indexed text available, direct text extraction empty |
| S19, S34 | KEV concerns known exploitation in the wild. It supplies prioritization evidence, not proof that Northstar was compromised. | [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog); CISA-domain indexed catalog text available, direct retrieval failed |
| S22–S30 | Credentialed host inspection can provide more detail but has coverage limits. Greenbone manager, scanner, UI and test feed have separate functions. The scene explains architecture without claiming a current installation recipe. | [Greenbone Community Edition 22.4 architecture](https://forum.greenbone.net/t/about-greenbone-community-edition-22-4-architecture/12705) |
| S23, S29 | ZAP passive scanning inspects proxied requests and responses. Active scanning sends attack tests and requires permission. Saved response review does not authorize a live scan. | [ZAP Getting Started](https://www.zaproxy.org/getting-started/) |
| S32–S33, S36, S56 | CVSS describes severity on a 0–10 scale. v3.1 groups are Base, Temporal and Environmental. v4.0 groups are Base, Threat, Environmental and Supplemental. CVSS Base is not complete local business risk. | [FIRST v3.1 specification](https://www.first.org/cvss/v3.1/specification-document), [FIRST v4.0 specification](https://www.first.org/cvss/v4.0/specification-document) |
| S34 | EPSS estimates exploitation probability for a published CVE over the next 30 days. It is distinct from severity and known-exploitation evidence. | [FIRST EPSS](https://www.first.org/epss/), [How EPSS Works](https://www.first.org/epss/how-it-works.html) |
| Whole curriculum | Public Module 05 covers vulnerability analysis, assessment types/tools, scoring/databases and AI. This film aligns with those headings; public headings do not prove exhaustive proprietary course or exam coverage. | [EC-Council CEH, Module 05](https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/) |

## Case evidence and production constraints

- **SIM-001 remains unconfirmed.** `file_server_alert.txt` contains a fictional banner; `mock_vendor_note.txt` says some builds may contain backported fixes. Neither provides the installed package record. S37 teaches a hypothetical false-positive resolution. Do not label this actual case resolved or display a verified checkmark. S45 and the instructor key correctly retain uncertainty.
- **SIM-002 supports a configuration concern.** `lab_share.txt` records a broader group than the intended policy. Actual allowed and denied access has not been tested. S44's initial “None yet” and S45's later supported configuration conclusion are consistent with staged review; the latter establishes the policy mismatch only.
- **SIM-003 needs context.** `web_header.txt` gives a saved response but does not name the recommended absent header. It cannot establish a specific browser effect, severity or repair choice. Keep S29/S44/S47 generic and conditional; inventing a CSP, HSTS or other specific finding would exceed this evidence.
- **SIM-004 uses a dated note.** `switch_policy.txt` provides neither a current configuration nor confirmed reachability. Keep current-state and external-exposure claims open.
- **No completed repair evidence exists.** `after_repair.txt` is explicitly a planned retest template with status `NOT RUN`. S47 correctly specifies future tests. S50's Friday update and S52's lifecycle board illustrate a process. Any completed-looking animation must identify an illustrative workflow and must not advance SIM findings to verified.
- **Scope is offline only.** The more general fictional authorization described in S05 is narrowed by its final offline-record statement and by S43 and `scope.txt`. The actual task authorizes source interpretation, not a live security test. External viewpoint is expressly unapproved in `coverage.txt`.
- **S35 follows its narration.** It discusses three hypothetical prioritization examples. The storyboard says four; the narration is authoritative. Do not silently turn the three examples into the four SIM findings or imply that the actual staff portal is publicly exposed.

## Teaching-package gaps to retain in the handoff

1. S58 requests a “likely false positive.” The packet establishes a possible false-positive candidate, not a likelihood measurement or confirmed outcome. Accept SIM-001 as a candidate with a required package check; do not grade a definitive false-positive assertion as supported. The instructor key already uses conditional reasoning.
2. S58 mentions a repair budget, but no numeric budget or itemized repair costs appear in the reviewed case files. Use qualitative constrained-priority reasoning and explicitly leave cost estimates open.
3. S32 says official examples will support formulas, but the locked narration contains no worked CVSS calculation. This is a depth limitation, not an incorrect definition. Do not claim that the film teaches hands-on vector calculation or invent numbers for fictional findings.
4. S03 loosely groups CVSS with public records. S32 and S53 correctly define it as a scoring system; the introductory shorthand does not warrant altering the locked script.

## Limits and provenance

The web check used primary publisher sources only. CISA direct retrieval returned an error; NVD direct retrieval returned no extractable body. Their official-domain search excerpts supported the narrow claims above. The archived CVE page and Greenbone 22.4 article support stable concepts; they are not evidence of current deployment instructions. No current CVE listing, score, EPSS value, exploit or vendor vulnerability was assigned to a fictional SIM finding. No target was contacted and no repair was performed.

This report leaves source files unchanged. It does not certify narration pronunciation, subtitle alignment, visual readability, or the final MP4; those require production checks.
