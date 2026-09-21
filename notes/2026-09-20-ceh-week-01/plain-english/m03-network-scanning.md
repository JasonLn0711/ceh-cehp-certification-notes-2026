# M03 — Network behavior, scanning and defensive interpretation

[Reading map](README.md) · [Every source heading](coverage.md) · [Connections](connections.md) · [Unchanged source](../../../source/2026-09-21-ceh-merged-plain-english/CEH_Full_Merged_Plain_English.md)

Captured 2026-09-21, Asia/Taipei. The source-derived text below retains the supplied explanation, examples, correction labels, uncertainty and citations. Heading levels are adjusted for reading; explicit anchors and **Study connection — editorial** paragraphs are additions. References to recordings or earlier checking are the source author's statements, not new observations. This file covers original lines 1458–1850.

## Reading route

- [Part 2 · 20. Hosts, ports, services, and sockets — How does a packet reach the right program?](#p2-20)
- [Part 2 · 21. Packets, headers, payloads, and MTU — Not every way of splitting data is the same](#p2-21)
- [Part 2 · 22. TCP and UDP — Reliability, delay, and application needs](#p2-22)
- [Part 2 · 23. TCP flags and the three-way handshake — More than memorizing three abbreviations](#p2-23)
- [Part 2 · 24. Host discovery — ARP and ICMP ask different questions](#p2-24)
- [Part 2 · 25. Port scanning — What do open, closed, and filtered mean?](#p2-25)
- [Part 2 · 26. Banners, version detection, and OS fingerprinting — Three different types of evidence](#p2-26)
- [Part 2 · 27. How should the classroom commands be read?](#p2-27)
- [Part 2 · 28. Evasion and spoofing concepts from class — Understand the mechanisms, not supposed guarantees of success](#p2-28)
- [Part 2 · 29. Proxies, VPNs, and no-logs claims — A different intermediary does not remove the trust problem](#p2-29)
- [Part 2 · 30. Final defensive measures — What does each one actually protect?](#p2-30)
- [Worked scan interpretation](#worked-example)

<!-- source-derived-text-begin -->


<a id="en-h138"></a>

## Section C: Module 3 — Understand networking before interpreting scan results


<a id="en-h139"></a>

<a id="p2-20"></a>

## Part 2 · 20. Hosts, ports, services, and sockets — How does a packet reach the right program?

**Study connection — editorial:** The operating system uses sockets and protocol state to deliver traffic; a service-name table is only a convention. [Chinese explanation](../handouts-zh/part-02.md#h2-20) · [Audited detail](../m03-network-scanning.md#transport) · [Source coverage](coverage.md#en-h139). Source section: lines 1460–1487.

In the classroom scanning context, **host** is used broadly for a target device. It may be a desktop computer or another network device. Strict internet architecture still distinguishes end hosts from roles such as routers.

A **service** is software that provides a function, such as a website or file transfer.

A **port** is a number that distinguishes endpoints at the transport layer. It is not a physical USB socket. TCP and UDP ports belong to separate protocol spaces.

Teaching example: One server may provide both a website and FTP. A request needs to reach the correct service endpoint.


<a id="en-h140"></a>

### Common port numbers are conventions, not proof of service identity

TCP port 21 is commonly used for FTP control connections. TCP port 80 is commonly used for HTTP.

But an open TCP port 21 only supports a conclusion about the behavior of that TCP endpoint. The number alone does not prove that it is FTP, much less that it has a vulnerability.


<a id="en-h141"></a>

### Fact-check correction: The `services` file is not the packet-dispatch center

Linux `/etc/services` and the corresponding Windows `services` file map common service names to port numbers.

**Actual delivery to a program depends on sockets and the operating system's network processing. It does not require looking up every packet in this name table.**

A **socket** can be understood as an endpoint through which a program communicates over a network. A server program creates a socket, binds the relevant address and port, and enters the appropriate receiving state. The operating system uses protocol and connection information to deliver data to the matching endpoint.

Changing the number associated with `http` in `/etc/services` therefore does not automatically change the listening port of a running web service.

---


<a id="en-h142"></a>

<a id="p2-21"></a>

## Part 2 · 21. Packets, headers, payloads, and MTU — Not every way of splitting data is the same

**Study connection — editorial:** Keep layers explicit when discussing headers, payloads, segmentation, fragmentation and MTU arithmetic. [Chinese explanation](../handouts-zh/part-02.md#h2-21) · [Audited detail](../m03-network-scanning.md#tcp-state) · [Source coverage](coverage.md#en-h142). Source section: lines 1488–1517.

A **packet** is a unit of data transmitted over a network. A **header** contains the information its layer needs to process the data. The **payload** is the content carried by that layer.

Payload is relative to the layer. For example, an IP packet's payload may contain both a TCP header and TCP data. Headers from different layers should not all be treated as one header.

**Fact-check correction: Source and destination IP addresses are in the IP header. TCP source and destination ports are in the TCP header.**


<a id="en-h143"></a>

### Three different processes

**Packetization:** Organizing data into units that can be transmitted.

**TCP segmentation:** Organizing a byte stream into TCP segments.

**IP fragmentation:** Dividing an IP packet into fragments under applicable conditions, with corresponding reassembly needed later.

These processes are related, but they are not synonyms.

**MTU**, or **Maximum Transmission Unit**, describes the maximum unit size that can be sent under particular link conditions. It should not be treated directly as the amount of application data in every packet.

Teaching calculation: Suppose the IP MTU is 1,500 bytes, the IPv4 header is 20 bytes, the TCP header is 20 bytes, and there are no additional options. The space remaining for TCP data is:

**1,500 − 20 − 20 = 1,460 bytes.**

This calculation applies under the stated conditions. It is not a fixed value for every network or packet. The classroom phrase “1.5K per packet” should be read as an illustration.

Packetization is not merely a response to poor historical line quality. Limited-size transmission units also relate to sharing network resources, traveling over different links, and retransmission efficiency.

---


<a id="en-h144"></a>

<a id="p2-22"></a>

## Part 2 · 22. TCP and UDP — Reliability, delay, and application needs

**Study connection — editorial:** Transport acknowledgment and business completion are different events; application requirements determine the useful reliability model. [Chinese explanation](../handouts-zh/part-02.md#h2-22) · [Audited detail](../m03-network-scanning.md#transport) · [Source coverage](coverage.md#en-h144). Source section: lines 1518–1545.

**TCP**, the **Transmission Control Protocol**, provides an ordered byte stream with reliability mechanisms.

**UDP**, the **User Datagram Protocol**, sends datagrams. It does not itself provide TCP's connection-establishment, ordering, and reliable-delivery mechanisms.


<a id="en-h145"></a>

### What does a TCP acknowledgment acknowledge?

TCP uses sequence numbers, acknowledgments, and retransmissions when necessary to handle data delivery. It does not guarantee success regardless of network conditions, and it is not an encryption mechanism. ([RFC Editor](https://www.rfc-editor.org/rfc/rfc9293.html))

Teaching example: You upload a file. TCP helps move the data between the communication endpoints. The application must still confirm that the file was validated and successfully written to storage.

Therefore:

**Receiving a TCP ACK does not establish that a business operation has completed.**

For example, the network stack receiving a request's data does not automatically mean that the database has finished updating.


<a id="en-h146"></a>

### UDP does not make acknowledgment impossible; it simply does not provide it for you

An application using UDP can design its own acknowledgment or retransmission mechanism.

The teaching trade-off is that file transfer usually places high importance on complete, correctly ordered content. Some real-time interactions place more importance on timely arrival. Data that arrives too late may no longer have its original value.

**Fact-check correction: UDP is not guaranteed to be faster in every situation. The choice between TCP and UDP is also not always impossible to change through implemented configuration options.** However, an administrator cannot unilaterally switch a TCP-only application to UDP and expect the other endpoint to understand it automatically.

---


<a id="en-h147"></a>

<a id="p2-23"></a>

## Part 2 · 23. TCP flags and the three-way handshake — More than memorizing three abbreviations

**Study connection — editorial:** Flags describe control state and sequence-space behavior; packet counts in diagrams are examples rather than universal rules. [Chinese explanation](../handouts-zh/part-02.md#h2-23) · [Audited detail](../m03-network-scanning.md#tcp-state) · [Source coverage](coverage.md#en-h147). Source section: lines 1546–1586.

A **flag** is a bit that expresses a control state. The class emphasizes six traditional TCP flags, but these are not the complete set of TCP control bits.

| Flag | Meaning to understand | Do not confuse it with |
| --- | --- | --- |
| **SYN** | Synchronizes sequence numbers; commonly used to establish a connection. | A simple request for permission to perform an operation. |
| **ACK** | Indicates that the acknowledgment-number field is meaningful. | A requirement to send a separate reply for every packet. |
| **FIN** | Indicates that this direction has no more data to send. | Something unrelated to closing a connection. |
| **RST** | Resets, rejects, or aborts the relevant connection state. | The only way to end a connection normally. |
| **PSH** | Relates to pushing data to the receiving application. | Immediately emptying every buffer. |
| **URG** | Indicates that the urgent-pointer field is meaningful. | Giving the entire packet the highest processing priority. |

These are the meanings retained after the source's fact-checking. In particular, URG does not tell the operating system to execute the entire packet's content immediately at top priority.


<a id="en-h148"></a>

### A typical three-way handshake

The ordinary case can be written as:

```text
Client → Server: SYN
Server → Client: SYN + ACK
Client → Server: ACK
```

This is not merely exchanging greetings. It involves synchronizing both sides' sequence numbers and confirming connection state.

The following numbers are a teaching example, not a reconstruction of the classroom whiteboard:

The client sends SYN with an initial sequence number of 100. The server responds with SYN using its own initial sequence number of 500 and acknowledges the client's SYN with ACK 101. The client then acknowledges the server's SYN with ACK 501.

This shows that each side has its own sequence-number space and needs to acknowledge the other's starting information. Later ACK values concern the position of the next expected byte, not simply which numbered packet was seen. ([RFC Editor](https://www.rfc-editor.org/rfc/rfc9293.html))


<a id="en-h149"></a>

### FIN and normal connection closure

The two directions of a TCP connection can close separately. A FIN from A means that A has no more data to send in that direction. It does not necessarily mean that B also has nothing left to send.

Common diagrams show FIN and ACK messages from both sides, but acknowledgments can be combined and packets can be retransmitted. “Closing always takes exactly four packets” is not an exception-free rule.

---


<a id="en-h150"></a>

<a id="p2-24"></a>

## Part 2 · 24. Host discovery — ARP and ICMP ask different questions

**Study connection — editorial:** Interpret the actual probe and response, including local ARP behavior, before inferring host state. [Chinese explanation](../handouts-zh/part-02.md#h2-24) · [Audited detail](../m03-network-scanning.md#discovery) · [Source coverage](coverage.md#en-h150). Source section: lines 1587–1620.


<a id="en-h151"></a>

### ARP: Finding address mappings on a local network

**ARP**, the **Address Resolution Protocol**, handles address resolution on the local IPv4 link in this context.

A **MAC address** is an address used at the link layer. Do not think of it as an unchangeable personal identity card that remains the same across the entire internet.

The simplified classroom process is:

**Ask which device corresponds to this IP address → Receive a relevant reply → Obtain link-layer address information.**

This is a useful way to observe hosts on a local network.

**Fact-check correction: ARP is not a device for measuring whether a computer's power is on.** A reply establishes that a corresponding protocol response was received. It does not directly prove that a particular physical computer has fully booted or that its application is healthy. Proxy replies, virtualization, and other factors may affect interpretation.


<a id="en-h152"></a>

### ICMP Echo: Did this type of probe receive a reply?

**ICMP**, the **Internet Control Message Protocol**, provides network-control and error-reporting messages. The common `ping` utility uses Echo Request and Echo Reply.

A simplified process is:

**Send an Echo Request → The target or relevant network entity processes it → Receive an Echo Reply if permitted.**

No reply may result from filtering, the path, configuration, or the target's state. “The computer is off” is not the only possible explanation.


<a id="en-h153"></a>

### An important detail when experimenting with Nmap

On a local Ethernet network, Nmap may use ARP for host discovery even when another probe method has been selected.

Therefore, **putting an ICMP option in the command does not establish that an ICMP response caused the result**. Understand the tool's actual behavior and environment rather than relying only on the command's name. ([Nmap](https://nmap.org/book/man-host-discovery.html))

---


<a id="en-h154"></a>

<a id="p2-25"></a>

## Part 2 · 25. Port scanning — What do open, closed, and filtered mean?

**Study connection — editorial:** Port states are observations under particular conditions; completing or avoiding a full connection does not decide detectability. [Chinese explanation](../handouts-zh/part-02.md#h2-25) · [Audited detail](../m03-network-scanning.md#discovery) · [Source coverage](coverage.md#en-h154). Source section: lines 1621–1652.

**Port scanning** uses probes and responses to judge the state a particular port presents under the conditions of that observation.

**Open:** Behavior consistent with accepting the relevant communication was observed.

**Closed:** The target can respond, but the port does not present a state that accepts service connections.

**Filtered:** Filtering or related factors prevent the tool from determining whether the port is open or closed. ([Nmap](https://nmap.org/book/man-port-scanning-basics.html))

These are results from a particular place, time, and method of observation. They are not permanent certificates of state.


<a id="en-h155"></a>

### TCP connect scan: `-sT`

A TCP connect scan uses the operating system's connection functions to try to establish an ordinary TCP connection. For an open endpoint, it normally completes the handshake and then ends the test connection. ([Nmap](https://nmap.org/book/man-port-scanning-techniques.html))

It asks, “Can a TCP connection be established this way?”

A successful TCP connection does not establish that every application function is working.


<a id="en-h156"></a>

### TCP SYN scan: `-sS`

A SYN scan judges state from earlier TCP responses without completing the ordinary full connection-establishment process. This is why it is often called a **half-open scan**. ([Nmap](https://nmap.org/book/man-port-scanning-techniques.html))

Typically, a SYN+ACK response to SYN is a clue that the endpoint is open. RST is often a clue that it is closed. No response or certain error reports need further interpretation according to the tool's rules.

**Fact-check correction: Half-open does not mean unlogged, and it certainly does not mean undetectable.** Even if the application has no complete connection record, network devices, packet monitoring, or an IDS may still observe the probes. Nmap's documentation explicitly notes that an appropriate IDS can detect both scan types. ([Nmap](https://nmap.org/book/man-port-scanning-techniques.html))

Also, Nmap does not necessarily start at port 1 and scan every port in numerical order. The actual range depends on its defaults and options.

---


<a id="en-h157"></a>

<a id="p2-26"></a>

## Part 2 · 26. Banners, version detection, and OS fingerprinting — Three different types of evidence

**Study connection — editorial:** A banner, a service match and an OS fingerprint provide different evidence and leave different uncertainties. [Chinese explanation](../handouts-zh/part-02.md#h2-26) · [Audited detail](../m03-network-scanning.md#identification) · [Source coverage](coverage.md#en-h157). Source section: lines 1653–1692.


<a id="en-h158"></a>

### Banner: Identification information supplied by the service

A **banner** may be a welcome message or identification information returned when interaction with a service begins.

For example, an FTP service may include its product name in a response. This is a useful clue, but the content may be omitted, changed, or disguised.

**Fact-check correction: Not every service or operating system returns a banner from which the version can be read directly.**


<a id="en-h159"></a>

### Service and version detection: `-sV`

Nmap's `-sV` identifies services and versions using probes, response patterns, and related information. It does not merely print a table of conventional service names for port numbers. ([Nmap](https://nmap.org/book/man-version-detection.html))

Teaching example: First, TCP port 21 is observed to be open. Further probing produces a response consistent with a particular FTP product. That provides more evidence than saying port 21 is usually FTP, but it still does not establish exploitability.

Remember this distinction:

**`-v` increases output verbosity. `-sV` performs service and version detection. Capitalization and option combinations matter.**


<a id="en-h160"></a>

### OS fingerprinting: `-O`

**Operating-system fingerprinting** may compare the response characteristics of a TCP/IP stack with known patterns.

It does not require the target to announce “I am Windows,” and it is not simply banner reading. ([Nmap](https://nmap.org/book/man-os-detection.html))

Teaching example: If a tool reports that the target may belong to a particular Windows family, retain that uncertainty and the matching conditions. Do not rewrite it as a confirmed exact version and patch state.


<a id="en-h161"></a>

### NSE and `smb-os-discovery`

**NSE**, the **Nmap Scripting Engine**, allows scripts to perform different kinds of tasks.

The `smb-os-discovery` script mentioned in class tries to obtain system information through information exposed by SMB. The target must provide the relevant service and permit the information to be obtained. Not every run will return every field.

`.nse` is the extension for these script files. `/usr/share/nmap/scripts` is a common Linux package path, not a universal path for every platform.

**A script name that sounds like a simple query does not mean every script is harmless.** Check what it does and whether it is within the authorized scope before running it.

---


<a id="en-h162"></a>

<a id="p2-27"></a>

## Part 2 · 27. How should the classroom commands be read?

**Study connection — editorial:** Read each command as a question about a specific layer, with a placeholder target and an explicit interpretation limit. [Chinese explanation](../handouts-zh/part-02.md#h2-27) · [Audited detail](../m03-network-scanning.md#command-reference) · [Source coverage](coverage.md#en-h162). Source section: lines 1693–1714.

The following are documented examples supplied by the checked source, not word-for-word reconstructions of missing commands. `<LAB_IP>` is a placeholder. It should not be pasted unchanged into a terminal and does not designate an already authorized target.

| Example | Main purpose |
| --- | --- |
| `nmap -sn -PR <LAB_IP>` | Perform ARP host discovery in a suitable local IPv4 environment, without an ordinary port scan. |
| `nmap -sn -PE <LAB_IP>` | Request ICMP Echo host discovery; still account for actual behavior such as local ARP use. |
| `nmap -sT <LAB_IP>` | Perform a TCP connect scan. |
| `nmap -sS <LAB_IP>` | Perform a TCP SYN scan. |
| `nmap -p 21 -sV <LAB_IP>` | Select port 21 and perform service/version detection. |
| `nmap -O <LAB_IP>` | Perform operating-system fingerprinting. |
| `nmap --script smb-os-discovery <LAB_IP>` | Select the specified script for obtaining SMB information. |

These purposes and limitations are listed in the checked source's command reference.

The point is not to memorize seven commands. It is to be able to answer, every time:

**Am I observing a host, a port, a service, or an operating system? What kind of conclusion can this result support?**

---


<a id="en-h163"></a>

<a id="p2-28"></a>

## Part 2 · 28. Evasion and spoofing concepts from class — Understand the mechanisms, not supposed guarantees of success

**Study connection — editorial:** Understand the field or processing discrepancy being discussed; a mechanism is not a guarantee of bypass or invisibility. [Chinese explanation](../handouts-zh/part-02.md#h2-28) · [Audited detail](../m03-network-scanning.md#evasion-and-defense) · [Source coverage](coverage.md#en-h163). Source section: lines 1715–1768.


<a id="en-h164"></a>

### Fragmentation: Differences in reassembly and inspection

IP fragmentation can have legitimate uses, but it also creates reassembly and processing costs. If an intermediate device and the receiving host handle fragments differently, they may interpret the security significance differently. ([RFC Editor](https://www.rfc-editor.org/rfc/rfc8900.html))

A teaching explanation is that a defensive device may inspect separate pieces while the receiver interprets their reassembled content. The two may therefore see different meanings.

**Fact-check correction: “Every fragment is an attack, so drop them all without exception” is not a universal rule.** Whether and how to restrict fragments depends on the protocol, network requirements, and device capabilities.


<a id="en-h165"></a>

### Source routing: Routing information supplied by the source

**Source routing** involves a packet's source providing some routing information rather than leaving the path entirely to ordinary forwarding decisions.

It may conflict with security policy, but not all routing functions are the same. Identify the specific mechanism and whether it is needed.


<a id="en-h166"></a>

### Source-port manipulation is not the same as destination-port abuse

The **source port** belongs to the sending endpoint; the **destination port** belongs to the receiving endpoint.

Using a particular source-port number to fool an insufficiently strict rule into trusting traffic is different from placing an external data-receiving service on destination port 80.

**Fact-check correction: The classroom heading may refer to source-port manipulation, but the example of sending data out to port 80 mainly concerns the destination port and outbound-connection policy.**

This also shows why allowing only ports 80 or 443 does not establish that all permitted content is legitimate business traffic.


<a id="en-h167"></a>

### Decoys: Making source identification more confusing

Here, a **decoy** is an apparent additional source. Packets appearing to come from several sources do not mean the tester owns those IP addresses, and they do not guarantee that defensive equipment will be misled.

Several claimed source addresses should not be interpreted as several verified real identities.


<a id="en-h168"></a>

### IP spoofing: Falsifying the source claimed by a packet

**IP spoofing** makes a packet's source information differ from its actual sending source.

Teaching example: A sends a message to B but writes C as the reply address. If B replies to that address, the response may go to C rather than A. This helps explain **reflection**.

However, changing a source IP address does not automatically allow the sender to receive all traffic in a two-way connection. Reply paths and protocol state still matter.


<a id="en-h169"></a>

### MAC spoofing: Changing a link-layer address

Some devices and system configurations allow the MAC address in use to be changed, but this is not identical across all equipment. It is also not an identity-hiding function that spans the whole internet.


<a id="en-h170"></a>

### Packet builders and checksums

A **packet builder** creates packets with specified fields or content. The class mentions **Colasoft Packet Builder** to show that packet content is not only something to observe passively; software can construct it.

A **checksum** checks for certain data errors over a defined portion of data. The covered data and rules differ across protocols.

**Fact-check correction: A checksum is not a digital signature and does not prove a trusted source.** Someone who can change the content may also be able to calculate a matching checksum. Likewise, the broad claim that an intentionally wrong checksum lets traffic pass through a firewall cannot be accepted without examining the device and protocol.

---


<a id="en-h171"></a>

<a id="p2-29"></a>

## Part 2 · 29. Proxies, VPNs, and no-logs claims — A different intermediary does not remove the trust problem

**Study connection — editorial:** Changing the intermediary changes the trust arrangement; a no-logs claim needs a defined scope and evidence. [Chinese explanation](../handouts-zh/part-02.md#h2-29) · [Audited detail](../m03-network-scanning.md#evasion-and-defense) · [Source coverage](coverage.md#en-h171). Source section: lines 1769–1784.

A **proxy** communicates with another party on someone's behalf. Which communication it supports depends on the proxy type and configuration.

A **VPN**, or **Virtual Private Network**, is a different mechanism for establishing network connections and protecting communication. It should not be treated merely as a larger web proxy.

These arrangements may change the source address seen by the target, but the activity still interacts with it. **Accessing a target through a proxy does not make the activity passive reconnaissance.**

Teaching example: An employee accesses an outside website through a company-controlled proxy. The website may see the proxy's connection, while the company can still control allowed destinations through its policies.

**No-logs** is a claim about record retention. You still need to ask: Which records? Over what period? On which systems? How can the claim be verified?

**Fact-check correction: Multiple VPN layers, foreign IP addresses, or no-logs claims do not guarantee that activity cannot be linked. Nor do they establish that every investigation must fail.**

---


<a id="en-h172"></a>

<a id="p2-30"></a>

## Part 2 · 30. Final defensive measures — What does each one actually protect?

**Study connection — editorial:** State exactly what a defensive control changes and which risks remain after it is applied. [Chinese explanation](../handouts-zh/part-02.md#h2-30) · [Audited detail](../m03-network-scanning.md#countermeasures) · [Source coverage](coverage.md#en-h172). Source section: lines 1785–1826.


<a id="en-h173"></a>

### ICMP: Restricting Echo is not the same as blocking all ICMP

ICMP is used for more than ping. It also supports network-control and error-reporting functions.

Restricting Echo Requests from particular sources is therefore different from dropping every ICMP message. The latter may affect normal network functions.


<a id="en-h174"></a>

### IDS and IPS: Detection is not the same as blocking

An **IDS**, or **Intrusion Detection System**, primarily provides detection and alerts.

An **IPS**, or **Intrusion Prevention System**, can block activity when deployed with appropriate rules and placement.

An IDS alert does not establish that traffic was blocked. No alert does not establish that nothing went wrong. Keep this distinction whenever the class treats detection equipment as automatically providing prevention.


<a id="en-h175"></a>

### Do not confuse these two Apache settings

`ServerSignature Off` controls the related signature information in server-generated pages.

`ServerTokens` controls the information exposed in the HTTP `Server` header. For example, a less detailed setting may still show the product name rather than removing the header entirely. ([Apache HTTP Server](https://httpd.apache.org/docs/2.4/mod/core.html))

**Fact-check correction: `ServerSignature Off` does not mean the HTTP `Server` header has been removed.**

Reducing version disclosure also does not fix a vulnerability. The real software version, permission issues, and configuration problems remain.


<a id="en-h176"></a>

### TTL and IP ID: An unusual value is a clue, not proof of spoofing

Different TTL values may result from different paths or settings. The IPv4 ID is also not necessarily a system-wide counter that increases by one for every packet.

Therefore, large differences in TTL or IP ID do not, by themselves, prove a spoofed source.

One relevant defense against source-address spoofing is **source-address validation**: checking whether a source address should appear from that network location. ([RFC Editor](https://www.rfc-editor.org/rfc/rfc2827.html))


<a id="en-h177"></a>

### Encryption: State the boundary it protects

Encryption can protect the confidentiality of the relevant content. Combined with suitable authentication and integrity mechanisms, it can also support other security goals.

However, encryption is not a universal filter for forged packets. It does not automatically repair infected endpoints or prevent limited bandwidth from being exhausted.

**The claim that encryption solves 80% of network problems is not supported by evidence in this material.** The right question is: “Which part of the communication, which data, and which security properties does this encryption protect?”


<a id="en-h178"></a>

<a id="worked-example"></a>

## Bringing the class together: An interpretation you should be able to make

Suppose you observe a designated VM in **an authorized laboratory** and obtain the following teaching scenario:

ARP receives a reply. ICMP Echo does not. TCP port 21 is reported as open. Service detection returns a result consistent with a particular FTP product.

The correct conclusion is not: “This computer is confirmed to be fully booted and healthy, runs an exact version, and can be hacked.”

A more accurate interpretation is:

**The ARP reply** provides an observation about local address resolution.
**The missing ICMP reply** means that this probe did not receive the expected response; the cause still needs assessment.
**TCP port 21 being open** provides evidence that the endpoint was reachable under those conditions at that time.
**The service-detection result** adds a clue about the product or protocol, but is not proof of successful exploitation. This is why the checked source requires recording the probe type, source location, time, version, and limitations.

The next step should follow the original testing objective. Are you checking the asset inventory, identifying an unnecessary service, or assessing whether a specific vulnerability applies? Do not keep expanding the test simply because the tool has more options.

The most useful thinking sequence to take from this class is:

**Gather information to generate leads. Design probes to obtain observations. Check conditions to form judgments. Keep evidence to support conclusions. Fix and retest to confirm improvement.**

Your first exercise can be a one-page **scan-interpretation record**. State the testing purpose, authorized scope, probe method, actual observations, supported conclusions, and what remains uncertain.

**The standard for completion is not how many commands you can recite. It is whether you can explain to another student what question the tool asked, what the system actually answered, and why your conclusion does not go beyond the evidence.**

<!-- source-derived-text-end -->
