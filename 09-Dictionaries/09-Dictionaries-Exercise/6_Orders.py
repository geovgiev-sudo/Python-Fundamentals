command = input()
products = {}
while command != "buy":
    info = command.split()
    name, price, quantity = info[0], float(info[1]), int(info[2])
    if name not in products.keys():
        products[name] = {}
        products[name]["quantity"] = quantity
        products[name]["price"] = price

    else:
        products[name]["quantity"] += quantity
        products[name]["price"] = price

    command = input()

for product_name, quantity_price in products.items():
    count = 0
    cost = 0
    for key, value in quantity_price.items():
        if key == "quantity":
            count = value
        elif key == "price":
            cost = value
    total_price = count * cost
    print(f"{product_name} -> {total_price:.2f}")


# UPGRADED VERSION

products = {}

while True:
    command = input()
    if command == "buy":
        break

    # 1. Unpack and convert in one go
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    # 2. Simplified update logic
    if name not in products:
        # Store as [price, quantity]
        products[name] = [price, quantity] # правим си директно лист
    else:
        # Update quantity and replace price
        products[name][0] = price
        products[name][1] += quantity

# 3. Direct access in the final loop
for name, data in products.items():
    current_price = data[0] # достъпваме листа
    total_quantity = data[1] # достъпваме листа
    total_cost = current_price * total_quantity

    print(f"{name} -> {total_cost:.2f}")