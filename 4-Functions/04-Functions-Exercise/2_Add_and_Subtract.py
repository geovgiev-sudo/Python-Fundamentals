def sum_numbers(n1: int, n2: int) -> int:
    return n1 + n2


def subtract(result: int, n3: int) -> int:
    return result - n3


def add_and_subtract(n1: int, n2: int, n3: int) -> int:
    result = sum_numbers(n1, n2)
    final_result = subtract(result, n3)
    return final_result

num1 = int(input())
num2 = int(input())
num3 = int(input())
print(add_and_subtract(num1, num2, num3))