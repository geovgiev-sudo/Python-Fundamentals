words = input()
my_dict = {}
value = 1
for i in words:
    if i == " ":
        continue
    key = i
    if key in my_dict.keys():
        my_dict[key] += value
    else:
        my_dict[key] = value

for symbol, value in my_dict.items():
    print(f"{symbol} -> {value}")


# characters  = input()
# occurrences = {}
# for character in characters:
#     if character == " ":
#         continue
#     if character not in occurrences.keys():
#         occurrences[character] = 0 # просто си я създавам
#     occurrences[character] += 1 # така или иначе ще увеличавам
#     # if character not in occurrences.keys():
#     #     occurrences[character] = 1
#     # else:
#     #     occurrences[character] += 1
# for character, repetitions in occurrences.items():
#     print(f"{character} -> {repetitions}")
