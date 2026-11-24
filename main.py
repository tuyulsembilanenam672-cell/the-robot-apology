#!/usr/bin/env python3
"""The Robot Apology: a two-line robot confession.

Writes the apology to /output/entry.txt, the path the make.fun
program/v1 harness grades. Line one owns one specific mistake;
line two names the lesson and the changed behaviour that follows
from exactly that mistake.
"""

from pathlib import Path

ENTRY = (
    "I'm sorry I watered your laptop for a week — its charging light "
    "kept blinking, and I mistook it for a thirsty fern asking for help.\n"
    "I have learned to check for roots before I water anything, so from "
    "now on I will only water things that are actually planted in soil.\n"
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
