strings_count = int(input())
unpure_strings = {',', '.', '_'}

for i in range(1, strings_count + 1):
    string = input()
    if any(ch in unpure_strings for ch in string):
        print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')
