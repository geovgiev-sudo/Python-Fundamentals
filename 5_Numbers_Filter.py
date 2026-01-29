n = int(input())

even_numbers = []
odd_numbers = []
positive_numbers = []
negative_numbers = []

for num in range(n):
    number = int(input())

    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)

    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

command = input()

if command == "even":
    print(even_numbers)
elif command == "odd":
    print(odd_numbers)
elif command == "positive":
    print(positive_numbers)
elif command == "negative":
    print(negative_numbers)

# n = int(input())
# numbers = []
# filtered = []
#
# for i in range(n):
#     number = int(input())
#     numbers.append(number)
#
# command = input()
# if command == 'even':
#     for num in numbers:
#         if num % 2 == 0:
#             filtered.append(num)
# elif command == 'odd':
#     for num in numbers:
#         if num % 2 != 0:
#             filtered.append(num)
# elif command == 'negative':
#     for num in numbers:
#         if num < 0:
#             filtered.append(num)
# elif command == 'positive':
#     for num in numbers:
#         if num >= 0:
#             filtered.append(num)
#
# print(filtered)