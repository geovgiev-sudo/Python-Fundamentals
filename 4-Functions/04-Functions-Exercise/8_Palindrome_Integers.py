def palindrome_check(list_of_numbers: list) -> bool | None:
    for number in list_of_numbers:
        if str(number) == str(number)[::-1]:
            print(True)
        else:
            print(False)
    return None


numbers_as_strings = input().split(", ")
numbers_as_integers = []
for num in numbers_as_strings:
    numbers_as_integers.append(int(num))

result = palindrome_check(numbers_as_integers)

