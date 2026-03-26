password = input()

while True:
    command = input().split()
    action = command[0]
    if action == "Done":
        break

    if action == "TakeOdd":
        password = password[1::2]
        print(password)

    elif action == "Cut":
        start_index = int(command[1])
        length = int(command[2])
        end_index = start_index + length
        substring_to_remove = password[start_index:end_index]
        password = password[:start_index] + password[end_index:]
        print(password)
    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print(f"Nothing to replace!")
print(f"Your password is: {password}")