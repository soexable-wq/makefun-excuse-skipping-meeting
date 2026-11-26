#!/usr/bin/env python3
"""Funniest Excuse for Skipping a Meeting — make.fun entry.

Writes a single line, at most 200 characters, to /output/entry.txt.
Deterministic, no network, no secrets, no dependencies.
"""

import os

ENTRY = "Sorry, I can't make the meeting — my calendar invited me to a meeting about the meeting, and I'm still recovering from the last one."


def main() -> None:
    assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, limit 200"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
