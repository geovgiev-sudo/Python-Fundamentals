string = input()
numbers = []
non_numbers = []

for i in string:
    if i.isdigit():
        numbers.append(int(i))
    else:
        non_numbers.append(i)


take_list = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
skip_list = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]

rope = "".join(non_numbers)
result = ""


for i in range(len(take_list)):
    take_count = take_list[i]
    skip_count = skip_list[i]

    result += rope[:take_count]
    rope = rope[take_count + skip_count:]

print(result)