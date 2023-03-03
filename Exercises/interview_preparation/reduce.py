import itertools
from functools import reduce


class Calculator:
    @staticmethod
    def add(*args):
        return reduce(lambda x, y: x + y, args)


print(Calculator.add(*[el for el in range(0, 11)]))


list1 = itertools.accumulate([el for el in range(0, 11)], lambda x, y: x + 100)
print(list(list1))