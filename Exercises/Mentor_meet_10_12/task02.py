def game_result(teams, results):
    winner = ""
    tournament_result = {}
    for index in range(len(teams)):
        if results[index] == 0:
            winner = teams[index][1]
        else:
            winner = teams[index][0]
        tournament_result.setdefault(winner, 0)  # add element in dict only if there is not exist
        tournament_result[winner] += 3           # increase value
    v = list(tournament_result.values())
    k = list(tournament_result.keys())
    return k[v.index(max(v))]    # max value in dict


competitions = [["Germany", "Japan"], ["Japan", "Spain"], ["Spain", "Germany"]]
results1 = [0, 0, 1]
world_cham = game_result(competitions, results1)
print(world_cham)
