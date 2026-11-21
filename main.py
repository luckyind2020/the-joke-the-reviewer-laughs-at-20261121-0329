"""One-line joke about working beside an AI coding agent.

Writes the joke to <output>/entry.txt, where <output> comes from the
MAKEFUN_OUTPUT_DIR environment variable when set, else /output.
"""

import os
import sys


JOKE = (
    "My AI agent writes the code, the tests, and the docs; "
    "I rename one variable so the commit still looks like mine."
)


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_text(text):
    """Gate: 1-280 Unicode code points, not only whitespace."""
    if not (1 <= len(text) <= 280):
        return f"entry must be 1-280 characters, got {len(text)}"
    if not text.strip():
        return "entry must not be only whitespace"
    return None


def main():
    text = JOKE.strip()
    problem = check_text(text)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
