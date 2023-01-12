def check_is_higher_wall_forward(left_wall_index, water_bunker):
    for check_is_higher_wall_index in range(left_wall_index + 1, len(water_bunker)):
        if water_bunker[check_is_higher_wall_index] > water_bunker[left_wall_index]:
            return check_is_higher_wall_index
    else:
        return 0


def water_calculate(water_bunker):
    end_of_bunker = len(water_bunker)
    water = 0
    end_of_bunker_reached = False
    left_wall_index = 0
    left_wall_height = 0
    is_higher_wall_forward = False
    # searching first wall height and index that can stop water and set it like left wall
    for left_wall_index in range(end_of_bunker):
        if water_bunker[left_wall_index]:
            left_wall_height = water_bunker[left_wall_index]
            break
    # searching next wall height and index that can stop water and set it like right wall
    # for right_wall_index in range(left_wall_index + 1, end_of_bunker):
    while left_wall_index != end_of_bunker_reached:
        is_higher_wall_forward_index = check_is_higher_wall_forward(left_wall_index, water_bunker)
        if is_higher_wall_forward_index != 0:
            higher_water_level = water_bunker[is_higher_wall_forward_index]
            lower_water_level = left_wall_height
            # iterate between walls and add water with max capacity of lower level
            for inside_bunker in range(left_wall_index + 1, is_higher_wall_forward_index):
                if not water_bunker[inside_bunker]:
                    water += lower_water_level
                else:
                    water += lower_water_level - water_bunker[inside_bunker]
            left_wall_index = is_higher_wall_forward_index
            left_wall_height = higher_water_level
        else:
            next_lower_wall = 0
            lower_water_level = 0
            for next_lower_wall in range(left_wall_index + 1, end_of_bunker):
                if water_bunker[next_lower_wall] and water_bunker[next_lower_wall] != left_wall_height:
                    lower_water_level = water_bunker[next_lower_wall]
                    break
            for inside_bunker in range(left_wall_index + 1, next_lower_wall):
                water += lower_water_level
            left_wall_index = next_lower_wall
            left_wall_height = lower_water_level
        right_wall_index = left_wall_index

    return water


water_list1 = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
water_list2 = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
# water_list4 = [0, 100, 0, 0, 10, 1, 1, 10, 1, 0, 1, 1, 0, 0]
print(water_calculate(water_list1))
print(water_calculate(water_list2))
# print(water_calculate(water_list3))
