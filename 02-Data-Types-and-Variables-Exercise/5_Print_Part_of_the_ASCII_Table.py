starting_index = int(input())
ending_index = int(input())

for char in range(starting_index, ending_index + 1):
    symbol = chr(char)
    if char == ending_index:
        print(chr(char))
    else:
        print(f'{symbol} ', end='')