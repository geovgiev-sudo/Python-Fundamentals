import re

text = input()

pattern = r"[@#]+([a-z]{3,})[@#]+[^A-Za-z0-9]*\/+(\d+)\/+"
eggs_found = re.findall(pattern, text)

for color, amount in eggs_found:
    print(f"You found {amount} {color} eggs!")