force_users = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        side, user = command.split(" | ")

        user_exists = False
        for users_list in force_users.values():
            if user in users_list:
                user_exists = True
                break

        if not user_exists:
            if side not in force_users:
                force_users[side] = []
            force_users[side].append(user)

    elif " -> " in command:
        user, side = command.split(" -> ")


        for current_side in force_users:
            if user in force_users[current_side]:
                force_users[current_side].remove(user)
                break


        if side not in force_users:
            force_users[side] = []

        force_users[side].append(user)
        print(f"{user} joins the {side} side!")


for side, users in force_users.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")