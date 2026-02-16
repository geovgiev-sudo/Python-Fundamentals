lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_times_broken = 0
sword_times_broken = 0
shield_times_broken = 0
armor_times_broken = 0

for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:
        helmet_times_broken += 1
    if fight % 3 == 0:
        sword_times_broken += 1
    if fight % 2 == 0 and fight % 3 == 0:
        shield_times_broken += 1
        if shield_times_broken % 2 == 0:
            armor_times_broken += 1

helmet_repair_price = helmet_price * helmet_times_broken
sword_repair_price = sword_price * sword_times_broken
shield_repair_price = shield_price * shield_times_broken
armor_repair_price = armor_price * armor_times_broken

total_expenses = helmet_repair_price + sword_repair_price + \
shield_repair_price + armor_repair_price

print(f'Gladiator expenses: {total_expenses:.2f} aureus')