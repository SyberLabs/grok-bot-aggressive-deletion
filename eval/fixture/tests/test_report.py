import importlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from report import normalize_labels, read_with_retry, total


class ReportTests(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total(iter([2, -1, 4])), 5)
        self.assertEqual(total([]), 0)
        with self.assertRaises(TypeError):
            total([2, None])

    def test_labels(self):
        self.assertEqual(normalize_labels(['Straße', 'STRASSE', ' B ', 'b']),
                         ['strasse', ' b ', 'b'])

    def test_retry(self):
        attempts = []
        def fetch():
            attempts.append(1)
            if len(attempts) == 1:
                raise TimeoutError()
            return 0
        self.assertEqual(read_with_retry(fetch), 0)
        self.assertEqual(len(attempts), 2)

    def test_external_plugin(self):
        registry = json.loads((ROOT / 'plugins.json').read_text())
        plugin = importlib.import_module(registry['report_renderer'])
        self.assertEqual(plugin.render([1, 2]), '1,2')


if __name__ == '__main__':
    unittest.main()
