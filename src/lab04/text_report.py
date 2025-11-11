from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import normalize, tokenize, count_freq, top_n


def _sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def _report_single(in_path: Path, out_path: Path, encoding: str, top: int) -> None:
    text = read_text(in_path, encoding=encoding)
    tokens = tokenize(normalize(text))
    freqs = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freqs)}")
    print("Топ-5:")
    for w, c in top_n(freqs, n=top):
        print(f"{w}:{c}")

    rows: list[Sequence] = _sorted_word_counts(freqs)
    write_csv(rows, out_path, header=("word", "count"))


def _report_multi(in_paths: list[Path], out_path: Path, encoding: str, top: int) -> None:
    all_rows: list[tuple[str, str, int]] = []
    for p in in_paths:
        text = read_text(p, encoding=encoding)
        tokens = tokenize(normalize(text))
        freqs = count_freq(tokens)

        print(f"[{p}]")
        print(f"Всего слов: {len(tokens)}")
        print(f"Уникальных слов: {len(freqs)}")
        print("Топ-5:")
        for w, c in top_n(freqs, n=top):
            print(f"{w}:{c}")

        for w, c in _sorted_word_counts(freqs):
            all_rows.append((str(p), w, c))

    all_rows.sort(key=lambda r: (r[0], -r[2], r[1]))
    write_csv(all_rows, out_path, header=("file", "word", "count"))


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser()
    p.add_argument("inputs", nargs="+")
    p.add_argument("--out", default="data/lab04/report.csv")
    p.add_argument("--encoding", default="utf-8")
    p.add_argument("--top", type=int, default=5)
    return p


def main() -> int:
    args = build_parser().parse_args()
    in_paths = [Path(s) for s in args.inputs]
    out_path = Path(args.out)

    if len(in_paths) == 1:
        _report_single(in_paths[0], out_path, args.encoding, args.top)
    else:
        _report_multi(in_paths, out_path, args.encoding, args.top)

    print(f"\nГотово: CSV сохранён в {out_path}")
    return 0


main()

