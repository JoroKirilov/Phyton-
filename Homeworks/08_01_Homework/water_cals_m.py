# 4*) Получавате лист с положителни числа. Всяко число представлява височината на дига. Представете си, че над дигите се излива вода. Трябва да изчислите точно колко вода се е задържала между дигите.
# примерен Input = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
# очакван изход = 48
# Обяснение:
# Всяка точка между дигите се брои за 1 вода. Няма нужда да правите такава графика.
# Целта й е да ви ориентира в условието. Трябва да се върне единствено количеството задържана вода.

from copy import deepcopy


def get_water(input: list):
    water = 0

    if len(input) <= 2:
        return water

    input_copy = deepcopy(input)

    # get the value of highest dike:
    max_dike = max(input_copy)
    if max_dike == 0:
        return water

    # find all indexes with max dike
    indexes_with_max_dike = [i for i, value in enumerate(input_copy) if value == max_dike]

    if len(indexes_with_max_dike) > 1:
        left_highest_dike_id = min(indexes_with_max_dike)
        right_highest_dike_id = max(indexes_with_max_dike)
        water += get_water_between_two_dikes(input, left_highest_dike_id, right_highest_dike_id)
        water += get_water(input_copy[:left_highest_dike_id + 1])
        water += get_water(input_copy[right_highest_dike_id::])
    else:
        input_copy[indexes_with_max_dike[0]] -= 1
        water += get_water(input_copy)

    return water


def get_water_between_two_dikes(input: list, left_dike_id: int, right_dike_id: int):
    water = 0
    for idx in range(left_dike_id + 1, right_dike_id):
        water += input[left_dike_id] - input[idx]

    return water


if __name__ == "__main__":
    input = [0, 5, 0, 5]
    print(get_water(input))