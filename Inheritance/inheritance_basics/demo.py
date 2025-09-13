from src.vehicles import Car, Truck, ElectricCar

def main() -> None:
    car = Car("VW", "Golf", 2012)
    truck = Truck("MAN", "TGS", 2018, 18.0)
    ev = ElectricCar("Tesla", "Model 3", 2023, 75)

    for v in (car, truck, ev):
        print(v.spec())

if __name__ == "__main__":
    main()