# M08 source validation

Exact copies of actual M08 package QA and the closed-ZIP receipt. [Copy integrity](copy-integrity.json) records the preserved identities.

- [Source checks](source_qa.json): 811 passed, 0 failed.
- [Browser checks](browser_qa.json): 94 passed, 0 failed; 58 boards, four actual examples, 12 repeated seek pairs with identical screenshot hashes.
- [Offline packet checks](packet_qa.json): 43 passed, 0 failed; nine actual filters across six synthetic files.
- [Verbose decoding](packet_verbose_decode.json): all six actual tcpdump reads exit zero; no bad-checksum diagnostics.
- [ZIP receipt](release_receipt.json): 308 files, 306 extracted payload hashes, CRC and extraction checks pass.
- [Visual review](visual-review.md) and [toolchain](toolchain.json) record actual review and versions.
- Four hyperframes-*.json receipts pass, each with one nonblocking single-clip Studio structure warning.

Source checks assert packet/browser receipt success without replacing their separate scopes. Full M08 speech, aligned captions, all 58 final animated scenes, MP4 and switch enforcement are not established by these receipts.

[Production record](../../../notes/m08-sniffing/video-production-2026-10-18.md) owns the interpretation and next gate.
