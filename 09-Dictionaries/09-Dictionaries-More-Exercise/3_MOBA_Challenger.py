players = {}

while True:
    command = input()
    if command == "Season end":
        break

    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        if player not in players:
            players[player] = {}
        # if position not in players[player] or players[player][position] < int(skill):
        #     players[player][position] = int(skill)

        players[player][position] = max(players[player].get(position, 0), skill)


    elif "vs" in command:
        player1, player2 = command.split(" vs ")
        if player1 in players and player2 in players:
            common_position = False
            for position in players[player1]:
                if position in players[player2]:
                    common_position = True
                    break

            if common_position:
                p1_total_skill = sum(players[player1].values())
                p2_total_skill = sum(players[player2].values())

                if p1_total_skill > p2_total_skill:
                    del players[player2]
                elif p2_total_skill > p1_total_skill:
                    del players[player1]


players_data = {}

# Първи начин да се добавят тотал точките :

# for player, info in players.items():
#     for role, points in info.items():
#         if player not in players_data:
#             players_data[player] = 0
#         players_data[player] += points

# sorted_total = sorted(players_data.items(), key=lambda x: (-x[1], x[0]))

# Втори начин да се добавят тотал точките :

# for player, info in players.items():
#     players_data[player] = sum(info.values())


# sorted_total = sorted(players_data.items(), key=lambda x: (-x[1], x[0]))


# Трети начин да се добавят тотал точките :

sorted_total = sorted(players.items(), key=lambda x: (-sum(x[1].values()), x[0]))

for player, info in sorted_total:
    total_skill = sum(info.values())
    print(f"{player}: {total_skill} skill")
    current_player = players[player]
    sorted_position = sorted(current_player.items(), key=lambda x: (-x[1], x[0]))
    for position, skill in sorted_position:
        print(f"- {position} <::> {skill}")

