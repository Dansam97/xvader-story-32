#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters - make.fun entry.

Writes one Wi-Fi network name (at most 32 characters) to entry.txt in
the output directory: a name that lands a joke and implies a whole
story - she left, she took the kids, and she took the router, which
is why this network is broadcasting its own obituary.
"""

import os

ENTRY_TEXT = "SheTookTheKidsAndTheRouter"
MAX_CHARS = 32


def validated_text() -> str:
    """Return the entry text after checking it against the gate:
    UTF-8 text of 1 to 32 characters, not only white space."""
    text = ENTRY_TEXT
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    text.encode("utf-8")  # raises if the text is not UTF-8 encodable
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="" keeps the write byte-exact: the text itself, no trailing
    # newline added, so the character count the gate sees is exact.
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(validated_text())


if __name__ == "__main__":
    main()
