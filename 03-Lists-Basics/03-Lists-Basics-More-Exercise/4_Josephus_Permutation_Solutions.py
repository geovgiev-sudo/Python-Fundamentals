items = input().split()
k = int(input())

result = []
current_index = 0

while len(items) > 0:
    current_index = (current_index + k - 1) % len(items)
    result.append(items.pop(current_index))
print(f"[{','.join(result)}]")



# people = input().split(' ')
# kills = int(input())
# executed = []
# counter = 0
# current_index = 0
#
# while len(people) > 0:
#     counter += 1
#
#     if counter % kills == 0:
#         executed.append(people.pop(current_index))
#     else:
#         current_index += 1
#
#     if current_index >= len(people):
#         current_index = 0
#
# print(str(executed).replace(' ', '').replace('\'', ''))





# circle = input().split(' ')
# kill_count = int(input())
# result = []
# circle_int = []
# counter = 0
# # making str circle into int
# for i in circle:
#     circle_int.append(int(i))
#
# while len(circle_int) >= 1:
#     # adding killed man to result list
#     for i in circle_int:
#         counter += 1
#         if counter % kill_count == 0:
#             result.append(i)
#     # removing killed man from the circle
#     for i in result:
#         if i in circle_int:
#             circle_int.remove(i)
#
# print(str(result).replace(' ', ''))




# people = input().split()
# people_int = list((map(int, people)))
# step = int(input())
#
#
# for i in range(1, len(people_int) + 1, step):
#     people_int.remove(people_int[i + 1])
#     continue
#
# print(people_int)


