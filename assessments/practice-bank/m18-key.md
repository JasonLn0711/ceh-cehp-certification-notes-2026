# M18 — IoT and OT — instructor key v1.0.0

[Question form](m18.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M18-Q001

**Answer: D — MQTT**

MQTT uses a publish/subscribe model through a broker; authentication, topic authorization and transport protection require configuration.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — CoAP:** CoAP is designed for constrained environments and uses a resource-oriented request/response model, commonly over UDP.
- **B — Zigbee:** Zigbee supports low-power wireless networking for constrained devices; joining, keys and implementation security still matter.
- **C — Modbus:** Modbus supports industrial register-oriented communication; security depends on variant and deployment controls rather than assuming every installation authenticates commands.

Coverage: M18; CEH v5 domain 7; IoT protocol roles.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q002

**Answer: C — Unique device credentials**

Use distinct credentials per device rather than a shared default secret across a fleet.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Secure boot:** Secure boot verifies the authorized boot chain and helps prevent execution of untrusted boot components.
- **B — Rollback protection:** Rollback protection prevents installation of disallowed older versions even if those versions were once correctly signed.
- **D — Authenticated firmware update:** Verify update authenticity and integrity before accepting firmware; signature checks need a trusted key and correct implementation.

Coverage: M18; CEH v5 domain 7; Device lifecycle security.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q003

**Answer: C — Safety impact**

OT security decisions must consider possible harm to people, equipment and the physical process, not only data loss.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Passive-first observation:** Where active tests could affect fragile systems, approved passive evidence may be the appropriate initial assessment method.
- **B — Change coordination:** Changes to operational systems require the process owner's approved timing, validation and recovery procedures.
- **D — Process availability:** Industrial operations may require continuity and predictable control behavior; unplanned disruption can have physical consequences.

Coverage: M18; CEH v5 domain 7; OT priorities.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q004

**Answer: B — PLC**

A programmable logic controller executes control logic and interfaces with process inputs and outputs.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — HMI:** A human-machine interface presents process information and controls to an operator.
- **C — Historian:** A historian stores time-series process data for analysis and operational records.
- **D — SCADA:** SCADA supervises and gathers data across industrial operations, often involving distributed control assets.

Coverage: M18; CEH v5 domain 7; Industrial roles.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q005

**Answer: C — Industrial zones and conduits**

Separate assets by trust and function, and restrict the communication paths that cross those boundaries.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Controlled jump host:** A managed intermediary can constrain and log approved administrative access instead of exposing controllers directly.
- **B — Time-bounded vendor access:** Limit vendor remote access to authorized identities, purpose and windows, with reviewable revocation.
- **D — Asset inventory:** Maintain known devices, firmware, function and ownership so exposure and change decisions have an operational basis.

Coverage: M18; CEH v5 domain 7; Segmentation and remote access.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q006

**Answer: B — Topic or resource authorization**

Authenticate a client and separately check which topics or resources it may read or modify.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Replay protection:** Use appropriate freshness, sequence or challenge mechanisms so an old valid message cannot be reused as a new command.
- **C — Message authenticity:** Verify that commands or measurements come from an authorized sender and have not been altered under the chosen trust model.
- **D — Fail-safe behavior:** On failure or uncertainty, a device should move to the defined safe operational condition rather than an arbitrary convenient state.

Coverage: M18; CEH v5 domain 7; IoT data and trust.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q007

**Answer: A — CoAP**

CoAP is designed for constrained environments and uses a resource-oriented request/response model, commonly over UDP.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Zigbee:** Zigbee supports low-power wireless networking for constrained devices; joining, keys and implementation security still matter.
- **C — Modbus:** Modbus supports industrial register-oriented communication; security depends on variant and deployment controls rather than assuming every installation authenticates commands.
- **D — MQTT:** MQTT uses a publish/subscribe model through a broker; authentication, topic authorization and transport protection require configuration.

Coverage: M18; CEH v5 domain 7; IoT protocol roles.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q008

**Answer: D — Authenticated firmware update**

Verify update authenticity and integrity before accepting firmware; signature checks need a trusted key and correct implementation.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Secure boot:** Secure boot verifies the authorized boot chain and helps prevent execution of untrusted boot components.
- **B — Rollback protection:** Rollback protection prevents installation of disallowed older versions even if those versions were once correctly signed.
- **C — Unique device credentials:** Use distinct credentials per device rather than a shared default secret across a fleet.

Coverage: M18; CEH v5 domain 7; Device lifecycle security.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q009

**Answer: B — Process availability**

Industrial operations may require continuity and predictable control behavior; unplanned disruption can have physical consequences.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Passive-first observation:** Where active tests could affect fragile systems, approved passive evidence may be the appropriate initial assessment method.
- **C — Safety impact:** OT security decisions must consider possible harm to people, equipment and the physical process, not only data loss.
- **D — Change coordination:** Changes to operational systems require the process owner's approved timing, validation and recovery procedures.

Coverage: M18; CEH v5 domain 7; OT priorities.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q010

**Answer: A — HMI**

A human-machine interface presents process information and controls to an operator.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — PLC:** A programmable logic controller executes control logic and interfaces with process inputs and outputs.
- **C — SCADA:** SCADA supervises and gathers data across industrial operations, often involving distributed control assets.
- **D — Historian:** A historian stores time-series process data for analysis and operational records.

Coverage: M18; CEH v5 domain 7; Industrial roles.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q011

**Answer: A — Controlled jump host**

A managed intermediary can constrain and log approved administrative access instead of exposing controllers directly.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Industrial zones and conduits:** Separate assets by trust and function, and restrict the communication paths that cross those boundaries.
- **C — Asset inventory:** Maintain known devices, firmware, function and ownership so exposure and change decisions have an operational basis.
- **D — Time-bounded vendor access:** Limit vendor remote access to authorized identities, purpose and windows, with reviewable revocation.

Coverage: M18; CEH v5 domain 7; Segmentation and remote access.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q012

**Answer: B — Message authenticity**

Verify that commands or measurements come from an authorized sender and have not been altered under the chosen trust model.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Replay protection:** Use appropriate freshness, sequence or challenge mechanisms so an old valid message cannot be reused as a new command.
- **C — Topic or resource authorization:** Authenticate a client and separately check which topics or resources it may read or modify.
- **D — Fail-safe behavior:** On failure or uncertainty, a device should move to the defined safe operational condition rather than an arbitrary convenient state.

Coverage: M18; CEH v5 domain 7; IoT data and trust.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q013

**Answer: C — Modbus**

Modbus supports industrial register-oriented communication; security depends on variant and deployment controls rather than assuming every installation authenticates commands.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — CoAP:** CoAP is designed for constrained environments and uses a resource-oriented request/response model, commonly over UDP.
- **B — MQTT:** MQTT uses a publish/subscribe model through a broker; authentication, topic authorization and transport protection require configuration.
- **D — Zigbee:** Zigbee supports low-power wireless networking for constrained devices; joining, keys and implementation security still matter.

Coverage: M18; CEH v5 domain 7; IoT protocol roles.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q014

**Answer: A — Secure boot**

Secure boot verifies the authorized boot chain and helps prevent execution of untrusted boot components.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Rollback protection:** Rollback protection prevents installation of disallowed older versions even if those versions were once correctly signed.
- **C — Authenticated firmware update:** Verify update authenticity and integrity before accepting firmware; signature checks need a trusted key and correct implementation.
- **D — Unique device credentials:** Use distinct credentials per device rather than a shared default secret across a fleet.

Coverage: M18; CEH v5 domain 7; Device lifecycle security.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q015

**Answer: D — Change coordination**

Changes to operational systems require the process owner's approved timing, validation and recovery procedures.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Process availability:** Industrial operations may require continuity and predictable control behavior; unplanned disruption can have physical consequences.
- **B — Passive-first observation:** Where active tests could affect fragile systems, approved passive evidence may be the appropriate initial assessment method.
- **C — Safety impact:** OT security decisions must consider possible harm to people, equipment and the physical process, not only data loss.

Coverage: M18; CEH v5 domain 7; OT priorities.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q016

**Answer: D — SCADA**

SCADA supervises and gathers data across industrial operations, often involving distributed control assets.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — HMI:** A human-machine interface presents process information and controls to an operator.
- **B — Historian:** A historian stores time-series process data for analysis and operational records.
- **C — PLC:** A programmable logic controller executes control logic and interfaces with process inputs and outputs.

Coverage: M18; CEH v5 domain 7; Industrial roles.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q017

**Answer: B — Time-bounded vendor access**

Limit vendor remote access to authorized identities, purpose and windows, with reviewable revocation.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Industrial zones and conduits:** Separate assets by trust and function, and restrict the communication paths that cross those boundaries.
- **C — Controlled jump host:** A managed intermediary can constrain and log approved administrative access instead of exposing controllers directly.
- **D — Asset inventory:** Maintain known devices, firmware, function and ownership so exposure and change decisions have an operational basis.

Coverage: M18; CEH v5 domain 7; Segmentation and remote access.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q018

**Answer: A — Replay protection**

Use appropriate freshness, sequence or challenge mechanisms so an old valid message cannot be reused as a new command.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Topic or resource authorization:** Authenticate a client and separately check which topics or resources it may read or modify.
- **C — Message authenticity:** Verify that commands or measurements come from an authorized sender and have not been altered under the chosen trust model.
- **D — Fail-safe behavior:** On failure or uncertainty, a device should move to the defined safe operational condition rather than an arbitrary convenient state.

Coverage: M18; CEH v5 domain 7; IoT data and trust.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q019

**Answer: B — Zigbee**

Zigbee supports low-power wireless networking for constrained devices; joining, keys and implementation security still matter.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — MQTT:** MQTT uses a publish/subscribe model through a broker; authentication, topic authorization and transport protection require configuration.
- **C — CoAP:** CoAP is designed for constrained environments and uses a resource-oriented request/response model, commonly over UDP.
- **D — Modbus:** Modbus supports industrial register-oriented communication; security depends on variant and deployment controls rather than assuming every installation authenticates commands.

Coverage: M18; CEH v5 domain 7; IoT protocol roles.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q020

**Answer: C — Rollback protection**

Rollback protection prevents installation of disallowed older versions even if those versions were once correctly signed.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Authenticated firmware update:** Verify update authenticity and integrity before accepting firmware; signature checks need a trusted key and correct implementation.
- **B — Unique device credentials:** Use distinct credentials per device rather than a shared default secret across a fleet.
- **D — Secure boot:** Secure boot verifies the authorized boot chain and helps prevent execution of untrusted boot components.

Coverage: M18; CEH v5 domain 7; Device lifecycle security.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q021

**Answer: C — Passive-first observation**

Where active tests could affect fragile systems, approved passive evidence may be the appropriate initial assessment method.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Safety impact:** OT security decisions must consider possible harm to people, equipment and the physical process, not only data loss.
- **B — Process availability:** Industrial operations may require continuity and predictable control behavior; unplanned disruption can have physical consequences.
- **D — Change coordination:** Changes to operational systems require the process owner's approved timing, validation and recovery procedures.

Coverage: M18; CEH v5 domain 7; OT priorities.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q022

**Answer: B — Historian**

A historian stores time-series process data for analysis and operational records.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — HMI:** A human-machine interface presents process information and controls to an operator.
- **C — PLC:** A programmable logic controller executes control logic and interfaces with process inputs and outputs.
- **D — SCADA:** SCADA supervises and gathers data across industrial operations, often involving distributed control assets.

Coverage: M18; CEH v5 domain 7; Industrial roles.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q023

**Answer: D — Asset inventory**

Maintain known devices, firmware, function and ownership so exposure and change decisions have an operational basis.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Industrial zones and conduits:** Separate assets by trust and function, and restrict the communication paths that cross those boundaries.
- **B — Controlled jump host:** A managed intermediary can constrain and log approved administrative access instead of exposing controllers directly.
- **C — Time-bounded vendor access:** Limit vendor remote access to authorized identities, purpose and windows, with reviewable revocation.

Coverage: M18; CEH v5 domain 7; Segmentation and remote access.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q024

**Answer: D — Fail-safe behavior**

On failure or uncertainty, a device should move to the defined safe operational condition rather than an arbitrary convenient state.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Topic or resource authorization:** Authenticate a client and separately check which topics or resources it may read or modify.
- **B — Message authenticity:** Verify that commands or measurements come from an authorized sender and have not been altered under the chosen trust model.
- **C — Replay protection:** Use appropriate freshness, sequence or challenge mechanisms so an old valid message cannot be reused as a new command.

Coverage: M18; CEH v5 domain 7; IoT data and trust.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q025

**Answer: A — MQTT**

MQTT uses a publish/subscribe model through a broker; authentication, topic authorization and transport protection require configuration.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Zigbee:** Zigbee supports low-power wireless networking for constrained devices; joining, keys and implementation security still matter.
- **C — Modbus:** Modbus supports industrial register-oriented communication; security depends on variant and deployment controls rather than assuming every installation authenticates commands.
- **D — CoAP:** CoAP is designed for constrained environments and uses a resource-oriented request/response model, commonly over UDP.

Coverage: M18; CEH v5 domain 7; IoT protocol roles.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q026

**Answer: D — Authenticated firmware update**

Verify update authenticity and integrity before accepting firmware; signature checks need a trusted key and correct implementation.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Secure boot:** Secure boot verifies the authorized boot chain and helps prevent execution of untrusted boot components.
- **B — Rollback protection:** Rollback protection prevents installation of disallowed older versions even if those versions were once correctly signed.
- **C — Unique device credentials:** Use distinct credentials per device rather than a shared default secret across a fleet.

Coverage: M18; CEH v5 domain 7; Device lifecycle security.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q027

**Answer: A — Safety impact**

OT security decisions must consider possible harm to people, equipment and the physical process, not only data loss.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Passive-first observation:** Where active tests could affect fragile systems, approved passive evidence may be the appropriate initial assessment method.
- **C — Process availability:** Industrial operations may require continuity and predictable control behavior; unplanned disruption can have physical consequences.
- **D — Change coordination:** Changes to operational systems require the process owner's approved timing, validation and recovery procedures.

Coverage: M18; CEH v5 domain 7; OT priorities.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q028

**Answer: A — PLC**

A programmable logic controller executes control logic and interfaces with process inputs and outputs.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — HMI:** A human-machine interface presents process information and controls to an operator.
- **C — SCADA:** SCADA supervises and gathers data across industrial operations, often involving distributed control assets.
- **D — Historian:** A historian stores time-series process data for analysis and operational records.

Coverage: M18; CEH v5 domain 7; Industrial roles.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q029

**Answer: B — Industrial zones and conduits**

Separate assets by trust and function, and restrict the communication paths that cross those boundaries.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Asset inventory:** Maintain known devices, firmware, function and ownership so exposure and change decisions have an operational basis.
- **C — Controlled jump host:** A managed intermediary can constrain and log approved administrative access instead of exposing controllers directly.
- **D — Time-bounded vendor access:** Limit vendor remote access to authorized identities, purpose and windows, with reviewable revocation.

Coverage: M18; CEH v5 domain 7; Segmentation and remote access.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)

### CEH26-M18-Q030

**Answer: C — Topic or resource authorization**

Authenticate a client and separately check which topics or resources it may read or modify.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Message authenticity:** Verify that commands or measurements come from an authorized sender and have not been altered under the chosen trust model.
- **B — Fail-safe behavior:** On failure or uncertainty, a device should move to the defined safe operational condition rather than an arbitrary convenient state.
- **D — Replay protection:** Use appropriate freshness, sequence or challenge mechanisms so an old valid message cannot be reused as a new command.

Coverage: M18; CEH v5 domain 7; IoT data and trust.
Technical references: [NIST OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) · [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252) · [NIST IoT baseline](https://csrc.nist.gov/pubs/ir/8259/a/final)
