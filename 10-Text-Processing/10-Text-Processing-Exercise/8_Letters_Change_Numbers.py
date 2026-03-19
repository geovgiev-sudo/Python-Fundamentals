text = input().split()
result = 0

for string in text:
    letter1 = ord(string[0])
    letter2 = ord(string[-1])
    number = int(string[1:-1])

    if chr(letter1).isupper():
        result += number / (letter1 - 64)
    elif chr(letter1).islower():
        result += number * (letter1 - 96)
    if chr(letter2).isupper():
        result -= (letter2 - 64)
    elif chr(letter2).islower():
        result += (letter2 - 96)

print(f"{result:.2f}")


#
# def upper(current_char:str) -> bool:
#     return current_char.isupper()
#
#
# def lower(current_char:str) -> bool:
#     return current_char.islower()
#
#
# sequence_of_strings = input().split()
# result = 0
# for string in sequence_of_strings:
#     current_number = ""
#
#     for char in string:
#         if char.isdigit():
#             current_number += char
#
#     first_letter = string[0]
#     last_letter = string[-1]
#
#     if upper(first_letter):
#         result += int(current_number) / (ord(first_letter) - 64)
#
#     elif lower(first_letter):
#         result += int(current_number) * (ord(first_letter) - 96)
#
#     if upper(last_letter):
#         result -= ord(last_letter) - 64
#
#     elif lower(last_letter):
#         result += ord(last_letter) - 96
#
# print(f"{result:.2f}")