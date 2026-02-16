command = input()

while command != 'End':
    string = command
    if string != 'SoftUni':
        new_string = ""
        for letter in string:
            new_string += letter * 2
        print(new_string)

    command = input()