number_of_words = int(input())
synonyms = {}

for i in range(number_of_words):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")




word_synonyms = {}
words = int(input())

for synonyms in range(words):
    word = input()
    synonym = input()
    if word not in word_synonyms:
        word_synonyms[word] = []
        word_synonyms[word].append(synonym)
    else:
        word_synonyms[word].append(synonym)

for word, synonym in word_synonyms.items():
    print(f"{word} - ", end="")
    print(*synonym, sep=", ")