# Offline trust-evidence exercise

**SIMULATED OUTPUT:** 14 inert artifact files and their manifest, including one constructed email, JSON records, authored call/witness/notice text, a generated QR SVG and two CSV tables. The fixed campus dates are fictional context, not collection timestamps.

From the package root run `python3 tooling/verify_evidence.py`. Add `--record` only when deliberately refreshing validation/evidence_qa.json. The verifier uses Python's local email/JSON/CSV parsers and SHA-256. It sends nothing, opens no links, resolves no hosts, collects no credentials and starts no network service. Read the complete [case guide](../case/EVIDENCE_CARDS.md).

E01's Authentication-Results strings are stipulated receiver claims, not actual SPF/DKIM/DMARC execution. E03's QR encoder and source string are recorded; independent QR decoding is not exercised. These boundaries remain explicit. The reserved test-domain destination has no supplied collection page.

The assessment table has 20 fictional eligible rows, 18 delivered rows, six link events (five stipulated learners, one automated scanner), and four reports. Define a denominator and event before computing a rate. These counts describe constructed rows, not employee performance or a population experiment.
