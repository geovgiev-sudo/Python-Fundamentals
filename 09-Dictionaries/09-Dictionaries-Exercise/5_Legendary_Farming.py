# # ПРАВИЛНО РЕШЕНИЕ С "ПРАВИЛНИ" ВХОДОВЕ
#
# materials = {"shards": 0, "fragments": 0, "motes": 0}
# legendary_item = ""
# won_legendary_item = False
#
# while not won_legendary_item:
#     current_materials = input().split()
#
#     for index in range(0, len(current_materials), 2):
#         key = current_materials[index + 1].lower()
#         value = int(current_materials[index])
#
#         if key not in materials.keys():
#             materials[key] = 0
#         materials[key] += value
#
#         if materials["shards"] >= 250:
#             legendary_item = "Shadowmourne"
#             materials["shards"] -= 250
#             won_legendary_item = True
#
#         elif materials["fragments"] >= 250:
#             legendary_item = "Valanyr"
#             materials["fragments"] -= 250
#             won_legendary_item = True
#
#         elif materials["motes"] >= 250:
#             legendary_item = "Dragonwrath"
#             materials["motes"] -= 250
#             won_legendary_item = True
#
#         if won_legendary_item:
#             break
#
# print(f"{legendary_item} obtained!")
#
# for material, quantity in materials.items():
#     print(f"{material}: {quantity}")


# Gemini решение

key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}
legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
obtained = False

while not obtained:
    line = input().split()
    for i in range(0, len(line), 2):
        quantity = int(line[i])
        material = line[i+1].lower()

        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                print(f"{legendary_items[material]} obtained!")
                key_materials[material] -= 250
                obtained = True
                break
        else:
            junk_items[material] = junk_items.get(material, 0) + quantity

# Printing results
for mat, qty in key_materials.items():
    print(f"{mat}: {qty}")
for mat, qty in junk_items.items():
    print(f"{mat}: {qty}")




# МОЕТО РЕШЕНИЕ С ОПРАВЕНИ ВХОДОВЕ НА СОФТУНИ ПЕДЕРАСИ


materials = input().split()
my_dict = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item = ""

for i in range(0, len(materials), 2):
    quantity = int(materials[i])
    material = materials[i + 1].lower()

    if material not in my_dict.keys():
        my_dict[material] = quantity

    else:
        my_dict[material] += quantity


    if my_dict["shards"] >= 250 or my_dict["fragments"] >= 250 or my_dict["motes"] >= 250:
        if my_dict["shards"] >= 250:
            legendary_item = "Shadowmourne"
            my_dict["shards"] -= 250
        elif my_dict["fragments"] >= 250:
            legendary_item = "Valanyr"
            my_dict["fragments"] -= 250
        elif my_dict["motes"] >= 250:
            legendary_item = "Dragonwrath"
            my_dict["motes"] -= 250

        print(f"{legendary_item} obtained!")
        print(f"shards: {my_dict['shards']}")
        print(f"fragments: {my_dict['fragments']}")
        print(f"motes: {my_dict['motes']}")
        for item, quantity in my_dict.items():
            if item != "shards" and item != "fragments" and item != "motes":
                print(f"{item}: {quantity}")
        break


# GEMINI решение


# key_materials = {"shards": 0, "fragments": 0, "motes": 0}
# junk_items = {}
# legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
# obtained = False
#
# while not obtained:
#     line = input().split()
#     for i in range(0, len(line), 2):
#         quantity = int(line[i])
#         material = line[i+1].lower()
#
#         if material in key_materials:
#             key_materials[material] += quantity
#             if key_materials[material] >= 250:
#                 print(f"{legendary_items[material]} obtained!")
#                 key_materials[material] -= 250
#                 obtained = True
#                 break
#         else:
#             junk_items[material] = junk_items.get(material, 0) + quantity
#
# # Printing results
# for mat, qty in key_materials.items():
#     print(f"{mat}: {qty}")
# for mat, qty in junk_items.items():
#     print(f"{mat}: {qty}")