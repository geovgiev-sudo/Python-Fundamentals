# string = input().split(", ")
# numbers = []
# for num in string:
#     numbers.append(int(num))
# positive_numbers = []
# negative_numbers = []
# even_numbers = []
# odd_numbers = []
#
# for num in numbers:
#     if num >= 0:
#         positive_numbers.append(str(num))
#     if num < 0:
#         negative_numbers.append(str(num))
#     if num % 2 == 0:
#         even_numbers.append(str(num))
#     if num % 2 != 0:
#         odd_numbers.append(str(num))
#
# print("Positive: " + " ".join(positive_numbers))
# print("Negative: " + " ".join(negative_numbers))
# print("Even: " + " ".join(even_numbers))
# print("Odd: " + " ".join(odd_numbers))


# numbers_input = input().split(", ")
# positive_numbers = [number for number in numbers if int(number) >= 0]
# negative_numbers = [number for number in numbers if int(number) < 0]
# even_numbers = [number for number in numbers if int(number) % 2 == 0]
# odd_numbers = [number for number in numbers if int(number) % 2 != 0]
#
# print(f"Positive: {', '.join(positive_numbers)}")
# print(f"Negative: {', '.join(negative_numbers)}")
# print(f"Even: {', '.join(even_numbers)}")
# print(f"Odd: {', '.join(odd_numbers)}")

def positive_numbers(numbers: list) -> list:
    return [number for number in numbers if int(number) >= 0]


def negative_numbers(numbers: list) -> list:
    return [number for number in numbers if int(number) < 0]


def even_numbers(numbers: list) -> list:
    return [number for number in numbers if int(number) % 2 == 0]


def odd_numbers(numbers: list) -> list:
    return [number for number in numbers if int(number) % 2 != 0]

numbers_input = input().split(", ")
print(f"Positive: {', '.join(positive_numbers(numbers_input))}")
print(f"Negative: {', '.join(negative_numbers(numbers_input))}")
print(f"Even: {', '.join(even_numbers(numbers_input))}")
print(f"Odd: {', '.join(odd_numbers(numbers_input))}")

