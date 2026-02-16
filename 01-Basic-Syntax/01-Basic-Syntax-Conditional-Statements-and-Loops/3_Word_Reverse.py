from operator import index

word = input()
reversed_word = ""

for i in range(len(word) -1, -1, -1):
    reversed_word += word[i]
    print(word[i], end="")
#reversed_word = word[::-1]

print(reversed_word)