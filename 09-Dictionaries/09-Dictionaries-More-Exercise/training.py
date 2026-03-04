for contest, participants in contests.items():
    print(f"{contest}: {(len(participants))} participants")
    participant_count = 0
    sorted_users = sorted(participants.items(), key=lambda x: x[0])
    sorted_points = sorted(sorted_users, key=lambda x: x[1], reverse=True)
    for participant, points in sorted_points:
        participant_count += 1
        print(f"{participant_count}. {participant} <::> {points}")

print(f"Individual standings:")
sorted_users = sorted(users_data.items(), key=lambda x: x[0])
sorted_points = sorted(sorted_users, key=lambda x: x[1], reverse=True)
user_count = 0
for user, points in sorted_points:
    user_count += 1
    print(f"{user_count}. {user} -> {points}")