class InvalidChoice(Exception):
    pass


class FullColumnError(Exception):
    pass


def valid_choice(player_selected_column, max_cols_count):
    if not 0 <= player_selected_column <= max_cols_count:
        raise InvalidChoice


def create_matrix(row: int, col: int):
    # create matrix
    tmp_matrix = [[0 for _ in range(col)] for _ in range(row)]
    return tmp_matrix


def print_matrix(ma):
    # print matrix
    for element in ma:
        print(element)


def place_player_mark(ma, selected_column_idx, player_mark):
    row = len(ma)
    current_row = 0
    for row_index in range(row - 1, -1, -1):
        if ma[row_index][selected_column_idx] == 0:
            ma[row_index][selected_column_idx] = player_mark
            current_row = row_index
            print_matrix(ma)
            return row_index
    raise FullColumnError


def check_out_of_range(ma, row: int, col: int, current_player: int):
    try:
        if ma[row][col] == current_player:
            return True
    except IndexError:
        return False


def horizontal_check(ma, player_sign):
    count_to_win = 0
    for row in range(len(ma)):
        for col in range(len(ma[0])):
            if ma[row][col] == player_sign:
                count_to_win += 1
                if count_to_win == 4:
                    return True
            else:
                count_to_win = 0
        count_to_win = 0
    return False

def check_is_winner(ma, row: int, col: int, player: int, need_to_win_num=4):
    # count = 0
    # for step in range(need_to_win_num):
    #     if (col + step) > (len(ma[0]) - 1):
    #         break
    #     if ma[row][col+step] == current_player:
    #         count += 1
    # if count == 4:
    #     return True
    # else:
    #     count = 0
    is_win_horizontal = horizontal_check(ma, player)
    if is_win_horizontal:
        return True

    is_win_down = [check_out_of_range(ma, row + index, col, player) for index in range(need_to_win_num)]
    if all(is_win_down):
        return True
    # is_win_right = [check_out_of_range(ma, row, col + index, player) for index in range(need_to_win_num)]
    #
    # if all(is_win_right):
    #     return True
    # is_win_left = [check_out_of_range(ma, row, col - index, player) for index in range(need_to_win_num)]
    # if all(is_win_left):
    #     return True

    is_win_left_diagonal = [check_out_of_range(ma, row + index, col - index, player) for index in
                            range(need_to_win_num)]
    if all(is_win_left_diagonal):
        return True

    is_win_right_diagonal = [check_out_of_range(ma, row + index, col + index, player) for index in
                             range(need_to_win_num)]
    if all(is_win_right_diagonal):
        return True


rows_count = 6
cols_count = 7

matrix = create_matrix(rows_count, cols_count)
print_matrix(matrix)

player = 1
while True:
    player = 2 if player % 2 == 0 else 1
    try:
        player_choice = int(input(f"Player {player} choice:")) - 1
        valid_choice(player_choice, cols_count - 1)
        row_index = place_player_mark(matrix, player_choice, player)
        game_status = check_is_winner(matrix, row_index, player_choice, player)
        if game_status:
            print(f"Player {player} is win")
            break
    except InvalidChoice:
        print("Please enter valid choice")
        continue
    except ValueError:
        print("Please enter only digits!")
        continue
    except FullColumnError:
        print("Choose another column. This is full!")
        continue
    player += 1
