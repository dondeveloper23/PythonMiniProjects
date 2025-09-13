from src.vehicles import Car, Truck, ElectricCar

def main() -> None:
    car = Car("VW", "Golf", 2012)
    truck = Truck("MAN", "TGS", 2018, 18.0)
    ev = ElectricCar("Tesla", "Model 3", 2023, 75)

    print(truck.spec())         
    print(ev.spec())            
    print(f"Truck age: {truck.age()}")   
    print(f"EV range ~ {ev.range_estimate()} km")

if __name__ == "__main__":
    main()
