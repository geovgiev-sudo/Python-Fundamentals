string = input()
capital_indices = []
for i in range(len(string)):
    if string[i].isupper():
        capital_indices.append(i)
print(capital_indices)


# text = input()
# indices = []
# counter = 0
#
# for char in text:
#     if char.isupper():
#         indices.append(counter)
#     counter += 1
#
# print(indices)