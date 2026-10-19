#!/usr/bin/env python3
"""Build M10 learning companions and four local, seekable motion references.

Run from the completed source package. Uses only Python's standard library and
physically copies the approved local font, Tally and GSAP assets. It creates no
network traffic, learner scores, production deployment or rendered-film claim.
"""
from pathlib import Path
import argparse
import html
import json
import re
import shutil
import sys
import time
import wave

R = Path(__file__).resolve().parents[1]
SOURCE_NS = "M10-source-v1"
FILM_NS = "M10-film-v1"


def write(name, text):
    path = R / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def dump(name, value):
    write(name, json.dumps(value, ensure_ascii=False, indent=2))


def words(text):
    return len(re.findall(r"\b\w+(?:['’-]\w+)*\b", text))


def item(ident, prompt, choices, answer, explanation, scenes):
    return dict(id=ident, prompt=prompt,
                choices=[dict(letter=letter, text=text)
                         for letter, text in zip("ABCD", choices)],
                correct_letter=answer, explanation=explanation, scenes=scenes)


PRETEST = [
    item("PRE01", "A portal answers its basic health endpoint, but authorized students cannot finish enrollment. Which measure best tests the required availability?", [
        "Whether the machine has electrical power",
        "Whether the defined enrollment task reaches its confirmation",
        "Whether every source address is different",
        "Whether the application has the newest visual theme"], "B",
        "The service objective is a completed enrollment, so test that task and record its result, time window and denominator. Electrical power and a basic endpoint can remain healthy while another part of the user path fails. Source distribution does not measure completion, and a visual theme does not establish reachability. A failed task records an availability symptom; its cause and any malicious intent need separate evidence.", ["S01", "S02", "S03"]),
    item("PRE02", "Two links carry the same byte rate, but one carries many more small packets. Which additional measurement helps examine packet-handling pressure?", [
        "Only the total number of domain names",
        "Only the display resolution of the server",
        "Packets per second with relevant device drops and health",
        "The number of letters in each source address"], "C",
        "Packets per second describes the number of packet-processing events. Device drops and health can help determine whether that processing is constrained. Equal byte rates can contain different packet counts. Domain-name counts, display resolution and address-string length do not measure this resource. A real device limit still depends on its configuration and traffic mix; the comparison alone does not establish a specific measured capacity.", ["S07", "S13"]),
    item("PRE03", "A campus counter stops at link capacity while an aligned provider counter reports greater offered demand. Which interpretation preserves both observations?", [
        "The counters can describe accepted traffic and offered traffic at different points",
        "The provider value must be added to the campus value as independent arrivals",
        "The campus value proves that no other traffic tried to arrive",
        "The larger value identifies a particular human attacker"], "A",
        "Keep the accepted campus traffic and the offered provider demand tied to their observation points and aligned interval. A constrained ingress can accept less than is offered. Adding both as independent arrivals can double-count traffic, while the campus counter cannot reveal all upstream demand by itself. Neither value identifies a person or establishes intent. Verify the counter definitions before combining real measurements.", ["S11", "S12", "S35"]),
    item("PRE04", "A fixture reports 1,024 half-open entries at one observation and 6,000 unique attempts during a minute. What must an analyst preserve?", [
        "Every attempt must occupy state simultaneously",
        "The number of attempts is the server's backlog capacity",
        "Every repeated packet creates a distinct new user",
        "A state snapshot and an interval total measure different things"], "D",
        "Half-open occupancy is a state observation; attempts accumulate across the interval. The two values cannot establish simultaneous occupancy for every attempt. Capacity is a separate stipulated limit, and retransmissions must not silently become new unique attempts. Keep the clock, definitions and active defenses with the counters. This distinction helps explain resource pressure without inventing an exact connection history.", ["S17", "S18", "S19"]),
    item("PRE05", "Which remaining limit can still affect a server using suitable SYN cookies?", [
        "Packet-processing or application-work capacity",
        "No limit, because cookies create unlimited resources",
        "Only the color of the operating-system interface",
        "No legitimate-client tradeoffs need review"], "A",
        "SYN cookies address a particular incomplete-handshake state problem. They do not create unlimited bandwidth, packet-processing capacity, completed-connection resources or application capacity. Their implementation and legitimate-client behavior still need review. Interface colors do not address the mechanism, and removing tradeoff checks would omit important evidence. Treat cookies as a candidate with a narrow expected benefit, followed by an authorized validation plan.", ["S20", "S21", "S22"]),
    item("PRE06", "The same request and reply have IP lengths of 60 and 3,000 bytes and Ethernet lengths of 74 and 3,014 bytes. Why do the two consistent-layer ratios differ?", [
        "The packet file must have sent the reply twice",
        "Added Ethernet header bytes change both totals and the denominator",
        "Ethernet byte totals always equal IP byte totals",
        "Any larger ratio proves the fixture came from the Internet"], "B",
        "The Ethernet header adds bytes to each saved frame. Dividing 3,000 by 60 gives 50, while dividing 3,014 by 74 gives about 40.7. Both describe their stated accounting boundary. Neither includes every possible physical-link overhead or proves an Internet observation. The different results do not imply duplicate transmission. Use paired values from the same layer and state the inclusion rule.", ["S24", "S25"]),
    item("PRE07", "Which operator is positioned to reject traffic with an invalid source prefix as it enters from the originating customer's network?", [
        "Only a finance employee reviewing invoices",
        "Only the destination web application after every constrained link",
        "The network operator at that source-validation boundary",
        "Any analyst who opens a local packet file"], "C",
        "Source-address validation belongs at a network boundary where the operator can determine the permitted source ranges. That operator can reject source values outside the policy. A finance role or local file inspection does not grant network-change authority. A destination application sits at a different point. Prefix validation still allows some abusive traffic and requires appropriate routing exceptions; it is not a universal proof that permitted traffic is harmless.", ["S26", "S27", "S28"]),
    item("PRE08", "In a separate toy calculation, 250 requests per second each need 40 milliseconds of CPU service. What is the offered processor demand?", [
        "0.04 core-seconds per second",
        "250 core-seconds per second",
        "6.25 core-seconds per second",
        "10 core-seconds per second"], "D",
        "Convert 40 milliseconds into 0.04 core-seconds per request, then multiply by 250 requests per second. The result is 10 core-seconds per second. Per-request time alone omits the rate, while the other alternatives omit or reverse the conversion. These invented inputs are a separate simulated transfer example, not another row in E04. The result estimates offered work under the toy assumptions, not measured response time or malicious intent.", ["S29", "S30"]),
    item("PRE09", "A saved record contains many HTTP/2 stream cancellations. Which next interpretation is justified before declaring a Rapid Reset attack?", [
        "Every cancellation proves a malicious user",
        "Examine behavior over time, implementation costs, resource pressure and user impact",
        "A canceled request proves all downstream work stopped instantly",
        "Count only bandwidth because stream behavior cannot affect work"], "B",
        "Cancellation is legitimate protocol behavior. A useful investigation checks patterns over time, the implementation's work, resource pressure and actual service impact. A count alone establishes neither intent nor whether downstream work stopped. Bandwidth is only one resource. The historical Rapid Reset discussion explains a cost imbalance and implementation-specific defenses; it does not authorize replaying an attack or establish the state of an uninspected deployment.", ["S31", "S32", "S33"]),
    item("PRE10", "Which action is authorized by this source package's practical exercise?", [
        "Replay the PCAP toward a public resolver",
        "Load-test a school service without separate scope",
        "Parse the supplied local files and write an evidence-based incident brief",
        "Deploy a provider filter based only on an AI recommendation"], "C",
        "The package authorizes offline reading, local parsing and written reasoning over supplied synthetic evidence. It sends no packets and grants no scope to stress a service or deploy operational controls. Replaying the PCAP, loading a public service, or changing a provider filter would require separate appropriate authority and validation. Keep the learner's actual command, result and saved brief distinct from the builder's prepared materials.", ["S04", "S37", "S49", "S58"]),
]

TRANSFER = [
    item("POST09", "In a separate simulated recovery review, request rate drops after a rule, but enrollment success remains 10 of 100 and the database pool stays full. Which closeout is best supported?", [
        "Declare service recovery because fewer requests arrived",
        "Treat the rule as the proven cause of improvement",
        "Close the incident because processor use is low",
        "Keep recovery open and investigate the user path and constrained dependency"], "D",
        "The defined enrollment task still fails for most sampled checks, and the dependency remains full. Lower request rate alone does not satisfy the user objective or show that the rule caused improvement. Processor use can be low while another resource prevents completion. Keep the recovery claim open, review the dependency's operations and timing, and apply the incident owner's agreed criteria. These are separate simulated transfer values, not additional E04 observations. A further authorized check needs aligned user and resource evidence, a named owner and an appropriate rollback or escalation condition.", ["S32", "S41", "S48"]),
    item("POST10", "A security rule blocks a shared campus address, reducing load while preventing legitimate students behind that gateway from enrolling. Which validation improvement best addresses this tradeoff?", [
        "Measure legitimate-task rejection alongside resource benefit and define revision or rollback conditions",
        "Count dropped traffic as the only success measure",
        "Treat the shared address as proof that all users are one attacker",
        "Hide failed legitimate tasks from the incident record"], "A",
        "Protection must be evaluated against both the constrained resource and the intended users. Record legitimate-task rejection, service outcomes and resource changes in comparable windows, then use the agreed revision or rollback condition. Dropped traffic alone can make a damaging control appear successful. Shared addresses do not establish a single person or common intent, and removing unfavorable outcomes would corrupt the record. This transfer scenario illustrates a validation decision. It does not establish that Northstar deployed such a rule or that a particular replacement control will work without its own evidence.", ["S09", "S36", "S39", "S41"]),
]

CAPSTONE = """## Offline Northstar incident brief

Use only the [supplied fixtures](lab_mock/README.md). Every campus record is **SIMULATED OUTPUT**. Read the existing [verifier](tooling/verify_evidence.py) and, when the learner task is activated, run `python3 tooling/verify_evidence.py` from the package root. It reads local evidence and writes its local validation report; it sends no traffic. Preserve the learner's command, interpreter/tool identity, actual output and evidence location separately from the package-builder report.

1. Map each file to its observation point, interval, units and stipulated user result. Preserve original bytes and hashes.
2. Reproduce E01's offered/accepted/discarded accounting, E02's completion fraction, both E03 byte ratios, and E04's three work-demand calculations.
3. Explain the constrained resource and alternative explanations. Distinguish a state snapshot from an interval total, and resource pressure from malicious intent or attribution.
4. Propose a control at the appropriate location with a named owner, expected effect and legitimate-user tradeoff. Record its status as proposed.
5. Define the user task, resource measurements, comparison interval and rollback condition needed for a future separately authorized validation.
6. Submit the brief, calculations, source references and unresolved questions. Label any AI draft and the human corrections separately.

No packets are sent or replayed. No live listener, stress tool, target scan, provider contact or production change is part of this exercise. A constructed recovery row demonstrates a proposed comparison; it does not prove deployment or recovery.
"""


def render_questions(items, title, intro, mapped=False):
    blocks = [title, intro]
    for q in items:
        mapping = ""
        if mapped:
            mapping = ("\n\nMapping: " + q.get("mapping", SOURCE_NS + "/" + q["id"]) +
                       ". Scenes: " + ", ".join(q.get("scenes", [])) + ".")
        blocks.append("## " + q["id"] + "\n\n" + q["prompt"] + "\n\n" +
                      "\n".join(c["letter"] + ". " + c["text"] for c in q["choices"]) +
                      mapping + "\n\nFirst choice: ____ · Confidence: low / medium / high.\n\nReasoning before key: ____ · Assistance or prior exposure: ____.")
    return "\n\n".join(blocks)


def render_key(items, title, intro, mapped=False):
    blocks = [title, intro]
    for q in items:
        mapping = "\n\nMapping: " + q["mapping"] + "." if mapped else ""
        blocks.append("## " + q["id"] + " — " + q["correct_letter"] + mapping +
                      "\n\n" + q["explanation"])
    return "\n\n".join(blocks)


def build_documents(scenes, questions):
    actual_words = sum(words(s["narration_en_US"]) for s in scenes)
    route = """Prepared assessment namespace: **M10-source-v1**. The eight film items retain **M10-film-v1/Q01–Q08**. These are original teaching items, not official exam questions. Existing 600-question bank IDs, first answers and scores remain unchanged.

At an activated learning block, record the learner's used minutes, remaining capacity and endpoint. New concepts use one question at a time with choice and low / medium / high confidence before feedback. Familiar concepts may use a ten-item drill with feedback after the batch or endpoint. Preserve original answers before showing the independent key. Mark prior exposure or assistance. For each actual error, explain the mechanism and assign at least three varied retests; retain their results separately. At the endpoint, save partial work and the exact next question. Prepared questions and package QA are not learner progress.
"""
    film_intro = ("Eight original film questions use **M10-film-v1**, separate from the existing 600-question bank. Record your first choice, categorical confidence and reasoning before opening the [independent instructor reference](ASSESSMENT_INSTRUCTOR.md). The film reads the full stem and A–D choices, then has a 1.000-second silent hold before its answer. Pause playback whenever you need more time.\n\n" + route)
    write("ASSESSMENT_STUDENT.md", render_questions(questions, "# M10 film assessment and capstone", film_intro) + "\n\n" + CAPSTONE + "\n\nContinue in the [worksheet](WORKSHEET.md) and [blank closeout](CLOSEOUT.md).")
    rubric = """## Capstone reference and acceptance criteria

| Case | Supported result | Evidence limit | Appropriate next decision |
| --- | --- | --- | --- |
| E01 | In the aligned 60-second incident, provider offered demand is 2,400 Mbps, campus acceptance is 200 Mbps and equivalent constrained-ingress discard is 2,200 Mbps. Sampled user success is 20/100; server CPU is 25%. | Observation points differ. Saturation does not identify an attacker. | Ask the provider to evaluate protection before constrained ingress, with legitimate-user checks. |
| E02 | Half-open occupancy and capacity are both 1,024. The stipulated completion fraction is 60/6,000 = 1%. Link traffic is 30 Mbps; client success is 5/100. | Occupancy is a snapshot, attempts/completions are interval totals, and retransmissions are separate. No deployed cookie or proxy test is supplied. | Define an implementation-specific connection-state control trial and legitimate-client criteria. |
| E03 | IP sizes 60/3,000 yield 50×; Ethernet sizes 74/3,014 yield about 40.7×. Two constructed packets support local field parsing. | Forged source is constructed, no traffic is sent, and the teaching MTU is stipulated rather than an Internet path measurement. | Assign source validation, resolver/response controls and victim upstream protection to the appropriate owners. |
| E04 | Toy CPU demand is 2 core-seconds/second ordinarily, 24 in the incident and 1.5 in the legitimate counterexample, against an eight-core budget. Incident dependency occupancy is 32/32 with queue 400. | Offered work is a toy calculation, not a benchmark. Pool occupancy does not prove its cause. | Evaluate bounded work, admission, queues, appropriate caching and dependency isolation at their respective resources. |

Accept the offline brief only when the learner's own saved output demonstrates all of the following: identifiable input/tool/command and reproducible calculations; correct observation points and units; correct resource explanation without unsupported attribution; proposed controls matched to owner and location; both legitimate-task and resource validation criteria; and explicit unresolved questions and execution status. Review conceptual or calculation errors and their required varied retests. Missing learner execution requires activation before practical acceptance. This rubric supplies criteria; it records no accepted practical task.
"""
    write("ASSESSMENT_INSTRUCTOR.md", render_key(questions, "# M10 independent instructor reference", "Open after recording the original choice and confidence. Keep original and retest scores separate. Film items use M10-film-v1; prepared answers do not add 600-bank first answers.") + "\n\n" + rubric + "\n\nUse the [blank closeout](CLOSEOUT.md) for the actual learner record.")
    pre_intro = (route + "\nThese ten independently authored prepared questions are PRE01–PRE10 under M10-source-v1. [Answer key](PRETEST_KEY.md) stays separate. An unanswered item remains unanswered.")
    write("PRETEST.md", render_questions(PRETEST, "# M10 prepared pretest", pre_intro, mapped=True))
    write("PRETEST_KEY.md", render_key(PRETEST, "# M10 independent pretest key", "Namespace: M10-source-v1/PRE01–PRE10. Read after first choice/confidence. These explanations support correction, not an automatic score or readiness claim.") + "\n\n[Return to questions](PRETEST.md) · [Correction record](WORKSHEET.md).")
    post = []
    for i, q in enumerate(questions, 1):
        p = dict(q)
        p["id"] = f"POST{i:02}"
        p["mapping"] = f"{SOURCE_NS}/{p['id']} reuses {FILM_NS}/{q['id']} at {q['scene_id']}"
        p["scenes"] = [q["scene_id"]]
        post.append(p)
    for q in TRANSFER:
        p = dict(q)
        p["mapping"] = f"{SOURCE_NS}/{p['id']} is a new transfer item"
        post.append(p)
    post_intro = (route + "\nPOST01–POST08 reproduce the eight film items with explicit mappings. Prior film exposure means they are review items rather than fresh unseen measurements. POST09–POST10 are new transfer items; their invented values are simulated examples, not added case observations. [Independent key](POSTTEST_KEY.md).")
    write("POSTTEST.md", render_questions(post, "# M10 prepared posttest", post_intro, mapped=True))
    write("POSTTEST_KEY.md", render_key(post, "# M10 independent posttest key", "Namespace: M10-source-v1/POST01–POST10. POST01–POST08 reuse M10-film-v1; POST09–POST10 transfer the concepts. Preserve exposure, original answers and retests separately.", mapped=True) + "\n\n[Return to questions](POSTTEST.md) · [Actual closeout](CLOSEOUT.md).")

    write("STUDY_GUIDE.md", f"""# M10 availability study guide

The complete [English narration](SCRIPT_en-US.md) contains **{actual_words:,} canonical spoken words** across 11 chapters and 58 scenes. This guide supplies a compact lookup path; use the full script for explanation and case continuity. See the [chapter map](chapters.json), [coverage matrix](COVERAGE_MATRIX.md) and [concept connections](CONCEPT_CONNECTIONS.md).

## Start with the service and the resource

Availability means the authorized user can obtain the defined service when needed. Record a completed task, its delay or failure, denominator and interval. Resource pressure explains a constraint; deliberate interference, actor identity and distribution require their own evidence. A large rate or many addresses alone does not establish those claims.

Ask four questions: which finite resource is needed; how much demand reaches it; what was observed at which point; and which owner can control that boundary? Bandwidth, packet handling, connection state, processor work and dependencies can each constrain useful completion.

## Formula and interpretation card

| Calculation | Formula and unit | Northstar example | Limit |
| --- | --- | --- | --- |
| Data rate | IP octets × 8 ÷ seconds ÷ 1,000,000 = Mbps | E01 uses aligned 60-second windows. | Keep layer and observation point consistent. |
| Ingress accounting | offered = accepted + discarded equivalent | Incident: 2,400 = 200 + 2,200 Mbps. | This is the fixture's stipulated boundary accounting. |
| Completion fraction | completed unique handshakes ÷ unique attempts | E02: 60 ÷ 6,000 = 1%. | Preserve counter definitions and interval boundaries; occupancy is separate. |
| Amplification | paired response bytes ÷ paired request bytes | E03 IP: 3,000 ÷ 60 = 50×; Ethernet: 3,014 ÷ 74 ≈ 40.7×. | Pair the same layer; a ratio is not a traffic rate or universal server property. |
| Offered processor work | requests/second × CPU seconds/request | E04: 100 × 0.020 = 2; 120 × 0.200 = 24; 300 × 0.005 = 1.5 core-seconds/second. | Toy service-demand inputs, not a measured benchmark or elapsed request time. |
| Sampled task success | completed stipulated tasks ÷ attempted tasks | E01 20/100; E02 5/100. | Describes the stated sample and task, not every user. |

## Mechanisms and controls

- A saturated access link needs suitable protection before that constraint. A later application filter can protect later work while leaving link capacity consumed.
- Incomplete TCP handshakes can pressure finite pending state. A backlog, timeout, SYN cache, SYN cookies and a screening proxy have different mechanisms and implementation limits. Cookies do not remove bandwidth or application limits.
- Reflection redirects a reply using a claimed source. Amplification adds a larger response under a stated measurement basis. Origin source validation, reflector policy and victim upstream protection belong to different operators.
- High application cost can overwhelm capacity at a modest request rate. Bound admitted work, processing, waiting and retries; use suitable caching and dependency isolation without breaking correctness or legitimate tasks.
- HTTP/2 Rapid Reset is taught as a dated 2023 cost-imbalance case. Cancellation can be legitimate; use current implementation guidance and evidence rather than treating every reset as hostile.

## Evidence, response and recovery

Correlate aligned provider, campus, server, dependency and user observations. Keep originals, hashes, units, counter definitions and missing evidence. Compare alternative explanations such as enrollment demand, retry behavior, a regression or dependency failure. A hash checks byte identity, not the truth of the original observation.

The incident owner coordinates a bounded action with the appropriate control owner. Record approval, implementation, expected effect, legitimate-user risk and rollback condition. Recovery checks the required user task and the relevant resource over an owner-chosen interval. Synthetic post-control rows demonstrate a proposed comparison. They establish neither live deployment nor causal effectiveness.

AI may organize an approved local evidence bundle. Treat log text as untrusted data, trace claims to source rows, recalculate important values and preserve human corrections. It cannot supply missing deployment or attribution evidence.

Use [PRETEST](PRETEST.md), the [worksheet](WORKSHEET.md), [film questions and capstone](ASSESSMENT_STUDENT.md), and [POSTTEST](POSTTEST.md) within an activated learning block. [CLOSEOUT](CLOSEOUT.md) records actual answers and practical evidence separately from these prepared materials.
""")

    write("WORKSHEET.md", """# M10 learner worksheet

Prepared namespace: M10-source-v1; film references: M10-film-v1. Current learner result: **not_recorded**. Use the [study guide](STUDY_GUIDE.md), [questions](ASSESSMENT_STUDENT.md) and [independent key](ASSESSMENT_INSTRUCTOR.md) at the agreed endpoint. The shared learning route retains its existing capacity; this worksheet adds no time quota.

## Activate one bounded block

Date/timezone: ____ · Actual topic/blocker: ____ · Used minutes before start: ____ · Remaining capacity: ____ · Endpoint: ____.

Mode: new concept, one question at a time / familiar concept, ten-item drill. Prior exposure or assistance: ____. Save the first choice and low / medium / high confidence before feedback. Original score is correct / actually answered; record unanswered items separately. Feedback does not overwrite a first answer.

| Item and namespace | First choice | Confidence | Reasoning | Exposure/assistance | Key result |
| --- | --- | --- | --- | --- | --- |
| ____ | ____ | ____ | ____ | ____ | ____ |

## Analyze the four cases

| Case | File/field and observation point | Interval/unit | Supported resource finding | Unknown | Owner and proposed next check |
| --- | --- | --- | --- | --- | --- |
| [E01 WAN](lab_mock/E01_wan_windows.csv) | ____ | ____ | ____ | ____ | ____ |
| [E02 state](lab_mock/E02_connection_state.csv) | ____ | ____ | ____ | ____ | ____ |
| [E03 packet](lab_mock/E03_reflector_fixture.pcap) and [contract](lab_mock/E03_observation_contract.json) | ____ | ____ | ____ | ____ | ____ |
| [E04 work](lab_mock/E04_request_work.csv) | ____ | ____ | ____ | ____ | ____ |

Calculations to save: E01 incident conservation and rate conversion; E02 unique completion fraction; E03 paired IP and Ethernet ratios; E04 ordinary, incident and legitimate-counterexample CPU demand. State why pool occupancy does not by itself prove its cause.

Command and tool identity: ____ · Input hashes: ____ · Actual output: ____ · Saved brief/calculation paths: ____ · Blocker if any: ____.

The [local verifier](tooling/verify_evidence.py) parses supplied files and writes [its local report](validation/evidence-verification.json). A builder-created report is source QA. Your own activation, command and saved result establish what you personally executed.

## Correct an observed error

Original item/choice/confidence: ____ · Specific misconception: ____ · Plain-English correction: ____ · Supporting scene/source: ____.

Assign at least three varied retests that require the corrected reasoning in different situations. Give each a distinct retest ID and preserve its relation to the original. A wrong retest needs its own correction and varied retests; retain unfinished work at the endpoint. Low-confidence correct answers need a reasoning check.

| Retest | New situation/question ID | Choice and confidence | Result and correction | Evidence |
| --- | --- | --- | --- | --- |
| 1 | ____ | ____ | ____ | ____ |
| 2 | ____ | ____ | ____ | ____ |
| 3 | ____ | ____ | ____ | ____ |

## Plan two-sided validation

Proposed control/location/owner: ____ · Expected resource effect: ____ · Required legitimate-user task: ____ · Unwanted condition to address: ____ · Observation interval and counters: ____ · Approval needed for a real test: ____ · Rollback condition: ____.

All case records remain SIMULATED OUTPUT. Offline calculation, a proposed test, a real operational result and accepted learner practice each have their own evidence. Complete the [blank closeout](CLOSEOUT.md) using only the layer actually executed.
""")

    coverage = [
        ("Service availability and evidence scope", list(range(1, 7)), "Define useful completion, authority, resource explanations and evidence limits."),
        ("Rates, capacity and distribution", list(range(7, 11)), "Separate bits, packets, requests, state, waiting work and actor attribution."),
        ("Volumetric and packet-processing pressure", list(range(11, 17)), "Correlate offered/accepted traffic, user impact, packet work and control placement."),
        ("TCP connection-state pressure", list(range(17, 23)), "Explain handshakes, backlog, counters, cache/cookie/proxy mechanisms and tradeoffs."),
        ("Reflection and amplification", list(range(23, 29)), "Pair consistent layers; distinguish sender, reflector, victim and their defense owners."),
        ("Application and dependency exhaustion", list(range(29, 33)), "Compute toy work demand; bound waiting and protect shared dependency capacity."),
        ("Historical HTTP/2 Rapid Reset", [33], "Explain residual work after cancellation without replaying traffic or making current-largest claims."),
        ("Detection and offline tool roles", list(range(34, 39)), "Use baseline, aligned views, alternatives, local packet analysis and reproducible calculations."),
        ("Layered controls and incident handoff", list(range(39, 43)), "Match controls to resource and owner; evaluate false rejection, rollback and escalation."),
        ("Four connected evidence cases", list(range(43, 47)), "Integrate E01–E04 observations, supported findings and missing validation."),
        ("Response, recovery and AI review", list(range(47, 50)), "Coordinate changes, test useful recovery and trace AI claims to source evidence."),
        ("Film assessment and offline capstone", list(range(50, 59)), "Eight questions with individual one-second holds and one reproducible incident brief."),
    ]
    rows = []
    for topic, nums, teaching in coverage:
        ids = [f"S{n:02}" for n in nums]
        display = ids[0] if len(ids) == 1 else ids[0] + "–" + ids[-1]
        rows.append(dict(topic=topic, scenes=display, scene_ids=ids, teaching=teaching))
    dump("coverage.json", rows)
    write("COVERAGE_MATRIX.md", "# M10 official-topic coverage\n\nThe module backbone is Denial-of-Service in the EC-Council public course scope. These teaching labels are independently authored. [Complete narration](SCRIPT_en-US.md) and [machine-readable coverage](coverage.json) carry the scene mapping. The package's dated primary-source record supplies official references; prepared coverage is not official exam weighting or learner mastery.\n\n| Topic | Scenes | Teaching |\n| --- | --- | --- |\n" + "\n".join("| " + x["topic"] + " | " + x["scenes"] + " | " + x["teaching"] + " |" for x in rows) + "\n\n[Source assessments](PRETEST.md) use M10-source-v1. [Film items](ASSESSMENT_STUDENT.md) use M10-film-v1. [Practical criteria](ASSESSMENT_INSTRUCTOR.md) require the learner's actual saved evidence. Existing 600-bank records remain unchanged.")

    write("EXAM_FOCUS.md", """# M10 CEH exam-focus advice

Use the [official-topic coverage](COVERAGE_MATRIX.md) and [complete narration](SCRIPT_en-US.md) as the content map. These prepared items are independently authored; they make no prediction about question frequency and supply no recalled exam content.

For a scenario question, identify the required user task, constrained resource, observation point and units before choosing a technique name. DoS and DDoS concern deliberate availability interference; source distribution, resource pressure and malicious intent require distinct evidence. A source address does not uniquely identify a device or person.

Practice the distinction between a full link, packet-processing pressure, pending connection state, expensive application work and a shared dependency. Know the ordinary TCP handshake and what SYN cookies, compact state, timeouts or a proxy can and cannot protect. Compare reflection with direct traffic, and amplification with simple redirection. Retain the IP/Ethernet accounting boundary when dividing byte counts.

Select the control that can reach the constraint. Provider protection, source-address validation, restricted recursion, response limits, a CDN, a WAF, admission budgets, caching and dependency isolation serve different architectures and resources. A product category is not a universal guarantee. Legitimate users and rollback criteria belong in the validation.

Interpret tool roles by the evidence they can read: saved packet fields, flow summaries, interface counters, host state and defined service tasks. This package uses local analysis only. A successful parser does not prove attack execution, control efficacy or official Practical readiness.

Use [PRETEST](PRETEST.md) to find a real gap, preserve first choice/confidence, then review the separate key. [POSTTEST](POSTTEST.md) explicitly marks eight reused film items and two new transfers. Keep original, exposed, assisted and retest records separate. The existing 600-question bank and the declared P4 learner acceptance retain their own requirements; production of this package adds no first answers or accepted task.
""")

    write("TRACEABILITY.md", """# M10 teaching and acceptance traceability

Canonical speech: [SCRIPT_en-US.md](SCRIPT_en-US.md). Scene/audio interface: [scenes.json](scenes.json). Film items: [questions.json](questions.json), namespace M10-film-v1. Companion assessments: M10-source-v1, prepared content only. [Coverage data](coverage.json) enumerates every scene.

| Learning result | Scenes | Prepared diagnostic | Offline evidence or acceptance |
| --- | --- | --- | --- |
| Define availability and scope | S01–S06 | PRE01, PRE10; film Q01 / POST01 | Defined user task, denominator, authority and outcome boundary |
| Distinguish resource rates and traffic distribution | S07–S10,S13–S14 | PRE02; POST10 | Units, source uncertainty and resource explanation |
| Locate the WAN constraint | S11–S16,S34–S35,S43 | PRE03; film Q03 / POST03 | [E01](lab_mock/E01_wan_windows.csv), aligned offered/accepted/discarded accounting |
| Interpret state pressure | S17–S22,S44 | PRE04–PRE05; film Q04 / POST04 | [E02](lab_mock/E02_connection_state.csv), snapshot/interval distinction and 1% fraction |
| Explain reflected amplification and ownership | S23–S28,S45 | PRE06–PRE07; film Q02,Q05 / POST02,POST05 | [PCAP](lab_mock/E03_reflector_fixture.pcap), [observation contract](lab_mock/E03_observation_contract.json), consistent-layer ratios |
| Compute work demand and evaluate dependencies | S29–S33,S46 | PRE08–PRE09; film Q06 / POST06; POST09 | [E04](lab_mock/E04_request_work.csv), toy arithmetic and separate pool evidence |
| Make a reproducible protective decision | S36–S42,S47–S49 | PRE10; film Q07–Q08 / POST07–POST08; POST10 | Claim-to-source mapping, owner, proposal status, user check and rollback |
| Produce a bounded incident brief | S58 | [Student capstone](ASSESSMENT_STUDENT.md) | [Instructor rubric](ASSESSMENT_INSTRUCTOR.md), learner command/output and saved brief |

## Evidence layers

The [verifier](tooling/verify_evidence.py) establishes only the parsing and arithmetic described in [its actual local report](validation/evidence-verification.json). Case events and expected recovery values remain SIMULATED OUTPUT. The [motion references](examples/index.html) illustrate animation and timing; they contain no generated narration and prove no full-film delivery. A rendered master, human viewing/listening, learner first answers, accepted practical work and public media release each need their own evidence.

Record learner work in the [worksheet](WORKSHEET.md) and [closeout](CLOSEOUT.md). PRE/POST preparation and repeated film items do not add to the existing 600-bank first-answer count.
""")

    write("CLOSEOUT.md", """# M10 blank learner closeout

This is a blank record for an activated learning block. Current learner result: **not_recorded**. Source preparation and builder validation do not fill any field below.

Date/timezone: ____ · Learner: ____ · Topic/blocker: ____ · Actual used minutes: ____ · Remaining confirmed capacity: ____ · Agreed endpoint: ____.

## Conceptual assessment

Namespace and item IDs: ____ · Original actually answered / selected: ____ / ____ · Original correct / answered: ____ / ____ · Unanswered: ____ · Prior exposure/assistance: ____.

Confidence captured before key: ____ · Low-confidence correct items checked: ____ · Misconceptions and corrections: ____ · Varied retests completed / required: ____ / ____ · Retest correct / answered: ____ / ____ · Remaining corrections: ____.

Select the evidence-based posttest result after review: **pass / review / activation_needed**. Use pass for demonstrated understanding of the declared concepts with required corrections resolved; review for identified errors or incomplete correction; activation_needed where actual learner assessment or necessary execution has not occurred. State the evidence and any unresolved critical error: ____.

## Offline practical acceptance

Practical state, recorded independently: **planned / attempted / blocked / accepted**. Actual state: ____.

Input identities/hashes: ____ · Interpreter/tool and command: ____ · Actual output or blocker: ____ · Saved incident brief and calculations: ____ · Rubric checks: ____ · Reviewer: ____ · Acceptance evidence: ____.

A generated fixture, prepared scaffold, reading or package-builder parser run does not establish the learner's accepted task. Operational-control deployment and service recovery are separate from this offline exercise. Official readiness retains the current learning route's requirements.

## Next action and publication

Exact next question, varied retest or practical check: ____ · Owner: ____ · Required input/authority: ____ · Next activation condition: ____.

If the daily learning Blog route is active, record the learner's actual explanation, confirmed bilingual article and verified public URL through the existing route. Article review and publication remain partial until their own gates pass. No public media release or completed Blog is supplied by this template.

See [traceability](TRACEABILITY.md), the [worksheet](WORKSHEET.md) and [capstone rubric](ASSESSMENT_INSTRUCTOR.md). Keep source QA, film delivery, human viewing/listening, learner evidence and publication records distinct.
""")

    write("CONCEPT_CONNECTIONS.md", """# M10 concept and learning connections

The reusable reasoning chain is required task → finite resource → incoming demand → named observation → supported mechanism → control owner/location → two-sided validation → observed recovery. The [study guide](STUDY_GUIDE.md) supplies formulas; [E01–E04](lab_mock/README.md) ground the chain in connected offline evidence.

M03 and M04 help identify services and their exposure. M05 separates a suspected weakness from verified impact and a remediation claim. M06 connects resource symptoms to host state; M07 adds behavior and containment evidence. M08 explains packet directions, capture points and observation limits. M09 reinforces that plausible claims do not replace authority or independent verification. M10 applies those distinctions to availability and owner-specific response.

M11 distinguishes connection establishment from a protected application session. M12 examines what controls and telemetry can observe. M13–M15 connect server/application behavior and costly operations to service outcomes. M18 requires additional operational and safety stewardship when availability affects physical processes. M19 adds provider boundaries and shared responsibility. M20 preserves evidence identities through hashes while retaining the distinction between byte integrity and truth.

In the adopted local Practical map, P4 system attack analysis connects M06, M07, M10 and M12. M08 remains mapped to P3 traffic analysis; M09 supplies cross-cutting human risk. This package prepares an M10 offline incident brief but does not independently accept a P4 learner task or satisfy the official Practical domains.

The [coverage matrix](COVERAGE_MATRIX.md) links the lesson, [traceability map](TRACEABILITY.md) links the assessments and evidence, and [closeout](CLOSEOUT.md) records actual learner results. Existing 600-bank IDs, capacity limits, declared practical checks and publication gates retain their own owners and evidence.
""")
    return actual_words, len(rows)


BASE_CSS = """
@font-face{font-family:LocalSans;src:url('assets/fonts/LiberationSans-Regular.ttf')}
@font-face{font-family:LocalSans;src:url('assets/fonts/LiberationSans-Bold.ttf');font-weight:700}
*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;background:#F0EBE4;color:#292421;font-family:LocalSans,sans-serif}
.root,.clip{position:relative;width:100%;height:100%;overflow:hidden}.paper{position:absolute;inset:0;background:#F0EBE4}
.header{position:absolute;left:138px;top:76px;width:1510px}.eyebrow{font-size:26px;line-height:1.2;font-weight:700;margin:0}
h1{font-size:62px;line-height:1.12;margin:28px 0 0;font-weight:700;max-width:1510px}
.diagram{position:absolute;left:138px;top:300px;width:1500px;height:470px}.diagram svg{width:1500px;height:470px;overflow:visible}
svg text{font-family:LocalSans,sans-serif;fill:#292421;font-size:32px}svg .major{font-size:40px;font-weight:700}svg .small{font-size:30px}
.cue{position:absolute;left:138px;top:785px;width:1450px;font-size:32px;line-height:1.3;margin:0}
.foot{position:absolute;left:138px;top:860px;width:1460px;font-size:24px;line-height:1.2;margin:0}
.mascot{position:absolute;left:1680px;top:700px;width:130px;height:130px;object-fit:contain}
.arrive,.cue,.value,.packet{opacity:0}.fill{transform-origin:left center}.draw{fill:none;stroke:#C8755D;stroke-width:6;stroke-linecap:round;stroke-linejoin:round}
.question{position:absolute;left:138px;top:275px;width:1490px}.question h2{font-size:40px;line-height:1.2;margin:0 0 26px}
.question p{font-size:34px;line-height:1.25;margin:16px 0;padding:0}.hold,.answer{position:absolute;left:138px;top:740px;width:1470px;font-size:34px;line-height:1.25;opacity:0;margin:0}
.hold{padding:14px 22px;background:#F2D4B7}.answer{font-weight:700}.question{opacity:0}
"""


def wrap_example(eid, title, body, cue, tweens, has_audio=False):
    audio = ('<audio id="quiz-silence" src="assets/audio/silence_1s_48k_stereo.wav" '
             'data-start="6" data-duration="1" data-track-index="1"></audio>') if has_audio else ""
    cue_html = '<p class="cue">' + html.escape(cue) + '</p>' if cue else ""
    template = """<!doctype html>
<html lang="en-US"><head><meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="connect-src 'none'; form-action 'none'; base-uri 'none'">
<meta name="referrer" content="no-referrer"><title>@@TITLE@@</title><style>@@CSS@@</style></head>
<body><main class="root" data-composition-id="@@ID@@" data-width="1920" data-height="1080" data-duration="12">
<section id="@@ID@@-scene" class="clip" data-start="0" data-duration="12" data-track-index="0"><div class="paper"></div>
<header class="header"><p class="eyebrow">CEH M10 · NORTHSTAR · MOTION REFERENCE</p><h1>@@TITLE@@</h1></header>
@@BODY@@@@CUE@@<img class="mascot" src="assets/mascot/tally_point.png" alt="Original Tally">
<p class="foot">SIMULATED OUTPUT · illustrative timing · no generated narration · caption area kept clear</p></section>@@AUDIO@@</main>
<script src="assets/vendor/gsap.min.js"></script><script>
window.__timelines=window.__timelines||{};
document.fonts.ready.then(()=>{
 const tl=gsap.timeline({paused:true});
 for(const path of document.querySelectorAll('.draw')){
  const length=path.getTotalLength();path.style.strokeDasharray=String(length);path.style.strokeDashoffset=String(length);
 }
 @@TWEENS@@
 window.__timelines[@@ID_JSON@@]=tl;
 if(window.__hfForceTimelineRebind)window.__hfForceTimelineRebind();
});
</script></body></html>"""
    for token, value in {"@@TITLE@@": html.escape(title), "@@CSS@@": BASE_CSS,
                         "@@ID@@": html.escape(eid, quote=True), "@@BODY@@": body,
                         "@@CUE@@": cue_html, "@@AUDIO@@": audio,
                         "@@TWEENS@@": tweens, "@@ID_JSON@@": json.dumps(eid)}.items():
        template = template.replace(token, value)
    return template


def build_examples(questions):
    # Each reference keeps final positions authored in the SVG; GSAP transforms
    # explain the mechanism without measuring layout during a tween.
    resource_body = """<div class="diagram"><svg viewBox="0 0 1500 470" role="img" aria-label="Three CPU service-demand comparisons against an eight-core budget">
<text x="500" y="32">CPU core-seconds per second</text>
<path d="M500 68H1280 M500 193H1280 M500 318H1280" stroke="#DCD3C8" stroke-width="3" fill="none"/>
<g class="arrive"><text class="major" x="0" y="118">Ordinary</text><text x="0" y="158">100 RPS × 20 ms</text></g>
<g class="arrive"><text class="major" x="0" y="243">Incident</text><text x="0" y="283">120 RPS × 200 ms</text></g>
<g class="arrive"><text class="major" x="0" y="368">Legitimate surge</text><text x="0" y="408">300 RPS × 5 ms</text></g>
<rect class="fill f0" x="500" y="96" width="65" height="48" fill="#F2D4B7" stroke="#292421" stroke-width="3"/>
<rect class="fill f1" x="500" y="221" width="780" height="48" fill="#C8755D" stroke="#292421" stroke-width="3"/>
<rect class="fill f2" x="500" y="346" width="48.75" height="48" fill="#F2D4B7" stroke="#292421" stroke-width="3"/>
<g class="value v0"><text class="major" x="1320" y="134">2</text></g><g class="value v1"><text class="major" x="1320" y="259">24</text></g><g class="value v2"><text class="major" x="1320" y="384">1.5</text></g>
<g class="budget arrive"><path d="M760 60V416" stroke="#292421" stroke-width="4" stroke-dasharray="10 8"/><text x="760" y="455" text-anchor="middle">Budget: 8</text></g>
</svg></div>"""
    resource_js = """
 tl.fromTo('.arrive',{opacity:0,y:18},{opacity:1,y:0,duration:.45,stagger:.15,ease:'power2.out'},.3);
 tl.fromTo('.f0',{scaleX:0},{scaleX:1,duration:.9,ease:'power2.out'},1.5);tl.set('.v0',{opacity:1},2.4);
 tl.fromTo('.f1',{scaleX:0},{scaleX:1,duration:1.4,ease:'power2.out'},3.4);tl.set('.v1',{opacity:1},4.8);
 tl.fromTo('.f2',{scaleX:0},{scaleX:1,duration:.8,ease:'power2.out'},6);tl.set('.v2',{opacity:1},6.8);
 tl.fromTo('.cue',{opacity:0},{opacity:1,duration:.5,ease:'power1.out'},8.1);
 """

    tiles = "".join('<rect class="slot" x="' + str(1135 + c * 40) + '" y="' + str(180 + r * 43) + '" width="30" height="32" rx="3" fill="#C8755D" stroke="#292421" stroke-width="2"/>' for r in range(4) for c in range(8))
    tcp_body = """<div class="diagram"><svg viewBox="0 0 1500 470" role="img" aria-label="Schematic TCP handshake with separate simulated backlog and interval counters">
<defs><marker id="tcp-arrow" markerWidth="12" markerHeight="12" refX="10" refY="5" orient="auto"><path d="M0 0L10 5L0 10" fill="none" stroke="#C8755D" stroke-width="2"/></marker></defs>
<g class="arrive"><path d="M0 3L280 0L283 78L0 80Z" fill="#FFFAF3" stroke="#292421" stroke-width="4"/><text class="major" x="140" y="54" text-anchor="middle">Client</text></g>
<g class="arrive"><path d="M700 3L1000 0L1003 78L700 80Z" fill="#FFFAF3" stroke="#292421" stroke-width="4"/><text class="major" x="850" y="54" text-anchor="middle">Server</text></g>
<path d="M140 80V408 M850 80V408" fill="none" stroke="#B8B0A9" stroke-width="4"/>
<path class="draw syn" d="M140 145H850" marker-end="url(#tcp-arrow)"/><text class="syn-label arrive" x="495" y="128" text-anchor="middle">SYN</text>
<path class="draw synack" d="M850 240H140" marker-end="url(#tcp-arrow)"/><text class="synack-label arrive" x="495" y="223" text-anchor="middle">SYN + ACK</text>
<path class="draw ack" d="M140 335H850" marker-end="url(#tcp-arrow)"/><text class="ack-label arrive" x="495" y="318" text-anchor="middle">ACK</text>
<text class="small" x="0" y="455">Same window: 6,000 attempts; 60 completed</text>
<g class="backlog arrive"><rect x="1090" y="0" width="390" height="415" rx="10" fill="#FFFAF3" stroke="#292421" stroke-width="4"/><text x="1285" y="52" text-anchor="middle" font-weight="700">Half-open backlog</text><text class="major" x="1285" y="110" text-anchor="middle">1,024 / 1,024</text><text class="small" x="1285" y="150" text-anchor="middle">Snapshot occupancy</text>""" + tiles + """<text class="small" x="1285" y="390" text-anchor="middle">Tiles are schematic</text></g>
</svg></div>"""
    tcp_js = """
 tl.fromTo('.arrive',{opacity:0,y:14},{opacity:1,y:0,duration:.45,stagger:.12,ease:'power2.out'},.3);
 tl.to('.syn',{strokeDashoffset:0,duration:1.2,ease:'none'},1.5);
 tl.to('.synack',{strokeDashoffset:0,duration:1.2,ease:'none'},3.1);
 tl.to('.ack',{strokeDashoffset:0,duration:1.2,ease:'none'},4.7);
 tl.fromTo('.slot',{opacity:0},{opacity:1,duration:.15,stagger:.045,ease:'none'},5.8);
 tl.fromTo('.cue',{opacity:0},{opacity:1,duration:.5,ease:'power1.out'},8.6);
 """

    reflection_body = """<div class="diagram"><svg viewBox="0 0 1500 470" role="img" aria-label="Constructed reflected request and response with paired IP-byte amplification">
<defs><marker id="reflection-arrow" markerWidth="12" markerHeight="12" refX="10" refY="5" orient="auto"><path d="M0 0L10 5L0 10" fill="none" stroke="#C8755D" stroke-width="2"/></marker></defs>
<g class="arrive"><path d="M0 83L320 80L323 220L0 223Z" fill="#FFFAF3" stroke="#292421" stroke-width="4"/><text class="major" x="160" y="137" text-anchor="middle">Request origin</text><text class="small" x="160" y="184" text-anchor="middle">Constructed sender</text></g>
<g class="arrive"><path d="M590 83L950 80L953 220L590 223Z" fill="#F2D4B7" stroke="#292421" stroke-width="4"/><text class="major" x="770" y="137" text-anchor="middle">DNS reflector</text><text class="small" x="770" y="184" text-anchor="middle">Answers claimed source</text></g>
<g class="arrive"><path d="M1215 83L1490 80L1493 220L1215 223Z" fill="#FFFAF3" stroke="#292421" stroke-width="4"/><text class="major" x="1352" y="137" text-anchor="middle">Victim</text><text class="small" x="1352" y="184" text-anchor="middle">Receives reply</text></g>
<path class="draw request" d="M325 150H585" marker-end="url(#reflection-arrow)"/>
<path class="draw response" d="M958 150H1205" marker-end="url(#reflection-arrow)"/>
<rect class="packet packet-request" x="340" y="130" width="35" height="40" rx="4" fill="#E9B94D" stroke="#292421" stroke-width="3"/>
<rect class="packet packet-response" x="975" y="118" width="70" height="64" rx="4" fill="#E9B94D" stroke="#292421" stroke-width="3"/>
<g class="value paired"><text x="0" y="285">Request source is set to the victim in this fixture.</text><text class="major" x="0" y="367">60 IP bytes → 3,000 IP bytes</text><text class="major" x="900" y="367">3,000 ÷ 60 = 50×</text><text class="small" x="0" y="428">Reflector-side fixture · paired IP bytes · drawing not to scale</text></g>
</svg></div>"""
    reflection_js = """
 tl.fromTo('.arrive',{opacity:0,y:18},{opacity:1,y:0,force3D:false,duration:.5,stagger:.18,ease:'power2.out'},.3);
 tl.to('.request',{strokeDashoffset:0,duration:.8,ease:'none'},1.5);
 tl.set('.packet-request',{opacity:1},2.4);tl.fromTo('.packet-request',{x:0},{x:195,duration:1.2,ease:'none'},2.4);tl.set('.packet-request',{opacity:0},3.6);
 tl.to('.response',{strokeDashoffset:0,duration:.8,ease:'none'},4.3);
 tl.set('.packet-response',{opacity:1},5.2);tl.fromTo('.packet-response',{x:0},{x:160,duration:1.3,ease:'none'},5.2);tl.set('.packet-response',{opacity:0},6.5);
 tl.fromTo('.paired',{opacity:0},{opacity:1,duration:.5,ease:'power1.out'},7.1);
 tl.fromTo('.cue',{opacity:0},{opacity:1,duration:.5,ease:'power1.out'},8.6);
 """

    q = questions[0]
    correct_text = next(c["text"] for c in q["choices"] if c["letter"] == q["correct_letter"])
    question_body = '<div class="question"><h2>Q01. ' + html.escape(q["prompt"]) + '</h2>' + "".join('<p>' + c["letter"] + '. ' + html.escape(c["text"]) + '</p>' for c in q["choices"]) + '</div><p class="hold">Think: exact 1.000-second reference window [6, 7).</p><p class="answer">Answer ' + q["correct_letter"] + ': ' + html.escape(correct_text) + '.</p>'
    quiz_js = """
 tl.fromTo('.question',{opacity:0,y:12},{opacity:1,y:0,duration:.4,ease:'power2.out'},0);
 tl.set('.hold',{opacity:0},0);tl.set('.answer',{opacity:0},0);
 tl.set('.hold',{opacity:1},6);tl.set('.hold',{opacity:0},7);tl.set('.answer',{opacity:1},7);
 """
    examples = [
        dict(id="resource-budget", title="Request count does not measure work", body=resource_body,
             cue="Toy work demand: multiply request rate by service cost, then compare the resource budget.", tweens=resource_js,
             rules=["stat-bars-and-fills", "discrete-text-sequence"], scenes=["S29", "S30", "S46"]),
        dict(id="tcp-state", title="Connection state can fill below link capacity", body=tcp_body,
             cue="A full state snapshot differs from attempts and completions counted across a window.", tweens=tcp_js,
             rules=["svg-path-draw", "stat-bars-and-fills"], scenes=["S17", "S18", "S44"]),
        dict(id="reflection-path", title="Follow the claimed return address", body=reflection_body,
             cue="Match the IP layer; Ethernet counts have a different amplification ratio.", tweens=reflection_js,
             rules=["svg-path-draw", "discrete-text-sequence"], scenes=["S23", "S24", "S25", "S45"]),
        dict(id="quiz-one-second", title="Read every choice, then pause", body=question_body,
             cue="", tweens=quiz_js, rules=["discrete-text-sequence"], scenes=["S50"]),
    ]
    manifest = []
    for example in examples:
        eid = example["id"]
        for rel in ["fonts/LiberationSans-Regular.ttf", "fonts/LiberationSans-Bold.ttf",
                    "vendor/gsap.min.js", "mascot/tally_point.png"]:
            destination = R / "examples" / eid / "assets" / rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(R / "assets" / rel, destination)
        has_audio = eid == "quiz-one-second"
        if has_audio:
            silence = R / "examples" / eid / "assets/audio/silence_1s_48k_stereo.wav"
            silence.parent.mkdir(parents=True, exist_ok=True)
            with wave.open(str(silence), "wb") as out:
                out.setnchannels(2)
                out.setsampwidth(2)
                out.setframerate(48000)
                out.writeframes(bytes(48000 * 2 * 2))
            # Read the emitted reference; this verifies the reference file only.
            with wave.open(str(silence), "rb") as reference:
                assert (reference.getnchannels(), reference.getsampwidth(),
                        reference.getframerate(), reference.getnframes()) == (2, 2, 48000, 48000)
                assert not any(reference.readframes(reference.getnframes()))
            dump(f"examples/{eid}/timing.json", dict(
                reference_only=True, generated_narration=False, question_namespace=FILM_NS,
                question_id="Q01", illustration_duration_seconds=12,
                hold_interval_seconds=[6, 7], interval_convention="start inclusive, end exclusive",
                silence=dict(path="assets/audio/silence_1s_48k_stereo.wav", sample_rate=48000,
                             channels=2, sample_width_bytes=2, frames=48000, all_samples_zero=True),
                boundary_contract="hold visible at 6 <= t < 7; answer hidden before 7 and visible at t >= 7",
                evidence_limit="Measured PCM reference and authored visual thresholds, not measured spoken-question timing or a rendered full-film result."))
        dump(f"examples/{eid}/hyperframes.json", dict(width=1920, height=1080, fps=30, duration=12))
        write(f"examples/{eid}/index.html", wrap_example(eid, example["title"], example["body"], example["cue"], example["tweens"], has_audio))
        manifest.append(dict(id=eid, title=example["title"], path=eid + "/index.html",
                             duration_seconds=12, scenes=example["scenes"], rules=example["rules"],
                             generated_narration=False, external_assets=False,
                             timeline_id=eid, status="authored_reference_pending_browser_validation"))
    dump("examples/manifest.json", dict(module="M10", examples=manifest,
                                       validation_boundary="Builder writes references; actual runtime, seek, layout and contrast checks are separate."))
    options = "".join('<option value="' + x["id"] + '">' + html.escape(x["title"]) + '</option>' for x in examples)
    write("examples/index.html", """<!doctype html><html lang="en-US"><head><meta charset="utf-8"><title>M10 local motion references</title>
<meta http-equiv="Content-Security-Policy" content="connect-src 'none'; form-action 'none'; base-uri 'none'">
<style>@font-face{font-family:LocalSans;src:url('resource-budget/assets/fonts/LiberationSans-Regular.ttf')}*{box-sizing:border-box}body{font:20px/1.4 LocalSans,sans-serif;background:#F0EBE4;color:#292421;margin:28px}h1{font-size:36px}select,button,input{font:inherit}select{max-width:600px}input{width:450px;vertical-align:middle}.viewport{width:960px;height:540px;overflow:hidden;border:2px solid #292421;margin-top:22px}iframe{width:1920px;height:1080px;border:0;transform:scale(.5);transform-origin:top left}output{display:inline-block;min-width:90px}.controls{display:flex;gap:14px;align-items:center;flex-wrap:wrap;max-width:1200px}.boundary{margin-top:14px}p{max-width:1120px}</style></head>
<body><h1>M10 seekable motion references</h1><p>Four local 12-second examples. Drag in either direction. These illustrative timings contain no generated narration; the full film follows measured speech. All assets are bundled, and no requests are sent to outside services.</p>
<div class="controls"><label>Example <select id="which">""" + options + """</select></label><label>Time <input id="seek" type="range" min="0" max="12" step="0.001" value="0"></label><output id="time">0.000 s</output></div>
<div class="boundary"><button data-time="5.999">Before hold</button> <button data-time="6">Hold start</button> <button data-time="6.5">Hold middle</button> <button data-time="6.999">Before answer</button> <button data-time="7">Answer start</button> <button data-time="0">Reset</button></div>
<p id="state">Open a local example and move the scrubber. Boundary buttons use the quiz example's illustrative six-to-seven-second hold.</p>
<div class="viewport"><iframe id="frame" title="M10 motion example" src="resource-budget/index.html"></iframe></div>
<p><a href="README.md">Reference and validation contract</a> · <a href="../TRACEABILITY.md">Lesson connections</a></p>
<script>
const frame=document.querySelector('#frame'), seek=document.querySelector('#seek'), which=document.querySelector('#which'), output=document.querySelector('#time'), state=document.querySelector('#state');
function seekTo(value){const t=Math.max(0,Math.min(12,Number(value)));seek.value=String(t);output.value=t.toFixed(3)+' s';const timeline=frame.contentWindow.__timelines?.[which.value];if(timeline){timeline.seek(t,false);state.textContent=which.value==='quiz-one-second'?(t<6?'Question and all choices; hold and answer hidden.':t<7?'Hold visible; answer hidden.':'Hold hidden; answer visible.'):'Paused native timeline at '+t.toFixed(3)+' seconds.';}else{state.textContent='Timeline is loading; move the scrubber after local fonts are ready.';}}
which.addEventListener('change',()=>{seek.value='0';output.value='0.000 s';frame.src=which.value+'/index.html';state.textContent='Loading local assets.';});
seek.addEventListener('input',()=>seekTo(seek.value));for(const button of document.querySelectorAll('[data-time]'))button.addEventListener('click',()=>seekTo(button.dataset.time));window.seekExample=seekTo;
</script></body></html>""")
    write("examples/README.md", """# M10 native motion references

Open [the local scrubber](index.html) through the package's local preview server. It embeds the full 1920×1080 canvas and scales the viewport for inspection without changing authored coordinates. Each example is a separate 12-second HyperFrames composition with one paused GSAP timeline registered under the root composition ID. Assets are physically copied: approved Tally, Liberation Sans regular/bold and GSAP. The package's licenses retain their provenance. No external assets or network APIs are used; connection requests are disabled by the page policy.

| Example | Teaching motion | Lesson connection |
| --- | --- | --- |
| [Resource budget](resource-budget/index.html) | Work bars compare 2, 24 and 1.5 core-seconds/second against an eight-core budget. | S29,S30,S46 |
| [TCP state](tcp-state/index.html) | Handshake paths draw separately from full half-open state and interval totals. Grid tiles are schematic, not 1,024 individually drawn entries. | S17,S18,S44 |
| [Reflection path](reflection-path/index.html) | A constructed request and larger reply traverse the correct actors; paired IP counts yield 50×. Packet drawings are not to scale. | S23–S25,S45 |
| [Quiz one second](quiz-one-second/index.html) | The complete Q01 remains visible; the hold is shown at 6 ≤ t < 7 and the answer from t = 7. | S50; M10-film-v1/Q01 |

The quiz includes a separately verified 48 kHz, stereo, 16-bit, 48,000-frame zero PCM reference placed at [6,7). This measures the reference file and defines visual thresholds. There is no generated narration, so six seconds does not claim that the spoken question fits that interval. The final film must derive the hold position from its actual complete spoken stem and options.

After building, run actual HyperFrames runtime/layout/contrast checks and test repeated and backward seeks. For the quiz, test 0, 5.999, 6, 6.5, 6.999, 7 and a late frame, then repeat them backward. Verify that hold and answer never overlap and compare identical-time snapshots after different seek histories. Inspect each diagram's complete late state and its lower caption clearance. The builder marks references as pending browser validation; authored HTML alone does not establish those results.

[Machine-readable reference manifest](manifest.json) · [Quiz timing contract](quiz-one-second/timing.json) · [Learning traceability](../TRACEABILITY.md).
""")
    return len(examples)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-progress", action="store_true", help="Keep only the final JSON on stdout.")
    parser.add_argument("--json", action="store_true", help="Emit the final JSON without human progress events.")
    args = parser.parse_args()
    started = time.perf_counter()
    progress = not (args.no_progress or args.json)
    if progress:
        print("[M10 companions] Reading completed scene/quiz inputs; building guides and four local motion references.", file=sys.stderr, flush=True)
    scene_data = json.loads((R / "scenes.json").read_text(encoding="utf-8"))
    scenes = scene_data["scenes"]
    question_data = json.loads((R / "questions.json").read_text(encoding="utf-8"))
    questions = question_data["questions"]
    assert [s["id"] for s in scenes] == [f"S{i:02}" for i in range(1, 59)]
    assert [q["id"] for q in questions] == [f"Q{i:02}" for i in range(1, 9)]
    assert [q["scene_id"] for q in questions] == [f"S{i:02}" for i in range(50, 58)]
    assert question_data["namespace"] == FILM_NS
    assert all(q["silent_think_seconds"] == 1 for q in questions)
    for q in PRETEST + TRANSFER:
        assert len(q["choices"]) == 4
        assert [c["letter"] for c in q["choices"]] == list("ABCD")
        assert q["correct_letter"] in "ABCD"
    actual_words, coverage_rows = build_documents(scenes, questions)
    example_count = build_examples(questions)
    required = ["ASSESSMENT_STUDENT.md", "ASSESSMENT_INSTRUCTOR.md", "STUDY_GUIDE.md",
                "WORKSHEET.md", "PRETEST.md", "PRETEST_KEY.md", "POSTTEST.md",
                "POSTTEST_KEY.md", "EXAM_FOCUS.md", "TRACEABILITY.md", "CLOSEOUT.md",
                "COVERAGE_MATRIX.md", "coverage.json", "CONCEPT_CONNECTIONS.md",
                "examples/index.html", "examples/manifest.json", "examples/README.md"]
    required += [f"examples/{name}/index.html" for name in
                 ("resource-budget", "tcp-state", "reflection-path", "quiz-one-second")]
    assert all((R / name).is_file() and (R / name).stat().st_size > 0 for name in required)
    elapsed = round(time.perf_counter() - started, 3)
    if progress:
        print(f"[M10 companions] Completed {len(required)} required nonempty outputs in {elapsed:.3f}s; browser validation remains pending.", file=sys.stderr, flush=True)
    print(json.dumps(dict(stage="companions_built", module="M10", canonical_spoken_words=actual_words,
                          prepared_pretest_items=10, prepared_posttest_items=10,
                          film_items=8, source_namespace=SOURCE_NS, film_namespace=FILM_NS,
                          motion_examples=example_count, official_topic_rows=coverage_rows,
                          learner_progress_recorded=False, generated_narration=False,
                          required_nonempty_outputs=len(required), elapsed_seconds=elapsed,
                          browser_validation="not_run_by_builder", full_film_rendered="not_claimed")))


if __name__ == "__main__":
    main()
