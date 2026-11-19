#!/usr/bin/env python3
"""Copy the news-image entry to the output directory.

Reads assets/entry.png (the 1024x1024 infographic summing up the world
news of 19 November 2026) and writes it to /output/entry.png, creating
the output directory when it does not exist yet.

The copy is verified afterwards: the SHA-256 of the output must match
the SHA-256 of the source, so the program is deterministic and the
delivered image is byte-identical to the one in the repository.
"""

import hashlib
import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(__file__), "assets", "entry.png")
OUTPUT_DIR = "/output"
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not os.path.isfile(SOURCE):
        print(f"missing source image: {SOURCE}", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    source_hash = sha256(SOURCE)
    output_hash = sha256(OUTPUT)
    print(f"copied {SOURCE} -> {OUTPUT}")
    print(f"sha256: {output_hash}")
    if source_hash != output_hash:
        print("error: output differs from source", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
