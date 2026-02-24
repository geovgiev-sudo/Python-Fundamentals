# Write a program that finds if the multiplication of three integers is negative, positive, or zero.
# Try to do this WITHOUT multiplying the 3 numbers!
def multiplication(a, b, c):
    result = None
    if (c > 0 and a < 0 and b < 0) or \
            (b > 0 and a < 0 and c < 0) or \
            (a > 0 and b < 0 and c < 0) or \
            (a > 0 and b > 0 and c > 0):
        result = "positive"

    elif a == 0 or b == 0 or c == 0:
        result = "zero"

    elif a < 0 or b < 0 or c < 0:
        result = "negative"

    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(multiplication(first_number, second_number, third_number))









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