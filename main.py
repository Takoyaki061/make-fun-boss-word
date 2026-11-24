#!/usr/bin/env python3
"""One Word for the Boss — writes one word to /output/entry.txt.

The word: "Meetingholic". The boss who calls a meeting about the
meeting, then schedules a follow-up to discuss what the meeting
decided. Every worker in every industry has sat in that meeting,
which is why the word lands on its own with no caption needed.

Stdlib only, deterministic, no network.
"""

import os

WORD = "Meetingholic"


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-30 characters,
    # not only whitespace, and exactly one word — no spaces, no
    # phrase, no caption — or the entry scores 0 and never reaches
    # the judge.
    if not 1 <= len(WORD) <= 30:
        raise ValueError(f"word is {len(WORD)} characters, must be 1-30")
    if not WORD.strip():
        raise ValueError("word must not be only whitespace")
    if len(WORD.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if any(ch.isspace() for ch in WORD):
        raise ValueError("word must contain no whitespace")
    if not WORD.isalpha():
        raise ValueError("word must be letters only, no digits or punctuation")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read back and verify: the grader reads this file, so confirm the
    # bytes on disk are exactly the word that passed the gate above.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        raise ValueError("entry.txt on disk differs from the word")
    print(WORD)


if __name__ == "__main__":
    main()
