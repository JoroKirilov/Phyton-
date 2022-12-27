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
    for index in range(row - 1, -1, -1):
        if ma[index][selected_column_idx] == 0:
            ma[index][selected_column_idx] = player_mark
            print_matrix(ma)
            return
    raise FullColumnError


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
        place_player_mark(matrix, player_choice, player)
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
