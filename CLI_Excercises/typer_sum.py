import typer

app = typer.Typer()  

@app.command()
def add(x: int, y: int):
    total = x + y
    print(total)

if __name__ == "__main__":
    app()  