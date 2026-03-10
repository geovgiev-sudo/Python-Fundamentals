text = input()
for char in range(len(text) - 1):
    if text[char] == ":":
        print(f":{text[char + 1]}")