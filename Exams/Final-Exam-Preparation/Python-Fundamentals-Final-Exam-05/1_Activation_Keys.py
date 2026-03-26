key = input()

while True:
    command = input().split(">>>")
    action = command[0]
    if action == "Generate":
        break

    elif action == "Contains":
        substring = command[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print(f"Substring not found!")

    elif action == "Flip":
        case = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        part_to_change = key[start_index:end_index]
        if case == "Upper":
            part_upper = part_to_change.upper()
            key = key.replace(part_to_change, part_upper)
        elif case == "Lower":
            part_lower = part_to_change.lower()
            key = key.replace(part_to_change, part_lower)
        print(key)


    elif action == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        part_to_delete = key[start_index:end_index]
        key = key.replace(part_to_delete, "")
        print(key)

print(f"Your activation key is: {key}")