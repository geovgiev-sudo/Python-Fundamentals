number_list = list(map(int, input().split(", ")))
found_indices_or_no = map(
    lambda x: x if number_list[x] % 2 == 0 else 'no',
    range(len(number_list))
)
even_indices = list(filter(lambda a: a!= 'no', found_indices_or_no))
print(even_indices)




# numbers_as_string = input().split(", ")
# numbers_as_integers = []
# even_integers_indices = []
#
# for number in numbers_as_string:
#     numbers_as_integers.append(int(number))
#
# for i, number in enumerate(numbers_as_integers):
#     if number % 2 == 0:
#         even_integers_indices.append(i)
#
# print(even_integers_indices)