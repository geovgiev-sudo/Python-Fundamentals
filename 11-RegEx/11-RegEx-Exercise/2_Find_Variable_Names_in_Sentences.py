import re

text = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
matches = re.findall(pattern, text)
print(",".join(matches))





import re
pattern = r'\b_(?P<word>[A-Za-z0-9]+\b)'
strings = input()
variables = re.findall(pattern, strings)
print(','.join(variables))