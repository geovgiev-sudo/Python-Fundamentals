# text = input()
# for char in range(len(text) - 1):
#     if text[char] == ":":
#         print(f":{text[char + 1]}")
#

# zip

sentence = input()

for a, b in zip(sentence, sentence[1:]):
    if a == ":":
        print(a + b)


# text = input()
#
# for i in range(len(text)):
#     if text[i] == ":" and text[i + 1] != " ":
#         result = text[i] + text[i + 1]
#         print(result)