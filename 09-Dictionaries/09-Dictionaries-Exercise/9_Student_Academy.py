n = int(input())
grades = {}
for i in range(n):
    student_name = input()
    grade = float(input())
    if student_name not in grades:
        grades[student_name] = []
    grades[student_name].append(grade)

for name, grades in grades.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
