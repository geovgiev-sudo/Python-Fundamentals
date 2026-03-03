contests = {}
users_data = {}
while True:
    data = input().split(":")

    if "end of contests" in data:
        break

    contest = data[0]
    password = data[1]
    contests[contest] = password

while True:
    info = input().split("=>")

    if "end of submissions" in info:
        break

    submission_contest = info[0]
    submission_password = info[1]
    username = info[2]
    points = int(info[3])

    for contest, password in contests.items():
        if submission_contest == contest:
            if submission_password == password:
                if username not in users_data:
                    users_data[username] = {}

                if submission_contest not in users_data[username]:
                    users_data[username][submission_contest] = points

                else:
                    if points > users_data[username][submission_contest]:
                        users_data[username][submission_contest] = points

best_user = ""
max_points = 0
for user, contests_dict in users_data.items():
    total_points = sum(contests_dict.values())
    if total_points > max_points:
        max_points = total_points
        best_user = user

print(f"Best candidate is {best_user} with total {max_points} points.")
# sorted_usernames = sorted(users_data.keys())
# print(f"Ranking:")
# for user in sorted_usernames:
#     print(user)
#     student_contests = users_data[user]
#     sorted_contest_names = sorted(student_contests, key=student_contests.get, reverse=True)
#
#     for contest in sorted_contest_names:
#         points = student_contests[contest]
#         print(f"#  {contest} -> {points}")



# lambda alternative

# 1. Sort the main dictionary by username (keys) alphabetically
sorted_users = sorted(users_data.items(), key=lambda x: x[0])

print("Ranking:")  # [cite: 47, 71]
for user, contests_dict in sorted_users:
    print(user)  # [cite: 21]

    # 2. Sort the inner dictionary by points (values) in descending order
    # x[1] refers to the points in the (contest, points) tuple
    sorted_contests = sorted(contests_dict.items(), key=lambda x: x[1], reverse=True)

    for contest, points in sorted_contests:
        print(f"# {contest} -> {points}")  # [cite: 22-25]