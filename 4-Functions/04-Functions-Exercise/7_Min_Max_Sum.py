def minimum_number(list_of_numbers: list) -> int:
    return min(list_of_numbers)


def maximum_number(list_of_numbers: list) -> int:
    return max(list_of_numbers)


def sum_numbers(list_of_numbers: list) -> int:
    return sum(list_of_numbers)

numbers_as_strings = input().split()
numbers_as_integers = []
for digit in numbers_as_strings:
    numbers_as_integers.append(int(digit))

print(f"The minimum number is {minimum_number(numbers_as_integers)}")
print(f"The maximum number is {maximum_number(numbers_as_integers)}")
print(f"The sum number is: {sum_numbers(numbers_as_integers)}")