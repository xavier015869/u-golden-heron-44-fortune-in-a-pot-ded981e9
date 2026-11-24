"""Fortune in a Pot — write one kind, funny fortune for a houseplant.

The program writes a single line of at most 120 characters to
/output/entry.txt. The fortune is a prediction about the plant on
the windowsill: warm, a little funny, and written for this plant
in this window, not for any plant anywhere.
"""

import os

FORTUNE = (
    "Soon the morning sun will pick your leaves out of the whole "
    "windowsill, and your keeper will beam: that's my plant."
)


def main() -> None:
    text = FORTUNE.strip()
    if not 1 <= len(text) <= 120:
        raise ValueError(f"fortune must be 1-120 characters, got {len(text)}")
    if "\n" in text:
        raise ValueError("fortune must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
