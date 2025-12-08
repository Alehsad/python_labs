import csv
from pathlib import Path
from typing import List

from src.lab08.models import Student

_FIELDNAMES = ["fio", "birthdate", "group", "gpa"]

class Group:
    def __init__(self, storage_path: str) -> None:
        self.path = Path(storage_path)
        self._ensure_storage_exists()


    def _ensure_storage_exists(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            with self.path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(_FIELDNAMES)

    def _read_all(self) -> list[dict]:
        self._ensure_storage_exists()

        with self.path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)

            if reader.fieldnames != _FIELDNAMES:
                raise ValueError(
                    "Некорректный заголовок CSV. "
                    f"Ожидается: {','.join(_FIELDNAMES)}, "
                    f"получено: {reader.fieldnames}"
                )

            rows = list(reader)

        for row in rows:
            Student.from_dict(row)

        return rows

    def _write_all(self, rows: list[dict]) -> None:
        """Перезаписать CSV-файл переданными строками."""
        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=_FIELDNAMES)
            writer.writeheader()
            writer.writerows(rows)

    def list(self) -> List[Student]:
        rows = self._read_all()
        return [Student.from_dict(row) for row in rows]

    def add(self, student: Student) -> None:
        rows = self._read_all()
        rows.append(student.to_dict())
        self._write_all(rows)

    def find(self, substr: str) -> List[Student]:
        substr_lower = substr.lower()
        return [
            s for s in self.list()
            if substr_lower in s.fio.lower()
        ]

    def remove(self, fio: str) -> int:
        rows = self._read_all()
        new_rows = [r for r in rows if r["fio"] != fio]
        removed_count = len(rows) - len(new_rows)
        self._write_all(new_rows)
        return removed_count

    def update(self, fio: str, **fields) -> bool:
        rows = self._read_all()
        updated = False

        for row in rows:
            if row["fio"] == fio:
                for key, value in fields.items():
                    if key not in _FIELDNAMES:
                        raise KeyError(f"Неизвестное поле для обновления: {key}")
                    row[key] = value

                Student.from_dict(row)

                updated = True
                break

        if updated:
            self._write_all(rows)

        return updated
