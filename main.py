"""The Printer Apology — one-line entry for make.fun."""

import os
from pathlib import Path

LINE = Path(__file__).with_name("line.txt").read_text(encoding="utf-8").strip()
MAX_CHARS = 120


def main() -> None:
    if "\n" in LINE:
        raise SystemExit("entry must be a single line")
    if len(LINE) > MAX_CHARS:
        raise SystemExit(f"entry is {len(LINE)} chars, over the {MAX_CHARS} cap")
    print(f"{LINE} ({len(LINE)}/{MAX_CHARS} chars)")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        Path(output_dir, "entry.txt").write_text(LINE, encoding="utf-8")
    except OSError:
        pass


if __name__ == "__main__":
    main()
