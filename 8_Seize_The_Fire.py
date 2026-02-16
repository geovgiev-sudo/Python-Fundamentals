# # Решение Марио Захариев януари 2022
#
# fires_cells = input().split('#')
# water_amount = int(input())
# effort = 0
# total_fire = 0
#
# # Булева променлива, за да избегнем да пишем цялото за всяка една проверка по-долу
# # Виж ред 32
# condition = False
#
# print(f"Cells:")
# for current_fire in fires_cells:
#     fire_info = current_fire.split(' = ') # втори сплит
#     type_of_fire = fire_info[0]
#     value_of_fire = int(fire_info[1])
#
#     # Тук го ресетвам на False, иначе като го сетна долу на True,
#     # ще си остане True завинаги и става лошо
#     condition = False
#
#     if type_of_fire == 'High':
#         if 81 <= value_of_fire <= 125:
#             condition = True
#     elif type_of_fire == 'Medium':
#         if 51 <= value_of_fire <= 80:
#             condition = True
#     elif type_of_fire == 'Low':
#         if 1 <= value_of_fire <= 50:
#             condition = True
#
#     if condition: # Виж ред 8
#         if water_amount >= value_of_fire:
#             water_amount -= value_of_fire
#             effort += value_of_fire * 0.25
#             total_fire += value_of_fire
#             print(f' - {value_of_fire}')
#
# print(f'Effort: {effort:.2f}')
# print(f'Total Fire: {total_fire}')
#










# Решение Иван Шопов Януари 2021

all_cells = input().split("#")
water = int(input())
total_efforts = 0
total_fire = 0
cells_values = []

for cell in all_cells:
    current_cell = cell.split(" = ")
    type_of_fire = current_cell[0]
    cell_value = int(current_cell[-1])

    if type_of_fire == "High":
        if not 81 <= cell_value <= 125:
            continue
    elif type_of_fire == "Medium":
        if not 51 <= cell_value <= 80:
            continue
    elif type_of_fire == "Low":
        if not 1 <= cell_value <= 50:
            continue

    if water < cell_value:
        continue
    cells_values.append(cell_value)
    water -= cell_value
    total_efforts += cell_value * 0.25
    total_fire += cell_value

print("Cells:")
for cell in cells_values:
    print(f" - {cell}")

print(f"Effort: {total_efforts:.2f}")
print(f"Total Fire: {total_fire}")

