input_data = input().split(" ")
team_a = [el for el in range(1, 12)]
team_b = [el for el in range(1, 12)]

for idx in range(len(input_data)):
    team, player = input_data[idx].split("-")
    player = int(player)
    if team == "A":
        if player in team_a:
            team_a.remove(player)
    else:
        if player in team_b:
            team_b.remove(player)

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if len(team_a) < 7 or len(team_b) < 7:
    print("Game was terminated")
