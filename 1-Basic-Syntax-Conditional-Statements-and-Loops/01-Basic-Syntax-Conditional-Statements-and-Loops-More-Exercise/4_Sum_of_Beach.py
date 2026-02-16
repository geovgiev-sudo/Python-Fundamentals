string = input().lower()
my_list = ['water', 'sand', 'fish', 'sun']
counter = 0
for word in my_list:
    counter += string.count(word)
print(counter)



# text = input().lower()
# targets = ['water', 'sand', 'fish', 'sun']
# total_count = 0
#
# # Loop through every character index in the string
# for i in range(len(text)):
#     # Check if any of our target words start at this specific index
#     for word in targets:
#         if text[i:].startswith(word):
#             total_count += 1
#
# print(total_count)