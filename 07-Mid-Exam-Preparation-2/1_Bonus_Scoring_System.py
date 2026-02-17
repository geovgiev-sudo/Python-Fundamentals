# from math import ceil
#
# number_of_students = int(input())
# number_of_lectures = int(input())
# bonus = int(input())
# max_bonus = 0
# lectures_attended = 0
#
# for student in range(1, number_of_students + 1):
#     attendance = int(input())
#     total_bonus = attendance / number_of_lectures * (5 + bonus)
#     if total_bonus > max_bonus:
#         max_bonus = total_bonus
#         lectures_attended = attendance
#
# print(f"Max Bonus: {ceil(max_bonus)}.")
# print(f"The student has attended {lectures_attended} lectures.")


### ИВАН ШОПОВ


number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_attendances = 0
total_bonus = 0
for current_student in range(number_of_students):
    attendance_of_current_student = int(input())
    if attendance_of_current_student > max_attendances:
        max_attendances = attendance_of_current_student
if number_of_lectures > 0:
    total_bonus = max_attendances / number_of_lectures * (5 + additional_bonus)
print(f"Max Bonus: {round(total_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")