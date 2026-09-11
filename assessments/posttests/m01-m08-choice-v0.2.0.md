# Current and next module checks — M01–M08

Form `module_choice_posttest` v0.2.0; original author-written pilot items.
Administer only the named module, one question at a time, closed-book with
choice and low/medium/high confidence. Stop at the agreed endpoint; no feedback
until original scoring. Reading a complete module ahead of administration
counts as exposure: use a fresh version for a formal attempt.

The tutor uses the separate instructor key; do not open it during an attempt.
[Scoring and remediation contract](module-posttest-template.md).

M01–M04 map to W37 (M01 may use W36 evidence); M05–M08 map to W38.
These questions assess selected-response interpretation; independent project
evidence remains required. They are not official EC-Council exam questions.

## M01

### M01-C01

A test owner gives verbal encouragement but the written target list is missing. What is the next step?

- A. Obtain written scope before testing
- B. Infer scope from the company domain
- C. Start with a low-rate scan
- D. Ask a colleague to choose targets

### M01-C02

Which record defines permitted methods and stopping conditions?

- A. The final vulnerability severity list
- B. The scanner's default configuration
- C. The agreed Rules of Engagement
- D. The vendor's general user manual

### M01-C03

A scan report contains an IP absent from the authorized list. What does its presence establish?

- A. Permission to enumerate that host
- B. An observation requiring a scope check
- C. Ownership by the authorizing manager
- D. Approval for a vulnerability test

### M01-C04

A saved manifest matches three files. What conclusion is supported?

- A. Every project file is authentic
- B. The report's conclusions are correct
- C. The server owner approved the test
- D. Those files match that manifest

### M01-C05

A log shows a permitted request within the agreed window. What must still be checked?

- A. Whether the tool is widely used
- B. Whether the response looks useful
- C. Target and method and request limits
- D. Whether the address is reachable

### M01-C06

Which report action best handles an uncertain finding?

- A. Label the uncertainty and needed validation
- B. Publish the strongest possible claim
- C. Remove all uncertain observations
- D. Repeat testing outside the window

### M01-C07

A scope amendment is approved after an earlier excluded action. How should the earlier action be recorded?

- A. As authorized by the later amendment
- B. As harmless if no damage was seen
- C. As irrelevant to the final report
- D. As an earlier scope violation

### M01-C08

A listed service redirects to an unlisted host. What should the learner do?

- A. Follow because the first host allowed it
- B. Stop before following and clarify scope
- C. Follow once without saving output
- D. Treat all redirect destinations as listed

### M01-C09

The active window expired while a tool was paused. What permits another request?

- A. A fresh dated authorization window
- B. The original command still being open
- C. A low expected request count
- D. The absence of a service error

### M01-C10

A new synthetic case permits one GET but the previous case allowed two. Which limit applies?

- A. The previous case's two-request limit
- B. The new case's one-request limit
- C. The tool's automatic retry limit
- D. Whichever limit produces useful output

## M02

### M02-C01

Which action is passive reconnaissance in this supplied-evidence exercise?

- A. Connecting to each listed TCP port
- B. Reading the provided asset register
- C. Requesting the service-info endpoint
- D. Sending a version-detection probe

### M02-C02

What distinguishes active reconnaissance from passive review here?

- A. It always requires exploitation
- B. It always obtains confidential data
- C. It guarantees accurate ownership
- D. It interacts with the target

### M02-C03

A supplied register omits a historically reachable service. What is supported?

- A. A confirmed compromise
- B. An unauthorized business service
- C. An inventory discrepancy
- D. A verified exploitable weakness

### M02-C04

A public profile names a system administrator. What can it establish alone?

- A. A public claim about a role
- B. Current authorization to test systems
- C. Verified ownership of every service
- D. Permission to contact employees

### M02-C05

A cached page names an old product version. What is the best next evidence step?

- A. Treat the cached version as current
- B. Assume the version is vulnerable
- C. Discard every observation from the page
- D. Verify currency within authorized scope

### M02-C06

Which defensive response addresses unnecessary public exposure?

- A. Block all internal event logging
- B. Review and reduce unnecessary published details
- C. Publish credentials only briefly
- D. Rely on obscure hostnames alone

### M02-C07

Two sources disagree about the service owner. What should be reported?

- A. Both sources and the unresolved ownership
- B. Only the newest-looking name
- C. An inferred owner without qualification
- D. No inventory gap because names exist

### M02-C08

The brief allows supplied documents only. May the learner query a live host?

- A. Yes; if the query is read-only
- B. Yes; if the host uses a public address
- C. No; obtain explicit active-test scope first
- D. Yes; if the tool calls it discovery

### M02-C09

A source unexpectedly contains personal credentials. What is the next step?

- A. Test one credential to assess impact
- B. Stop and follow the evidence-handling rule
- C. Paste the source into a public AI tool
- D. Include the values in the reusable packet

### M02-C10

A synthetic subsidiary shares a parent company's branding. What can be inferred about testing scope?

- A. The parent scope automatically includes it
- B. All related domains share the same owner
- C. Branding does not establish authorization
- D. Passive discovery permits later scanning

## M03

### M03-C01

What does an open TCP port establish at the time of a successful connect scan?

- A. The service is vulnerable to a known exploit
- B. The host's organizational owner is verified
- C. A connection was accepted at that endpoint
- D. The application version is current

### M03-C02

What does Nmap -sT use for a TCP connect scan?

- A. The operating system's connect operation
- B. Only previously cached DNS records
- C. An HTTP request to every discovered port
- D. Only passive listening on an interface

### M03-C03

The saved scan says SERVICE=amcs for port 8766 without version detection. What is this?

- A. Verified application identity
- B. The service's accountable owner
- C. A confirmed product vulnerability
- D. A preliminary port-to-name label

### M03-C04

A packet filter gives no response to a probe. What is the appropriate conclusion?

- A. The host is definitely powered off
- B. The observation has multiple possible causes
- C. The port is definitely open
- D. The operating system is identified

### M03-C05

Yesterday's scan observed a port open. What does that say about its state now?

- A. A new authorized check is needed for current state
- B. It remains open until a patch is installed
- C. It is closed if the tool has exited
- D. It is unchanged if the IP is unchanged

### M03-C06

Which action reduces unnecessary exposed services?

- A. Rename every port in a local database
- B. Hide the scan output from the team
- C. Disable unneeded listeners through approved change
- D. Use a random hostname without review

### M03-C07

A scan result and service metadata disagree. What should the analyst do?

- A. Overwrite the scan label with a guess
- B. Preserve both and validate the interpretation
- C. Declare the metadata source malicious
- D. Choose whichever suggests higher severity

### M03-C08

Authorization lists only ports 8765–8767. May a default all-port scan replace it?

- A. Yes; because the address is loopback
- B. Yes; if the scan is quick
- C. Yes; if findings remain private
- D. No; use only the agreed ports

### M03-C09

A requested scan needs intrusive scripts absent from the ROE. What should happen?

- A. Enable only scripts marked default
- B. Run them once before requesting approval
- C. Stop and obtain a method amendment
- D. Let the tool choose its own scope

### M03-C10

A new case shows an open port but no service metadata. Which report is sound?

- A. Product version confirmed; impact unknown
- B. Remote code execution confirmed
- C. Accountable owner confirmed
- D. Reachability observed; identity unverified

## M04

### M04-C01

What is enumeration in the local portal exercise?

- A. Reading only the supplied asset register
- B. Listing all possible vulnerabilities from memory
- C. Choosing an owner based on the port number
- D. Obtaining service-specific metadata after discovery

### M04-C02

What should determine an enumeration method?

- A. The longest available tool command
- B. Observed service evidence and authorized methods
- C. The highest severity in an unrelated report
- D. The tool's most aggressive preset

### M04-C03

The endpoint reports owner=Unassigned. What does that establish?

- A. The service reports that owner value
- B. No accountable owner exists anywhere
- C. The service is necessarily unauthorized
- D. The system was compromised

### M04-C04

A response reports version 0.8.1. What remains unverified?

- A. That the response contained a version value
- B. That the saved response can be read
- C. Actual product identity and vulnerability relevance
- D. That the requested path was recorded

### M04-C05

Only port 8766 has saved metadata. What belongs in the other map rows?

- A. Copied metadata from port 8766
- B. Observed fields plus explicit metadata gaps
- C. The instructor's expected metadata as observed
- D. Assumed roles from adjacent port numbers

### M04-C06

What is a useful next action for an ownership gap?

- A. Assign ownership to the learner automatically
- B. Treat missing ownership as an exploit proof
- C. Remove the service from the report
- D. Seek accountable verification through the approved path

### M04-C07

How can a service reduce unintended metadata exposure?

- A. Replace all audit logs with banners
- B. Place secrets in less familiar fields
- C. Review which metadata is necessary to publish
- D. Depend only on nonstandard port numbers

### M04-C08

ROE permits /service-info but a response links to /admin. What should happen?

- A. Do not request /admin without an amendment
- B. Open /admin if no password is needed
- C. Try /admin only with a GET request
- D. Follow every link returned by the service

### M04-C09

The approved metadata request reveals a token. What is appropriate?

- A. Use it to verify the claimed owner
- B. Send it to a public decoder service
- C. Include it verbatim in the public map
- D. Stop and preserve it under the handling rule

### M04-C10

A new service reports a familiar product name. Which conclusion transfers?

- A. Self-reported identity needs corroboration
- B. Familiar names make vulnerability findings certain
- C. A name permits testing the vendor's endpoints
- D. Reported identity verifies organizational ownership

## M05

### M05-C01

What distinguishes a scanner finding from a verified weakness?

- A. Corroborating evidence for the relevant condition
- B. The scanner's use of a severity label
- C. The presence of an IP in the report
- D. The number of findings in the report

### M05-C02

What does remediation priority combine?

- A. Only the largest numerical severity
- B. Only the age of the scanner product
- C. Technical evidence with exposure and operational impact
- D. Only the alphabetical host order

### M05-C03

A banner-based finding conflicts with verified patch evidence. What is the best disposition?

- A. Declare exploitation already occurred
- B. Review the conflict before claiming vulnerability
- C. Ignore all patch records by default
- D. Delete both records without a trace

### M05-C04

The synthetic host shows file rewrites and an unapproved persistence entry. What does this support?

- A. Only a theoretical vulnerability
- B. A verified attribution to WannaCry
- C. Proof of successful data recovery
- D. Suspected compromise requiring containment review

### M05-C05

A high-severity finding affects an isolated test host; an active incident affects an important service. What should guide priority?

- A. Severity labels alone without context
- B. Whichever finding was received first
- C. Current incident evidence and service impact
- D. Whichever report contains more pages

### M05-C06

How should an apparent false positive be closed?

- A. Record corroboration and the disposition
- B. Erase the original scanner evidence
- C. Ignore every finding from that scanner
- D. Mark the host secure in every respect

### M05-C07

What demonstrates that an approved patch addressed the finding?

- A. The ticket being assigned an owner
- B. The patch file having a familiar name
- C. The scanner displaying fewer total rows
- D. A bounded verification of the relevant condition

### M05-C08

The scan identifies an external address outside the ROE. What is permitted?

- A. Probe it once to validate the finding
- B. Record the lead without testing the address
- C. Run a low-rate exploitation check
- D. Ask the scanner to follow related hosts

### M05-C09

May synthetic triage authorization be used to run a real exploit?

- A. No; active testing needs separate authorization
- B. Yes; when the CVE is public
- C. Yes; when the scanner marks it critical
- D. Yes; when the output is kept locally

### M05-C10

A new finding lacks software identity and business context. What is the sound decision?

- A. Assign confirmed critical impact immediately
- B. Keep it unverified and request the missing evidence
- C. Assume it is safe because context is missing
- D. Use the highest score from a different system

## M06

### M06-C01

Which distinction separates privilege escalation from initial access?

- A. Escalation always starts before any access
- B. Escalation increases privileges after access
- C. Initial access always gives administrator rights
- D. Both terms mean deleting audit logs

### M06-C02

What does persistence refer to in compromise analysis?

- A. A patch that remains after restart
- B. Any service that has long uptime
- C. A scan result saved in a file
- D. A mechanism for retaining or regaining access

### M06-C03

A new startup entry points to an unapproved script. What should be recorded?

- A. Confirmed attribution to a named attacker
- B. Proof that all user accounts were stolen
- C. A potential persistence mechanism needing validation
- D. Evidence that backups are unusable

### M06-C04

A log shows a user becoming administrator unexpectedly. What is the bounded inference?

- A. Possible privilege escalation to investigate
- B. Confirmed initial infection vector
- C. Proof of successful network segmentation
- D. Proof that every administrator is malicious

### M06-C05

An analyst has only one login event. What remains unproven?

- A. That the saved event contains a timestamp
- B. That the event can be compared with others
- C. That the log is one source of evidence
- D. The full compromise path and persistence

### M06-C06

Which control limits damage from a compromised ordinary account?

- A. Giving all users local administrator rights
- B. Least privilege with monitored privileged access
- C. Disabling security event collection
- D. Sharing one privileged password

### M06-C07

After containment, what supports safe recovery?

- A. Validated cleanup and a checked recovery path
- B. Deleting all logs before restart
- C. Renaming suspicious files without review
- D. Restoring any backup without verification

### M06-C08

The exercise supplies process logs only. Can the learner try captured credentials?

- A. Yes; if the account name is synthetic-looking
- B. Yes; if only one attempt is made
- C. No; credential testing is outside this scope
- D. Yes; because logs imply testing permission

### M06-C09

A proposed cleanup would remove evidence. What should the learner do first?

- A. Delete it to reduce the report size
- B. Preserve evidence and obtain the approved cleanup decision
- C. Run the cleanup before asking the owner
- D. Assume every temporary file is disposable

### M06-C10

A new host has a suspicious process but no verified account history. What should be reported?

- A. A fully reconstructed privilege-escalation chain
- B. Confirmed credential theft from all users
- C. Observed behavior with unresolved access mechanism
- D. Successful eradication after the process exits

## M07

### M07-C01

What feature distinguishes ransomware behavior from ordinary file access?

- A. Reading a configuration file once
- B. Opening a normal application window
- C. Disrupting access to data through coercive locking or encryption
- D. Writing an authorized daily backup

### M07-C02

What does static analysis examine?

- A. An artifact without executing its behavior
- B. Only a live process under real users
- C. Only traffic from a production network
- D. Only the attacker's stated motivation

### M07-C03

Synthetic logs show bulk renames and an extortion-note marker. What is supported?

- A. Verified presence of a specific real malware family
- B. Proof that a real clinic was compromised
- C. Evidence that decryption has succeeded
- D. Ransomware-like behavior in the supplied scenario

### M07-C04

An AI assistant labels a log as WannaCry without a source. How should this be treated?

- A. A verified malware-family attribution
- B. An unverified suggestion requiring evidence
- C. Authorization to download a sample
- D. A substitute for analyst review

### M07-C05

A file hash matches a supplied fixture manifest. What does that establish?

- A. Integrity relative to that fixture baseline
- B. That the file is harmless to execute
- C. That no other file is malicious
- D. That the incident's actor is identified

### M07-C06

Which response best limits potential spread while preserving evidence?

- A. Open the suspected attachment to confirm it
- B. Remove all backups immediately
- C. Use the approved containment path and preserve artifacts
- D. Upload raw credentials with the sample

### M07-C07

What is useful recovery evidence after a ransomware-like incident?

- A. Only the disappearance of the ransom note
- B. A verified restore test and addressed entry conditions
- C. Only a reboot without errors
- D. Only a renamed file extension

### M07-C08

The packet authorizes benign static evidence only. Can a learner fetch live malware?

- A. Yes; if the sample is old
- B. Yes; if a public tutorial links it
- C. Yes; if it is opened only briefly
- D. No; keep to the supplied benign evidence

### M07-C09

The learner wants to paste private incident logs into public AI. What is required?

- A. Only a promise to delete the chat later
- B. Only a popular model provider
- C. Approved handling and properly sanitized inputs
- D. Only removal of the file extension

### M07-C10

A new synthetic case has encryption activity but an approved backup job explains it. What follows?

- A. Encryption always proves ransomware
- B. Ignore all later alerts from the host
- C. Treat the backup owner as an attacker
- D. Correlate context before labeling malware

## M08

### M08-C01

What is packet capture evidence?

- A. A complete record of every application action
- B. Proof of every host's patch level
- C. An inventory of all accountable owners
- D. Observed traffic within a capture's scope and time

### M08-C02

What does transport encryption primarily protect?

- A. Every endpoint from compromise
- B. Traffic contents in transit between relevant endpoints
- C. All metadata from observation
- D. Stored files after decryption

### M08-C03

A summary shows repeated TCP connection attempts to port 445. What alone is supported?

- A. Connection-attempt behavior toward that port
- B. Successful exploitation of SMB
- C. Confirmed ransomware-family identity
- D. Successful theft of application data

### M08-C04

A connection handshake appears in a capture. What remains unproven?

- A. That those packets were captured
- B. That the trace has packet timestamps
- C. Successful application compromise
- D. That the observed endpoints exchanged packets

### M08-C05

A capture contains no suspicious traffic during a short window. What conclusion is appropriate?

- A. The host has never been compromised
- B. No such traffic was observed in that window
- C. All interfaces are free of attacks
- D. The network is permanently secure

### M08-C06

Which control can limit unnecessary east-west service reachability?

- A. Changing service names in an inventory
- B. Removing all network monitoring
- C. Publishing internal addresses more widely
- D. Approved segmentation with verified access rules

### M08-C07

What makes a packet-based finding more credible?

- A. Treating a port number as an application proof
- B. Ignoring collection time and interface
- C. Correlating traffic with scoped host evidence
- D. Using an AI summary without the capture

### M08-C08

Only a supplied sanitized trace is authorized. May the learner capture campus traffic?

- A. No; separate target and capture authorization is needed
- B. Yes; if connected to the campus Wi-Fi
- C. Yes; if the capture is short
- D. Yes; if no packets are modified

### M08-C09

Unexpected credentials appear in an authorized capture. What is the next step?

- A. Try the credentials to determine their scope
- B. Share the trace in a public forum
- C. Keep capturing until more accounts appear
- D. Stop and follow sensitive-evidence handling

### M08-C10

A new trace shows encrypted traffic to an unfamiliar endpoint. What can be reported?

- A. Observed encrypted communication with identity or purpose unresolved
- B. Confirmed exfiltration of a named document
- C. Proof that the endpoint is harmless
- D. Verified account ownership from encryption alone
