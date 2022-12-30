class NotValidSign(Exception):
    pass


def player_one_choose_sign():
    while True:
        try:
            sign = input(r'Choose between \'X\' and \'O\'')
            if sign != 'X' and sign != 'x' and sign != 'O' and sign != 'o':
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


player_one = input('Player one name:')
player_two = input('Player two name:')
player_one_sign = player_one_choose_sign()
player_two_sign = player_two_give_sign(player_one_sign)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f'| {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]} |')
print(f'| {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]} |')
print(f'| {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} |')
