def integers():
    for i in range(1, 9):
        yield i


chain = integers()
print(list(chain))


def squared(seq):
    for i in seq:
        yield i ** 2


chain = squared(integers())
print(list(chain))


def negated(seq):
    for i in seq:
        yield -i


chain = negated(squared(integers()))
print(list(chain))


