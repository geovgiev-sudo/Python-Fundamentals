import re

text_string = input()
pattern = r"(?i)([#|])([a-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
matches = re.findall(pattern, text_string)
total_calories = sum([int(calories[3]) for calories in matches])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for food in matches:
    item_name, expiration_date, calories = food[1], food[2], food[3]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")