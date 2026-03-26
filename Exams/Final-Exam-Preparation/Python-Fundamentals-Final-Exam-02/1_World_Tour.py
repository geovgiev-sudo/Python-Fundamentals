stops = input()
while True:
    command = input().split(":")
    action = command[0]
    if action == "Travel":
        break

    if action == "Add Stop":
        i = int(command[1])
        v = command[2]
        if 0 <= i < len(stops):
            stops = stops[:i] + v + stops[i:]
        print(stops)
    elif action == "Remove Stop":
        s = int(command[1])
        e = int(command[2])
        if 0 <= s < len(stops) and 0 <= e < len(stops):
            stops = stops.replace(stops[s:e+1], "")
        print(stops)
    elif action == "Switch":
        old = command[1]
        new = command[2]
        if old in stops:
            stops = stops.replace(old, new)
        print(stops)

print(f"Ready for world tour! Planned stops: {stops}")

