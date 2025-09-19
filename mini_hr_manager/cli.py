import typer
from storage import load_all, save_all
from models import Employee
app = typer.Typer()
from stats import average_salary, highest_paid_employee, n_highest_paid, count_employees_per_department

@app.command()
def list():
    """SHOW EMPLOYEES"""
    employees = load_all()
    for e in employees:
        typer.echo(f"{e.id} | {e.name} | {e.department} | {e.salary}")

@app.command()
def add(id: int, name: str, department: str, salary: float):
    """ADD NEW EMPLOYEE"""
    employees = load_all()
    new_emp = Employee(id=id, name=name, department=department, salary=salary)
    employees.append(new_emp)
    save_all(employees)
    typer.echo(f"Employee {name} added successfully")

@app.command()
def delete(id: int):
    """DELETE EMPLOYEE"""
    employees = load_all()
    for e in employees:
        if e.id == id:
            employees.remove(e)
            save_all(employees)
            typer.echo("Employee removed")
            return
    typer.echo(f"No employee found")
        

@app.command()
def statistics():
    """SHOW STATS OF ALL EMPLOYEES"""
    employees = load_all()

    average = average_salary(employees)
    top = highest_paid_employee(employees)
    counts = count_employees_per_department(employees)
    top5 = n_highest_paid(employees, 5)

    typer.echo(f"Average salary is {average:.2f}")
    typer.echo(f"{top.name} salary is {top.salary} and he is the highest paid employee")
    for dep, num in counts.items():
        typer.echo(f"{dep} has {num} employees")
    count = 1
    for emp in top5:
        typer.echo(f"{count} {emp.name} | {emp.salary}")
        count += 1



if __name__ == "__main__":
    app()
