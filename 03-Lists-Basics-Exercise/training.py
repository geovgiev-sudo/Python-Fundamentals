#МОЕТО РЕШЕНИЕ

items = input().split("|")
budget = float(input())
ticket_price = 150
max_price = 0
sold_sum = 0
items_sold = []
profit = 0

for current_item in items:
    items_info = current_item.split("->")
    item_type = items_info[0]
    item_price = float(items_info[1])

    if item_type == "Clothes":
        max_price = 50
    elif item_type == "Shoes":
        max_price = 35
    elif item_type == "Accessories":
        max_price = 20.50

    if item_price <= max_price:
        if item_price <= budget:
            budget -= item_price
            sell_price = item_price * 1.40
            sold_sum += sell_price
            profit += item_price * 0.40
            items_sold.append(sell_price)
            print(f"{sell_price:.2f}", end= " ")

# for item in items_sold: Еквивалент на ред 26
    # print(f"{item:.2f}", end= " ")
print()
print(f"Profit: {profit:.2f}")
new_budget = sold_sum + budget
if new_budget >= ticket_price:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")
