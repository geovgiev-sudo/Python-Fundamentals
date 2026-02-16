key = int(input())
number_of_lines = int(input())
message = ""

for i in range(1, number_of_lines + 1):
    letter = input()
    unlocked_letter = ord(letter) + key
    message += chr(unlocked_letter)

print(message)