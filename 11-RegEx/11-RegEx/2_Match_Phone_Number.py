import re
text = input()
# pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"
# matches = [obj.group() for obj in re.finditer(pattern, text)]

pattern = r"(\+359-2-[0-9]{3}-[0-9]{4}\\b|\+359 2 [0-9]{3}[0-9]{4})\\b"
matches = re.findall(pattern, text)

print(", ".join(matches))


import re
phone_numbers = input()
regex = r'(\+359 2 [0-9]{3} [0-9]{4}|\+359-2-[0-9]{3}-[0-9]{4})\b'
matches = re.findall(regex, phone_numbers)
print(', '.join(matches))