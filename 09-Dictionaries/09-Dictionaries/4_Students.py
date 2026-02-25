# students = []
# course_to_search = ""
#
# while True:
#     student_info = input()
#
#     if ":" not in student_info:
#         course_to_search = student_info
#         break
#
#     name, id_, course = student_info.split(":")
#     students.append({'name': name, 'ID': id_, 'course': course})
#
#
# for student in students:
#     if course_to_search.startswith(student['course'][0:4]):
#         print(f"{student['name']} - {student['ID']}")

command = input()
students = {}

while ":" in command:
    command = command.split(":")
    student_name = command[0]
    student_id = command[1]
    course = command[2]

    if course not in students:
        students[course] = {}
    students[course][student_id] = student_name
    command = input()

course = " ".join(command.split("_"))
for key, value in students.items():
    if key == course:
        for student_id, name in value.items():
            print(f"{name} - {student_id}")



# student_information = input()
# students = {}
#
# while not students.get(student_information):
#     student_information = student_information.split(":")
#     name = student_information[0]
#     id = student_information[1]
#     course = student_information[-1]
#
#     if course not in students:
#         students[course] = {}
#     students[course][name] = id
#     student_information = input()
#     student_information = student_information.replace("_", " ")
#
# for key, value in students[student_information].items():
#     print(f"{key} - {value}")