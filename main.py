"""Entry for the make.fun bounty "Describe Your Ex in One Word".

Writes exactly one word to /output/entry.txt.
"""

import os

ENTRY = "Recalled"  # like a defective product: recalled, returned, done.


def main() -> None:
    assert ENTRY.isalpha() and " " not in ENTRY, "entry must be one word"
    assert 1 <= len(ENTRY) <= 111, "entry must be 1-111 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
