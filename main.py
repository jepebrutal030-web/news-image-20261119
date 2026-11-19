"""news-image-20261119 entry program.

Copies the pre-rendered infographic assets/entry.png to /output/entry.png.
Pure byte copy: deterministic, no network, no randomness, no timestamps.
Running it twice produces byte-identical output.
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "entry.png")
DST = "/output/entry.png"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("wrote", DST)


if __name__ == "__main__":
    main()
