#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

This program produces the competition artifact: a single horror
sentence written to /output/entry.txt. The sentence lives in one
constant below, and the file is written byte-for-byte from that
constant, with no trailing newline and no added formatting, so what
the judge reads is exactly the sentence as drafted.
"""

import os

# The entry: a single sentence, under 200 characters. A ward log
# records a dead woman's final words, yet the script in the log is
# the narrator's own — the chill comes from what that implies: the
# narrator was present, writing, and has no memory of doing it.
# The closing word carries the turn, so nothing follows it.
LINE = (
    "The night nurse logged my mother's last words at 3am, "
    "but my mother died in 2019, and the handwriting in the log is mine."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write the sentence exactly as drafted: strip trailing
    # whitespace so the file's length equals the sentence itself,
    # with no newline at the end to inflate the byte count.
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE.strip())


if __name__ == "__main__":
    main()
