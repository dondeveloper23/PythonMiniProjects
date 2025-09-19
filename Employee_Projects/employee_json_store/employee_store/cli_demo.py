import typer
from .store import load_all
from .store import add_employee
from .store import remove_employee
from .store import find_employee
from .models import Employee
from .store import update_employee
app = typer.Typer()

@app.command(name="list")
def list_employees():
    """LIST EMPLOYEES"""
    employees = load_all()
    if not employees:
        typer.echo("No employees found")
        return
    for e in employees:
        typer.echo(f"{e.id}: {e.name} - {e.department} - {e.salary}")

@app.command(name="add")
def add_employee_cli(id: int, name: str, department: str, salary: float):
    """ADD NEW EMPLOYEE"""
    employee = Employee(id=id, name=name, department=department, salary=salary)
    add_employee(employee)
    typer.echo("New employee added!")

@app.command(name="remove")
def remove_employee_cli(id: int, name: str, department: str, salary: float):
    employee = Employee(id=id, name=name, department=department, salary=salary)
    remove_employee(employee)
    typer.echo("Employee removed!")

@app.command(name="find")
def find_employee_cli(id: int, name: str, department: str, salary: float):
    employee = Employee(id=id, name=name, department=department, salary=salary)
    find_employee(employee)
    typer.echo(f"Employee found: {employee.name} - {employee.department}!")
@app.command(name="update")
def update_employee_cli(id: int, name: str, department: str, salary: float):
    employee = Employee(id=id, name=name, department=department, salary=salary)
    update_employee(employee)
    typer.echo(f"Employee updated: {employee.name} - {employee.department}!")


if __name__ == "__main__":
    app()