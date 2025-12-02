def format_record(rec):

    fio, group, gpa = rec

    if not fio.strip() or not group.strip():
        print("ValueError")

    parts = fio.strip().split()
    parts = [p.capitalize() for p in parts]

    if len(parts) < 2:
        print("ValueError")

    surname = parts[0]
    initials = ""
    for p in parts[1:3]:
        initials += p[0].upper() + "."

    gpa = f"{float(gpa):.2f}"

    return f"{surname} {initials}, гр. {group.strip()}, GPA {gpa}"


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
