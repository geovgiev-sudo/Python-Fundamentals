contests = {}

while True:

    info = input().split(" -> ")
    if "no more time" in info:
        break

    username = info[0]
    contest = info[1]
    points = int(info[2])

    if contest not in contests:
        contests[contest] = {}

    if username not in contests[contest]:
        contests[contest][username] = points

    if points > contests[contest][username]:
        contests[contest][username] = points


users_data = {}
for contest, users in contests.items():
    for user, points in users.items():
        if user not in users_data:
            users_data[user] = 0
        users_data[user] += points


for contest, participants in contests.items():
    print(f"{contest}: {(len(participants))} participants")
    participant_count = 0
    sorted_points = sorted(participants.items(), key=lambda x: (-x[1], x[0]))
    for participant, points in sorted_points:
        participant_count += 1
        print(f"{participant_count}. {participant} <::> {points}")

print(f"Individual standings:")
sorted_points = sorted(users_data.items(), key=lambda x: (-x[1], x[0]))
user_count = 0
for user, points in sorted_points:
    user_count += 1
    print(f"{user_count}. {user} -> {points}")
