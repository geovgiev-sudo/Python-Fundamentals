message = input()

while True:
    command = input().split("|")
    if command[0] == "Decode":
        break

    if command[0] == "Move":
        n = int(command[1])
        message = message[n:] + message[:n]

    elif command[0] == "Insert":
        i = int(command[1])
        v = command[2]
        message = message[:i] + v + message[i:]

    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")