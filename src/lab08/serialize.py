import json

from .models import Student


def students_to_json(students, path):
    data = [s.to_dict() for s in students]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path) -> list[Student]:
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    if not isinstance(raw, list):
        raise ValueError("JSON must contain a list of students")

    students: list[Student] = []
    for item in raw:
        if not isinstance(item, dict):
            raise ValueError("Each item in JSON list must be an object")
        students.append(Student.from_dict(item))

    return students
