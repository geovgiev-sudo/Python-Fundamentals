number = input()

largest_number = ""

for digit in range(9, -1, -1):
    for current_digit in number:
        if int(current_digit) == digit:
            largest_number += current_digit

print(largest_number)

# number = list(input())
# number.sort(reverse=True)
# print(''.join(number))

# number = input()
# result = ""
#
# while number != "":
#     biggest = number[0]
#     for digit in number:
#         if digit > biggest:
#             biggest = digit
#     result += biggest
#     number = number.replace(biggest, "", 1)
# print(result)
#
# number = input()
# print(''.join(sorted(number, reverse=True)))