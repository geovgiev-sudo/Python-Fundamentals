n = int(input())
positive = []
negative = []

for i in range(n):
    num = int(input())
    if num >= 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)

print(positive)
print(negative)
print(f'Count of positives: {len(positive)}')
print(f'Sum of negatives: {sum(negative)}')
