words = input().split("\\")
extraction = words[-1].split(".")
print(f"File name: {extraction[0]}")
print(f"File extension: {extraction[1]}")