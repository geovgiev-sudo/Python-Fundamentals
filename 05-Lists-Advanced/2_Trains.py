wagons_count = int(input())
train = [0] * wagons_count
command = input()

while command != "End":
    tokens = command.split()
    action = tokens[0]
    if action == "add":
        train[-1] = train[-1] + int(tokens[1])
    elif action == "insert":
        train[int(tokens[1])] = train[int(tokens[1])] + int(tokens[2])
    elif action == "leave":
        train[int(tokens[1])] = train[int(tokens[1])] - int(tokens[2])
    command = input()

print(train)