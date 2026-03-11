# zip

words = input().split()

zipped = zip(words[0], words[1])
total_sum = 0
for char1, char2 in zipped:
    total_sum += ord(char1) * ord(char2)
leftovers = words[0][len(words[1]):] or words[1][len(words[0]):]
for char in leftovers:
    total_sum += ord(char)
print(total_sum)


# fancy shmens comprehension:

str1, str2 = input().split()

# Core sum using zip
total_sum = sum(ord(a) * ord(b) for a, b in zip(str1, str2))

# Remaining sum using slicing
total_sum += sum(ord(c) for c in str1[len(str2):])
total_sum += sum(ord(c) for c in str2[len(str1):])

print(total_sum)


# zip 2

first, second = input().split()
result = 0

for a, b in zip(first, second):
    result += ord(a) * ord(b)

longer = first[len(second):] + second[len(first):]

for char in longer:
    result += ord(char)

print(result)


# zip longest

from itertools import zip_longest

first, second = input().split()
result = 0

for a, b in zip_longest(first, second):

    if a and b:
        result += ord(a) * ord(b)

    elif a:
        result += ord(a)

    else:
        result += ord(b)

print(result)


# index

first, second = input().split()
result = 0

if len(first) > len(second):
    for idx in range(len(second)):
        result += ord(second[idx]) * ord(first[idx])
    for index in range(len(second), len(first)):
        result += ord(first[index])

elif len(second) > len(first):
    for idx in range(len(first)):
        result += ord(first[idx]) * ord(second[idx])
    for index in range(len(first), len(second)):
        result += ord(second[index])

elif len(first) == len(second):
    for idx in range(len(first)):
        result += ord(first[idx]) * ord(second[idx])

print(result)