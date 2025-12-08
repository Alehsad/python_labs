from src.lab08.models import Student
from src.lab09.group import Group


def main() -> None:
    group = Group("data/lab09/students.csv")

    print("=== Исходный список студентов ===")
    for s in group.list():
        print(" ", s)

    print("\n=== Добавление нового студента ===")
    new_student = Student("Сидоров Сидор Сидорович", "2005-01-20", "SE-03", 4.0)
    group.add(new_student)
    for s in group.list():
        print(" ", s)

    print("\n=== Поиск по подстроке 'Иван' ===")
    for s in group.find("Иван"):
        print(" ", s)

    print("\n=== Обновление GPA студента 'Сидоров Сидор Сидорович' ===")
    group.update("Сидоров Сидор Сидорович", gpa=4.7)
    for s in group.list():
        print(" ", s)

    print("\n=== Удаление студента 'Сидоров Сидор Сидорович' ===")
    removed = group.remove("Сидоров Сидор Сидорович")
    print("Удалено записей:", removed)
    for s in group.list():
        print(" ", s)


if __name__ == "__main__":
    main()
