import re

demon_names = re.split(r'\s*,\s*', input())

pattern_for_name = r'[^0-9\+\-\*\/.]'
pattern_for_damage = r'[+-]?\d+(?:\.\d+)?'
pattern_for_divide_or_multiply = r'[*]|[/]'
demon_dict = {}

for name in demon_names:
    result = re.findall(pattern_for_name, name)
    demon_health = 0

    for char in result:
        demon_health += ord(char)

    extracted_damage = re.findall(pattern_for_damage, name)
    extracted_damage = [float(damage) for damage in extracted_damage]
    dividers_or_multipliers = re.findall(pattern_for_divide_or_multiply, name)
    damage_sum = sum(extracted_damage)

    for operator in dividers_or_multipliers:
        if operator == "*":
            damage_sum *= 2
        elif operator == "/":
            damage_sum /= 2
    demon_dict[name] = demon_health, damage_sum

for demon, (health, dmg) in sorted(demon_dict.items()):
    print(f"{demon} - {health} health, {dmg:.2f} damage")




import re

demons = re.split(", *", input())
demon_book = {}

demon_health_pattern = r'[^\d\+\-*\/\.]'
demon_damage_pattern = r'(?:\+|-)?[0-9]+(?:\.[0-9]+)?'
demon_operators_pattern = r'[*\/]'

for demon in demons:
    demon = demon.strip()
    demon_health = re.findall(demon_health_pattern, demon)
    demon_book[demon] = []
    demon_book[demon].append(sum(ord(match) for match in demon_health))

    demon_damage = re.finditer(demon_damage_pattern, demon)
    operators = re.findall(demon_operators_pattern, demon)
    current_demon_damage = 0

    for value in demon_damage:
        current_demon_damage += float(value.group(0))

    for operator in operators:
        if operator == '*':
            current_demon_damage *= 2
        elif operator == '/':
            current_demon_damage /= 2

    demon_book[demon].append(current_demon_damage)

for demon, qualities in sorted(demon_book.items()):
    print(f'{demon} - {qualities[0]} health, {qualities[1]:.2f} damage')