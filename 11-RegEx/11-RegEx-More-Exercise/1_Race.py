import re

pattern_for_name = r"[A-Za-z]"
pattern_for_numbers = r"\d"

participants = input().split(', ')
line = input()
results = {}

while line != "end of race":
    found_name = re.findall(pattern_for_name, line)
    found_name = ''.join(found_name)

    if found_name in participants:
        distance = re.findall(pattern_for_numbers, line)
        if distance:
            distance = sum([int(meters) for meters in distance])
            results[found_name] = results.get(found_name, 0) + distance

    line = input()

sorted_names = sorted(results, key=lambda name: results[name], reverse=True)

print(f"1st place: {sorted_names[0]}")
print(f"2nd place: {sorted_names[1]}")
print(f"3rd place: {sorted_names[2]}")





import re

name_of_participants = {name.replace(" ", ""): 0 for name in input().split(",")}
racer_code = input()
letters_d = re.compile(r"([A-Za-z])")
numbers_d = re.compile(r"([0-9])")
while racer_code != "end of race":
    find_name = "".join(re.findall(letters_d, racer_code))
    find_numbers = sum(int(num) for num in re.findall(numbers_d, racer_code))
    if find_name in name_of_participants.keys():
        name_of_participants[find_name] += find_numbers
    racer_code = input()

name_of_participants = sorted(name_of_participants.items(), key=lambda x: -x[1])

print(f"1st place: {name_of_participants[0][0]}")
print(f"2nd place: {name_of_participants[1][0]}")
print(f"3rd place: {name_of_participants[2][0]}")