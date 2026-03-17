text = input()
substring = ""
final_rage = ""
for char in text:
    if not char.isdigit():
        substring += char
    elif char.isdigit():
        substring = substring * int(char)
        final_rage += substring.upper()
        substring = ""

print(f"Unique symbols used {len(set(final_rage))}")
print(final_rage)
