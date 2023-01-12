class EmptyWaterTank(Exception):
    pass

def check_is_higher_wall_forward(left_wall_index, water_bunker):
    for check_is_higher_wall_index in range(left_wall_index + 1, len(water_bunker)):
        if water_bunker[check_is_higher_wall_index] >= water_bunker[left_wall_index]:
            return check_is_higher_wall_index
    else:
        return 0


def check_next_higher_wall(left_wall_index, water_bunker):
    next_high_wall_index = left_wall_index
    next_high_wall = 0
    for i in range(left_wall_index + 1, len(water_bunker)):
        if water_bunker[i] == 0 and i == len(water_bunker) - 1:
            next_high_wall_index = len(water_bunker) - 1
            next_high_wall = 0
        if water_bunker[i] > next_high_wall:
            next_high_wall = water_bunker[i]
            next_high_wall_index = i
    return next_high_wall_index


def water_calculate(water_bunker):
    try:
        if not water_bunker:
            raise EmptyWaterTank
        end_of_bunker = len(water_bunker)
        water = 0
        left_wall_index = 0
        left_wall_height = 0
        # find first reached wall and set to current left border
        for left_wall_index in range(end_of_bunker):
            if water_bunker[left_wall_index]:
                left_wall_height = water_bunker[left_wall_index]
                left_wall_index = left_wall_index
                break

        while left_wall_index < end_of_bunker - 1:
            # look forward for highest or equal wall and if there is, set it to current right border
            is_higher_wall_forward_index = check_is_higher_wall_forward(left_wall_index, water_bunker)
            if is_higher_wall_forward_index != 0:
                next_wall = is_higher_wall_forward_index
                lower_water_level = left_wall_height
            else:
                # look for next highest wall in list and set current right border
                next_wall = check_next_higher_wall(left_wall_index, water_bunker)
                lower_water_level = water_bunker[next_wall]
            # iterate between two walls
            for inside_bunker in range(left_wall_index + 1, next_wall):
                if not water_bunker[inside_bunker]:
                    water += lower_water_level
                else:
                    water += lower_water_level - water_bunker[inside_bunker]
            # set left wall  (next left border )
            if next_wall == end_of_bunker - 1:
                break
            left_wall_index = next_wall
            left_wall_height = water_bunker[next_wall]
        if water == 0:
            return "There is no water in water tank!!!"
        return f"Water available {water} liters!"

    except EmptyWaterTank:
        return "There is no water tank at all!!!"


water_list1 = [1, 5, 1]
water_list2 = []
water_list3 = [0, 100, 0, 0, 10, 1, 1, 10, 4, 1, 1, 1, 0, 1]
print(water_calculate(water_list1))
print(water_calculate(water_list2))
print(water_calculate(water_list3))
