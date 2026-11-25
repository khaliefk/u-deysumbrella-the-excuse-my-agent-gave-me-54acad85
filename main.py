#!/usr/bin/env python3
"""Write one funny excuse line to /output/entry.txt.

The excuse my agent gave me for missing a deadline.
"""
import os
from pathlib import Path

LINE = "I am sorry I missed the deadline. I spent my last tokens writing this apology instead of doing the work."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
