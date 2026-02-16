# import sys
#
# divisor = int(input())
# boundary = int(input())
# number = 0
# largest = -sys.maxsize
#
# for number in range(1, boundary + 1):
#     if number % divisor == 0:
#         largest = number
#
# print(f'{largest}')

divisor = int(input())
boundary = int(input())
number = 0

for number in range(boundary, divisor - 1, - 1):
    if number % divisor == 0:
        break

print(number)
