# src/lab04/io_txt_csv.py
from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    return Path(path).read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    p = Path(path)
    if p.parent and not p.parent.exists():
        p.parent.mkdir(parents=True, exist_ok=True)


def write_csv(
    rows: Iterable[Sequence],
    path: str | Path,
    header: tuple[str, ...] | None = None,
) -> None:
    p = Path(path)
    ensure_parent_dir(p)

    rows_list = list(rows)
    row_len: int | None = len(rows_list[0]) if rows_list else None

    if header is not None:
        if row_len is None:
            row_len = len(header)
        elif len(header) != row_len:
            raise ValueError(f"Header length {len(header)} != row length {row_len}")

    if row_len is not None:
        for i, r in enumerate(rows_list):
            if len(r) != row_len:
                raise ValueError(f"Row {i} length {len(r)} != expected {row_len}")

    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows_list:
            w.writerow(r)
