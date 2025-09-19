import json
from pathlib import Path
from atomic_io import atomic_write_json

def test_atomic_write_json(tmp_path: Path):
    test_file = tmp_path / "test.json"
    data = {"employees": [{"id": 1, "name": "Ana"}]}
    atomic_write_json(test_file, data)
    saved = json.loads(test_file.read_text(encoding="utf-8"))
    assert saved == data