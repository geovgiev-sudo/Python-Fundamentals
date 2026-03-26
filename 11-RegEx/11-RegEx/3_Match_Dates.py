import re
dates = input()
regex = r'(?P<day>\d{2})([\/.-])(?P<month>[A-Z][a-z]{2})\2([0-9]{4})\b'
matches = re.findall(regex, dates)
for match in matches:
    print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')


# find iter се ползва повече, когато има групи


# import re
# dates = input()
# pattern = r"\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b"
# matches = re.finditer(pattern, dates)
# for match in matches:
#
#     day = match.group(1)
#     month = match.group(3)
#     year = match.group(4)
#     print(f"Day: {day}, Month: {month}, Year: {year}")