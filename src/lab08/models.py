from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self) -> None:
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                "birthdate must be in format YYYY-MM-DD"
            )

        try:
            self.gpa = float(self.gpa)
        except (TypeError, ValueError):
            raise ValueError(f"gpa must be a number, got {self.gpa!r}")

        if not (0.0 <= self.gpa <= 5.0):
            raise ValueError("gpa must be between 0 and 5")

    def age(self) -> int:
        birth = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        years = today.year - birth.year

        if (today.month, today.day) < (birth.month, birth.day):
            years -= 1

        return years

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"],
        )

    def __str__(self) -> str:
        return f"{self.fio} ({self.group}), {self.birthdate}, GPA: {self.gpa:.2f}"
