# news-image-20261119 entry (Python 3.13, standard library only).
#
# The entry is the image itself: entry.png in this repository is the
# finished picture, so all this program has to do is copy it to the
# output directory, where the gate reads it.
#
# Deterministic and offline: no network, no wall clock, no randomness,
# no files outside the repository. The same entry.png always produces
# the same output bytes.
#
# Run it the way the grader does:
#   MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
try:
    shutil.copyfile(HERE / "entry.png", Path(OUTPUT_DIR) / "entry.png")
except OSError as exc:
    print(f"entry.png could not be copied: {exc}")
    raise SystemExit(1)
