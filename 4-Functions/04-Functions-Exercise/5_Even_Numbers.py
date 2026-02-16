def is_even(current_number: int) -> bool:
    return current_number % 2 == 0


numbers_as_string = input().split()
numbers_as_digits = []
for number in numbers_as_string:
    numbers_as_digits.append(int(number))

result = list(filter(is_even, numbers_as_digits))
print(result)