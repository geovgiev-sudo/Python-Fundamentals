# version = input().split(".")
# version_int = int("".join(version)) # е тука е фатката
# version_next = version_int + 1
# version_next_list = []
#
# for number in str(version_next):
#     version_next_list.append(number)
#
# print(".".join(version_next_list))


version = [int(digit) for digit in input().split(".")]
version[-1] += 1
for index in range(len(version) - 1, 0, -1):
    if version[index] > 9:
        version[index] = 0
        version[index-1] += 1

print(*version, sep=".")

# version =  input().split(".")
# version_as_integer = int("".join(version))
# next_version = version_as_integer + 1
# next_version_as_list = [digit for digit in str(next_version)]
# print(".".join(next_version_as_list))

#print(version_int)
