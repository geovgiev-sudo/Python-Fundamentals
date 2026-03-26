def add_stop(stops_as_string:str, some_index:int, some_sub_string:str) -> str:
    if some_index in range(len(stops_as_string)):
        left_part = stops_as_string[:some_index]
        right_part = stops_as_string[some_index:]
        stops_as_string = left_part + some_sub_string + right_part
    return  stops_as_string

def remove_stop(stops_as_string:str, some_start_index:int, some_end_index:int) -> str:
    if some_start_index in range(len(stops_as_string)) and \
        some_end_index in range(len(stops_as_string)):
        left_part = stops_as_string[:some_start_index]
        right_part = stops_as_string[some_end_index + 1:]
        stops_as_string = left_part + right_part
    return  stops_as_string

def switch(stops_as_string:str, some_old_string:str, some_new_string:str) -> str:
    if some_old_string in stops_as_string:
        stops_as_string = stops_as_string.replace(some_old_string, some_new_string)
    return  stops_as_string


stops = input()
command = input().split(":")
while command [0] != "Travel":
    action = command[0]
    if action == "Add Stop":
        index, sub_string = int(command[1]), command[2]
        stops = add_stop(stops, index, sub_string)
    elif action == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        stops = remove_stop(stops, start_index, end_index)
    elif action == "Switch":
        old_string, new_string = command[1], command[2]
        stops = switch(stops, old_string, new_string)
    print(stops)
    command = input().split(":")

print(f"Ready for world tour! Planned stops: {stops}")



# stops = input()
# command = input()
# while command != "Travel":
#     actions = command.split(":")
#     action = actions[0]
#
#     if action == "Add Stop":
#         index = int(actions[1])
#         string = actions[2]
#         if 0 <= index < len(stops):
#             stops = stops[:index] + string + stops[index:]
#             # stops_list = [char for char in stops]
#             # stops_list.insert(index, string)
#             # stops = "".join(stops_list)
#
#             print(stops)
#
#     elif action == "Remove Stop":
#         start_index = int(actions[1])
#         end_index = int(actions[2])
#         if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
#             left = stops[:start_index]
#             right = stops[end_index + 1:]
#             stops = left + right
#             # stops_to_remove = stops[start_index:end_index + 1]
#             # empty_string = ""
#             # stops = stops.replace(stops_to_remove, empty_string)
#         print(stops)
#
#     elif action == "Switch":
#         old_string = actions[1]
#         new_string = actions[2]
#         if old_string in stops:
#             stops = stops.replace(old_string, new_string)
#         print(stops)
#
#     command = input()
#
# print(f"Ready for world tour! Planned stops: {stops}")
