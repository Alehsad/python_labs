import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Прочитать файл целиком и вернуть содержимое как строку."""
    return Path(path).read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительскую папку для path, если её ещё нет."""
    pathObj = Path(path)
    parent = pathObj.parent
    if parent and not parent.exists():
        parent.mkdir(parents=True, exist_ok=True)


def write_csv(
    rows: Iterable[Sequence],
    path: str | Path,
    header: tuple[str, ...] | None = None,
) -> None:
    """Записать строки в CSV-файл с разделителем запятая."""
    pathObj = Path(path)
    ensure_parent_dir(pathObj)

    rowList = list(rows)
    rowLen: int | None = len(rowList[0]) if rowList else None

    if header is not None:
        if rowLen is None:
            rowLen = len(header)
        elif len(header) != rowLen:
            raise ValueError(f"Header length {len(header)} != row length {rowLen}")

    if rowLen is not None:
        for index, row in enumerate(rowList):
            if len(row) != rowLen:
                raise ValueError(f"Row {index} length {len(row)} != expected {rowLen}")

    with pathObj.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if header is not None:
            writer.writerow(header)
        for row in rowList:
            writer.writerow(row)
