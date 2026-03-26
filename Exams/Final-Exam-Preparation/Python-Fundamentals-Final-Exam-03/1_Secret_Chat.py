message = input()
command = input()
while command != "Reveal":
    actions = command.split(":|:")
    action = actions[0]
    if action == "InsertSpace":
        i = int(actions[1])
        message = message[:i] + " " + message[i:]
        print(message)


    elif action == "Reverse":
        substring = actions[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            substring = substring[::-1]
            message = message + substring
            print(message)
        else:
            print(f"error")

    elif action == "ChangeAll":
        substring = actions[1]
        replacement = actions[2]
        message = message.replace(substring, replacement)
        print(message)


    command = input()

print(f"You have a new text message: {message}")