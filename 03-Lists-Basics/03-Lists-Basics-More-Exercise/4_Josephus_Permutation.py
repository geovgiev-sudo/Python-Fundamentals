people = input().split()
num = int(input())
result = []
current_index = 0
while people:
    current_index = (current_index + num - 1) % len(people)
    result.append(people.pop(current_index))

print(f"[{','.join(result)}]")