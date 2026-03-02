command = input()
products = {}
while command != "buy":
    info = command.split()
    name = info[0]
    price = float(info[1])
    quantity = int(info[2])
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