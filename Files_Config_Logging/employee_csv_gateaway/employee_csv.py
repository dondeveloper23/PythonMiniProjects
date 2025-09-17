import csv
from dataclasses import asdict
from pathlib import Path
from dataclasses import dataclass
PATH = Path(__file__).parent
PATH_FILE = PATH / "employees.csv"



@dataclass
class Employee:
    id: int
    name: str
    department: str
    salary: float


def save_to_csv(employees: list[Employee], path: str = PATH_FILE) -> None:
    with open(PATH_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "department", "salary"])
        writer.writeheader()
        writer.writerows(asdict(e) for e in employees)

def load_from_csv(path: str = PATH_FILE) -> list[Employee]:
    with open(PATH_FILE, "r", encoding="utf-8") as f:
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

if __name__ == "__main__":
    employees = [
        Employee(1, "Dule", "Dev", 3200.0),
        Employee(2, "Marko", "HR", 2800.5),
        Employee(3, "Ana", "Finance", 4100.75),
    ]

    save_to_csv(employees)

    loaded = load_from_csv()

    for emp in loaded:
        print(emp)