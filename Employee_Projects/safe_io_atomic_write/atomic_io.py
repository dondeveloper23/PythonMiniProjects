import os
import json
from pathlib import Path

def atomic_write(path: Path, data: str) -> None:
    tmp_path = path.with_suffix(".tmp")

    with open(tmp_path, "w") as f:
        f.write(data)

    os.replace(tmp_path, path)


def atomic_write_json(path: Path, obj: dict) -> None:
    text = json.dumps(obj, ensure_ascii=False, indent=2)
    atomic_write(path, text)
