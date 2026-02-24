rows = int(input())
ships_list = []

for current_row in range(rows):
    ships = input().split(' ')
    ships_list.append(ships)
attacked_squares = input().split(' ')

destroyed_counter = 0
for attack in attacked_squares:
    current_attack = attack.split('-')
    row = int(current_attack[0])
    col = int(current_attack[1])

    current_ship = ships_list[row]
    curr_ship = int(current_ship[col])

    if curr_ship > 0:
        curr_ship -= 1
        if curr_ship == 0:
            destroyed_counter += 1

    current_ship[col] = str(curr_ship)
    ships_list[row] = current_ship

print(destroyed_counter)



# field = []
# rows = int(input())
# for row in range(rows):
#     current_row = list(map(int, input().split()))
#     field.append(current_row)
#
# attacked = input().split()
# attacked_field = [[int(x) for x in attack.split("-")] for attack in attacked]
#
# destroyed = 0
# for row, col in attacked_field:
#     if field[row][col] > 0:
#         field[row][col] -= 1
#         if field[row][col] == 0:
#             destroyed += 1
#
# print(destroyed)