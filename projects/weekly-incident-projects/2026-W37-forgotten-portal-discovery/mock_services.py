#!/usr/bin/env python3
"""Loopback-only service inventory for WP-2026-W37."""

from __future__ import annotations

import argparse
import json
import sys
import threading
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


SERVICES = (
    (8765, "public-portal", "1.4.2", "Digital Services"),
    (8766, "legacy-reporting", "0.8.1", "Unassigned"),
    (8767, "observability", "2.1.0", "Platform Operations"),
)


class MockHTTPServer(ThreadingHTTPServer):
    def handle_error(self, request, client_address) -> None:
        if isinstance(sys.exception(), ConnectionResetError):
            return
        super().handle_error(request, client_address)


def handler_for(role: str, version: str, owner: str):
    class Handler(BaseHTTPRequestHandler):
        server_version = f"NorthbridgeMock/{version}"
        sys_version = ""

        def do_GET(self) -> None:
            if self.path == "/health":
                payload = {"status": "ok", "role": role}
            elif self.path == "/service-info":
                payload = {
                    "role": role,
                    "version": version,
                    "owner": owner,
                    "environment": "fictional-loopback-training",
                }
            else:
                self.send_error(404, "Path outside the mock service interface")
                return
            body = json.dumps(payload, sort_keys=True).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    return Handler


def start_servers(use_ephemeral_ports: bool = False):
    servers = []
    try:
        for port, role, version, owner in SERVICES:
            bind_port = 0 if use_ephemeral_ports else port
            server = MockHTTPServer(
                ("127.0.0.1", bind_port), handler_for(role, version, owner)
            )
            servers.append((server, role))
            threading.Thread(target=server.serve_forever, daemon=True).start()
        return servers
    except Exception:
        for server, _ in servers:
            server.shutdown()
            server.server_close()
        raise


def stop_servers(servers) -> None:
    for server, _ in servers:
        server.shutdown()
        server.server_close()


def self_test() -> None:
    servers = start_servers(use_ephemeral_ports=True)
    try:
        observed = []
        for server, expected_role in servers:
            port = server.server_address[1]
            with urllib.request.urlopen(
                f"http://127.0.0.1:{port}/service-info", timeout=2
            ) as response:
                payload = json.load(response)
            assert payload["role"] == expected_role
            assert payload["environment"] == "fictional-loopback-training"
            observed.append(expected_role)
        assert observed == [service[1] for service in SERVICES]
        print("SELF_TEST_OK: three loopback mock services returned expected metadata")
    finally:
        stop_servers(servers)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return

    servers = start_servers()
    for server, role in servers:
        print(f"LISTENING 127.0.0.1:{server.server_address[1]} role={role}")
    print("Press Ctrl-C to stop all mock services.")
    try:
        threading.Event().wait()
    except KeyboardInterrupt:
        print("\nStopping mock services.")
    finally:
        stop_servers(servers)


if __name__ == "__main__":
    main()
