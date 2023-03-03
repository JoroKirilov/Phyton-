# def gen_square(n):
#     num = 0
#     previous = 1
#     last = 0
#
#     while num <= n - 2:
#         if num == 0:
#             yield 0
#         elif num == 1:
#             yield 1
#         yield last + previous
#         num += 1
#         tmp = previous
#         previous = last + previous
#         last = tmp
#
# print(list(gen_square(10)))
from urllib3.connectionpool import xrange

n = 10
a = 0
b = 1
for i in xrange(0, n + 1):
    print(a)
    a, b = b, a + b


