integers = [int(i) for i in input().split()]
removed_sum = 0

while integers:
    index = int(input())
    removed = 0

    if 0 <= index < len(integers):
        removed = integers.pop(index)

    elif index < 0:
        removed = integers[0]
        integers[0] = integers[-1]

    elif index >= len(integers):
        removed = integers[-1]
        integers[-1] = integers[0]

    removed_sum += removed

    for j in range(len(integers)):
        if integers[j] <= removed:
            integers[j] += removed
        elif integers[j] > removed:
            integers[j] -= removed

print(removed_sum)