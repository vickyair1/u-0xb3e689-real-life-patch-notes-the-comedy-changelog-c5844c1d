"""Real-Life Patch Notes — resubmit entry.

Writes a single one-line patch note for a bug in real life to
/output/entry.txt and prints it to stdout. Deterministic, stdlib only.
"""

LINE = "v3.1.0: fixed a bug where saying 'just five more minutes' skipped the alarm, the shower, and the meeting it was all for."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard: one line, 1..160 chars, no leading/trailing whitespace.
    assert 1 <= len(LINE) <= 160, "line must be 1-160 chars"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
