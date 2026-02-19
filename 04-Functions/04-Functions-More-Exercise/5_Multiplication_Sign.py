def positive_negative_test(first, second, third):
    negative_counter = 0

    if first == 0 or second == 0 or third == 0:
        return "zero"
    if first < 0:
        negative_counter += 1
    if second < 0:
        negative_counter += 1
    if third < 0:
        negative_counter += 1
    if negative_counter % 2 != 0:
        return "negative"

    return "positive"

first_number = int(input())
second_number = int(input())
third_number = int(input())
result = positive_negative_test(first_number, second_number, third_number)

print(result)