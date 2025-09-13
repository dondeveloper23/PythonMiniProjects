from .base import Car

class Truck(Car):
    def __init__(self, make, model, year, capacity_tons: float):
        super().__init__(make, model, year)
        self.capacity_tons = capacity_tons

    def spec(self) -> str:
        base = super().spec()
        return f"{base} | capacity: {self.capacity_tons}t"
    def age(self) -> int:
        base_age = super().age()
        return base_age
