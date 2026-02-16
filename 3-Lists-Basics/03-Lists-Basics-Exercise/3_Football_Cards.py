cards_list = input().split()

team_a = [f'A-{number}' for number in range(1, 12)]
team_b = [f'B-{number}' for number in range (1, 12)]

players_team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
players_team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

players_count_a = 11
players_count_b = 11
game_was_terminated = False
for card in cards_list:
    if card in players_team_a:
        players_team_a.remove(card)
        players_count_a -= 1
    elif card in players_team_b:
        players_team_b.remove(card)
        players_count_b -= 1
    if len(players_team_a) < 7 or len(players_team_b) < 7:
        game_was_terminated = True
        break

print(f'Team A - {len(players_team_a)}; Team B - {len(players_team_b)}')
if game_was_terminated:
    print(f'Game was terminated')





team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
kicked_players = input().split()

for player in kicked_players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
        print("Game was terminated")
        break

else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")