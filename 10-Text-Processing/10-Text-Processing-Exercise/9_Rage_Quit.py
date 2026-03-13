# text = input()
# rage_message = ""
# sub_string = ""
# repetitions = ""
#
# for index in range(len(text)):
#     # Case where we have non-numeric symbol
#     if not text[index].isdigit():
#         sub_string += text[index].upper()
#         # Case where we have digit
#     else:  # elif text[index].isdigit()
#         repetitions += text[index]
#         if index + 1 < len(text):
#             if text[index + 1].isdigit():
#                 repetitions += text[index + 1]
#         rage_message += sub_string * int(repetitions)
#         sub_string = ""
#         repetitions = ""
#
# print(f"Unique symbols used: {len(set(rage_message))}")
# print(rage_message)
#
#
# # ver 2
#
# string_sequence = input()
#
# result = ""
# current_string = ""
# current_number = ""
#
# for char in string_sequence:
#     if not char.isdigit():
#         if current_number:
#             result += current_string * int(current_number)
#             current_string = ""
#             current_number = ""
#         current_string += char
#     else:
#         current_number += char
#
# result += current_string * int(current_number)
#
# result = result.upper()
#
# print(f"Unique symbols used: {len(set(result))}")
# print(result)


# ver 3 Ines Ivanova 2021

data = input()

index = 0
current_string = ""
final_result = ""

while index < len(data):

    if not data[index].isdigit():
        current_string += data[index]
        index += 1
    else:
        current_number = ""
        while data[index].isdigit():
            current_number += data[index]
            index += 1
            if index == len(data):
                break
        current_number = int(current_number)
        output = current_string.upper() * current_number
        final_result += output
        current_string = ""

print(f"Unique symbols used: {len(set(final_result))}")
print(final_result)