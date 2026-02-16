first_string = input().split(", ")
second_string = input().split(", ")
new_list = []
for word in first_string:
    for word2 in second_string:
        if word in word2:
            new_list.append(word)
            break

print(new_list)