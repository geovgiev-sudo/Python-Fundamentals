# Иван Шопов решение 2025
#
#
# def merge(some_list: list, current_command: list) -> list:
#     index1, index2 = int(current_command[1]), int(current_command[2])
#     if index1 not in range(len(some_list)): #start index is not valid
#         index1 = 0
#     if index2 not in range(len(some_list)):
#         index2 = len(some_list) - 1
#     some_list[index1] = "".join(some_list[index1: index2 + 1])
#     some_list = some_list[:index1 + 1] + some_list[index2 + 1:]
#     return some_list
#
#
# def divide(some_list: list, current_command: list) -> list:
#     index, partitions = int(current_command[1]), int(current_command[2])
#     element = some_list[index]
#     partition_size = len(element) // partitions
#     partitioned_elements = []
#     number_of_partition = 0
#     for current_index in range(0, len(element), partition_size):
#         number_of_partition += 1
#         if number_of_partition == partitions:
#             current_partition = element[current_index:]
#             partitioned_elements.append(current_partition)
#             break
#         else:
#             current_partition = element[current_index:current_index + partition_size]
#             partitioned_elements.append(current_partition)
#     some_list = some_list[:index] + partitioned_elements + some_list[index + 1:]
#     return some_list
#
#
#
# strings = input().split()
# command = input()
# while command != "3:1":
#     action = command.split()
#
#     if action[0] == "merge":
#         strings = merge(strings, action)
#
#     elif action[0] == "divide":
#         strings = divide(strings, action)
#
#     command = input()
#
# print(f"{' '.join(strings)}")


# Митко Втори решение 2022

# def merge(virus, command):
#
#     first_index = int(command[1])
#     second_index = int(command[-1])
#
#     if first_index < 0:
#         first_index = 0
#     if first_index < second_index:
#         length = len(virus)
#         if second_index >= length:
#             second_index = length - 1
#         for num in range(first_index, second_index):
#             virus[first_index] += f"{virus.pop(first_index + 1)}"
#
#
# def divide(virus):
#
#     first_index = int(command[1])
#     second_index = int(command[-1])
#
#     length = len(virus[first_index])
#     space_between = length // second_index
#     string_to_change = virus.pop(first_index)
#     result = []
#     for end in range(second_index - 1):
#         result.append(string_to_change[:space_between])
#         string_to_change = string_to_change[space_between:]
#     result.append(string_to_change)
#     for end in result[::-1]:
#         virus.insert(first_index, end)
#
#
# strings = input().split(' ')
# while True:
#     command = input().split(' ')
#
#     if command[0] == '3:1':
#         break
#
#     if command[0] == "merge":
#         merge(strings, command)
#
#     elif command[0] == 'divide':
#         divide(strings)
#
# print(' '.join(strings))



# Адаша от курса решение seaman2000

# def merge(sequence, start, end):
#     start = max(0, start)
#     end = min(len(sequence) - 1, end)
#
#     if start <= end:
#         merged = "".join(sequence[start:end + 1])
#         sequence[start:end + 1] = [merged] # Заменя предишните стойности на списъка с  вече merged.
#
#
# def divide(sequence, index, partitions):
#     element = sequence[index]
#
#     if partitions <= 1:
#         return
#
#     part_len = len(element) // partitions
#     parts_ = []
#     pos = 0
#
#     for _ in range(partitions - 1):
#         parts_.append(element[pos:pos + part_len])
#         pos += part_len
#
#     parts_.append(element[pos:])
#     sequence[index:index + 1] = parts_
#
#
# sequence_of_strings = input().split()
#
# while True:
#     command_line = input()
#
#     if command_line == "3:1":
#         break
#
#     parts = command_line.split()
#     command = parts[0]
#
#     if command == "merge":
#         start_idx = int(parts[1])
#         end_idx = int(parts[2])
#         merge(sequence_of_strings, start_idx, end_idx)
#
#     elif command == "divide":
#         index_ = int(parts[1])
#         partitions_ = int(parts[2])
#         divide(sequence_of_strings, index_, partitions_)
#
# print(" ".join(sequence_of_strings))