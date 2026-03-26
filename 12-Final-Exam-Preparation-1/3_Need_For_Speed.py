n = int(input())
cars = {}

for _ in range(n):
    car, mileage, fuel = input().split('|')
    cars[car] = {'mileage': int(mileage), 'fuel': int(fuel)}

while (command := input()) != 'Stop':
    parts = command.split(' : ')
    action, car = parts[0], parts[1]

    match action:
        case 'Drive':
            distance, fuel_needed = int(parts[2]), int(parts[3])
            if cars[car]['fuel'] < fuel_needed:
                print('Not enough fuel to make that ride')
            else:
                cars[car]['mileage'] += distance
                cars[car]['fuel'] -= fuel_needed
                print(f'{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.')

            if cars[car]['mileage'] >= 100000:
                print(f'Time to sell the {car}!')
                cars.pop(car)

        case 'Refuel':
            fuel_amount = int(parts[2])
            current_fuel = cars[car]['fuel']
            added_fuel = min(75 - current_fuel, fuel_amount) # питай за това, че нещо не го схванах
            cars[car]['fuel'] += added_fuel
            print(f'{car} refueled with {added_fuel} liters')

        case 'Revert':
            kilometers = int(parts[2])
            if cars[car]['mileage'] - kilometers < 10000:
                cars[car]['mileage'] = 10000
            else:
                cars[car]['mileage'] -= kilometers
                print(f"{car} mileage decreased by {kilometers} kilometers")

for car, data in cars.items():
    print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")