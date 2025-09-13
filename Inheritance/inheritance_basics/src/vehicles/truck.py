from .base import Car

class Truck(Car):
    def __init__(self, make: str, model: str, year: int, capacity_tons: float):
        super().__init__(make, model, year)
        self.capacity_tons = capacity_tons