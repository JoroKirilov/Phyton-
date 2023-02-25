water_tank = [1, 10, 0, 0, 5, 0, 2, 0]

max_height_idx = water_tank.index(max(water_tank))
left_max_height = water_tank[max_height_idx]

water = 0
for idx in range(water_tank.index(max(water_tank[max_height_idx + 1:])), water_tank[max_height_idx + 1], -1):
    water += max(water_tank[max_height_idx + 1:]) - water_tank[idx - 1]

print(water)
