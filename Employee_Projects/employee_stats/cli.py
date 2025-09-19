import typer
from employee import Employee
from storage import save_to_csv, load_from_csv
from stats import count_employees_per_department, max_salary_department


app = typer.Typer()


import typer
from storage import load_from_csv
from stats import count_employees_per_department, max_salary_department

app = typer.Typer()


@app.command()
def count():
    """EMPLOYEES PER DEPARTMENT"""
    employees = load_from_csv()
    if not employees:
        typer.echo("No employees in the selected deparment.")
        raise typer.Exit()

    counts = count_employees_per_department(employees)
    for dep, num in counts.items():
        typer.echo(f"{dep}: {num} employees")


@app.command()
def max():
    """BIGGEST SALARY IN THE DEPARTMENT"""
    employees = load_from_csv()
    if not employees:
        typer.echo("No employees there.")
        raise typer.Exit()

    max_sals = max_salary_department(employees)
    for dep, sal in max_sals.items():
        typer.echo(f"The biggest salary in {dep}: {sal}")


if __name__ == "__main__":
    app()
