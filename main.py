"""Write the one-chill entry line to the output file."""

import os

LINE = (
    "Every photo on my phone now has one extra person in it, "
    "standing a little closer each time."
)


def emit() -> None:
    folder = "/output"
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    emit()
