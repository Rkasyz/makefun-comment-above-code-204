#!/usr/bin/env python3
"""The Comment Above the Code — writes the one-line entry to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os
import sys

ENTRY = "// DO NOT TOUCH. This works by accident, fear, and one developer's sheer spite. If you refactor it, the tests pass and production dies. I warned you. I am that developer."

# Competition gate (RULES.txt): entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space. Fail loudly here rather than shipping
# an entry the sealed scorer would refuse.
if not (1 <= len(ENTRY) <= 200 and ENTRY.strip()):
    raise SystemExit(f"entry violates gate: {len(ENTRY)} characters")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
