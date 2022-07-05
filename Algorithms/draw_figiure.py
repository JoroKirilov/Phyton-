def draw_figiure(n):
    if n == 0:
        return
    print('*' * n)
    draw_figiure(n - 1)
    print('*' * n)

n = int(input())
draw_figiure(n)