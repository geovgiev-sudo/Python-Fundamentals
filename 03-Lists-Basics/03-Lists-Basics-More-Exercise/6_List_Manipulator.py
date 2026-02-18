integers = list(map(int, input().split()))
command = input()

while command != "end":
    command = command.split()
    action = command[0]

    if action == "exchange":
        index = int(command[1])
        if 0 <= index < len(integers):
            integers = integers[index + 1:] + integers[:index + 1]
        else:
            print("Invalid index")

    elif action == "max" or action == "min":
        odd_even = command[1]
        indices = []
        if odd_even == "even":
            indices = [i for i in range(len(integers)) if integers[i] % 2 == 0]
        elif odd_even == "odd":
            indices = [i for i in range(len(integers)) if integers[i] % 2 != 0]

        if not indices:
            print("No matches")
        else:
            min_max = 0
            if action == "max":
                min_max = max([integers[i] for i in indices])
            elif action == "min":
                min_max = min([integers[i] for i in indices])
            rightmost_index = [i for i in indices if integers[i] == min_max][-1]
            print(rightmost_index)

    elif action == "first" or action == "last":
        count = int(command[1])
        odd_even = command[2]
        filtered = []
        if 0 < count <= len(integers):
            if odd_even == "even":
                filtered = [x for x in integers if x % 2 == 0]
            elif odd_even == "odd":
                filtered = [x for x in integers if x % 2 != 0]
            if action == "first":
                print(filtered[:count])
            elif action == "last":
                print(filtered[-count:])
        else:
            print("Invalid count")
    command = input()

print(integers)





# integers = list(map(int, input().split()))
# command = input()
#
# while command != "end":
#     command = command.split()
#     action = command[0]
#
#     even_numbers = [even for even in integers if even % 2 == 0]
#     odd_numbers = [odd for odd in integers if odd % 2 != 0]
#
#     if action == "exchange":
#         index = int(command[1])
#         if 0 <= index < len(integers):
#             integers = integers[index + 1:] + integers[:index + 1]
#         else:
#             print("Invalid index")
#
#     elif action == "max":
#         odd_even = command[1]
#         if odd_even == "even" and even_numbers:
#             print((len(integers) - integers[::-1].index(max(even_numbers)) - 1))
#         elif odd_even == "odd" and odd_numbers:
#             print((len(integers) - integers[::-1].index(max(odd_numbers)) - 1))
#         else:
#             print("No matches")
#
#     elif action == "min":
#         odd_even = command[1]
#         if odd_even == "even" and even_numbers:
#             print((len(integers) - integers[::-1].index(min(even_numbers)) - 1))
#         elif odd_even == "odd" and odd_numbers:
#             print((len(integers) - integers[::-1].index(min(odd_numbers)) - 1))
#         else:
#             print("No matches")
#
#     elif action == "first":
#         count = int(command[1])
#         odd_even = command[2]
#         if 0 < count <= len(integers):
#             if odd_even == "even":
#                 print(even_numbers[0:count])
#             elif odd_even == "odd":
#                 print(odd_numbers[0:count])
#         else:
#             print("Invalid count")
#
#     elif action == "last":
#         count = int(command[1])
#         odd_even = command[2]
#         if 0 < count <= len(integers):
#             if odd_even == "even":
#                 print(even_numbers[-count:])
#             elif odd_even == "odd":
#                 print(odd_numbers[-count:])
#         else:
#             print("Invalid count")
#
#     command = input()
#
# print(integers)
#





# # Initial list setup [cite: 27]
# numbers = [int(x) for x in input().split()]
#
# while True:
#     line = input()
#     if line == "end":
#         break  # Stop taking input [cite: 24]
#
#     parts = line.split()
#     command = parts[0]
#
#     if command == "exchange":
#         index = int(parts[1])
#         # Check if index is within list boundaries [cite: 9] and not negative [cite: 10]
#         if 0 <= index < len(numbers):
#             # Split and exchange sub-lists [cite: 7]
#             numbers = numbers[index + 1:] + numbers[:index + 1]
#         else:
#             print("Invalid index")
#
#     elif command in ["max", "min"]:
#         num_type = parts[1]
#         # Get indices of all even/odd numbers [cite: 11, 13]
#         if num_type == "even":
#             filtered_indices = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
#         else:
#             filtered_indices = [i for i in range(len(numbers)) if numbers[i] % 2 != 0]
#
#         if not filtered_indices:
#             print("No matches")  # [cite: 16]
#         else:
#             # Find the target value (max or min)
#             target_value = max([numbers[i] for i in filtered_indices]) if command == "max" else min(
#                 [numbers[i] for i in filtered_indices])
#
#             # Find all indices where that value exists and pick the rightmost one
#             rightmost_index = [i for i in filtered_indices if numbers[i] == target_value][-1]
#             print(rightmost_index)
#
#     elif command in ["first", "last"]:
#         count = int(parts[1])
#         num_type = parts[2]
#
#         if count > len(numbers):  # Check if count is greater than list length
#             print("Invalid count")
#         else:
#             # Get even/odd elements [cite: 17, 19]
#             if num_type == "even":
#                 elements = [x for x in numbers if x % 2 == 0]
#             else:
#                 elements = [x for x in numbers if x % 2 != 0]
#
#             # Output the required number of elements [cite: 22, 23]
#             if command == "first":
#                 print(elements[:count])
#             else:
#                 print(elements[-count:])
#
# # Final state of the list in square brackets with comma-space separation [cite: 24, 33]
# print(numbers)


# МИТКО ВТОРИ


#numbers = [int(integer) for integer in input().split()]
# command = input().split()
#
# while command[0] != "end":
#     even_numbers = [even for even in numbers if even % 2 == 0]
#     odd_numbers = [odd for odd in numbers if odd % 2 != 0]
#
#     if command[0] == "exchange":
#         if 0 <= int(command[1]) < len(numbers):
#             numbers = numbers[int(command[1]) + 1:] + numbers[:int(command[1]) + 1]
#         else:
#             print(f'Invalid index')
#
#     elif command[0] == "max":
#         if command[1] == "even" and even_numbers:
#             print((len(numbers) - numbers[::-1].index(max(even_numbers)) - 1))
#         elif command[1] == "odd" and odd_numbers:
#             print((len(numbers) - numbers[::-1].index(max(odd_numbers)) - 1))
#         else:
#             print('No matches')
#
#     elif command[0] == "min":
#         if command[1] == "even" and even_numbers:
#             print((len(numbers) - numbers[::-1].index(min(even_numbers)) - 1))
#         elif command[1] == "odd" and odd_numbers:
#             print((len(numbers) - numbers[::-1].index(min(odd_numbers)) - 1))
#         else:
#             print('No matches')
#
#     elif command[0] == "first":
#         if 0 < int(command[1]) <= len(numbers):
#             if command[2] == "even":
#                 print(even_numbers[0:int(command[1])])
#             else:
#                 print(odd_numbers[0:int(command[1])])
#         else:
#             print(f"Invalid count")
#
#     elif command[0] == "last":
#         if 0 < int(command[1]) <= len(numbers):
#             if command[2] == "even":
#                 print(even_numbers[-int(command[1]):])
#             else:
#                 print(odd_numbers[-int(command[1]):])
#         else:
#             print(f"Invalid count")
#     command = input().split()
#
# print(numbers)
#
#
#
#
# initial_list = input().split()
# integers_list = [int(num) for num in initial_list]
#
# command_input = input()
#
# while command_input != "end":
#     action = command_input.split()
#     command = action[0]
#
#     # Pre-filter lists for easier access
#     even_indices = [i for i, x in enumerate(integers_list) if x % 2 == 0]
#     odd_indices = [i for i, x in enumerate(integers_list) if x % 2 != 0]
#
#     if command == "exchange":
#         index = int(action[1])
#         # Validate index range
#         if index < 0 or index >= len(integers_list):
#             print("Invalid index")
#         else:
#             # Split and exchange [cite: 7, 8]
#             integers_list = integers_list[index + 1:] + integers_list[:index + 1]
#
#     elif command == "max":
#         # Get the correct index list based on type [cite: 11]
#         target_indices = even_indices if action[1] == "even" else odd_indices
#         if not target_indices:
#             print("No matches")
#         else:
#             # Find the max value among the filtered elements
#             max_val = max([integers_list[i] for i in target_indices])
#             # Find rightmost index of that max value
#             rightmost_idx = [i for i in target_indices if integers_list[i] == max_val][-1]
#             print(rightmost_idx)
#
#     elif command == "min":
#         # Get the correct index list based on type [cite: 13]
#         target_indices = even_indices if action[1] == "even" else odd_indices
#         if not target_indices:
#             print("No matches")
#         else:
#             min_val = min([integers_list[i] for i in target_indices])
#             # Find rightmost index of that min value
#             rightmost_idx = [i for i in target_indices if integers_list[i] == min_val][-1]
#             print(rightmost_idx)
#
#     elif command == "first":
#         count = int(action[1])
#         if count > len(integers_list):
#             print("Invalid count")
#         else:
#             target_elements = [integers_list[i] for i in (even_indices if action[2] == "even" else odd_indices)]
#             # Return first 'count' elements [cite: 17, 18]
#             print(target_elements[:count])
#
#     elif command == "last":
#         count = int(action[1])
#         if count > len(integers_list):
#             print("Invalid count")
#         else:
#             target_elements = [integers_list[i] for i in (even_indices if action[2] == "even" else odd_indices)]
#             # Return last 'count' elements [cite: 19, 20]
#             print(target_elements[-count:])
#
#     command_input = input()
#
# # Final output format [cite: 24, 33]
# print(f"[{', '.join(map(str, integers_list))}]")