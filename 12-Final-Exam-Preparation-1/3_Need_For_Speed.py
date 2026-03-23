number_of_cars = int(input())
cars = {}
for i in range(number_of_cars):
    cars_info = input().split("|")
    name = cars_info[0]
    mileage = int(cars_info[1])
    fuel = int(cars_info[2])
    cars[name] = [mileage, fuel]


command = input()
while command != "Stop":
    info = command.split(" : ")
    action = info[0]
    car = info[1]

    if action == "Drive":
        fuel_in_car = cars[car][1]
        distance = int(info[2])
        fuel_needed = int(info[3])

        if fuel_in_car < fuel_needed:
            print(f"Not enough fuel to make that ride")

        if fuel_in_car > fuel_needed:
            cars[car][0] += distance
            cars[car][1] -= fuel_needed
            print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
        mileage_in_car = cars[car][0]
        if mileage_in_car >= 100000:
            del cars[car]
            print(f"Time to sell the {car}!")

    elif action == "Refuel":
        max_fuel = 75
        car_fuel = cars[car][1]
        fuel_to_refill = int(info[2])
        refueled = car_fuel + fuel_to_refill
        fuel_refilled = fuel_to_refill
        if refueled > max_fuel:
            refueled = max_fuel
            fuel_refilled = refueled - car_fuel
        cars[car][1] = refueled
        print(f"{car} refueled with {fuel_refilled} liters")

    elif action == "Revert":
        kilometers = int(info[2])
        cars[car][0] -= kilometers
        if cars[car][0] < 10000:
            cars[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()


for car, info in cars.items():
    mileage_left = info[0]
    fuel_left = info[1]
    print(f"{car} -> Mileage: {mileage_left} kms, Fuel in the tank: {fuel_left} lt.")