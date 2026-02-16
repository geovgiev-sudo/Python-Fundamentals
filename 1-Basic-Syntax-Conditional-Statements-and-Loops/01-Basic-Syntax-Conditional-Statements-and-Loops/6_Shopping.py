budget = int(input())
command = input()
total = 0

while command != 'End':
    product_price = int(command)
    total += product_price
    if total > budget:
        print(f'You went in overdraft!')
        break
    command = input()
else:
    print(f'You bought everything needed.')