import argparse
from collections import Counter
from pathlib import Path
import re
import sys


def cat(path, numbered):
    try:
        with open(path, encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                if numbered:
                    print(f"{i}\t{line.rstrip()}")
                else:
                    sys.stdout.write(line)
    except FileNotFoundError:
        raise


def stats(path, top):
    try:
        text = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        raise
    words = re.findall(r"\w+", text.lower())
    for w, c in Counter(words).most_common(top):
        print(w, c)


def main():
    parser = argparse.ArgumentParser(description="CLI текстовые утилиты")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_cat = sub.add_parser("cat", help="вывести файл")
    p_cat.add_argument("--input", required=True)
    p_cat.add_argument("-n", action="store_true")

    p_stats = sub.add_parser("stats", help="частоты слов")
    p_stats.add_argument("--input", required=True)
    p_stats.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    try:
        if args.cmd == "cat":
            cat(args.input, args.n)
        else:
            if args.top <= 0:
                parser.error("--top должно быть > 0")
            stats(args.input, args.top)
    except FileNotFoundError:
        parser.error("файл не найден")
    except BrokenPipeError:
        pass


main()
