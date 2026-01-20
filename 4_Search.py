n = int(input())
magic_word = input()
lst = []
magic_lst = []

for i in range(n):
    strings = input()
    lst.append(strings)
    if magic_word in strings:
        magic_lst.append(strings)

print(lst)
print(magic_lst)