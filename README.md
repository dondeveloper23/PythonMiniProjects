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
