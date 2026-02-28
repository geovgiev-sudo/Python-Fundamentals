command = input()
line_count = 0
resource = ""
resources = {}
while command != "stop":
    quantity = 0
    line_count += 1
    if line_count % 2 == 0:
        quantity = int(command)
    elif line_count % 2 != 0:
        resource = command

    if resource not in resources.keys():
        resources[resource] = quantity
    resources[resource] += quantity

    command = input()

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")


# resources = {}
# current_resource = input()
# while current_resource != "stop":
#     current_quantity = int(input())
#     if current_resource not in resources.keys():
#         resources[current_resource] = 0
#     resources[current_resource] += current_quantity
#     current_resource = input()
# for resource, quantity in resources.items():
#     print(f"{resource} -> {quantity}")