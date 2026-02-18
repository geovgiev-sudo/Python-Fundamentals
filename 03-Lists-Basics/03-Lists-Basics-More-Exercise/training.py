integers = list(map(int, input().split()))
command = input()

while command != "end":
    command = command.split()
    action = command[0]

    even_numbers = [even for even in integers if even % 2 == 0]
    odd_numbers = [odd for odd in integers if odd % 2 != 0]

    if action == "exchange":
        index = int(command[1])
        if 0 <= index < len(integers):
            integers = integers[index + 1:] + integers[:index + 1]
        else:
            print("Invalid index")

    elif action == "max":
        odd_even = command[1]
        if odd_even == "even" and even_numbers:
            print((len(integers) - integers[::-1].index(max(even_numbers)) - 1))
        elif odd_even == "odd" and odd_numbers:
            print((len(integers) - integers[::-1].index(max(odd_numbers)) - 1))
        else:
            print("No matches")

    elif action == "min":
        odd_even = command[1]
        if odd_even == "even" and even_numbers:
            print((len(integers) - integers[::-1].index(min(even_numbers)) - 1))
        elif odd_even == "odd" and odd_numbers:
            print((len(integers) - integers[::-1].index(min(odd_numbers)) - 1))
        else:
            print("No matches")

    elif action == "first":
        count = int(command[1])
        odd_even = command[2]
        if 0 < count <= len(integers):
            if odd_even == "even":
                print(even_numbers[0:count])
            elif odd_even == "odd":
                print(odd_numbers[0:count])
        else:
            print("Invalid count")

    elif action == "last":
        count = int(command[1])
        odd_even = command[2]
        if 0 < count <= len(integers):
            if odd_even == "even":
                print(even_numbers[-count:])
            elif odd_even == "odd":
                print(odd_numbers[-count:])
        else:
            print("Invalid count")

    command = input()

print(integers)