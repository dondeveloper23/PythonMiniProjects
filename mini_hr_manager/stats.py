from models import Employee
from collections import OrderedDict
import numpy as np

def count_employees(employees: list[Employee]):
    total = 0
    for e in employees:
        total += 1
    return total

def average_salary(employees: list[Employee]):
    count = 0
    total_salary = 0
    for e in employees:
        count += 1
        total_salary += float(e.salary)

    return total_salary / count

def salary_per_department(employees: list[Employee]) -> dict[str, float]:
    dep_sal = {}
    
    for e in employees:
        if e.department not in dep_sal.keys():
            dep_sal[e.department] = 0
        dep_sal[e.department] += float(e.salary)

    return dep_sal

def count_employees_per_department(employees: list[Employee]) -> dict[str, float]:
    dep_count = {}
    for e in employees:
        if e.department not in dep_count.keys():
            dep_count[e.department] = 0
        dep_count[e.department] += 1

    return dep_count

def max_salary_per_department(employees: list[Employee]) -> dict[str, float]:
    max_dep = {}
    for e in employees:
        if e.department not in max_dep.keys():
            max_dep[e.department] = e.salary
        
        if e.salary > max_dep[e.department]:
            max_dep[e.department] = e.salary


    return max_dep

def avg_salary_per_department(employees: list[Employee]) -> dict [str, float]:
    dep = {}
    for e in employees:
        if e.department not in dep.keys():
            dep[e.department] = [0, 0]
        dep[e.department][0] += 1
        dep[e.department][1] += float(e.salary)
    averages = {}
    for d, (count, total_salary) in dep.items():
        
        averages[d] = total_salary / count

        return averages


    
def highest_paid_employee(employees: list[Employee]) -> Employee:
    biggest = None
    for e in employees:
        if biggest is None or biggest.salary < e.salary:
            biggest = e

    return biggest

def n_highest_paid(employees: list[Employee], n) -> list[Employee]:
    sorted_list = sorted(employees, key=lambda e: e.salary, reverse=True)[:n]
    
    return sorted_list






