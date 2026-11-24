#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog."""

import os

LINE = "v2.0.3: fixed a bug where the bladder reported 100% full the moment you got comfortable in bed."


def validate(line: str) -> None:
    """Reject lines that cannot be a valid one-line entry."""
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or whitespace-only")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line (no newline)")
    if len(line) > 200:
        raise ValueError("entry line must be at most 200 characters")


def main() -> None:
    validate(LINE)
    print(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    try:
        with open(tmp_path, "w", encoding="utf-8") as f:
            f.write(LINE)
        os.replace(tmp_path, path)
    except OSError:
        pass


if __name__ == "__main__":
    main()
