# food = input("What is your name:\n")
# print(f"{food}")
# is_good = "good" if food == "apple" else "no good"
# print(is_good)
import itertools
import math
import operator
from functools import reduce
from itertools import accumulate

n = 3
print(math.factorial(n))
result = accumulate(range(1, n + 1), operator.mul)
print(list(result)[-1])

result1 = 1
for i in range(1, n + 1):
    result1 = i * result1
print(result1)

result_factoriel = reduce(operator.mul, range(1, n + 1))
print(result_factoriel)

