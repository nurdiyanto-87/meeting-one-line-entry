#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line — entry.

Writes one sentence to /output/entry.txt: the single line that could
have replaced an entire pointless meeting.

Pure standard library, deterministic, no network, no input files.
The text is fixed so both grader runs produce byte-identical output.
"""

import os

# Candidate B (final, revised from A): same idea, sharper delivery.
# The deadpan list up front ("An hour, six salaries, and...") names
# the cost before the punchline, and "the only decision this meeting
# made was to schedule another meeting" says the meeting's sole output
# was itself — it kills the meeting outright, it is instantly
# relatable, and the sting is that meetings reproduce. Dropped A's
# "we need another meeting" for the more concrete "schedule another
# meeting", and "exactly one thing" for the flatter "only decision".
ENTRY = (
    "An hour, six salaries, and the only decision this meeting made "
    "was to schedule another meeting."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the gate: 1-200 chars, UTF-8, not whitespace-only,
    exactly one line."""
    if not text or not text.strip():
        raise SystemExit("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text:
        raise SystemExit("entry must be exactly one line")


def main() -> None:
    text = ENTRY
    validate(text)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
