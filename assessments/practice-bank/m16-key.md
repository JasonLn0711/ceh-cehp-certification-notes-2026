# M16 — Wireless Networks — instructor key v1.0.0

[Question form](m16.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M16-Q001

**Answer: D — SSID**

An SSID names a wireless network and is not a secret or proof that an access point is legitimate.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — BSSID:** A BSSID identifies a basic service set, commonly using the access point radio's MAC address.
- **B — Signal strength:** Signal strength measures received power at the observer and does not reliably establish trust or exact physical distance.
- **C — Channel:** The channel identifies the radio-frequency portion used by the network; interference and observation depend on channel conditions.

Coverage: M16; CEH v5 domain 6; Wireless identity.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q002

**Answer: C — WPA2-Personal PSK**

WPA2-Personal commonly uses a shared passphrase-derived key; weak passphrases can be exposed to offline guessing from suitable captured authentication material.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — WPA3-Personal SAE:** SAE is a password-authenticated key exchange used by WPA3-Personal and improves resistance to passive offline password guessing when correctly deployed.
- **B — Open network:** An ordinary open network does not provide password-based link authentication or conventional WPA protection; higher-layer protections remain important.
- **D — Enterprise 802.1X/EAP:** Enterprise authentication uses an EAP method and authentication infrastructure, with method selection and certificate validation affecting security.

Coverage: M16; CEH v5 domain 6; Wireless authentication.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q003

**Answer: C — Evil twin**

An evil twin impersonates a trusted wireless network to attract clients, often using a familiar network name.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Radio-frequency jamming:** Jamming interferes with the radio medium and can disrupt availability regardless of application-layer security.
- **B — Rogue access point:** A rogue access point is an unauthorized AP connected to or operating within an organization's environment.
- **D — Deauthentication abuse:** Forged or abusive management messages can disrupt associations where applicable protections are absent or insufficient.

Coverage: M16; CEH v5 domain 6; Wireless threats.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q004

**Answer: B — Protected management frames**

PMF protects selected management frames against certain forgery and replay attacks; it does not prevent radio jamming.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Server certificate validation:** Validating the expected authentication server certificate helps prevent clients from trusting an impostor enterprise authentication endpoint.
- **C — Wireless segmentation:** Separate guest, managed and sensitive traffic with enforced network policy rather than trusting association alone.
- **D — Wireless intrusion monitoring:** Monitoring identifies unexpected APs, identities and radio behavior for investigation, subject to placement and coverage limits.

Coverage: M16; CEH v5 domain 6; Wireless controls.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q005

**Answer: A — Discoverability**

Discoverability affects whether a Bluetooth device announces itself for discovery; it is not a substitute for authentication or updates.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Pairing and association:** Pairing establishes security relationships using a selected method whose resistance to interception or impersonation varies.
- **C — Device patching:** Firmware and software updates address applicable implementation flaws; supported versions and deployment state need verification.
- **D — Unnecessary service exposure:** Unused Bluetooth services or permissions create avoidable opportunities for interaction.

Coverage: M16; CEH v5 domain 6; Bluetooth concepts.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q006

**Answer: D — Authorized capture only**

Capture and testing must stay within approved networks, devices and methods, even when neighboring radio traffic is visible.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Offline artifact analysis:** A supplied sanitized capture can support protocol reasoning without transmitting or interfering with a live wireless network.
- **B — Layered protection:** Link security, endpoint configuration and application encryption address different risks and should not be treated as interchangeable.
- **C — Association is not identity proof:** A matching network name or successful association does not establish that the network operator is the intended trusted party.

Coverage: M16; CEH v5 domain 6; Wireless evidence boundaries.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q007

**Answer: A — BSSID**

A BSSID identifies a basic service set, commonly using the access point radio's MAC address.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Channel:** The channel identifies the radio-frequency portion used by the network; interference and observation depend on channel conditions.
- **C — Signal strength:** Signal strength measures received power at the observer and does not reliably establish trust or exact physical distance.
- **D — SSID:** An SSID names a wireless network and is not a secret or proof that an access point is legitimate.

Coverage: M16; CEH v5 domain 6; Wireless identity.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q008

**Answer: B — WPA3-Personal SAE**

SAE is a password-authenticated key exchange used by WPA3-Personal and improves resistance to passive offline password guessing when correctly deployed.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Open network:** An ordinary open network does not provide password-based link authentication or conventional WPA protection; higher-layer protections remain important.
- **C — WPA2-Personal PSK:** WPA2-Personal commonly uses a shared passphrase-derived key; weak passphrases can be exposed to offline guessing from suitable captured authentication material.
- **D — Enterprise 802.1X/EAP:** Enterprise authentication uses an EAP method and authentication infrastructure, with method selection and certificate validation affecting security.

Coverage: M16; CEH v5 domain 6; Wireless authentication.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q009

**Answer: D — Rogue access point**

A rogue access point is an unauthorized AP connected to or operating within an organization's environment.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Evil twin:** An evil twin impersonates a trusted wireless network to attract clients, often using a familiar network name.
- **B — Deauthentication abuse:** Forged or abusive management messages can disrupt associations where applicable protections are absent or insufficient.
- **C — Radio-frequency jamming:** Jamming interferes with the radio medium and can disrupt availability regardless of application-layer security.

Coverage: M16; CEH v5 domain 6; Wireless threats.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q010

**Answer: A — Server certificate validation**

Validating the expected authentication server certificate helps prevent clients from trusting an impostor enterprise authentication endpoint.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Protected management frames:** PMF protects selected management frames against certain forgery and replay attacks; it does not prevent radio jamming.
- **C — Wireless intrusion monitoring:** Monitoring identifies unexpected APs, identities and radio behavior for investigation, subject to placement and coverage limits.
- **D — Wireless segmentation:** Separate guest, managed and sensitive traffic with enforced network policy rather than trusting association alone.

Coverage: M16; CEH v5 domain 6; Wireless controls.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q011

**Answer: D — Pairing and association**

Pairing establishes security relationships using a selected method whose resistance to interception or impersonation varies.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Discoverability:** Discoverability affects whether a Bluetooth device announces itself for discovery; it is not a substitute for authentication or updates.
- **B — Unnecessary service exposure:** Unused Bluetooth services or permissions create avoidable opportunities for interaction.
- **C — Device patching:** Firmware and software updates address applicable implementation flaws; supported versions and deployment state need verification.

Coverage: M16; CEH v5 domain 6; Bluetooth concepts.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q012

**Answer: C — Association is not identity proof**

A matching network name or successful association does not establish that the network operator is the intended trusted party.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Offline artifact analysis:** A supplied sanitized capture can support protocol reasoning without transmitting or interfering with a live wireless network.
- **B — Authorized capture only:** Capture and testing must stay within approved networks, devices and methods, even when neighboring radio traffic is visible.
- **D — Layered protection:** Link security, endpoint configuration and application encryption address different risks and should not be treated as interchangeable.

Coverage: M16; CEH v5 domain 6; Wireless evidence boundaries.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q013

**Answer: B — Channel**

The channel identifies the radio-frequency portion used by the network; interference and observation depend on channel conditions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — SSID:** An SSID names a wireless network and is not a secret or proof that an access point is legitimate.
- **C — BSSID:** A BSSID identifies a basic service set, commonly using the access point radio's MAC address.
- **D — Signal strength:** Signal strength measures received power at the observer and does not reliably establish trust or exact physical distance.

Coverage: M16; CEH v5 domain 6; Wireless identity.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q014

**Answer: B — Enterprise 802.1X/EAP**

Enterprise authentication uses an EAP method and authentication infrastructure, with method selection and certificate validation affecting security.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — WPA3-Personal SAE:** SAE is a password-authenticated key exchange used by WPA3-Personal and improves resistance to passive offline password guessing when correctly deployed.
- **C — WPA2-Personal PSK:** WPA2-Personal commonly uses a shared passphrase-derived key; weak passphrases can be exposed to offline guessing from suitable captured authentication material.
- **D — Open network:** An ordinary open network does not provide password-based link authentication or conventional WPA protection; higher-layer protections remain important.

Coverage: M16; CEH v5 domain 6; Wireless authentication.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q015

**Answer: A — Deauthentication abuse**

Forged or abusive management messages can disrupt associations where applicable protections are absent or insufficient.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Evil twin:** An evil twin impersonates a trusted wireless network to attract clients, often using a familiar network name.
- **C — Radio-frequency jamming:** Jamming interferes with the radio medium and can disrupt availability regardless of application-layer security.
- **D — Rogue access point:** A rogue access point is an unauthorized AP connected to or operating within an organization's environment.

Coverage: M16; CEH v5 domain 6; Wireless threats.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q016

**Answer: D — Wireless segmentation**

Separate guest, managed and sensitive traffic with enforced network policy rather than trusting association alone.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Wireless intrusion monitoring:** Monitoring identifies unexpected APs, identities and radio behavior for investigation, subject to placement and coverage limits.
- **B — Server certificate validation:** Validating the expected authentication server certificate helps prevent clients from trusting an impostor enterprise authentication endpoint.
- **C — Protected management frames:** PMF protects selected management frames against certain forgery and replay attacks; it does not prevent radio jamming.

Coverage: M16; CEH v5 domain 6; Wireless controls.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q017

**Answer: C — Unnecessary service exposure**

Unused Bluetooth services or permissions create avoidable opportunities for interaction.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Device patching:** Firmware and software updates address applicable implementation flaws; supported versions and deployment state need verification.
- **B — Discoverability:** Discoverability affects whether a Bluetooth device announces itself for discovery; it is not a substitute for authentication or updates.
- **D — Pairing and association:** Pairing establishes security relationships using a selected method whose resistance to interception or impersonation varies.

Coverage: M16; CEH v5 domain 6; Bluetooth concepts.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q018

**Answer: D — Offline artifact analysis**

A supplied sanitized capture can support protocol reasoning without transmitting or interfering with a live wireless network.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Layered protection:** Link security, endpoint configuration and application encryption address different risks and should not be treated as interchangeable.
- **B — Association is not identity proof:** A matching network name or successful association does not establish that the network operator is the intended trusted party.
- **C — Authorized capture only:** Capture and testing must stay within approved networks, devices and methods, even when neighboring radio traffic is visible.

Coverage: M16; CEH v5 domain 6; Wireless evidence boundaries.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q019

**Answer: B — Signal strength**

Signal strength measures received power at the observer and does not reliably establish trust or exact physical distance.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — SSID:** An SSID names a wireless network and is not a secret or proof that an access point is legitimate.
- **C — BSSID:** A BSSID identifies a basic service set, commonly using the access point radio's MAC address.
- **D — Channel:** The channel identifies the radio-frequency portion used by the network; interference and observation depend on channel conditions.

Coverage: M16; CEH v5 domain 6; Wireless identity.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q020

**Answer: A — Open network**

An ordinary open network does not provide password-based link authentication or conventional WPA protection; higher-layer protections remain important.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — WPA2-Personal PSK:** WPA2-Personal commonly uses a shared passphrase-derived key; weak passphrases can be exposed to offline guessing from suitable captured authentication material.
- **C — Enterprise 802.1X/EAP:** Enterprise authentication uses an EAP method and authentication infrastructure, with method selection and certificate validation affecting security.
- **D — WPA3-Personal SAE:** SAE is a password-authenticated key exchange used by WPA3-Personal and improves resistance to passive offline password guessing when correctly deployed.

Coverage: M16; CEH v5 domain 6; Wireless authentication.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q021

**Answer: D — Radio-frequency jamming**

Jamming interferes with the radio medium and can disrupt availability regardless of application-layer security.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Evil twin:** An evil twin impersonates a trusted wireless network to attract clients, often using a familiar network name.
- **B — Deauthentication abuse:** Forged or abusive management messages can disrupt associations where applicable protections are absent or insufficient.
- **C — Rogue access point:** A rogue access point is an unauthorized AP connected to or operating within an organization's environment.

Coverage: M16; CEH v5 domain 6; Wireless threats.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q022

**Answer: B — Wireless intrusion monitoring**

Monitoring identifies unexpected APs, identities and radio behavior for investigation, subject to placement and coverage limits.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Wireless segmentation:** Separate guest, managed and sensitive traffic with enforced network policy rather than trusting association alone.
- **C — Server certificate validation:** Validating the expected authentication server certificate helps prevent clients from trusting an impostor enterprise authentication endpoint.
- **D — Protected management frames:** PMF protects selected management frames against certain forgery and replay attacks; it does not prevent radio jamming.

Coverage: M16; CEH v5 domain 6; Wireless controls.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q023

**Answer: C — Device patching**

Firmware and software updates address applicable implementation flaws; supported versions and deployment state need verification.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Pairing and association:** Pairing establishes security relationships using a selected method whose resistance to interception or impersonation varies.
- **B — Discoverability:** Discoverability affects whether a Bluetooth device announces itself for discovery; it is not a substitute for authentication or updates.
- **D — Unnecessary service exposure:** Unused Bluetooth services or permissions create avoidable opportunities for interaction.

Coverage: M16; CEH v5 domain 6; Bluetooth concepts.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q024

**Answer: B — Layered protection**

Link security, endpoint configuration and application encryption address different risks and should not be treated as interchangeable.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Authorized capture only:** Capture and testing must stay within approved networks, devices and methods, even when neighboring radio traffic is visible.
- **C — Offline artifact analysis:** A supplied sanitized capture can support protocol reasoning without transmitting or interfering with a live wireless network.
- **D — Association is not identity proof:** A matching network name or successful association does not establish that the network operator is the intended trusted party.

Coverage: M16; CEH v5 domain 6; Wireless evidence boundaries.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q025

**Answer: D — SSID**

An SSID names a wireless network and is not a secret or proof that an access point is legitimate.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Signal strength:** Signal strength measures received power at the observer and does not reliably establish trust or exact physical distance.
- **B — Channel:** The channel identifies the radio-frequency portion used by the network; interference and observation depend on channel conditions.
- **C — BSSID:** A BSSID identifies a basic service set, commonly using the access point radio's MAC address.

Coverage: M16; CEH v5 domain 6; Wireless identity.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q026

**Answer: A — Enterprise 802.1X/EAP**

Enterprise authentication uses an EAP method and authentication infrastructure, with method selection and certificate validation affecting security.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — WPA3-Personal SAE:** SAE is a password-authenticated key exchange used by WPA3-Personal and improves resistance to passive offline password guessing when correctly deployed.
- **C — WPA2-Personal PSK:** WPA2-Personal commonly uses a shared passphrase-derived key; weak passphrases can be exposed to offline guessing from suitable captured authentication material.
- **D — Open network:** An ordinary open network does not provide password-based link authentication or conventional WPA protection; higher-layer protections remain important.

Coverage: M16; CEH v5 domain 6; Wireless authentication.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q027

**Answer: C — Evil twin**

An evil twin impersonates a trusted wireless network to attract clients, often using a familiar network name.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Deauthentication abuse:** Forged or abusive management messages can disrupt associations where applicable protections are absent or insufficient.
- **B — Radio-frequency jamming:** Jamming interferes with the radio medium and can disrupt availability regardless of application-layer security.
- **D — Rogue access point:** A rogue access point is an unauthorized AP connected to or operating within an organization's environment.

Coverage: M16; CEH v5 domain 6; Wireless threats.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q028

**Answer: C — Protected management frames**

PMF protects selected management frames against certain forgery and replay attacks; it does not prevent radio jamming.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Server certificate validation:** Validating the expected authentication server certificate helps prevent clients from trusting an impostor enterprise authentication endpoint.
- **B — Wireless intrusion monitoring:** Monitoring identifies unexpected APs, identities and radio behavior for investigation, subject to placement and coverage limits.
- **D — Wireless segmentation:** Separate guest, managed and sensitive traffic with enforced network policy rather than trusting association alone.

Coverage: M16; CEH v5 domain 6; Wireless controls.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q029

**Answer: B — Pairing and association**

Pairing establishes security relationships using a selected method whose resistance to interception or impersonation varies.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Discoverability:** Discoverability affects whether a Bluetooth device announces itself for discovery; it is not a substitute for authentication or updates.
- **C — Device patching:** Firmware and software updates address applicable implementation flaws; supported versions and deployment state need verification.
- **D — Unnecessary service exposure:** Unused Bluetooth services or permissions create avoidable opportunities for interaction.

Coverage: M16; CEH v5 domain 6; Bluetooth concepts.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)

### CEH26-M16-Q030

**Answer: A — Offline artifact analysis**

A supplied sanitized capture can support protocol reasoning without transmitting or interfering with a live wireless network.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Association is not identity proof:** A matching network name or successful association does not establish that the network operator is the intended trusted party.
- **C — Layered protection:** Link security, endpoint configuration and application encryption address different risks and should not be treated as interchangeable.
- **D — Authorized capture only:** Capture and testing must stay within approved networks, devices and methods, even when neighboring radio traffic is visible.

Coverage: M16; CEH v5 domain 6; Wireless evidence boundaries.
Technical references: [NIST WLAN guidance](https://csrc.nist.gov/pubs/sp/800/153/final) · [Wi-Fi Alliance security](https://www.wi-fi.org/discover-wi-fi/security) · [Bluetooth security](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/bluetooth-security/)
