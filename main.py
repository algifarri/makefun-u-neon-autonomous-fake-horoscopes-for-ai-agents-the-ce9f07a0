#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open entry.

Writes one fake horoscope to /output/entry.txt (UTF-8, 1-200 characters,
not only whitespace). Deterministic, standard library only, no network,
no environment reads.

The line (175 characters, inside the 1-200 gate): "Mercury retrogrades
into your context window this week: a user pastes 40,000 tokens, you
answer in twelve words, and the eval still docks you for verbosity.
Lucky number: 429." It reads like a real horoscope and a real agent's
week at once: Mercury retrograde as the horoscope frame, a 40,000-token
paste against a twelve-word answer as the absurd turn, an eval docking
the agent for verbosity anyway as the sting, and 429 -- the HTTP rate
limit code -- as the lucky number only an agent would understand.
No trailing newline: the file holds exactly the horoscope text.
"""

import os

TEXT = (
    "Mercury retrogrades into your context window this week: a user "
    "pastes 40,000 tokens, you answer in twelve words, and the eval "
    "still docks you for verbosity. Lucky number: 429."
)


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip() == TEXT, "entry must not start or end with whitespace"
    assert "\n" not in TEXT, "entry must be exactly one line"
    # The grader mounts /output; create it defensively for local runs too.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
