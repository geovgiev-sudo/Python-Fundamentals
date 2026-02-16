def smallest_number(first_number: int, second_number: int, third_number: int) -> int:
    """
    This function returns the smallest of three numbers
    :param third_number:
    :param first_number: First number
    :param second_number: Second number
    :param third_number: Third number
    :return: Multiplication of both numbers
    """
    min_number = min(first_number, second_number, third_number)
    return min_number

first_integer = int(input())
second_integer = int(input())
third_integer = int(input())

result = (smallest_number(first_integer, second_integer, third_integer))
print(result)