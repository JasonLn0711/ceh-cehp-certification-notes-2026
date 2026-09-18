# M20 — Cryptography — instructor key v1.0.0

[Question form](m20.md) · [Administration and version rules](README.md)

Use only after an answer or drill batch is committed. Explanations are in plain English. Options describe different mechanisms or decisions; use the facts in the stem to select the best fit. Original scores remain unchanged after this teaching. For an error, add at least three distinct retests within the endpoint.

### CEH26-M20-Q001

**Answer: B — Cryptographic hash**

A cryptographic hash produces a fixed-size digest without a secret key; an untrusted digest alone does not prove origin.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — HMAC:** HMAC uses a shared secret key and a hash-based construction to authenticate messages; any party holding the key can generate a valid tag.
- **C — Symmetric encryption:** Symmetric encryption uses shared secret key material to protect confidentiality, with suitable modes and key handling.
- **D — Digital signature:** A digital signature uses a private signing key and public verification key to authenticate signed content under a trust model.

Coverage: M20; CEH v5 domain 9; Cryptographic primitives.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q002

**Answer: B — Preimage resistance**

Preimage resistance makes finding an input for a specified hash output computationally impractical under the intended security level.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Forward secrecy:** Forward secrecy protects past session keys against later compromise of a long-term key when the protocol and key exchange provide it.
- **C — Collision resistance:** Collision resistance makes finding any two distinct inputs with the same digest impractical under the intended security level.
- **D — Second-preimage resistance:** Second-preimage resistance makes finding a different input with the same digest as a given input impractical.

Coverage: M20; CEH v5 domain 9; Security properties.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q003

**Answer: D — ECB pattern leakage**

ECB independently encrypts equal plaintext blocks under the same key into equal ciphertext blocks, exposing repeated structure.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Authenticated encryption:** Authenticated encryption, such as correctly used GCM, protects confidentiality and detects tampering while still requiring proper nonce and key handling.
- **B — CTR nonce uniqueness:** CTR-style encryption requires avoiding reuse of the relevant nonce/counter stream under the same key, or plaintext relationships can leak.
- **C — CBC IV requirement:** CBC encryption needs a suitable unpredictable initialization vector and separate integrity protection when used without an authenticated construction.

Coverage: M20; CEH v5 domain 9; Encryption modes.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q004

**Answer: C — Certificate-chain validation**

Validate a certificate through an accepted trust chain under the verifier's policy.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Private-key protection:** Protect the private key from disclosure or misuse; a public certificate does not need to be kept secret.
- **B — Validity and revocation handling:** Consider validity periods and applicable revocation mechanisms according to the client and deployment policy.
- **D — Hostname validation:** Check that the certificate identity matches the intended service name rather than merely trusting its issuer.

Coverage: M20; CEH v5 domain 9; PKI and certificates.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q005

**Answer: A — Cryptographically secure randomness**

Security-sensitive keys and nonces need an appropriate unpredictable generator and correct construction-specific handling.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Key separation:** Use keys for their intended purpose and trust boundary rather than reusing one key across unrelated functions.
- **C — Secure destruction and retention:** Retain keys only as needed and destroy them appropriately when their authorized lifetime ends, considering recovery obligations.
- **D — Rotation and revocation:** Replace or invalidate keys when required while managing dependent systems and retained data.

Coverage: M20; CEH v5 domain 9; Key lifecycle.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q006

**Answer: D — Encoding is not encryption**

Encoding changes representation for interoperability and generally provides no secret-based confidentiality.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Hashing is not password encryption:** Password verification normally uses a suitable one-way password KDF and salt rather than reversible encryption or a fast unsalted hash.
- **B — Signing is not confidentiality:** A signature can authenticate content while leaving that content readable to anyone who receives it.
- **C — Steganography hides presence:** Steganography hides information within another carrier; secrecy of content may still require encryption.

Coverage: M20; CEH v5 domain 9; Common confusions.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q007

**Answer: D — Symmetric encryption**

Symmetric encryption uses shared secret key material to protect confidentiality, with suitable modes and key handling.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Digital signature:** A digital signature uses a private signing key and public verification key to authenticate signed content under a trust model.
- **B — HMAC:** HMAC uses a shared secret key and a hash-based construction to authenticate messages; any party holding the key can generate a valid tag.
- **C — Cryptographic hash:** A cryptographic hash produces a fixed-size digest without a secret key; an untrusted digest alone does not prove origin.

Coverage: M20; CEH v5 domain 9; Cryptographic primitives.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q008

**Answer: C — Second-preimage resistance**

Second-preimage resistance makes finding a different input with the same digest as a given input impractical.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Preimage resistance:** Preimage resistance makes finding an input for a specified hash output computationally impractical under the intended security level.
- **B — Collision resistance:** Collision resistance makes finding any two distinct inputs with the same digest impractical under the intended security level.
- **D — Forward secrecy:** Forward secrecy protects past session keys against later compromise of a long-term key when the protocol and key exchange provide it.

Coverage: M20; CEH v5 domain 9; Security properties.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q009

**Answer: A — CBC IV requirement**

CBC encryption needs a suitable unpredictable initialization vector and separate integrity protection when used without an authenticated construction.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — CTR nonce uniqueness:** CTR-style encryption requires avoiding reuse of the relevant nonce/counter stream under the same key, or plaintext relationships can leak.
- **C — Authenticated encryption:** Authenticated encryption, such as correctly used GCM, protects confidentiality and detects tampering while still requiring proper nonce and key handling.
- **D — ECB pattern leakage:** ECB independently encrypts equal plaintext blocks under the same key into equal ciphertext blocks, exposing repeated structure.

Coverage: M20; CEH v5 domain 9; Encryption modes.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q010

**Answer: C — Hostname validation**

Check that the certificate identity matches the intended service name rather than merely trusting its issuer.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Certificate-chain validation:** Validate a certificate through an accepted trust chain under the verifier's policy.
- **B — Validity and revocation handling:** Consider validity periods and applicable revocation mechanisms according to the client and deployment policy.
- **D — Private-key protection:** Protect the private key from disclosure or misuse; a public certificate does not need to be kept secret.

Coverage: M20; CEH v5 domain 9; PKI and certificates.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q011

**Answer: A — Key separation**

Use keys for their intended purpose and trust boundary rather than reusing one key across unrelated functions.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Cryptographically secure randomness:** Security-sensitive keys and nonces need an appropriate unpredictable generator and correct construction-specific handling.
- **C — Rotation and revocation:** Replace or invalidate keys when required while managing dependent systems and retained data.
- **D — Secure destruction and retention:** Retain keys only as needed and destroy them appropriately when their authorized lifetime ends, considering recovery obligations.

Coverage: M20; CEH v5 domain 9; Key lifecycle.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q012

**Answer: D — Steganography hides presence**

Steganography hides information within another carrier; secrecy of content may still require encryption.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Encoding is not encryption:** Encoding changes representation for interoperability and generally provides no secret-based confidentiality.
- **B — Signing is not confidentiality:** A signature can authenticate content while leaving that content readable to anyone who receives it.
- **C — Hashing is not password encryption:** Password verification normally uses a suitable one-way password KDF and salt rather than reversible encryption or a fast unsalted hash.

Coverage: M20; CEH v5 domain 9; Common confusions.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q013

**Answer: C — Digital signature**

A digital signature uses a private signing key and public verification key to authenticate signed content under a trust model.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — HMAC:** HMAC uses a shared secret key and a hash-based construction to authenticate messages; any party holding the key can generate a valid tag.
- **B — Symmetric encryption:** Symmetric encryption uses shared secret key material to protect confidentiality, with suitable modes and key handling.
- **D — Cryptographic hash:** A cryptographic hash produces a fixed-size digest without a secret key; an untrusted digest alone does not prove origin.

Coverage: M20; CEH v5 domain 9; Cryptographic primitives.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q014

**Answer: A — Collision resistance**

Collision resistance makes finding any two distinct inputs with the same digest impractical under the intended security level.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Second-preimage resistance:** Second-preimage resistance makes finding a different input with the same digest as a given input impractical.
- **C — Forward secrecy:** Forward secrecy protects past session keys against later compromise of a long-term key when the protocol and key exchange provide it.
- **D — Preimage resistance:** Preimage resistance makes finding an input for a specified hash output computationally impractical under the intended security level.

Coverage: M20; CEH v5 domain 9; Security properties.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q015

**Answer: D — CTR nonce uniqueness**

CTR-style encryption requires avoiding reuse of the relevant nonce/counter stream under the same key, or plaintext relationships can leak.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Authenticated encryption:** Authenticated encryption, such as correctly used GCM, protects confidentiality and detects tampering while still requiring proper nonce and key handling.
- **B — CBC IV requirement:** CBC encryption needs a suitable unpredictable initialization vector and separate integrity protection when used without an authenticated construction.
- **C — ECB pattern leakage:** ECB independently encrypts equal plaintext blocks under the same key into equal ciphertext blocks, exposing repeated structure.

Coverage: M20; CEH v5 domain 9; Encryption modes.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q016

**Answer: D — Validity and revocation handling**

Consider validity periods and applicable revocation mechanisms according to the client and deployment policy.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Hostname validation:** Check that the certificate identity matches the intended service name rather than merely trusting its issuer.
- **B — Certificate-chain validation:** Validate a certificate through an accepted trust chain under the verifier's policy.
- **C — Private-key protection:** Protect the private key from disclosure or misuse; a public certificate does not need to be kept secret.

Coverage: M20; CEH v5 domain 9; PKI and certificates.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q017

**Answer: B — Rotation and revocation**

Replace or invalidate keys when required while managing dependent systems and retained data.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Secure destruction and retention:** Retain keys only as needed and destroy them appropriately when their authorized lifetime ends, considering recovery obligations.
- **C — Key separation:** Use keys for their intended purpose and trust boundary rather than reusing one key across unrelated functions.
- **D — Cryptographically secure randomness:** Security-sensitive keys and nonces need an appropriate unpredictable generator and correct construction-specific handling.

Coverage: M20; CEH v5 domain 9; Key lifecycle.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q018

**Answer: C — Hashing is not password encryption**

Password verification normally uses a suitable one-way password KDF and salt rather than reversible encryption or a fast unsalted hash.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Encoding is not encryption:** Encoding changes representation for interoperability and generally provides no secret-based confidentiality.
- **B — Signing is not confidentiality:** A signature can authenticate content while leaving that content readable to anyone who receives it.
- **D — Steganography hides presence:** Steganography hides information within another carrier; secrecy of content may still require encryption.

Coverage: M20; CEH v5 domain 9; Common confusions.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q019

**Answer: A — HMAC**

HMAC uses a shared secret key and a hash-based construction to authenticate messages; any party holding the key can generate a valid tag.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Digital signature:** A digital signature uses a private signing key and public verification key to authenticate signed content under a trust model.
- **C — Cryptographic hash:** A cryptographic hash produces a fixed-size digest without a secret key; an untrusted digest alone does not prove origin.
- **D — Symmetric encryption:** Symmetric encryption uses shared secret key material to protect confidentiality, with suitable modes and key handling.

Coverage: M20; CEH v5 domain 9; Cryptographic primitives.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q020

**Answer: B — Forward secrecy**

Forward secrecy protects past session keys against later compromise of a long-term key when the protocol and key exchange provide it.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Collision resistance:** Collision resistance makes finding any two distinct inputs with the same digest impractical under the intended security level.
- **C — Preimage resistance:** Preimage resistance makes finding an input for a specified hash output computationally impractical under the intended security level.
- **D — Second-preimage resistance:** Second-preimage resistance makes finding a different input with the same digest as a given input impractical.

Coverage: M20; CEH v5 domain 9; Security properties.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q021

**Answer: A — Authenticated encryption**

Authenticated encryption, such as correctly used GCM, protects confidentiality and detects tampering while still requiring proper nonce and key handling.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — ECB pattern leakage:** ECB independently encrypts equal plaintext blocks under the same key into equal ciphertext blocks, exposing repeated structure.
- **C — CTR nonce uniqueness:** CTR-style encryption requires avoiding reuse of the relevant nonce/counter stream under the same key, or plaintext relationships can leak.
- **D — CBC IV requirement:** CBC encryption needs a suitable unpredictable initialization vector and separate integrity protection when used without an authenticated construction.

Coverage: M20; CEH v5 domain 9; Encryption modes.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q022

**Answer: A — Private-key protection**

Protect the private key from disclosure or misuse; a public certificate does not need to be kept secret.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Certificate-chain validation:** Validate a certificate through an accepted trust chain under the verifier's policy.
- **C — Validity and revocation handling:** Consider validity periods and applicable revocation mechanisms according to the client and deployment policy.
- **D — Hostname validation:** Check that the certificate identity matches the intended service name rather than merely trusting its issuer.

Coverage: M20; CEH v5 domain 9; PKI and certificates.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q023

**Answer: B — Secure destruction and retention**

Retain keys only as needed and destroy them appropriately when their authorized lifetime ends, considering recovery obligations.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Cryptographically secure randomness:** Security-sensitive keys and nonces need an appropriate unpredictable generator and correct construction-specific handling.
- **C — Rotation and revocation:** Replace or invalidate keys when required while managing dependent systems and retained data.
- **D — Key separation:** Use keys for their intended purpose and trust boundary rather than reusing one key across unrelated functions.

Coverage: M20; CEH v5 domain 9; Key lifecycle.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q024

**Answer: D — Signing is not confidentiality**

A signature can authenticate content while leaving that content readable to anyone who receives it.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Encoding is not encryption:** Encoding changes representation for interoperability and generally provides no secret-based confidentiality.
- **B — Steganography hides presence:** Steganography hides information within another carrier; secrecy of content may still require encryption.
- **C — Hashing is not password encryption:** Password verification normally uses a suitable one-way password KDF and salt rather than reversible encryption or a fast unsalted hash.

Coverage: M20; CEH v5 domain 9; Common confusions.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q025

**Answer: C — Cryptographic hash**

A cryptographic hash produces a fixed-size digest without a secret key; an untrusted digest alone does not prove origin.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Symmetric encryption:** Symmetric encryption uses shared secret key material to protect confidentiality, with suitable modes and key handling.
- **B — Digital signature:** A digital signature uses a private signing key and public verification key to authenticate signed content under a trust model.
- **D — HMAC:** HMAC uses a shared secret key and a hash-based construction to authenticate messages; any party holding the key can generate a valid tag.

Coverage: M20; CEH v5 domain 9; Cryptographic primitives.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q026

**Answer: B — Second-preimage resistance**

Second-preimage resistance makes finding a different input with the same digest as a given input impractical.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Forward secrecy:** Forward secrecy protects past session keys against later compromise of a long-term key when the protocol and key exchange provide it.
- **C — Preimage resistance:** Preimage resistance makes finding an input for a specified hash output computationally impractical under the intended security level.
- **D — Collision resistance:** Collision resistance makes finding any two distinct inputs with the same digest impractical under the intended security level.

Coverage: M20; CEH v5 domain 9; Security properties.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q027

**Answer: D — ECB pattern leakage**

ECB independently encrypts equal plaintext blocks under the same key into equal ciphertext blocks, exposing repeated structure.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — CTR nonce uniqueness:** CTR-style encryption requires avoiding reuse of the relevant nonce/counter stream under the same key, or plaintext relationships can leak.
- **B — CBC IV requirement:** CBC encryption needs a suitable unpredictable initialization vector and separate integrity protection when used without an authenticated construction.
- **C — Authenticated encryption:** Authenticated encryption, such as correctly used GCM, protects confidentiality and detects tampering while still requiring proper nonce and key handling.

Coverage: M20; CEH v5 domain 9; Encryption modes.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q028

**Answer: A — Certificate-chain validation**

Validate a certificate through an accepted trust chain under the verifier's policy.

Why the other choices do not identify the asked-for mechanism or decision:

- **B — Validity and revocation handling:** Consider validity periods and applicable revocation mechanisms according to the client and deployment policy.
- **C — Hostname validation:** Check that the certificate identity matches the intended service name rather than merely trusting its issuer.
- **D — Private-key protection:** Protect the private key from disclosure or misuse; a public certificate does not need to be kept secret.

Coverage: M20; CEH v5 domain 9; PKI and certificates.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q029

**Answer: B — Key separation**

Use keys for their intended purpose and trust boundary rather than reusing one key across unrelated functions.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Cryptographically secure randomness:** Security-sensitive keys and nonces need an appropriate unpredictable generator and correct construction-specific handling.
- **C — Secure destruction and retention:** Retain keys only as needed and destroy them appropriately when their authorized lifetime ends, considering recovery obligations.
- **D — Rotation and revocation:** Replace or invalidate keys when required while managing dependent systems and retained data.

Coverage: M20; CEH v5 domain 9; Key lifecycle.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)

### CEH26-M20-Q030

**Answer: C — Encoding is not encryption**

Encoding changes representation for interoperability and generally provides no secret-based confidentiality.

Why the other choices do not identify the asked-for mechanism or decision:

- **A — Hashing is not password encryption:** Password verification normally uses a suitable one-way password KDF and salt rather than reversible encryption or a fast unsalted hash.
- **B — Signing is not confidentiality:** A signature can authenticate content while leaving that content readable to anyone who receives it.
- **D — Steganography hides presence:** Steganography hides information within another carrier; secrecy of content may still require encryption.

Coverage: M20; CEH v5 domain 9; Common confusions.
Technical references: [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · [OWASP Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) · [NIST GCM specification](https://csrc.nist.gov/pubs/sp/800/38/d/final) · [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)
