message = input()
while True:
    command = input().split()
    if command[0] == "Finalize":
        break

    action = command[0]
    if action == "Encrypt":
        message = message[::-1]
        print(message)

    elif action == "Decrypt":
        message = message.swapcase()
        print(message)

    elif action == "Substitute":
        old_char = command[1]
        new_char = command[2]
        if old_char in message:
            message = message.replace(old_char, new_char)
            print(message)
        else:
            print("Character not found.")

    elif action == "Scramble":
        index = int(command[1])
        char = command[2]
        if index in range(len(message)):
            message = message[:index] + char + message[index + 1:]
            print(message)
        else:
            print("Index out of bounds.")

    elif action == "Remove":
        substring = command[1]
        message = message.replace(substring, "")
        print(message)



    else:
        print("Invalid command detected!")