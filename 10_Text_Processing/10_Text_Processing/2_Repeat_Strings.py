text = input().split()
#for word in text:
    #print(f"{word * len(word)}", end="")

new_text = [text * len(text) for text in text]
print("".join(new_text))