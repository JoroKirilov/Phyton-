from helper.mapper import operations


class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign


def read_players():
    first_player_name = input(f"Player one name: ").title()
    second_player_name = input(f"Player two name: ").title()

    while True:
        first_player_sign = input(f'{first_player_name} would you like to play with X or 0 ? ').upper()
        if first_player_sign == 'X' or first_player_sign == 'O':
            break
    second_player_sign = 'O' if first_player_sign == 'X' else 'X'
    return Player(first_player_name, first_player_sign), Player(second_player_name, second_player_sign)


def print_board_numeration():
    print('This is the numeration of the board')
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")


def print_board(matrix):
    print(f"| {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]} |")
    print(f"| {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]} |")
    print(f"| {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} |")


def is_valid_position(ma, pos):
    if pos < 1 or pos > 9:
        return False
    row, col = operations[pos]
    if ma[row][col] != ' ':
        return False
    return True


def mark_slot(ma, pos, sign):
    row, cow = operations[pos]
    ma[row][cow] = sign


def is_winner(ma, sign):
    # check rows
    for row in ma:
        if all([x == sign for x in row]):
            return True
    # check cols
    for col in range(len(ma)):
        is_win = True
        for row in range(len(ma)):
            if ma[row][col] != sign:
                is_win = False
                break
        if is_win:
            return True

    # check right diagonal
    is_win = True
    for index in range(len(ma)):
        if ma[index][index] != sign:
            is_win = False
            break
    if is_win:
        return True

    # check left diagonal
    is_win = True
    for index in range(len(ma)):
        if ma[(len(ma) - 1) - index][(len(ma) - 1) - index] != sign:
            is_win = False
    if is_win:
        return True


first_player, second_player = read_players()

print_board_numeration()

print(f'{first_player.name} starts first')

board = [[' ' for _ in range(3)] for _ in range(3)]

turn = 0

while True:
    current_player = first_player if turn % 2 == 0 else second_player
    print_board(board)
    position = int(input(f'{current_player.name} choose your position from 1-9.'))
    if not is_valid_position(board, position):
        continue
    mark_slot(board, position, current_player.sign)
    if is_winner(board, current_player.sign):
        print(f'{current_player.name} has won')
        print_board(board)
        break
    else:
        print('draw')
    turn += 1