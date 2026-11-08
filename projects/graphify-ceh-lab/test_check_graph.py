import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("graph_check", Path(__file__).with_name("check_graph.py"))
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)

class GraphReadReuse(unittest.TestCase):
    def test_one_read_per_source_and_fresh_snapshot_per_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            corpus = root / "corpus"
            corpus.mkdir()
            note = corpus / "note.md"
            note.write_text("# Evidence\ntext\n", encoding="utf-8")
            labels = ["Port Observation", "Service Identification", "Vulnerability Assessment", "Remediation Plan", "Verification Record"]
            nodes = [dict(id=str(i), label=label, source_file="note.md", source_location="Evidence") for i, label in enumerate(labels)]
            links = [dict(source=str(i), target=str(i+1), source_file="note.md", source_location="L2", confidence="EXTRACTED", confidence_score=1.0) for i in range(4)]
            graph = root / "graph.json"
            graph.write_text(json.dumps(dict(directed=True, graph=dict(schema_version="1", graphify_version="test"), nodes=nodes, links=links)))
            reads = []
            original = Path.read_text
            def counted(path, *args, **kwargs):
                reads.append(path)
                return original(path, *args, **kwargs)
            with patch.object(Path, "read_text", counted):
                self.assertEqual(CHECK.check(graph, corpus), ([], 5, 4))
            self.assertEqual(reads.count(note), 1)
            # Cache must be invocation-local: changed headings/ranges are detected.
            note.write_text("# Changed\n", encoding="utf-8")
            errors, _, _ = CHECK.check(graph, corpus)
            self.assertEqual(sum("section not found" in e for e in errors), 5)
            self.assertEqual(sum("line location out of range" in e for e in errors), 4)

if __name__ == "__main__":
    unittest.main()
