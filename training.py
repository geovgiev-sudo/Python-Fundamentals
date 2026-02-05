numbers_as_string = input().split(", ")
numbers_as_integers = []
even_integers_indices = []

for number in numbers_as_string:
    numbers_as_integers.append(int(number))

for i, number in enumerate(numbers_as_integers):
    if number % 2 == 0:
        even_integers_indices.append(i)

print(even_integers_indices)