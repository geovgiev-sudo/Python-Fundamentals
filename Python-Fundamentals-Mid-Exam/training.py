integers = list(map(int, input().split("|")))
command = input()
total_items_collected = 0
while command != "Adventure over":
    if "Step" in command:
        command = command.split("$")
        action = command[0]
        start_index = int(command[1])
        steps = int(command[2])

        if 0 <= start_index < len(integers):
            if action == "Step Backward":
                landing_index = (start_index - steps) % len(integers)
            else:
                landing_index = (start_index + steps) % len(integers)

        total_items_collected += integers[landing_index]
        integers[landing_index] = 0

    else:
        command = command.split()
        action = command[0]

        if action == "Double":
            index = int(command[1])
            if 0 <= index < len(integers):
                integers[index] *= 2

        elif action == "Switch":
            integers.reverse()

    command = input()