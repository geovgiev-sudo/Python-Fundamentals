text = input()
final_text = ""
strength = 0
for i in range(len(text)):
    if text[i] == ">":
        final_text += ">"
        explosion_strength = int(text[i + 1])
        strength += explosion_strength
    elif strength > 0:
        strength -= 1
    else:
        final_text += text[i]

print(final_text)




some_string = input()
final_string = ""
strength = 0
for index in range(len(some_string)):
    # Explosion
    if strength > 0 and some_string[index] != ">":
        strength -= 1
    # Explosion mark
    elif some_string[index] == ">":
        final_string += ">"
        strength += int(some_string[index + 1])
    # No explosion, no explosion mark
    else:
        final_string += some_string[index]
print(final_string)



# ver 2

# string_explosion = input()
# after_explosion = ""
# strength = 0
#
# for index, char in enumerate(string_explosion):
#
#     if char == ">":
#         after_explosion += char
#         strength += int(string_explosion[index + 1])
#
#     else:
#         if strength > 0:
#             strength -= 1
#         elif strength == 0:
#             after_explosion += char
#
# print(after_explosion)