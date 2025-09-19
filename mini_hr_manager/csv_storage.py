import csv
from models import Employee
from pathlib import Path
from dataclasses import asdict, dataclass

PATH = Path(__file__).parent


def get_storage_path_csv() -> Path:
    path = PATH / "_data"
    path.mkdir(parents=True, exist_ok=True)
    return path / "employees.csv"

def save_all_csv(employees: list[Employee]) -> None:
    path = get_storage_path_csv()

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "department", "salary"])
        writer.writeheader()
        writer.writerows(asdict(e) for e in employees)

def load_all_csv() -> list[Employee]:
    path = get_storage_path_csv()

    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
        employees = []
        for row in data:
            emp = Employee(
                id=int(row["id"]),
                name=row["name"],
                department=row["department"],
                salary=float(row["salary"])
            )
            employees.append(emp)

    return employees