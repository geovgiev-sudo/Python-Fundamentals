def smallest_number(list_with_numbers: list) -> int:
    return min(list_with_numbers)

first_integer = int(input())
second_integer = int(input())
third_integer = int(input())

result = (smallest_number([first_integer, second_integer, third_integer]))
print(result)