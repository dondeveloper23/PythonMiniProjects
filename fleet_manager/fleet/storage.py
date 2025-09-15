from pathlib import Path
import json


def get_storage_path() -> Path:
    data_dir = Path("./_data")
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir / "fleet.json"


def ensure_data_file() -> Path:
    path = get_storage_path()
    if not path.exists():
        path.write_text("[]", encoding="utf-8")
    return path
def load_all() -> list[dict]:
    path = ensure_data_file()
    try: 
        raw = path.read_text(encoding="utf-8")
        return json.loads(raw) if raw.strip() else []
    except json.JSONDecodeError:
        return []
    
def save_all(records: list[dict]) -> None:
    path = ensure_data_file()
    text = json.dumps(records, ensure_ascii=False, indent=2)
    path.write_text(text, encoding="utf-8")

def main():
    save_all([{"id": 1, "model": "Ford Focus", "year": 2020}])

if __name__ == "__main__":
    main()