sequence_of_numbers = input().split(", ")
numbers = [int(number) for number in sequence_of_numbers]

group = 10
while numbers: # while len(number) > 0
    list_of_numbers = [number for number in numbers if number <= group]
    print(f"Group of {group}'s: {list_of_numbers}")
    numbers = [number for number in numbers if number not in list_of_numbers]
    group += 10