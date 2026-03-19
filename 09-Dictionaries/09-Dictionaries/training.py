n = int(input())
my_dict = {}

for i in range(n):
    word = input()
    synonym = input()

    if word not in my_dict:
        my_dict[word] = [synonym] # директно създаваме лист
    else:
        my_dict[word].append(synonym)

for word, synonyms in my_dict.items():
    print(f"{word} - {', '.join(synonyms)}")