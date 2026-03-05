command = input()
while command != "end":
    word = command
    # reversed_word = ""
    reversed_word = word[::-1]
    # for i in range(len(word) - 1, - 1, - 1):
    #     reversed_word += word[i]
    print(f"{word} = {reversed_word}")
    command = input()
