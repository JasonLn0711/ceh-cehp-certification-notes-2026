# Four connected Northstar availability cases

All are **SIMULATED OUTPUT**. Read the original artifact bytes, then distinguish observation, interpretation, missing evidence, owner and next check. Run tooling/verify_evidence.py for actual local parsing; no traffic generation is used.

| Case | Source | Supported teaching result | Boundary and next check |
| --- | --- | --- | --- |
| E01 | ../lab_mock/E01_wan_windows.csv | Provider offered2400Mbps, campus accepted200Mbps and constrained ingress discarded2200Mbps across aligned60-second IP-octet windows; user success20/100 | Distinct observation points; source identity/intent are unproved. Upstream control needs actual deployment and two-sided user validation. |
| E02 | ../lab_mock/E02_connection_state.csv | Half-open1024/capacity1024,60of6000unique attempts completed,30Mbps link and5/100user checks | Unique counters exclude separately counted retransmissions. SYN cookies/proxy proposals need real stack/service validation. |
| E03 | ../lab_mock/E03_reflector_fixture.pcap | Two constructed valid DNS/IP packets:60/3000IPoctets,74/3014Ethernetoctets;50×onlyatIPlayer | Constructed reflector view, spoofed-source stipulation and9000-byte teachingMTU; not a live capture, victim measurement or attribution proof. |
| E04 | ../lab_mock/E04_request_work.csv | Offered CPU service demand2/24/1.5core-seconds/sec atbaseline/incident/legitimateenrollment versus8corebudget;dependency32/32andqueue400 | Toy demand arithmetic is not measured CPU benchmarking. Generated post-control rows do not prove actual mitigation. |

The same inherited Northstar campus hosts these teaching overlays; its original device identities and map remain unchanged. Resource budgets and synthetic observation roles are separately declared. Preserve normal enrollment as a counterexample to rate-only hostile-intent classification.
