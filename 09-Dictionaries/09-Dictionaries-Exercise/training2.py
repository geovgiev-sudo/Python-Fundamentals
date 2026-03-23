
results = {}
submissions = {}
while True:
    command = input()

    if command == "exam finished":
        break

    if "banned" in command:
        username, banned = command.split("-")
        del results[username]
        continue

    else:
        username, language, points = command.split("-")
        points = int(points)
        if username not in results:
            results[username] = 0
        if points > results[username]:
            results[username] = points
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1


print("Results:")
for name, points in results.items():
    print(f"{name} | {points}")
print(f"Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")

