import json
from pathlib import Path
from atomic_io import atomic_write_json


config = json.loads(Path("config.json").read_text(encoding="utf-8"))
data_file = Path(config["data_file"])

employees = [
    {"id": 1, "name": "Ana"},
    {"id": 2, "name": "Marko"},
    {"id": 3, "name": "Ivana"},
    {"id": 4, "name": "Nikola"},
    {"id": 5, "name": "Mila"}
]

atomic_write_json(data_file, {"employees": employees})

print(json.loads(data_file.read_text(encoding="utf-8")))