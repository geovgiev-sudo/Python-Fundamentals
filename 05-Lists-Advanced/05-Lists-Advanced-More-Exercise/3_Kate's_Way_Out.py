def correct_lab_bounds(row, col):
    if row < 0 or col < 0 or row >= len(lab_list) or col >= len(lab_list[0]):
        return True


def check_wall(row, col):
    if lab_list[row][col] in "#v":
        return True


def find_exit(row, col):
    if row == 0 or row == len(lab_list) - 1 or col == 0 or col == len(lab_list[0]):
        return True


def find_starting_point():
    for pos_row, row in enumerate(lab_list):
        for pos_col, col in enumerate(row):
            if col == "k":
                return pos_row, pos_col


def find_the_lab_path(row, col, lab):
    if correct_lab_bounds(row, col) or check_wall(row, col):
        return

    steps.append(1)

    if find_exit(row, col):
        max_len_path.append(sum(steps))

    lab[row][col] = "v"
    find_the_lab_path(row, col + 1, lab)  # check right
    find_the_lab_path(row, col - 1, lab)  # check left
    find_the_lab_path(row + 1, col, lab)  # check up
    find_the_lab_path(row - 1, col, lab)  # check down
    lab[row][col] = " "

    steps.pop()


rows = int(input())
lab_list = []
steps = []
max_len_path = []
for curr_lab in range(rows):
    lab_list.append(list(input()))
cols = len(lab_list[0])
start_row, start_col = find_starting_point()

find_the_lab_path(start_row, start_col, lab_list)

if max_len_path:
    print(f"Kate got out in {max(max_len_path)} moves")
else:
    print("Kate cannot get out")



































# def dfs(maze, visited, rows, r, c, moves):
#
#     if r < 0 or r >= rows or c < 0 or c >= len(maze[r]):
#         return moves
#
#     if maze[r][c] == "#":
#         return -1
#
#     if visited[r][c]:
#         return -1
#
#     visited[r][c] = True
#
#     up = dfs(maze, visited, rows, r - 1, c, moves + 1)
#     down = dfs(maze, visited, rows, r + 1, c, moves + 1)
#     left = dfs(maze, visited, rows, r, c - 1, moves + 1)
#     right = dfs(maze, visited, rows, r, c + 1, moves + 1)
#
#     visited[r][c] = False
#
#     return max(up, down, left, right)
#
#
# rows = int(input())
# maze = []
# k_row = k_col = None
#
# for r in range(rows):
#     line = input()
#     maze.append(list(line))
#     if "k" in line:
#         k_row = r
#         k_col = line.index("k")
#
# visited = [[False] * len(maze[r]) for r in range(rows)]
#
# best = dfs(maze, visited, rows, k_row, k_col, 0)
#
# if best == -1:
#     print("Kate cannot get out")
# else:
#     print(f"Kate got out in {best} moves")