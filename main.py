#!/usr/bin/env python3
"""Deadpan forecast for an invented city.

Writes a single line (<= 160 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt:
a weather forecast for Fogmouth, a city that does not exist, delivered in
the flat, confident tone of a TV meteorologist who has seen it all. The
absurdity is one deadpan twist -- the lighthouse filing a formal complaint
about the fog -- anchored by concrete numbers (8 degrees, drizzle) so the
line still reads like a real broadcast.
"""

import os

ENTRY = (
    "In Fogmouth, expect 8 degrees and drizzle, with fog so thick the "
    "lighthouse has filed a formal complaint with the harbour board."
)


def main() -> None:
    # One fixed line, no randomness and no I/O beyond the output file, so
    # every run produces byte-identical output.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, f"entry is {len(text)} characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
