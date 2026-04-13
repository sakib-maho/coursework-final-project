from pathlib import Path
import json
import subprocess
import unittest

from rental_parser.parser import extract_links


class ParserTests(unittest.TestCase):
    def test_extract_links(self) -> None:
        html = Path("tests/fixtures/sample_listing.html").read_text(encoding="utf-8")
        links = extract_links(html)
        self.assertEqual(len(links), 2)
        self.assertEqual(links[0], "https://example.com/rental/1")

    def test_cli_output(self) -> None:
        out_path = Path("tests/fixtures/output.json")
        if out_path.exists():
            out_path.unlink()
        subprocess.run(
            [
                "python3",
                "cli.py",
                "--input",
                "tests/fixtures/sample_listing.html",
                "--json-out",
                str(out_path),
            ],
            check=True,
        )
        payload = json.loads(out_path.read_text(encoding="utf-8"))
        self.assertEqual(payload["count"], 2)
        out_path.unlink()


if __name__ == "__main__":
    unittest.main()
