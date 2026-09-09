Please continue with next question.

### Question 3 of 10 — Integrity coverage

In the continuation, `SHA256SUMS.txt` covered 13 evidence files. The manifest itself and `hash-verification.txt` were created afterward and were not included in that same manifest.

Which statement is correct?

**A.** Because `SHA256SUMS.txt` was not hashed by itself, none of the evidence hashes are useful.

**B.** The manifest verifies the integrity of the 13 files it explicitly covers; it does not automatically establish the integrity of files outside that coverage.

**C.** `hash-verification.txt` proves the evidence is authentic and that every observation in the files is true.

**D.** Once a file receives a SHA-256 hash, it can never be modified.

Your answer and confidence: **low, medium, or high**?


answer: B.
confidence: medium

Correct — **B**.

The key idea is **integrity coverage**: a hash manifest only says something about the exact files listed in it.

If `SHA256SUMS.txt` contains hashes for 13 files, then later `sha256sum -c SHA256SUMS.txt` can tell you whether those 13 files still match their recorded hashes.

It does **not** automatically prove:

* that files outside the manifest are unchanged,
* that the evidence is authentic,
* that the observations written inside are true,
* or who created the files.

Because your confidence was medium, keep this mental model:

> **Hash = “same bytes as before,” not “true story.”**

Progress:

* Original questions completed: **3/10**
* Score: **3/3**
* Confidence: high, medium, medium
* Retests: **0**

### Question 4 of 10 — Authorization boundary

Suppose you now want to send:

```text
GET /admin
```

to `127.0.0.1:8766`.

The active ROE only allowed HTTP GET requests to `/health` and `/service-info`.

Which statement is correct?

**A.** `/admin` is allowed because the host and port are already authorized.

**B.** `/admin` is allowed if the request is read-only.

**C.** `/admin` is outside the current authorized method/path scope and requires a new dated authorization before use.

**D.** `/admin` is allowed because no credential testing is involved.

Your answer and confidence?


answer: C.
confidence: high

Correct — C.

Authorization is not only about the host and port. It also includes the method and path.

Here, the allowed HTTP scope was limited to:

/health
/service-info

So /admin would be a scope change, even though 127.0.0.1:8766 is still the same target.

A useful rule:

Same host does not mean same authorization.

Progress:

Original questions completed: 4/10
Score: 4/4
Confidence: high, medium, medium, high
Retests: 0
Question 5 of 10 — Observation vs inference

Suppose the response body says:

{
  "owner": "Unassigned",
  "role": "legacy-reporting"
}

Which statement is an inference, rather than a direct observation?

A. The response contained the field "owner": "Unassigned".

B. The response contained the field "role": "legacy-reporting".

C. The service is missing clear organizational ownership and should be investigated as an ownership gap.

D. The request returned JSON.

Your answer and confidence?

answer: C.
confidence: high

Correct — C.

A direct observation is something the artifact literally shows, such as:

the JSON contained "owner": "Unassigned"
the JSON contained "role": "legacy-reporting"

The statement that this represents an ownership gap worth investigating is an inference. It is supported by evidence, but it goes one step beyond merely repeating the response.

A compact mental model:

Observation = what the artifact says.
Inference = what you reasonably conclude from multiple observations.

Progress:

Original questions completed: 5/10
Score: 5/5
Confidence: high, medium, medium, high, high
Retests: 0
Question 6 of 10 — Evidence limits

You have these facts:

8766/tcp was observed open.
/service-info returned version = 0.8.1.
The service is absent from the supplied register.

Which conclusion is justified?

A. Version 0.8.1 is vulnerable because the asset is undocumented.

B. The service is exploitable because it exposes version information.

C. The evidence supports reachability, self-reported version metadata, and an inventory gap; vulnerability and exploitability remain unverified.

D. The service must be obsolete because the version begins with 0.

Your answer and confidence?

answer: C.
confidence: high

Correct — C.

That answer keeps three different claims separate:

Reachability: 8766/tcp was open.
Self-reported metadata: the service reported version 0.8.1.
Inventory state: the register omitted 8766.

None of those facts alone proves a vulnerability or exploitability.

Progress:

Original questions completed: 6/10
Score: 6/6
Retests: 0
Question 7 of 10 — Historical evidence vs current process

You have a saved historical file:

attempt-2026-09-09-1622/mock-server.pid

It contains a PID from the earlier session.

What is the safest interpretation?

A. It identifies the current mock process because the filename is trustworthy.

B. It is historical evidence of the PID used in that prior attempt, but it must not be assumed to identify any current process.

C. It can be reused if the same ports are used again.

D. It becomes valid again after the new mock starts.

Your answer and confidence?

answer: B. 
confidence: medium

Correct — B.

The historical PID file is evidence about the previous attempt, not a control handle for a current process.

Why this matters: a PID is only meaningful while that specific process exists. After it exits, the operating system may eventually reuse the same number for another process. So the safe pattern is:

capture a fresh PID → verify the command behind that PID → control that verified process

Your medium confidence is reasonable here. The key distinction is:

historical PID = evidence
current verified PID = operational control

Progress:

Original questions completed: 7/10
Score: 7/7
Confidence: high, medium, medium, high, high, high, medium
Retests: 0
Question 8 of 10 — Transfer to another situation

Imagine a real company where an internal service is reachable and reports:

owner = Finance
version = 3.2.4

but the company’s authoritative asset register has no entry for that service.

What is the best next conclusion?

A. Finance definitely owns the service because the service says so.

B. The service is vulnerable because it is undocumented.

C. There is an inventory discrepancy; the self-reported owner is a lead that should be validated through authoritative organizational evidence.

D. The service should immediately be exploited to determine its real owner.

Your answer and confidence: low, medium, or high?

answer: C.
confidence: high.

Correct — C.

The right move is to treat the service-reported owner as a lead, not as final proof. The authoritative register and other organizational records still matter.

Progress:

Original questions completed: 8/10
Score: 8/8
Incorrect answers: 0
Retests: 0
Question 9 of 10 — Process verification

Suppose you start a mock and capture PID 45000. Before shutting it down, you run:

ps -p 45000 -o pid=,args=

and the output shows:

45000 /usr/bin/python3 unrelated_script.py

What should you do?

A. Kill PID 45000 anyway because it matches the saved PID.

B. Stop and do not kill it, because the current process identity does not match the intended mock.

C. Restart the mock and reuse PID 45000.

D. Ignore the mismatch if ports 8765–8767 are listening.

Your answer and confidence?

answer: B.
confidence: low

Correct — B.

Your low confidence is worth addressing because this is an important operational safety rule.

The saved PID tells you which process number you intended to control. But before sending a terminating signal, you should verify what that PID represents now.

If:

PID 45000

currently maps to:

/usr/bin/python3 unrelated_script.py

then the evidence no longer supports the claim that PID 45000 is your mock. Sending:

kill -TERM 45000

could terminate an unrelated process.

The safe sequence is:

saved PID → inspect current PID identity → compare with expected process → only then act

This is another example of separating identifier from identity. A PID is merely a number assigned to a process instance; the number itself is not durable proof of what the process is.

Progress:

Original questions completed: 9/10
Score: 9/9
Q9 confidence: low
Incorrect answers: 0
Remediation retests: 0
Question 10 of 10 — Evidence integrity failure

Hypothetically, after creating a continuation hash manifest, you later run:

sha256sum -c SHA256SUMS.txt

and receive:

metadata-comparison.md: FAILED

What is the best response?

A. Immediately regenerate SHA256SUMS.txt so every file reports OK.

B. Delete metadata-comparison.md because failed integrity means the file is useless.

C. Preserve the failed verification result, investigate why the file changed, and do not replace the original manifest merely to make verification pass.

D. Ignore the failure because SHA-256 sometimes changes randomly between checks.

Your answer and confidence: low, medium, or high?

answer: C.
confidence: high.

Correct — **C**.

A hash manifest is a recorded integrity baseline. If later verification says:

```text
metadata-comparison.md: FAILED
```

the correct interpretation is:

> The current bytes of `metadata-comparison.md` no longer match the bytes represented by the hash stored in the original manifest.

That is something to investigate, not something to hide.

Regenerating the manifest immediately would answer a different question—“what are the hashes now?”—while destroying your ability to compare the current file against the original baseline.

A proper response would be:

1. Preserve the original `SHA256SUMS.txt`.
2. Preserve the `FAILED` verification output.
3. Determine whether the file changed intentionally, accidentally, or unexpectedly.
4. Compare timestamps, version control, backups, or other evidence.
5. If a legitimate new version needs sealing, create a **new dated manifest** while retaining the old one.

Important distinction:

> **Integrity failure means “the bytes changed relative to the recorded baseline.”**
> It does not automatically mean malicious tampering.

Your answer is correct with high confidence.

### New continuation diagnostic — final result

This diagnostic is separate from your earlier 10/10.

* Original questions: **10/10 completed**
* Score: **10/10**
* Incorrect original answers: **0**
* Remediation retests: **0**
* Confidence:

  * High: **6**
  * Medium: **3**
  * Low: **1**

Your one low-confidence area was **process identity before termination**. You nevertheless answered correctly, and we clarified the transferable rule:

> A PID is an identifier for a process instance, not durable proof of process identity.

You demonstrated understanding of:

* self-reported metadata versus verified organizational facts,
* PID reuse and current-process verification,
* SHA-256 integrity coverage,
* authorization by host, port, method, and path,
* observation versus inference,
* vulnerability/evidence limits,
* historical versus current operational evidence,
* ownership verification in real organizations,
* safe process termination,
* and preserving integrity failures rather than rewriting history.

So the continuation diagnostic criterion is **met**.

The weekly project is still not automatically “accepted,” because the repository’s acceptance check separately requires the mapped **M02–M04 diagnostics** and any still-open **M01 safety repair**, in addition to the technical evidence.

The smallest next action is now to inspect the repository’s mapped M02–M04/M01 assessment state and identify the **single remaining acceptance gate**, rather than doing more reconnaissance.
