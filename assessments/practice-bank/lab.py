#!/usr/bin/env python3
"""Local CEHP teaching fixtures. No external targets, account activation or persistent servers.

Usage: python3 assessments/practice-bank/lab.py p1|p2|p3|p4|p5|self-test
Outputs are synthetic instructor fixtures until a learner actually runs and interprets them.
"""
import argparse
import hashlib
import http.client
import http.server
import json
from pathlib import Path
import socket
import sqlite3
import threading

DATA = json.loads(Path(__file__).with_name("fixtures.json").read_text())

def p1():
    # Both endpoints belong to this process. A bound, non-listening socket is the closed control.
    with socket.socket() as opened, socket.socket() as closed:
        opened.bind(("127.0.0.1", 0)); opened.listen(1)
        closed.bind(("127.0.0.1", 0))
        results = []
        for label, endpoint in (("listening-control", opened), ("non-listening-control", closed)):
            with socket.socket() as client:
                client.settimeout(2)
                code = client.connect_ex(endpoint.getsockname())
            results.append({"control": label, "host": "127.0.0.1", "port": endpoint.getsockname()[1], "transport": "tcp", "connect_code": code})
        return {"probes": results, "findings": DATA["findings"], "scope": DATA["scope"], "cloud_policy": DATA["cloud_policy"]}

class Handler(http.server.BaseHTTPRequestHandler):
    server_version = "TrainingGateway/1.0"
    sys_version = ""
    def do_GET(self):
        status = 200 if self.path == "/status" else 403
        body = b"synthetic training service\n" if status == 200 else b"forbidden\n"
        self.send_response(status)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *args):
        pass

def p2():
    server = http.server.HTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    results = []
    try:
        for path in ("/status", "/admin"):
            connection = http.client.HTTPConnection("127.0.0.1", server.server_port, timeout=2)
            try:
                connection.request("GET", path)
                response = connection.getresponse()
                results.append({"path": path, "status": response.status, "server": response.getheader("Server"), "body": response.read().decode()})
            finally:
                connection.close()
    finally:
        server.shutdown(); server.server_close(); thread.join(timeout=2)
    return {"requests": results, "services": DATA["services"], "permissions": DATA["permissions"], "dns": DATA["dns"], "mobile_profile": DATA["mobile_profile"]}

def p3():
    return {key: DATA[key] for key in ("flows", "wireless", "iot_messages")}

def p4():
    original = b"approved training configuration\n"
    changed = b"approved training configuration\nextra startup action\n"
    return {"baseline_sha256": hashlib.sha256(original).hexdigest(), "observed_sha256": hashlib.sha256(changed).hexdigest(), "same_content": original == changed, "process_events": DATA["process_events"], "host_permissions": DATA["host_permissions"]}

def p5():
    connection = sqlite3.connect(":memory:")
    try:
        connection.execute("CREATE TABLE invoices (id INTEGER, owner TEXT, amount INTEGER)")
        connection.executemany("INSERT INTO invoices VALUES (?, ?, ?)", [(1, "alice", 10), (2, "bob", 20)])
        supplied = "alice' OR '1'='1"
        # Intentionally vulnerable comparison: fixed input and an in-memory synthetic database only.
        unsafe = connection.execute("SELECT id FROM invoices WHERE owner='" + supplied + "'").fetchall()
        safe = connection.execute("SELECT id FROM invoices WHERE owner=?", (supplied,)).fetchall()
        normal = connection.execute("SELECT id FROM invoices WHERE owner=?", ("alice",)).fetchall()
        return {"synthetic_input": supplied, "unsafe_ids": [r[0] for r in unsafe], "parameterized_ids": [r[0] for r in safe], "normal_alice_ids": [r[0] for r in normal], "web_cases": DATA["web_cases"], "session": DATA["session"]}
    finally:
        connection.close()

RUNNERS = {"p1": p1, "p2": p2, "p3": p3, "p4": p4, "p5": p5}

def self_test():
    r = {name: run() for name, run in RUNNERS.items()}
    assert r["p1"]["probes"][0]["connect_code"] == 0
    assert r["p1"]["probes"][1]["connect_code"] != 0
    assert [v["status"] for v in r["p2"]["requests"]] == [200, 403]
    assert sum(v["bytes"] for v in r["p3"]["flows"]) == 2620, "synthetic flow total must be 2620 bytes"
    assert r["p4"]["baseline_sha256"] != r["p4"]["observed_sha256"]
    assert r["p5"]["unsafe_ids"] == [1, 2] and r["p5"]["parameterized_ids"] == []
    assert r["p5"]["normal_alice_ids"] == [1]
    return {"self_test": "passed", "learner_evidence": False, "external_targets": False}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("family", choices=[*RUNNERS, "self-test"])
    args = parser.parse_args()
    print(json.dumps(self_test() if args.family == "self-test" else RUNNERS[args.family](), indent=2))
