def length_check(some_password: str) -> bool or str:
    if 6 <= len(password) <= 10:
        return True
    return "Password must be between 6 and 10 characters"


def letter_digit_check(some_password: str) -> bool or str:
    if some_password.isalnum():
            return True
    return "Password must consist only of letters and digits"


def digit_count_check(some_password: str) -> bool or str:
    digit_count = 0
    for symbol in some_password:
        if symbol.isdigit():
            digit_count += 1
    if digit_count >= 2:
        return True
    return "Password must have at least 2 digits"

def validate_password(some_password: str):
    is_valid = []
    is_valid.append(length_check(some_password))
    is_valid.append(letter_digit_check(some_password))
    is_valid.append(digit_count_check(some_password))
    while True in is_valid:
        is_valid.remove(True)
    return is_valid


password = input()
password_is_not_valid = validate_password(password)
if password_is_not_valid:
    print("\n".join(password_is_not_valid))
else:
    print("Password is valid")

