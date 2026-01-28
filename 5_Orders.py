def order_calculator(order_type, quantity):
    price = 0

    if order_type == "coffee":
        price = 1.50
    elif order_type == "water":
        price = 1
    elif order_type == "coke":
        price = 1.40
    elif order_type == "snacks":
        price = 2

    return price * quantity

type_order = input()
order_quantity = int(input())
total_price = order_calculator(type_order, order_quantity)
print(f"{total_price:.2f}")

