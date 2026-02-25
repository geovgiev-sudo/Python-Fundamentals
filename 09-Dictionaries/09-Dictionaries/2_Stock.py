items = input().split()
products = input().split()
magasin = {}
for i in range(0, len(items), 2): # Трябва да е стъпка 2, иначе на key ще отиде числото
    key = items[i]
    value = int(items[i + 1])
    magasin[key] = value

for p in products:
    if p in magasin.keys():
        print(f"We have {magasin[p]} of {p} left")
    else:
        print(f"Sorry, we don't have {p}")