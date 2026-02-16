string = input()
counter = int(input())

repeat_string = lambda text, n: text * n
result = repeat_string(string, counter)
print(result)