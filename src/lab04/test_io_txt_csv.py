from pathlib import Path
from src.lab04.io_txt_csv import read_text, write_csv

def main() -> int:
    t = read_text("data/lab04/input.txt")
    print("[T1] len:", len(t))
    print("[T1] first:", t.splitlines()[0] if t else "(empty)")

    rows = [("привет", 2), ("мир", 1)]
    write_csv(rows, "data/lab04/report.csv", header=("word", "count"))
    print("[T2] report exists?", Path("data/lab04/report.csv").exists())
    print(Path("data/lab04/report.csv").read_text(encoding="utf-8").strip())

    write_csv([], "data/lab04/empty.csv", header=None)
    print("[T3] empty size:", Path("data/lab04/empty.csv").stat().st_size)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
