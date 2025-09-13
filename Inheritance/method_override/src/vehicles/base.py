from datetime import datetime

class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def spec(self) -> str:
        return f"{self.year} {self.make} {self.model}"

    def age(self) -> int:
        return datetime.now().year - self.year