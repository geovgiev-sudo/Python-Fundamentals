orders_count = int(input())
order_price = 0
total_price = 0

for i in range(1, orders_count + 1):
    capsule_price = float(input())
    days = int(input())
    capsules_needed_day = int(input())
    if 0.01 <= capsule_price <= 100 and 1 <= days <= 31 and 1 <= capsules_needed_day <= 2000:
        order_price = capsule_price * capsules_needed_day * days
        print(f'The price for the coffee is: ${order_price:.2f}')
        total_price += order_price

print(f'Total: ${total_price:.2f}')


