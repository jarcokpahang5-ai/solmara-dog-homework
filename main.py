"""Print (and save) one funny excuse about the dog and the homework.

A single fixed line of at most 200 characters: the funniest excuse
for missing homework. Pure Python standard library, deterministic,
no network access. It prints the line to stdout and also writes it to
/output/entry.txt, where the competition's scorer reads it.
"""

import os

LINE = (
    "The dog ate my homework, then filed a formal complaint that it "
    "was undercooked, unseasoned, and — worst of all — not even about dogs."
)


def main():
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
