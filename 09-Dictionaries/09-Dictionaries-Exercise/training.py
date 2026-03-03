force_side_dictionary = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        force_user_is_part_of_the_force = False
        for list_with_users in force_side_dictionary.values():
            if force_user in list_with_users:
                force_user_is_part_of_the_force = True
                break
        if not force_user_is_part_of_the_force:
            # We have no such force side in the dict
            if force_side not in force_side_dictionary.keys():
                force_side_dictionary[force_side] = []
            force_side_dictionary[force_side].append(force_user)
    elif "->" in command:  # else
        force_user, force_side = command.split(" -> ")
        for list_with_users in force_side_dictionary.values():
            if force_user in list_with_users:
                list_with_users.remove(force_user)
                break
        if force_side not in force_side_dictionary.keys():
            force_side_dictionary[force_side] = []
        force_side_dictionary[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_side, list_with_users in force_side_dictionary.items():
    if list_with_users: # if len(list_with_users) > 0
        print(f"Side: {force_side}, Members: {len(list_with_users)}")
        for force_user in list_with_users:
            print(f"! {force_user}")