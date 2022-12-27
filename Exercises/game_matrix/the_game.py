# Place player marker on to spot
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

def check_is_winner(ma, row: int,col: int,current_player: int, need_to_win_num = 4):
    count = 0
    for step in range(need_to_win_num):
        if (col + step) > (len(ma[0]) - 1):
            break
        if ma[row][col+step] == player:
            count += 1
    if count == 4:
        print(f"Player {player} is win")
        return True
    else:
        count = 0
    for step in range(need_to_win_num):
        if (col + step) == -1:
            break
        if ma[row][col - step] == player:
            count += 1
    if count == 4:
        print(f"Player {player} is win")
        return True
    else:
        count = 0
    for step in range(need_to_win_num):
        if (col + step) > (len(ma[0] - 1)) or ((row + step) > (len(ma) + 1)):
            break
        if ma[row + step][col + step] == player:
            count += 1
    if count == 4:
        print(f"Player {player} is win")
        return True
    else:
        count = 0




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
