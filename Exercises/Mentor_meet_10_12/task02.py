def game_result(teams, results):
    for index in range(len(teams)):
        if results[index] == 0:
            print(teams[index][1])
        else:
            print(teams[index][0])


competitions = [["Germany", "Japan"], ["Japan", "Spain"], ["Spain", "Germany"]]
results1 = [0, 0, 1]
game_result(competitions, results1)
