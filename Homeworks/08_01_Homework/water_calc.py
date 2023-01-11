def water_calculate(water_bunker):
    end_of_bunker = len(water_bunker)
    water = 0
    end_of_bunker_reached = False
    left_wall = 0
    left_wall_height = 0
    # searching first wall height and index that can stop water and set it like left wall
    for left_wall_index in range(end_of_bunker):
        if water_bunker[left_wall]:
            left_wall = left_wall_index
            left_wall_height = water_bunker[left_wall]
            break
    # searching next wall height and index that can stop water and set it like right wall
    for right_wall in range(left_wall + 1, end_of_bunker):
        if water_bunker[right_wall] >= left_wall_height or right_wall + 1 == end_of_bunker:
            right_wall_height = water_bunker[right_wall]
            lower_level, higher_level = left_wall_height, right_wall_height
            # check if we reach end of bunker
            if right_wall + 1 == end_of_bunker:
                end_of_bunker_reached = True
                # check if end of bunker is lower than left wall and in this case switch levels
                if left_wall_height > right_wall_height:
                    lower_level, higher_level = right_wall_height, left_wall_height
            # iterate between walls and add water with max capacity of lower level
            for inside_bunker in range(left_wall + 1, right_wall):
                if not water_bunker[inside_bunker]:
                    water += lower_level
                else:
                    water += lower_level - water_bunker[inside_bunker]
            else:
                if end_of_bunker_reached:
                    return water
                left_wall_height = right_wall_height
                left_wall = right_wall


water_list1 = [5, 0, 0, 2, 0, 0, 2, 0, 0, 5]
water_list2 = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
water_list3 = [0, 0, 4, 0, 0]
print(water_calculate(water_list1))
print(water_calculate(water_list2))
print(water_calculate(water_list3))
