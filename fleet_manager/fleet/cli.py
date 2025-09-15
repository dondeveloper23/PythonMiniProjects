import typer
from .storage import load_all, save_all

app = typer.Typer(no_args_is_help=True)

@app.command()
def version():
    """Show Fleet Manager version."""
    typer.echo("fleet-manager 0.1.0")

@app.command("list")
def list_cmd() -> None:
    """List Records."""
    records = load_all()
    for record in records:
        print(f"{record["id"]} | {record["model"]} | {record["year"]}\n")

@app.command()
def add(model: str, year: int) -> None:
    """Add Records."""
    records = load_all()
    next_id = (max((int(r.get("id", 0)) for r in records), default=0) + 1)
    new_record = {"id": next_id, "model": model, "year": int(year)}
    records.append(new_record)
    save_all(records)        


if __name__ == "__main__":
    app()