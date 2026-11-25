#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes a single sentence to /output/entry.txt (or ./output/entry.txt
when /output is not writable, e.g. during a local run).
Standard library only. Deterministic: same output on every run.
"""

import os
import sys

ENTRY = "This meeting could have been an email, and that email could have been deleted unread."


def main() -> int:
    text = ENTRY.strip()
    # Gate check, mirroring the contest gate: 1-200 chars, one line,
    # one sentence, not only whitespace.
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.endswith(".") and text.count(".") == 1, "entry must be one sentence"
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
