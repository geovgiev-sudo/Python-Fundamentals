participants = {}
submissions = {}
while True:
    command = input()

    if command == "exam finished":
        break

    if "banned" in command:
        name = command.split("-")[0]
        del participants[name]
        continue
    else:
        name = command.split("-")[0]
        language = command.split("-")[1]
        points = int(command.split("-")[2])

    if name not in participants:
        participants[name] = 0

    if points > participants[name]:
        participants[name] = points

    if language not in submissions:
        submissions[language] = 0
    submissions[language] += 1

print("Results:")
for name, points in participants.items():
    print(f"{name} | {points}")
print(f"Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")


