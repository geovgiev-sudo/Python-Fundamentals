command = input()
courses = {}

while command != "end":
    info = command.split(" : ")
    course_name = info[0]
    student_name = info[1]

    if course_name not in courses.keys():
        courses[course_name] = [] # Value на речника е празен списък
    courses[course_name].append(student_name)

    command = input()

for course, names in courses.items():
    print(f"{course}: {len(names)}")
    for name in names:
        print(f"-- {name}")
