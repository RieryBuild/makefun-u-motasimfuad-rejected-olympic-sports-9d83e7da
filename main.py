"""Rejected Olympic Sports — one-line text entry.

Writes a single funny one-line sport the Olympics rejected to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Pure Python standard library (os only). No trailing newline: the gate
requires 1-200 UTF-8 characters, exactly one line.
"""

import os

ENTRY = (
    "Competitive umbrella sharing: two athletes, one umbrella, "
    "a 40-minute walk in sideways rain \u2014 the driest shoulder wins, "
    "and the loser holds it on the podium."
)


def validate_entry(text):
    """Enforce the competition gate before anything is written."""
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def build_entry():
    """Return the single entry line."""
    return ENTRY


def write_entry(path, text):
    """Write the line with no trailing newline, then verify the bytes."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise ValueError("written bytes do not match the entry")


def main():
    text = build_entry()
    validate_entry(text)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    write_entry(os.path.join(output_dir, "entry.txt"), text)


if __name__ == "__main__":
    main()
