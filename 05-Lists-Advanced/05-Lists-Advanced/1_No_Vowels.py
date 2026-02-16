word = input()
vowels_list = ['a', 'o', 'u', 'i', 'e']
# no_vowels = []
# for char in word:
#     if char.lower() not in vowels_list:
#         no_vowels.append(char)
#
# print(''.join(no_vowels))

no_vowels = [char for char in word if char.lower() not in ['a', 'o', 'u', 'i', 'e']]

print(''.join(no_vowels))