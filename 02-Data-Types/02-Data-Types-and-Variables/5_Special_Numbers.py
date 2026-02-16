number = int(input())

lst_specials = [5, 7, 11]
sum_of_digits = 0
for num in range(1, number + 1):
    string_of_num = str(num)
    for digit in string_of_num:
        sum_of_digits += int(digit)
    if sum_of_digits in lst_specials:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
    sum_of_digits = 0

# n = int(input())
#
# sum_num = 0
#
# for num in range(1, n + 1):
#
#     if num < 10:
#         if num == 5 or num == 7 or num == 11:
#             print(f"{num} -> True")
#         else:
#             print(f"{num} -> False")
#
#     else:
#         num_str = str(num)
#         num1 = int(num_str[0])
#         num2 = int(num_str[1])
#         sum_num = num1 + num2
#         if sum_num == 5 or sum_num == 7 or sum_num == 11:
#             print(f"{num} -> True")
#         else:
#             print(f"{num} -> False")

# n = int(input())
#
# special_number = 0
#
# for number in range(1, n + 1):
#     sum_of_digits = 0
#     digits = number
#     while digits > 0:
#         sum_of_digits += digits % 10
#         digits = int(digits / 10)
#
#     if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
#         print(f'{number} -> True')
#     else:
#         print(f'{number} -> False')