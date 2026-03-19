import re

all_matches = []
pattern = "\d+"
line = input()
while line:
    matches = re.findall(pattern, line)
    if matches:
        all_matches += matches
    line = input()
print(" ".join(all_matches))




import re
pattern = r'\d+'
digits = []
while True:
    string = input()
    if string:
        numbers = re.findall(pattern, string)
        if numbers:
            digits.append(' '.join(numbers))
        continue
    break

print(' '.join(digits))