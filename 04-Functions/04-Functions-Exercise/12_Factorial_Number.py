def calculate_factorial(some_number: int) -> int:
    for current_number in range(1, some_number):
        some_number *= current_number
    return some_number

first_integer = int(input())
second_integer = int(input())
first_factorial = calculate_factorial(first_integer)
second_factorial = calculate_factorial(second_integer)
result = first_factorial / second_factorial
print(f"{result:.2f}")