from pathlib import Path
import json
from dataclasses import asdict
from models import Employee


PATH = Path(__file__).parent
SCHEMA_VERSION = 1

def get_storage_path() -> Path:
    data_folder = PATH / "_data"
    data_folder.mkdir(parents=True, exist_ok=True)
    return data_folder / "employees.json"

def ensure_data_file() -> Path:
    path = get_storage_path()
    data = {
        "schema_version": SCHEMA_VERSION,
        "employees": []
    }
    if not path.exists():
       path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return path
    

def save_all(employees: list[object]) -> None:
    path = ensure_data_file()
    data = {
        "schema_version": SCHEMA_VERSION,
        "employees": [asdict(emp) for emp in employees]
    }
    text = json.dumps(data, ensure_ascii=False, indent=2)
    path.write_text(text, encoding="utf-8")

def load_all() -> list[Employee]:
    path = ensure_data_file()
    text = path.read_text(encoding="utf-8")
    data = json.loads(text)
    employees = []
    for emp_dict in data["employees"]:
        employee = Employee(
            id = int(emp_dict["id"]),
            salary = float(emp_dict["salary"]),
            department = emp_dict["department"],
            name=emp_dict["name"]
        )
        employees.append(employee)

    return employees