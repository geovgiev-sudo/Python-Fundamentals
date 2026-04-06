dragons = {}

n = int(input())

for i in range(n):
    info = input().split()
    dragon_type = info[0]
    dragon_name = info[1]

    # if info[2] != "null":
    #     damage = int(info[2])
    # else:
    #     damage = 45
    #
    # if info[3] != "null":
    #     health = int(info[3])
    # else:
    #     health = 250
    #
    # if info[4] != "null":
    #     armor = int(info[4])
    # else:
    #     armor = 10

    damage = int(info[2]) if info[2] != "null" else 45
    health = int(info[3]) if info[3] != "null" else 250
    armor = int(info[4]) if info[4] != "null" else 10


    if dragon_type not in dragons:
        dragons[dragon_type] = {}
    dragons[dragon_type][dragon_name] = {}
    dragons[dragon_type][dragon_name]["damage"] = damage
    dragons[dragon_type][dragon_name]["health"] = health
    dragons[dragon_type][dragon_name]["armor"] = armor

for d_type, infos in dragons.items():
    total_damage = 0
    total_health = 0
    total_armor = 0
    for name, stats in infos.items():
        total_damage += stats["damage"]
        total_health += stats["health"]
        total_armor += stats["armor"]

    average_damage = total_damage / len(dragons[d_type])
    average_health = total_health / len(dragons[d_type])
    average_armor = total_armor / len(dragons[d_type])

    print(f"{d_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
    for name in sorted(infos.keys()):
        stats = infos[name]
        damage, health, armor = stats["damage"], stats["health"], stats["armor"]
        print(f"-{name} -> damage: {damage}, health: {health}, armor: {armor}")