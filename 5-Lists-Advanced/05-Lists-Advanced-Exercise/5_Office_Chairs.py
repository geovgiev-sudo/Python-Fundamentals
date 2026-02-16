# number_of_rooms = int(input())
# total_chairs = 0
# total_visitors = 0
#
#
# for room in range(1, number_of_rooms + 1):
#     info = input().split()
#     chairs = len(info[0])
#     visitors = int(info[1])
#     total_chairs += chairs
#     total_visitors += visitors
#     difference = chairs - visitors
#     if difference < 0:
#         print(f"{abs(difference)} more chairs needed in room {room}")
#
# if total_chairs >= total_visitors:
#     free_chairs = total_chairs - total_visitors
#     print(f"Game On, {free_chairs} free chairs left")


number_of_rooms = int(input())
total_free_chairs = 0
for number_of_room in range(1, number_of_rooms +1):
    chairs_in_current_room, visitors = input().split()
    difference = len(chairs_in_current_room) - int(visitors)
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {number_of_room}")
    total_free_chairs += difference
if total_free_chairs >=0:
    print(f"Game On, {total_free_chairs} free chairs left")