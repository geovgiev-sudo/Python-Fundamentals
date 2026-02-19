# def print_tribonacci(n):
#     if n <= 0:
#         return
#     sequence = [1, 1, 2]
#     if n <= 3:
#         print(*(sequence[:n]))
#         return
#     for i in range(3, n):
#         next_val = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
#         sequence.append(next_val)
#     print(*sequence)
#
#
# num = int(input("Enter a number: "))
# print_tribonacci(num)
#


def print_tribonacci(n: int):
    if n <= 0: return
    a, b, c = 1, 1, 2

    results = []
    for i in range(1, n + 1):
        if i == 1:
            results.append(a)
        elif i == 2:
            results.append(b)
        elif i == 3:
            results.append(c)
        else:
            next_val = a + b + c
            results.append(next_val)
            a, b, c = b, c, next_val

    print(*results)

num = int(input())
print_tribonacci(num)


# def sum_previous_numbers(num: int):
#     sequence = []
#
#     for i in range(num):
#         if i == 0 or i == 1:
#             sequence.append(1)
#         elif i == 2:
#             sequence.append(2)
#         else:
#             next_number = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
#             sequence.append(next_number)
#
#     return sequence
#
# number = int(input())
# result = sum_previous_numbers(number)
# print(" ".join(str(num) for num in result))