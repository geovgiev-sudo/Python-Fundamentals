# text = input()
# final_text = ""
# for character in text:
#     if not final_text or character != final_text[-1]:
#         final_text += character
# print(final_text)
#


# zip

string = input()
fixed_string = string[0]

for a, b in zip(string, string[1:]):
    if a != b:
        fixed_string += b

print(fixed_string)