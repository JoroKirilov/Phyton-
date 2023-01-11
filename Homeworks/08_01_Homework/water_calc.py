def water_calculate(water_bunker):
    end_of_bunker = len(water_bunker)
    water = 0
    end_of_bunker_reached = False
    for left_wall in range(end_of_bunker):
        if water_bunker[left_wall]:
            left_wall_height = water_bunker[left_wall]
            for right_wall in range(left_wall + 1, end_of_bunker):
                right_wall_height = water_bunker[right_wall]
                if right_wall_height >= left_wall_height or right_wall + 1 == end_of_bunker:
                    if right_wall + 1 == end_of_bunker:
                        left_wall_height, right_wall_height = right_wall_height, left_wall_height
                        end_of_bunker_reached = True
                    for inside_bunker in range(left_wall + 1, right_wall):
                        if not water_bunker[inside_bunker]:
                            water += left_wall_height
                        else:
                            water += left_wall_height - water_bunker[inside_bunker]
                    else:
                        if end_of_bunker_reached:
                            return water
                        left_wall_height = right_wall_height
                        left_wall = right_wall


water_list1 = [5, 0, 0, 2, 0, 0, 2, 0, 0, 5]
water_list2 = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
print(water_calculate(water_list1))
print(water_calculate(water_list2))
