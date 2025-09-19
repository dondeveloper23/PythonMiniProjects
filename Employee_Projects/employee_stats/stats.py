from employee import Employee

def average_salary(employees: list[Employee]) -> float:
    total = sum(emp.salary for emp in employees)
    return total / len(employees)

def top_n_employees(employees: list[Employee], n) -> list[Employee]:
    sorted_employees = sorted(employees, key=lambda e: e.salary, reverse=True)
    return sorted_employees[0:n]

def salary_per_department(employees: list[Employee]) -> dict[str, float]:
    totals: dict[str, list[float]] = {}
    for e in employees:
        if e.department not in totals:
            totals[e.department] = [0, 0]
        totals[e.department][0] += e.salary
        totals[e.department][1] += 1

    averages: dict[str, float] = {}
    for dept, (total, count) in totals.items():
        averages[dept] = total / count
    return averages

def count_employees_per_department(employees: list[Employee]) -> dict[str, int]:
    counts = {}
    for e in employees:
        if e.department not in counts:
            counts[e.department] = 1
        else:
            counts[e.department] += 1
    return counts 

def max_salary_department(employees: list[Employee]) -> dict[str, float]:
    salaries = {}
    for e in employees:
        if e.department not in salaries:
            salaries[e.department] = []
        salaries[e.department].append(e.salary)
    list_salaries = {}
    for dep, sal in salaries.items():     
        salary = max(sal)
        list_salaries[dep] = salary
    return list_salaries
    