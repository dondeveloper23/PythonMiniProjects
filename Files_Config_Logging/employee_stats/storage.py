import csv
from pathlib import Path
from dataclasses import asdict
from typing import List
from employee import Employee


PATH = Path(__file__).parent
PATH_FILE = PATH / "_data" / "employees.csv"


PATH_FILE.parent.mkdir(parents=True, exist_ok=True)


def save_to_csv(employees: List[Employee], path: Path = PATH_FILE) -> None:

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "department", "salary"])
        writer.writeheader()
        for emp in employees:
            writer.writerow(asdict(emp))


def load_from_csv(path: Path = PATH_FILE) -> List[Employee]:

    employees: List[Employee] = []
    if not path.exists():
        return employees

    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            emp = Employee(
                id=int(row["id"]),
                name=row["name"],
                department=row["department"],
                salary=float(row["salary"])
            )
            employees.append(emp)
    return employees
