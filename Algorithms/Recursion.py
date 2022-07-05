def cal_fact(n):
    if n == 0:
        return 1
    return n * cal_fact(n - 1 )
n = int(input())

print(cal_fact(n))
