from .base import Car

class HybridCar(Car):
    def __init__(self, make, model, year, battery_kwh):
        super().__init__(make, model, year)
        self.battery_kwh = battery_kwh

    def range_estimate(self) -> int:
        return self.battery_kwh * 3
        

