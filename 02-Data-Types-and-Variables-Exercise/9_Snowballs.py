from sys import maxsize

number_of_snowballs = int(input())
max_value = -maxsize
max_weight = -maxsize
max_time = -maxsize
max_quality = -maxsize

for i in range(1, number_of_snowballs + 1):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight // snowball_time) ** snowball_quality

    if snowball_value >= max_value:
        max_value = snowball_value
        max_weight = snowball_weight
        max_time = snowball_time
        max_quality = snowball_quality

print(f'{max_weight} : {max_time} = {max_value} ({max_quality})')