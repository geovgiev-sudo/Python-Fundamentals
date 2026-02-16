loot = input().split("|")
command = input()

while command != "Yohoho!":
    command = command.split()
    action = command[0]
    if action == "Loot":
        items = command[1:]
        for item in items:
            if item not in loot:
                loot.insert(0, item)

    elif action == "Drop":
        i = int(command[1])
        if 0 <= i < len(loot):
            to_add = loot.pop(i)
            loot.append(to_add)


    elif action == "Steal":
        count = int(command[1])
        if len(loot) < count:
            count = len(loot)
        removed = []
        for item in range(- 1, -count - 1, - 1):
            to_remove = loot.pop(-1)
            removed.append(to_remove)

        print(f"{', '.join(list(reversed(removed)))}")


    command = input()

if len(loot) <= 0:
    print("Failed treasure hunt.")
else:
    length_sum = 0
    item_count = len(loot)
    for item in loot:
        length_sum += len(item)
    average_gain = length_sum / item_count
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")