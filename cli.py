"""CLI for parsing rental links from local HTML."""

from __future__ import annotations

import argparse
from pathlib import Path

from rental_parser.io_utils import read_html, write_json
from rental_parser.parser import extract_links


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="rental-parser",
        description="Extract links from local rental listing HTML pages.",
    )
    parser.add_argument("--input", type=Path, required=True, help="Path to HTML file")
    parser.add_argument("--json-out", type=Path, required=True, help="Output JSON path")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if not args.input.exists():
        raise SystemExit(f"Input file not found: {args.input}")

    html = read_html(args.input)
    links = extract_links(html)
    write_json(args.json_out, {"count": len(links), "links": links})
    print(f"Extracted {len(links)} links to {args.json_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
