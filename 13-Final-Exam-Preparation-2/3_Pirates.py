command = input()
cities = {}
while command != "Sail":
    info = command.split("||")
    city = info[0]
    population = int(info[1])
    gold = int(info[2])
    if city not in cities:
        cities[city] = [population, gold]
    else:
        cities[city][0] += population
        cities[city][1] += gold

    command = input()


while True:
    command2 = input()
    if command2 == "End":
        break
    events = command2.split("=>")
    action = events[0]
    town = events[1]

    if action == "Plunder":
        people = int(events[2])
        gold2 = int(events[3])
        cities[town][0] -= people
        cities[town][1] -= gold2
        print(f"{town} plundered! {gold2} gold stolen, {people} citizens killed.")
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")


    elif action == "Prosper":
        gold2 = int(events[2])
        if gold2 < 0:
            print(f"Gold added cannot be a negative number!")
            continue
        cities[town][1] += gold2
        print(f"{gold2} gold added to the city treasury. {town} now has {cities[town][1]} gold.")


if cities:
    print(f"Ahoy, Captain! There are {(len(cities))} wealthy settlements to go to:")
    for town_name, values in cities.items():
        print(f"{town_name} -> Population: {values[0]} citizens, Gold: {values[1]} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")