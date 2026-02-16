text = input().split()
even_words = [word for word in text if len(word) % 2 == 0]
# for word in text:
#     if len(word) % 2 == 0:
#         even_words.append(word)

print("\n".join(even_words))
