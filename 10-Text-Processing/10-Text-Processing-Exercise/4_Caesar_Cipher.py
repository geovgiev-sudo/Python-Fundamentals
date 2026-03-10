text = input()
encrypted_text = ""
for char in text:
    encrypted_char = ord(char) + 3
    encrypted_text += chr(encrypted_char)

print(encrypted_text)