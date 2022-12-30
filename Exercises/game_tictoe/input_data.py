
class NotValidSign(Exception):
    pass


def player_one_choose_sign():
    while True:
        try:
            sign = input(r'Choose between \'X\' and \'O\'')
            sign = sign.upper()
            if sign != 'X' and sign != 'O':
                raise NotValidSign
            break
        except NotValidSign:
            print('X or 0')
    return sign


def player_two_give_sign(player_one_sign: str):
    if player_one_sign == 'X':
        return 'O'
    else:
        return 'X'


def create_game_table():
    return [[' ' for _ in range(3)] for _ in range(3)]


def print_table(table):
    print(f'| {table[0][0]} | {table[0][1]} | {table[0][2]} |')
    print(f'| {table[1][0]} | {table[1][1]} | {table[1][2]} |')
    print(f'| {table[2][0]} | {table[2][1]} | {table[2][2]} |')


def is_win_horizontal_and_vertical(ma, sign):
    count = 0
    for i in range(3):
        for j in range(3):
            if ma[i][j] == sign:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
    for i in range(3):
        for j in range(3):
            if ma[j][i] == sign:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
    return False


def is_win_diagonal(ma, sign):
    count = 0
    for index in range(3):
        if ma[index][index] == sign:
            count += 1
            if count == 3:
                return True
        else:
            break
    count = 0
    for index in range(3):
        if ma[index][2-index] == sign:
            count += 1
            if count == 3:
                return True
        else:
            return False


def mark_slot(ma, slot, sign):
    if slot == 1:
        ma[0][0] = sign
    elif slot == 2:
        ma[0][1] = sign
    elif slot == 3:
        ma[0][2] = sign
    elif slot == 4:
        ma[1][0] = sign
    elif slot == 5:
        ma[1][1] = sign
    elif slot == 6:
        ma[1][2] = sign
    elif slot == 7:
        ma[2][0] = sign
    elif slot == 8:
        ma[2][1] = sign
    else:
        ma[2][2] = sign

players_info = {}

player_one = input('Player one name:')
player_two = input('Player two name:')
players_info[player_one] = player_one_choose_sign()
players_info[player_two] = player_two_give_sign(players_info[player_one])


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f'| {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]} |')
print(f'| {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]} |')
print(f'| {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} |')


game_table = create_game_table()
print()
print('Start game:')
print()
for idx in range(9):
    if idx % 2 == 0:
        player_on_turn = player_one
    else:
        player_on_turn = player_two
    print_table(game_table)
    choose_slot = int(input())
    mark_slot(game_table, choose_slot, players_info[player_on_turn])
    is_win = is_win_horizontal_and_vertical(game_table, players_info[player_on_turn])
    if is_win:
        print(f"{player_on_turn} win the game")
        break
    is_win = is_win_diagonal(game_table,players_info[player_on_turn])
    if is_win:
        print(f"{player_on_turn} win the game")
        break

print_table(game_table)