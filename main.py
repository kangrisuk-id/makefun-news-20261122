"""Entry program for make.fun bounty news-image-20261122.

The repository holds one finished front-page image, entry.png, drawn by
generate_image.py from the world news reported for Sunday 22 November
2026.  This program's only job is to place those exact bytes where the
bounty harness expects them: /output/entry.png.  It uses nothing but
the Python standard library and no network, so two runs always write
identical bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def destination():
    """Return the path the harness reads the entry image from."""
    if os.path.isdir("/output"):
        return os.path.join("/output", "entry.png")
    out_dir = os.path.join(HERE, "output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.png")


def main():
    if not os.path.isfile(SOURCE):
        print("entry.png is missing beside main.py", file=sys.stderr)
        return 1
    target = destination()
    shutil.copyfile(SOURCE, target)
    # Read both files back: a short or mismatched copy must fail loudly
    # here rather than hand the judge a truncated image.
    with open(SOURCE, "rb") as fh:
        expected = fh.read()
    with open(target, "rb") as fh:
        written = fh.read()
    if written != expected:
        print("copy verification failed for", target, file=sys.stderr)
        return 1
    print("wrote", target, len(written), "bytes, verified identical")
    return 0


if __name__ == "__main__":
    sys.exit(main())
