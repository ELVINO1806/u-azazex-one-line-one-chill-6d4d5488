"""One Line, One Chill — one-sentence horror entry.

Writes the horror line to /output/entry.txt when run.
"""

import os

LINE = (
    "Every photo on my phone now has one extra person in it, "
    "standing a little closer each time."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
