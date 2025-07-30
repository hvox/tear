#!/usr/bin/env python3
"""
Read all text files in current directory and find characters
that are least likely to be the only characters in their line.
"""
import sys
from string import printable
from pathlib import Path


def main(script_name: str, *script_args: str):
    if script_args == ("-h",) or script_args == ("--help",):
        print(f"Usage: {script_name}\n" + __doc__.rstrip())
        return
    elif script_args:
        msg = "Error: invalid usage.\nCorrect usage: just execute the script."
        print(msg, file=sys.stderr)
        exit(1)
    display_stats(process(Path()))


def display_stats(stats: dict[str, int]):
    sample_size = sum(stats.values())
    print(f"\nProcessed {sample_size} lines. Results:")
    print("| Char | Occurrence |")
    print("|------|------------|")
    ascii_stats = {char: stats.get(char, 0) for char in printable[:96]}
    table = reversed(sorted(ascii_stats.items(), key=(lambda kv: -kv[1])))
    table = [(char.replace("\t", "TAB"), x) for char, x in table]
    for char, count in table:
        print(f"| {char:>3}  | {count:<10} |")


def process(path: Path) -> dict[str, int]:
    statistics = {}
    if path.is_dir():
        if ".git" in str(path):
            eprint(f"{path}: .git directory, SKIP")
            return statistics
        eprint(f"{path}/")
        for file in path.iterdir():
            file_stats = process(file)
            for char, count in file_stats.items():
                statistics[char] = statistics.get(char, 0) + count
        return statistics
    elif not path.is_file():
        eprint(f"{path}: unknown file, SKIP")
        return statistics
    elif path.suffix.strip(".") in "png bin pyc woff2 jpg".split():
        eprint(f"{path}: binary file, SKIP")
        return statistics
    try:
        text = path.read_bytes().decode(encoding="utf8", errors="strict")
        if "\0" in text:
            raise ValueError()
        eprint(f"{path}: processed")
        for line in (x for x in text.splitlines() if x == x[:1]):
            char = line[:1]
            statistics[char] = statistics.get(char, 0) + 1
    except (UnicodeDecodeError, ValueError):
        eprint(f"{path}: binary file, SKIP")
    return statistics


def eprint(message: str):
    print(message, file=sys.stderr)


if __name__ == "__main__":
    main(*sys.argv)
