n = int(input())
cars = {}
for i in range(n):
    command = input().split()
    action = command[0]
    username = command[1]

    if action == "register":
        license_plate_number = command[2]
        if username in cars.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            cars[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    elif action == "unregister":
        if username not in cars.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del cars[username]

for key, value in cars.items():
    print(f"{key} => {value}")