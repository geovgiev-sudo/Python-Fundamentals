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