import json
import logging
from pathlib import Path
from .models import Employee
from dataclasses import asdict

SCHEMA_VERSION = 1

def get_storage_path() -> Path:
    base = Path(__file__).parent
    data_dir = base / "_data"
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir / "employees.json"

def ensure_data_file():
     path = get_storage_path()
     data = {
        "schema_version": SCHEMA_VERSION,
        "employees": []
    }
     if not path.exists():
          path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
     return path

def save_all(employees: list[Employee]):
    path = ensure_data_file()
    data = {
        "schema_version": SCHEMA_VERSION,
        "employees": [asdict(emp) for emp in employees]
    }
    text = json.dumps(data, ensure_ascii=False, indent=2)
    path.write_text(text, encoding="utf-8")
    

def load_all() -> dict:
    path = ensure_data_file()
    text = path.read_text(encoding="utf-8")
    data = json.loads(text)    
    employees: list[Employee] = []
    for emp_dict in data["employees"]:
            emp = Employee(
                id=emp_dict["id"],
                name=emp_dict["name"],
                department=emp_dict["department"],
                salary=emp_dict["salary"]
            )
            employees.append(emp)
    return employees

def add_employee(emp: Employee):
    employees = load_all()
    for e in employees:
         if e.id == emp.id:
              logging.warning("Employer with this ID already exists! Try again!")
              return
    employees.append(emp)
    save_all(employees)
    logging.info(f"{emp.name} - {emp.department} is added!")

def remove_employee(emp: Employee):
     employees = load_all()
     new_list: list[Employee] = []
     for employee in employees:
        if employee.id != emp.id:
             new_list.append(employee)
            

     save_all(new_list)

def find_employee(emp: Employee):
     employees = load_all()
     for e in employees:
          if e.id == emp.id:
               return e
     return None

def update_employee(emp: Employee):
     employees = load_all()
     for i, e in enumerate(employees):
          if e.id == emp.id:
               employees[i] = emp
               save_all(employees)
               logging.info(f"Employee {emp.id} {emp.name} is updated now!")
               return
     logging.warning(f"Employee with this ID is not found!")



    
if __name__ == "__main__":
    from .models import Employee 
    e1 = Employee(1, "Dule", "Dev", 50000)
    e2 = Employee(2, "Marko", "QA", 45000)
    save_all([e1, e2])         
    data = load_all()          
    