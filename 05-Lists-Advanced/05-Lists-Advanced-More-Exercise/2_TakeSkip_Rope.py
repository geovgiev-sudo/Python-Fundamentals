string = input()
numbers = []
non_numbers = []

for i in string:
    if i.isdigit():
        numbers.append(int(i))
    else:
        non_numbers.append(i)


take_list = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
skip_list = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]

rope = "".join(non_numbers)
result = ""


for i in range(len(take_list)):
    take_count = take_list[i]
    skip_count = skip_list[i]

    result += rope[:take_count]
    rope = rope[take_count + skip_count:]

print(result)




# string = input()
#
# numbers = []
# letters = ''
# take_list = []
# skip_list = []
#
# final_string = ''
#
# for character in string:
#     if character.isdigit():
#         numbers.append(int(character))
#     else:
#         letters += character
#
# for index, num in enumerate(numbers):
#     if index % 2 == 0:
#         take_list.append(num)
#     else:
#         skip_list.append(num)
#
# for take, skip in zip(take_list, skip_list):
#     if take == 0:
#         letters = letters[skip:]
#     elif take != 0:
#         final_string = final_string + letters[:take]
#         letters = letters[skip + take:]
#
# print(final_string)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # string = input()
# #
# # clean_string = "".join(char for char in string if  not char.isdigit())
# # digits_list = [int(digit) for digit in string if digit.isdigit()]
# # take_list = [take_digit for idx, take_digit in enumerate(digits_list) if idx % 2 == 0]
# # skip_list = [skip_digit for idx, skip_digit in enumerate(digits_list) if idx % 2 == 1]
# #
# # result = ""
# # pointer = 0
# #
# # for take, skip in zip(take_list, skip_list):
# #     result += clean_string[pointer:pointer + take]
# #     pointer += take
# #     pointer += skip
# #
# # print(result)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # string = input()
# #
# # clean_string = "".join(char for char in string if not char.isdigit())
# # digits_lst = [int(digit) for digit in string if digit.isdigit()]
# # take_indices = [digit for idx, digit in enumerate(digits_lst) if idx % 2 == 0]
# # skip_indices = [digit for idx, digit in enumerate(digits_lst) if idx % 2 == 1]
# #
# # index = 0
# # result = ""
# # for take, skip in zip(take_indices, skip_indices):
# #     result += clean_string[index:index + take]
# #     index += take
# #     index += skip
# #
# # difference = len(take_indices) - len(skip_indices)
# # if difference > 0:
# #     for remaining_take in take_indices[len(skip_indices):]:
# #         result += clean_string[index:index + remaining_take]
# #         index += remaining_take
# #
# # print(result)