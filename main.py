"""Backward-compatible entrypoint for the parser CLI."""

from cli import main


if __name__ == "__main__":
    raise SystemExit(main())
