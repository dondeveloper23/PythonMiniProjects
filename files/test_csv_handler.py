from csv_handler import CSVHandler
import pytest
def test_add_entry_single():
    handler = CSVHandler()
    handler.add_entry({"id": "1", "name": "dule"})
    assert handler.data == [{"id": "1", "name": "dule"}]

def test_duplicate_entry():
    handler = CSVHandler()
    handler.add_entry({"id": "1", "name": "dule"})
    with pytest.raises(ValueError) as e:
        handler.add_entry({"id": "1", "name": "dule"})

def test_save_load_csv(tmp_path):
    handler = CSVHandler()
    handler.add_entry({"id": "1", "name": "dule"})
    handler.add_entry({"id": "2", "name": "marko"})
    file = tmp_path / "test.csv"
    handler.save_csv(file)
    new_handler = CSVHandler()
    new_handler.load_csv(file)
    assert handler.data == new_handler.data
    

def test_remove_entry():
    handler = CSVHandler()
    handler.add_entry({"id": "1", "name": "dule"})
    handler.remove_entry("1")
    assert handler.data == []

def test_error_remove_entry():
    handler = CSVHandler()
    handler.add_entry({"id": "1", "name": "dule"})
    
    with pytest.raises(ValueError) as e:
        handler.remove_entry("333")

def test_update_entry():
    handler = CSVHandler()
    handler.add_entry({"id": "1", "name": "dule"})
    handler.update_entry("1", "Promenjeno")
    assert handler.data == [{"id": "1", "name": "Promenjeno"}]

def test_error_remove_entry_update():
    handler = CSVHandler()
    handler.add_entry({"id": "1", "name": "dule"})
    
    with pytest.raises(ValueError) as e:
        handler.update_entry("333", "Test")