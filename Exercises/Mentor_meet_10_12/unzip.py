team = ["Botev", "Lokomotiv", "Spartak"]
position = [16, 1, 2]
result = zip(team, position)
my_set = set(result)
print(my_set)

teams, pos = zip(*my_set)
print(teams)
print(pos)