from itertools import tee


def integers():
    for i in range(1, 9):
        yield i


chain = integers()

# print(len(chain)) generator has no method len
# for x in chain:
#     print(x)
# for x in chain:   # second time don't print, because the generator is exucite one time only
#     print(x)      # there is no data anymore

a, b = tee(range(5))  # duplicate iterator object
for i in a:            # make to generators to use
    print(i)
for i in b:
    print(i)


# def squared(seq):
#     for i in seq:
#         yield i ** 2
#
#
# chain = squared(integers())
# print(list(chain))
#
#
# def negated(seq):
#     for i in seq:
#         yield -i
#
#
# chain = negated(squared(integers()))
# print(list(chain))
#
# integer = range(8)
# squared = (i*i for i in range(8))
# print(integer)
# for i in squared:
#     print(i)