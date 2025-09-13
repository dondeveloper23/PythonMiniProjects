from .base import Car

class ElectricCar(Car):
    def __init__(self, make: str, model: str, year: int, battery_kwh: int):
        super().__init__(make, model, year)
        self.battery_kwh = battery_kwh