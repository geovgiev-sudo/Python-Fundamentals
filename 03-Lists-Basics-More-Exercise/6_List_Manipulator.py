initial_list = input().split()
integers_list = [int(num) for num in initial_list]

command_input = input()

while command_input != "end":
    action = command_input.split()
    command = action[0]

    # Pre-filter lists for easier access
    even_indices = [i for i, x in enumerate(integers_list) if x % 2 == 0]
    odd_indices = [i for i, x in enumerate(integers_list) if x % 2 != 0]

    if command == "exchange":
        index = int(action[1])
        # Validate index range
        if index < 0 or index >= len(integers_list):
            print("Invalid index")
        else:
            # Split and exchange [cite: 7, 8]
            integers_list = integers_list[index + 1:] + integers_list[:index + 1]

    elif command == "max":
        # Get the correct index list based on type [cite: 11]
        target_indices = even_indices if action[1] == "even" else odd_indices
        if not target_indices:
            print("No matches")
        else:
            # Find the max value among the filtered elements
            max_val = max([integers_list[i] for i in target_indices])
            # Find rightmost index of that max value
            rightmost_idx = [i for i in target_indices if integers_list[i] == max_val][-1]
            print(rightmost_idx)

    elif command == "min":
        # Get the correct index list based on type [cite: 13]
        target_indices = even_indices if action[1] == "even" else odd_indices
        if not target_indices:
            print("No matches")
        else:
            min_val = min([integers_list[i] for i in target_indices])
            # Find rightmost index of that min value
            rightmost_idx = [i for i in target_indices if integers_list[i] == min_val][-1]
            print(rightmost_idx)

    elif command == "first":
        count = int(action[1])
        if count > len(integers_list):
            print("Invalid count")
        else:
            target_elements = [integers_list[i] for i in (even_indices if action[2] == "even" else odd_indices)]
            # Return first 'count' elements [cite: 17, 18]
            print(target_elements[:count])

    elif command == "last":
        count = int(action[1])
        if count > len(integers_list):
            print("Invalid count")
        else:
            target_elements = [integers_list[i] for i in (even_indices if action[2] == "even" else odd_indices)]
            # Return last 'count' elements [cite: 19, 20]
            print(target_elements[-count:])

    command_input = input()

# Final output format [cite: 24, 33]
print(f"[{', '.join(map(str, integers_list))}]")