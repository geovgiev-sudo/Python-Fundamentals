budget = float(input())
flour_price_kg = float(input())
eggs_pack_price = 0.75 * flour_price_kg
milk_litre_price = 1.25 * flour_price_kg

loaf_price = flour_price_kg + eggs_pack_price + (milk_litre_price / 4)

number_of_loaves = 0
colored_eggs = 0

while True:
    if budget <= loaf_price:
        money_left = budget
        break

    number_of_loaves += 1
    budget -= loaf_price
    colored_eggs += 3

    if number_of_loaves % 3 == 0:
        lost_eggs = number_of_loaves - 2
        colored_eggs = colored_eggs - lost_eggs

print(f'You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.')