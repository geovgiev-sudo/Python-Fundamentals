# integers = list(map(int, input().split("|")))
# total_items_collected = 0
#
# while True:
#     command = input()
#     if command == "Adventure over":
#         break
#
#     if "Step" in command:
#         command = command.split("$")
#         action = command[0]
#         start_index = int(command[1])
#         step = int(command[2])
#         index_to_remove = 0
#
#         if 0 <= start_index < len(integers):
#             if action == "Step Backward":
#                 index_to_remove = (start_index - step) % len(integers)
#             elif action == "Step Forward":
#                 index_to_remove = (start_index + step) % len(integers)
#             total_items_collected += integers[index_to_remove]
#             integers[index_to_remove] = 0
#
#     else:
#         command = command.split()
#         action = command[0]
#         if action == "Double":
#             index = int(command[1])
#             if 0 <= index < len(integers):
#                 integers[index] *= 2
#
#         elif action == "Switch":
#             integers.reverse()
#
#
# print(f"{' - '.join(map(str, integers))}")
# print(f"Robo finished the adventure with {total_items_collected} items!")






sequence_of_integers = list(map(int, input().split("|")))
position_index = 0
total_items_collected = 0

while True:
    command = input()
    if command == "Adventure over":
        break
    if command.startswith("Step"):
        parts = command.split("$")
        action = parts[0].split()
        index = int(parts[1])
        step = int(parts[2])

        if index < 0 or index >= len(sequence_of_integers):
            continue
        position_index = index
        if action[1] == "Backward":
            for robo in range(step):
                position_index -= 1
                if position_index < 0:
                    position_index = len(sequence_of_integers) - 1

        elif action[1] == "Forward":
            for robo in range(step):
                position_index += 1
                if position_index >= len(sequence_of_integers):
                    position_index = 0

        total_items_collected += sequence_of_integers[position_index]
        sequence_of_integers[position_index] = 0


    elif command.startswith("Double"):
        idx = int(command.split()[1])
        if 0 <= idx < len(sequence_of_integers):
            sequence_of_integers[idx] *= 2

    elif command == "Switch":
        sequence_of_integers = sequence_of_integers[::-1]

print(' - '.join(map(str, sequence_of_integers)))
print(f"Robo finished the adventure with {total_items_collected} items!")