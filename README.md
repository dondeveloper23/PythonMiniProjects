# Python Mini Projects

This repository contains a collection of small Python projects for practice and learning. Each project is organized in its own folder with all necessary files and documentation.

## Projects

### CSVHandler
- A mini project demonstrating a CSV handler class with CRUD operations.
- Includes `pytest` tests for add, remove, update, save, and load operations.
- Folder: `CSVHandler`

### MovieLibrary_TypedHints
A mini project demonstrating the use of `TypedDict` and type hints in Python OOP.  
Includes classes `Movie` and `Library` with proper type annotations, and examples for using `mypy` to catch type errors.  
Folder: `MovieLibrary_TypedHints`

### CLI_Excerises
- A mini project demonstrating the creation of CLI applications using **Typer** and **sys.argv**.
- Includes examples for handling positional arguments, default values, and optional flags.
- Demonstrates simple command-line tools like:
  - `add` – adds two numbers and prints the result.
  - `char_count` – counts the number of characters in a word.
  - `hello` – simple greeting command (optional).
- Folder: `CLI_Excerises`

### Inheritance
- Practice with **object-oriented inheritance** in Python.  
- Implemented base class `Car` and child classes `Truck`, `ElectricCar`, and `HybridCar`.  
- Demonstrated:
  - use of `super()` to initialize parent attributes,
  - method overriding (`spec` method),
  - polymorphism with `getattr` to call optional methods like `range_estimate`.
- Folder: `inheritance`

### Encapsulation
- Practice with **encapsulation and properties** in Python.  
- Implemented class `BankAccount` with:
  - private attribute `__balance`,
  - `@property` getter and setter to control access and validate values,
  - `deposit` and `withdraw` methods with validation rules,
  - demo showing controlled balance changes and error handling with `try/except`.
- Folder: `Encapsulation`

### Banking_System
- A mini project simulating a simple banking system.  
- Implements:
  - `BankAccount` with balance, deposit, withdraw, overdraft limit, and transaction history,
  - `SavingsAccount` as a subclass with annual interest accrual (10% after one year).
- Demonstrates:
  - use of encapsulation with private attributes (`__balance`, `__overdraft_limit`),
  - inheritance and method overriding (`deposit`, `accrue_interest`),
  - logging and formatting of transactions with timestamps.
- Folder: `banking_system`

### Fleet Manager
- A CLI-based fleet management tool using **Typer** and **JSON** for storage.
- Implements:
  - `add` – add a new vehicle (with auto-incrementing ID),
  - `list` – display all stored vehicles,
  - `version` – show the app version.
- Data is persisted in `_data/fleet.json` and automatically created if missing.
- Demonstrates:
  - use of `pathlib.Path` for file handling,
  - JSON read/write (`load_all`, `save_all`),
  - command-line argument parsing with Typer.
- Folder: `fleet_manager`

### Employee CSV Gateway
- A project that demonstrates working with **CSV files** for employee storage.  
- Implements:
  - `employee_csv.py` with import/export functions using `csv.DictReader` and `csv.DictWriter`.  
  - Example dataset `employees.csv`.  
- Shows best practices for UTF-8 encoding and `newline=""`.  
- Folder: `employee_csv_gateway`

### Employee JSON Store
- A project for managing employees stored in **JSON format**.  
- Implements:
  - `employee_store` package with data schema and helper functions.  
  - Uses `dataclasses`, schema versioning, and logging.  
- Demonstrates safe JSON read/write and structured code organization.  
- Folder: `employee_json_store`

### Employee Stats
- A mini project for generating **statistics from employee data**.  
- Implements:
  - `employee.py` – Employee dataclass.  
  - `stats.py` – business logic for statistics (avg salary, max salary per department, counts).  
  - `storage.py` – JSON storage handling.  
  - `cli.py` – Typer CLI for stats commands.  
- Data is persisted in `_data/`.  
- Folder: `employee_stats`

### safe_io_atomic_write
- A project demonstrating **safe file write operations** with atomic replace.
- Implements helper functions to ensure data consistency when saving files:
  - write to a temporary file,
  - flush and sync to disk,
  - atomically replace the target file.
- Prevents corruption in case of crashes or interruptions.
- Folder: `safe_io_atomic_write`

### mini_hr_manager
- A complete **HR management CLI app** with JSON/CSV storage and statistics.
- Implements:
  - `add` – add a new employee,
  - `list` – show all employees,
  - `delete` – remove employee by ID,
  - `statistics` – show avg salary, highest paid, top N employees, and counts per department.
- Includes `pytest` tests for storage, business logic, and statistics functions.
- Demonstrates:
  - use of `dataclasses` for structured data,
  - JSON read/write and data validation,
  - Typer CLI for user interaction.
- Folder: `mini_hr_manager`