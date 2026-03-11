text = input()
rage_message = ""
sub_string = ""
repetitions = ""

for index in range(len(text)):
    # Case where we have non-numeric symbol
    if not text[index].isdigit():
        sub_string += text[index].upper()
        # Case where we have digit
    else:  # elif text[index].isdigit()
        repetitions += text[index]
        if index + 1 < len(text):
            if text[index + 1].isdigit():
                repetitions += text[index + 1]
        rage_message += sub_string * int(repetitions)
        sub_string = ""
        repetitions = ""

print(f"Unique symbols used: {len(set(rage_message))}")
print(rage_message)


# ver 2

string_sequence = input()

result = ""
current_string = ""
current_number = ""

for char in string_sequence:
    if not char.isdigit():
        if current_number:
            result += current_string * int(current_number)
            current_string = ""
            current_number = ""
        current_string += char
    else:
        current_number += char

result += current_string * int(current_number)

result = result.upper()

print(f"Unique symbols used: {len(set(result))}")
print(result)