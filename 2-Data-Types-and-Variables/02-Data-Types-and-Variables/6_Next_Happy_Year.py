year = int(input())
happy_year = 0

while True:
    year += 1
    year_str = str(year)

    if len(set(year_str)) == len(year_str):
        break

print(year)

# number = '9012'
# print(set(number))