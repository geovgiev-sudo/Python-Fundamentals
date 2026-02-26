words = input().split()
dictionary = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in dictionary:
        dictionary[word_lower] = 0
    dictionary[word_lower] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")


sequence = input().split(' ')

final_dic = {}
for element in sequence:
    counter = 0
    word = element.lower()
    for curr_element in sequence:
        if curr_element.lower() == word:
            counter += 1
    if counter % 2 != 0:
        final_dic[element.lower()] = element

print(' '.join(final_dic))