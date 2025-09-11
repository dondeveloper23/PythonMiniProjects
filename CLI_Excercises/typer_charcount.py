import typer

app = typer.Typer()

@app.command()
def char_count(word: str):
    print(len(word))

if __name__ == "__main__":
    app()