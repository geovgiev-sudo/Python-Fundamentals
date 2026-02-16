numbers = input().split(", ")

for num in numbers:
    if num == "0":
        numbers.remove(num)
        numbers.append(num)

num_integers = []
for num in numbers:
    num_integers.append(int(num))

print(num_integers)