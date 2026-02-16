capacity = 255
n = int(input())
liters_filled = 0

for i in range(1, n + 1):
    liters = int(input())
    if liters > capacity:
        print(f'Insufficient capacity!')
        continue
    capacity -= liters
    liters_filled += liters
print(liters_filled)
