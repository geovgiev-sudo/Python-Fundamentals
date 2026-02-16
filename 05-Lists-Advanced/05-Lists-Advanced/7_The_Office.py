string_of_number = input().split()
employees_count = []
for num in string_of_number:
    employees_count.append(int(num))

factor = int(input())
happiness_levels = []
for employee in employees_count:
    employee_happiness_level = employee * factor
    happiness_levels.append(employee_happiness_level)

total_happiness = 0

for i in happiness_levels:
    total_happiness += i

average_happiness = total_happiness / len(happiness_levels)

happy_employees_count = 0
for happiness_level in happiness_levels:
    if happiness_level >= average_happiness:
        happy_employees_count += 1

if happy_employees_count >= len(employees_count) / 2:
    print(f"Score: {happy_employees_count}/{len(employees_count)}. Employees are happy!")

else:
    print(f"Score: {happy_employees_count}/{len(employees_count)}. Employees are not happy!")