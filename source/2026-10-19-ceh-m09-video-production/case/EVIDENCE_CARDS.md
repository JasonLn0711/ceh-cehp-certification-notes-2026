# Four connected Northstar trust cases

**SIMULATED OUTPUT.** The files are constructed teaching artifacts. [Actual offline QA](../validation/evidence_qa.json) measures local parsing, hashes and arithmetic. Receiver authentication strings are stipulated, no QR decoder is exercised, and no contact, account, financial or physical system is activated.

## E01

Files: [E01_supplier_message.eml](../lab_mock/E01_supplier_message.eml), [E01_supplier_record.json](../lab_mock/E01_supplier_record.json), [E01_payment_ticket.json](../lab_mock/E01_payment_ticket.json)

Observation: Expected supplier mailbox, stipulated authentication passes, changed training destination and differing supplied/approved contacts.

Unknown: Sender control, supplier authorization and completed payment remain unmeasured.

Next check: Finance verifies through the approved independent contact and required approval/transaction records.

## E02

Files: [E02_call_transcript.md](../lab_mock/E02_call_transcript.md), [E02_directory_record.json](../lab_mock/E02_directory_record.json), [E02_recovery_ticket.json](../lab_mock/E02_recovery_ticket.json)

Observation: Urgent claimed-employee recovery request; supplied contact differs from directory; ticket pending verification.

Unknown: Verified identity, reset, enrollment and subsequent account use are not supplied.

Next check: Identity-service owner applies the recovery policy and checks actual account-state records.

## E03

Files: [E03_notice.md](../lab_mock/E03_notice.md), [E03_qr_code.svg](../lab_mock/E03_qr_code.svg), [E03_qr_payload.json](../lab_mock/E03_qr_payload.json), [E03_portal_context.json](../lab_mock/E03_portal_context.json)

Observation: Reserved encoded destination differs from the stipulated known learning portal; notice approval unconfirmed.

Unknown: QR scans, page loads, credential submissions and account use are unmeasured.

Next check: Learning owner verifies the announcement through the known campus route.

## E04

Files: [E04_appointments.json](../lab_mock/E04_appointments.json), [E04_door_events.csv](../lab_mock/E04_door_events.csv), [E04_witness_report.md](../lab_mock/E04_witness_report.md)

Observation: One credential event, a door-held interval and an unverified following-person report; claimed visit unconfirmed.

Unknown: Entrant count, visitor identity, intent and complete approval state are not established.

Next check: Authorized physical-security owner reviews appointment, escort and access evidence safely.
