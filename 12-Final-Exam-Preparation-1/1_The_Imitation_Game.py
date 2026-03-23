message = input()
command = input()

while command != "Decode":
    instructions = command.split("|")
    action = instructions[0]
    if action == "Move":
        n = int(instructions[1])
        message = message[n:] + message[:n]

    elif action == "Insert":
        i = int(instructions[1])
        v = instructions[2]
        message = message[:i] + v + message[i:]
        # message_list = [char for char in message]
        # message_list.insert(i, v)
        # message = "".join(message_list)

    elif action == "ChangeAll":
        substring = instructions[1]
        replacement = instructions[2]
        while substring in message:
            message = message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {message}")