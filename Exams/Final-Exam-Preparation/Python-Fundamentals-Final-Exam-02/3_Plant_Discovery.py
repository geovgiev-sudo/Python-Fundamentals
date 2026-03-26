n = int(input())
plants = {}
ratings = {}
for i in range(n):
    planti, rarity = input().split("<->")
    rarity = int(rarity)
    plants[planti] = rarity


while True:
    command = input().split(": ")
    action = command[0]
    if action == "Exhibition":
        break
    info = command[1].split(" - ")
    plant = info[0]


    if plant not in plants:
        print(f"error")
        continue

    elif action == "Rate":
        rating = int(info[1])
        if plant not in ratings:
            ratings[plant] = []
        ratings[plant].append(rating)

    elif action == "Update":
        new_rarity = int(info[1])
        plants[plant] = new_rarity

    elif action == "Reset":
        if plant in ratings:
            del ratings[plant]

print(f"Plants for the exhibition:")
for plant, rarity in plants.items():
    if plant not in ratings:
        average_rating = 0
    else:
        average_rating = sum(ratings[plant]) / len(ratings[plant])
    print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")