from src.vehicles import Car, Truck, ElectricCar, HybridCar

def main() -> None:
    fleet = [
        Car("VW", "Golf", 2012),
        Truck("MAN", "TGS", 2018, 18.0),
        ElectricCar("Tesla", "Model 3", 2023, 75),
        HybridCar("Toyota", "Prius", 2020, 10),
    ]

    for v in fleet:
        print(v.spec(), "| age:", v.age())
        rng = getattr(v, "range_estimate", None)
        if callable(rng):
            print(" range_estimate:", rng(), "km")

if __name__ == "__main__":
    main()