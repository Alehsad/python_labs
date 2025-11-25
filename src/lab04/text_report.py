import sys
import argparse
from pathlib import Path
from typing import Sequence

scriptFile = Path(__file__).resolve()
srcDir = scriptFile.parents[1]
if str(srcDir) not in sys.path:
    sys.path.insert(0, str(srcDir))

from lab04.io_txt_csv import read_text, write_csv
from lib.text import normalize, tokenize, count_freq, top_n


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda pair: (-pair[1], pair[0]))


def report_single(in_path: Path, out_path: Path, encoding: str, top_size: int) -> None:
    text = read_text(in_path, encoding=encoding)
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, amount in top_n(freq, n=top_size):
        print(f"{word}:{amount}")

    rows: list[Sequence] = sorted_word_counts(freq)
    write_csv(rows, out_path, header=("word", "count"))


def report_multi(path_list: list[Path], out_path: Path, encoding: str, top_size: int) -> None:
    all_rows: list[tuple[str, str, int]] = []

    for path in path_list:
        text = read_text(path, encoding=encoding)
        tokens = tokenize(normalize(text))
        freq = count_freq(tokens)

        print(f"[{path}]")
        print(f"Всего слов: {len(tokens)}")
        print(f"Уникальных слов: {len(freq)}")
        print("Топ-5:")
        for word, amount in top_n(freq, n=top_size):
            print(f"{word}:{amount}")

        for word, amount in sorted_word_counts(freq):
            all_rows.append((str(path), word, amount))

    all_rows.sort(key=lambda item: (item[0], -item[2], item[1]))
    write_csv(all_rows, out_path, header=("file", "word", "count"))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", nargs="+")
    parser.add_argument("--out", default="data/lab04/report.csv")
    parser.add_argument("--encoding", default="utf-8")
    parser.add_argument("--top", type=int, default=5)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    path_list = [Path(text_path) for text_path in args.inputs]
    out_path = Path(args.out)

    if len(path_list) == 1:
        report_single(path_list[0], out_path, args.encoding, args.top)
    else:
        report_multi(path_list, out_path, args.encoding, args.top)

    print(f"\nГотово: CSV сохранён в {out_path}")
    return 0


main()
