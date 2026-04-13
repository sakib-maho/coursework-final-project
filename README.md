# Coursework Final Project - Rental HTML Parser

<!-- BrandCloud:readme-standard -->
[![Maintained](https://img.shields.io/badge/Maintained-yes-brightgreen.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Showcase](https://img.shields.io/badge/Portfolio-Showcase-blue.svg)](#)

_Part of the `sakib-maho` project showcase series with consistent documentation and quality standards._

This project was upgraded into a practical Python CLI that extracts rental listing links from
local HTML files and exports structured JSON output.

## Features

- HTML anchor extraction for listing links
- Filters links to web/local paths (`http`, `https`, `/...`)
- JSON export with link count
- Fixture-based unit tests
- Modular parser package structure

## Quick Start

```bash
git clone https://github.com/sakib-maho/coursework-final-project.git
cd coursework-final-project
python3 cli.py --input tests/fixtures/sample_listing.html --json-out output/links.json
```

## Run Tests

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## Project Structure

```text
coursework-final-project/
├── cli.py
├── rental_parser/
│   ├── io_utils.py
│   └── parser.py
├── tests/
│   ├── fixtures/sample_listing.html
│   └── test_parser.py
└── main.py
```

## License

MIT License. See `LICENSE`.
