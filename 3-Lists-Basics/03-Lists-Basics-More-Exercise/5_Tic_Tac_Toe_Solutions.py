# Tic-Tac-Toe solved with current knowledge

first_row = input().split()
second_row = input().split()
third_row = input().split()

player = 1
name_player = "First"
found = False

while player < 3:
    player = str(player)
    line = [player, player, player]
    if line == first_row or second_row == line or third_row == line: # rows check
        found = True
    for column in range(0, 3):
        if first_row[column] == player and second_row[column] == player and third_row[column] == player: # columns check
            found = True
    if first_row[0] == player and second_row[1] == player and third_row[2] == player: # left diagonal
        found = True
    elif first_row[2] == player and second_row[1] == player and third_row[0] == player: # right diagonal
        found = True
    if found:
        print(f"{name_player} player won")
        break
    player = int(player) + 1
    name_player = "Second"
else:
    print("Draw!")

# Tic-Tac-Toe solved with functions and loops

# def check_win(board, player):
#     # check rows
#     for rows in range(3):
#         row = board[rows]
#         if row.count(player) == 3:
#             return True
#
#     # check columns
#     for columns in range(3):
#         column = [row[columns] for row in board]
#         if column.count(player) == 3:
#             return True
#
#     # check diagonals
#     primary_diagonal = [board[diagonal][diagonal] for diagonal in range(3)]
#     if primary_diagonal.count(player) == 3:
#         return True
#
#     secondary_diagonal = [board[secondary_diagonal][len(board) - secondary_diagonal - 1] for secondary_diagonal
#                           in range(3)]
#     if secondary_diagonal.count(player) == 3:
#         return True
#
#
# board = []
# for winner in range(3):
#     board.append(input().split())
#
# if check_win(board, "1"):
#     print("First player won")
# elif check_win(board, "2"):
#     print("Second player won")
# else:
#     print("Draw!")

# Tic-Tac-Toe solved with if-elif-else.py

first_line = input().split(' ')
second_line = input().split(' ')
third_line = input().split(' ')

if first_line[0] == '1' and first_line[1] == '1' and first_line[2] == '1' or second_line[0] == '1' \
        and second_line[1] == '1' and second_line[2] == '1' or third_line[0] == '1' and third_line[1] == '1' and third_line[2] == '1':
    print('First player won')
elif first_line[0] == '2' and first_line[1] == '2' and first_line[2] == '2' or second_line[0] == '2' \
        and second_line[1] == '2' and second_line[2] == '2' or third_line[0] == '2' and third_line[1] == '2' \
        and third_line[2] == '2':
    print('Second player won')
elif first_line[0] == '1' and second_line[0] == '1' and third_line[0] == '1' or first_line[1] == '1' \
        and second_line[1] == '1' and third_line[1] == '1' or first_line[2] == '1' and second_line[2] == '1' \
        and third_line[2] == '1':
    print('First player won')
elif first_line[0] == '2' and second_line[0] == '2' and third_line[0] == '2' or first_line[1] == '2' \
        and second_line[1] == '2' and third_line[1] == '2' or first_line[2] == '2' and second_line[2] == '2' \
        and third_line[2] == '2':
    print('Second player won')
elif first_line[0] == '1' and second_line[1] == '1' and third_line[2] == '1' or \
     first_line[2] == '1' and second_line[1] == '1' and third_line[0] == '1':
    print('First player won')
elif first_line[0] == '2' and second_line[1] == '2' and third_line[2] == '2' or \
     first_line[2] == '2' and second_line[1] == '2' and third_line[0] == '2':
    print('Second player won')
else:
    print("Draw!")