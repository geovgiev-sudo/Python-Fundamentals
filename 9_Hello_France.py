# МОЕТО РЕШЕНИЕ
#
# items = input().split("|")
# budget = float(input())
# ticket_price = 150
# max_price = 0
# sold_sum = 0
# items_sold = []
# profit = 0
#
# for current_item in items:
#     items_info = current_item.split("->")
#     item_type = items_info[0]
#     item_price = float(items_info[1])
#
#     if item_type == "Clothes":
#         max_price = 50
#     elif item_type == "Shoes":
#         max_price = 35
#     elif item_type == "Accessories":
#         max_price = 20.50
#
#     if item_price <= max_price:
#         if item_price <= budget:
#             budget -= item_price
#             sell_price = item_price * 1.40
#             sold_sum += sell_price
#             profit += item_price * 0.40
#             items_sold.append(sell_price)
#             print(f"{sell_price:.2f}", end= " ")
#
# # for item in items_sold: Еквивалент на ред 26
#     # print(f"{item:.2f}", end= " ")
# print()
# print(f"Profit: {profit:.2f}")
# new_budget = sold_sum + budget
# if new_budget >= ticket_price:
#     print(f"Hello, France!")
# else:
#     print(f"Not enough money.")



# РЕШЕНИЕ МАРИО ЗАХАРИЕВ ЯНУАРИ 2022

items = input().split("|")
budget = float(input())
profit = 0
new_item_prices = []
data_prices = []
condition = False

for item in items:
    current_item_info = item.split("->")
    type_of_product = current_item_info[0]
    price = float(current_item_info[1])
    condition = False

    if type_of_product == "Clothes":
        if price <= 50:
            condition = True
    elif type_of_product == "Shoes":
        if price <= 35:
            condition = True
    elif type_of_product == "Accessories":
        if price <= 20.50:
            condition = True

    if condition:
        if budget >= price:
            budget -= price
            profit += price * 0.40
            new_price = price + (price * 0.40)
            new_item_prices.append(new_price) # Съхраняваме ги като integer 
            data_prices.append(f"{new_price:.2f}") # Съхраняваме ги като стрингове, за да можем да ги джойннем

print(" ".join(data_prices))
print(f"Profit: {profit:.2f}")

total_sum = budget + sum(new_item_prices)
if total_sum >= 150:
    print(f"Hello, France!")
else:
    print("Not enough money.")