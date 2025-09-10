import csv

class CSVHandler:
    def __init__(self):
        self.data = []

    def add_entry(self, entry: dict):        
        for row in self.data:
            if row["id"] == entry["id"]:
                raise ValueError(f"entry with id {entry['id']} already exists")
        self.data.append(entry)

    def save_csv(self, file_path):
        with open(file_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "name"])
            writer.writeheader()
            writer.writerows(self.data)
    
    def load_csv(self, file_path):
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            self.data = list(reader)

    def remove_entry(self, entry_id):
        for row in self.data:
            if entry_id == row["id"]:
                self.data.remove(row)
                return
        raise ValueError(f"Entry with {entry_id} not fount")
    def update_entry(self, row_id: str, new_name: str):
        for row in self.data:
            if row["id"] == row_id:
                row["name"] = new_name
                return
        raise ValueError(f"entry with id {row_id} not found")
    
handler = CSVHandler()
handler.add_entry({"id": "2", "name": "marko"})
handler.save_csv("test.csv")