import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
import pytest
from models import Employee
from storage import save_all, load_all
from stats import average_salary, highest_paid_employee, n_highest_paid, count_employees_per_department

employees = [
    Employee(id=1, name="John Doe", department="Dev", salary=1200.50),
    Employee(id=2, name="Ana Smith", department="HR", salary=950.00),
    Employee(id=3, name="Marko Markovic", department="Marketing", salary=1100.75),
    Employee(id=4, name="Elena Petrova", department="Dev", salary=1500.00),
    Employee(id=5, name="David Johnson", department="Sales", salary=1300.25),
]


def test_save_load(tmp_path):
    
    employees = [
        Employee(id=1, name="John", department="Dev", salary=1200.0),
        Employee(id=2, name="Ana", department="HR", salary=900.0),
    ]
     
    save_all(employees)
    load = load_all()

    assert load[0].department == "Dev"
    assert load[1].department == "HR"

def test_average_salary():
    avg = average_salary(employees)
    expected = (1200.50 + 950.00 + 1100.75 + 1500.00 + 1300.25) / 5
    assert round(avg, 2) == round(expected, 2)

def test_highest_paid_employee():
    highest = highest_paid_employee(employees)
    assert highest.salary == 1500.00

def test_n_highest_paid_employee():
    highest = n_highest_paid(employees, 3)
    assert highest[2].id == 1
    
def test_count_employees_per_department():
    departments = count_employees_per_department(employees)
    assert departments["Dev"] == 2
