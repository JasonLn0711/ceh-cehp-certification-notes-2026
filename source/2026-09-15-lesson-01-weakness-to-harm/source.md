## Lesson 1: How a weakness can lead to harm

Start with this question:

**What should a system allow—and what can it accidentally allow instead?**

The gap between those two things is where many security problems begin. For example, access-control weaknesses can let people read or change information outside their permissions. ([OWASP Foundation][1])

### One situation to keep in mind

**Hypothetical example:** A university website stores students’ private feedback.

The intended rule is:

> Each student can read only their own feedback.

However, the website checks only whether a person has logged in. It does not check whether that person is allowed to read the particular document they requested.

Imagine a records clerk who asks, “Are you a student?” but never asks, “Are these records yours?”

Keep that situation in mind. We will examine it through four connected concepts.

## 1. Vulnerability: the weakness that makes harm possible

A **vulnerability** is a weakness that could allow a security problem. It can exist in software, settings, design, or a process—not just in computer code. ([NIST Computer Security Resource Center][2])

In our example, the vulnerability is:

> **The website does not check permission before returning a private document.**

Here is how the weakness works. The website receives a request, checks that the user has logged in, and returns the requested document. It leaves out a necessary decision: whether this user may read this document.

That missing decision matters because the website can behave exactly as programmed while still violating its intended security rule.

There are two related terms:

**Authentication** checks identity: “Who are you?”

**Authorization** checks permission: “Are you allowed to do this?”

Our hypothetical website has a working identity check but a broken permission check. OWASP describes access control as enforcing the limits on what a user may do. ([OWASP Foundation][1])

**Common mistake:** “Nobody has used the weakness, so there is no vulnerability.”

The weakness does not appear only when an attack happens. An attack may reveal or use a weakness that was already present. This follows from the definition: a vulnerability is something that *could* be exploited or triggered. ([NIST Computer Security Resource Center][2])

**Connection to the next concept:** A vulnerability explains what is weak. It does not yet explain what might cause harm.

## 2. Threat: the possibility of a harmful event

A **threat** is a circumstance or event that could cause harm. A **threat actor** is a person or group that poses a threat. Not every threat involves an attacker; accidents can also cause harm. ([NIST Computer Security Resource Center][3])

In our hypothetical example:

> A student might deliberately access another student’s private feedback.

The student is the **threat actor**. The possible unauthorized access is the **threat event**.

Why does this distinction matter? Because the person and the weakness are different things.

Imagine that the university removes the missing permission check. The same student might still want private information, but this particular opportunity would no longer be available.

Or imagine that the student leaves the university. The missing permission check would still exist.

**Common mistake:** “The threat is the software bug.”

The bug is the vulnerability. The potential harmful activity is the threat. Keeping these separate helps us distinguish the weakness we can repair from the activity we need to defend against. ([NIST Computer Security Resource Center][2])

**Connection to the next concept:** A threat describes what might happen. An exploit describes a way to make it happen by using a weakness.

## 3. Exploit: a way to use the weakness

An **exploit** is a method or piece of code that takes advantage of a vulnerability. **Exploitation** is the act of using it. An exploit can be as simple as a request that takes advantage of a missing permission check; it does not have to be a large or complicated program. OWASP gives examples of requests that access another user’s information when permission checks are missing. ([OWASP Foundation][1])

In our hypothetical example:

> A student requests someone else’s private document, and the website returns it because the permission check is missing.

Notice the separation:

The **missing check** is the weakness.

The **request that takes advantage of it** is the exploit method.

The **unauthorized disclosure** is the harmful result.

This distinction matters because repairing the weakness and blocking one particular request are not necessarily the same response. In our example, the intended fix is to enforce the permission rule—not merely reject one document request we happened to observe.

**Common mistake:** “The exploit and the vulnerability are the same thing.”

Think of our records-clerk analogy. The clerk’s failure to check ownership is the weakness. Asking the clerk for someone else’s records is a way to take advantage of it.

**Connection to the next concept:** Even after we understand an exploit, we still need to ask how likely harm is and how much it would matter.

## 4. Risk: how likely the harm is, and how serious it would be

**Risk** concerns the likelihood of a harmful event and the seriousness of its consequences. **Likelihood** means how likely it is to happen. **Impact** means how much harm it would cause. ([NIST Computer Security Resource Center][4])

Risk matters because finding a weakness is not enough to decide what to fix first.

Consider two **hypothetical** copies of our website.

**Copy A** is an isolated classroom demonstration. It contains invented names and invented feedback. Only the instructor can reach it.

**Copy B** is the real university service. Thousands of students can use it, and it contains confidential evaluations.

Both copies have the same missing permission check.

Under those stated conditions, I would treat Copy B as the more urgent concern. More people can reach the weakness, and the information at stake is more important.

This shows how the concepts connect:

> **Risk depends on the weakness, possible harmful activity, access to the system, and consequences—not just the existence of a bug.**

A related term is **severity**, which describes how serious a vulnerability is technically. FIRST, the organization that maintains CVSS, warns that a CVSS Base severity score alone is not a complete risk assessment. ([FIRST][5])

**Common mistake:** “Same vulnerability means same risk.”

Our two copies show why that does not follow. The weakness is the same; the circumstances are different.

Another mistake is treating uncertainty as proof of safety. “We do not know whether anyone has tried this” is different from “We have good evidence that harmful use is unlikely.”

## A real incident that connects the concepts

**Documented example: Equifax, 2017.**

In its July 22, 2019 settlement announcement, the US Federal Trade Commission described the 2017 Equifax breach as affecting approximately **147 million people**. The FTC alleged that Equifax received a vulnerability warning in **March 2017** but failed to ensure the necessary fixes were completed. Attackers used the weakness to enter the network, then used exposed administrative login information to gain access to sensitive personal data. Suspicious traffic was detected in **July 2017**. ([Federal Trade Commission][6])

**Applying our model:** The uncorrected weakness was the vulnerability. The attackers were threat actors. Their method of using the weakness was exploitation. Before the theft, the possibility of serious information loss was a risk; the theft itself was an actual harmful outcome.

The teaching lesson is:

**A weakness, an attack method, and a harmful outcome are connected—but they are not interchangeable.**

## Put the model into one sentence

For a deliberate attack, a useful model is:

> **An attacker may use an exploit to take advantage of a vulnerability and cause harm. Risk asks how likely that harm is and how serious it would be in this situation.** ([NIST Computer Security Resource Center][2])

This is the foundation for the rest of vulnerability analysis. We first need to understand the possible failure before we can choose how to assess it or respond to it.

### Your turn: explain it back

Return to our hypothetical university website. A student says:

> “Nobody has stolen any documents yet, so the website has no vulnerability and no risk.”

**How would you correct that statement in three to five simple English sentences?**

Explain what the weakness is, how someone could take advantage of it, and why harm does not have to happen before risk exists. Finish with your confidence: **low, medium, or high**.

[1]: https://owasp.org/Top10/2021/A01_2021-Broken_Access_Control/ "A01 Broken Access Control - OWASP Top 10:2021"
[2]: https://csrc.nist.gov/glossary/term/vulnerability "vulnerability - Glossary | CSRC"
[3]: https://csrc.nist.gov/glossary/term/threat "threat - Glossary | CSRC"
[4]: https://csrc.nist.gov/glossary/term/risk "risk - Glossary | CSRC"
[5]: https://www.first.org/cvss/v4.0/user-guide "CVSS v4.0 User Guide"
[6]: https://www.ftc.gov/news-events/news/press-releases/2019/07/equifax-pay-575-million-part-settlement-ftc-cfpb-states-related-2017-data-breach "Equifax to Pay $575 Million as Part of Settlement with FTC, CFPB, and States Related to 2017 Data Breach | Federal Trade Commission"
