usernames = input().split(", ")
valid_usernames = []

for username in usernames:
    if 3 <= len(username) <= 16:
        username_valid = True
        for char in username:
            if not (char.isalnum() or char == "-" or char == "_"):
                username_valid = False
                break
        if username_valid:
            valid_usernames.append(username)

print("\n".join(valid_usernames))

# all comprehension

usernames = input().split(", ")

for username in usernames:
    # Check length
    length_valid = 3 <= len(username) <= 16

    # Check if ALL characters are allowed
    # (isalnum() covers letters and numbers)
    chars_valid = all(char.isalnum() or char == "-" or char == "_" for char in username)

    if length_valid and chars_valid:
        print(username)


# for-else

usernames = input().split(", ")

for username in usernames:
    # Rule 1: Check length
    if 3 <= len(username) <= 16:

        # Rule 2: Check characters
        for char in username:
            if not (char.isalnum() or char == "-" or char == "_"):
                break  # We found an invalid char, STOP checking this name
        else:
            # This block only runs if the 'for' loop above FINISHED
            # without ever hitting the 'break' line.
            print(username)


# Functions

def length_is_valid(name: str) -> bool:
    if 3 <= len(name) <= 16:
        return True
    return False


def symbols_are_valid(name: str) -> bool:
    for character in name:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def no_redundant_symbols(name: str) -> bool:
    if " " in name:
        return False
    return True


def username_is_valid(name: str) -> bool:
    if length_is_valid(name) and symbols_are_valid(name) and no_redundant_symbols(name):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)