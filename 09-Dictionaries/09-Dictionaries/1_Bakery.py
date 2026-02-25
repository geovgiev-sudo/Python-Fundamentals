items = input().split()
bakery = {}
for i in range(0, len(items), 2): # Трябва да е стъпка 2, иначе на key ще отиде числото
    key = items[i]
    value = int(items[i + 1])
    bakery[key] = value

print(bakery)