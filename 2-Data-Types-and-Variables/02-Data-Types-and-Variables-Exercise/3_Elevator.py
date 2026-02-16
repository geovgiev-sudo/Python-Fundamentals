from math import ceil

n = int(input())
p = int(input())

full_courses = ceil(n / p)
remaining_course = n % p

print(full_courses)