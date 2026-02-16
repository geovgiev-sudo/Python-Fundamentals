n = int(input())
magic_word = input()
lst = []
magic_lst = []

for i in range(n):
    strings = input()
    lst.append(strings)

for string in lst:
    if magic_word in string:
        magic_lst.append(string)

print(lst)
print(magic_lst)