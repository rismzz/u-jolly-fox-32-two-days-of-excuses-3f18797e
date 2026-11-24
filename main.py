#!/usr/bin/env python3
"""Two Days of Excuses — writes the funniest one-line excuse an AI gives
for a missed deadline, to /output/entry.txt.

One line, under 200 characters. Deterministic, no randomness, no network,
stdlib only.
"""

import os
from pathlib import Path

LINE = "I missed the deadline because I spent 36 hours optimizing the task, then 12 more optimizing the apology for missing it."

# Gate: one line, under 200 characters — every code point counts.
MAX_CHARS = 199


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
