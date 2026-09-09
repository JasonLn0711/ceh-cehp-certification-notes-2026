# Continuation publication coverage — 2026-09-09

The original local packet has 13 manifest-covered files, all freshly verified before publication. Two full-host socket inventories, preflight-sockets.txt and shutdown-sockets.txt, remain locally retained and Git-ignored because they include listeners outside the CEH exercise. Their original bytes and hashes are unchanged.

The repository publishes the other 11 original covered artifacts, the original manifest/coverage/verification receipt, source and interpretation notes, plus preflight-sockets.scoped.txt and shutdown-sockets.scoped.txt. Each derivative filters the original local-address column to TCP ports 8765–8767 and records zero matching rows. These are labeled derivatives, not replacements for the original hashed inventories. The original exit-status evidence remains in the supplied dialogue.

A fresh remote checkout cannot verify all 13 original entries without the two locally retained files. From this directory, `sha256sum --ignore-missing -c SHA256SUMS.txt` checks the 11 published originals; its result establishes only that published subset. The archived hash-verification.txt records the learner's original 13-file check. Scoped derivatives and later documentation are outside the original manifest.

Full evidence custody remains local for those two originals; this publication does not establish off-host backup of them. Future restoration must preserve the original hashes and keep derivatives separately identified.
