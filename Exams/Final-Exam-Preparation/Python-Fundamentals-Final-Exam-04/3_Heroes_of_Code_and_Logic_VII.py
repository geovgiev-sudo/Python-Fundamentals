n = int(input())
heroes = {}
for i in range(n):
    info = input().split()
    name = info[0]
    hit_points = int(info[1])
    mana_points = int(info[2])

    heroes[name] = [hit_points, mana_points]
    if heroes[name][0] >= 100:
        heroes[name][0] = 100
    if heroes[name][1] >= 200:
        heroes[name][1] = 200

while True:
    command = input().split(" - ")
    action = command[0]
    if action == "End":
        break
    hero_name = command[1]

    if action == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes[hero_name][1] >= mp_needed:
            heroes[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        elif heroes[hero_name][1] < mp_needed:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        heroes[hero_name][0] -= damage
        if heroes[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]

    elif action == "Recharge":
        recharge = int(command[2])
        recharged_total = heroes[hero_name][1] + recharge
        mana_recharged = recharge
        if recharged_total >= 200:
            recharged_total = 200
            mana_recharged = recharged_total - heroes[hero_name][1]
        heroes[hero_name][1] = recharged_total
        print(f"{hero_name} recharged for {mana_recharged} MP!")

    elif action == "Heal":
        heal = int(command[2])
        healed_total = heroes[hero_name][0] + heal
        healed = heal
        if healed_total >= 100:
            healed_total = 100
            healed = healed_total - heroes[hero_name][0]
        heroes[hero_name][0] = healed_total
        print(f"{hero_name} healed for {healed} HP!")

for hero, values in heroes.items():
    print(f"{hero}\n"
          f" HP: {values[0]}\n"
          f" MP: {values[1]}")
