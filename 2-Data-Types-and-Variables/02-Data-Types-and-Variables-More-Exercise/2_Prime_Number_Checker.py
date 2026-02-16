number = int(input())

is_prime = True

if number <= 1:
    is_prime = False
else:
    for num in range(2, number):
        if number % num  == 0:
            is_prime = False
            break

print(is_prime)






# n = int(input())
# is_Prime = True
#
# if n <= 2:
#     print(is_Prime)
#
# else:
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0: # ако има делител -> не е просто
#             is_Prime = False
#             print(is_Prime)
#             break
#     else:
#         print(is_Prime)