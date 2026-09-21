# M02 — Reconnaissance, sources and evidence

[Reading map](README.md) · [Every source heading](coverage.md) · [Connections](connections.md) · [Unchanged source](../../../source/2026-09-21-ceh-merged-plain-english/CEH_Full_Merged_Plain_English.md)

Captured 2026-09-21, Asia/Taipei. The source-derived text below retains the supplied explanation, examples, correction labels, uncertainty and citations. Heading levels are adjusted for reading; explicit anchors and **Study connection — editorial** paragraphs are additions. References to recordings or earlier checking are the source author's statements, not new observations. This file covers original lines 1199–1457.

## Reading route

- [Part 2 · 11. Footprinting and reconnaissance — Turning scattered information into an understanding that can be tested](#p2-11)
- [Part 2 · 12. Search engines, Shodan, DNSDumpster, and the Wayback Machine — Different views of the environment](#p2-12)
- [Part 2 · 13. Competitive intelligence and OSINT tools — Public information does not guarantee a correct inference](#p2-13)
- [Part 2 · 14. The dark web, Tor, and Bitcoin — Three concepts at different levels](#p2-14)
- [Part 2 · 15. WHOIS, RDAP, and DNS — Names, registration data, and addresses are different things](#p2-15)
- [Part 2 · 16. Traceroute, TTL, and CDNs — Why one number cannot prove an operating system](#p2-16)
- [Part 2 · 17. Email headers — Clues to a delivery route, not a complete network map](#p2-17)
- [Part 2 · 18. Social engineering and information exposure — Focus on how procedures are bypassed](#p2-18)
- [Part 2 · 19. Remote desktop, VMs, terminals, and root — Know which layer you are operating in](#p2-19)

<!-- source-derived-text-begin -->


<a id="en-h112"></a>

## Section B: Module 2 — Footprinting and Reconnaissance


<a id="en-h113"></a>

<a id="p2-11"></a>

## Part 2 · 11. Footprinting and reconnaissance — Turning scattered information into an understanding that can be tested

**Study connection — editorial:** Record the source and date of each clue, and distinguish existing information from new interaction with the target. [Chinese explanation](../handouts-zh/part-02.md#h2-11) · [Audited detail](../m02-reconnaissance.md#collection-boundary) · [Source coverage](coverage.md#en-h113). Source section: lines 1201–1226.

In this class, **footprinting** and **reconnaissance** both involve gathering information about a target and its environment. Their scopes overlap, but they do not need to be declared identical in every context.

The class broadly groups the information into organizational, personnel, network, and system information. Examples include what the company does, where it operates, which domains it uses, and which IP addresses or systems may be associated with it.

A genuinely useful process is:

**Define the purpose and scope → Gather information you are allowed to obtain → Record its source and time → Separate observation from inference → Identify the next question that needs verification.**

Teaching example: A job advertisement requiring CCNA supports the conclusion that the job needs related knowledge. It does not necessarily prove that the company uses one particular brand throughout its internal network. The company may be recruiting for customer projects.

Likewise, an email username of `alex` does not prove that the person's internal AD username is also `alex`. This example also cannot establish a fixed percentage of successful guesses.


<a id="en-h114"></a>

### Passive and active reconnaissance

**Passive reconnaissance** can use existing third-party information to understand a target without initiating new probes against it.

**Active reconnaissance** creates probes or other interactions with the target's infrastructure. A completed TCP connection is not required for it to count as active.

**Fact-check correction: Sending a probe through a proxy or third-party tool does not automatically make it passive.**

Ask whether this operation causes a new interaction with the target, not merely whether packets leave your own computer directly.

---


<a id="en-h115"></a>

<a id="p2-12"></a>

## Part 2 · 12. Search engines, Shodan, DNSDumpster, and the Wayback Machine — Different views of the environment

**Study connection — editorial:** Each search service observes a different surface; its results need freshness, ownership and scope checks. [Chinese explanation](../handouts-zh/part-02.md#h2-12) · [Audited detail](../m02-reconnaissance.md#search-tools) · [Source coverage](coverage.md#en-h115). Source section: lines 1227–1270.


<a id="en-h116"></a>

### Search operators

Search operators narrow a query. For example:

```text
site:example.org filetype:pdf
```

`site:` limits the website scope, and `filetype:` limits the file type. This is a search query, not a terminal command. Search results reflect the search engine's index, not a complete inventory of the website's current state.

Teaching example: A company wants to check whether its public PDFs contain information that should not have been published. It can limit a query to its own domain, then review how it manages public documents.


<a id="en-h117"></a>

### Google Hacking Database, or GHDB

GHDB is a third-party collection of example searches. It is not a Google product. It shows how search conditions can locate particular kinds of information.

For defenders, the point is understanding which accidental exposures may be searchable. Finding a result does not justify unrestricted access to any private information it contains.


<a id="en-h118"></a>

### Shodan

Shodan indexes information about internet-connected services and devices. It observes a different aspect of the internet from an ordinary web-content search engine.

Teaching example: An organization can check whether a device it believed was internal-only has left records of an externally available service.

However, appearing in Shodan does not prove a current vulnerability. The absence of a login page also does not mean the data owner has permitted everyone to use it.


<a id="en-h119"></a>

### DNSDumpster

DNSDumpster organizes domain-related information and relationships. It helps generate initial asset leads. It is not the company's complete DNS database or a map of the routes that packets actually travel.

For example, a record associated with a cloud provider supports the existence of some service relationship. It does not prove that the company's entire network runs through that provider.


<a id="en-h120"></a>

### Wayback Machine

The Wayback Machine provides historical captures of web pages.

**Fact-check correction: A capture timestamp is not necessarily the time the website was changed.** A snapshot taken on a particular day shows what that capture preserved. It does not establish that the website was modified at that exact moment.

Teaching example: Comparing a company's past and present public service offerings can provide historical leads. But a company name changing in a page footer is not enough to establish the legal relationship or business motives behind an acquisition.

---


<a id="en-h121"></a>

<a id="p2-13"></a>

## Part 2 · 13. Competitive intelligence and OSINT tools — Public information does not guarantee a correct inference

**Study connection — editorial:** Public availability does not make an inference correct; tools also depend on their installed version and supported sources. [Chinese explanation](../handouts-zh/part-02.md#h2-13) · [Audited detail](../m02-reconnaissance.md#competitive-intelligence) · [Source coverage](coverage.md#en-h121). Source section: lines 1271–1294.

**Competitive intelligence** means gathering and analyzing information about business competitors. Lawful analysis of public information is not the same as stealing trade secrets.

Teaching example: A company compares competitors' public products, job advertisements, and patent information to identify developments worth watching.

However, a patent application or publication does not guarantee that a related product will launch soon. The lighting in an interview photograph also cannot prove that the interview was paid for, much less reveal its price.


<a id="en-h122"></a>

### theHarvester

theHarvester is an information-gathering tool. The `-d`, `-b`, and `-l` options mentioned in class concern the query target, data sources, and result limits, respectively.

Tool versions and supported sources may change. **Understanding an option's purpose does not establish that an old combination of services in the recording still works.** Check the documentation for the installed version before using it; do not guess options from speech-recognition output.


<a id="en-h123"></a>

### OSINT Framework

**OSINT** stands for **Open-Source Intelligence**. “Open source” here refers to the public availability of the information sources. It does not mean that the software used must have publicly available source code.

OSINT Framework is a resource directory that helps users find services and tools by task. It does not guarantee that every link is free or that every tool is open-source software.

The recording may also mention Maltego, Recon-ng, and FOCA, but those names are interpretations based on context. The original does not provide complete versions or operating instructions, so these mentions should not be expanded into supposedly verified lab procedures.

---


<a id="en-h124"></a>

<a id="p2-14"></a>

## Part 2 · 14. The dark web, Tor, and Bitcoin — Three concepts at different levels

**Study connection — editorial:** Separate access mechanisms, visible source addresses, public transactions and identity attribution. [Chinese explanation](../handouts-zh/part-02.md#h2-14) · [Audited detail](../m02-reconnaissance.md#tor-and-bitcoin) · [Source coverage](coverage.md#en-h124). Source section: lines 1295–1312.

The class discusses dark-web access, Tor, and Bitcoin together, but they are not the same technology.

The **dark web**, in this context, concerns services that require particular networks or software to access. Not all information missing from search engines belongs to the dark web.

**Tor Browser** uses the Tor network. A **Tor relay** is not simply another name for a commercial VPN server. Tor's design uses relays and layered protection to distribute knowledge about a connection. ([Support](https://support.torproject.org/about-tor/how-tor-works/key-management/))

An ordinary website may see a Tor exit relay as the source address. **Onion services** use a different connection arrangement, so the diagram of reaching an ordinary website through an exit relay should not be applied directly to them.

Therefore, visiting an IP-checking website and observing a changed address only shows that the source address observed by that website changed. It does not prove that all activity is impossible to link together.

**Bitcoin** is a separate subject involving payments and a ledger. Its transaction history is public. Decentralization does not mean that transactions cannot be traced, while public transactions do not mean the identity behind every address can be established directly. ([bitcoin.org](https://bitcoin.org/en/protect-your-privacy))

The particular data-sale incidents mentioned in the recording lack enough identifying information to be treated as verified cases. Those descriptions also cannot establish what proportions of all Bitcoin transactions serve different purposes.

---


<a id="en-h125"></a>

<a id="p2-15"></a>

## Part 2 · 15. WHOIS, RDAP, and DNS — Names, registration data, and addresses are different things

**Study connection — editorial:** Registration records, DNS records, reverse mappings and location estimates answer different questions. [Chinese explanation](../handouts-zh/part-02.md#h2-15) · [Audited detail](../m02-reconnaissance.md#dns-and-history) · [Source coverage](coverage.md#en-h125). Source section: lines 1313–1347.


<a id="en-h126"></a>

### WHOIS and RDAP

WHOIS is a traditional service for querying registration data. **RDAP**, the **Registration Data Access Protocol**, provides a more modern, standardized way to query that data.

From **January 28, 2025**, ICANN made RDAP the definitive source for generic top-level domain registration data. This does not mean that WHOIS for every country-code top-level domain stopped on the same day. ([ICANN](https://www.icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en))

Teaching example: You look up a domain's registration status, registrar, or publicly available date information. You are obtaining registration data, not the configuration of all the website's servers. You may also be unable to obtain everyone's private contact details.


<a id="en-h127"></a>

### DNS and resource records

**DNS**, the **Domain Name System**, does more than translate website names into IP addresses. It stores different types of **resource records** for different purposes.

The records relevant to this class include:

**A:** An IPv4 address associated with a name.
**MX:** Information about the servers handling mail for the domain.
**NS:** Information about the name servers responsible for the zone.
**CNAME:** A name alias.
**TXT:** Text information used for particular configuration or verification purposes.
**PTR:** A record commonly used for reverse name lookups. ([RFC Editor](https://www.rfc-editor.org/rfc/rfc1035))


<a id="en-h128"></a>

### Forward and reverse lookups

**Forward lookup:** Start with a name and look up associated information, such as an address.

**Reverse lookup:** Start with an IP address and look up an associated name, usually through separately managed PTR records.

**Fact-check correction: Reverse DNS is not the mathematical inverse of a forward lookup.** A successful forward lookup does not guarantee a reverse lookup will return the same name. A PTR result also does not verify the actual user or device owner.

**IP geolocation** should also be treated as a lead. An estimated address location, the service provider's location, and the actual user's location are not necessarily the same.

---


<a id="en-h129"></a>

<a id="p2-16"></a>

## Part 2 · 16. Traceroute, TTL, and CDNs — Why one number cannot prove an operating system

**Study connection — editorial:** A route or TTL observation belongs to its observation point and path; a CDN edge does not identify the origin system. [Chinese explanation](../handouts-zh/part-02.md#h2-16) · [Audited detail](../m02-reconnaissance.md#paths-and-ttl) · [Source coverage](coverage.md#en-h129). Source section: lines 1348–1383.


<a id="en-h130"></a>

### What does traceroute do?

Traceroute tries to identify some of the intermediate nodes on the path from a source to a target. On Windows, the common command name is `tracert`. Different platforms do not necessarily use identical probe methods.

**TTL**, or **Time To Live**, is a field in an IP packet that limits how long or how far it can be forwarded. In ordinary routing, the TTL decreases at each router. Once it is exhausted, the packet cannot continue traveling indefinitely.

Traceroute uses probes with different TTL values and their responses to observe the path step by step. A hop that does not respond does not mean that no device exists there, nor does it necessarily mean that the connection is broken.

A teaching analogy is sending test letters with different permitted numbers of forwarding steps, then using reports from intermediate stops to learn which places they pass through.


<a id="en-h131"></a>

### Values such as 64 and 128 are only clues

The class mentions 64 as a common initial TTL for Linux and 128 for Windows. These can be introductory memory aids, but TTL is configurable and is not an identity marker exclusive to one operating system.

More importantly:

**The number of hops on the outward path does not necessarily equal the number of hops taken by the reply.**

If you receive a TTL of 58 and add the six outward hops shown by traceroute, the arithmetic gives 64. However, that does not necessarily recover the correct initial TTL, and it certainly does not prove that a website's back end runs Linux.

DNS records also have a TTL, but it concerns cache lifetime. It is not the same field as the IP-packet TTL discussed here. ([RFC Editor](https://www.rfc-editor.org/rfc/rfc1035))


<a id="en-h132"></a>

### A CDN is not simply a high-speed submarine cable

A **CDN**, or **Content Delivery Network**, is a distributed architecture for delivering content. For now, think of multiple service nodes in different places helping respond to users' content requests.

Teaching example: A user may first reach a CDN edge node rather than the origin server that actually produces business data.

The observed response, IP address, or network characteristics may therefore belong to that edge node. **The operating system on the front-facing node does not establish that the back-end business system runs the same operating system.**

Likewise, using a cloud service or CDN does not establish that denial-of-service is impossible.

---


<a id="en-h133"></a>

<a id="p2-17"></a>

## Part 2 · 17. Email headers — Clues to a delivery route, not a complete network map

**Study connection — editorial:** A mail header can support a bounded delivery-path interpretation, while source authentication needs its own evidence. [Chinese explanation](../handouts-zh/part-02.md#h2-17) · [Audited detail](../m02-reconnaissance.md#email-and-human-factors) · [Source coverage](coverage.md#en-h133). Source section: lines 1384–1401.

An **email header** contains information related to the processing of a message. **SMTP**, the **Simple Mail Transfer Protocol**, is an important protocol for delivering email.

SMTP servers add relevant `Received` fields while handling a message, so the original email can provide some clues about its delivery path. ([RFC Editor](https://www.rfc-editor.org/rfc/rfc5321))

A teaching workflow is:

**Preserve the original email → Examine its headers → Identify trustworthy processing nodes → Compare timestamps and other server records → Form a limited conclusion about the delivery path.**

The class illustrates possible processing with an email gateway, spam checks, archiving, and a mail server. These roles may exist, but not every company uses the same sequence.

**Fact-check correction: Not every email allows you to map an entire company's network.** Some internal processing is not visible in the headers, and some earlier fields may be untrustworthy.

Likewise, `Message-ID` identifies a message. It is not a digital signature that, on its own, proves the sender's true identity.

---


<a id="en-h134"></a>

<a id="p2-18"></a>

## Part 2 · 18. Social engineering and information exposure — Focus on how procedures are bypassed

**Study connection — editorial:** Protect the confirmation process and the underlying information, not merely a directory listing or surface appearance. [Chinese explanation](../handouts-zh/part-02.md#h2-18) · [Audited detail](../m02-reconnaissance.md#email-and-human-factors) · [Source coverage](coverage.md#en-h134). Source section: lines 1402–1441.

In this class, **social engineering** means exploiting people's trust, habits, pressure, or interactions to make them disclose information or take an improper action.

The classroom example of a caller impersonating IT illustrates how an identity claim and pressure can make someone skip normal verification. It is not a phone script to try on coworkers.

The abstract process is:

**Contact the person → Build trust or apply pressure → Ask them to depart from the normal procedure → Obtain information or cause an action.**

The matching defensive questions are: Is there an independent, trusted channel to verify someone claiming to be IT? Can a person pause to verify a request before performing a sensitive action?


<a id="en-h135"></a>

### Four classroom terms

**Eavesdropping:** Obtaining information that one should not hear. For example, a bystander overhears sensitive work being discussed in a public place.

**Shoulder surfing:** Watching another person's input or screen. For example, seeing an account name or sensitive document from beside them.

**Dumpster diving:** Obtaining information from discarded documents or media, such as printouts that were not properly disposed of.

**Impersonation:** Claiming another person's identity or role, such as pretending to be a manager or support worker. These methods are not mutually exclusive, and they are not all the same form of deception.

**Fact-check correction: A photograph's appearance, a wrong answer to a geography question, or a single conversational response is not enough to reliably determine whether someone is a bot or a criminal.**


<a id="en-h136"></a>

### Countermeasures should address the actual source of exposure

The class discusses security policies, training, social-media use, and directory listing.

**Directory listing** is a website feature that lists the files or subdirectories in a directory. It can accidentally expose content, but it also has legitimate uses, such as deliberately providing an index of public files.

The key distinction is:

**Not listing a filename is not the same as preventing access to the file.**

Teaching example: A backup file remains in a public website directory, but directory listing is disabled. Someone who knows the full path may still request the file directly. Protect the content itself rather than merely hiding its index.

Likewise, blocking social-media access on the company network does not remove information that was already made public. A platform's ability to obtain information about off-site activity also does not establish that every use of its built-in browser steals every password.

---


<a id="en-h137"></a>

<a id="p2-19"></a>

## Part 2 · 19. Remote desktop, VMs, terminals, and root — Know which layer you are operating in

**Study connection — editorial:** Identify the remote interface, VM, terminal, shell and effective user separately; local privilege does not grant target permission. [Chinese explanation](../handouts-zh/part-02.md#h2-19) · [Audited detail](../course-overview.md#virtualization) · [Source coverage](coverage.md#en-h137). Source section: lines 1442–1457.

This recording explicitly identifies four laboratory VMs:

**Parrot, Windows Server 2019, Windows Server 2022, and Windows 11.**

The class operates through a designated remote-desktop environment. However, the whiteboard and login manual are missing, so a complete IP-address plan or each person's credentials cannot be guessed from the automatic transcript.

**RDP**, the **Remote Desktop Protocol**, supports interaction with a remote-desktop environment. Windows `mstsc` is a related connection program. A remote desktop and a VM are not the same thing: the first is a way to connect and interact, while the second is a virtual computer.

A **terminal** is the interface where you type text commands and see their results. A **shell** is the program that interprets commands and interacts with the operating system. They often appear together, but they are different concepts.

**root** is a highly privileged Linux account. **sudo** runs a command as a specified identity according to system policy, commonly to perform operations that require administrative privileges.

**whoami** only displays the current effective username. It does not raise your privileges. Even a result of root only describes your local execution identity. It does not authorize you to test arbitrary devices on the network.


<!-- source-derived-text-end -->
