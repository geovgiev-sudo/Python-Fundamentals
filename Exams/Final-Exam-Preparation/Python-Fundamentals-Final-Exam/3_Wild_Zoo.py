animals = {}

while True:
    command = input().split(": ")
    if command[0] == "EndDay":
        break

    action = command[0]
    info = command[1].split("-")
    animal_name = info[0]

    if action == "Add":
        food_needed = int(info[1])
        area = info[2]
        if animal_name not in animals.keys():
            animals[animal_name] = {"food_needed": 0, "area": area}
        animals[animal_name]["food_needed"] += food_needed

    elif action == "Feed":
        food_eaten = int(info[1])
        if animal_name in animals.keys():
            animals[animal_name]["food_needed"] -= food_eaten
            if animals[animal_name]["food_needed"] <= 0:
                print(f"{animal_name} was successfully fed")
                animals.pop(animal_name)

print(f"Animals:")
for animal, values in animals.items():
    needed_food = values["food_needed"]
    print(f" {animal} -> {needed_food}g")

areas = {}

for animal, values in animals.items():
    hungry_area = values["area"]
    if hungry_area not in areas.keys():
        areas[hungry_area] = 0
    areas[hungry_area] += 1

print("Areas with hungry animals:")
for area, quantity in areas.items():
    print(f" {area}: {quantity}")