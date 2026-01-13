command = input()
coffees_needed = 0

while command != 'END':
    event = command
    if (event == 'coding'
            or event == 'dog'
            or event == 'cat'
            or event == 'movie'):
        coffees_needed += 1
    elif (event == 'CODING'
            or event == 'DOG'
            or event == 'CAT'
            or event == 'MOVIE'):
        coffees_needed += 2
    else:
        command = input()
        continue

    command = input()

if coffees_needed > 5:
    print('You need extra sleep')
else:
    print(coffees_needed)