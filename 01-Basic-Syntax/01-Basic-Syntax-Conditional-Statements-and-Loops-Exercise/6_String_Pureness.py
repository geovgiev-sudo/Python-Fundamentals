strings_count = int(input())
unpure_strings = {',', '.', '_'}

for i in range(1, strings_count + 1):
    string = input()
    for ch in string:
        if ch in unpure_strings:
            print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')
