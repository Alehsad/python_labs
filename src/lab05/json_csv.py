import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if json_file.suffix.lower() != ".json" or csv_file.suffix.lower() != ".csv":
        raise ValueError("Ожидаются файлы .json (вход) и .csv (выход)")

    try:
        with json_file.open(encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise
    except json.JSONDecodeError as e:
        raise ValueError("Пустой JSON или ошибка формата") from e

    if not isinstance(data, list) or not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура (нужен список словарей)")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON должен содержать только словари")

    fieldnames = list(data[0].keys())
    for row in data[1:]:
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)

    csv_file.parent.mkdir(parents=True, exist_ok=True)

    with csv_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for obj in data:
            row = {}
            for key in fieldnames:
                value = obj.get(key, "")
                if value is None:
                    value = ""
                row[key] = str(value)
            writer.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_file = Path(csv_path)
    json_file = Path(json_path)

    if csv_file.suffix.lower() != ".csv" or json_file.suffix.lower() != ".json":
        raise ValueError("Ожидаются файлы .csv (вход) и .json (выход)")

    try:
        with csv_file.open(encoding="utf-8") as f:
            reader = csv.DictReader(f)

            if not reader.fieldnames or all(not (h or "").strip() for h in reader.fieldnames):
                raise ValueError("CSV без заголовка или пустой")

            rows = []
            for row in reader:
                clean_row = {}
                for k, v in row.items():
                    clean_row[k] = "" if v is None else str(v)
                rows.append(clean_row)
    except FileNotFoundError:
        raise

    if not rows:
        raise ValueError("Пустой CSV")

    json_file.parent.mkdir(parents=True, exist_ok=True)

    with json_file.open("w", encoding="utf-8") as f:
        import json
        json.dump(rows, f, ensure_ascii=False, indent=2)
