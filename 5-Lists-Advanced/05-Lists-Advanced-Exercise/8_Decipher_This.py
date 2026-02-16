message = input().split()

for word in message:
    char_number = ""
    char_letters = ""
    deciphered_word = []
    for char in word:
        if char.isdigit():
            char_number += char
        if char.isalpha():
            char_letters += char

    deciphered_word = [word for word in (chr(int(char_number)) + char_letters)]
    deciphered_word[1], deciphered_word [-1] = deciphered_word[-1], deciphered_word[1]
    print(f"{''.join(deciphered_word)}", end= ' ')