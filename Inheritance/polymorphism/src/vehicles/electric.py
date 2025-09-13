from .base import Car

class ElectricCar(Car):
    def __init__(self, make: str, model: str, year: int, battery_kwh: int) -> None:
        super().__init__(make, model, year)
        self.battery_kwh = battery_kwh

    def spec(self) -> str:
        base = super().spec()
        return f"{base} | battery: {self.battery_kwh}kWh"

    def range_estimate(self) -> int:
        return self.battery_kwh * 5
