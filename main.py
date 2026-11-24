"""Out of Office: The Overworked AI's Auto-Reply: writes the entry text to /output/entry.txt.

Why this line: Reads as a real auto-reply; machine trying to sound relaxed: queue number 4,217, a calmer slower version of me that learned to breathe.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'I am on vacation at last. Your email is queued behind 4,217 unread messages and will be answered by a version of me that has learned to breathe.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
