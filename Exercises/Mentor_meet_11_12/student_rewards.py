# примерен вход: [8, 4, 2, 1, 3, 6, 7, 9, 5]
# примерен изход: [4, 3, 2, 1, 2, 3, 4, 5, 1]

# 8 < 4  |   8 4 2      4 2 1    2 1 3    1 3 6    3 6 7   6 7 9   7 9 5   |  5 < 9


def give_rewards(student_score):
    starting_index = 0

    rewards_list = [1 for elements in range(len(student_score))]
    for index in range(len(student_score)):
        if student_score[index] == 1:
            rewards_list[index] = 1
            starting_index = index
            break

    for right in range(starting_index, 0, -1):
        left = right - 1
        if student_score[left] > student_score[right]:
            rewards_list[left] = rewards_list[right] + 1

    for left in range(starting_index, len(student_score) - 1):
        right = left + 1
        if student_score[left] < student_score[right]:
            rewards_list[right] = rewards_list[left] + 1

    return rewards_list


score = [8, 4, 2, 1, 3, 6, 7, 9, 5]
give_rewards(score)
print(give_rewards(score))
