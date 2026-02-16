def sort_numbers(list_of_integers: list) -> list:
    return sorted(list_of_integers)

numbers_as_strings = input().split()
numbers_as_digits = []
for digit in numbers_as_strings:
    numbers_as_digits.append(int(digit))


result = sort_numbers(numbers_as_digits)
print(result)
