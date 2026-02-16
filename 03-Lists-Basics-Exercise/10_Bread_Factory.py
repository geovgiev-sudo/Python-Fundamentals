events = input().split("|")
energy = 100
coins = 100


for event in events:
    event_info = event.split("-")
    event_name = event_info[0]
    number = int(event_info[1])

    if event_name == "rest":
        old_energy = energy
        energy += number

        if energy > 100:
            energy = 100

        gained_energy = energy - old_energy

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event_name == "order":
        if energy >= 30:
            print(f"You earned {number} coins.")
            energy -= 30
            coins += number
        else:
            energy += 50
            if energy > 100:
                energy = 100
            print("You had to rest!")

    else:
        if coins >= number:
            print(f"You bought {event_name}.")
            coins -= number
        else:
            print(f"Closed! Cannot afford {event_name}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")