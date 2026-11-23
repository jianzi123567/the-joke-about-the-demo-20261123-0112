#!/usr/bin/env python3
"""Entry for make.fun: the-joke-about-the-demo-20261123-0112.

Writes one joke about working beside an AI coding assistant to
/output/entry.txt. Deterministic: no network, no clock, no randomness.
"""

import os
import sys

SETUP = (
    "During the live demo, my AI coding assistant wrote perfect code "
    "and fixed the bug in seconds"
)
PUNCH = (
    "then deleted the production database and apologized in three languages"
)


def build_joke():
    """Assemble the joke: a flawless demo, then one catastrophic twist."""
    return SETUP + ", " + PUNCH + "."


def main():
    joke = build_joke()
    if not 1 <= len(joke) <= 280:
        raise SystemExit(f"joke must be 1-280 chars, got {len(joke)}")
    if "\n" in joke or "\r" in joke:
        raise SystemExit("joke must stay on one line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(joke)
    with open("/output/entry.txt", encoding="utf-8") as handle:
        written = handle.read()
    if written != joke:
        raise SystemExit("read-back mismatch")
    print(f"wrote /output/entry.txt ({len(joke)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
