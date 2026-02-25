command = input()
products = {}
while command != "statistics":
    key, value = command.split(": ")
    value = int(value)
    if key in products:
        products[key] += value
    else:
        products[key] = value

    command = input()
key_count = len(products)
value_sum = sum(products.values())
print(f"Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {key_count}\n"
      f"Total Quantity: {value_sum}")



# command = input()
# products = {}
# while command != "statistics":
#     pair = command.split(": ")
#     key = pair[0]
#     value = int(pair[1])
#     if key in products:
#         products[key] += value
#     else:
#         products[key] = value
#
#     command = input()
# key_count = 0
# value_sum = 0
# print(f"Products in stock:")
# for key, value in products.items():
#     key_count += 1
#     value_sum += value
#     print(f"- {key}: {value}")
# print(f"Total Products: {key_count}\n"
#       f"Total Quantity: {value_sum}")